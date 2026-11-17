# -*- coding: utf-8 -*-
"""
verificacion_lula_t2.py — Campaña de verificacion, TANDA 2 de Lula (2do mandato 2008-2010).
35 tramos auditados: 33 VERIFICADOS con URL, 2 VIAJES QUE NO OCURRIERON, 1 tramo DESDOBLADO, 0 no-verificables.
Match por (Journey_ID, Destination_City). Idempotente.

HALLAZGOS PRINCIPALES (2 viajes que la base daba por realizados y NO ocurrieron):
  - J087 Davos (ene-2010): Lula NO viajo. Cuadro de hipertension; segun Klaus Schwab "estava sentado em seu
    aviao quando o medico vetou a viagem". Lo represento Celso Amorim, y Kofi Annan le entrego el premio
    "Estadista Global" el 29-ene-2010. La Biblioteca no registra viaje en enero 2010.
  - J093 Toronto G20 (jun-2010): Lula CANCELO el 25-jun para monitorear las inundaciones del Nordeste
    (40 muertos en Pernambuco y Alagoas). Lo represento el ministro Guido Mantega.
  Ambos se convierten a Trip_Status=Canceled (el destino estaba formalmente anunciado), NO se borran,
  siguiendo el precedente de Bachelet-Punta Cana.

DESDOBLAMIENTO:
  - J083 mezclaba dos ciudades y fechas: 64ª AGNU en Nueva York (23-sep) y Cumbre del G20 en PITTSBURGH
    (24-25 sep). Se acota la fila de NY al 23-sep y se crea un tramo nuevo para Pittsburgh (mismo Journey).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")

BIB = "https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/viagens/viagens-1"
SEN_ISR = "https://www2.senado.leg.br/bdsf/bitstream/handle/id/45100/noticia.htm?sequence=1&isAllowed=y"
SEN_RAM = "https://www2.senado.leg.br/bdsf/bitstream/handle/id/45432/noticia.htm?sequence=1"

URLS = {
    ("BRA-LU-J076", "Washington D.C."): (BIB, "High"),
    ("BRA-LU-J077", "Washington D.C."): ("https://globalvoices.org/2009/03/15/brazil-lula-and-obama-meet-as-economic-crisis-hits-brazil/", "Medium"),
    ("BRA-LU-J078", "Doha"): (BIB, "High"),
    ("BRA-LU-J078", "London"): ("https://g20.utoronto.ca/2009/2009communique0402-br.html", "High"),
    ("BRA-LU-J079", "Port of Spain"): (BIB, "High"),
    ("BRA-LU-J080", "Beijing"): (BIB, "High"),
    ("BRA-LU-J081", "Geneva"): (BIB, "High"),
    ("BRA-LU-J081", "Yekaterinburg"): (BIB, "High"),
    ("BRA-LU-J082", "L'Aquila"): ("https://obamawhitehouse.archives.gov/realitycheck/the-press-office/readout-press-secretary-robert-gibbs-presidents-bilateral-meeting-with-president-lu", "High"),
    ("BRA-LU-J084", "Isla Margarita"): ("https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/galeria-de-fotos/fotos-de-viagens-internacionais-2009/venezuela/presidente-lula-e-o-presidente-da-libia-muamar-khadafi-durante-a-ii-cupula-america-do-sul-e-africa-em-isla-margarita/view", "High"),
    ("BRA-LU-J085", "Copenhagen"): (BIB, "High"),
    ("BRA-LU-J086", "Copenhagen"): ("https://www.terra.com.br/noticias/ciencia/em-copenhague-lula-afina-discurso-do-brasil-para-a-cop-15,64d8cb535a8ea310VgnCLD200000bbcceb0aRCRD.html", "Medium"),
    ("BRA-LU-J088", "Cancún"): (BIB, "High"),
    ("BRA-LU-J088", "Port-au-Prince"): (BIB, "High"),
    ("BRA-LU-J089", "Jerusalem"): (SEN_ISR, "Medium"),
    ("BRA-LU-J089", "Ramallah"): (SEN_RAM, "Medium"),
    ("BRA-LU-J089", "Amman"): (SEN_RAM, "Medium"),
    ("BRA-LU-J090", "Washington D.C."): (BIB, "High"),
    ("BRA-LU-J091", "Moscow"): (BIB, "High"),
    ("BRA-LU-J091", "Tehran"): (BIB, "High"),
    ("BRA-LU-J091", "Madrid"): (BIB, "High"),
    ("BRA-LU-J092", "Buenos Aires"): (BIB, "High"),
    ("BRA-LU-J094", "Sal"): (BIB, "High"),
    ("BRA-LU-J094", "Malabo"): (BIB, "High"),
    ("BRA-LU-J094", "Nairobi"): (BIB, "High"),
    ("BRA-LU-J094", "Dar es Salaam"): (BIB, "High"),
    ("BRA-LU-J094", "Lusaka"): (BIB, "High"),
    ("BRA-LU-J094", "Johannesburg"): (BIB, "High"),
    ("BRA-LU-J095", "Maputo"): ("https://www.publico.pt/2010/11/10/jornal/lula-despedese-de-africa-com-visita-a-mocambique-20586786", "Medium"),
    ("BRA-LU-J095", "Seoul"): ("https://www.voaportugues.com/a/article-11-08-2010-lula-da-silva-mozambique-voanews-106904663/1258893.html", "Medium"),
    ("BRA-LU-J096", "Georgetown"): ("https://www2.senado.leg.br/bdsf/bitstream/handle/id/47381/noticia.htm?sequence=1", "Medium"),
    ("BRA-LU-J097", "Mar del Plata"): ("https://segib.org/es/cumbre/xx-cumbre-iberoamericana/", "High"),
}

# Fila de NY: se acota al dia de la AGNU (el G20 fue en Pittsburgh, se desdobla)
AJUSTES = {
    ("BRA-LU-J083", "New York"): {
        "End_Date": "2009-09-23", "Duration_Days": "1",
        "Counterpart_Event": "64ª Asamblea General de la ONU",
        "Trip_Objective": "Discurso de apertura del debate general de la 64ª AGNU.",
        "Source_Verification": "https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/discursos/2o-mandato/2009/23-09-2009-discurso-do-presidente-da-republica-luiz-inacio-lula-da-silva-durante-a-abertura-do-debate-geral-da-64a-assembleia-geral-das-nacoes-unidas",
        "Source_Reliability": "High", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": ("DESDOBLADO 2026-07-08: la fila original mezclaba la 64ª AGNU (Nueva York, 23-sep) con la "
            "Cumbre del G20 de Pittsburgh (24-25 sep), que son ciudades y fechas distintas. Se acota esta fila a Nueva York "
            "y se creo un tramo nuevo para Pittsburgh dentro del mismo Journey."),
    },
}

# Viajes que NO ocurrieron -> Canceled (destino formalmente anunciado)
NO_OCURRIERON = {
    ("BRA-LU-J087", "Davos"): {
        "Trip_Status": "Canceled", "End_Date": "NA", "Duration_Days": "NA",
        "Trip_Objective": ("Objetivo original: recibir el premio 'Estadista Global' del Foro Economico Mundial. "
            "CANCELADO por un cuadro de hipertension; lo represento el excanciller Celso Amorim."),
        "Source_Verification": "https://pt.org.br/ha-nove-anos-lula-recebia-trofeu-de-estadista-global/",
        "Source_Reliability": "Medium", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": ("CORREGIDO 2026-07-08: la base lo daba por REALIZADO y NO OCURRIO. Lula no viajo a Davos: "
            "segun Klaus Schwab, 'estava sentado em seu aviao quando o medico vetou a viagem porque estava sofrendo de "
            "pressao alta'. Kofi Annan entrego el premio a Celso Amorim el 29-ene-2010. La lista de viajes de la Biblioteca "
            "da Presidencia no registra ningun viaje en enero de 2010."),
    },
    ("BRA-LU-J093", "Toronto"): {
        "Trip_Status": "Canceled", "End_Date": "NA", "Duration_Days": "NA",
        "Trip_Objective": ("Objetivo original: Cumbre del G20 de Toronto. CANCELADO el 25-jun para monitorear las "
            "inundaciones del Nordeste brasileno; lo represento el ministro de Hacienda Guido Mantega."),
        "Source_Verification": "https://en.wikipedia.org/wiki/2010_G20_Toronto_summit",
        "Source_Reliability": "Medium", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": ("CORREGIDO 2026-07-08: la base lo daba por REALIZADO y NO OCURRIO. Celso Amorim: 'o ministro "
            "Mantega o representara na reuniao do G20, porque ele quer acompanhar as medidas que estao sendo tomadas em "
            "relacao as enchentes no Nordeste' (40 muertos en Pernambuco y Alagoas). La Biblioteca no registra viaje a "
            "Canada en junio de 2010."),
    },
}

def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    n_url = n_aj = n_no = 0
    for r in rows:
        k = (r["Journey_ID"], r["Destination_City"])
        if k in URLS:
            u, rel = URLS[k]
            r["Source_Verification"] = u; r["Source_Reliability"] = rel
            r["Verificacion_Status"] = "Verificada-URL"; n_url += 1
        if k in AJUSTES:
            r.update(AJUSTES[k]); n_aj += 1
        if k in NO_OCURRIERON:
            r.update(NO_OCURRIERON[k]); n_no += 1

    # Nuevo tramo: Pittsburgh (desdoblamiento de J083)
    if not any(r["Journey_ID"] == "BRA-LU-J083" and r["Destination_City"] == "Pittsburgh" for r in rows):
        tid = max(int(r["Trip_ID"]) for r in rows) + 1
        rows.append(new_row(
            Journey_ID="BRA-LU-J083", Trip_ID=tid, President="Luiz Inácio Lula da Silva", Origin_Country="Brasil",
            Trip_Status="Completed", Start_Date="2009-09-24", End_Date="2009-09-25", Duration_Days=2,
            Destination_Country="United States", Destination_City="Pittsburgh",
            Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
            Counterpart_Event="Cumbre del G20 de Pittsburgh",
            Trip_Objective="Cumbre del G20 de Pittsburgh; agenda de reforma de la gobernanza economica global.",
            Source_Verification="https://2009-2017.state.gov/e/eb/ecosum/pittsburgh2009/resources/165081.htm",
            Source_Reliability="High",
            Methodological_Notes=("Tramo CREADO 2026-07-08 por desdoblamiento de la fila de Nueva York (J083), que mezclaba "
                "la 64ª AGNU con la Cumbre del G20 de Pittsburgh. Comparte Journey_ID: fue el mismo viaje fisico a EEUU."),
            Tema_Foro="Comercio/Integración Económica"))
        print("  + tramo nuevo: Pittsburgh (G20, 24-25 sep 2009)")

    with open(CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"brasil: {n_url} URLs | {n_aj} ajustes | {n_no} viajes reclasificados a Canceled")

if __name__ == "__main__":
    main()
