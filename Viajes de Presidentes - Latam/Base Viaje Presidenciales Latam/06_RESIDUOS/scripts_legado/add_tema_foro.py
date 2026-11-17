# -*- coding: utf-8 -*-
"""
add_tema_foro.py — Migración de esquema 19 -> 20 columnas (agrega Tema_Foro)
y saneamiento de celdas vacías (auditoría 2026-07-06).

Qué hace, en orden:
  1) Celdas genuinamente vacías -> "NA" declarado (regla: sin celdas vacías).
     - End_Date / Duration_Days vacíos: los 12 casos son viajes Canceled (verificado);
       "NA" es el valor metodológicamente correcto.
     - Sideline_Bilaterals vacíos (331): "NA" por decisión del 2026-07-06
       (verificación de bilaterales al margen DIFERIDA; ver PENDIENTES_VERIFICACION).
     - Methodological_Notes vacías (154): "NA".
  2) Agrega la columna Tema_Foro (posición 20):
     - Visit_Category != Multilateral -> "NA".
     - Visit_Category == Multilateral -> clasificación por (a) tabla de match exacto
       (eventos verificados por investigación 2026-07-06) y (b) reglas por patrón
       (keywords, doctrina del "mandato fundacional"; ver CODEBOOK 5.7).
  3) Reporta todo evento multilateral que no matchee (para revisión manual).

Uso:
    python add_tema_foro.py <csv1> [<csv2> ...]
Sobrescribe los CSV en el lugar (hacer backup antes si se desea).
"""
import csv, sys, os, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, MISSING

# ──────────────────────────────────────────────────────────────────────────
# A) TABLA DE MATCH EXACTO (investigación 2026-07-06, confianza Alta/Media)
#    Clave = texto EXACTO de Counterpart_Event.
# ──────────────────────────────────────────────────────────────────────────
CPG = "Cooperación Política General"
COM = "Comercio/Integración Económica"
AMB = "Medio Ambiente/Clima"
SEG = "Seguridad"
OTR = "Otro"

EXACT = {
    "44ª Cumbre del G7 (invitado)": CPG,
    "50º aniversário da União Africana": CPG,
    "56ª Asamblea General de la ONU (debate post-11S)": CPG,
    "59ª AGNU + Cúpula da Ação contra a Fome e a Pobreza": CPG,
    "64ª AGNU + Cúpula do G20 de Pittsburgh": CPG,
    "68ª AGNU (discurso contra a espionagem da NSA)": CPG,
    "70ª AGNU + Cúpula da Agenda 2030": CPG,
    "78ª AGNU (+ Biden, Lançamento parceria trabalhista)": CPG,
    "80ª AGNU (+ encontro breve com Trump)": CPG,
    "Assinatura do Acordo de Paris (ONU)": AMB,
    "Conferencia Internacional sobre Financiación para el Desarrollo (Consenso de Monterrey)": COM,
    "Conferência da OIT (Pacto Mundial pelo Emprego)": OTR,   # laboral/empleo; sin categoría propia
    "Conferência da ONU sobre Financiamento para o Desenvolvimento": COM,
    "Coroação de Carlos III": CPG,
    "Cumbre APEC / COP25": COM,          # primario APEC; secundario COP25 (nota en fila)
    "Cumbre Extraordinaria de las Américas": CPG,
    "Cumbre G77+China (50° aniversario)": CPG,
    "Cumbre Mundial 2005 / 60ª Asamblea General ONU": CPG,
    "Cumbre Progresista (Bachelet; Biden)": CPG,
    "Cumbre de Gobiernos Progresistas (Tony Blair)": CPG,
    "Cumbre de Líderes de la Tercera Vía (Gerhard Schröder)": CPG,
    "Cumbre de Seguridad Nuclear (Obama)": SEG,
    "Cumbre de la Amazonía (OTCA)": AMB,
    "Cumbre de presidentes sudamericanos": CPG,   # I Reunión de Pdtes. de América del Sur, Brasilia 2000
}

# ──────────────────────────────────────────────────────────────────────────
# B) REGLAS POR PATRÓN (keywords, en orden de prioridad; case/acentos-insensible)
#    Doctrina: agenda amplia -> CPG; mandato fundacional económico -> COM.
#    El PRIMER patrón que matchee gana (por eso lo específico va antes que lo genérico).
# ──────────────────────────────────────────────────────────────────────────
def _norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower()

