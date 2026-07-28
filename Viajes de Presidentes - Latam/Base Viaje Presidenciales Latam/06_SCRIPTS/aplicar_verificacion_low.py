# -*- coding: utf-8 -*-
"""
aplicar_verificacion_low.py — Incorpora la campaña de verificación de fuentes
(research 2026-07-07) a los módulos país. Idempotente.

CLAVE DE MATCH: (Journey_ID, Destination_City), ESTABLE entre base y módulos.
NO se usa Trip_ID: integrate.py lo reasigna (bug detectado y corregido 2026-07-07).

  1) Agrega columna Verificacion_Status (21) si falta: "Verificada-URL" si la
     fuente empieza con http, si no "Solo-Query".
  2) Aplica URLs verificadas del lote Low (+ reliability + status).
  3) Marca "No-verificable" las filas sin fuente consultable.
  4) Punta Cana (Bachelet-CELAC): NO ocurrió -> Trip_Status=Canceled.
NO toca errores de fecha (Sarkozy 2009, Indonesia 2017, Lima 2017) ni CPAC Paraguay
de Milei: quedan para el build de correcciones posterior a la verificación confirmatoria.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(ROOT, "03_MODULOS_PAIS")

VERIF = {
    ("ARG-DLR-J002", "Berlin"):        ("https://www.cidob.org/lider-politico/gerhard-schroder", "Medium"),
    ("ARG-AF-J159", "Bridgetown"):     ("https://www.pagina12.com.ar/400384-alberto-fernandez-en-barbados-ultima-escala-de-su-gira", "Medium"),
    ("ARG-JM-J174", "Washington D.C."):("https://www.casarosada.gob.ar/informacion/discursos/50371-palabras-del-presidente-de-la-nacion-javier-milei-en-la-conferencia-politica-de-accion-conservadora-cpac-en-washington-estados-unidos", "High"),
    ("ARG-JM-J177", "Los Angeles"):    ("https://www.infobae.com/politica/2024/05/30/en-estados-unidos-javier-milei-diserto-ante-empresarios-de-silicon-valley-hablo-de-desregulacion-e-inteligencia-artificial/", "Medium"),
    ("ARG-JM-J179", "Prague"):         ("https://www.casarosada.gob.ar/informacion/discursos/50552-discurso-completo-del-presidente-javier-milei-al-recibir-el-premio-del-instituto-liberal-de-la-republica-checa-en-praga", "High"),
    ("ARG-JM-J194", "Davos"):          ("https://www.weforum.org/stories/2026/01/davos-2026-special-address-by-javier-milei-president-of-argentina/", "High"),
    ("BRA-FHC-J015", "Quito"):         ("https://pt.wikipedia.org/wiki/Lista_de_viagens_presidenciais_de_Fernando_Henrique_Cardoso", "Medium"),
    ("BRA-FHC-J016", "Paris"):         ("https://pt.wikipedia.org/wiki/Lista_de_viagens_presidenciais_de_Fernando_Henrique_Cardoso", "Medium"),
    ("BRA-LU-J063", "Stockholm"):      ("https://pt.wikipedia.org/wiki/Lista_de_viagens_presidenciais_de_Luiz_In%C3%A1cio_Lula_da_Silva", "Medium"),
    ("BRA-LU-J063", "Copenhagen"):     ("https://pt.wikipedia.org/wiki/Lista_de_viagens_presidenciais_de_Luiz_In%C3%A1cio_Lula_da_Silva", "Medium"),
    ("BRA-LU-J063", "Oslo"):           ("https://pt.wikipedia.org/wiki/Lista_de_viagens_presidenciais_de_Luiz_In%C3%A1cio_Lula_da_Silva", "Medium"),
    ("BRA-LU-J080", "Riyadh"):         ("https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/viagens/viagens-1", "High"),
    ("BRA-LU-J080", "Ankara"):         ("https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/viagens/viagens-1", "High"),
    ("BRA-LU3-J197", "Hanoi"):         ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-adotados-por-ocasiao-da-visita-de-estado-do-presidente-luiz-inacio-lula-da-silva-a-hanoi-vietna-27-a-29-de-marco-de-2025", "High"),
    ("BRA-DR-J132", "Stockholm"):      ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/viagem-da-presidenta-da-republica-a-suecia-e-a-finlandia-18-a-20-de-outubro-de-2015", "High"),
    ("BRA-DR-J132", "Helsinki"):       ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/viagem-da-presidenta-da-republica-a-suecia-e-a-finlandia-18-a-20-de-outubro-de-2015", "High"),
    ("BRA-JB-J169", "Manama"):         ("https://agenciabrasil.ebc.com.br/politica/noticia/2021-11/presidente-viaja-para-o-oriente-medio", "High"),
    ("BRA-JB-J169", "Doha"):           ("https://agenciabrasil.ebc.com.br/politica/noticia/2021-11/presidente-viaja-para-o-oriente-medio", "High"),
    ("CHL-RL-J008", "London"):         ("https://www.latercera.com/la-tercera-sabado/noticia/el-derrumbe-de-las-torres-gemelas-asi-se-vivio-el-11s-en-chile/ZHFF3MFYXRFOHGKQ7DN7ZOAQWM/", "Medium"),
    ("CHL-MB1-J033", "Wellington"):    ("https://es.wikipedia.org/wiki/Primer_gobierno_de_Michelle_Bachelet", "Medium"),
    ("CHL-MB1-J037", "Madrid"):        ("https://www.chile.gob.cl/chile/blog/espana/madrid/visita-de-estado-a-espana-de-s-e-michelle-bachelet", "Medium"),
    ("CHL-MB1-J039", "New York"):      ("https://ask.un.org/faq?gid=181&qid=73684", "High"),
    ("CHL-MB1-J049", "New York"):      ("https://gadebate.un.org/en/64/chile", "High"),
    ("CHL-MB2-J083", "Milan"):         ("https://www.gob.cl/2015/06/06/presidenta-bachelet-en-expo-milan-2015-estamos-aqui-mostrando-una-vez-mas-al-mundo-lo-mejor-de-nuestro-pais/", "High"),
    ("CHL-MB2-J091", "New York"):      ("https://ask.un.org/faq?gid=181&qid=73684", "High"),
    ("CHL-MB2-J097", "New York"):      ("https://ask.un.org/faq?gid=181&qid=73684", "High"),
    ("CHL-SP1-J054", "Brasília"):      ("https://www.elcolombiano.com/historico/lula_y_pinera_se_reunen_en_brasilia-CWEC_84996", "Medium"),
    ("CHL-SP1-J057", "Paris"):         ("https://archivo.eluniversal.com.mx/notas/717938.html", "Medium"),
    ("CHL-SP1-J057", "Berlin"):        ("https://archivo.eluniversal.com.mx/notas/717938.html", "Medium"),
    ("CHL-SP1-J063", "New York"):      ("https://ask.un.org/faq?gid=181&qid=73684", "High"),
    ("CHL-SP1-J074", "Asunción"):      ("https://www.chile.gob.cl/chile/blog/paraguay/asuncion/presidente-pinera-en-paraguay-tenemos-la-firme-voluntad-e-intencion-de", "High"),
}

NO_VERIF = {
    ("ARG-CFK-J061", "Caracas"), ("ARG-CFK-J088", "Havana"),
    ("CHL-RL-J006", "Paris"), ("CHL-RL-J020", "Normandy"), ("CHL-RL-J021", "Jakarta"),
    ("CHL-MB1-J035", "Quito"), ("CHL-MB1-J037", "Paris"), ("CHL-SP1-J060", "Montevideo"),
}
CANCEL = ("CHL-MB2-J094", "Punta Cana")

def process(pais):
    path = os.path.join(MOD, pais, f"{pais}_viajes.csv")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    add_col = verif = noverif = cancel = 0
    for r in rows:
        key = (r["Journey_ID"], r["Destination_City"])
        sv = str(r.get("Source_Verification", ""))
        if r.get("Verificacion_Status", "") in ("", None):
            r["Verificacion_Status"] = "Verificada-URL" if sv.startswith("http") else "Solo-Query"
            add_col += 1
        if key in VERIF:
            url, rel = VERIF[key]
            r["Source_Verification"], r["Source_Reliability"], r["Verificacion_Status"] = url, rel, "Verificada-URL"
            verif += 1
        elif key in NO_VERIF:
            r["Verificacion_Status"] = "No-verificable"; noverif += 1
        if key == CANCEL:
            r["Trip_Status"], r["End_Date"], r["Duration_Days"] = "Canceled", "NA", "NA"
            r["Source_Verification"] = "https://www.latercera.com/noticia/presidenta-bachelet-suspende-viaje-a-cumbre-celac-por-incendios/"
            r["Source_Reliability"], r["Verificacion_Status"] = "High", "Verificada-URL"
            base = r["Trip_Objective"].split(" VIAJE NO REALIZADO")[0].rstrip(".")
            r["Trip_Objective"] = base + ". VIAJE NO REALIZADO: suspendido el 23-01-2017 por los incendios forestales en Chile; asistió el canciller Heraldo Muñoz."
            nota = "Reclasificado a Canceled el 2026-07-07 (campaña de verificacion): el viaje no ocurrio."
            r["Methodological_Notes"] = nota if r["Methodological_Notes"] == "NA" else r["Methodological_Notes"].rstrip(".") + ". " + nota
            cancel += 1
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"{pais}: +col {add_col} | URLs {verif} | no-verif {noverif} | cancelados {cancel}")

if __name__ == "__main__":
    for p in ("argentina", "brasil", "chile"): process(p)
