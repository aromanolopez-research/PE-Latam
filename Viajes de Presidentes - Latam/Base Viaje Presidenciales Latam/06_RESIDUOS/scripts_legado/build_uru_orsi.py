# -*- coding: utf-8 -*-
"""
URUGUAY — Yamandu Orsi (Frente Amplio, 2025-03-01 a corte 2026-07-07). SEXTO y ULTIMO bloque uruguayo.
Investigacion dedicada (modo investigador, 2026-07-08): 18 viajes confirmados (15 journeys) + 2 cancelados.
Trip_ID 134-153. Convencion: URU-YO-JXXX. Anexa al CSV existente. COMPLETA URUGUAY.
Mandato EN CURSO: todo verificado con busqueda web activa (posterior al limite de conocimiento).
Perfil: retorno frenteamplista a diplomacia regional/ideologica (CELAC, MERCOSUR, BRICS, Democracia Siempre)
combinado con pragmatismo comercial (Panama 1er destino, visita de Estado a China, firma MERCOSUR-UE).
Tramo dic-2025/jul-2026 CERRADO: Foz de Iguazu, firma MERCOSUR-UE Asuncion, China, Kast Chile, CELAC Bogota, Luque.
NO viajo a COP30 Belem (representacion ministerial). Cancelados: CELAC-UE Santa Marta y Mundial 2026 (venia retirada).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "uruguay", "uruguay_viajes.csv")
P = "Yamandú Orsi"; O = "Uruguay"
rows = []; tid = 134

def add(jid, vs=None, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    r = new_row(**kw)
    if vs: r["Verificacion_Status"] = vs
    rows.append(r); tid += 1

add("URU-YO-J001", Trip_Status="Completed", Start_Date="2025-04-07", End_Date="2025-04-07", Duration_Days=1,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="José Raúl Mulino",
    Trip_Objective="Primer viaje oficial; apertura de mercados con delegacion arrocera; bilateral con Mulino.",
    Source_Verification="https://www.subrayado.com.uy/yamandu-orsi-se-reunio-el-presidente-panama-su-primer-viaje-oficial-queremos-ser-el-camino-la-certeza-n973872",
    Source_Reliability="High", Methodological_Notes="Primera visita de un presidente uruguayo a Panama en 17 anios; encadenado con Honduras.")

add("URU-YO-J001", Trip_Status="Completed", Start_Date="2025-04-08", End_Date="2025-04-09", Duration_Days=2,
    Destination_Country="Honduras", Destination_City="Tegucigalpa", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IX Cumbre CELAC",
    Trip_Objective="IX Cumbre CELAC; bilaterales con Petro y Castro.",
    Source_Verification="https://www.laprensa.hn/honduras/yamandu-orsi-presidente-uruguay-llega-honduras-participar-cumbre-celac-AM25295511",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-YO-J002", Trip_Status="Completed", Start_Date="2025-06-29", End_Date="2025-07-01", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Seville", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IV Conferencia ONU Financiación para el Desarrollo",
    Trip_Objective="Debate general FfD4; cena con Felipe VI y Letizia; defensa del multilateralismo.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/presidente-orsi-llego-sevilla-para-participar-conferencia-sobre-financiacion",
    Source_Reliability="High", Methodological_Notes="Llego 29-jun (cena Real Alcazar); debate 30-jun a 1-jul.", Tema_Foro="Comercio/Integración Económica")

add("URU-YO-J003", Trip_Status="Completed", Start_Date="2025-07-02", End_Date="2025-07-03", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="LXVI Cumbre MERCOSUR",
    Trip_Objective="Debut en cumbre MERCOSUR; bilateral con Milei; anuncio del acuerdo MERCOSUR-EFTA.",
    Source_Verification="https://www.ambito.com/uruguay/yamandu-orsi-debuta-su-primera-cumbre-del-mercosur-n6163189",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

add("URU-YO-J004", Trip_Status="Completed", Start_Date="2025-07-05", End_Date="2025-07-07", Duration_Days=3,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XVII Cumbre BRICS",
    Trip_Objective="Invitado por Lula; sesion sobre multilateralismo e IA; bilaterales con India, Sudafrica y Vietnam.",
    Source_Verification="https://www.elobservador.com.uy/nacional/yamandu-orsi-participo-nueva-cumbre-los-brics-brasil-las-reuniones-bilaterales-y-la-broma-lula-n6007387",
    Source_Reliability="High", Methodological_Notes="Salio 4-jul de noche.", Tema_Foro="Cooperación Política General")

add("URU-YO-J005", Trip_Status="Completed", Start_Date="2025-07-20", End_Date="2025-07-21", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Reunión de Alto Nivel 'Democracia Siempre'",
    Trip_Objective="Cumbre progresista con Boric, Lula, Petro y Sanchez; declaracion en defensa de la democracia.",
    Source_Verification="https://www.elobservador.com.uy/nacional/tras-reunion-chile-orsi-sanchez-lula-boric-y-petro-manifestaron-su-compromiso-la-defensa-la-democracia-n6009407",
    Source_Reliability="High", Methodological_Notes="Llego el domingo 20; reunion el 21 en La Moneda.", Tema_Foro="Cooperación Política General")

add("URU-YO-J006", Trip_Status="Completed", Start_Date="2025-09-21", End_Date="2025-09-24", Duration_Days=4,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="80ª Asamblea General ONU",
    Trip_Objective="Primer discurso ante la AGNU (23-sep); homenaje a Mujica en NYU (24-sep); bilateral con el BID.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/orsi-nueva-york-mujica-onu",
    Source_Reliability="High", Methodological_Notes="Viajo el domingo 21.", Tema_Foro="Cooperación Política General")

add("URU-YO-J007", vs="Solo-Query", Trip_Status="Completed", Start_Date="2025-10-15", End_Date="2025-10-15", Duration_Days=1,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Autoridades de la Unión Europea",
    Trip_Objective="Escala inicial de la gira europea; reuniones con Consejo y Parlamento Europeo por el acuerdo MERCOSUR-UE.",
    Source_Verification="https://www.elobservador.com.uy/nacional/la-gira-orsi-europa-entrega-escultura-pablo-atchugarry-y-reuniones-el-papa-leon-xiv-rey-belgica-y-autoridades-union-europea-n6019236",
    Source_Reliability="Medium", Methodological_Notes="DUDOSO: escala confirmada en previa; falta nota post-facto de Presidencia. CONFIRMAR.")

add("URU-YO-J007", Trip_Status="Completed", Start_Date="2025-10-16", End_Date="2025-10-16", Duration_Days=1,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="80º aniversario FAO / Día Mundial de la Alimentación",
    Trip_Objective="Unico jefe de Estado latinoamericano que hablo; bilaterales con Meloni y Mattarella.",
    Source_Verification="https://www.infobae.com/america/america-latina/2025/10/15/el-papa-leon-xiv-recibira-este-viernes-a-yamandu-orsi-en-el-vaticano/",
    Source_Reliability="High", Methodological_Notes="Traspaso mando a Cosse el 15-oct.", Tema_Foro="Cooperación Política General")

add("URU-YO-J007", Trip_Status="Completed", Start_Date="2025-10-17", End_Date="2025-10-17", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Papa León XIV",
    Trip_Objective="Audiencia papal; reunion con el secretario de Estado Parolin; invitacion al papa a Uruguay.",
    Source_Verification="https://www.infobae.com/america/america-latina/2025/10/17/el-papa-leon-xiv-recibio-al-presidente-orsi-en-el-vaticano/",
    Source_Reliability="High", Methodological_Notes="Dentro de la gira de Roma.")

add("URU-YO-J008", Trip_Status="Completed", Start_Date="2025-11-07", End_Date="2025-11-08", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="La Paz", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Rodrigo Paz",
    Trip_Objective="Investidura de Rodrigo Paz; bilateral con Christopher Landau (EEUU).",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/orsi-bolivia-asuncion-rodrigo-paz",
    Source_Reliability="High", Methodological_Notes="Llego 7-nov; ceremonia 8-nov.", Tema_Foro="Cooperación Política General")

add("URU-YO-J009", Trip_Status="Completed", Start_Date="2025-11-22", End_Date="2025-11-23", Duration_Days=2,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Cumbre G20",
    Trip_Objective="Uruguay como pais invitado; foto de familia y sesion plenaria Ambiente/COP30/Salud.",
    Source_Verification="https://www.swissinfo.ch/spa/ramaphosa-viaja-a-espa%C3%B1a-para-reunirse-con-el-rey-y-s%C3%A1nchez-y-asistir-a-varias-cumbres/91263363",
    Source_Reliability="Medium", Methodological_Notes="FUENTE-MEDIA: confirmado por prensa y nota de contexto de Presidencia, sin comunicado especifico del viaje.", Tema_Foro="Cooperación Política General")

add("URU-YO-J010", Trip_Status="Completed", Start_Date="2025-12-19", End_Date="2025-12-20", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Foz do Iguaçu", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="67ª Cumbre MERCOSUR",
    Trip_Objective="Traspaso PPT Brasil-Paraguay; expreso desilusion por no firmarse MERCOSUR-UE.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/orsi-cumbre-mercsosur-foz-iguazu",
    Source_Reliability="High", Methodological_Notes="Partio 19-dic; cumbre 20-dic.", Tema_Foro="Comercio/Integración Económica")

add("URU-YO-J011", Trip_Status="Completed", Start_Date="2026-01-17", End_Date="2026-01-17", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Firma del acuerdo MERCOSUR-UE",
    Trip_Objective="Ceremonia de firma del acuerdo de asociacion MERCOSUR-Union Europea.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/orsi-tras-firma-acuerdo-entre-mercosur-ue-estamos-asumiendo-responsabilidad",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

add("URU-YO-J012", Trip_Status="Completed", Start_Date="2026-02-01", End_Date="2026-02-07", Duration_Days=7,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Xi Jinping",
    Trip_Objective="Visita de Estado; mas de 30 acuerdos; delegacion de 107 empresarios; Beijing y Shanghai.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/orsi-mision-china-resultados-regreso",
    Source_Reliability="High", Methodological_Notes="Cumbre con Xi el 3-feb (38º aniversario de relaciones); incluye Shanghai 5-6 feb. Venia art.170: ausencia 29-ene a 8-feb-2026.")

add("URU-YO-J013", Trip_Status="Completed", Start_Date="2026-03-10", End_Date="2026-03-11", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Valparaíso", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de José Antonio Kast",
    Trip_Objective="Investidura de Kast; recibido por Boric el 10-mar; ceremonia el 11-mar.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/publicaciones/presidente-orsi-asuncion-jose-antonio-kast-chile",
    Source_Reliability="High", Methodological_Notes="Distinto de la recepcion a Kast en Montevideo el 1-jul-2026 (entrante, excluido).", Tema_Foro="Cooperación Política General")

add("URU-YO-J014", Trip_Status="Completed", Start_Date="2026-03-21", End_Date="2026-03-21", Duration_Days=1,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="X Cumbre CELAC / Foro CELAC-África",
    Trip_Objective="Uruguay recibe la presidencia pro tempore de la CELAC (2026-2027) de manos de Petro.",
    Source_Verification="https://mediospublicos.uy/el-presidente-orsi-recibira-en-bogota-la-presidencia-pro-tempore-de-la-celac/",
    Source_Reliability="High", Methodological_Notes="Fecha de viaje asumida el mismo dia del evento.", Tema_Foro="Cooperación Política General")

add("URU-YO-J015", Trip_Status="Completed", Start_Date="2026-06-30", End_Date="2026-06-30", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Luque", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="68ª Cumbre MERCOSUR",
    Trip_Objective="Uruguay asume la presidencia pro tempore del MERCOSUR hasta dic-2026.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/uruguay-asumio-presidencia-pro-tempore-del-mercosur-es-verdadero-orgullo",
    Source_Reliability="High", Methodological_Notes="Antes del corte 2026-07-07.", Tema_Foro="Comercio/Integración Económica")

add("URU-YO-J016", Trip_Status="Canceled", Start_Date="2025-11-09", End_Date="NA", Duration_Days="NA",
    Destination_Country="Colombia", Destination_City="Santa Marta", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IV Cumbre CELAC-UE",
    Trip_Objective="Objetivo: cumbre birregional CELAC-UE. Cancelacion: priorizo la asuncion de Paz en Bolivia; envio al canciller Lubetkin.",
    Source_Verification="https://cnnespanol.cnn.com/2025/11/09/latinoamerica/nueve-jefes-estado-gobierno-cumbre-celac-ue-colombia-efe",
    Source_Reliability="High", Methodological_Notes="Asistencia confirmada por Colombia y luego no concretada.", Tema_Foro="Cooperación Política General")

add("URU-YO-J017", Trip_Status="Canceled", Start_Date="2026-06-13", End_Date="NA", Duration_Days="NA",
    Destination_Country="United States", Destination_City="Miami", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mundial FIFA 2026",
    Trip_Objective="Objetivo: asistir al Mundial 2026. Cancelacion: retiro la venia por razones de fuerza mayor el 8-jun-2026.",
    Source_Verification="https://www.telenoche.com.uy/nacionales/yamandu-orsi-retiro-la-solicitud-viajar-al-mundial-2026-y-no-se-ausentara-del-pais-la-proxima-semana-n5400598",
    Source_Reliability="High", Methodological_Notes="Venia solicitada 4-jun y retirada 8-jun-2026; caracter cuasi-personal.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
print(f"OK: {len(rows)} filas de {P} anexadas. Ultimo Trip_ID = {tid-1}")
