# -*- coding: utf-8 -*-
"""
aplicar_verificacion_fhc.py — Campaña de verificación, Fernando Henrique Cardoso
(Brasil, ventana 2000-2003, 2do mandato), investigación 2026-07-21. Idempotente.

CLAVE DE MATCH: Trip_ID (dentro de brasil_viajes.csv, estable en este módulo;
el Trip_ID del módulo NO es el mismo que en la base consolidada).

Fuente usada: pt.wikipedia.org "Lista de viagens presidenciais de Fernando Henrique
Cardoso" (misma fuente y misma confiabilidad ya aplicada al tramo Francia de este
Journey_ID, Trip_ID 16, ver Source_Verification de esa fila). Se verificó por fetch
directo que la página es real, accesible y que sus notas de pie citan fuentes
primarias/periodísticas con fechas exactas que coinciden con las 3 filas cargadas:
  - Portugal (Trip_ID 1): MRE "Programa da Visita a Portugal do Presidente Fernando
    Henrique Cardoso" (03/03/2000, nota oficial); Folha "FHC usará avião fretado
    para viagem a Portugal" (09/02/2000) y Diário do Grande ABC "FHC define comitiva
    para viagens a Portugal e Chile" (03/03/2000).
  - Venezuela (Trip_ID 3): MRE "Visita do Presidente Fernando Henrique Cardoso à
    Venezuela" (31/03/2000, nota oficial post-visita); Folha "FHC busca aproximação
    entre América Central e Mercosul" (04/04/2000).
  - Espanha/Madrid (Trip_ID 15): O Estado de S. Paulo "FHC em viagem a Espanha e
    França" (25/10/2001) — fecha exacta coincidente con el inicio del tramo.

Intentos de acceder directamente a fuentes gold-standard (biblioteca.presidencia.gov.br,
gov.br/mre, web.archive.org, estadao.com.br, folha.uol.com.br) fueron bloqueados por
la política de red del entorno de investigación (captcha en gov.br, 403 blocklist en
web.archive.org/estadao/folha) o devolvieron contenido vacío (biblioteca.presidencia.gov.br,
posible renderizado JS). Se documenta para no repetir el intento sin cambiar de entorno.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, region_for

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")

WIKI_URL = "https://pt.wikipedia.org/wiki/Lista_de_viagens_presidenciais_de_Fernando_Henrique_Cardoso"

# Trip_ID -> (url, reliability, nota)
VERIF = {
    "1": (
        WIKI_URL, "Medium",
        "NOTA 2026-07-21: confirmado por lista verificada (pt.wikipedia.org, "
        "Lista de viagens presidenciais de Fernando Henrique Cardoso), que cita "
        "nota oficial do MRE 'Programa da Visita a Portugal do Presidente Fernando "
        "Henrique Cardoso' (03/03/2000) y notas de prensa Folha de S.Paulo 'FHC "
        "usará avião fretado para viagem a Portugal' (09/02/2000) y Diário do "
        "Grande ABC 'FHC define comitiva para viagens a Portugal e Chile' "
        "(03/03/2000). Fechas (07-08/03/2000) y ciudad (Lisboa) consistentes con "
        "lo cargado."
    ),
    "3": (
        WIKI_URL, "Medium",
        "NOTA 2026-07-21: confirmado por lista verificada (pt.wikipedia.org, "
        "Lista de viagens presidenciais de Fernando Henrique Cardoso), que cita "
        "nota oficial del MRE 'Visita do Presidente Fernando Henrique Cardoso à "
        "Venezuela' (31/03/2000) y Folha de S.Paulo 'FHC busca aproximação entre "
        "América Central e Mercosul' (04/04/2000, post-visita). Fecha (29-30/03/2000) "
        "y ciudad (Caracas) consistentes con lo cargado."
    ),
    "15": (
        WIKI_URL, "Medium",
        "NOTA 2026-07-21: confirmado por lista verificada (pt.wikipedia.org, "
        "Lista de viagens presidenciais de Fernando Henrique Cardoso), que cita "
        "O Estado de S. Paulo 'FHC em viagem a Espanha e França' (25/10/2001), "
        "fecha exacta coincidente con el inicio del tramo España. Mismo criterio "
        "de fuente ya usado para el tramo Francia (Trip_ID 16) de este mismo "
        "Journey_ID (BRA-FHC-J016)."
    ),
}

ALL_IDS = set(VERIF.keys())


def append_note(existing, nota):
    if existing in ("NA", "", None):
        return nota
    if nota[:40] in existing:
        return existing
    return existing.rstrip(".") + ". " + nota


def process():
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    n_verif = 0
    for r in rows:
        tid = r["Trip_ID"]
        if tid not in ALL_IDS:
            continue
        if r["President"] != "Fernando Henrique Cardoso":
            continue
        url, rel, nota = VERIF[tid]
        r["Source_Verification"] = url
        r["Source_Reliability"] = rel
        r["Verificacion_Status"] = "Verificada-URL"
        r["Methodological_Notes"] = append_note(r["Methodological_Notes"], nota)
        n_verif += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"brasil (Fernando Henrique Cardoso): filas verificadas={n_verif}")


if __name__ == "__main__":
    process()
