# -*- coding: utf-8 -*-
"""
aplicar_verificacion_bolsonaro.py — Campaña de verificación, Jair Bolsonaro
(Brasil, 2019-2023), investigación 2026-07-20. Idempotente.

CLAVE DE MATCH: Trip_ID (dentro de brasil_viajes.csv, estable en este módulo;
el Trip_ID del módulo NO es el mismo que en la base consolidada).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, region_for

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")

# Trip_ID -> (url, reliability)
VERIF = {}
DATE_FIX = {}

# ---- LOTE 1: Trip_ID 205-218 ----
VERIF.update({
    "205": ("https://www.gov.br/funag/pt-br/centrais-de-conteudo/politica-externa-brasileira/discurso-do-presidente-da-republica-jair-bolsonaro-durante-a-sessao-plenaria-do-forum-economico-mundial", "High"),
    "206": ("https://br.usembassy.gov/pt/declaracao-do-secretario-de-imprensa-sobre-a-visita-do-presidente-jair-bolsonaro-do-brasil/", "High"),
    "207": ("http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/bolsonaro/entrevistas/entrevista-coletiva-concedida-pelo-presidente-da-republica-jair-bolsonaro-na-sua-chegada-ao-chile-santiago-chile", "High"),
    "208": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/2019/visita-oficial-a-israel-de-sua-excelencia-o-presidente-da-republica-federativa-do-brasil-jair-bolsonaro", "High"),
    "209": ("https://agenciabrasil.ebc.com.br/politica/noticia/2019-06/bolsonaro-e-macri-se-reunem-em-buenos-aires-nesta-quinta-feira", "High"),
    "210": ("http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/bolsonaro/entrevistas/entrevista-coletiva-concedida-pelo-presidente-da-republica-jair-bolsonaro-osaka-japao", "High"),
    "211": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/jair-messias-bolsonaro-2019-2022/discurso-do-presidente-da-republica-jair-bolsonaro-cupula-mercosul-santa-fe-argentina-17-7-2019", "High"),
    "212": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/jair-messias-bolsonaro-2019-2022/discurso-do-presidente-jair-bolsonaro-na-abertura-da-74-assembleia-geral-das-nacoes-unidas-nova-york-24-de-setembro-de-2019", "High"),
    "213": ("https://agenciabrasil.ebc.com.br/internacional/noticia/2019-10/bolsonaro-chega-ao-japao-para-giro-por-asia-e-oriente-medio", "High"),
    "214": ("https://agenciabrasil.ebc.com.br/politica/noticia/2019-10/bolsonaro-chega-pequim-e-reune-se-com-empresarios", "High"),
    "215": ("https://agenciabrasil.ebc.com.br/politica/noticia/2019-10/bolsonaro-se-reune-com-empresarios-nos-emirados-arabes-unidos", "High"),
    "216": ("https://mofa.gov.qa/en/qatar/latest-articles/latest-news/details/2019/10/28/joint-statement-of-the-state-of-qatar-and-the-federative-republic-of-brazil", "High"),
    "217": ("https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/bolsonaro/discursos/discurso-do-presidente-da-republica-jair-bolsonaro-durante-sessao-sobre-o-brasil-do-fii-riade-arabia-saudita", "High"),
    "218": ("http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/bolsonaro/discursos/discurso-do-presidente-da-republica-jair-bolsonaro-durante-cafe-da-manha-de-trabalho-com-empresarios-indianos-nova-delhi-india", "High"),
})

# ---- LOTE 2: Trip_ID 219-224, 227-229, 231-234 (NO incluye 230, ver nota abajo) ----
VERIF.update({
    "219": ("https://agenciabrasil.ebc.com.br/internacional/noticia/2020-03/bolsonaro-vai-montevideu-para-posse-de-novo-presidente-uruguaio", "High"),
    "220": ("https://trumpwhitehouse.archives.gov/briefings-statements/remarks-president-trump-president-bolsonaro-brazil-working-dinner-west-palm-beach-fl/", "High"),
    "221": ("https://agenciabrasil.ebc.com.br/internacional/noticia/2021-05/guillermo-lasso-assume-presidencia-do-equador", "High"),
    "222": ("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2021/09/discurso-do-presidente-da-republica-jair-bolsonaro-na-abertura-da-76deg-assembleia-geral-da-onu", "High"),
    "223": ("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2021/10/presidente-jair-bolsonaro-ja-esta-na-italia-para-participar-do-g20", "High"),
    "224": ("https://agenciabrasil.ebc.com.br/politica/noticia/2021-11/em-dubai-presidente-bolsonaro-participa-de-forum-de-investimentos", "High"),
    "227": ("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2022/02/presidente-jair-bolsonaro-ja-esta-em-moscou-para-visita-oficial-a-russia", "High"),
    "228": ("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2022/02/presidente-jair-bolsonaro-faz-visita-oficial-a-hungria", "High"),
    "229": ("https://agenciabrasil.ebc.com.br/politica/noticia/2022-06/presidentes-bolsonaro-e-biden-fazem-reuniao-bilateral-nos-eua", "High"),
    "231": ("https://agenciabrasil.ebc.com.br/politica/noticia/2022-09/bolsonaro-participa-do-funeral-da-rainha-elizabeth-ii-em-londres", "High"),
    "232": ("https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/bolsonaro/discursos/discurso-do-presidente-da-republica-jair-bolsonaro-na-abertura-do-debate-geral-da-77a-sessao-da-assembleia-geral-das-nacoes-unidas-agnu", "High"),
    "233": ("https://www.cnnbrasil.com.br/politica/governo-gastou-pelo-menos-r-795-mil-com-viagem-de-bolsonaro-a-orlando/", "Medium"),
    "234": ("https://www.poder360.com.br/governo/bolsonaro-cancela-ida-a-davos/", "Medium"),
})

DATE_FIX.update({
    "233": dict(nota="NOTA 2026-07-20: multiples fuentes cruzadas (CNN Brasil, Al Jazeera, Publico) "
                     "confirman salida el 30/12/2022 hacia Orlando (avion da FAB), sin agenda oficial, "
                     "para no traspasar la banda presidencial a Lula el 1/1/2023; permanecio en EE.UU. "
                     "mas de un mes tras el fin del mandato (dato no cargado, fuera del periodo de "
                     "observacion). Fuente exclusivamente periodistica: no hay comunicado oficial de "
                     "Planalto/MRE sobre este viaje (consistente con 'sin agenda oficial')."),
    "234": dict(nota="NOTA 2026-07-20: segun el vocero de la Presidencia (Otavio do Rego Barros), la "
                     "cancelacion de Davos 2020 respondio a una combinacion de factores economicos, de "
                     "seguridad y politicos, SIN que la seguridad fuera el motivo exclusivo o principal "
                     "(poder360, 8/1/2020). El texto cargado ('razones de seguridad/conveniencia') es "
                     "consistente con esta fuente."),
})

# Trip_ID 230 (BRA-JB-J172, Cupula Mercosur, Asuncion, Paraguay, 21/7/2022):
# HALLAZGO CRITICO -- NO SE APLICA VERIFICACION. Fuente oficial de la Agencia Brasil
# (https://agenciabrasil.ebc.com.br/internacional/noticia/2022-07/presidentes-se-reunem-na-60a-cupula-do-mercosul-no-paraguai,
# titular: "Presidente Bolsonaro participa do encontro por videoconferencia") confirma que
# Bolsonaro CANCELO su viaje presencial a Asuncion y participo de la 60a Cumbre del Mercosur
# POR VIDEOCONFERENCIA desde Brasil. Es decir, el tramo de viaje tal como esta cargado
# (Trip_Status=Completed, viaje fisico a Asuncion) NO OCURRIO. Se deja nota metodologica y
# el Verificacion_Status SIN CAMBIOS (Solo-Query) para que el usuario decida: dar de baja la
# fila, marcarla como Canceled, o mantenerla con la aclaracion (la participacion virtual en
# una cumbre no constituye un "tramo de viaje" segun la unidad de observacion del CODEBOOK).
NOTA_230 = ("HALLAZGO 2026-07-20 (INVESTIGACION, NO APLICADO): fuente oficial Agencia Brasil "
            "confirma que Bolsonaro CANCELO el viaje presencial a Asuncion y participo de la "
            "60a Cupula del Mercosur POR VIDEOCONFERENCIA desde Brasil (titular: 'Presidente "
            "Bolsonaro participa do encontro por videoconferencia'). URL: "
            "https://agenciabrasil.ebc.com.br/internacional/noticia/2022-07/presidentes-se-reunem-na-60a-cupula-do-mercosul-no-paraguai "
            "-- Esta fila probablemente NO deberia estar cargada como tramo de viaje fisico "
            "(Trip_Status=Completed). PENDIENTE DE DECISION DEL USUARIO: no se modifico "
            "Verificacion_Status ni Trip_Status.")

ALL_IDS = set(VERIF.keys())

def append_note(existing, nota):
    if existing in ("NA", "", None):
        return nota
    if nota[:40] in existing:
        return existing
    return existing.rstrip(".") + ". " + nota

def process():
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    n_verif = n_datefix = 0
    for r in rows:
        tid = r["Trip_ID"]
        if tid == "230":
            r["Methodological_Notes"] = append_note(r["Methodological_Notes"], NOTA_230)
            continue
        if tid not in ALL_IDS:
            continue
        url, rel = VERIF[tid]
        r["Source_Verification"] = url
        r["Source_Reliability"] = rel
        r["Verificacion_Status"] = "Verificada-URL"
        n_verif += 1

        if tid in DATE_FIX:
            fix = DATE_FIX[tid]
            for k in ("Start_Date", "End_Date", "Duration_Days",
                      "Destination_Country", "Destination_City", "Trip_Objective"):
                if k in fix:
                    r[k] = fix[k]
            if "Destination_Country" in fix:
                r["Destination_Region"] = region_for(r["Destination_Country"])
            r["Methodological_Notes"] = append_note(r["Methodological_Notes"], fix["nota"])
            n_datefix += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"brasil (Bolsonaro): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
