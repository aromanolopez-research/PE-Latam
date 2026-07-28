# -*- coding: utf-8 -*-
"""
CHILE — Sebastián Piñera, SEGUNDO MANDATO (11/3/2018 a 11/3/2022, Chile Vamos). Bloque separado del 1ro.
Continua Trip_ID tras Bachelet 2 (ultimo=110). Journey continua en CHL-SP2-J101.
Modo research (2026-07-06): 15 viajes fisicos completados (26 filas pais) + 4 cancelados.
Perfil: arranque hiperactivo 2018-2019 (Cumbre Americas, 2 G20, APEC, 1er chileno invitado al G7,
visita de Estado a China / unico latinoamericano en Franja y la Ruta II, Cucuta) cortado por el
estallido social (18-O) y la pandemia: apagon total mar-2020 a ago-2021; rebrote final sep-2021/ene-2022.
Cumbres VIRTUALES no cuentan como viaje (AGNU 2020-2021, Iberoamericana Andorra 2021, cumbres climaticas Biden).
Excluidos por ser en Chile: fundacion PROSUR (Santiago mar-2019); APEC/COP25 canceladas como SEDE (no son viajes).
CORRECCION DOCTRINARIA vs informe research: G20 -> Cooperacion Politica General (CODEBOOK 5.7), no Comercio.
Gira europea cancelada jun-2021: multi-pais con destinos confirmados -> una fila Canceled por destino (mismo Journey).
Brechas documentadas en PENDIENTES_VERIFICACION.txt.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "chile", "chile_viajes.csv")
P = "Sebastián Piñera"; O = "Chile"
rows = []; tid = 111

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2018 (desde 11/3) =====
add("CHL-SP2-J101", Trip_Status="Completed", Start_Date="2018-04-13", End_Date="2018-04-14", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VIII Cumbre de las Américas",
    Trip_Objective="Cumbre sobre gobernabilidad y corrupcion; bilaterales con Santos, Temer, Moise, Holness y Pence.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=73268",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-SP2-J102", Trip_Status="Completed", Start_Date="2018-04-25", End_Date="2018-04-26", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mauricio Macri",
    Trip_Objective="Primera gira del mandato; agenda energetica, comercial e integracion Mercosur-Alianza del Pacifico.",
    Source_Verification="https://minrel.gob.cl/minrel/noticias-anteriores/comunicado-conjunto-de-la-visita-oficial-a-la-republica-argentina-del",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-SP2-J102", Trip_Status="Completed", Start_Date="2018-04-27", End_Date="2018-04-27", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Michel Temer",
    Trip_Objective="Respaldo a Temer; situacion de Venezuela y acercamiento comercial.",
    Source_Verification="https://www.perfil.com/noticias/politica/sebastian-pinera-inicia-su-primera-gira-internacional-en-argentina.phtml",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("CHL-SP2-J103", Trip_Status="Completed", Start_Date="2018-09-25", End_Date="2018-09-27", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="73ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante AGNU; bilaterales con Trudeau, Ardern, Moon, Tusk y Guterres.",
    Source_Verification="https://www.gob.cl/noticias/presidente-pinera-en-la-onu-y-agenda-de-reuniones-con-organismos-internacionales-estamos-tratando-temas-que-chile-le-interesan-y-preocupan/",
    Source_Reliability="High", Methodological_Notes="Fechas de estancia estimadas.", Tema_Foro="Cooperación Política General")

add("CHL-SP2-J103", Trip_Status="Completed", Start_Date="2018-09-28", End_Date="2018-09-28", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington DC", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump",
    Trip_Objective="Reunion en la Casa Blanca; Venezuela, comercio, energia y ciberseguridad.",
    Source_Verification="https://www.latercera.com/politica/noticia/trump-recibe-pinera-la-casa-blanca/334525/",
    Source_Reliability="High", Methodological_Notes="Mismo Journey que AGNU (una salida fisica).")

add("CHL-SP2-J104", Trip_Status="Completed", Start_Date="2018-11-17", End_Date="2018-11-18", Duration_Days=2,
    Destination_Country="Papua New Guinea", Destination_City="Port Moresby", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre APEC 2018",
    Trip_Objective="Foro APEC; libre comercio y guerra comercial EEUU-China.",
    Source_Verification="https://en.wikipedia.org/wiki/APEC_Papua_New_Guinea_2018",
    Source_Reliability="Medium", Methodological_Notes="Fechas de estancia estimadas.", Tema_Foro="Comercio/Integración Económica")

add("CHL-SP2-J105", Trip_Status="Completed", Start_Date="2018-11-30", End_Date="2018-12-01", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Buenos Aires (invitado)",
    Trip_Objective="Chile pais invitado; defensa del libre comercio y del multilateralismo.",
    Source_Verification="https://www.latercera.com/politica/noticia/pinera-asegura-se-creo-clima-mayor-dialogo-mejor-voluntad-cumbre-del-g20/426723/",
    Source_Reliability="High", Methodological_Notes="Tema G20 -> Cooperacion Politica General por doctrina CODEBOOK 5.7 (corregido vs informe research).",
    Tema_Foro="Cooperación Política General")

# ===== 2019 =====
add("CHL-SP2-J106", Trip_Status="Completed", Start_Date="2019-01-01", End_Date="2019-01-01", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Jair Bolsonaro",
    Trip_Objective="Cambio de mando; bilaterales con Bolsonaro y Abdo Benitez; anuncio de TLC Chile-Brasil.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=89377",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-SP2-J107", Trip_Status="Completed", Start_Date="2019-02-22", End_Date="2019-02-23", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Cúcuta", Visit_Category="Multilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Iván Duque / Venezuela Aid Live",
    Trip_Objective="Entrega de ayuda humanitaria para Venezuela junto a Duque, Abdo y Guaido; operativo fronterizo.",
    Source_Verification="https://www.emol.com/noticias/Nacional/2019/02/24/938942/El-breve-pero-intenso-paso-de-Pinera-por-Cucuta-Del-accidentado-viaje-al-envio-de-ayuda-humanitaria.html",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-SP2-J108", Trip_Status="Completed", Start_Date="2019-04-23", End_Date="2019-04-23", Duration_Days=1,
    Destination_Country="Singapore", Destination_City="Singapore", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Singapur",
    Trip_Objective="Escala de la gira asiatica; comercio e innovacion.",
    Source_Verification="https://www.france24.com/es/20190505-chile-china-pinera-xi-huawei",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; France24 lista Singapur-China-Corea, sugiere primera parada; confirmar orden.")

add("CHL-SP2-J108", Trip_Status="Completed", Start_Date="2019-04-24", End_Date="2019-04-28", Duration_Days=5,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Xi Jinping / II Foro de la Franja y la Ruta",
    Trip_Objective="Visita de Estado; hoja de ruta estrategica 2019-2022; unico lider latinoamericano en Franja y la Ruta II.",
    Source_Verification="https://www.emol.com/noticias/Nacional/2019/04/24/945654/Pinera-tras-bilateral-con-Xi-Jinping-China-es-nuestro-principal-socio-comercial-y-queremos-estrechar-los-lazos-en-otros-frentes.html",
    Source_Reliability="High", Methodological_Notes="Incluye Beijing y Shenzhen. Categoria Bilateral (primario: visita de Estado); Foro FyR anotado como evento.")

add("CHL-SP2-J108", Trip_Status="Completed", Start_Date="2019-04-29", End_Date="2019-04-29", Duration_Days=1,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Corea del Sur",
    Trip_Objective="Segunda escala de la gira asiatica; inversiones y tecnologia.",
    Source_Verification="https://www.france24.com/es/20190505-chile-china-pinera-xi-huawei",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada.")

add("CHL-SP2-J109", Trip_Status="Completed", Start_Date="2019-06-28", End_Date="2019-06-29", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Osaka", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del G20 de Osaka (invitado)",
    Trip_Objective="Chile invitado; guerra comercial, cambio climatico y preparacion APEC/COP25.",
    Source_Verification="https://www.latercera.com/politica/noticia/diseno-pinera-la-cumbre-del-g20/688711/",
    Source_Reliability="High", Methodological_Notes="Tema G20 -> Cooperacion Politica General por doctrina CODEBOOK 5.7 (corregido vs informe research).",
    Tema_Foro="Cooperación Política General")

add("CHL-SP2-J110", Trip_Status="Completed", Start_Date="2019-08-24", End_Date="2019-08-26", Duration_Days=3,
    Destination_Country="France", Destination_City="Biarritz", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="45ª Cumbre del G7 (invitado)",
    Trip_Objective="Primer mandatario chileno invitado al G7; coordina con Macron la respuesta a los incendios amazonicos.",
    Source_Verification="https://prensa.presidencia.cl/fotonoticia.aspx?id=96161",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-SP2-J110", Trip_Status="Completed", Start_Date="2019-08-28", End_Date="2019-08-28", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jair Bolsonaro",
    Trip_Objective="Escala tras el G7; coordinacion de ayuda amazonica y reunion de lideres.",
    Source_Verification="https://www.t13.cl/noticia/politica/mundo/pinera-visita-bolsonaro-brasil-su-paso-cumbre-g7",
    Source_Reliability="High", Methodological_Notes="Escala en Portugal considerada tecnica (sin actividad diplomatica documentada); ver pendientes.")

add("CHL-SP2-J111", Trip_Status="Completed", Start_Date="2019-09-23", End_Date="2019-09-25", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="74ª Asamblea General de la ONU + Cumbre de Acción Climática",
    Trip_Objective="Discurso ante AGNU; agenda climatica pre-COP25 y crisis venezolana.",
    Source_Verification="https://www.latercera.com/politica/noticia/la-intervencion-pinera-la-asamblea-la-onu-respondio-trump-no-ninguna-incompatibilidad-pensar-mundo-global-patriota/833135/",
    Source_Reliability="High", Methodological_Notes="Fechas de estancia estimadas. Ultimo viaje antes del estallido social (18-O).",
    Tema_Foro="Cooperación Política General")

# ===== 2020 (cierre pre-pandemia) =====
add("CHL-SP2-J112", Trip_Status="Completed", Start_Date="2020-03-01", End_Date="2020-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Luis Lacalle Pou",
    Trip_Objective="Cambio de mando; bilaterales con el rey Felipe VI y Duque; ultimo viaje pre-pandemia.",
    Source_Verification="https://www.chile.gob.cl/uruguay/noticias/presidente-pinera-participa-en-ceremonia-de-transmision-del-mando",
    Source_Reliability="High", Methodological_Notes="Viaja y regresa el mismo dia. Primer viaje tras el 18-O.",
    Tema_Foro="Cooperación Política General")

# ===== 2021 (rebrote presencial) =====
add("CHL-SP2-J113", Trip_Status="Completed", Start_Date="2021-09-05", End_Date="2021-09-06", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Retoma agenda internacional; ciberseguridad, energias limpias y agenda pre-COP26.",
    Source_Verification="https://www.latercera.com/politica/noticia/gira-europea-pinera-se-reune-con-rey-felipe-vi-y-el-presidente-espanol-pedro-sanchez/W7VG5YG5AFEQVIC5PMAUZ6O6QA/",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada (reunion con Macron ~6/9).")

add("CHL-SP2-J113", Trip_Status="Completed", Start_Date="2021-09-07", End_Date="2021-09-07", Duration_Days=1,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rey Felipe VI / Pedro Sánchez",
    Trip_Objective="Visita oficial; relacion bilateral, acuerdo con la UE y proceso constituyente.",
    Source_Verification="https://www.lamoncloa.gob.es/presidente/actividades/paginas/2021/070921-sanchez-pinera.aspx",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-SP2-J113", Trip_Status="Completed", Start_Date="2021-09-08", End_Date="2021-09-08", Duration_Days=1,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Sergio Mattarella / Mario Draghi",
    Trip_Objective="Reuniones bilaterales; cooperacion y agenda climatica.",
    Source_Verification="https://prensa.presidencia.cl/fotonoticia.aspx?id=179522",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("CHL-SP2-J113", Trip_Status="Completed", Start_Date="2021-09-09", End_Date="2021-09-09", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Papa Francisco",
    Trip_Objective="Coloquio privado de una hora con el papa Francisco; reunion con el cardenal Parolin.",
    Source_Verification="https://www.vaticannews.va/es/papa/news/2021-09/papa-francisco-audiencia-presidente-chile-pinera-echenique.html",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-SP2-J113", Trip_Status="Completed", Start_Date="2021-09-09", End_Date="2021-09-10", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Boris Johnson",
    Trip_Objective="Cierre de gira; pandemia y transicion de la presidencia COP25 a COP26.",
    Source_Verification="https://www.gov.uk/government/news/pm-meeting-with-chilean-president-sebastian-pinera-10-september-2021.es-419",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-SP2-J114", Trip_Status="Completed", Start_Date="2021-09-24", End_Date="2021-09-26", Duration_Days=3,
    Destination_Country="Colombia", Destination_City="Cartagena de Indias", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Iván Duque",
    Trip_Objective="Visita oficial; Alianza del Pacifico, PROSUR, tratado de extradicion y proceso de paz.",
    Source_Verification="https://www.minrel.gob.cl/noticias-anteriores/canciller-participa-en-gira-del-presidente-pinera-para-fortalecer-lazos",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-SP2-J114", Trip_Status="Completed", Start_Date="2021-09-26", End_Date="2021-09-27", Duration_Days=2,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Luis Lacalle Pou",
    Trip_Objective="Visita oficial; manejo de pandemia, vacunacion y MOU de salud.",
    Source_Verification="https://prensa.presidencia.cl/fotonoticia.aspx?id=180591",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-SP2-J114", Trip_Status="Completed", Start_Date="2021-09-28", End_Date="2021-09-28", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mario Abdo Benítez",
    Trip_Objective="Cierre de gira; donacion de 100000 dosis AstraZeneca y acuerdo de complementacion economica.",
    Source_Verification="https://www.minrel.gob.cl/noticias-anteriores/canciller-participa-en-gira-del-presidente-pinera-para-fortalecer-lazos",
    Source_Reliability="High", Methodological_Notes="Fecha estimada.")

# ===== 2022 (hasta 11/3) =====
add("CHL-SP2-J115", Trip_Status="Completed", Start_Date="2022-01-26", End_Date="2022-01-27", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Bahía Málaga / Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XVI Cumbre Alianza del Pacífico / III Cumbre PROSUR",
    Trip_Objective="Ultimo viaje del mandato; ingreso de Singapur como Estado Asociado y cumbre de PROSUR.",
    Source_Verification="https://www.chile.gob.cl/colombia/noticias/visita-oficial-del-presidente-de-la-republica-para-participar-en-la-xvi",
    Source_Reliability="High", Methodological_Notes="Evento primario: Alianza del Pacifico (regla de evento combinado).",
    Tema_Foro="Comercio/Integración Económica")

# ===== CANCELADOS =====
add("CHL-SP2-J116", Trip_Status="Canceled", Start_Date="2019-12-02", End_Date="NA", Duration_Days="NA",
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="COP25",
    Trip_Objective="Presidir la cumbre climatica (reubicada de Santiago a Madrid tras el 18-O); no asistio, priorizando la crisis domestica.",
    Source_Verification="https://www.elmostrador.cl/dia/2019/11/27/sebastian-pinera-no-acudira-a-la-cop25-que-se-desarrollara-en-madrid/",
    Source_Reliability="High", Methodological_Notes="Chile mantuvo la presidencia de la COP; asistio la ministra Schmidt.",
    Tema_Foro="Medio Ambiente/Clima")

add("CHL-SP2-J117", Trip_Status="Canceled", Start_Date="2019-12-10", End_Date="NA", Duration_Days="NA",
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Alberto Fernández",
    Trip_Objective="Asistir al cambio de mando; cancelado tras el accidente del Hercules C-130 de la FACh y el contexto del estallido social.",
    Source_Verification="https://www.emol.com/noticias/Internacional/2020/03/01/978135/Luis-Lacalle-Uruguay-elecciones-Presidente.html",
    Source_Reliability="Medium", Methodological_Notes="Confirmar fecha y comunicado exacto de la cancelacion (fuente indirecta).",
    Tema_Foro="Cooperación Política General")

# Gira europea cancelada por COVID (jun-2021): multi-pais planificado con destinos confirmados
# por prensa -> una fila Canceled por destino, mismo Journey_ID (regla: una fila por pais).
_gira_jun2021 = [
    ("Italy", "Rome", "Sergio Mattarella / Mario Draghi"),
    ("Vatican City", "Vatican City", "Papa Francisco"),
    ("United Kingdom", "London", "Boris Johnson"),
    ("Spain", "Madrid", "Rey Felipe VI / Pedro Sánchez"),
    ("France", "Paris", "Emmanuel Macron"),
]
for pais, ciudad, contraparte in _gira_jun2021:
    add("CHL-SP2-J118", Trip_Status="Canceled", Start_Date="2021-06-22", End_Date="NA", Duration_Days="NA",
        Destination_Country=pais, Destination_City=ciudad, Visit_Category="Bilateral", Visit_Subtype="Working Visit",
        Sideline_Bilaterals="NA", Counterpart_Event=contraparte,
        Trip_Objective="Gira europea para retomar agenda internacional; cancelada por alza de casos COVID-19 y cuarentena de la RM.",
        Source_Verification="https://www.latercera.com/la-tercera-pm/noticia/como-se-gesto-y-cayo-la-gira-de-pinera-a-europa-y-su-frustrada-apuesta-por-retomar-la-agenda-internacional/RNKMRAIFHNBBBIITU4OAYRZR7E/",
        Source_Reliability="High",
        Methodological_Notes="Fecha estimada (gira planificada ~22/6/2021). Reprogramada y concretada en sep-2021 (J113).")

add("CHL-SP2-J119", Trip_Status="Canceled", Start_Date="2021-11-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="United Kingdom", Destination_City="Glasgow", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="COP26",
    Trip_Objective="Asistir a la cumbre climatica; no viajo y envio a la ministra Schmidt para la entrega de la presidencia de la COP.",
    Source_Verification="https://www.gob.cl/noticias/chile-entrega-presidencia-de-la-cop-y-ministra-schmidt-destaca-impulso-la-accion-climatica-en-el-pais/",
    Source_Reliability="Medium", Methodological_Notes="Sin comunicado oficial con justificacion textual de la inasistencia (BRECHA en pendientes).",
    Tema_Foro="Medio Ambiente/Clima")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (2do mandato) agregadas. Ultimo Trip_ID = {tid-1}")
