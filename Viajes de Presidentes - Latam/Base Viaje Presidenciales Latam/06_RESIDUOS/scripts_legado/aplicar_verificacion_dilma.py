# -*- coding: utf-8 -*-
"""
aplicar_verificacion_dilma.py — Campana de verificacion, tanda Dilma Rousseff
(Brasil, 2011-2016), investigacion 2026-07-20. Idempotente.

CLAVE DE MATCH: Trip_ID (dentro de brasil_viajes.csv, estable en este modulo;
el Trip_ID del modulo NO es el mismo que en la base consolidada).

Se ejecuta en LOTES INCREMENTALES: cada corrida agrega entradas nuevas a los
diccionarios VERIF / DATE_FIX y se corre de nuevo sobre el CSV ya parcialmente
actualizado.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, region_for

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")

# Trip_ID -> (url, reliability)
VERIF = {
    "145": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-assinados-por-ocasiao-da-visita-da-presidenta-dilma-roussef-a-argentina-buenos-aires-31-de-janeiro-de-2011", "High"),
    "146": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/visita-da-presidenta-dilma-rousseff-a-china-pequim-11-a-13-de-abril-de-2011-programa-de-imprensa", "High"),
    "147": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/discurso-na-abertura-do-debate-geral-da-66-assembleia-geral-das-nacoes-unidas-nova-york-eua-21-09-2011", "High"),
    "148": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/v-cupula-brasil-uniao-europeia-declaracao-conjunta-bruxelas-4-outubro-de-2011", "High"),
    "149": ("https://www.gov.br/mre/en/contact-us/press-area/press-releases/president-dilma-rousseff-visits-the-republic-of-bulgaria-sofia-october-5-6-2011", "High"),
    "150": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/dilma-vana-rousseff-2011-2016/discurso-da-presidenta-da-republica-dilma-rousseff-durante-reuniao-plenaria-da-v-cupula-do-ibas-pretoria-africa-do-sul-18-10-2011", "High"),
    "151": ("https://www.gov.br/mre/en/contact-us/press-area/press-releases/president-dilma-rousseff-to-take-part-in-the-6th-g20-summit-meeting-cannes-3-and-4-november-2011", "High"),
    "152": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/i-cupula-da-comunidade-dos-estados-latinoamericanos-e-caribenhos-celac-caracas-2-e-3-de-dezembro-de-2011-documentos-aprovados", "High"),
    "153": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/xlii-cupula-de-presidentes-do-mercosul-e-xlii-reuniao-do-conselho-do-mercado-comum-montevideu-19-e-20-de-dezembro-de-2011", "High"),
    "154": ("https://www.gov.br/mre/en/contact-us/press-area/press-releases/greeting-words-of-brazilian-president-dilma-rousseff-cebit-hannover-2012", "Medium"),
    "155": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/dilma-vana-rousseff-2011-2016/discurso-da-presidenta-da-republica-dilma-rousseff-durante-sessao-ampliada-da-iv-cupula-do-brics", "High"),
    "156": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-assinados-por-ocasiao-da-visita-da-presidenta-dilma-rousseff-aos-estados-unidos-da-america-washington-9-de-abril-de-2012", "High"),
    "157": ("http://www.itamaraty.gov.br/notas-a-imprensa/3017-visita-da-presidenta-dilma-rousseff-a-colombia-cartagena-das-indias-13-a-15-de-abril-de-2012-programa-de-imprensa", "High"),
    "158": ("https://en.wikipedia.org/wiki/2012_G20_Los_Cabos_summit", "Medium"),
    "159": ("https://en.mercopress.com/2011/12/20/chavez-expected-in-montevideo-to-announce-venezuela-s-mercosur-full-membership", "Medium"),
    "160": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/visita-da-presidenta-dilma-rousseff-a-nova-york-por-ocasiao-da-67-assembleia-geral-da-onu", "High"),
    "161": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/iii-cupula-america-do-sul-paises-arabes-aspa-lima-peru-2-de-outubro-de-2012", "High"),
    "162": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/i-cupula-celac-uniao-europeia-santiago-do-chile-26-e-27-de-janeiro-de-2013", "High"),
    "163": ("https://en.mercopress.com/2013/03/20/the-pope-is-argentine-but-god-is-brazilian-says-rousseff-francis-is-expected-in-rio-next-july", "Medium"),
    "164": ("http://www.brics.utoronto.ca/docs/130327-rousseff-statement.html", "Medium"),
    "165": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/atos-assinados-por-ocasiao-da-visita-da-presidenta-dilma-rousseff-a-republica-federal-democratica-da-etiopia-adis-abeba-24-de-maio-de-2013", "High"),
    "166": ("http://www.itamaraty.gov.br/pt-BR/notas-a-imprensa/3266-comunicado-conjunto-da-presidenta-da-republica-federativa-do-brasil-dilma-rousseff-e-do-presidente-da-federacao-da-russia-vladimir-vladimirovich-putin", "High"),
    "167": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/dilma-vana-rousseff-2011-2016/discurso-da-presidenta-da-republica-dilma-rousseff-na-abertura-do-debate-geral-da-68-assembleia-geral-das-nacoes-unidas", "High"),
    "168": ("https://www.npr.org/sections/thetwo-way/2013/09/17/223414386/brazilian-president-postpones-state-visit-over-spying-concerns", "Medium"),
    "169": ("http://www.itamaraty.gov.br/pt-BR/?option=com_content&view=article&id=5908:discurso-da-presidenta-da-republica-dilma-rousseff-durante-cerimonia-de-inauguracao-do-porto-de-mariel-provincia-de-artemisa-cuba-27-de-janeiro-de-2014&catid=197&Itemid=448&lang=pt-br", "High"),
    "171": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/discurso-proferido-pela-presidenta-da-republica-dilma-rousseff-na-abertura-do-debate-de-alto-nivel-da-69-assembleia-geral-das-nacoes-unidas-onu-nova-york-24-de-setembro-de-2014", "High"),
    "172": ("https://en.wikipedia.org/wiki/2014_G20_Brisbane_summit", "Medium"),
    "173": ("https://www.gov.br/casacivil/pt-br/assuntos/noticias/2014/dezembro/dilma-assume-presidencia-do-mercosul", "High"),
    "174": ("https://www.gov.br/mre/en/contact-us/press-area/press-releases/participation-of-president-dilma-rousseff-in-the-third-summit-of-the-community-of-latin-american-and-caribbean-states-celac-san-jose-costa-rica-january-28-29-2015", "High"),
    "175": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/vii-cupula-das-americas-cidade-do-panama-10-e-11-de-abril-de-2015", "High"),
    "176": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/visita-de-estado-da-presidenta-dilma-rousseff-ao-mexico-cidade-do-mexico-26-e-27-de-maio-de-2015", "High"),
    "177": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/comunicado-conjunto-da-presidenta-dilma-rousseff-e-do-presidente-barack-obama-washington-30-de-junho-de-2015", "High"),
    "178": ("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/vii-cupula-do-brics-declaracao-de-ufa-ufa-russia-9-de-julho-de-2015", "High"),
    "179": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/dilma-vana-rousseff-2011-2016/discurso-da-presidenta-da-republica-dilma-roussef-por-ocasiao-da-abertura-da-septuagesima-assembleia-geral-das-nacoes-unidas-nova-york-28-de-setembro-de-2015", "High"),
    "182": ("https://agenciabrasil.ebc.com.br/internacional/noticia/2015-11/dilma-defende-acao-internacional-urgente-contra-o-terrorismo-em-reuniao-do-Brics", "High"),
    "183": ("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos/dilma-vana-rousseff-2011-2016/discurso-da-presidenta-da-republica-dilma-rousseff-durante-sessao-de-abertura-da-21-conferencia-das-partes-da-convencao-quadro-das-nacoes-unidas-sobre-a-mudanca-do-clima-cop21-paris-30-de-novembro-de-2015", "High"),
    "184": ("http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/dilma-rousseff/discursos/discursos-da-presidenta/discurso-da-presidenta-da-republica-dilma-rousseff-durante-a-xlix-cupula-dos-estados-partes-do-mercosul-e-estados-associados-assuncao-paraguai", "High"),
    "185": ("https://www.gov.br/mre/en/contact-us/press-area/press-releases/president-dilma-rousseff-to-take-part-in-the-fourth-summit-of-the-community-of-latin-american-and-caribbean-states-celac-quito-ecuador-january-27-2016", "High"),
    "186": ("https://agenciabrasil.ebc.com.br/politica/noticia/2016-04/presidenta-dilma-discursa-em-sessao-da-onu", "High"),
}

# Trip_ID -> dict de correcciones de fecha/duracion (y nota)
DATE_FIX = {
    "149": dict(End_Date="2011-10-06", Duration_Days="2",
                nota="CORRECCION 2026-07-20: End_Date 2011-10-07 -> 2011-10-06. Fuente oficial "
                     "MRE ('President Dilma Rousseff visits the Republic of Bulgaria - Sofia, "
                     "October 5 and 6, 2011') y Wikipedia (lista de viajes) confirman que la "
                     "presidenta partio hacia Turquia la noche del 6/10/2011; la visita a Bulgaria "
                     "(Sofia + Gabrovo) fue 5-6 de octubre, no hasta el 7."),
    "160": dict(Start_Date="2012-09-23", End_Date="2012-09-26", Duration_Days="4",
                nota="CORRECCION 2026-07-20: fecha original (dia unico 25/09/2012) reemplazada "
                     "por el rango completo de la estancia. Fuente oficial MRE ('Visita da "
                     "Presidenta Dilma Rousseff a Nova York por ocasiao da 67a Assembleia-Geral "
                     "da ONU') confirma visita de trabalho a Nova York entre 23 e 26 de setembro "
                     "de 2012; discurso de abertura e reuniao com Ban Ki-moon no dia 25."),
    "165": dict(nota="NOTA 2026-07-20: fuente oficial MRE ('Atos assinados por ocasiao da visita "
                     "da Presidenta Dilma Rousseff a Republica Federal Democratica da Etiopia') "
                     "titula la visita el 24/05/2013, mientras que fuentes secundarias (Forcas "
                     "Terrestres) datan el anuncio de perdao de dividas africanas el 25/05/2013. "
                     "Fecha cargada (25/05) se mantiene sin cambios por tratarse de una visita de "
                     "un solo dia con posible discrepancia menor entre fuentes; no hay evidencia "
                     "de error claro que amerite correccion."),
    "176": dict(Start_Date="2015-05-26", Duration_Days="2",
                nota="CORRECCION 2026-07-20: Start_Date 2015-05-25 -> 2015-05-26. Fuente oficial "
                     "MRE ('Visita de Estado da Presidenta Dilma Rousseff ao Mexico - Cidade do "
                     "Mexico, 26 e 27 de maio de 2015') acota la visita de Estado a los dias 26-27; "
                     "no hay evidencia de actividad oficial el 25."),
}

def append_note(existing, nota):
    if existing in ("NA", "", None):
        return nota
    return existing.rstrip(".") + ". " + nota

def process():
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    n_verif = n_datefix = 0
    for r in rows:
        tid = r["Trip_ID"]
        if tid not in VERIF:
            continue
        url, rel = VERIF[tid]
        r["Source_Verification"] = url
        r["Source_Reliability"] = rel
        r["Verificacion_Status"] = "Verificada-URL"
        n_verif += 1

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
    print(f"brasil (Dilma): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
