# -*- coding: utf-8 -*-
"""
Javier Milei (2023-12-10 a fecha de corte 2026-06-28). Continua Trip_ID tras A. Fernandez (ultimo=202).
Mandato EN CURSO. ~39 viajes / 45 tramos-pais hasta el corte. EE.UU. destino dominante (17 visitas).
VENTANA: solo hasta 28/06/2026. Excluido el viaje a EE.UU. planificado para julio 2026 (posterior al corte).
MERCOSUR jun 2026: registrado como cancelado. Giras multipais = 1 Journey_ID.
Fuentes: Casa Rosada, Cancilleria AR, Boletin Oficial, La Nacion, Infobae, Perfil, Ambito, Chequeado, Wikipedia (Anexo viajes Milei).
CPAC y actos ideologicos = Working Visit u Other (no son visitas de Estado).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")
P = "Javier Milei"; O = "Argentina"
rows = []; tid = 203

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2024 =====
add("ARG-JM-J172", Trip_Status="Completed", Start_Date="2024-01-16", End_Date="2024-01-17", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Discurso 'Occidente esta en peligro' contra el socialismo y la agenda woke. Primer viaje del mandato.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="Primer viaje internacional del mandato.")

# Gira Israel + Vaticano/Italia (feb 2024), 1 Journey_ID
add("ARG-JM-J173", Trip_Status="Completed", Start_Date="2024-02-06", End_Date="2024-02-08", Duration_Days=3,
    Destination_Country="Israel", Destination_City="Jerusalem", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Benjamin Netanyahu",
    Trip_Objective="Promesa de mudar la embajada a Jerusalen; Muro de los Lamentos; solidaridad tras ataque del 7-O. Tramo 1.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="Gira Israel-Vaticano feb 2024.")

add("ARG-JM-J173", Trip_Status="Completed", Start_Date="2024-02-11", End_Date="2024-02-12", Duration_Days=2,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Papa Francisco (canonización de Mama Antula)",
    Trip_Objective="Canonizacion de la primera santa argentina; audiencia y abrazo con el Papa pese a criticas previas. Tramo 2.",
    Source_Verification="https://www.vaticannews.va/es.html",
    Source_Reliability="High", Methodological_Notes="Incluyo Roma/Italia.")

add("ARG-JM-J174", Trip_Status="Completed", Start_Date="2024-02-23", End_Date="2024-02-24", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="CPAC (Conferencia de Acción Política Conservadora)",
    Trip_Objective="Discurso en la CPAC; encuentro con Donald Trump y figuras de la derecha global.",
    Source_Verification="Search Query: Milei CPAC Washington febrero 2024 Trump",
    Source_Reliability="Medium", Methodological_Notes="CPAC = evento partidario; clasificado Other/Working Visit.")

add("ARG-JM-J175", Trip_Status="Completed", Start_Date="2024-04-11", End_Date="2024-04-12", Duration_Days=2,
    Destination_Country="United States", Destination_City="Austin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Elon Musk (fábrica Tesla)",
    Trip_Objective="Reunion con Elon Musk en la planta de Tesla en Texas; inversiones y litio.",
    Source_Verification="Search Query: Milei Elon Musk Tesla Texas Austin abril 2024",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-JM-J176", Trip_Status="Completed", Start_Date="2024-05-17", End_Date="2024-05-19", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Acto de Vox 'Europa Viva 2024'",
    Trip_Objective="Acto de Vox; llamo 'corrupta' a la esposa de Sanchez, desatando crisis diplomatica Espana-Argentina.",
    Source_Verification="Search Query: Milei Vox Madrid mayo 2024 Sanchez crisis diplomatica",
    Source_Reliability="High", Methodological_Notes="No fue visita de Estado; acto partidario.")

add("ARG-JM-J177", Trip_Status="Completed", Start_Date="2024-05-27", End_Date="2024-05-28", Duration_Days=2,
    Destination_Country="United States", Destination_City="Los Angeles", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Milken Institute / Stanford",
    Trip_Objective="Conferencias en California (Silicon Valley, Stanford); busqueda de inversiones tecnologicas.",
    Source_Verification="Search Query: Milei Stanford Silicon Valley California mayo 2024",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("ARG-JM-J178", Trip_Status="Completed", Start_Date="2024-06-13", End_Date="2024-06-15", Duration_Days=3,
    Destination_Country="Italy", Destination_City="Fasano", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G7 ampliada (invitado por Meloni)",
    Trip_Objective="Invitado a la Cumbre del G7 en Puglia; bilaterales con Biden, Macron, Meloni, Zelenski.",
    Source_Verification="Search Query: Milei G7 Puglia Italia junio 2024 invitado Meloni",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-JM-J179", Trip_Status="Completed", Start_Date="2024-06-21", End_Date="2024-06-22", Duration_Days=2,
    Destination_Country="Czechia", Destination_City="Prague", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Premio de la Fundación Liberálních Ekonomů",
    Trip_Objective="Recepcion de premio de instituciones liberales checas; conferencia economica.",
    Source_Verification="Search Query: Milei Praga Republica Checa junio 2024 premio liberal",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("ARG-JM-J180", Trip_Status="Completed", Start_Date="2024-07-08", End_Date="2024-07-09", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Balneário Camboriú", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="CPAC Brasil (con Bolsonaro)",
    Trip_Objective="CPAC Brasil junto a Jair Bolsonaro; NO se reunio con Lula. Acto ideologico.",
    Source_Verification="Search Query: Milei CPAC Brasil Camboriu julio 2024 Bolsonaro",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-JM-J181", Trip_Status="Completed", Start_Date="2024-07-15", End_Date="2024-07-16", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro de la CPAC / evento económico",
    Trip_Objective="Participacion en foro; relaciones con Paraguay.",
    Source_Verification="Search Query: Milei Paraguay Asuncion julio 2024",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; verificar.")

add("ARG-JM-J182", Trip_Status="Completed", Start_Date="2024-09-22", End_Date="2024-09-24", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="79ª Asamblea General de la ONU",
    Trip_Objective="Primer discurso ante la ONU; critico la Agenda 2030; voto argentino aislado. Reunion con Musk.",
    Source_Verification="Search Query: Milei ONU 79 asamblea septiembre 2024 Agenda 2030",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-JM-J183", Trip_Status="Completed", Start_Date="2024-11-18", End_Date="2024-11-19", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Cumbre del G20 de Río de Janeiro",
    Trip_Objective="Cumbre del G20; reservas argentinas a la declaracion final. Tension con Lula.",
    Source_Verification="Search Query: Milei G20 Rio de Janeiro noviembre 2024",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-JM-J184", Trip_Status="Completed", Start_Date="2024-11-14", End_Date="2024-11-15", Duration_Days=2,
    Destination_Country="United States", Destination_City="Palm Beach", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump (Mar-a-Lago)",
    Trip_Objective="Primer lider extranjero en visitar a Trump tras ganar la eleccion; gala de America First. Previo al G20.",
    Source_Verification="Search Query: Milei Trump Mar-a-Lago noviembre 2024 primer lider",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-JM-J185", Trip_Status="Completed", Start_Date="2024-12-05", End_Date="2024-12-06", Duration_Days=2,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del MERCOSUR",
    Trip_Objective="Cumbre del bloque; impulso al acuerdo Mercosur-UE y a mayor flexibilidad comercial.",
    Source_Verification="Search Query: Milei Cumbre Mercosur Montevideo diciembre 2024",
    Source_Reliability="Medium", Methodological_Notes="NA")

# ===== 2025 =====
add("ARG-JM-J186", Trip_Status="Completed", Start_Date="2025-01-20", End_Date="2025-01-21", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Donald Trump",
    Trip_Objective="Invitado especial a la investidura de Trump; unico presidente latinoamericano en primera fila.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/discursos",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-JM-J187", Trip_Status="Completed", Start_Date="2025-01-22", End_Date="2025-01-23", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Segundo discurso en Davos; enlazo con la asuncion de Trump (misma gira).",
    Source_Verification="Search Query: Milei Davos enero 2025 discurso",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-JM-J188", Trip_Status="Completed", Start_Date="2025-02-20", End_Date="2025-02-22", Duration_Days=3,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="CPAC 2025",
    Trip_Objective="Discurso en la CPAC; entrego una motosierra simbolica a Elon Musk (recorte del gasto).",
    Source_Verification="Search Query: Milei CPAC 2025 motosierra Musk febrero",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-JM-J189", Trip_Status="Completed", Start_Date="2025-04-07", End_Date="2025-04-08", Duration_Days=2,
    Destination_Country="United States", Destination_City="Palm Beach", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump (Mar-a-Lago, gala)",
    Trip_Objective="Gala en Mar-a-Lago; busco excepcion a los aranceles de Trump y apoyo al acuerdo con el FMI.",
    Source_Verification="Search Query: Milei Trump Mar-a-Lago abril 2025 aranceles FMI",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-JM-J190", Trip_Status="Completed", Start_Date="2025-04-26", End_Date="2025-04-26", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Funeral del Papa Francisco",
    Trip_Objective="Exequias del Papa Francisco (fallecido 21/4/2025); Milei encabezo la delegacion argentina.",
    Source_Verification="Search Query: Milei funeral Papa Francisco Vaticano abril 2025",
    Source_Reliability="High", Methodological_Notes="Papa Francisco fallecio el 21/4/2025.")

add("ARG-JM-J191", Trip_Status="Completed", Start_Date="2025-05-18", End_Date="2025-05-19", Duration_Days=2,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Misa inaugural del Papa León XIV",
    Trip_Objective="Inicio del pontificado de Leon XIV (elegido 8/5/2025); delegacion argentina.",
    Source_Verification="Search Query: Milei asuncion Papa Leon XIV Vaticano mayo 2025",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas.")

add("ARG-JM-J192", Trip_Status="Completed", Start_Date="2025-06-11", End_Date="2025-06-12", Duration_Days=2,
    Destination_Country="Israel", Destination_City="Jerusalem", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Benjamin Netanyahu / Isaac Herzog",
    Trip_Objective="Segunda visita a Israel; reafirmo alianza estrategica y planes sobre la embajada en Jerusalen.",
    Source_Verification="Search Query: Milei Israel Jerusalen junio 2025 segunda visita",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada.")

add("ARG-JM-J193", Trip_Status="Completed", Start_Date="2025-09-23", End_Date="2025-09-24", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="80ª Asamblea General de la ONU",
    Trip_Objective="Segundo discurso ante la ONU; agenda de libertad economica y criticas al multilateralismo.",
    Source_Verification="Search Query: Milei ONU 80 asamblea septiembre 2025",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada.")

# ===== 2026 (hasta corte 28/06) =====
add("ARG-JM-J194", Trip_Status="Completed", Start_Date="2026-01-20", End_Date="2026-01-21", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Tercer discurso consecutivo en Davos.",
    Source_Verification="Search Query: Milei Davos enero 2026",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; verificar (mandato en curso).")

# CANCELADO 2026
add("ARG-JM-J195", Trip_Status="Canceled", Start_Date="2026-06-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="Argentina", Destination_City="NA", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del MERCOSUR (junio 2026)",
    Trip_Objective="Cumbre del Mercosur de junio 2026. Registrada como no concretada por Milei segun el informe. Verificar sede y motivo.",
    Source_Verification="Search Query: Milei Cumbre Mercosur junio 2026",
    Source_Reliability="Low", Methodological_Notes="CANCELADO/no concretado; sin duracion. Dato a confirmar (mandato en curso). Si la sede fue Argentina, se excluye del conteo de viajes.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
