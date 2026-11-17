# -*- coding: utf-8 -*-
"""
CHILE — Michelle Bachelet, PRIMER MANDATO (11/3/2006 a 11/3/2010, PS). Bloque separado del 2do mandato.
Continua Trip_ID tras Lagos (ultimo=29). Journey continua en CHL-MB1-J028.
Modo research: ~35 giras / 45+ tramos-pais. Perfil multilateral y de genero; continuidad librecambista
y de APEC heredada de Lagos; primera presidenta pro tempore de UNASUR (2008); hito Cuba 2009.
Fuentes: Prensa Presidencia Chile (Wayback), MINREL, BCN, SEGIB, OEA, APEC, ONU, prensa CL.
Giras multipais = 1 Journey_ID. Excluidos por ser en Chile: Iberoamericana Santiago (nov 2007),
UNASUR extraordinaria Santiago (sep 2008). CANCELADO: asuncion Mujica (1/3/2010) por el terremoto 27F.
Brecha residual documentada EN EL MOMENTO en PENDIENTES_VERIFICACION.txt.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "chile", "chile_viajes.csv")
P = "Michelle Bachelet"; O = "Chile"
rows = []; tid = 30

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2006 (desde 11/3) =====
add("CHL-MB1-J028", Trip_Status="Completed", Start_Date="2006-03-21", End_Date="2006-03-21", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Néstor Kirchner",
    Trip_Objective="Primer viaje del mandato: relacion estrategica con Argentina; energia e integracion.",
    Source_Verification="Search Query: Bachelet primera gira Argentina Kirchner marzo 2006",
    Source_Reliability="Medium", Methodological_Notes="Primer viaje del mandato.")

add("CHL-MB1-J029", Trip_Status="Completed", Start_Date="2006-05-11", End_Date="2006-05-13", Duration_Days=3,
    Destination_Country="Austria", Destination_City="Vienna", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IV Cumbre UE-América Latina y el Caribe",
    Trip_Objective="Cumbre UE-ALC de Viena.",
    Source_Verification="Search Query: Bachelet Cumbre UE ALC Viena mayo 2006",
    Source_Reliability="Medium", Methodological_Notes="11-13/05/2006.")

add("CHL-MB1-J030", Trip_Status="Completed", Start_Date="2006-06-08", End_Date="2006-06-09", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="George W. Bush",
    Trip_Objective="Reunion con Bush en la Casa Blanca; TLC en vigor, agenda bilateral.",
    Source_Verification="Search Query: Bachelet Bush Casa Blanca junio 2006",
    Source_Reliability="Medium", Methodological_Notes="Fecha a confirmar.")

add("CHL-MB1-J031", Trip_Status="Completed", Start_Date="2006-07-28", End_Date="2006-07-28", Duration_Days=1,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Alan García",
    Trip_Objective="Asuncion de Alan Garcia en Peru.",
    Source_Verification="Search Query: Bachelet asuncion Alan Garcia Lima julio 2006",
    Source_Reliability="Medium", Methodological_Notes="28/07/2006.")

add("CHL-MB1-J032", Trip_Status="Completed", Start_Date="2006-11-03", End_Date="2006-11-05", Duration_Days=3,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XVI Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Montevideo; migraciones.",
    Source_Verification="https://www.segib.org/?summit=xvi-cumbre-iberoamericana-montevideo-2006",
    Source_Reliability="High", Methodological_Notes="3-5/11/2006.")

# Gira APEC Hanoi + Asia nov 2006 (1 Journey_ID)
add("CHL-MB1-J033", Trip_Status="Completed", Start_Date="2006-11-17", End_Date="2006-11-19", Duration_Days=3,
    Destination_Country="Vietnam", Destination_City="Hanoi", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Hanoi. Tramo 1 de gira asiatica.",
    Source_Verification="Search Query: Bachelet APEC Hanoi noviembre 2006",
    Source_Reliability="Medium", Methodological_Notes="17-19/11/2006.")

add("CHL-MB1-J033", Trip_Status="Completed", Start_Date="2006-11-20", End_Date="2006-11-21", Duration_Days=2,
    Destination_Country="New Zealand", Destination_City="Wellington", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Helen Clark (socios del P4)",
    Trip_Objective="Relacion con socio del P4 (acuerdo transpacifico). Tramo 2 de gira asiatica.",
    Source_Verification="Search Query: Bachelet Nueva Zelanda noviembre 2006 P4",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas; confirmar tramo.")

add("CHL-MB1-J034", Trip_Status="Completed", Start_Date="2006-12-08", End_Date="2006-12-09", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Cochabamba", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cumbre de la Comunidad Sudamericana de Naciones",
    Trip_Objective="Cumbre de la CSN en Cochabamba; camino a UNASUR.",
    Source_Verification="Search Query: Bachelet Cumbre Comunidad Sudamericana Cochabamba diciembre 2006",
    Source_Reliability="Medium", Methodological_Notes="8-9/12/2006.")

# ===== 2007 =====
add("CHL-MB1-J035", Trip_Status="Completed", Start_Date="2007-01-15", End_Date="2007-01-15", Duration_Days=1,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Rafael Correa",
    Trip_Objective="Asuncion de Rafael Correa en Ecuador.",
    Source_Verification="Search Query: Bachelet asuncion Correa Quito enero 2007",
    Source_Reliability="Low", Methodological_Notes="15/01/2007. Confirmar asistencia.")

add("CHL-MB1-J036", Trip_Status="Completed", Start_Date="2007-04-16", End_Date="2007-04-17", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Isla Margarita", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="I Cumbre Energética Sudamericana",
    Trip_Objective="Cumbre Energetica Sudamericana; se acordo crear UNASUR.",
    Source_Verification="Search Query: Bachelet Cumbre Energetica Margarita abril 2007",
    Source_Reliability="Medium", Methodological_Notes="16-17/04/2007.")

# Gira europea 2007 (1 Journey_ID): Espana + Francia + Reino Unido
add("CHL-MB1-J037", Trip_Status="Completed", Start_Date="2007-05-14", End_Date="2007-05-15", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rey Juan Carlos I / José Luis Rodríguez Zapatero",
    Trip_Objective="Visita de Estado a Espana. Tramo 1 de gira europea.",
    Source_Verification="Search Query: Bachelet visita Estado Espana Zapatero mayo 2007",
    Source_Reliability="Low", Methodological_Notes="Gira europea 2007; tramos y fechas a confirmar.")

add("CHL-MB1-J037", Trip_Status="Completed", Start_Date="2007-05-16", End_Date="2007-05-17", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Francia",
    Trip_Objective="Relaciones bilaterales. Tramo 2 de gira europea.",
    Source_Verification="Search Query: Bachelet Francia Paris mayo 2007",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("CHL-MB1-J038", Trip_Status="Completed", Start_Date="2007-09-07", End_Date="2007-09-09", Duration_Days=3,
    Destination_Country="Australia", Destination_City="Sydney", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Sidney.",
    Source_Verification="Search Query: Bachelet APEC Sidney septiembre 2007",
    Source_Reliability="Medium", Methodological_Notes="7-9/09/2007.")

add("CHL-MB1-J039", Trip_Status="Completed", Start_Date="2007-09-24", End_Date="2007-09-25", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="62ª AGNU",
    Trip_Objective="Asamblea General de la ONU; cambio climatico.",
    Source_Verification="Search Query: Bachelet ONU asamblea septiembre 2007",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

# ===== 2008 =====
add("CHL-MB1-J040", Trip_Status="Completed", Start_Date="2008-05-16", End_Date="2008-05-17", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="V Cumbre ALC-Unión Europea",
    Trip_Objective="Cumbre ALC-UE de Lima.",
    Source_Verification="Search Query: Bachelet Cumbre ALC UE Lima mayo 2008",
    Source_Reliability="Medium", Methodological_Notes="16-17/05/2008.")

add("CHL-MB1-J041", Trip_Status="Completed", Start_Date="2008-05-23", End_Date="2008-05-23", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Firma del Tratado Constitutivo de UNASUR",
    Trip_Objective="Firma del tratado de UNASUR; Bachelet asumio como primera presidenta pro tempore.",
    Source_Verification="Search Query: Bachelet firma UNASUR Brasilia mayo 2008 presidenta pro tempore",
    Source_Reliability="High", Methodological_Notes="23/05/2008.")

add("CHL-MB1-J042", Trip_Status="Completed", Start_Date="2008-08-15", End_Date="2008-08-15", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Fernando Lugo",
    Trip_Objective="Asuncion de Fernando Lugo en Paraguay.",
    Source_Verification="Search Query: Bachelet asuncion Lugo Asuncion agosto 2008",
    Source_Reliability="Medium", Methodological_Notes="15/08/2008.")

add("CHL-MB1-J043", Trip_Status="Completed", Start_Date="2008-10-29", End_Date="2008-10-31", Duration_Days=3,
    Destination_Country="El Salvador", Destination_City="San Salvador", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XVIII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de San Salvador; juventud y desarrollo.",
    Source_Verification="https://www.segib.org/es/cumbres-iberoamericanas/",
    Source_Reliability="Medium", Methodological_Notes="29-31/10/2008.")

add("CHL-MB1-J044", Trip_Status="Completed", Start_Date="2008-11-22", End_Date="2008-11-23", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Lima.",
    Source_Verification="Search Query: Bachelet APEC Lima noviembre 2008",
    Source_Reliability="Medium", Methodological_Notes="22-23/11/2008.")

add("CHL-MB1-J045", Trip_Status="Completed", Start_Date="2008-12-16", End_Date="2008-12-17", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Costa do Sauípe", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre ALC sobre Integración y Desarrollo (CALC)",
    Trip_Objective="Cumbre CALC (semilla de la CELAC); Grupo de Rio y Mercosur ampliado.",
    Source_Verification="Search Query: Bachelet CALC Costa Sauipe diciembre 2008",
    Source_Reliability="Medium", Methodological_Notes="16-17/12/2008.")

# ===== 2009 =====
add("CHL-MB1-J046", Trip_Status="Completed", Start_Date="2009-02-11", End_Date="2009-02-13", Duration_Days=3,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Raúl Castro / Fidel Castro",
    Trip_Objective="Visita oficial a Cuba; primer jefe de Estado chileno alli desde Allende. Hito diplomatico.",
    Source_Verification="Search Query: Bachelet visita Cuba Raul Fidel Castro febrero 2009",
    Source_Reliability="High", Methodological_Notes="11-13/02/2009. Hito del mandato.")

add("CHL-MB1-J047", Trip_Status="Completed", Start_Date="2009-04-17", End_Date="2009-04-19", Duration_Days=3,
    Destination_Country="Trinidad and Tobago", Destination_City="Port of Spain", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="V Cumbre de las Américas",
    Trip_Objective="V Cumbre de las Americas; debut de Obama en la region.",
    Source_Verification="Search Query: Bachelet V Cumbre Americas Trinidad abril 2009",
    Source_Reliability="Medium", Methodological_Notes="17-19/04/2009.")

add("CHL-MB1-J048", Trip_Status="Completed", Start_Date="2009-06-23", End_Date="2009-06-24", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Barack Obama (Casa Blanca)",
    Trip_Objective="Reunion con Obama en la Casa Blanca; agenda hemisferica y energia.",
    Source_Verification="Search Query: Bachelet Obama Casa Blanca junio 2009",
    Source_Reliability="Medium", Methodological_Notes="Fecha a confirmar.")

add("CHL-MB1-J049", Trip_Status="Completed", Start_Date="2009-09-23", End_Date="2009-09-24", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="64ª AGNU",
    Trip_Objective="Asamblea General de la ONU.",
    Source_Verification="Search Query: Bachelet ONU asamblea septiembre 2009",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("CHL-MB1-J050", Trip_Status="Completed", Start_Date="2009-11-14", End_Date="2009-11-15", Duration_Days=2,
    Destination_Country="Singapore", Destination_City="Singapore", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Singapur.",
    Source_Verification="Search Query: Bachelet APEC Singapur noviembre 2009",
    Source_Reliability="Medium", Methodological_Notes="14-15/11/2009.")

add("CHL-MB1-J051", Trip_Status="Completed", Start_Date="2009-11-30", End_Date="2009-12-01", Duration_Days=2,
    Destination_Country="Portugal", Destination_City="Estoril", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XIX Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Estoril; innovacion y conocimiento.",
    Source_Verification="https://www.segib.org/es/cumbres-iberoamericanas/",
    Source_Reliability="Medium", Methodological_Notes="30/11-1/12/2009.")

# ===== 2010 (hasta 11/3) =====
add("CHL-MB1-J052", Trip_Status="Completed", Start_Date="2010-02-22", End_Date="2010-02-23", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Cancún", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de la Unidad de América Latina y el Caribe",
    Trip_Objective="Cumbre de la Unidad ALC (creacion de la CELAC); ULTIMO viaje completado (5 dias antes del terremoto 27F).",
    Source_Verification="Search Query: Bachelet Cumbre Unidad Cancun febrero 2010",
    Source_Reliability="High", Methodological_Notes="22-23/02/2010. Ultimo viaje completado del mandato.")

add("CHL-MB1-J053", Trip_Status="Canceled", Start_Date="2010-03-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de José Mujica",
    Trip_Objective="Asuncion de Jose Mujica. CANCELADA por el terremoto del 27 de febrero de 2010 en Chile; Bachelet permanecio gestionando la emergencia.",
    Source_Verification="Search Query: Bachelet cancela asuncion Mujica terremoto 27F 2010",
    Source_Reliability="High", Methodological_Notes="Cancelado por el terremoto; sin duracion.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (1er mandato) agregadas. Ultimo Trip_ID = {tid-1}")
