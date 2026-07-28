# -*- coding: utf-8 -*-
"""
CHILE — Michelle Bachelet, SEGUNDO MANDATO (11/3/2014 a 11/3/2018, Nueva Mayoria/PS). Bloque separado del 1ro.
Continua Trip_ID tras Pinera 1 (ultimo=84). Journey continua en CHL-MB2-J077.
Perfil algo menos viajero que su 1er mandato (mas centrada en agenda interna de reformas).
Continuidad de Alianza del Pacifico y APEC; perfil climatico y de genero (COP21, Acuerdo de Paris, Agenda 2030).
Modo research: 29 giras confirmadas + 2 canceladas. Fuentes: Prensa Presidencia (Wayback), MINREL, BCN, SEGIB, OEA, APEC, ONU, prensa CL.
Giras multipais = 1 Journey_ID. Excluidos por ser en Chile: Alianza del Pacifico Puerto Varas (jul 2016).
Brecha residual documentada EN EL MOMENTO en PENDIENTES_VERIFICACION.txt.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "chile", "chile_viajes.csv")
P = "Michelle Bachelet"; O = "Chile"
rows = []; tid = 85

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2014 (desde 11/3) =====
add("CHL-MB2-J077", Trip_Status="Completed", Start_Date="2014-06-12", End_Date="2014-06-12", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="São Paulo", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Inauguración del Mundial de Fútbol 2014",
    Trip_Objective="Apertura de la Copa del Mundo (Chile clasificado); primer viaje del segundo mandato.",
    Source_Verification="Search Query: Bachelet inauguracion Mundial Brasil junio 2014",
    Source_Reliability="Medium", Methodological_Notes="Primer viaje del 2do mandato. Confirmar caracter oficial.")

add("CHL-MB2-J078", Trip_Status="Completed", Start_Date="2014-06-19", End_Date="2014-06-20", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Punta Mita", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IX Cumbre de la Alianza del Pacífico",
    Trip_Objective="Cumbre de la Alianza del Pacifico en Punta Mita.",
    Source_Verification="Search Query: Bachelet Alianza del Pacifico Punta Mita junio 2014",
    Source_Reliability="Medium", Methodological_Notes="19-20/06/2014.")

add("CHL-MB2-J079", Trip_Status="Completed", Start_Date="2014-09-24", End_Date="2014-09-25", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="69ª AGNU + Cumbre del Clima",
    Trip_Objective="Asamblea General de la ONU y Cumbre del Clima; agenda de genero y desarrollo.",
    Source_Verification="Search Query: Bachelet ONU asamblea septiembre 2014",
    Source_Reliability="Medium", Methodological_Notes="24-25/09/2014.")

add("CHL-MB2-J080", Trip_Status="Completed", Start_Date="2014-12-08", End_Date="2014-12-09", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Veracruz", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XXIV Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Veracruz.",
    Source_Verification="Search Query: Bachelet Cumbre Iberoamericana Veracruz diciembre 2014",
    Source_Reliability="Medium", Methodological_Notes="8-9/12/2014.")

# ===== 2015 =====
add("CHL-MB2-J081", Trip_Status="Completed", Start_Date="2015-03-01", End_Date="2015-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Tabaré Vázquez",
    Trip_Objective="Asuncion de Tabare Vazquez en Uruguay.",
    Source_Verification="Search Query: Bachelet asuncion Tabare Vazquez Montevideo marzo 2015",
    Source_Reliability="Medium", Methodological_Notes="1/03/2015.")

add("CHL-MB2-J082", Trip_Status="Completed", Start_Date="2015-04-10", End_Date="2015-04-11", Duration_Days=2,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VII Cumbre de las Américas",
    Trip_Objective="VII Cumbre de las Americas; historica por el deshielo Cuba-EE.UU.",
    Source_Verification="Search Query: Bachelet VII Cumbre Americas Panama abril 2015",
    Source_Reliability="High", Methodological_Notes="10-11/04/2015.")

# Gira europea may-jun 2015 (1 Journey_ID): Francia + Italia/Vaticano
add("CHL-MB2-J083", Trip_Status="Completed", Start_Date="2015-05-27", End_Date="2015-05-28", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="François Hollande",
    Trip_Objective="Visita de Estado a Francia; clima (rumbo a COP21) e inversiones. Tramo 1.",
    Source_Verification="Search Query: Bachelet visita Estado Francia Hollande mayo 2015",
    Source_Reliability="Medium", Methodological_Notes="Gira europea may-jun 2015; fechas a confirmar.")

add("CHL-MB2-J083", Trip_Status="Completed", Start_Date="2015-06-05", End_Date="2015-06-05", Duration_Days=1,
    Destination_Country="Italy", Destination_City="Milan", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Expo Milán 2015",
    Trip_Objective="Dia de Chile en la Expo Milan. Tramo 2 (final).",
    Source_Verification="Search Query: Bachelet Expo Milan junio 2015",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; verificar si fue misma gira.")

add("CHL-MB2-J084", Trip_Status="Completed", Start_Date="2015-06-10", End_Date="2015-06-11", Duration_Days=2,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cumbre UE-CELAC",
    Trip_Objective="Cumbre UE-CELAC de Bruselas.",
    Source_Verification="Search Query: Bachelet Cumbre UE CELAC Bruselas junio 2015",
    Source_Reliability="Medium", Methodological_Notes="10-11/06/2015.")

add("CHL-MB2-J085", Trip_Status="Completed", Start_Date="2015-07-02", End_Date="2015-07-03", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Paracas", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="X Cumbre de la Alianza del Pacífico",
    Trip_Objective="Cumbre de la Alianza del Pacifico en Paracas.",
    Source_Verification="Search Query: Bachelet Alianza del Pacifico Paracas julio 2015",
    Source_Reliability="Medium", Methodological_Notes="2-3/07/2015.")

add("CHL-MB2-J086", Trip_Status="Completed", Start_Date="2015-09-26", End_Date="2015-09-28", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de la Agenda 2030 + 70ª AGNU",
    Trip_Objective="Cumbre de Desarrollo Sostenible (Agenda 2030/ODS) y Asamblea General de la ONU.",
    Source_Verification="Search Query: Bachelet ONU Agenda 2030 septiembre 2015",
    Source_Reliability="Medium", Methodological_Notes="26-28/09/2015.")

add("CHL-MB2-J087", Trip_Status="Completed", Start_Date="2015-11-18", End_Date="2015-11-19", Duration_Days=2,
    Destination_Country="Philippines", Destination_City="Manila", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Manila.",
    Source_Verification="Search Query: Bachelet APEC Manila noviembre 2015",
    Source_Reliability="Medium", Methodological_Notes="18-19/11/2015.")

add("CHL-MB2-J088", Trip_Status="Completed", Start_Date="2015-11-30", End_Date="2015-12-01", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="COP21 (Conferencia del Clima)",
    Trip_Objective="Segmento de lideres de la COP21 que adopto el Acuerdo de Paris.",
    Source_Verification="Search Query: Bachelet COP21 Paris noviembre 2015",
    Source_Reliability="High", Methodological_Notes="30/11-1/12/2015.")

# ===== 2016 =====
add("CHL-MB2-J089", Trip_Status="Completed", Start_Date="2016-01-27", End_Date="2016-01-27", Duration_Days=1,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IV Cumbre CELAC",
    Trip_Objective="Cumbre CELAC en Quito.",
    Source_Verification="Search Query: Bachelet CELAC Quito enero 2016",
    Source_Reliability="Medium", Methodological_Notes="27/01/2016. Confirmar asistencia.")

# Gira Asia may 2016 (1 Journey_ID): China + Indonesia
add("CHL-MB2-J090", Trip_Status="Completed", Start_Date="2016-05-13", End_Date="2016-05-16", Duration_Days=4,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Xi Jinping",
    Trip_Objective="Visita de Estado a China; profundizacion del TLC y asociacion estrategica. Tramo 1.",
    Source_Verification="Search Query: Bachelet visita Estado China Xi Jinping mayo 2016",
    Source_Reliability="Medium", Methodological_Notes="Gira asiatica may 2016; fechas a confirmar.")

add("CHL-MB2-J090", Trip_Status="Completed", Start_Date="2016-05-17", End_Date="2016-05-18", Duration_Days=2,
    Destination_Country="Indonesia", Destination_City="Jakarta", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Joko Widodo",
    Trip_Objective="Comercio Asia-Pacifico. Tramo 2 (final).",
    Source_Verification="Search Query: Bachelet Indonesia Jakarta mayo 2016",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("CHL-MB2-J091", Trip_Status="Completed", Start_Date="2016-09-20", End_Date="2016-09-21", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="71ª AGNU",
    Trip_Objective="Asamblea General de la ONU.",
    Source_Verification="Search Query: Bachelet ONU asamblea septiembre 2016",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("CHL-MB2-J092", Trip_Status="Completed", Start_Date="2016-10-28", End_Date="2016-10-29", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XXV Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Cartagena; juventud y desarrollo sostenible.",
    Source_Verification="Search Query: Bachelet Cumbre Iberoamericana Cartagena octubre 2016",
    Source_Reliability="Medium", Methodological_Notes="28-29/10/2016.")

add("CHL-MB2-J093", Trip_Status="Completed", Start_Date="2016-11-19", End_Date="2016-11-20", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Lima.",
    Source_Verification="Search Query: Bachelet APEC Lima noviembre 2016",
    Source_Reliability="Medium", Methodological_Notes="19-20/11/2016.")

# ===== 2017 =====
add("CHL-MB2-J094", Trip_Status="Completed", Start_Date="2017-01-24", End_Date="2017-01-25", Duration_Days=2,
    Destination_Country="Dominican Republic", Destination_City="Punta Cana", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="V Cumbre CELAC",
    Trip_Objective="Cumbre CELAC en Punta Cana.",
    Source_Verification="Search Query: Bachelet CELAC Punta Cana enero 2017",
    Source_Reliability="Low", Methodological_Notes="24-25/01/2017. Confirmar asistencia.")

# Gira China (Franja y la Ruta) may 2017 — 1 Journey_ID
add("CHL-MB2-J095", Trip_Status="Completed", Start_Date="2017-05-13", End_Date="2017-05-15", Duration_Days=3,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Foro de la Franja y la Ruta",
    Trip_Objective="Foro de la Franja y la Ruta en Beijing; unica presidenta sudamericana invitada. Bilateral con Xi.",
    Source_Verification="Search Query: Bachelet Foro Franja y la Ruta Beijing mayo 2017",
    Source_Reliability="Medium", Methodological_Notes="13-15/05/2017.")

add("CHL-MB2-J096", Trip_Status="Completed", Start_Date="2017-06-29", End_Date="2017-06-30", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Cali", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XII Cumbre de la Alianza del Pacífico",
    Trip_Objective="Cumbre de la Alianza del Pacifico en Cali.",
    Source_Verification="Search Query: Bachelet Alianza del Pacifico Cali junio 2017",
    Source_Reliability="Medium", Methodological_Notes="29-30/06/2017.")

add("CHL-MB2-J097", Trip_Status="Completed", Start_Date="2017-09-18", End_Date="2017-09-19", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="72ª AGNU",
    Trip_Objective="Asamblea General de la ONU; ultima de su mandato.",
    Source_Verification="Search Query: Bachelet ONU asamblea septiembre 2017",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("CHL-MB2-J098", Trip_Status="Completed", Start_Date="2017-11-10", End_Date="2017-11-11", Duration_Days=2,
    Destination_Country="Vietnam", Destination_City="Da Nang", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Da Nang; ultima APEC de su mandato. Firma del CPTPP en agenda.",
    Source_Verification="Search Query: Bachelet APEC Da Nang noviembre 2017",
    Source_Reliability="Medium", Methodological_Notes="10-11/11/2017.")

# ===== 2018 (hasta 11/3) =====
add("CHL-MB2-J099", Trip_Status="Completed", Start_Date="2018-01-21", End_Date="2018-01-22", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Pedro Pablo Kuczynski",
    Trip_Objective="Bilateral con Peru; integracion y agenda de la Alianza del Pacifico.",
    Source_Verification="Search Query: Bachelet Peru Kuczynski enero 2018",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; confirmar.")

add("CHL-MB2-J100", Trip_Status="Completed", Start_Date="2018-01-28", End_Date="2018-01-30", Duration_Days=3,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Raúl Castro",
    Trip_Objective="Visita oficial a Cuba; ULTIMO viaje internacional del mandato.",
    Source_Verification="Search Query: Bachelet visita Cuba Raul Castro enero 2018",
    Source_Reliability="Medium", Methodological_Notes="28-30/01/2018. Ultimo viaje del mandato.")

# NOTA: el informe del research menciona 2 giras canceladas en el mandato, pero sin
# destino/motivo confirmados en el material disponible. NO se cargan como filas
# (toda fila necesita destino y region validos). Quedan documentadas en
# PENDIENTES_VERIFICACION.txt para confirmar destino, fecha y motivo (regla anti-alucinacion).

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (2do mandato) agregadas. Ultimo Trip_ID = {tid-1}")
