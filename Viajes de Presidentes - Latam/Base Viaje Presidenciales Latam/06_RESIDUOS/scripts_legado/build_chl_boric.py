# -*- coding: utf-8 -*-
"""
CHILE — Gabriel Boric (11/3/2022 a 11/3/2026, Apruebo Dignidad/FA). Sexto bloque chileno.
Continua Trip_ID tras Pinera 2 (ultimo=144). Journey continua en CHL-GB-J120.
Modo research (2026-07-07): 31 viajes fisicos completados (40 filas pais) + 1 cancelado (COP28).
Perfil: presidente muy viajero (sin pandemia activa), multilateralista y latinoamericanista.
AGNU los 4 anios; APEC x3; G20 y BRICS como invitado; COP30; 7 asunciones regionales.
Dos aperturas asiaticas de peso: China 2023 (Estado + Franja y la Ruta III) y 2025; India 2025 (Estado, CEPA).
Relacion con Argentina: calida con Fernandez (1er viaje, tradicion), fria con Milei (sin bilaterales tras dic-2023).
2026 (ene-11/mar): sin viajes confirmados (verificar con decretos de ausencia al cerrar el pais).
NO cargados (envio delegacion, no viajo): funeral papa Francisco (abr-2025), CELAC Tegucigalpa (abr-2025),
Conferencia Oceanos Niza (jun-2025), CELAC-UE Santa Marta (nov-2025). Virtuales no cuentan.
AJUSTES vs informe research (documentados en bitacora):
 - Sideline_Bilaterals=FALSE sin evidencia explicita -> NA (regla CODEBOOK 5.4: FALSE requiere evidencia directa).
 - Cumbre por la Paz en Ucrania (Burgenstock 2024) -> Tema_Foro=Seguridad (guerra/paz), no Coop. Politica Gral.
Brechas documentadas en PENDIENTES_VERIFICACION.txt (2022: 6-7 journeys aqui vs 8 en conteo de prensa).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "chile", "chile_viajes.csv")
P = "Gabriel Boric"; O = "Chile"
rows = []; tid = 145

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2022 (desde 11/3) =====
add("CHL-GB-J120", Trip_Status="Completed", Start_Date="2022-04-03", End_Date="2022-04-05", Duration_Days=3,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Alberto Fernández",
    Trip_Objective="Primer viaje oficial (tradicion del primer destino); cooperacion energetica, DDHH, genero y comercio.",
    Source_Verification="https://www.latercera.com/politica/noticia/boric-inicia-visita-de-estado-en-argentina-con-foco-en-cooperacion-economica-y-no-se-reuniria-con-cristina-fernandez/4RHD7F6WTVFPVJPXWI5MGKCOPU/",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-GB-J121", Trip_Status="Completed", Start_Date="2022-06-05", End_Date="2022-06-06", Duration_Days=2,
    Destination_Country="Canada", Destination_City="NA", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Justin Trudeau",
    Trip_Objective="Etapa canadiense de la gira norteamericana previa a la Cumbre de las Americas; reunion con Trudeau.",
    Source_Verification="https://www.lanacion.cl/ix-cumbres-de-las-americas-presidente-boric-ya-arribo-a-los-angeles/",
    Source_Reliability="Low", Methodological_Notes="Ciudad no confirmada; etapa reportada pero no plenamente verificada (FUENTE-DEBIL en pendientes).")

add("CHL-GB-J121", Trip_Status="Completed", Start_Date="2022-06-07", End_Date="2022-06-10", Duration_Days=4,
    Destination_Country="United States", Destination_City="Los Angeles", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IX Cumbre de las Américas",
    Trip_Objective="IX Cumbre de las Americas; bilateral con Biden y lanzamiento de coalicion oceanica.",
    Source_Verification="https://www.cooperativa.cl/noticias/pais/presidente-boric/viajes-al-exterior/boric-ya-esta-en-los-angeles-para-asistir-a-la-cumbre-de-las-americas-y/2022-06-06/114143.html",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-GB-J122", Trip_Status="Completed", Start_Date="2022-08-06", End_Date="2022-08-08", Duration_Days=3,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Gustavo Petro",
    Trip_Objective="Transmision de mando de Petro; bilaterales con Petro y Arce.",
    Source_Verification="https://www.chile.gob.cl/colombia/noticias/el-presidente-de-chile-gabriel-boric-participo-en-la-transmision-del",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-GB-J123", Trip_Status="Completed", Start_Date="2022-09-19", End_Date="2022-09-21", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="77ª Asamblea General de la ONU",
    Trip_Objective="Discurso debut ante la AGNU; bilaterales con Sanchez y Macron.",
    Source_Verification="https://www.emol.com/noticias/Nacional/2022/09/18/1073204/viaje-boric-asamblea-general-onu.html",
    Source_Reliability="Medium", Methodological_Notes="Fechas de estancia estimadas; discurso el 20/9/2022.",
    Tema_Foro="Cooperación Política General")

add("CHL-GB-J124", Trip_Status="Completed", Start_Date="2022-11-16", End_Date="2022-11-19", Duration_Days=4,
    Destination_Country="Thailand", Destination_City="Bangkok", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre APEC 2022",
    Trip_Objective="Debut en APEC; bilaterales con Xi Jinping, Kishida y Trudeau; agenda TPP11.",
    Source_Verification="https://www.emol.com/noticias/Nacional/2022/11/16/1078523/presidente-apec-tailandia.html",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Comercio/Integración Económica")

add("CHL-GB-J125", Trip_Status="Completed", Start_Date="2022-11-22", End_Date="2022-11-24", Duration_Days=3,
    Destination_Country="Mexico", Destination_City="Ciudad de México", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Andrés Manuel López Obrador",
    Trip_Objective="Visita oficial; reunion con AMLO, sesion solemne del Senado y promocion de inversiones.",
    Source_Verification="https://www.chile.gob.cl/mexico/noticias/presidente-gabriel-boric-realiza-visita-oficial-a-mexico",
    Source_Reliability="High", Methodological_Notes="NA")

# ===== 2023 =====
add("CHL-GB-J126", Trip_Status="Completed", Start_Date="2023-01-01", End_Date="2023-01-01", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Luiz Inácio Lula da Silva",
    Trip_Objective="Investidura de Lula.",
    Source_Verification="Search Query: Boric asuncion Lula enero 2023 Brasilia",
    Source_Reliability="Medium", Methodological_Notes="Estancia estimada; confirmar contra decreto de ausencia (pendientes).",
    Tema_Foro="Cooperación Política General")

add("CHL-GB-J127", Trip_Status="Completed", Start_Date="2023-01-24", End_Date="2023-01-24", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="VII Cumbre de la CELAC",
    Trip_Objective="Participacion en la VII Cumbre de la CELAC.",
    Source_Verification="https://www.infobae.com/america/agencias/2023/01/20/lula-petro-y-boric-entre-los-asistentes-a-la-cumbre-de-la-celac-que-promete-ser-tensa/",
    Source_Reliability="Medium", Methodological_Notes="Estancia estimada.", Tema_Foro="Cooperación Política General")

add("CHL-GB-J128", Trip_Status="Completed", Start_Date="2023-03-24", End_Date="2023-03-25", Duration_Days=2,
    Destination_Country="Dominican Republic", Destination_City="Santo Domingo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XXVIII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Santo Domingo.",
    Source_Verification="Search Query: Boric Cumbre Iberoamericana Santo Domingo marzo 2023",
    Source_Reliability="Medium", Methodological_Notes="Confirmado por prensa retrospectiva (Emol 15/11/2023); fechas estimadas.",
    Tema_Foro="Cooperación Política General")

add("CHL-GB-J129", Trip_Status="Completed", Start_Date="2023-05-29", End_Date="2023-05-30", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre de presidentes sudamericanos (retiro convocado por Lula)",
    Trip_Objective="Cumbre sudamericana convocada por Lula; retorno el 30/5 para preparar la Cuenta Publica.",
    Source_Verification="https://www.elmostrador.cl/noticias/pais/2023/05/30/presidente-boric-aterriza-en-brasil-para-reunion-convocada-por-lula-con-mandatarios-de-sudamerica/",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-GB-J130", Trip_Status="Completed", Start_Date="2023-07-13", End_Date="2023-07-15", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Pedro Sánchez / Rey Felipe VI",
    Trip_Objective="Primera gira europea; agenda economica, litio e inversion; conmemoracion 50 anios del golpe.",
    Source_Verification="https://www.df.cl/economia-y-politica/gobierno/boric-inicia-gira-en-madrid-donde-busca-consolidar-a-espana-como-tercer",
    Source_Reliability="High", Methodological_Notes="Parte de gira europea multi-pais (J130).")

add("CHL-GB-J130", Trip_Status="Completed", Start_Date="2023-07-17", End_Date="2023-07-18", Duration_Days=2,
    Destination_Country="Belgium", Destination_City="Bruselas", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="III Cumbre UE-CELAC",
    Trip_Objective="Cumbre UE-CELAC; agenda de bilaterales con lideres europeos y latinoamericanos.",
    Source_Verification="https://www.elmostrador.cl/noticias/pais/2023/07/13/presidente-boric-viaja-a-espana-para-su-primera-gira-europea-que-incluye-belgica-suiza-y-francia/",
    Source_Reliability="High", Methodological_Notes="Cifra de ~15 bilaterales citada por el canciller, sin registro oficial verificable.",
    Tema_Foro="Cooperación Política General")

add("CHL-GB-J130", Trip_Status="Completed", Start_Date="2023-07-19", End_Date="2023-07-20", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Ginebra", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="CERN / OMS (Tedros Adhanom)",
    Trip_Objective="Visita al CERN (Chile miembro asociado) y encuentro con el director general de la OMS.",
    Source_Verification="https://www.emol.com/noticias/Nacional/2023/07/07/1100363/gira-europa-presidente-gabriel-boric.html",
    Source_Reliability="High", Methodological_Notes="Fechas estimadas dentro de la gira. Visita a organismos, no bilateral pais-pais: Other.")

add("CHL-GB-J130", Trip_Status="Completed", Start_Date="2023-07-21", End_Date="2023-07-21", Duration_Days=1,
    Destination_Country="France", Destination_City="París", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Cierre de la gira europea; bilateral con Macron.",
    Source_Verification="https://www.emol.com/noticias/Nacional/2023/07/07/1100363/gira-europa-presidente-gabriel-boric.html",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-GB-J131", Trip_Status="Completed", Start_Date="2023-08-14", End_Date="2023-08-15", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Santiago Peña",
    Trip_Objective="Cambio de mando de Penia; viajo junto al expresidente Pinera.",
    Source_Verification="https://minrel.gob.cl/noticias-anteriores/canciller-alberto-van-klaveren-acompana-al-presidente-boric-en-cambio-de",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-GB-J132", Trip_Status="Completed", Start_Date="2023-09-19", End_Date="2023-09-20", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="78ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la AGNU; bilaterales con Trudeau, Boluarte y Zelenski.",
    Source_Verification="https://www.chile.gob.cl/onu/noticias/78-asamblea-general-presidente-de-la-republica-gabriel-boric-font",
    Source_Reliability="High", Methodological_Notes="Discurso el 20/9/2023; posible escala en Washington 22-23/9 no confirmada (pendientes).",
    Tema_Foro="Cooperación Política General")

add("CHL-GB-J133", Trip_Status="Completed", Start_Date="2023-10-14", End_Date="2023-10-18", Duration_Days=5,
    Destination_Country="China", Destination_City="Chengdú / Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Xi Jinping / III Foro de la Franja y la Ruta",
    Trip_Objective="Visita de Estado; III Foro Franja y la Ruta; reunion con Xi; Chile Week China.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=273070",
    Source_Reliability="High", Methodological_Notes="Categoria Bilateral (primario: visita de Estado); foro FyR al margen. Precedente: Pinera 2019 (J108).")

add("CHL-GB-J134", Trip_Status="Completed", Start_Date="2023-11-02", End_Date="2023-11-03", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington DC", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre APEP",
    Trip_Objective="Cumbre de la Alianza para la Prosperidad Economica de las Americas; bilateral con Biden en la Casa Blanca.",
    Source_Verification="https://www.larepublica.ec/blog/2023/11/01/boric-viaja-a-la-apep-el-foro-organizado-por-biden-en-seguimiento-a-la-cumbre-de-las-americas/",
    Source_Reliability="High", Methodological_Notes="APEP: mandato fundacional economico-comercial (doctrina 5.7).",
    Tema_Foro="Comercio/Integración Económica")

add("CHL-GB-J135", Trip_Status="Completed", Start_Date="2023-11-15", End_Date="2023-11-16", Duration_Days=2,
    Destination_Country="United States", Destination_City="San Francisco", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre APEC 2023",
    Trip_Objective="Cumbre APEC; CEO Summit y plenario de lideres; agenda de inversion.",
    Source_Verification="https://cooperativa.cl/noticias/pais/presidente-boric/viajes-al-exterior/presidente-boric-ya-esta-en-eeuu-para-participar-de-cumbre-apec/2023-11-15/141311.html",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Comercio/Integración Económica")

add("CHL-GB-J136", Trip_Status="Completed", Start_Date="2023-12-09", End_Date="2023-12-10", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Javier Milei",
    Trip_Objective="Investidura de Milei pese a diferencias ideologicas; breve saludo protocolar.",
    Source_Verification="https://www.cnnchile.com/pais/boric-llega-argentina-asuncion-milei_20231209/",
    Source_Reliability="High", Methodological_Notes="Ultima visita a Argentina del mandato (relacion fria con Milei).",
    Tema_Foro="Cooperación Política General")

add("CHL-GB-J137", Trip_Status="Canceled", Start_Date="2023-11-30", End_Date="NA", Duration_Days="NA",
    Destination_Country="United Arab Emirates", Destination_City="Dubái", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="COP28",
    Trip_Objective="Participar en la COP28; cancelado el 22/11/2023 por agenda de seguridad interna; asistieron el canciller van Klaveren y la ministra Rojas.",
    Source_Verification="https://www.emol.com/noticias/Nacional/2023/11/22/1113662/boric-desiste-de-cop28.html",
    Source_Reliability="Medium", Methodological_Notes="Fecha de inicio estimada segun planificacion original.",
    Tema_Foro="Medio Ambiente/Clima")

# ===== 2024 =====
add("CHL-GB-J138", Trip_Status="Completed", Start_Date="2024-01-14", End_Date="2024-01-15", Duration_Days=2,
    Destination_Country="Guatemala", Destination_City="Ciudad de Guatemala", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Bernardo Arévalo",
    Trip_Objective="Investidura de Arevalo; bilaterales con Arevalo y Josep Borrell (UE).",
    Source_Verification="https://cooperativa.cl/noticias/pais/presidente-boric/viajes-al-exterior/boric-viaja-a-guatemala-para-asistir-a-la-toma-de-posesion-de-arevalo/2024-01-13/182729.html",
    Source_Reliability="High", Methodological_Notes="NA", Tema_Foro="Cooperación Política General")

add("CHL-GB-J139", Trip_Status="Completed", Start_Date="2024-06-10", End_Date="2024-06-12", Duration_Days=3,
    Destination_Country="Germany", Destination_City="Berlín", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Olaf Scholz / Frank-Walter Steinmeier",
    Trip_Objective="Segunda gira europea; visita oficial, ESO en Munich, inversion y ciencia.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=285010",
    Source_Reliability="High", Methodological_Notes="Fechas estimadas dentro de la gira (J139).")

add("CHL-GB-J139", Trip_Status="Completed", Start_Date="2024-06-13", End_Date="2024-06-14", Duration_Days=2,
    Destination_Country="Sweden", Destination_City="Estocolmo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Ulf Kristersson / Rey Carlos XVI Gustavo",
    Trip_Objective="Visita oficial a Suecia; agenda economica y de innovacion.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=285010",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas.")

add("CHL-GB-J139", Trip_Status="Completed", Start_Date="2024-06-15", End_Date="2024-06-16", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Bürgenstock", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre por la Paz en Ucrania",
    Trip_Objective="Participacion en la Cumbre por la Paz en Ucrania.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=285010",
    Source_Reliability="High", Methodological_Notes="Tema Seguridad (guerra/paz), decision doctrinaria 2026-07-07 (vs Coop. Politica Gral. del informe research).",
    Tema_Foro="Seguridad")

add("CHL-GB-J139", Trip_Status="Completed", Start_Date="2024-06-17", End_Date="2024-06-18", Duration_Days=2,
    Destination_Country="France", Destination_City="París", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Cierre de gira; evento de alto nivel sobre educacion (ODS4) y bilateral con Macron.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=285010",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas.")

add("CHL-GB-J140", Trip_Status="Completed", Start_Date="2024-07-16", End_Date="2024-07-17", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Santiago Peña",
    Trip_Objective="Visita oficial; agenda comercial y Corredor Bioceanico Vial; discurso ante el Congreso.",
    Source_Verification="https://cooperativa.cl/noticias/pais/presidente-boric/viajes-al-exterior/pendiente-de-la-crisis-de-seguridad-boric-inicia-su-visita-en-paraguay/2024-07-16/225224.html",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-GB-J141", Trip_Status="Completed", Start_Date="2024-09-23", End_Date="2024-09-25", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="79ª Asamblea General de la ONU + Cumbre del Futuro",
    Trip_Objective="Cumbre del Futuro y AGNU; bilaterales con Arevalo y Mahmoud Abbas; foro en Columbia.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=290392",
    Source_Reliability="High", Methodological_Notes="Discurso el 24/9/2024.", Tema_Foro="Cooperación Política General")

add("CHL-GB-J142", Trip_Status="Completed", Start_Date="2024-11-14", End_Date="2024-11-16", Duration_Days=3,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre APEC 2024",
    Trip_Objective="Cumbre APEC Lima; bilaterales con Xi Jinping, Trudeau y Boluarte.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=292253",
    Source_Reliability="High", Methodological_Notes="Parte de gira Peru-Brasil (J142).", Tema_Foro="Comercio/Integración Económica")

add("CHL-GB-J142", Trip_Status="Completed", Start_Date="2024-11-16", End_Date="2024-11-19", Duration_Days=4,
    Destination_Country="Brazil", Destination_City="Río de Janeiro", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Río de Janeiro (invitado)",
    Trip_Objective="Cumbre del G20; bilaterales con Modi y Starmer; Alianza Global contra el Hambre.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=292513",
    Source_Reliability="High", Methodological_Notes="Tema G20 -> Cooperacion Politica General (doctrina 5.7).",
    Tema_Foro="Cooperación Política General")

# ===== 2025 =====
add("CHL-GB-J143", Trip_Status="Completed", Start_Date="2025-02-03", End_Date="2025-02-04", Duration_Days=2,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Luis Lacalle Pou / Yamandú Orsi (electo) / José Mujica",
    Trip_Objective="Visita de trabajo; encuentros con Lacalle Pou, Orsi (electo) y Mujica.",
    Source_Verification="https://www.cnnchile.com/pais/presidente-gabriel-boric-uruguay-reunion-lacalle-orsi-pepe-mujica_20250203/",
    Source_Reliability="High", Methodological_Notes="NA")

add("CHL-GB-J144", Trip_Status="Completed", Start_Date="2025-02-28", End_Date="2025-03-01", Duration_Days=2,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Yamandú Orsi",
    Trip_Objective="Investidura de Orsi; bilaterales con Arce y Penia; cena de lideres progresistas.",
    Source_Verification="https://www.df.cl/economia-y-politica/gobierno/boric-viaja-a-uruguay-a-transmision-del-mando-en-que-asumira-el-presidente",
    Source_Reliability="High", Methodological_Notes="Segundo viaje a Uruguay en un mes.", Tema_Foro="Cooperación Política General")

add("CHL-GB-J145", Trip_Status="Completed", Start_Date="2025-04-01", End_Date="2025-04-05", Duration_Days=5,
    Destination_Country="India", Destination_City="Nueva Delhi / Mumbai / Bangalore", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Narendra Modi / Draupadi Murmu",
    Trip_Objective="Visita de Estado; anuncio del inicio de negociaciones del CEPA; comercio, tecnologia e innovacion.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=297935",
    Source_Reliability="High", Methodological_Notes="Primera visita de un mandatario chileno a India en 16 anios (anterior: Bachelet 2009).")

add("CHL-GB-J146", Trip_Status="Completed", Start_Date="2025-04-21", End_Date="2025-04-24", Duration_Days=4,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Luiz Inácio Lula da Silva",
    Trip_Objective="Visita de Estado; firma de 13 acuerdos/MOU; foro empresarial; Corredor Bioceanico.",
    Source_Verification="https://www.gob.cl/noticias/visita-de-estado-brasil-presidente-gabriel-boric-firma-acuerdos-presidente-lula-da-silva/",
    Source_Reliability="High", Methodological_Notes="Planalto reporta 13 acuerdos; conteos chilenos citan hasta 19 (discrepancia menor documentada).")

add("CHL-GB-J147", Trip_Status="Completed", Start_Date="2025-05-11", End_Date="2025-05-12", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Tokio / Osaka", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Shigeru Ishiba",
    Trip_Objective="Gira asiatica; reunion con Ishiba y Dia Nacional de Chile en Expo Osaka 2025.",
    Source_Verification="https://www.cooperativa.cl/noticias/pais/presidente-boric/viajes-al-exterior/presidente-boric-llego-a-japon-para-iniciar-su-gira-por-asia/2025-05-10/221114.html",
    Source_Reliability="High", Methodological_Notes="Parte de gira Japon-China (J147).")

add("CHL-GB-J147", Trip_Status="Completed", Start_Date="2025-05-12", End_Date="2025-05-13", Duration_Days=2,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Xi Jinping / IV Foro China-CELAC",
    Trip_Objective="Segunda visita a China; bilateral con Xi; Foro China-CELAC y Foro Empresarial Chile-China.",
    Source_Verification="https://www.biobiochile.cl/noticias/economia/actualidad-economica/2025/05/09/gobierno-confirma-que-boric-se-reunira-con-xi-jinping-en-china-y-detalla-agenda-del-presidente-en-asia.shtml",
    Source_Reliability="High", Methodological_Notes="Incluyo la IV Reunion Ministerial del Foro China-CELAC (primario: bilateral con Xi).")

add("CHL-GB-J148", Trip_Status="Completed", Start_Date="2025-07-06", End_Date="2025-07-07", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Río de Janeiro", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XVII Cumbre del BRICS (invitado)",
    Trip_Objective="Participacion como invitado en la cumbre BRICS; multilateralismo, medio ambiente y salud.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=300978",
    Source_Reliability="High", Methodological_Notes="Xi Jinping y Putin no asistieron a esta cumbre.",
    Tema_Foro="Cooperación Política General")

add("CHL-GB-J149", Trip_Status="Completed", Start_Date="2025-09-22", End_Date="2025-09-25", Duration_Days=4,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="80ª Asamblea General de la ONU",
    Trip_Objective="Ultima AGNU como presidente; nomino a Bachelet como candidata a secretaria general de la ONU.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=303931",
    Source_Reliability="High", Methodological_Notes="Discurso el 23/9/2025.", Tema_Foro="Cooperación Política General")

add("CHL-GB-J150", Trip_Status="Completed", Start_Date="2025-11-06", End_Date="2025-11-07", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Belém", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="COP30 (Cumbre de Líderes)",
    Trip_Objective="Cumbre de Lideres de la COP30; sesion de transicion energetica.",
    Source_Verification="https://www.elperiodista.cl/2025/11/boric-cierra-participacion-en-cop30/",
    Source_Reliability="Medium", Methodological_Notes="Luego viajo via Iquique a Bolivia (salida fisica distinta: journey separado).",
    Tema_Foro="Medio Ambiente/Clima")

add("CHL-GB-J151", Trip_Status="Completed", Start_Date="2025-11-07", End_Date="2025-11-08", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="La Paz", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Rodrigo Paz",
    Trip_Objective="Transmision de mando de Rodrigo Paz; saludo con Paz; tenso cruce con Milei.",
    Source_Verification="https://prensa.presidencia.cl/comunicado.aspx?id=306209",
    Source_Reliability="High", Methodological_Notes="Reingreso via Iquique entre COP30 y Bolivia (fuente El Periodista): J150 y J151 son salidas separadas.",
    Tema_Foro="Cooperación Política General")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