PATTERNS = [
    # Medio Ambiente/Clima
    (["cop1", "cop2", "cop3", "conferencia del clima", "conferencia do clima",
      "cambio climatico", "mudanca do clima", "accion climatica", "acao climatica",
      "ambicion climatica", "rio+20", "rio +20", "desarrollo sostenible",
      "desenvolvimento sustentavel", "acuerdo de paris", "acordo de paris",
      "amazonia", "otca", "cumbre de la tierra"], AMB),
    # Seguridad (incluye cumbres de paz sobre conflictos armados; decision 2026-07-07)
    (["seguridad nuclear", "seguranca nuclear", "cumbre de seguridad",
      "conferencia de seguridad", "defensa", "cumbre por la paz", "cupula pela paz",
      "paz en ucrania"], SEG),
    # Comercio / Integración Económica (mandato fundacional económico)
    (["mercosur", "mercosul", "apec", "davos", "foro economico mundial",
      "forum economico mundial", "foro de boao", "boao", "omc", "aladi",
      "financiacion para el desarrollo", "financiamento para o desenvolvimento",
      "consenso de monterrey", "foro empresarial", "forum empresarial",
      "foro de negocios", "forum de negocios", "foro de inversion",
      "aspa", "america do sul-paises arabes", "america del sur-paises arabes",
      "america do sul-africa", "america del sur-africa", "africa-america do sul",
      "ibas", "ibsa", "prosur",
      # Bloques/foros de mandato fundacional económico-comercial (doctrina CODEBOOK 5.7):
      "alianza del pacifico", "alianca do pacifico",     # bloque de integración comercial
      "apep", "prosperidad economica de las americas",   # APEP (mandato fundacional económico)
      "caricom",                                          # Comunidad y Mercado Común del Caribe
      "cedeao", "ecowas",                                 # Comunidad Económica de Estados de África Occidental
      "franja y la ruta", "franja e rota", "obor", "belt and road",  # infraestructura/comercio
      "global compact",                                   # foro empresarial ONU (+inversores)
      "milken",                                           # foro economico privado (analogo Davos)
      "pacto financeiro global", "pacto financiero global",  # arquitectura financiera (París 2023)
      "seminario de investimentos", "seminario de inversiones", "seminario de inversion"], COM),
    # Salud
    (["salud global", "saude global", "oms", "pandemia", "cumbre de vacunas"], "Salud"),
    # Energía
    (["cumbre energetica", "energia"], "Energía"),
    # Derechos Humanos (incluye foros de memoria del Holocausto)
    (["derechos humanos", "direitos humanos", "contra el racismo",
      "contra la discriminacion", "holocausto", "holocaust"], "Derechos Humanos"),
    # Trabajo / empleo -> Otro (sin categoría propia; documentado en CODEBOOK 5.7)
    (["oit", "pacto mundial pelo emprego", "pacto mundial por el empleo"], OTR),
    # Cooperación Política General (agenda amplia + protocolo de Estado)
    (["agnu", "asamblea general de la onu", "assembleia geral da onu",
      "g20", "g7", "g8", "brics", "bric", "celac", "unasur", "unasul", "alba",
      "grupo de rio", "grupo do rio", "g-15", "g15",
      "cumbre iberoamericana", "cupula iberoamericana", "ibero-americana",
      "cumbre de las americas", "cupula das americas", "das americas", "de las americas",
      "asean", "cplp",                                   # organismos regionales de agenda amplia
      "uniao europeia", "union europea", "ue-america", "alc-ue", "ue-alc",  # cumbres birregionales UE-ALC
      "integracion y desarrollo", "calc",                # CALC, precursora de CELAC
      "unidad de america latina",                        # Cumbre de la Unidad (Cancún 2010), precursora de CELAC
      "misa inaugural", "missa inaugural",               # ceremonias papales
      "dia d",                                           # aniversarios/conmemoraciones de Estado
      "trilateral", "cumbre regional",                   # reuniones político-regionales ad hoc
      "cumbre del milenio", "cupula do milenio", "g77",
      "ue-alc", "celac-ue", "ue-celac", "america latina-uniao europeia",
      "union europea-america latina", "alc-ue",
      "asuncion de", "asuncion presidencial", "toma de posesion", "posse de",
      "investidura", "funeral", "exequias", "coronacion", "coroacao",
      "cumbre de los pueblos", "foro de sao paulo", "foro de san pablo",
      "progresista", "tercera via", "terceira via", "en defensa de la democracia",
      "cpac", "europa viva",                             # foros ideologicos de derecha (doctrina 2026-07-07)
      "hambre", "fome", "pobreza", "uniao africana", "union africana",
      "cumbre mundial", "cupula mundial", "onu", "naciones unidas", "nacoes unidas",
      "presidentes sudamericanos", "presidentes de america del sur",
      "sudamericana", "sul-americana", "oea"], CPG),
]

def classify(event: str):
    """Devuelve (tema, metodo) o (None, None) si no matchea."""
    if event in EXACT:
        return EXACT[event], "exacto"
    ev = _norm(event)
    for keys, tema in PATTERNS:
        for k in keys:
            if k in ev:
                return tema, f"patron:{k}"
    return None, None


def process(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fixed_empty, classified, unmatched = 0, 0, []

    for row in rows:
        # 1) celdas vacías -> NA
        for col in list(row.keys()):
            if row[col] is None or str(row[col]).strip() == "":
                row[col] = MISSING
                fixed_empty += 1
        # 2) Tema_Foro
        if row.get("Tema_Foro") in (None, "", MISSING):
            if row["Visit_Category"] != "Multilateral":
                row["Tema_Foro"] = MISSING
            else:
                tema, met = classify(row["Counterpart_Event"])
                if tema is None:
                    row["Tema_Foro"] = MISSING  # queda marcado por validate.py
                    unmatched.append(row["Counterpart_Event"])
                else:
                    row["Tema_Foro"] = tema
                    classified += 1

    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for row in rows:
            w.writerow({c: row.get(c, MISSING) for c in COLUMNS})

    print(f"{os.path.basename(path)}: {len(rows)} filas | "
          f"celdas vacías->NA: {fixed_empty} | multilaterales clasificados: {classified} | "
          f"sin match: {len(unmatched)}")
    for u in sorted(set(unmatched)):
        print(f"   SIN MATCH -> {u}")
    return unmatched


if __name__ == "__main__":
    pend = []
    for p in sys.argv[1:]:
        pend += process(p)
    sys.exit(0 if not pend else 1)
