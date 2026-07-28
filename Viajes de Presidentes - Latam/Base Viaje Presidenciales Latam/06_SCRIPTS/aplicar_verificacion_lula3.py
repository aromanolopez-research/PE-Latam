# -*- coding: utf-8 -*-
"""
aplicar_verificacion_lula3.py — Campaña de verificación, tanda Lula 3er mandato
(Brasil, 2023-2025), investigación 2026-07-20. Idempotente.

CLAVE DE MATCH: Trip_ID (dentro de brasil_viajes.csv, estable en este módulo;
el Trip_ID del módulo NO es el mismo que en la base consolidada).

Aplica:
  1) URL real + Source_Reliability + Verificacion_Status = "Verificada-URL"
     para las 36 filas de la tanda Lula-3 (Trip_ID 235-263, 265-271).
  2) Correcciones de fecha donde la fuente oficial difiere del dato cargado
     (9 correcciones), con nota en Methodological_Notes.
  3) Corrección estructural del Trip_ID 258 (Cúpula del Mercosur): el dato
     original ubicaba el evento multilateral en Santa Cruz de la Sierra,
     Bolivia; fuentes oficiales (Planalto, Agência Brasil) confirman que la
     64a Cúpula del Mercosur ocurrió en Asunción, Paraguay (8/7/2024), y que
     Lula viajó luego a Santa Cruz de la Sierra (9/7/2024) para una VISITA
     BILATERAL SEPARADA con Luis Arce -- tramo no representado como fila
     propia en la base. Se corrige país/ciudad/fecha de esta fila al evento
     multilateral (Asunción) y se deja nota para que el usuario decida si
     agrega una fila nueva para el tramo bilateral a Bolivia.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, region_for

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")

# Trip_ID -> (url, reliability)
VERIF = {
    "235": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/visita-oficial-do-presidente-luiz-inacio-lula-da-silva-a-argentina-2013-buenos-aires-23-e-24-de-janeiro-de-2023", "High"),
    "236": ("https://www.gov.br/mre/pt-br/embaixada-montevideu/noticias/visita-del-presidente-lula-a-uruguay-fortalecer-los-lazos-con-el-pais-vecino-25-01-2023-1", "High"),
    "237": ("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos-e-pronunciamentos/2023/pronunciamento-na-chegada-a-casa-branca", "High"),
    "238": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/declaracao-conjunta-entre-a-republica-federativa-do-brasil-e-a-republica-popular-da-china-sobre-o-aprofundamento-da-parceria-estrategica-global-pequim-14-de-abril-de-2023", "High"),
    "239": ("https://www.em.com.br/app/noticia/politica/2023/04/15/interna_politica,1481771/lula-chega-a-abu-dhabi-para-encontro-com-presidente-dos-emirados-arabes.shtml", "Medium"),
    "240": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/lista-e-integra-dos-atos-assinados-no-centro-cultural-de-belem-em-22-de-abril-de-2023-por-ocasiao-da-visita-do-presidente-luiz-inacio-lula-da-silva-a-portugal", "High"),
    "241": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/visita-do-presidente-luiz-inacio-lula-da-silva-a-madri-2013-25-e-26-de-abril-de-2023-2013-credenciamento-de-imprensa", "High"),
    "242": ("https://agenciabrasil.ebc.com.br/politica/noticia/2023-05/lula-chega-londres-para-coroacao-do-rei-charles-iii", "High"),
    "243": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/cupula-do-g7-2013-hiroshima-19-a-21-de-maio-2013-credenciamento-de-imprensa", "High"),
    "244": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/visita-do-presidente-lula-a-italia-e-ao-vaticano-20-a-22-de-junho-de-2023", "High"),
    "245": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/visita-a-franca-do-presidente-lula-a-paris-22-e-23-de-junho-de-202", "High"),
    "246": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/participacao-do-presidente-lula-na-iii-cupula-celac-ue-2013-bruxelas-17-e-18-de-julho-de-2023", "High"),
    "247": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/cupula-dos-brics-2023-2013-joanesburgo-22-a-24-de-agosto-de-2023-2013-credenciamento-de-imprensa", "High"),
    "248": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/cupula-de-lideres-do-g20-2013-nova-delhi-9-e-10-de-setembro-de-2023-2013-reiteracao-de-prazo-de-credenciamento", "High"),
    "249": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/visita-do-presidente-luiz-inacio-lula-da-silva-a-cuba-por-ocasiao-da-cupula-do-g-77-china-2013-havana-15-e-16-de-setembro-de-2023", "High"),
    "250": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/participacao-do-presidente-lula-na-78a-sessao-da-assembleia-geral-das-nacoes-unidas-2013-nova-york-18-a-21-de-setembro-de-2023", "High"),
    "251": ("https://agenciagov.ebc.com.br/noticias/202311/presidente-lula-chega-a-arabia-saudita-em-busca-de-investimentos-para-o-brasil", "High"),
    "252": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/viagem-do-presidente-luiz-inacio-lula-da-silva-a-dubai-por-ocasiao-da-cop28-30-de-novembro-a-3-de-dezembro-de-2023-2013-credenciamento-de-imprensa", "High"),
    "253": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/ii-reuniao-de-consultas-intergovernamentais-de-alto-nivel-brasil-alemanha-2013-berlim-4-de-dezembro-de-2023", "High"),
    "254": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-assinados-por-ocasiao-da-visita-do-presidente-luiz-inacio-lula-da-silva-ao-egito-15-de-janeiro-de-2024/", "High"),
    "255": ("https://www.correiobraziliense.com.br/politica/2024/02/6803363-lula-embarca-para-a-etiopia-e-participa-de-reuniao-com-uniao-africana.html", "Medium"),
    "256": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/viagem-do-presidente-lula-a-georgetown-por-ocasiao-da-46a-cupula-do-mercado-comum-e-comunidade-no-caribe-2013-caricom-2013-28-de-fevereiro-credenciamento", "High"),
    "257": ("https://agenciagov.ebc.com.br/noticias/202402/viii-cupula-da-comunidade-de-estados-latino-americanos-e-caribenhos-celac-2013-kingstown-1o-de-marco-de-2024", "High"),
    "258": ("https://www.gov.br/planalto/en/latest-news/2024/07/lula-to-attend-64th-mercosur-summit-in-paraguay-make-official-visit-to-bolivia", "High"),
    "259": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/viagem-do-presidente-luiz-inacio-lula-da-silva-a-santiago-chile-5-e-6-de-agosto-de-2024-credenciamento-de-imprensa", "High"),
    "260": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/participacao-do-presidente-lula-na-79a-sessao-da-assembleia-geral-das-nacoes-unidas-2013-nova-york-22-a-25-de-setembro-2013-credenciamento-de-imprensa", "High"),
    "261": ("https://agenciabrasil.ebc.com.br/internacional/noticia/2024-10/lula-cancela-ida-ao-brics-na-russia-apos-acidente-domestico", "High"),
    "262": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/participacao-do-presidente-luiz-inacio-lula-da-silva-na-cerimonia-de-posse-do-presidente-eleito-do-uruguai-yamandu-orsi", "High"),
    "263": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-adotados-por-ocasiao-da-visita-do-presidente-luiz-inacio-lula-da-silva-ao-japao-toquio-de-25-a-27-de-marco-de-2025", "High"),
    "265": ("https://www.gov.br/planalto/en/latest-news/2025/04/president-lula-attends-celac-summit-in-honduras-strengthening-regional-integration", "High"),
    "266": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/viagem-do-presidente-luiz-inacio-lula-da-silva-a-moscou-russia-08-a-10-de-maio-de-2025-medicamentos-ilegais-na-russia-e-risco-de-prisao", "High"),
    "267": ("https://agenciagov.ebc.com.br/noticias/202505/201co-apoio-chines-e-decisivo-para-tirar-do-papel-rodovias-ferrovias-portos-e-linhas-de-transmissao201d-diz-lula-em-pequim", "High"),
    "268": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-adotados-por-ocasiao-da-visita-de-estado-do-presidente-luiz-inacio-lula-da-silva-a-franca-paris-5-e-6-de-junho-de-2025", "High"),
    "269": ("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2025/09/lula-tem-serie-de-eventos-estrategicos-durante-a-80a-assembleia-geral-da-onu", "High"),
    "270": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-celebrados-por-ocasiao-da-visita-de-estado-do-presidente-luiz-inacio-lula-da-silva-a-kuala-lumpur-malasia-24-a-28-de-outubro-de-2025", "High"),
    "271": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/aviso-as-redacoes/iv-cupula-celac-ue-santa-marta-colombia-9-e-10-de-novembro-2013-credenciamento-de-imprensa", "High"),
}

# Trip_ID -> dict de correcciones de fecha/duracion (y nota)
DATE_FIX = {
    "240": dict(End_Date="2023-04-25", Duration_Days="4",
                nota="CORRECCION 2026-07-20: End_Date 2023-04-24 -> 2023-04-25. La visita de "
                     "Estado a Portugal fue 22-25/04/2023 (Presidencia de Portugal + MRE), no 22-24."),
    "250": dict(End_Date="2023-09-21", Duration_Days="4",
                nota="CORRECCION 2026-07-20: End_Date 2023-09-20 -> 2023-09-21, segun aviso "
                     "oficial MRE 'Participacao do Presidente Lula na 78a AGNU - Nova York, "
                     "18 a 21 de setembro de 2023'."),
    "251": dict(Start_Date="2023-11-28", End_Date="2023-11-29", Duration_Days="2",
                nota="CORRECCION 2026-07-20: fechas originales (21-23/11/2023) eran erroneas. "
                     "Fuentes oficiales (Agencia Gov) confirman llegada a Riad el martes 28/11/2023 "
                     "y agenda empresarial el miercoles 29/11/2023, previo a Doha y Dubai (COP28)."),
    "253": dict(Start_Date="2023-12-03", End_Date="2023-12-04", Duration_Days="2",
                nota="CORRECCION 2026-07-20: Start_Date 2023-12-04 -> 2023-12-03. MRE confirma "
                     "llegada a Berlin el domingo 3/12 y la II Reuniao de Consultas Intergovernamentais "
                     "el 4/12/2023."),
    "266": dict(Start_Date="2025-05-08", Duration_Days="3",
                nota="CORRECCION 2026-07-20: Start_Date 2025-05-09 -> 2025-05-08, segun aviso "
                     "oficial MRE 'Viagem...a Moscou, Russia (08 a 10 de maio de 2025)'."),
    "270": dict(Start_Date="2025-10-25", Duration_Days="3",
                nota="CORRECCION 2026-07-20: Start_Date 2025-10-26 -> 2025-10-25. MRE confirma "
                     "recepcion oficial y bilateral con PM Anwar Ibrahim el 25/10 en Putrajaya, "
                     "previo a la Cupula ASEAN (26-28/10) y conferencia de cierre el 27/10/2025."),
    "271": dict(End_Date="2025-11-09", Duration_Days="1",
                nota="CORRECCION 2026-07-20: End_Date 2025-11-10 -> 2025-11-09. Lula participo "
                     "solo del primer dia de la IV Cupula CELAC-UE en Santa Marta (9/11) y retorno "
                     "el mismo dia a Belem para la apertura de la COP30 (fuentes: Agencia Brasil, "
                     "Diario do Grande ABC)."),
    "248": dict(nota="NOTA 2026-07-20: la Cupula de Lideres del G20 en si fue el 9-10/09/2023; "
                     "el rango cargado (8-11/09) incluye dias de viaje/traslado, consistente con "
                     "el aviso MRE de credenciamiento."),
    "261": dict(nota="NOTA 2026-07-20: la caida domestica de Lula (corte occipital, 5 puntos) fue "
                     "el sabado 19/10/2024; participo por videoconferencia en la sesion plenaria del "
                     "BRICS Kazan el miercoles 23/10/2024 (fuentes: Agencia Brasil, Planalto)."),
}

# Correccion estructural fila 258: evento multilateral (Cupula Mercosur) estaba
# mal ubicado en Bolivia/Santa Cruz de la Sierra; en realidad fue en Paraguay/Asuncion.
FIX_258 = dict(
    Destination_Country="Paraguay",
    Destination_City="Asunción",
    Start_Date="2024-07-08",
    End_Date="2024-07-08",
    Duration_Days="1",
    Trip_Objective="64a Cumbre del Mercosur en Asuncion, Paraguay (ingreso pleno de Bolivia al bloque anunciado en la cumbre).",
    nota="CORRECCION ESTRUCTURAL 2026-07-20: el dato original ubicaba la Cumbre del Mercosur en "
         "Santa Cruz de la Sierra, Bolivia. Fuentes oficiales (Planalto, Agencia Brasil) confirman "
         "que la 64a Cumbre del Mercosur (evento multilateral, Counterpart_Event) ocurrio en "
         "Asuncion, Paraguay, el 8/7/2024; Lula viajo luego a Santa Cruz de la Sierra, Bolivia, el "
         "9/7/2024 para una VISITA BILATERAL SEPARADA con el presidente Luis Arce. Se corrige "
         "pais/ciudad/fecha de ESTA fila al evento multilateral (Asuncion). PENDIENTE DE DECISION "
         "DEL USUARIO: el tramo bilateral a Bolivia (Santa Cruz de la Sierra, 9/7/2024, reunion con "
         "Arce) NO esta representado como fila propia en la base; evaluar si corresponde agregarlo "
         "como nueva fila Bilateral/Working Visit.",
)

ALL_IDS = set(VERIF.keys())

def append_note(existing, nota):
    if existing in ("NA", "", None):
        return nota
    return existing.rstrip(".") + ". " + nota

def process():
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    n_verif = n_datefix = 0
    for r in rows:
        tid = r["Trip_ID"]
        if tid not in ALL_IDS:
            continue
        url, rel = VERIF[tid]
        r["Source_Verification"] = url
        r["Source_Reliability"] = rel
        r["Verificacion_Status"] = "Verificada-URL"
        n_verif += 1

        if tid == "258":
            for k in ("Destination_Country", "Destination_City", "Start_Date", "End_Date",
                      "Duration_Days", "Trip_Objective"):
                r[k] = FIX_258[k]
            r["Destination_Region"] = region_for(r["Destination_Country"])
            r["Methodological_Notes"] = append_note(r["Methodological_Notes"], FIX_258["nota"])
            n_datefix += 1
            continue

        if tid in DATE_FIX:
            fix = DATE_FIX[tid]
            for k in ("Start_Date", "End_Date", "Duration_Days"):
                if k in fix:
                    r[k] = fix[k]
            r["Methodological_Notes"] = append_note(r["Methodological_Notes"], fix["nota"])
            n_datefix += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"brasil (Lula-3): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
