# -*- coding: utf-8 -*-
"""
Mauricio Macri (2015-12-10 a 2019-12-10). Continua Trip_ID tras CFK (ultimo=125).
~46 visitas-pais verificadas + 3 cancelados. Giras multipais = 1 Journey_ID.
Correcciones del informe: Davos solo 2016 y 2018; NO asuncion Bolsonaro 1/1/2019 (lo visito 16/1);
NO Iberoamericanas Cartagena 2016 ni Antigua 2018 (fue Michetti); NO ONU 2017 (fue Michetti).
Excluidos por ser en Argentina: Obama mar2016, OMC dic2017, G20 BsAs 2018, Mercosur Mendoza 2017 y Santa Fe 2019.
Fuentes: Casa Rosada, Cancilleria AR, La Nacion, Infobae, Perfil, Ambito, Telam, Chequeado, El Cronista, AA.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")
P = "Mauricio Macri"; O = "Argentina"
rows = []; tid = 126

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# 2015
add("ARG-MM-J117", Trip_Status="Completed", Start_Date="2015-12-21", End_Date="2015-12-21", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="49ª Cumbre del MERCOSUR",
    Trip_Objective="Primera actividad internacional; pidio liberacion de presos politicos en Venezuela. Con Cartes, Bachelet, Tabare, Dilma, Evo.",
    Source_Verification="https://www.cronista.com/economia-politica/Primeros-viajes-oficiales-que-destinos-eligieron-los-ex-presidentes-20200116-0035.html",
    Source_Reliability="High", Methodological_Notes="Primer viaje del mandato.")

# 2016
add("ARG-MM-J118", Trip_Status="Completed", Start_Date="2016-01-07", End_Date="2016-01-07", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Colonia del Sacramento", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Tabaré Vázquez",
    Trip_Objective="Relanzar relacion bilateral; candidatura conjunta Mundial 2030.",
    Source_Verification="Search Query: Macri Tabare Vazquez Colonia enero 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J119", Trip_Status="Completed", Start_Date="2016-01-20", End_Date="2016-01-23", Duration_Days=4,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Primer presidente argentino en el WEF desde Duhalde (2003); atraer inversiones. Reuniones con Biden, Cameron, Netanyahu.",
    Source_Verification="https://www.lanacion.com.ar/politica/las-claves-del-viaje-que-se-trajo-macri-de-las-montanas-de-davos-nid1864404/",
    Source_Reliability="High", Methodological_Notes="Acompanado por Sergio Massa.")

add("ARG-MM-J120", Trip_Status="Completed", Start_Date="2016-02-27", End_Date="2016-02-27", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Papa Francisco",
    Trip_Objective="Primera audiencia con el Papa argentino.",
    Source_Verification="Search Query: Macri primera audiencia Papa Francisco Vaticano febrero 2016",
    Source_Reliability="Medium", Methodological_Notes="Combinada con Italia/Roma.")

add("ARG-MM-J121", Trip_Status="Completed", Start_Date="2016-03-31", End_Date="2016-04-01", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Seguridad Nuclear (Obama)",
    Trip_Objective="Nuclear Security Summit; reunion con Obama.",
    Source_Verification="Search Query: Macri Cumbre Seguridad Nuclear Washington Obama marzo abril 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J122", Trip_Status="Completed", Start_Date="2016-06-15", End_Date="2016-06-16", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Juan Manuel Santos",
    Trip_Objective="Comercio, inversiones, proceso de paz colombiano.",
    Source_Verification="Search Query: Macri Colombia Santos Bogota Medellin junio 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J123", Trip_Status="Completed", Start_Date="2016-06-30", End_Date="2016-07-01", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Puerto Varas", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XI Cumbre Alianza del Pacífico",
    Trip_Objective="Acercamiento Mercosur-Alianza del Pacifico (Argentina observador).",
    Source_Verification="Search Query: Macri Cumbre Alianza Pacifico Puerto Varas Chile julio 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

# Gira Europa+EEUU julio 2016 (1 Journey_ID)
add("ARG-MM-J124", Trip_Status="Completed", Start_Date="2016-07-02", End_Date="2016-07-02", Duration_Days=1,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="François Hollande",
    Trip_Objective="Relaciones bilaterales, inversiones, acuerdo Mercosur-UE. Tramo 1 de gira europea.",
    Source_Verification="http://www.lanacion.com.ar/1914428-mauricio-macri-viaje-francia-alemania-belgica-estados-unidos",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J124", Trip_Status="Completed", Start_Date="2016-07-03", End_Date="2016-07-04", Duration_Days=2,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Tusk; rey Felipe de Bélgica",
    Trip_Objective="Negociacion con la UE. Tramo 2 de gira europea.",
    Source_Verification="http://www.lanacion.com.ar/1914428-mauricio-macri-viaje-francia-alemania-belgica-estados-unidos",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J124", Trip_Status="Completed", Start_Date="2016-07-05", End_Date="2016-07-06", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Angela Merkel; Joachim Gauck",
    Trip_Objective="Relaciones bilaterales, inversiones (Mercedes, Volkswagen, Siemens). Tramo 3.",
    Source_Verification="http://www.lanacion.com.ar/1914428-mauricio-macri-viaje-francia-alemania-belgica-estados-unidos",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J124", Trip_Status="Completed", Start_Date="2016-07-07", End_Date="2016-07-08", Duration_Days=2,
    Destination_Country="United States", Destination_City="Sun Valley", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Sun Valley Conference (Allen & Co)",
    Trip_Objective="Encuentro con lideres empresariales/tecnologicos en Idaho. Tramo 4 (final).",
    Source_Verification="http://www.lanacion.com.ar/1914428-mauricio-macri-viaje-francia-alemania-belgica-estados-unidos",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J125", Trip_Status="Completed", Start_Date="2016-07-28", End_Date="2016-07-28", Duration_Days=1,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Pedro Pablo Kuczynski",
    Trip_Objective="Representar a Argentina en el cambio de mando.",
    Source_Verification="Search Query: Macri asuncion Kuczynski Lima julio 2016",
    Source_Reliability="Medium", Methodological_Notes="Fecha a confirmar.")

add("ARG-MM-J126", Trip_Status="Completed", Start_Date="2016-08-05", End_Date="2016-08-05", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Apertura JJOO Río 2016",
    Trip_Objective="Asistir a la inauguracion olimpica (invitado por Dilma).",
    Source_Verification="Search Query: Macri apertura Juegos Olimpicos Rio agosto 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

# Gira Qatar+China sept 2016 (G20 Hangzhou)
add("ARG-MM-J127", Trip_Status="Completed", Start_Date="2016-09-03", End_Date="2016-09-03", Duration_Days=1,
    Destination_Country="Qatar", Destination_City="Doha", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emir Tamim bin Hamad Al Thani",
    Trip_Objective="Inversiones; inicio de gira a Asia. Tramo 1.",
    Source_Verification="Search Query: Macri Qatar Doha septiembre 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J127", Trip_Status="Completed", Start_Date="2016-09-04", End_Date="2016-09-05", Duration_Days=2,
    Destination_Country="China", Destination_City="Hangzhou", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Hangzhou",
    Trip_Objective="Participacion en el G20; primer cruce con Putin. Tramo 2.",
    Source_Verification="Search Query: Macri G20 Hangzhou China septiembre 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J128", Trip_Status="Completed", Start_Date="2016-09-19", End_Date="2016-09-21", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="71ª Asamblea General de la ONU",
    Trip_Objective="Primer discurso ante la ONU; Clinton Global Initiative; paseo en bicicleta.",
    Source_Verification="https://www.perfil.com/noticias/politica/macri-viajo-a-nueva-york-para-asistir-a-la-asamblea-general-de-la-onu.phtml",
    Source_Reliability="Medium", Methodological_Notes="Fecha aproximada.")

add("ARG-MM-J129", Trip_Status="Completed", Start_Date="2016-10-15", End_Date="2016-10-15", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Papa Francisco (2da audiencia)",
    Trip_Objective="Segunda visita al Papa; paseo en bicicleta en Roma.",
    Source_Verification="Search Query: Macri segunda audiencia Papa Francisco Roma octubre 2016",
    Source_Reliability="Medium", Methodological_Notes="NA")

# 2017
add("ARG-MM-J130", Trip_Status="Completed", Start_Date="2017-02-20", End_Date="2017-02-25", Duration_Days=6,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rey Felipe VI; Mariano Rajoy",
    Trip_Objective="Visita de Estado; recepcion en el Palacio Real; ~200 empresarios; inversiones.",
    Source_Verification="Search Query: Macri visita de Estado Espana Madrid febrero 2017 rey Felipe",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J131", Trip_Status="Completed", Start_Date="2017-03-16", End_Date="2017-03-16", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Horacio Cartes",
    Trip_Objective="Deuda de Yacyreta; lucha contra el narcotrafico.",
    Source_Verification="Search Query: Macri Paraguay Cartes marzo 2017 Yacyreta",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J132", Trip_Status="Completed", Start_Date="2017-03-27", End_Date="2017-03-28", Duration_Days=2,
    Destination_Country="Netherlands", Destination_City="Amsterdam", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rey Guillermo-Alejandro y reina Máxima",
    Trip_Objective="Foro economico; relaciones bilaterales.",
    Source_Verification="Search Query: Macri Paises Bajos Amsterdam marzo 2017 reina Maxima",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J133", Trip_Status="Completed", Start_Date="2017-04-26", End_Date="2017-04-27", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump",
    Trip_Objective="Primera visita a la Casa Blanca con Trump; comercio (limones), inversiones energeticas (Houston).",
    Source_Verification="Search Query: Macri Trump Casa Blanca abril 2017 limones",
    Source_Reliability="High", Methodological_Notes="Incluyo Houston.")

# Gira Asia mayo 2017 (EAU+China+Japon)
add("ARG-MM-J134", Trip_Status="Completed", Start_Date="2017-05-12", End_Date="2017-05-13", Duration_Days=2,
    Destination_Country="United Arab Emirates", Destination_City="Dubai", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gira Asia (EAU)",
    Trip_Objective="Inversiones; inicio de gira asiatica. Tramo 1.",
    Source_Verification="Search Query: Macri Emiratos Dubai mayo 2017",
    Source_Reliability="Medium", Methodological_Notes="Gira multipais.")

add("ARG-MM-J134", Trip_Status="Completed", Start_Date="2017-05-14", End_Date="2017-05-18", Duration_Days=5,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Foro de la Franja y la Ruta (OBOR) + Visita de Estado a Xi Jinping",
    Trip_Objective="Foro OBOR (Macri y Bachelet unicos de la region); Asociacion Estrategica Integral. Tramo 2.",
    Source_Verification="Search Query: Macri China Foro Franja y Ruta Xi Jinping mayo 2017",
    Source_Reliability="High", Methodological_Notes="45 aniversario de relaciones.")

add("ARG-MM-J134", Trip_Status="Completed", Start_Date="2017-05-18", End_Date="2017-05-19", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Tokyo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Shinzo Abe; Emperador",
    Trip_Objective="Relaciones bilaterales, comercio. Tramo 3 (final).",
    Source_Verification="Search Query: Macri Japon Tokio Abe mayo 2017",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J135", Trip_Status="Completed", Start_Date="2017-05-24", End_Date="2017-05-24", Duration_Days=1,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Lenín Moreno",
    Trip_Objective="Representar a Argentina en el cambio de mando.",
    Source_Verification="Search Query: Macri asuncion Lenin Moreno Quito mayo 2017",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J136", Trip_Status="Completed", Start_Date="2017-06-27", End_Date="2017-06-27", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Michelle Bachelet",
    Trip_Objective="Integracion Mercosur-Alianza del Pacifico.",
    Source_Verification="Search Query: Macri Chile Bachelet Santiago junio 2017",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J137", Trip_Status="Completed", Start_Date="2017-07-07", End_Date="2017-07-08", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Hamburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Hamburgo",
    Trip_Objective="Participacion en el G20; festival Global Citizen con Trudeau.",
    Source_Verification="Search Query: Macri G20 Hamburgo julio 2017",
    Source_Reliability="Medium", Methodological_Notes="NA")

# 2018 - Gira Rusia+Davos+Francia enero (1 Journey_ID)
add("ARG-MM-J138", Trip_Status="Completed", Start_Date="2018-01-22", End_Date="2018-01-23", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Vladímir Putin",
    Trip_Objective="Energia, comercio, cooperacion militar; agradecio apoyo ruso en busqueda del ARA San Juan. Tramo 1.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/eventos-destacados-presi/41683-el-presidente-macri-abre-su-agenda-internacional-de-2018-con-una-gira-por-rusia-suiza-y-francia",
    Source_Reliability="High", Methodological_Notes="Gira Rusia-Suiza-Francia.")

add("ARG-MM-J138", Trip_Status="Completed", Start_Date="2018-01-24", End_Date="2018-01-25", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Diserto en plenario como presidente del G20 (1er sudamericano). Bilaterales con Gates, Merkel, Trudeau, Maxima. Tramo 2.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/eventos-destacados-presi/41683-el-presidente-macri-abre-su-agenda-internacional-de-2018-con-una-gira-por-rusia-suiza-y-francia",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J138", Trip_Status="Completed", Start_Date="2018-01-26", End_Date="2018-01-27", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Destrabar acuerdo Mercosur-UE; compras militares (Super Etendard); cena de honor. Tramo 3 (final).",
    Source_Verification="https://www.infobae.com/politica/2018/01/14/mauricio-macri-visitara-moscu-davos-y-paris-para-atraer-inversiones-extranjeras-y-avanzar-en-el-acuerdo-mercosur-ue/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J139", Trip_Status="Completed", Start_Date="2018-03-11", End_Date="2018-03-11", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Valparaíso", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Sebastián Piñera",
    Trip_Objective="Asuncion de Pinera (2do mandato); bilateral previa en Vina del Mar.",
    Source_Verification="Search Query: Macri asuncion Pinera Valparaiso marzo 2018",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J140", Trip_Status="Completed", Start_Date="2018-04-13", End_Date="2018-04-14", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VIII Cumbre de las Américas",
    Trip_Objective="Agenda hemisferica; crisis de Venezuela.",
    Source_Verification="Search Query: Macri VIII Cumbre Americas Lima abril 2018",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J141", Trip_Status="Completed", Start_Date="2018-06-08", End_Date="2018-06-10", Duration_Days=3,
    Destination_Country="Canada", Destination_City="La Malbaie", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="44ª Cumbre del G7 (invitado)",
    Trip_Objective="Participacion ampliada del G7 en Charlevoix.",
    Source_Verification="Search Query: Macri G7 Charlevoix Canada junio 2018 invitado",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J142", Trip_Status="Completed", Start_Date="2018-08-07", End_Date="2018-08-07", Duration_Days=1,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Iván Duque",
    Trip_Objective="Cambio de mando; reuniones con Pinera y Nikki Haley.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/actividad-oficial/9-noticias/43400-macri-asistio-a-la-ceremonia-de-asuncion-del-nuevo-presidente-de-paraguay",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J143", Trip_Status="Completed", Start_Date="2018-08-15", End_Date="2018-08-15", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Mario Abdo Benítez",
    Trip_Objective="Representar a Argentina en el cambio de mando.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/actividad-oficial/9-noticias/43400-macri-asistio-a-la-ceremonia-de-asuncion-del-nuevo-presidente-de-paraguay",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J144", Trip_Status="Completed", Start_Date="2018-09-24", End_Date="2018-09-25", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="73ª Asamblea General de la ONU",
    Trip_Objective="Discurso; reuniones con inversores y FMI; Global Citizen Award.",
    Source_Verification="Search Query: Macri ONU 73 asamblea septiembre 2018",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J145", Trip_Status="Completed", Start_Date="2018-12-18", End_Date="2018-12-18", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="53ª Cumbre del MERCOSUR",
    Trip_Objective="Argentina recibe presidencia pro tempore; condena a Venezuela; acuerdo con UE.",
    Source_Verification="https://www.infobae.com/politica/2018/12/18/mauricio-macri-asumio-como-presidente-del-mercosur-y-volvio-a-condenar-la-dictadura-en-venezuela/",
    Source_Reliability="High", Methodological_Notes="NA")

# 2019
add("ARG-MM-J146", Trip_Status="Completed", Start_Date="2019-01-16", End_Date="2019-01-16", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jair Bolsonaro",
    Trip_Objective="Primer encuentro presidencial; Mercosur, acuerdo UE, Venezuela. NO asistio a la asuncion del 1/1/2019.",
    Source_Verification="https://www.lanacion.com.ar/politica/macri-brasil-nid2211454/",
    Source_Reliability="High", Methodological_Notes="CORRECCION: no fue a la asuncion de Bolsonaro (1/1); lo visito el 16/1.")

# Gira India+Vietnam feb 2019 (1 Journey_ID)
add("ARG-MM-J147", Trip_Status="Completed", Start_Date="2019-02-17", End_Date="2019-02-19", Duration_Days=3,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Narendra Modi; Ram Nath Kovind",
    Trip_Objective="Visita de Estado; 10 acuerdos (defensa, antartida, agroindustria); foro empresarial. 70 aniversario. Tramo 1.",
    Source_Verification="https://www.ambito.com/macri-llego-nueva-delhi-comenzar-su-visita-estado-la-india-n5016459",
    Source_Reliability="High", Methodological_Notes="Escala breve en Dubai ~16/2.")

add("ARG-MM-J147", Trip_Status="Completed", Start_Date="2019-02-20", End_Date="2019-02-21", Duration_Days=2,
    Destination_Country="Vietnam", Destination_City="Hanoi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Nguyen Xuan Phuc",
    Trip_Objective="Comercio agroindustrial, pesca, biotecnologia. Tramo 2 (final).",
    Source_Verification="https://www.perfil.com/noticias/politica/macri-busca-inversiones-en-su-gira-por-india-y-vietnam.phtml",
    Source_Reliability="Medium", Methodological_Notes="NA")

# Gira Indonesia+Japon junio 2019 (G20 Osaka)
add("ARG-MM-J148", Trip_Status="Completed", Start_Date="2019-06-26", End_Date="2019-06-26", Duration_Days=1,
    Destination_Country="Indonesia", Destination_City="Jakarta", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Joko Widodo",
    Trip_Objective="Ampliar comercio bilateral; escala camino al G20. Tramo 1.",
    Source_Verification="Search Query: Macri Indonesia Yakarta junio 2019 Widodo",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-MM-J148", Trip_Status="Completed", Start_Date="2019-06-27", End_Date="2019-06-29", Duration_Days=3,
    Destination_Country="Japan", Destination_City="Osaka", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Osaka",
    Trip_Objective="Argentina en la troika del G20; anuncio del acuerdo Mercosur-UE (28/6). Bilaterales con Trump, Xi, Macron, Putin. Tramo 2.",
    Source_Verification="Search Query: Macri G20 Osaka junio 2019 acuerdo Mercosur UE",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J149", Trip_Status="Completed", Start_Date="2019-09-24", End_Date="2019-09-25", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="74ª Asamblea General de la ONU",
    Trip_Objective="Ultimo discurso ante la ONU (tras derrota en PASO); reunion con Bachelet por Venezuela; recepcion de Trump.",
    Source_Verification="https://www.infobae.com/politica/2019/09/09/mauricio-macri-hara-un-viaje-relampago-a-la-onu-en-medio-de-la-campana-se-reunira-con-donald-trump-y-xi-jinping/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-MM-J150", Trip_Status="Completed", Start_Date="2019-12-05", End_Date="2019-12-05", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Bento Gonçalves", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="55ª Cumbre del MERCOSUR",
    Trip_Objective="Ultima actividad internacional del mandato; Brasil traspasa presidencia a Paraguay. Con Bolsonaro y Abdo.",
    Source_Verification="https://www.ambito.com/politica/mauricio-macri/macri-pidio-al-gobierno-que-haga-todo-lo-necesario-mantener-la-unidad-del-mercosur-n5217414",
    Source_Reliability="High", Methodological_Notes="Ultimo viaje del mandato.")

# CANCELADOS
add("ARG-MM-J151", Trip_Status="Canceled", Start_Date="2019-04-26", End_Date="NA", Duration_Days="NA",
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron (gira Francia-Bélgica)",
    Trip_Objective="Gira Paris-Bruselas (Macron, OCDE, rey Felipe, UE). CANCELADA por la inflacion (4,7% en marzo) y suba del dolar.",
    Source_Verification="Search Query: Macri suspende gira Francia Belgica abril 2019 inflacion",
    Source_Reliability="High", Methodological_Notes="Cancelado; sin duracion. Anuncio 16/4/2019.")

add("ARG-MM-J152", Trip_Status="Canceled", Start_Date="2019-11-16", End_Date="NA", Duration_Days="NA",
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre APEC / COP25",
    Trip_Objective="Cumbres APEC y COP25 en Chile. CANCELADAS por el pais anfitrion (Pinera) por la crisis social chilena.",
    Source_Verification="Search Query: Chile cancela APEC COP25 2019 crisis social Pinera",
    Source_Reliability="Medium", Methodological_Notes="Cancelado por el anfitrion; sin duracion.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
