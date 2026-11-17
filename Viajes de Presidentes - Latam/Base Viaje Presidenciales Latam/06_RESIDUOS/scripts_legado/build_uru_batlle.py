# -*- coding: utf-8 -*-
"""
URUGUAY — Jorge Batlle Ibanez (Partido Colorado, 2000-03-01 a 2005-03-01). PRIMER bloque uruguayo.
Investigacion dedicada (modo investigador, 2026-07-08): 20 viajes fisicos (Journey_ID), 23 filas pais.
19 giras completadas (22 filas) + 1 cancelada (Guayaquil jul-2002 por crisis financiera).
Cierra la brecha previa (estimada 12-20) por el extremo alto.
Fuente gold standard: venias parlamentarias art.170 via vLex + actas ONU (undocs.org) + State Dept + SEGIB + Congreso de Espania.
Trip_ID arranca en 1 (Uruguay es pais nuevo). Convencion Journey: URU-JB-JXXX.
Crea el CSV del modulo uruguay con encabezado (primer bloque del pais).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "uruguay", "uruguay_viajes.csv")
P = "Jorge Batlle"; O = "Uruguay"
rows = []; tid = 1

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

add("URU-JB-J001", Trip_Status="Completed", Start_Date="2000-06-30", End_Date="2000-06-30", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del MERCOSUR",
    Trip_Objective="Cumbre semestral del MERCOSUR; defendio el ingreso de Chile.",
    Source_Verification="https://www.cidob.org/lider-politico/jorge-luis-batlle-ibanez",
    Source_Reliability="High", Methodological_Notes="Duracion estimada 1 dia.", Tema_Foro="Comercio/Integración Económica")

add("URU-JB-J002", Trip_Status="Completed", Start_Date="2000-08-31", End_Date="2000-09-01", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="I Reunion de Presidentes de America del Sur",
    Trip_Objective="Primera cumbre sudamericana; Comunicado de Brasilia (IIRSA).",
    Source_Verification="http://integracionsur.com/wp-content/uploads/2016/11/CumbreSudamericanaBrasilia2000.pdf",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-JB-J003", Trip_Status="Completed", Start_Date="2000-09-06", End_Date="2000-09-08", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del Milenio / 55º AGNU",
    Trip_Objective="Intervencion presidencial en la Cumbre del Milenio (8-sep-2000).",
    Source_Verification="http://undocs.org/en/A/55/PV.7",
    Source_Reliability="High", Methodological_Notes="Fechas cubren la Cumbre del Milenio 6-8 sep.", Tema_Foro="Cooperación Política General")

add("URU-JB-J004", Trip_Status="Completed", Start_Date="2001-04-20", End_Date="2001-04-22", Duration_Days=3,
    Destination_Country="Canada", Destination_City="Quebec City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="III Cumbre de las Américas",
    Trip_Objective="III Cumbre de las Americas (Carta Democratica, ALCA).",
    Source_Verification="https://summit-americas.org/sas/Cumbres_previas_IIICumbre.html",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-JB-J005", Trip_Status="Completed", Start_Date="2001-11-08", End_Date="2001-11-10", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="56º período AGNU",
    Trip_Objective="Intervencion presidencial en el debate general (10-nov-2001); venia art.170 del 8-nov.",
    Source_Verification="https://uy.vlex.com/vid/gobiernos-departamentales-organismos-prestacion-899401057",
    Source_Reliability="High", Methodological_Notes="Debate pospuesto a noviembre por los atentados del 11-S.", Tema_Foro="Cooperación Política General")

add("URU-JB-J006", Trip_Status="Completed", Start_Date="2002-02-11", End_Date="2002-02-16", Duration_Days=6,
    Destination_Country="United States", Destination_City="Washington DC", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de EEUU (administracion Bush)",
    Trip_Objective="Visita de trabajo oficial a EEUU; venia art.170 a partir del 10-feb-2002.",
    Source_Verification="https://history.state.gov/departmenthistory/visits/uruguay",
    Source_Reliability="High")

add("URU-JB-J007", Trip_Status="Completed", Start_Date="2002-02-18", End_Date="2002-02-18", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre informal del MERCOSUR",
    Trip_Objective="Cumbre presidencial del MERCOSUR; transmitio a Duhalde mensajes de Bush y del FMI.",
    Source_Verification="http://archivo.presidencia.gub.uy/noticias/archivo/2002/febrero/2002021916.htm",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada; comunicado presidencial del 19-feb-2002.", Tema_Foro="Comercio/Integración Económica")

add("URU-JB-J008", Trip_Status="Completed", Start_Date="2002-06-04", End_Date="2002-06-04", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Presidente Eduardo Duhalde",
    Trip_Objective="Disculpas en Olivos tras la entrevista con Bloomberg TV difundida el 3-jun-2002 (frase 'manga de ladrones').",
    Source_Verification="Search Query: Batlle disculpas Duhalde Olivos manga de ladrones junio 2002",
    Source_Reliability="Medium", Methodological_Notes="Fecha citada por prensa; venia no localizada.")

add("URU-JB-J009", Trip_Status="Canceled", Start_Date="2002-07-26", End_Date="NA", Duration_Days="NA",
    Destination_Country="Ecuador", Destination_City="Guayaquil", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="II Cumbre Sudamericana",
    Trip_Objective="Cumbre sudamericana; CANCELADA por la crisis financiera; asistio el vicepresidente Hierro Lopez.",
    Source_Verification="https://www.cidob.org/lider-politico/jorge-luis-batlle-ibanez",
    Source_Reliability="High", Methodological_Notes="Feriado bancario decretado el 30-jul-2002.", Tema_Foro="Cooperación Política General")

add("URU-JB-J010", Trip_Status="Completed", Start_Date="2002-12-05", End_Date="2002-12-06", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del MERCOSUR de Brasilia",
    Trip_Objective="Cumbre semestral del MERCOSUR.",
    Source_Verification="Search Query: Batlle cumbre Mercosur Brasilia diciembre 2002",
    Source_Reliability="Medium", Methodological_Notes="Asistencia presidencial no confirmada nominalmente (candidata a PENDIENTES).", Tema_Foro="Comercio/Integración Económica")

add("URU-JB-J011", Trip_Status="Completed", Start_Date="2003-04-23", End_Date="2003-04-23", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington DC", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Presidente George W. Bush (Casa Blanca)",
    Trip_Objective="Visita de trabajo a la Casa Blanca un mes tras el inicio de la guerra de Irak.",
    Source_Verification="https://history.state.gov/departmenthistory/visits/uruguay",
    Source_Reliability="High")

add("URU-JB-J012", Trip_Status="Completed", Start_Date="2003-08-25", End_Date="2003-08-27", Duration_Days=3,
    Destination_Country="Puerto Rico", Destination_City="San Juan", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno del Estado Libre Asociado de Puerto Rico",
    Trip_Objective="Visita oficial a Puerto Rico; venia art.170 concedida el 21-ago-2003.",
    Source_Verification="https://uy.vlex.com/vid/ciudad-educativa-san-ramon-899450907",
    Source_Reliability="High", Methodological_Notes="Fecha estimada; venia sin fecha exacta de salida.")

add("URU-JB-J012", Trip_Status="Completed", Start_Date="2003-08-27", End_Date="2003-08-28", Duration_Days=2,
    Destination_Country="United States", Destination_City="Miami", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Encuentro de empresarios uruguayos",
    Trip_Objective="Encuentro de empresarios uruguayos en Florida (misma venia que Puerto Rico).",
    Source_Verification="https://uy.vlex.com/vid/ciudad-educativa-san-ramon-899450907",
    Source_Reliability="High", Methodological_Notes="Fecha estimada; leg de la gira con Puerto Rico.")

add("URU-JB-J013", Trip_Status="Completed", Start_Date="2003-10-11", End_Date="2003-10-12", Duration_Days=2,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Santa Sede (Juan Pablo II)",
    Trip_Objective="Visita oficial al Vaticano; venia art.170 a partir del 11-oct-2003.",
    Source_Verification="https://uy.vlex.com/vid/servicio-retiro-pensiones-policiales-899398597",
    Source_Reliability="High", Methodological_Notes="Fecha de leg estimada.")

add("URU-JB-J013", Trip_Status="Completed", Start_Date="2003-10-13", End_Date="2003-10-14", Duration_Days=2,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de la Republica Italiana",
    Trip_Objective="Visita oficial a Italia (misma venia).",
    Source_Verification="https://uy.vlex.com/vid/servicio-retiro-pensiones-policiales-899398597",
    Source_Reliability="High", Methodological_Notes="Fecha de leg estimada.")

add("URU-JB-J013", Trip_Status="Completed", Start_Date="2003-10-15", End_Date="2003-10-17", Duration_Days=3,
    Destination_Country="Angola", Destination_City="Luanda", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de la Republica de Angola",
    Trip_Objective="Visita oficial a Angola (misma venia).",
    Source_Verification="https://uy.vlex.com/vid/servicio-retiro-pensiones-policiales-899398597",
    Source_Reliability="High", Methodological_Notes="Fecha de leg estimada.")

add("URU-JB-J014", Trip_Status="Completed", Start_Date="2003-11-14", End_Date="2003-11-15", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Santa Cruz de la Sierra", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XIII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana; firmo TLC con Mexico (Fox) el 15-nov.",
    Source_Verification="https://segib.org/es/xiii-cumbre-iberoamericana-inclusion-social-como-motor-del-desarrollo-de-la-region/",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-JB-J015", Trip_Status="Completed", Start_Date="2004-01-12", End_Date="2004-01-13", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Monterrey", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre Extraordinaria de las Américas",
    Trip_Objective="Cumbre Extraordinaria (Declaracion de Nuevo Leon).",
    Source_Verification="https://summit-americas.org/sas/Cumbres_previas_CumbreExtraordinaria.html",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-JB-J016", Trip_Status="Completed", Start_Date="2004-02-02", End_Date="2004-02-02", Duration_Days=1,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Congreso de los Diputados de Espania",
    Trip_Objective="Visita a Espania y al Congreso de los Diputados.",
    Source_Verification="https://www.congreso.es/es/cem/visituruguay2004",
    Source_Reliability="High", Methodological_Notes="Fecha confirmada por fuente oficial primaria (Congreso de los Diputados).")

add("URU-JB-J017", Trip_Status="Completed", Start_Date="2004-04-24", End_Date="2004-04-25", Duration_Days=2,
    Destination_Country="Democratic Republic of the Congo", Destination_City="Kinshasa", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Presidente Joseph Kabila / contingente MONUC",
    Trip_Objective="Primer presidente uruguayo en visitar la RDC; visito los cascos azules de MONUC y firmo declaracion conjunta.",
    Source_Verification="https://en.wikipedia.org/wiki/Democratic_Republic_of_the_Congo%E2%80%93Uruguay_relations",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada ('fines de abril 2004').")

add("URU-JB-J018", Trip_Status="Completed", Start_Date="2004-09-22", End_Date="2004-09-23", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="59º período AGNU",
    Trip_Objective="Intervencion presidencial en el debate general (23-sep-2004).",
    Source_Verification="http://undocs.org/en/A/59/PV.8",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-JB-J019", Trip_Status="Completed", Start_Date="2004-11-18", End_Date="2004-11-20", Duration_Days=3,
    Destination_Country="Costa Rica", Destination_City="San José", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XIV Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana (creacion de la SEGIB); venia a partir del 17-nov.",
    Source_Verification="https://uy.vlex.com/vid/900245683",
    Source_Reliability="High", Methodological_Notes="Cumbre los dias 19-20 nov.", Tema_Foro="Cooperación Política General")

add("URU-JB-J020", Trip_Status="Completed", Start_Date="2004-12-16", End_Date="2004-12-17", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Ouro Preto", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XXVII Cumbre del MERCOSUR (CMC)",
    Trip_Objective="Cumbre semestral; venia a partir del 15-dic-2004.",
    Source_Verification="https://uy.vlex.com/vid/900245683",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

# Crear CSV nuevo con encabezado (Uruguay es pais nuevo)
with open(CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader()
    for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
print(f"OK: {len(rows)} filas de {P} escritas en uruguay_viajes.csv. Ultimo Trip_ID = {tid-1}")
