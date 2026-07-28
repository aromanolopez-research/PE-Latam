# -*- coding: utf-8 -*-
"""
CFK segundo mandato (2011-12-10 a 2015-12-10). Continua Trip_ID tras CFK 1er mandato (ultimo=93).
31 viajes completados verificados. Giras multipais = 1 Journey_ID. No-asistencias quedan en bitacora.
Fuentes: La Nacion (radiografia 99 viajes/Boletin Oficial), Cancilleria AR, Casa Rosada, ONU, Infobae, Telam, El Cronista, La Capital, Microjuris.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")
P = "Cristina Fernández de Kirchner"; O = "Argentina"
rows = []; tid = 94

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# 2011
add("ARG-CFK-J087", Trip_Status="Completed", Start_Date="2011-12-20", End_Date="2011-12-20", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XLII Cumbre del MERCOSUR",
    Trip_Objective="Cumbre ordinaria del Mercosur; traspaso de presidencia pro tempore Argentina-Uruguay.",
    Source_Verification="Search Query: Cristina Kirchner Cumbre Mercosur Montevideo diciembre 2011",
    Source_Reliability="Medium", Methodological_Notes="NA")

# 2012
add("ARG-CFK-J088", Trip_Status="Completed", Start_Date="2012-01-15", End_Date="2012-01-15", Duration_Days=1,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Hugo Chávez (convaleciente)",
    Trip_Objective="Visita a Chavez en recuperacion de cirugia oncologica.",
    Source_Verification="Search Query: Cristina Kirchner visita Chavez La Habana enero 2012",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; ocurrio durante su propia recuperacion de tiroides.")

add("ARG-CFK-J089", Trip_Status="Completed", Start_Date="2012-04-14", End_Date="2012-04-15", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VI Cumbre de las Américas",
    Trip_Objective="Cumbre hemisferica; planteo Malvinas. Bilateral con Obama a agenda abierta. Se retiro antes del cierre.",
    Source_Verification="https://cancilleria.gob.ar/es/actualidad/comunicados/visita-de-estado-de-la-presidenta-cristina-fernandez-de-kirchner-brasil",
    Source_Reliability="High", Methodological_Notes="Anfitrion Santos.")

add("ARG-CFK-J090", Trip_Status="Completed", Start_Date="2012-05-17", End_Date="2012-05-18", Duration_Days=2,
    Destination_Country="Angola", Destination_City="Luanda", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="José Eduardo dos Santos",
    Trip_Objective="Mision comercial con ~400 empresarios; linea de credito Banco Nacion US$100M; energia, nuclear, agroindustria.",
    Source_Verification="Search Query: Cristina Kirchner Angola Luanda mayo 2012 mision comercial",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J091", Trip_Status="Completed", Start_Date="2012-06-18", End_Date="2012-06-19", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Los Cabos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Los Cabos",
    Trip_Objective="Foro economico global (crisis europea). Cruce con Cameron por Malvinas.",
    Source_Verification="Search Query: Cristina Kirchner G20 Los Cabos junio 2012",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J092", Trip_Status="Completed", Start_Date="2012-07-31", End_Date="2012-07-31", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre especial MERCOSUR (ingreso de Venezuela)",
    Trip_Objective="Oficializacion del ingreso de Venezuela al Mercosur tras la suspension de Paraguay.",
    Source_Verification="Search Query: Cumbre Mercosur Brasilia julio 2012 ingreso Venezuela Cristina",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J093", Trip_Status="Completed", Start_Date="2012-09-24", End_Date="2012-09-25", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="67ª Asamblea General de la ONU",
    Trip_Objective="Discurso sobre fondos buitre y Malvinas.",
    Source_Verification="Search Query: Cristina Kirchner ONU 67 asamblea septiembre 2012 fondos buitre",
    Source_Reliability="Medium", Methodological_Notes="NA")

# 2013
add("ARG-CFK-J094", Trip_Status="Completed", Start_Date="2013-01-13", End_Date="2013-01-15", Duration_Days=3,
    Destination_Country="United Arab Emirates", Destination_City="Abu Dhabi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gira Asia (EAU)",
    Trip_Objective="Mision comercial con ~200 empresarios. Tramo 1 de gira Asia (EAU-Indonesia-Vietnam).",
    Source_Verification="Search Query: Cristina Kirchner gira Emiratos Indonesia Vietnam enero 2013",
    Source_Reliability="Medium", Methodological_Notes="Gira multipais.")

add("ARG-CFK-J094", Trip_Status="Completed", Start_Date="2013-01-16", End_Date="2013-01-18", Duration_Days=3,
    Destination_Country="Indonesia", Destination_City="Jakarta", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gira Asia (Indonesia)",
    Trip_Objective="Mision comercial. Tramo 2 de gira Asia.",
    Source_Verification="Search Query: Cristina Kirchner Indonesia Yakarta enero 2013",
    Source_Reliability="Medium", Methodological_Notes="Gira multipais.")

add("ARG-CFK-J094", Trip_Status="Completed", Start_Date="2013-01-19", End_Date="2013-01-20", Duration_Days=2,
    Destination_Country="Vietnam", Destination_City="Hanoi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Truong Tan Sang / Nguyen Tan Dung",
    Trip_Objective="Mision comercial. Tramo 3 de gira Asia. Escala tecnica controvertida en Seychelles al regreso.",
    Source_Verification="Search Query: Cristina Kirchner Vietnam enero 2013",
    Source_Reliability="Medium", Methodological_Notes="Vietnam cancelado en dic 2012 y restablecido.")

add("ARG-CFK-J095", Trip_Status="Completed", Start_Date="2013-01-26", End_Date="2013-01-27", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="I Cumbre CELAC-UE / I Cumbre CELAC",
    Trip_Objective="Relacion birregional; bilaterales con Merkel, Pena Nieto, Raul Castro, Pinera, Dilma.",
    Source_Verification="Search Query: Cristina Kirchner Cumbre CELAC-UE Santiago enero 2013",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J096", Trip_Status="Completed", Start_Date="2013-03-06", End_Date="2013-03-07", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Velatorio de Hugo Chávez",
    Trip_Objective="Velatorio de Chavez. Regreso el 7/3; NO asistio al funeral de Estado del 8/3 (hipotension).",
    Source_Verification="https://www.elimpulso.com/2013/04/20/cristina-fernandez-visita-el-cuartel-de-la-montana/",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J097", Trip_Status="Completed", Start_Date="2013-03-18", End_Date="2013-03-19", Duration_Days=2,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Asunción del Papa Francisco",
    Trip_Objective="Misa inaugural del pontificado del primer papa argentino; almuerzo 18/3. Primera jefa de Estado recibida.",
    Source_Verification="https://www.infobae.com/politica/2024/02/12/de-cristina-a-macri-de-alberto-a-milei-fotos-gestos-y-la-duracion-de-las-reuniones-del-papa-francisco-con-los-presidentes-argentinos/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J098", Trip_Status="Completed", Start_Date="2013-04-19", End_Date="2013-04-20", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Asunción de Nicolás Maduro",
    Trip_Objective="Investidura de Maduro (19/4); homenaje en la tumba de Chavez (20/4).",
    Source_Verification="https://www.elimpulso.com/2013/04/20/cristina-fernandez-visita-el-cuartel-de-la-montana/",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J099", Trip_Status="Completed", Start_Date="2013-07-12", End_Date="2013-07-12", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XLV Cumbre del MERCOSUR",
    Trip_Objective="Traspaso de presidencia pro tempore a Venezuela; levantamiento de la suspension de Paraguay.",
    Source_Verification="Search Query: Cumbre Mercosur Montevideo julio 2013 Cristina",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J100", Trip_Status="Completed", Start_Date="2013-07-27", End_Date="2013-07-28", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Papa Francisco (Jornada Mundial de la Juventud)",
    Trip_Objective="Saludar al Papa en la JMJ (su primer viaje internacional).",
    Source_Verification="Search Query: Cristina Kirchner JMJ Rio Papa Francisco julio 2013",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada.")

add("ARG-CFK-J101", Trip_Status="Completed", Start_Date="2013-09-05", End_Date="2013-09-06", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Saint Petersburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de San Petersburgo",
    Trip_Objective="Foro economico; fondos buitre y Siria. Bilaterales con Putin, Xi, India, Japon.",
    Source_Verification="Search Query: Cristina Kirchner G20 San Petersburgo septiembre 2013",
    Source_Reliability="Medium", Methodological_Notes="ASISTIO; la operacion de cabeza fue posterior (8/10/2013).")

add("ARG-CFK-J102", Trip_Status="Completed", Start_Date="2013-09-24", End_Date="2013-09-24", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="68ª Asamblea General de la ONU",
    Trip_Objective="Discurso anual ante la ONU.",
    Source_Verification="Search Query: Cristina Kirchner ONU 68 asamblea 24 septiembre 2013",
    Source_Reliability="Medium", Methodological_Notes="ASISTIO 24/9; operacion subdural posterior (8/10/2013).")

# 2014
add("ARG-CFK-J103", Trip_Status="Completed", Start_Date="2014-01-28", End_Date="2014-01-29", Duration_Days=2,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cumbre de la CELAC",
    Trip_Objective="Cumbre regional CELAC; anfitrion Raul Castro.",
    Source_Verification="https://www.infobae.com/2014/01/25/1539270-cristina-kirchner-viajo-cuba-la-cumbre-la-celac/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J104", Trip_Status="Completed", Start_Date="2014-03-17", End_Date="2014-03-17", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Papa Francisco (audiencia)",
    Trip_Objective="Audiencia papal y almuerzo. Tramo previo a Francia.",
    Source_Verification="https://www.infobae.com/2014/03/05/1548011-cristina-kirchner-viajara-francia-invitada-el-presidente-hollande/",
    Source_Reliability="Medium", Methodological_Notes="Enlazo con viaje a Francia.")

add("ARG-CFK-J105", Trip_Status="Completed", Start_Date="2014-03-18", End_Date="2014-03-20", Duration_Days=3,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="François Hollande",
    Trip_Objective="Relaciones bilaterales; Salon del Libro de Paris (Argentina invitada de honor). Honores militares.",
    Source_Verification="https://www.telam.com.ar/notas/201403/55769-la-presidenta-ya-se-encuentra-en-el-palacio-nacional-de-los-invalidos.html",
    Source_Reliability="Medium", Methodological_Notes="Unico viaje a Francia del 2do mandato.")

add("ARG-CFK-J106", Trip_Status="Completed", Start_Date="2014-06-14", End_Date="2014-06-15", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Santa Cruz de la Sierra", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre G77+China (50° aniversario)",
    Trip_Objective="Foro Sur-Sur 'Hacia un nuevo orden mundial para vivir bien'; anfitrion Evo Morales.",
    Source_Verification="Search Query: Cristina Kirchner G77 China Santa Cruz Bolivia junio 2014",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J107", Trip_Status="Completed", Start_Date="2014-07-15", End_Date="2014-07-16", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Fortaleza", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VI Cumbre BRICS + BRICS-UNASUR",
    Trip_Objective="Invitada a la Cumbre BRICS; lanzamiento del Nuevo Banco de Desarrollo. Bilaterales con Putin, Xi, Modi, Zuma, Dilma.",
    Source_Verification="Search Query: Cristina Kirchner Cumbre BRICS Fortaleza julio 2014",
    Source_Reliability="High", Methodological_Notes="Fortaleza (15/7) y Brasilia (16/7).")

add("ARG-CFK-J108", Trip_Status="Completed", Start_Date="2014-07-29", End_Date="2014-07-29", Duration_Days=1,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="46ª Cumbre del MERCOSUR",
    Trip_Objective="Cumbre del bloque; busco apoyo por los fondos buitre a horas del default tecnico. Anfitrion Maduro.",
    Source_Verification="Search Query: Cumbre Mercosur Caracas julio 2014 Cristina default",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J109", Trip_Status="Completed", Start_Date="2014-09-24", End_Date="2014-09-25", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="69ª Asamblea General de la ONU",
    Trip_Objective="Discurso contra los fondos buitre ('terrorismo economico y financiero').",
    Source_Verification="https://www.lanacion.com.ar/politica/cristina-volvio-a-criticar-a-obama-porsu-postura-ante-siria-y-los-fondos-buitre-nid1617743/",
    Source_Reliability="High", Methodological_Notes="NA")

# 2015
add("ARG-CFK-J110", Trip_Status="Completed", Start_Date="2015-02-02", End_Date="2015-02-05", Duration_Days=4,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Xi Jinping",
    Trip_Objective="Visita de Estado; 15 acuerdos (centrales nucleares IV y V, aeroespacial, swap hasta US$11.000M).",
    Source_Verification="https://www.lanacion.com.ar/el-mundo/el-papa-francisco-llego-a-la-habana-para-una-historica-gira-a-cuba-y-eeuu-nid1829468/",
    Source_Reliability="High", Methodological_Notes="Tuit sobre 'aloz' y 'petloleo'.")

add("ARG-CFK-J111", Trip_Status="Completed", Start_Date="2015-04-10", End_Date="2015-04-11", Duration_Days=2,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VII Cumbre de las Américas",
    Trip_Objective="Cumbre historica por el reingreso de Cuba; critico a Obama por el decreto sobre Venezuela. Reunion con Maduro.",
    Source_Verification="https://www.larepublica.ec/blog/2015/04/11/fernandez-de-kirchner-reclama-sinceridad-a-los-lideres-de-las-americas/",
    Source_Reliability="High", Methodological_Notes="Anfitrion Varela; presentes Obama y Raul Castro.")

add("ARG-CFK-J112", Trip_Status="Completed", Start_Date="2015-04-22", End_Date="2015-04-23", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Vladímir Putin",
    Trip_Objective="Acuerdo Estrategico Integral; ~20 acuerdos (represa Chihuido I, 6ta central nuclear).",
    Source_Verification="Search Query: Cristina Kirchner visita Estado Rusia Moscu abril 2015 Putin Chihuido",
    Source_Reliability="High", Methodological_Notes="Cancilleria.")

add("ARG-CFK-J113", Trip_Status="Completed", Start_Date="2015-07-12", End_Date="2015-07-12", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Papa Francisco (misa)",
    Trip_Objective="Misa de cierre de la gira sudamericana del Papa (Ecuador-Bolivia-Paraguay).",
    Source_Verification="Search Query: Cristina Kirchner misa Papa Francisco Asuncion julio 2015",
    Source_Reliability="Medium", Methodological_Notes="NO fue cumbre Mercosur (esa fue en Brasilia, ver J114).")

add("ARG-CFK-J114", Trip_Status="Completed", Start_Date="2015-07-16", End_Date="2015-07-17", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XLVIII Cumbre del MERCOSUR",
    Trip_Objective="Cumbre del bloque; adhesion de Bolivia; traspaso de presidencia Brasil-Paraguay. Bilateral con Dilma.",
    Source_Verification="https://aldiaargentina.microjuris.com/2015/07/17/cristina-participa-de-la-cumbre-del-mercosur-y-se-reune-con-dilma/",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J115", Trip_Status="Completed", Start_Date="2015-09-19", End_Date="2015-09-20", Duration_Days=2,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Papa Francisco (misa en La Habana)",
    Trip_Objective="Saludar al Papa antes de viajar a Nueva York; tambien Fidel y Raul Castro.",
    Source_Verification="https://www.lanacion.com.ar/el-mundo/el-papa-francisco-llego-a-la-habana-para-una-historica-gira-a-cuba-y-eeuu-nid1829468/",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J116", Trip_Status="Completed", Start_Date="2015-09-27", End_Date="2015-09-28", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="70ª Asamblea General de la ONU",
    Trip_Objective="Ultimo discurso como presidenta (28/9); fondos buitre, AMIA/Iran, pedido por Antonio Stiuso.",
    Source_Verification="https://news.un.org/es/audio/2015/09/1411141",
    Source_Reliability="High", Methodological_Notes="Ultimo viaje internacional del mandato.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (2do mandato) agregadas. Ultimo Trip_ID = {tid-1}")
