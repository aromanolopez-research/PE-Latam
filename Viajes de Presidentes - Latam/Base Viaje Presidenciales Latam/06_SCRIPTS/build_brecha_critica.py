# -*- coding: utf-8 -*-
"""
BRECHA-CRITICA CERRADA — Milei (ARG) y Lula III (BRA), ventanas nov-2025 a mar-2026.
Investigacion complementaria (modo investigador, 2026-07-08): 16 viajes nuevos verificados
(9 Milei + 7 Lula), todos Completed y con URL consultable (14 High / 2 Medium, 0 No-verificable).
Journey_ID en rango alto (J900+) para no colisionar con la numeracion existente.
Trip_ID: se asignan continuando el maximo de cada modulo; integrate.py los reasigna globalmente.
EXCLUSIONES aplicadas: COP30 Belem y Cumbre MERCOSUR Foz de Iguazu NO cuentan para Lula (son EN Brasil),
si para Milei (viajo a Brasil). Escala tecnica de Lula en Tunez no computa.
6 AUSENCIAS CONFIRMADAS documentadas aparte en hallazgos (no son filas).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(ROOT, "03_MODULOS_PAIS")

def siguiente_tid(pais):
    rows = list(csv.DictReader(open(os.path.join(MOD, pais, f"{pais}_viajes.csv"), encoding="utf-8")))
    return max(int(r["Trip_ID"]) for r in rows) + 1

# ---------------- MILEI (Argentina) ----------------
MILEI = "Javier Milei"
arg_rows = []; tid = siguiente_tid("argentina")

def addm(jid, **kw):
    global tid
    kw.setdefault("President", MILEI); kw.setdefault("Origin_Country", "Argentina")
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    arg_rows.append(new_row(**kw)); tid += 1

addm("ARG-JM-J900", Trip_Status="Completed", Start_Date="2025-10-14", End_Date="2025-10-14", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington DC", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump",
    Trip_Objective="Visita a la Casa Blanca; bilateral y almuerzo con Trump; respaldo financiero y politico previo a las legislativas.",
    Source_Verification="https://www.argentina.gob.ar/noticias/el-presidente-javier-milei-se-reunio-con-el-presidente-de-los-estados-unidos-donald-trump",
    Source_Reliability="High")

addm("ARG-JM-J901", Trip_Status="Completed", Start_Date="2025-11-05", End_Date="2025-11-07", Duration_Days=3,
    Destination_Country="United States", Destination_City="Miami / New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="FALSE", Counterpart_Event="America Business Forum",
    Trip_Objective="Diserto en el America Business Forum (Miami); reuniones con inversores del Council of the Americas.",
    Source_Verification="https://www.infobae.com/estados-unidos/2025/11/06/en-vivo-de-serena-williams-a-jeff-bezos-y-javier-milei-todos-los-protagonistas-de-la-segunda-jornada-del-american-business-forum/",
    Source_Reliability="High", Methodological_Notes="No coincidio con Trump pese a versiones previas; incluyo gala CPAC en Mar-a-Lago.",
    Tema_Foro="Comercio/Integración Económica")

addm("ARG-JM-J902", Trip_Status="Completed", Start_Date="2025-11-08", End_Date="2025-11-08", Duration_Days=1,
    Destination_Country="Bolivia", Destination_City="La Paz", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Rodrigo Paz Pereira",
    Trip_Objective="Asuncion de Rodrigo Paz; reunion informal e intercambio de regalos con el nuevo presidente boliviano.",
    Source_Verification="https://www.argentina.gob.ar/noticias/el-presidente-milei-participo-de-la-asuncion-del-mandatario-electo-de-bolivia-rodrigo-paz",
    Source_Reliability="High", Methodological_Notes="Viajo directo desde EEUU.", Tema_Foro="Cooperación Política General")

addm("ARG-JM-J903", Trip_Status="Completed", Start_Date="2025-12-20", End_Date="2025-12-20", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Foz de Iguazú", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="LXVII Cumbre del MERCOSUR",
    Trip_Objective="Cumbre del MERCOSUR; pidio flexibilizacion del bloque; frio saludo con Lula, sin bilateral programada.",
    Source_Verification="https://www.argentina.gob.ar/noticias/javier-milei-emplazo-al-mercosur-definir-si-va-luchar-por-el-cambio-que-nuestros-paises",
    Source_Reliability="High", Methodological_Notes="Sin almuerzo ni bilaterales del lado argentino.", Tema_Foro="Comercio/Integración Económica")

addm("ARG-JM-J904", Trip_Status="Completed", Start_Date="2026-01-17", End_Date="2026-01-18", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Firma del acuerdo MERCOSUR-UE",
    Trip_Objective="Testigo de honor en la firma del acuerdo MERCOSUR-Union Europea; respaldo a Pena; anuncio envio al Congreso.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos/51152-discurso-del-presidente-javier-milei-durante-la-ceremonia-de-firma-del-acuerdo-entre-el-mercosur-y-la-union-europea",
    Source_Reliability="High", Methodological_Notes="Partio luego a Davos (viaje ya cargado).", Tema_Foro="Comercio/Integración Económica")

addm("ARG-JM-J905", Trip_Status="Completed", Start_Date="2026-02-18", End_Date="2026-02-19", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington DC", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Junta de la Paz (Board of Peace)",
    Trip_Objective="Primera sesion de la Junta de la Paz de Trump; ofrecio los Cascos Blancos para la reconstruccion de Gaza.",
    Source_Verification="https://www.infobae.com/politica/2026/02/19/durante-la-primera-sesion-de-la-junta-de-paz-javier-milei-ofrecio-los-cascos-blancos-para-la-reconstruccion-de-gaza/",
    Source_Reliability="High", Methodological_Notes="14º viaje a EEUU del mandato.", Tema_Foro="Seguridad")

addm("ARG-JM-J906", Trip_Status="Completed", Start_Date="2026-03-07", End_Date="2026-03-10", Duration_Days=4,
    Destination_Country="United States", Destination_City="Miami / New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre Escudo de las Américas / Argentina Week",
    Trip_Objective="Cumbre Escudo de las Americas (Doral) con almuerzo de trabajo de Trump; inauguro Argentina Week en NY.",
    Source_Verification="https://www.state.gov/translations/spanish/estados-unidos-sera-anfitrion-de-la-cumbre-escudo-de-las-americas",
    Source_Reliability="High", Methodological_Notes="Arribo a Doral el 6-mar por la noche; 16º viaje a EEUU.", Tema_Foro="Seguridad")

addm("ARG-JM-J907", Trip_Status="Completed", Start_Date="2026-03-11", End_Date="2026-03-11", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Valparaíso", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Asunción de José Antonio Kast",
    Trip_Objective="Asuncion de Kast; la bilateral prevista en Cerro Castillo se suspendio a ultimo momento.",
    Source_Verification="https://www.ambito.com/politica/javier-milei-participa-la-asuncion-jose-antonio-kast-chile-n6254788",
    Source_Reliability="High", Methodological_Notes="Bilateral con Kast cancelada por demoras.", Tema_Foro="Cooperación Política General")

addm("ARG-JM-J908", Trip_Status="Completed", Start_Date="2026-03-16", End_Date="2026-03-16", Duration_Days=1,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico de Madrid",
    Trip_Objective="Discurso de cierre del Foro Economico de Madrid ante empresarios e inversores.",
    Source_Verification="https://www.infobae.com/politica/2026/03/09/javier-milei-confirmo-su-participacion-en-el-foro-economico-de-madrid-y-suma-un-nuevo-viaje-a-espana/",
    Source_Reliability="Medium", Methodological_Notes="FUENTE-DEBIL: cobertura consultada es previa al evento; itinerario firme confirmado oficialmente. CONFIRMAR ex-post.",
    Tema_Foro="Comercio/Integración Económica")

# ---------------- LULA III (Brasil) ----------------
LULA = "Luiz Inácio Lula da Silva"
bra_rows = []; tidb = siguiente_tid("brasil")

def addl(jid, **kw):
    global tidb
    kw.setdefault("President", LULA); kw.setdefault("Origin_Country", "Brasil")
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tidb
    bra_rows.append(new_row(**kw)); tidb += 1

addl("BRA-LULA3-J900", Trip_Status="Completed", Start_Date="2025-11-21", End_Date="2025-11-23", Duration_Days=3,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XX Cumbre del G20",
    Trip_Objective="Cumbre del G20; advirtio que el foro esta amenazado; bilaterales al margen (Ramaphosa, IBSA).",
    Source_Verification="https://agenciabrasil.ebc.com.br/en/politica/noticia/2025-11/lula-arrives-south-africa-g20-summit",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

addl("BRA-LULA3-J901", Trip_Status="Completed", Start_Date="2025-11-23", End_Date="2025-11-24", Duration_Days=2,
    Destination_Country="Mozambique", Destination_City="Maputo", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Daniel Chapo",
    Trip_Objective="Visita oficial por 50 anios de relaciones; nueve acuerdos de cooperacion; Doutor Honoris Causa en Maputo.",
    Source_Verification="https://agenciabrasil.ebc.com.br/politica/noticia/2025-11/lula-recebe-titulo-de-doutor-honoris-causa-em-mocambique",
    Source_Reliability="High", Methodological_Notes="Viajo directo desde el G20.")

addl("BRA-LULA3-J902", Trip_Status="Completed", Start_Date="2026-01-27", End_Date="2026-01-28", Duration_Days=2,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Foro Económico CAF América Latina y Caribe / José Raúl Mulino",
    Trip_Objective="Abrio el Foro Economico de la CAF; visita de Estado y bilateral con Mulino; acuerdos comerciales y de inversion.",
    Source_Verification="https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2026/01/201camerica-latina-e-caribe-sao-capazes-de-construir-um-projeto-autonomo-de-insercao-internacional201d-diz-lula-no-panama",
    Source_Reliability="High", Methodological_Notes="Sustituyo a Davos, al que no fue.", Tema_Foro="Comercio/Integración Económica")

addl("BRA-LULA3-J903", Trip_Status="Completed", Start_Date="2026-02-18", End_Date="2026-02-22", Duration_Days=5,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Narendra Modi / Cumbre sobre Impacto de la IA",
    Trip_Objective="Visita de Estado; cumbre global de IA; foro empresarial; 11 acuerdos; meta comercial de USD 20000 millones.",
    Source_Verification="https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2026/02/lula-fortalece-parcerias-comerciais-e-economicas-em-viagem-a-india-e-a-coreia-do-sul",
    Source_Reliability="High", Methodological_Notes="Escala tecnica en Tunez no computa.")

addl("BRA-LULA3-J904", Trip_Status="Completed", Start_Date="2026-02-22", End_Date="2026-02-24", Duration_Days=3,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Lee Jae-myung",
    Trip_Objective="Primera visita de Estado a Corea del Sur; Plan de Accion Trienal 2026-2029; Foro Empresarial Brasil-Corea.",
    Source_Verification="https://agenciabrasil.ebc.com.br/internacional/noticia/2026-02/itamaraty-detalha-viagem-de-lula-india-e-coreia-do-sul",
    Source_Reliability="High")

addl("BRA-LULA3-J905", Trip_Status="Completed", Start_Date="2026-02-24", End_Date="2026-02-25", Duration_Days=2,
    Destination_Country="United Arab Emirates", Destination_City="Abu Dhabi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mohammed bin Zayed Al Nahyan",
    Trip_Objective="Reunion con el emir de Abu Dhabi para cerrar el giro asiatico; sin visita de Estado ni firma de acuerdos.",
    Source_Verification="https://www.poder360.com.br/poder-governo/lula-vai-a-abu-dhabi-em-escala-surpresa-para-encerrar-tour-pela-asia/",
    Source_Reliability="Medium", Methodological_Notes="FUENTE-DEBIL en fechas: estimadas; la parada era escala tecnica y se incorporo a la agenda oficial. CONFIRMAR con Itamaraty/Planalto.")

addl("BRA-LULA3-J906", Trip_Status="Completed", Start_Date="2026-03-21", End_Date="2026-03-21", Duration_Days=1,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="X Cumbre CELAC / I Foro CELAC-África",
    Trip_Objective="Cumbre de la CELAC y Foro CELAC-Africa; defensa de la soberania regional; baja adhesion de lideres.",
    Source_Verification="https://www.correiobraziliense.com.br/politica/2026/03/7381003-lula-participa-de-cupula-da-celac-e-forum-com-paises-africanos.html",
    Source_Reliability="High", Methodological_Notes="Solo 5 de los 33 jefes de Estado de la CELAC presentes.", Tema_Foro="Cooperación Política General")

# ---------------- ESCRITURA ----------------
for pais, rows in (("argentina", arg_rows), ("brasil", bra_rows)):
    path = os.path.join(MOD, pais, f"{pais}_viajes.csv")
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"{pais}: +{len(rows)} filas de brecha-critica")
print(f"TOTAL: {len(arg_rows)+len(bra_rows)} filas nuevas")
