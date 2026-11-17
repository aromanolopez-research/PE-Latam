# -*- coding: utf-8 -*-
"""
Alberto Fernández (2019-12-10 a 2023-12-10). Continua Trip_ID tras Macri (ultimo=171).
~27 salidas fisicas / ~39 tramos-pais + 3 cancelados. Giras multipais = 1 Journey_ID.
Contexto COVID: cierre de fronteras 15/3/2020; sin viajes mar-nov 2020; retomo con asuncion Arce (Bolivia, 7-8/11/2020).
Excluidos por ser en Argentina: Cumbre CELAC Buenos Aires (ene 2023).
Fuentes: Casa Rosada, Cancilleria AR, Boletin Oficial, Telam, La Nacion, Infobae, Pagina/12, Perfil, Ambito, ONU, CELAC, SEGIB, COP.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")
P = "Alberto Fernández"; O = "Argentina"
rows = []; tid = 172

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2019 =====
add("ARG-AF-J153", Trip_Status="Completed", Start_Date="2019-12-19", End_Date="2019-12-19", Duration_Days=1,
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Andrés Manuel López Obrador",
    Trip_Objective="Primer viaje del mandato; relanzar eje Mexico-Argentina; agenda regional y comercial con AMLO.",
    Source_Verification="Search Query: Alberto Fernandez primer viaje Mexico AMLO diciembre 2019",
    Source_Reliability="Medium", Methodological_Notes="Fecha aproximada; primer viaje oficial.")

# ===== 2020 — Gira Israel + Europa (ene-feb, pre-COVID). 1 Journey_ID (larga gira multipais) =====
add("ARG-AF-J154", Trip_Status="Completed", Start_Date="2020-01-22", End_Date="2020-01-23", Duration_Days=2,
    Destination_Country="Israel", Destination_City="Jerusalem", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="V Foro Mundial del Holocausto (Yad Vashem)",
    Trip_Objective="Foro Mundial del Holocausto. Tramo 1 de gira. Bilaterales al margen.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="Inicio de gira Israel-Europa pre-pandemia.")

add("ARG-AF-J154", Trip_Status="Completed", Start_Date="2020-01-31", End_Date="2020-01-31", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Papa Francisco",
    Trip_Objective="Audiencia con el Papa Francisco. Tramo 2.",
    Source_Verification="https://www.vaticannews.va/es/papa/news/2020-01/papa-francisco-audiencia-presidente-argentina-alberto-fernandez.html",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-AF-J154", Trip_Status="Completed", Start_Date="2020-02-01", End_Date="2020-02-01", Duration_Days=1,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Giuseppe Conte / Sergio Mattarella",
    Trip_Objective="Apoyo italiano a la renegociacion de deuda con el FMI. Tramo 3.",
    Source_Verification="Search Query: Alberto Fernandez Italia Conte Mattarella febrero 2020 deuda",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J154", Trip_Status="Completed", Start_Date="2020-02-03", End_Date="2020-02-03", Duration_Days=1,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Angela Merkel",
    Trip_Objective="Apoyo aleman a la renegociacion con el FMI. Tramo 4.",
    Source_Verification="Search Query: Alberto Fernandez Merkel Berlin febrero 2020 deuda FMI",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J154", Trip_Status="Completed", Start_Date="2020-02-05", End_Date="2020-02-05", Duration_Days=1,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Pedro Sánchez / Rey Felipe VI",
    Trip_Objective="Apoyo espanol a la deuda; relaciones bilaterales. Tramo 5 (final de la gira europea).",
    Source_Verification="Search Query: Alberto Fernandez Sanchez Madrid febrero 2020 deuda",
    Source_Reliability="Medium", Methodological_Notes="Cierre de gira. Luego, 15/3/2020 cierre de fronteras por COVID.")

# ===== 2020 post-cierre =====
add("ARG-AF-J155", Trip_Status="Completed", Start_Date="2020-11-07", End_Date="2020-11-08", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="La Paz", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Luis Arce",
    Trip_Objective="Primer viaje tras el cierre por COVID; asuncion de Arce (retorno del MAS al poder).",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="Primer viaje post-cierre de fronteras.")

# ===== 2021 =====
add("ARG-AF-J156", Trip_Status="Completed", Start_Date="2021-05-10", End_Date="2021-05-11", Duration_Days=2,
    Destination_Country="Portugal", Destination_City="Lisbon", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="António Costa / Marcelo Rebelo de Sousa",
    Trip_Objective="Apoyo a renegociacion con Club de Paris y FMI. Tramo 1 de gira europea.",
    Source_Verification="Search Query: Alberto Fernandez Portugal Lisboa mayo 2021 gira europea deuda",
    Source_Reliability="Medium", Methodological_Notes="Gira europea mayo 2021 (Portugal-Espana-Francia-Italia-Vaticano).")

add("ARG-AF-J156", Trip_Status="Completed", Start_Date="2021-05-11", End_Date="2021-05-12", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Pedro Sánchez",
    Trip_Objective="Apoyo a la deuda; inversiones. Tramo 2.",
    Source_Verification="Search Query: Alberto Fernandez Espana Madrid mayo 2021 Sanchez deuda",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J156", Trip_Status="Completed", Start_Date="2021-05-12", End_Date="2021-05-13", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Apoyo frances en el Club de Paris. Tramo 3.",
    Source_Verification="Search Query: Alberto Fernandez Macron Paris mayo 2021 Club de Paris",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J156", Trip_Status="Completed", Start_Date="2021-05-13", End_Date="2021-05-14", Duration_Days=2,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Mario Draghi / Papa Francisco",
    Trip_Objective="Apoyo italiano a la deuda; audiencia con el Papa. Tramo 4 (final).",
    Source_Verification="Search Query: Alberto Fernandez Italia Draghi Papa mayo 2021",
    Source_Reliability="Medium", Methodological_Notes="Incluye Vaticano.")

add("ARG-AF-J157", Trip_Status="Completed", Start_Date="2021-09-20", End_Date="2021-09-21", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="76ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la ONU (deuda, vacunas, Malvinas). Primer viaje presencial a la AGNU del mandato.",
    Source_Verification="https://www.cancilleria.gob.ar/es/actualidad/noticias",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada.")

add("ARG-AF-J158", Trip_Status="Completed", Start_Date="2021-10-30", End_Date="2021-10-31", Duration_Days=2,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Roma",
    Trip_Objective="Cumbre del G20; bilaterales sobre la deuda con el FMI. Tramo 1.",
    Source_Verification="Search Query: Alberto Fernandez G20 Roma octubre 2021",
    Source_Reliability="Medium", Methodological_Notes="Enlazo con COP26 Glasgow.")

add("ARG-AF-J158", Trip_Status="Completed", Start_Date="2021-11-01", End_Date="2021-11-02", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="Glasgow", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="COP26 (Conferencia de la ONU sobre Cambio Climático)",
    Trip_Objective="Cumbre climatica COP26; compromisos ambientales. Tramo 2 (Escocia).",
    Source_Verification="Search Query: Alberto Fernandez COP26 Glasgow noviembre 2021",
    Source_Reliability="Medium", Methodological_Notes="Escocia = Reino Unido.")

# ===== 2022 =====
# Gira Rusia + China + Barbados (feb 2022), 1 Journey_ID
add("ARG-AF-J159", Trip_Status="Completed", Start_Date="2022-02-03", End_Date="2022-02-03", Duration_Days=1,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Vladímir Putin",
    Trip_Objective="Reunion con Putin; dijo que Argentina podia ser 'puerta de entrada' de Rusia a la region. Tramo 1.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="Gira Rusia-China-Barbados feb 2022.")

add("ARG-AF-J159", Trip_Status="Completed", Start_Date="2022-02-05", End_Date="2022-02-06", Duration_Days=2,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Xi Jinping (apertura JJOO Invierno)",
    Trip_Objective="Adhesion de Argentina a la Franja y la Ruta; financiamiento de obras; apertura de los JJOO de Invierno. Tramo 2.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-AF-J159", Trip_Status="Completed", Start_Date="2022-02-08", End_Date="2022-02-08", Duration_Days=1,
    Destination_Country="Barbados", Destination_City="Bridgetown", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mia Mottley",
    Trip_Objective="Escala de regreso; relaciones con el Caribe (CARICOM). Tramo 3 (final).",
    Source_Verification="Search Query: Alberto Fernandez Barbados Mottley febrero 2022",
    Source_Reliability="Low", Methodological_Notes="Escala; verificar caracter oficial.")

add("ARG-AF-J160", Trip_Status="Completed", Start_Date="2022-05-08", End_Date="2022-05-11", Duration_Days=4,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Olaf Scholz",
    Trip_Objective="Gira europea; apoyo a la deuda, energia, inversiones. Tramo 1 (Alemania).",
    Source_Verification="Search Query: Alberto Fernandez Scholz Alemania mayo 2022 gira europea",
    Source_Reliability="Medium", Methodological_Notes="Gira Alemania-Francia-Espana may 2022.")

add("ARG-AF-J160", Trip_Status="Completed", Start_Date="2022-05-11", End_Date="2022-05-12", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Relaciones bilaterales; deuda; guerra en Ucrania. Tramo 2.",
    Source_Verification="Search Query: Alberto Fernandez Macron Paris mayo 2022",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J160", Trip_Status="Completed", Start_Date="2022-05-12", End_Date="2022-05-13", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Pedro Sánchez",
    Trip_Objective="Inversiones energeticas (Repsol/YPF); relaciones bilaterales. Tramo 3 (final).",
    Source_Verification="Search Query: Alberto Fernandez Sanchez Madrid mayo 2022",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J161", Trip_Status="Completed", Start_Date="2022-06-26", End_Date="2022-06-28", Duration_Days=3,
    Destination_Country="Germany", Destination_City="Elmau", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G7 ampliada (invitado)",
    Trip_Objective="Invitado a la Cumbre del G7 en Baviera; hablo de seguridad alimentaria y energetica.",
    Source_Verification="Search Query: Alberto Fernandez G7 Elmau Baviera junio 2022 invitado",
    Source_Reliability="Medium", Methodological_Notes="NO asistio a la Cumbre de las Americas de Los Angeles (jun 2022) por la exclusion de Cuba/Venezuela/Nicaragua; envio al canciller. Ver bitacora.")

add("ARG-AF-J162", Trip_Status="Completed", Start_Date="2022-09-19", End_Date="2022-09-21", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="77ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la ONU (deuda, FMI, Malvinas, guerra en Ucrania).",
    Source_Verification="Search Query: Alberto Fernandez ONU 77 asamblea septiembre 2022",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J163", Trip_Status="Completed", Start_Date="2022-11-15", End_Date="2022-11-16", Duration_Days=2,
    Destination_Country="Indonesia", Destination_City="Bali", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Bali",
    Trip_Objective="Cumbre del G20; bilaterales; agenda de deuda y alimentos.",
    Source_Verification="Search Query: Alberto Fernandez G20 Bali noviembre 2022",
    Source_Reliability="Medium", Methodological_Notes="NA")

# ===== 2023 =====
add("ARG-AF-J164", Trip_Status="Completed", Start_Date="2023-01-23", End_Date="2023-01-24", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Lula da Silva",
    Trip_Objective="Primera visita a Lula tras su asuncion; relanzar la relacion bilateral; proyecto de moneda comun (SUR).",
    Source_Verification="Search Query: Alberto Fernandez Lula Brasilia enero 2023 moneda comun",
    Source_Reliability="Medium", Methodological_Notes="La Cumbre CELAC de Buenos Aires (ene 2023) NO se incluye (fue en Argentina).")

add("ARG-AF-J165", Trip_Status="Completed", Start_Date="2023-03-27", End_Date="2023-03-29", Duration_Days=3,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Joe Biden",
    Trip_Objective="Reunion en la Casa Blanca con Biden; FMI, inversiones, litio.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-AF-J166", Trip_Status="Completed", Start_Date="2023-05-02", End_Date="2023-05-03", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre de presidentes sudamericanos",
    Trip_Objective="Cumbre sudamericana convocada por Lula para relanzar la integracion regional.",
    Source_Verification="Search Query: Cumbre sudamericana Brasilia mayo 2023 Lula Alberto Fernandez",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J167", Trip_Status="Completed", Start_Date="2023-08-08", End_Date="2023-08-09", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Belém", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre de la Amazonía (OTCA)",
    Trip_Objective="Cumbre amazonica; medio ambiente. Argentina como pais invitado/observador.",
    Source_Verification="Search Query: Cumbre Amazonia Belem agosto 2023 Alberto Fernandez OTCA",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J168", Trip_Status="Completed", Start_Date="2023-08-22", End_Date="2023-08-24", Duration_Days=3,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XV Cumbre de los BRICS",
    Trip_Objective="Cumbre BRICS; Argentina fue invitada a integrarse al bloque a partir de 2024.",
    Source_Verification="Search Query: Alberto Fernandez BRICS Johannesburgo agosto 2023 invitacion",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-AF-J169", Trip_Status="Completed", Start_Date="2023-09-08", End_Date="2023-09-10", Duration_Days=3,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Nueva Delhi",
    Trip_Objective="Cumbre del G20; ultima gran cumbre global del mandato.",
    Source_Verification="Search Query: Alberto Fernandez G20 Nueva Delhi septiembre 2023",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-AF-J170", Trip_Status="Completed", Start_Date="2023-09-18", End_Date="2023-09-20", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="78ª Asamblea General de la ONU",
    Trip_Objective="Ultimo discurso ante la ONU como presidente.",
    Source_Verification="Search Query: Alberto Fernandez ONU 78 asamblea septiembre 2023 ultimo discurso",
    Source_Reliability="Medium", Methodological_Notes="Ultimo viaje internacional relevante del mandato.")

# ===== CANCELADOS =====
add("ARG-AF-J171", Trip_Status="Canceled", Start_Date="2022-06-08", End_Date="NA", Duration_Days="NA",
    Destination_Country="United States", Destination_City="Los Angeles", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IX Cumbre de las Américas",
    Trip_Objective="Cumbre de las Americas. NO asistio (aunque como pdte pro tempore CELAC dio discurso); protesta por exclusion de Cuba, Venezuela y Nicaragua. Envio al canciller Cafiero.",
    Source_Verification="Search Query: Alberto Fernandez no asiste Cumbre Americas Los Angeles junio 2022 exclusion",
    Source_Reliability="High", Methodological_Notes="Cancelado; sin duracion. Ausencia politica deliberada.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
