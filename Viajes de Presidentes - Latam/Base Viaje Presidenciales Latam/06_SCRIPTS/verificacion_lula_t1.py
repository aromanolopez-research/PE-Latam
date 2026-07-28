# -*- coding: utf-8 -*-
"""
verificacion_lula_t1.py — Campaña de verificacion, TANDA 1 de Lula (1er mandato 2003-2007).
35 tramos auditados: 34 VERIFICADOS con URL, 1 con correccion de fecha, 0 no-verificables, 0 inexistentes.
Match por (Journey_ID, Destination_City) — clave estable. Idempotente.

GOLD STANDARD confirmado para Brasil: Biblioteca da Presidencia ("Viagens"), que lista aniо por aniо
todos los viajes con rango de fechas y resume las giras multi-pais en una sola entrada.
Complementos productivos: Itamaraty (gov.br/mre, discursos fechados por ciudad), FUNAG (funag.gov.br),
Agencia Brasil (memoria.ebc.com.br), y los organismos del evento (ONU, Consejo UE, G7 Info Centre, MOFA Japon).

CORRECCION APLICADA:
  BRA-LU-J054 San Petersburgo: la base tenia 15-17/07/2006 (rango completo de la cumbre G8), pero el
  Chair's Summary oficial precisa que los lideres invitados (Brasil, China, India, Mexico, Sudafrica)
  se sumaron el 17/07. Se acota al dia confirmado de participacion.

MARCADO PARA REVISION (no se toca la fecha):
  BRA-LU-J041 Sao Tome: la base tiene 23-24/07/2004; la Biblioteca fecha la gira 25-29/07/2004.
  Discrepancia de dias de escala, pendiente de conciliar.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")

BIBLIO = "https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/viagens/viagens-1"
SENADO = "https://www2.senado.leg.br/bdsf/bitstream/handle/id/331531/noticia.htm?sequence=1&isAllowed=y"

# (Journey_ID, Destination_City) -> (URL, Reliability)
URLS = {
    ("BRA-LU-J028", "Évian-les-Bains"): ("https://memoria.ebc.com.br/agenciabrasil/noticia/2003-06-01/leia-integra-do-discurso-de-lula-na-reuniao-do-g-8", "High"),
    ("BRA-LU-J029", "Washington D.C."): (BIBLIO, "High"),
    ("BRA-LU-J030", "New York"): ("https://www.un.org/webcast/ga/58/statements/brazil-spanish.htm", "High"),
    ("BRA-LU-J031", "Havana"): ("https://www.publico.pt/2003/09/28/mundo/noticia/lula-fortalece-cooperacao-com-cuba-1168185", "Medium"),
    ("BRA-LU-J032", "São Tomé"): (BIBLIO, "High"),
    ("BRA-LU-J032", "Luanda"): (BIBLIO, "High"),
    ("BRA-LU-J032", "Maputo"): (BIBLIO, "High"),
    ("BRA-LU-J032", "Windhoek"): (BIBLIO, "High"),
    ("BRA-LU-J032", "Pretoria"): (BIBLIO, "High"),
    ("BRA-LU-J034", "Damascus"): (BIBLIO, "High"),
    ("BRA-LU-J034", "Beirut"): (BIBLIO, "High"),
    ("BRA-LU-J034", "Dubai"): (BIBLIO, "High"),
    ("BRA-LU-J034", "Cairo"): (BIBLIO, "High"),
    ("BRA-LU-J034", "Tripoli"): (BIBLIO, "High"),
    ("BRA-LU-J041", "São Tomé"): (BIBLIO, "High"),
    ("BRA-LU-J041", "Libreville"): (BIBLIO, "High"),
    ("BRA-LU-J041", "Praia"): (BIBLIO, "High"),
    ("BRA-LU-J042", "New York"): (BIBLIO, "High"),
    ("BRA-LU-J044", "Cusco"): ("https://es.wikisource.org/wiki/Declaraci%C3%B3n_de_Cusco_sobre_la_Comunidad_Suramericana_de_Naciones", "High"),
    ("BRA-LU-J045", "Montevideo"): (BIBLIO, "High"),
    ("BRA-LU-J046", "Seoul"): ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/luiz-inacio-lula-da-silva-2003-2011/discurso-em-jantar-oferecido-pelo-presidente-da-coreia-roh-moo-hyun-seul-25-de-maio-de-2005", "High"),
    ("BRA-LU-J053", "Vienna"): ("https://ec.europa.eu/commission/presscorner/detail/en/pres_06_137", "High"),
    ("BRA-LU-J054", "Saint Petersburg"): ("https://www.mofa.go.jp/policy/economy/summit/2006/summary.html", "High"),
    ("BRA-LU-J055", "New York"): ("https://www.funag.gov.br/loja/download/505-discursos_selecionados_lula.pdf", "Medium"),
    ("BRA-LU-J057", "Abuja"): ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/luiz-inacio-lula-da-silva-2003-2007/discurso-da-abertura-da-cupula-africa-america-do-sul-abuja-nigeria-30-de-novembro-de-2006", "High"),
    ("BRA-LU-J058", "Cochabamba"): (BIBLIO, "High"),
    ("BRA-LU-J059", "Quito"): (BIBLIO, "High"),
    ("BRA-LU-J060", "Camp David"): ("https://georgewbush-whitehouse.archives.gov/news/releases/2007/03/20070331-3.html", "High"),
    ("BRA-LU-J061", "Heiligendamm"): ("https://g7.utoronto.ca/portugues/br-070607.html", "High"),
    ("BRA-LU-J062", "Lisbon"): ("https://www.consilium.europa.eu/ueDocs/cms_Data/docs/pressData/en/er/95167.pdf", "High"),
    ("BRA-LU-J064", "New York"): ("https://ask.un.org/faq/70473", "High"),
    ("BRA-LU-J065", "Ouagadougou"): (SENADO, "Medium"),
    ("BRA-LU-J065", "Brazzaville"): (SENADO, "Medium"),
    ("BRA-LU-J065", "Pretoria"): ("https://icwa.in/show_content.php?lang=1&level=3&ls_id=2336&lid=1758", "High"),
    ("BRA-LU-J065", "Luanda"): (SENADO, "Medium"),
}

CORRECCIONES = {
    ("BRA-LU-J054", "Saint Petersburg"): {
        "Start_Date": "2006-07-17", "End_Date": "2006-07-17", "Duration_Days": "1",
        "Methodological_Notes": ("Fecha ACOTADA 2026-07-08 (la base tenia 15-17/07/2006, rango completo de la cumbre). "
            "El Chair's Summary oficial (MOFA Japon) precisa que los lideres invitados -Brasil, China, India, Mexico y "
            "Sudafrica- se sumaron el 17/07. Se consigna el dia confirmado de participacion de Lula."),
    },
}

REVISAR = {
    ("BRA-LU-J041", "São Tomé"):
        "REVISION 2026-07-08: discrepancia de fechas. La base consigna 23-24/07/2004, pero la Biblioteca da Presidencia "
        "fecha la gira CPLP/Gabon/Cabo Verde entre el 25 y el 29/07/2004. Conciliar el dia exacto de la escala. "
        "El evento (V Cumbre CPLP) esta confirmado; lo dudoso es el dia de arribo.",
}

def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    n_url = n_fix = n_rev = 0
    for r in rows:
        k = (r["Journey_ID"], r["Destination_City"])
        if k in URLS:
            url, rel = URLS[k]
            r["Source_Verification"] = url
            r["Source_Reliability"] = rel
            r["Verificacion_Status"] = "Verificada-URL"
            n_url += 1
        if k in CORRECCIONES:
            r.update(CORRECCIONES[k]); n_fix += 1
        if k in REVISAR:
            base = r["Methodological_Notes"].split(" REVISION 2026-07-08")[0].rstrip(".")
            r["Methodological_Notes"] = REVISAR[k] if base == "NA" else base + ". " + REVISAR[k]
            n_rev += 1
    with open(CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"brasil: {n_url} URLs aplicadas | {n_fix} correcciones de fecha | {n_rev} marcados para revision")

if __name__ == "__main__":
    main()
