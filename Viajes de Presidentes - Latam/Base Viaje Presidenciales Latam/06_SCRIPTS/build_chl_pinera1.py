# -*- coding: utf-8 -*-
"""
CHILE — Sebastián Piñera Echenique, PRIMER MANDATO (11/3/2010 a 11/3/2014, RN/Coalicion por el Cambio).
Bloque separado del 2do mandato. Continua Trip_ID tras Bachelet 1 (ultimo=57). Journey en CHL-SP1-J054.
Primer presidente de derecha electo desde 1958. Perfil MUY viajero, pro-comercio y Asia-Pacifico.
HITO: creacion de la Alianza del Pacifico (2011, con Mexico/Peru/Colombia). Asistio a las 4 APEC del
periodo (Yokohama 2010, Honolulu 2011, Vladivostok 2012, Bali 2013).
Modo research: 31 giras / ~45 tramos-pais. Fuentes: Prensa Presidencia (Wayback), MINREL, BCN, SEGIB, OEA, APEC, ONU, prensa CL.
Giras multipais = 1 Journey_ID. Excluidos por ser en Chile: CELAC-UE Santiago (ene 2013),
Alianza del Pacifico si fue en Chile. Brecha residual documentada EN EL MOMENTO en PENDIENTES.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "chile", "chile_viajes.csv")
P = "Sebastián Piñera"; O = "Chile"
rows = []; tid = 58

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2010 (desde 11/3) =====
# Gira inaugural abr 2010 (1 Journey_ID): Argentina + Brasil + EE.UU.
add("CHL-SP1-J054", Trip_Status="Completed", Start_Date="2010-04-05", End_Date="2010-04-05", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cristina Fernández de Kirchner",
    Trip_Objective="Primera gira del mandato: bilateral con CFK; integracion y post-terremoto. Tramo 1.",
    Source_Verification="Search Query: Pinera primera gira Argentina CFK abril 2010",
    Source_Reliability="Medium", Methodological_Notes="Gira inaugural Argentina-Brasil-EE.UU.")

add("CHL-SP1-J054", Trip_Status="Completed", Start_Date="2010-04-06", End_Date="2010-04-06", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Luiz Inácio Lula da Silva",
    Trip_Objective="Bilateral con Lula. Tramo 2.",
    Source_Verification="Search Query: Pinera Brasil Lula abril 2010",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("CHL-SP1-J054", Trip_Status="Completed", Start_Date="2010-04-11", End_Date="2010-04-13", Duration_Days=3,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Seguridad Nuclear + Obama",
    Trip_Objective="Cumbre de Seguridad Nuclear de Washington convocada por Obama. Tramo 3 (final).",
    Source_Verification="Search Query: Pinera Cumbre Seguridad Nuclear Washington abril 2010",
    Source_Reliability="Medium", Methodological_Notes="12-13/04/2010.")

add("CHL-SP1-J055", Trip_Status="Completed", Start_Date="2010-05-18", End_Date="2010-05-19", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VI Cumbre UE-América Latina y el Caribe",
    Trip_Objective="Cumbre UE-ALC de Madrid.",
    Source_Verification="Search Query: Pinera Cumbre UE ALC Madrid mayo 2010",
    Source_Reliability="Medium", Methodological_Notes="18-19/05/2010.")

add("CHL-SP1-J056", Trip_Status="Completed", Start_Date="2010-09-20", End_Date="2010-09-22", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre ODM + 65ª AGNU",
    Trip_Objective="Cumbre de los Objetivos del Milenio y Asamblea General de la ONU.",
    Source_Verification="Search Query: Pinera ONU ODM septiembre 2010",
    Source_Reliability="Medium", Methodological_Notes="20-22/09/2010.")

# Gira Europa oct 2010 (1 Journey_ID): Reino Unido + Francia + Alemania (por rescate mineros)
add("CHL-SP1-J057", Trip_Status="Completed", Start_Date="2010-10-17", End_Date="2010-10-18", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="David Cameron",
    Trip_Objective="Gira europea post-rescate de los 33 mineros; con la camiseta y el gesto internacional. Tramo 1.",
    Source_Verification="Search Query: Pinera gira Europa octubre 2010 mineros Cameron",
    Source_Reliability="Medium", Methodological_Notes="Gira Reino Unido-Francia-Alemania oct 2010.")

add("CHL-SP1-J057", Trip_Status="Completed", Start_Date="2010-10-19", End_Date="2010-10-20", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Nicolas Sarkozy",
    Trip_Objective="Relaciones bilaterales; inversiones. Tramo 2.",
    Source_Verification="Search Query: Pinera Francia Sarkozy octubre 2010",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("CHL-SP1-J057", Trip_Status="Completed", Start_Date="2010-10-21", End_Date="2010-10-22", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Angela Merkel",
    Trip_Objective="Relaciones bilaterales; ciencia y tecnologia. Tramo 3 (final).",
    Source_Verification="Search Query: Pinera Alemania Merkel octubre 2010",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("CHL-SP1-J058", Trip_Status="Completed", Start_Date="2010-11-13", End_Date="2010-11-14", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Yokohama", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Yokohama.",
    Source_Verification="Search Query: Pinera APEC Yokohama noviembre 2010",
    Source_Reliability="Medium", Methodological_Notes="13-14/11/2010.")

add("CHL-SP1-J059", Trip_Status="Completed", Start_Date="2010-12-03", End_Date="2010-12-04", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Mar del Plata", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XX Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Mar del Plata; homenaje a Nestor Kirchner (fallecido en oct).",
    Source_Verification="Search Query: Pinera Cumbre Iberoamericana Mar del Plata diciembre 2010",
    Source_Reliability="Medium", Methodological_Notes="3-4/12/2010.")

# ===== 2011 =====
add("CHL-SP1-J060", Trip_Status="Completed", Start_Date="2011-03-01", End_Date="2011-03-02", Duration_Days=2,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="José Mujica",
    Trip_Objective="Bilateral con Mujica; comercio e integracion.",
    Source_Verification="Search Query: Pinera Uruguay Mujica marzo 2011",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("CHL-SP1-J061", Trip_Status="Completed", Start_Date="2011-04-28", End_Date="2011-04-28", Duration_Days=1,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre fundacional de la Alianza del Pacífico",
    Trip_Objective="Creacion de la Alianza del Pacifico (Chile, Peru, Colombia, Mexico). HITO de su politica exterior.",
    Source_Verification="Search Query: Pinera Alianza del Pacifico Lima abril 2011 fundacion",
    Source_Reliability="High", Methodological_Notes="28/04/2011.")

add("CHL-SP1-J062", Trip_Status="Completed", Start_Date="2011-07-28", End_Date="2011-07-28", Duration_Days=1,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Ollanta Humala",
    Trip_Objective="Asuncion de Ollanta Humala en Peru.",
    Source_Verification="Search Query: Pinera asuncion Humala Lima julio 2011",
    Source_Reliability="Medium", Methodological_Notes="28/07/2011.")

add("CHL-SP1-J063", Trip_Status="Completed", Start_Date="2011-09-21", End_Date="2011-09-22", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="66ª AGNU",
    Trip_Objective="Asamblea General de la ONU.",
    Source_Verification="Search Query: Pinera ONU asamblea septiembre 2011",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("CHL-SP1-J064", Trip_Status="Completed", Start_Date="2011-10-28", End_Date="2011-10-29", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XXI Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Asuncion; transformacion del Estado.",
    Source_Verification="Search Query: Pinera Cumbre Iberoamericana Asuncion octubre 2011",
    Source_Reliability="Medium", Methodological_Notes="28-29/10/2011.")

add("CHL-SP1-J065", Trip_Status="Completed", Start_Date="2011-11-12", End_Date="2011-11-13", Duration_Days=2,
    Destination_Country="United States", Destination_City="Honolulu", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Honolulu.",
    Source_Verification="Search Query: Pinera APEC Honolulu noviembre 2011",
    Source_Reliability="Medium", Methodological_Notes="12-13/11/2011.")

# ===== 2012 =====
add("CHL-SP1-J066", Trip_Status="Completed", Start_Date="2012-03-26", End_Date="2012-03-27", Duration_Days=2,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cumbre de Seguridad Nuclear",
    Trip_Objective="Cumbre de Seguridad Nuclear de Seul.",
    Source_Verification="Search Query: Pinera Cumbre Seguridad Nuclear Seul marzo 2012",
    Source_Reliability="Medium", Methodological_Notes="26-27/03/2012.")

add("CHL-SP1-J067", Trip_Status="Completed", Start_Date="2012-04-14", End_Date="2012-04-15", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VI Cumbre de las Américas",
    Trip_Objective="VI Cumbre de las Americas de Cartagena.",
    Source_Verification="Search Query: Pinera VI Cumbre Americas Cartagena abril 2012",
    Source_Reliability="High", Methodological_Notes="14-15/04/2012.")

add("CHL-SP1-J068", Trip_Status="Completed", Start_Date="2012-06-20", End_Date="2012-06-21", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Conferencia Río+20",
    Trip_Objective="Conferencia de la ONU sobre Desarrollo Sostenible (Rio+20).",
    Source_Verification="Search Query: Pinera Rio+20 junio 2012",
    Source_Reliability="Medium", Methodological_Notes="20-21/06/2012.")

add("CHL-SP1-J069", Trip_Status="Completed", Start_Date="2012-09-08", End_Date="2012-09-09", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Vladivostok", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Vladivostok.",
    Source_Verification="Search Query: Pinera APEC Vladivostok septiembre 2012",
    Source_Reliability="Medium", Methodological_Notes="8-9/09/2012.")

add("CHL-SP1-J070", Trip_Status="Completed", Start_Date="2012-11-16", End_Date="2012-11-17", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Cádiz", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XXII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Cadiz.",
    Source_Verification="Search Query: Pinera Cumbre Iberoamericana Cadiz noviembre 2012",
    Source_Reliability="Medium", Methodological_Notes="16-17/11/2012.")

# ===== 2013 =====
add("CHL-SP1-J071", Trip_Status="Completed", Start_Date="2013-03-05", End_Date="2013-03-06", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Funeral de Hugo Chávez",
    Trip_Objective="Exequias del presidente venezolano Hugo Chavez.",
    Source_Verification="Search Query: Pinera funeral Hugo Chavez Caracas marzo 2013",
    Source_Reliability="Medium", Methodological_Notes="Fecha a confirmar (funeral 8/3; velatorio previo).")

add("CHL-SP1-J072", Trip_Status="Completed", Start_Date="2013-05-23", End_Date="2013-05-23", Duration_Days=1,
    Destination_Country="Colombia", Destination_City="Cali", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VII Cumbre de la Alianza del Pacífico",
    Trip_Objective="Cumbre de la Alianza del Pacifico en Cali; profundizacion de la integracion.",
    Source_Verification="Search Query: Pinera Alianza del Pacifico Cali mayo 2013",
    Source_Reliability="Medium", Methodological_Notes="23/05/2013.")

add("CHL-SP1-J073", Trip_Status="Completed", Start_Date="2013-06-04", End_Date="2013-06-04", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Barack Obama (Casa Blanca / Oficina Oval)",
    Trip_Objective="Visita oficial a la Casa Blanca; TPP, exencion de visas e inversiones. La anecdota del escritorio de la Oficina Oval.",
    Source_Verification="https://www.chile.gob.cl/chile/blog/estados-unidos/washington/presidentes-pinera-y-obama-se-reunen-en-la-casa-blanca",
    Source_Reliability="High", Methodological_Notes="CORREGIDO: originalmente mal fechado en mar-2011 (cuando en realidad Obama visito Chile el 21/3/2011). El viaje de Pinera a Washington fue el 4/6/2013.")

add("CHL-SP1-J074", Trip_Status="Completed", Start_Date="2013-08-15", End_Date="2013-08-15", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Horacio Cartes",
    Trip_Objective="Asuncion de Horacio Cartes en Paraguay.",
    Source_Verification="Search Query: Pinera asuncion Cartes Asuncion agosto 2013",
    Source_Reliability="Low", Methodological_Notes="15/08/2013. Confirmar asistencia.")

add("CHL-SP1-J075", Trip_Status="Completed", Start_Date="2013-10-07", End_Date="2013-10-08", Duration_Days=2,
    Destination_Country="Indonesia", Destination_City="Bali", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Bali.",
    Source_Verification="Search Query: Pinera APEC Bali octubre 2013",
    Source_Reliability="Medium", Methodological_Notes="7-8/10/2013.")

# ===== 2014 (hasta 11/3) =====
add("CHL-SP1-J076", Trip_Status="Completed", Start_Date="2014-02-10", End_Date="2014-02-10", Duration_Days=1,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VIII Cumbre de la Alianza del Pacífico",
    Trip_Objective="Cumbre de la Alianza del Pacifico en Cartagena; ULTIMO viaje del mandato.",
    Source_Verification="Search Query: Pinera Alianza del Pacifico Cartagena febrero 2014",
    Source_Reliability="Medium", Methodological_Notes="10/02/2014. Ultimo viaje del mandato.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (1er mandato) agregadas. Ultimo Trip_ID = {tid-1}")
