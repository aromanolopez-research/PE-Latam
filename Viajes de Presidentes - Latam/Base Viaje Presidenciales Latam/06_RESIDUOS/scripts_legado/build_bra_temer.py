# -*- coding: utf-8 -*-
"""
BRASIL — Michel Temer (12/5/2016 interino; presidente efectivo 31/8/2016 a 1/1/2019, MDB).
Continua Trip_ID tras Dilma (ultimo=186). Journey continua en BRA-MT-J138.
Perfil POCO viajero, pragmatico-comercial ("diplomacia dos resultados").
Informe: 21 desplazamientos a 18 paises, TODOS posteriores al 31/8/2016 (CERO viajes en los
111 dias de interinato). Primer viaje: G20 Hangzhou (sep 2016). Ultimo: MERCOSUR Montevideo (dic 2018).
Asistio a las 3 AGNU, 3 G20 y 3 BRICS de su periodo. Ausencias verificadas: Iberoamericana
Cartagena 2016 y Davos 2017 (sin fila de cancelado por no constar anuncio formal de viaje;
documentadas en pendientes/hallazgos). Se cargan ~17 giras ancladas; brecha ~4 en pendientes.
Correccion del informe: Portugal fue en enero 2017 (funeral de Mario Soares).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Michel Temer"; O = "Brasil"
rows = []; tid = 187

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2016 (desde el 31/8; CERO viajes como interino 12/5-31/8) =====
add("BRA-MT-J138", Trip_Status="Completed", Start_Date="2016-09-02", End_Date="2016-09-05", Duration_Days=4,
    Destination_Country="China", Destination_City="Hangzhou", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Hangzhou",
    Trip_Objective="Debut internacional dias despues de la destitucion de Dilma; busco legitimar su gobierno y atraer inversiones.",
    Source_Verification="Search Query: Temer G20 Hangzhou setembro 2016 primeiro viagem",
    Source_Reliability="High", Methodological_Notes="Primer viaje del mandato efectivo (llegada via Shanghai).")

add("BRA-MT-J139", Trip_Status="Completed", Start_Date="2016-09-20", End_Date="2016-09-20", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="71ª AGNU",
    Trip_Objective="Apertura de la 71a AGNU; defendio la legalidad del impeachment ante criticas regionales.",
    Source_Verification="Search Query: Temer abertura 71 Assembleia Geral ONU setembro 2016",
    Source_Reliability="Medium", Methodological_Notes="20/09/2016.")

add("BRA-MT-J140", Trip_Status="Completed", Start_Date="2016-10-03", End_Date="2016-10-03", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mauricio Macri",
    Trip_Objective="Primera bilateral con Macri; relanzamiento del eje Brasil-Argentina y flexibilizacion del Mercosur.",
    Source_Verification="Search Query: Temer Macri Buenos Aires 3 outubro 2016",
    Source_Reliability="Medium", Methodological_Notes="Fecha a confirmar.")

# Gira India (BRICS Goa) + Japon oct 2016 — 1 Journey_ID
add("BRA-MT-J141", Trip_Status="Completed", Start_Date="2016-10-15", End_Date="2016-10-16", Duration_Days=2,
    Destination_Country="India", Destination_City="Goa", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VIII Cúpula BRICS (Goa)",
    Trip_Objective="Cumbre BRICS de Goa. Tramo 1.",
    Source_Verification="Search Query: Temer cupula BRICS Goa outubro 2016",
    Source_Reliability="Medium", Methodological_Notes="15-16/10/2016.")

add("BRA-MT-J141", Trip_Status="Completed", Start_Date="2016-10-18", End_Date="2016-10-19", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Tokyo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Shinzo Abe",
    Trip_Objective="Visita oficial a Japon; inversiones e infraestructura. Tramo 2 (final).",
    Source_Verification="Search Query: Temer Japao Abe outubro 2016",
    Source_Reliability="Medium", Methodological_Notes="18-19/10/2016.")

# ===== 2017 =====
add("BRA-MT-J142", Trip_Status="Completed", Start_Date="2017-01-10", End_Date="2017-01-10", Duration_Days=1,
    Destination_Country="Portugal", Destination_City="Lisbon", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Funeral de Mário Soares",
    Trip_Objective="Exequias del expresidente portugues Mario Soares.",
    Source_Verification="Search Query: Temer funeral Mario Soares Lisboa janeiro 2017",
    Source_Reliability="Medium", Methodological_Notes="CORRECCION del informe: Portugal fue ene-2017 (funeral), no feb.")

# Gira Rusia + Noruega jun 2017 — 1 Journey_ID
add("BRA-MT-J143", Trip_Status="Completed", Start_Date="2017-06-20", End_Date="2017-06-21", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Vladímir Putin",
    Trip_Objective="Visita oficial a Rusia; comercio e inversiones. Tramo 1.",
    Source_Verification="Search Query: Temer Putin Moscou junho 2017",
    Source_Reliability="Medium", Methodological_Notes="Gira Rusia-Noruega jun 2017.")

add("BRA-MT-J143", Trip_Status="Completed", Start_Date="2017-06-22", End_Date="2017-06-23", Duration_Days=2,
    Destination_Country="Norway", Destination_City="Oslo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Erna Solberg",
    Trip_Objective="Visita a Noruega en plena tension por el recorte noruego al Fondo Amazonia (deforestacion). Tramo 2 (final).",
    Source_Verification="Search Query: Temer Noruega Fundo Amazonia junho 2017",
    Source_Reliability="Medium", Methodological_Notes="22-23/06/2017.")

add("BRA-MT-J144", Trip_Status="Completed", Start_Date="2017-07-07", End_Date="2017-07-08", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Hamburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Hamburgo",
    Trip_Objective="G20 de Hamburgo, semanas despues de la denuncia de Janot; agenda de reformas.",
    Source_Verification="Search Query: Temer G20 Hamburgo julho 2017",
    Source_Reliability="Medium", Methodological_Notes="7-8/07/2017.")

add("BRA-MT-J145", Trip_Status="Completed", Start_Date="2017-08-31", End_Date="2017-09-05", Duration_Days=6,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Xi Jinping + IX Cúpula BRICS (Xiamen)",
    Trip_Objective="Visita de Estado a China (Pekin 1/9) y cumbre BRICS de Xiamen (4-5/9); inversiones en infraestructura.",
    Source_Verification="Search Query: Temer visita Estado China BRICS Xiamen setembro 2017",
    Source_Reliability="Medium", Methodological_Notes="Una salida: visita de Estado + BRICS en el mismo pais.")

add("BRA-MT-J146", Trip_Status="Completed", Start_Date="2017-09-19", End_Date="2017-09-19", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="72ª AGNU",
    Trip_Objective="Apertura de la 72a AGNU; cena con Trump y lideres latinoamericanos sobre Venezuela.",
    Source_Verification="Search Query: Temer abertura 72 Assembleia ONU setembro 2017 jantar Trump",
    Source_Reliability="Medium", Methodological_Notes="19/09/2017.")

# ===== 2018 =====
add("BRA-MT-J147", Trip_Status="Completed", Start_Date="2018-01-24", End_Date="2018-01-24", Duration_Days=1,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Discurso en Davos vendiendo la agenda de reformas (laboral, techo de gasto); primer presidente brasileno en el WEF desde Lula.",
    Source_Verification="Search Query: Temer Davos janeiro 2018 discurso",
    Source_Reliability="Medium", Methodological_Notes="24/01/2018. En 2017 NO fue (ausencia verificada).")

add("BRA-MT-J148", Trip_Status="Completed", Start_Date="2018-04-13", End_Date="2018-04-14", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VIII Cúpula das Américas",
    Trip_Objective="VIII Cumbre de las Americas en Lima (sin Trump, que cancelo); crisis venezolana en agenda.",
    Source_Verification="Search Query: Temer VIII Cupula das Americas Lima abril 2018",
    Source_Reliability="Medium", Methodological_Notes="13-14/04/2018. Confirmar duracion exacta de su presencia.")

add("BRA-MT-J149", Trip_Status="Completed", Start_Date="2018-07-26", End_Date="2018-07-27", Duration_Days=2,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="X Cúpula BRICS",
    Trip_Objective="Cumbre BRICS de Johannesburgo; decima cumbre del bloque.",
    Source_Verification="Search Query: Temer cupula BRICS Joanesburgo julho 2018",
    Source_Reliability="Medium", Methodological_Notes="26-27/07/2018.")

add("BRA-MT-J150", Trip_Status="Completed", Start_Date="2018-08-15", End_Date="2018-08-15", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Mario Abdo Benítez",
    Trip_Objective="Asuncion de Mario Abdo Benitez en Paraguay.",
    Source_Verification="Search Query: Temer posse Mario Abdo Benitez Assuncao agosto 2018",
    Source_Reliability="Medium", Methodological_Notes="15/08/2018. Confirmar asistencia.")

add("BRA-MT-J151", Trip_Status="Completed", Start_Date="2018-09-25", End_Date="2018-09-25", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="73ª AGNU",
    Trip_Objective="Ultima apertura de la AGNU de su mandato.",
    Source_Verification="Search Query: Temer abertura 73 Assembleia ONU setembro 2018",
    Source_Reliability="Medium", Methodological_Notes="25/09/2018.")

add("BRA-MT-J152", Trip_Status="Completed", Start_Date="2018-11-30", End_Date="2018-12-01", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Buenos Aires",
    Trip_Objective="G20 de Buenos Aires (primero en Sudamerica); firma del acuerdo automotriz con Argentina.",
    Source_Verification="Search Query: Temer G20 Buenos Aires novembro dezembro 2018",
    Source_Reliability="High", Methodological_Notes="30/11-1/12/2018.")

add("BRA-MT-J153", Trip_Status="Completed", Start_Date="2018-12-18", End_Date="2018-12-18", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="53ª Cúpula do MERCOSUL",
    Trip_Objective="Ultima cumbre del Mercosur y ULTIMO viaje internacional del mandato.",
    Source_Verification="Search Query: Temer cupula Mercosul Montevideu 18 dezembro 2018",
    Source_Reliability="Medium", Methodological_Notes="18/12/2018. Ultimo viaje del mandato.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
