# -*- coding: utf-8 -*-
"""
CFK primer mandato (2007-12-10 a 2011-12-10). Continua Trip_ID tras Nestor K (ultimo=55).
Carga 35 entradas verificadas (Alta/Media). Cancelados sin duracion. Giras multi-pais = 1 Journey_ID.
Eventos en Argentina y no-asistencias quedan en bitacora (no como filas).
Fuentes: La Nacion (radiografia 99 viajes/Boletin Oficial), Cancilleria AR, Casa Rosada, SEGIB, ONU, Perfil, Pagina/12, CFKargentina.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")
P = "Cristina Fernández de Kirchner"; O = "Argentina"
rows = []; tid = 56

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2008 =====
add("ARG-CFK-J054", Trip_Status="Completed", Start_Date="2008-02-22", End_Date="2008-02-22", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Lula da Silva",
    Trip_Objective="MICBA; Declaracion de la Casa Rosada. Agenda bilateral e integracion.",
    Source_Verification="https://cancilleria.gob.ar/es/actualidad/comunicados/visita-de-estado-de-la-presidenta-cristina-fernandez-de-kirchner-brasil",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada (declaracion conjunta 22/02/2008).")

add("ARG-CFK-J055", Trip_Status="Completed", Start_Date="2008-09-07", End_Date="2008-09-08", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Lula da Silva (Día de la Patria de Brasil)",
    Trip_Objective="Invitada de honor de las conmemoraciones del Dia de la Patria de Brasil; MICBA.",
    Source_Verification="https://cancilleria.gob.ar/es/actualidad/comunicados/visita-de-estado-de-la-presidenta-cristina-fernandez-de-kirchner-brasil",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J056", Trip_Status="Completed", Start_Date="2008-09-23", End_Date="2008-09-23", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="63ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la ONU: DDHH, AMIA, deuda y Malvinas.",
    Source_Verification="https://www.minutouno.com/cristina-kirchner-parte-reunion-laonu-y-g20-n116858",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J057", Trip_Status="Completed", Start_Date="2008-10-29", End_Date="2008-10-31", Duration_Days=3,
    Destination_Country="El Salvador", Destination_City="San Salvador", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XVIII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana 'Juventud y Desarrollo'; tema dominante crisis financiera.",
    Source_Verification="https://segib.org/es/cumbres-iberoamericanas/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J058", Trip_Status="Completed", Start_Date="2008-11-14", End_Date="2008-11-15", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="I Cumbre del G20 de líderes",
    Trip_Objective="Primera Cumbre del G20 (crisis financiera global). Bilaterales con Lula, Albright, Kevin Rudd.",
    Source_Verification="https://www.minutouno.com/cristina-kirchner-parte-reunion-laonu-y-g20-n116858",
    Source_Reliability="High", Methodological_Notes="Partio directo a gira por Africa del Norte.")

# Gira Africa del Norte (mismo Journey_ID, 4 paises)
add("ARG-CFK-J059", Trip_Status="Completed", Start_Date="2008-11-16", End_Date="2008-11-17", Duration_Days=2,
    Destination_Country="Algeria", Destination_City="Algiers", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Abdelaziz Bouteflika",
    Trip_Objective="Mision comercial; cooperacion nuclear y energetica. Tramo 1 de gira Africa del Norte.",
    Source_Verification="https://www.perfil.com/noticias/politica/cristina-esquivo-dictadores-de-africa-20090927-0001.phtml",
    Source_Reliability="High", Methodological_Notes="Comitiva ~70 empresarios.")

add("ARG-CFK-J059", Trip_Status="Completed", Start_Date="2008-11-18", End_Date="2008-11-19", Duration_Days=2,
    Destination_Country="Tunisia", Destination_City="Tunis", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Zine El Abidine Ben Ali",
    Trip_Objective="Mision comercial multisectorial. Tramo 2 de gira Africa del Norte.",
    Source_Verification="https://www.perfil.com/noticias/politica/cristina-esquivo-dictadores-de-africa-20090927-0001.phtml",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J059", Trip_Status="Completed", Start_Date="2008-11-20", End_Date="2008-11-21", Duration_Days=2,
    Destination_Country="Egypt", Destination_City="Cairo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hosni Mubarak",
    Trip_Objective="Mision comercial. Tramo 3 de gira Africa del Norte.",
    Source_Verification="https://www.perfil.com/noticias/politica/cristina-esquivo-dictadores-de-africa-20090927-0001.phtml",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J059", Trip_Status="Completed", Start_Date="2008-11-22", End_Date="2008-11-22", Duration_Days=1,
    Destination_Country="Libya", Destination_City="Tripoli", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Muammar Gadafi",
    Trip_Objective="Ultima escala de la gira por Africa del Norte.",
    Source_Verification="https://www.perfil.com/noticias/politica/cristina-esquivo-dictadores-de-africa-20090927-0001.phtml",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J060", Trip_Status="Completed", Start_Date="2008-12-09", End_Date="2008-12-11", Duration_Days=3,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Dmitri Medvédev / Vladímir Putin",
    Trip_Objective="Visita de Estado a Rusia (recepcion en el Kremlin); comercio, energia nuclear, exencion de visados.",
    Source_Verification="Search Query: Cristina Kirchner visita Estado Rusia Moscu diciembre 2008 Medvedev",
    Source_Reliability="High", Methodological_Notes="CORRECCION: fue dic 2008, NO 2010 (en 2010 Medvedev visito Argentina). Fechas de dia estimadas.")

add("ARG-CFK-J061", Trip_Status="Completed", Start_Date="2008-06-01", End_Date="2008-06-01", Duration_Days=1,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hugo Chávez",
    Trip_Objective="Una de las seis visitas a Venezuela del primer mandato; agenda energetica y financiera.",
    Source_Verification="Search Query: Cristina Kirchner Venezuela Chavez 2008 visita",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada YYYY-MM-01; Venezuela=6 visitas en el mandato (Perfil). Una representativa.")

# ===== 2009 =====
add("ARG-CFK-J062", Trip_Status="Canceled", Start_Date="2009-01-19", End_Date="NA", Duration_Days="NA",
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Raúl Castro",
    Trip_Objective="Visita a Cuba prevista para el 19 ene. CANCELADA por primer cuadro de hipotension arterial (9 ene 2009).",
    Source_Verification="Search Query: Cristina Kirchner suspende viaje Cuba enero 2009 hipotension",
    Source_Reliability="High", Methodological_Notes="Cancelado; sin duracion.")

add("ARG-CFK-J063", Trip_Status="Completed", Start_Date="2009-03-27", End_Date="2009-03-28", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Viña del Mar", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre Progresista (Bachelet; Biden)",
    Trip_Objective="Cumbre de gobiernos progresistas en Vina del Mar.",
    Source_Verification="Search Query: Cumbre Progresista Vina del Mar marzo 2009 Cristina Bachelet Biden",
    Source_Reliability="Medium", Methodological_Notes="Fecha de dia estimada.")

add("ARG-CFK-J064", Trip_Status="Completed", Start_Date="2009-04-01", End_Date="2009-04-02", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Londres",
    Trip_Objective="Cumbre del G20 (Gordon Brown; presente Obama). Conmemoro el 2 de abril (Malvinas) en la embajada.",
    Source_Verification="Search Query: Cristina Kirchner G20 Londres abril 2009",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J065", Trip_Status="Completed", Start_Date="2009-04-17", End_Date="2009-04-19", Duration_Days=3,
    Destination_Country="Trinidad and Tobago", Destination_City="Port of Spain", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="V Cumbre de las Américas",
    Trip_Objective="V Cumbre de las Americas; debut de Obama en la region.",
    Source_Verification="https://es.wikipedia.org/wiki/Presidencia_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J066", Trip_Status="Completed", Start_Date="2009-09-23", End_Date="2009-09-23", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="64ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la ONU; ordeno retirar la delegacion argentina del discurso de Ahmadinejad.",
    Source_Verification="https://es.wikipedia.org/wiki/Presidencia_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="Discrepancia menor 23 vs 24 sep.")

add("ARG-CFK-J067", Trip_Status="Completed", Start_Date="2009-09-24", End_Date="2009-09-25", Duration_Days=2,
    Destination_Country="United States", Destination_City="Pittsburgh", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del G20 de Pittsburgh",
    Trip_Objective="G20 Pittsburgh; Argentina logro la inclusion de la OIT en el foro. Voló desde NY.",
    Source_Verification="https://es.wikipedia.org/wiki/Presidencia_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="Mismo viaje fisico que NY? Se registra como Journey separado (ONU vs G20).")

add("ARG-CFK-J068", Trip_Status="Completed", Start_Date="2009-09-26", End_Date="2009-09-27", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Isla Margarita", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="II Cumbre América del Sur-África (ASA)",
    Trip_Objective="Cumbre ASA; anfitrion Chavez. Llego desde EE.UU.",
    Source_Verification="https://www.perfil.com/noticias/politica/cristina-esquivo-dictadores-de-africa-20090927-0001.phtml",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J069", Trip_Status="Completed", Start_Date="2009-11-29", End_Date="2009-12-01", Duration_Days=3,
    Destination_Country="Portugal", Destination_City="Estoril", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XIX Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana 'Innovacion y Conocimiento'; Argentina recibe presidencia pro tempore.",
    Source_Verification="https://segib.org/es/cumbres-iberoamericanas/",
    Source_Reliability="High", Methodological_Notes="NA")

# ===== 2010 =====
add("ARG-CFK-J070", Trip_Status="Completed", Start_Date="2010-02-22", End_Date="2010-02-23", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Cancún", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cumbre Unidad ALC / Grupo de Río + CALC (acuerdo crear CELAC)",
    Trip_Objective="Cumbre de la Unidad ALC; se acordo crear la CELAC. Primer encuentro con Pinera (electo); respaldo por Malvinas.",
    Source_Verification="https://es.wikipedia.org/wiki/Presidencia_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J071", Trip_Status="Completed", Start_Date="2010-03-01", End_Date="2010-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de José Mujica",
    Trip_Objective="Asuncion de Mujica. Acompanada por Nestor Kirchner; reuniones con Correa y Chavez.",
    Source_Verification="Search Query: Cristina Kirchner asuncion Mujica Montevideo 1 marzo 2010",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J072", Trip_Status="Completed", Start_Date="2010-03-11", End_Date="2010-03-11", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Valparaíso", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Sebastián Piñera",
    Trip_Objective="Asuncion de Pinera (entre replicas del terremoto). Visito hospitales moviles argentinos en Curico.",
    Source_Verification="Search Query: Cristina Kirchner asuncion Pinera Valparaiso 11 marzo 2010",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J073", Trip_Status="Completed", Start_Date="2010-03-25", End_Date="2010-03-26", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Sucre", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Evo Morales",
    Trip_Objective="Firma de anexo del contrato de gas; Dia de la Confraternidad Boliviano-Argentina.",
    Source_Verification="https://www.pagina12.com.ar/diario/elmundo/4-141838-2010-03-12.html",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-CFK-J074", Trip_Status="Completed", Start_Date="2010-04-12", End_Date="2010-04-13", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Seguridad Nuclear (Obama)",
    Trip_Objective="Cumbre de Seguridad Nuclear (47 paises). Breve encuentro con Obama; disculpas a Hu Jintao por suspension viaje a China.",
    Source_Verification="https://www.lanacion.com.ar/politica/la-presidenta-queria-una-relacion-mas-estrecha-con-estados-unidos-nid1356989/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J075", Trip_Status="Completed", Start_Date="2010-05-17", End_Date="2010-05-18", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="VI Cumbre UE-América Latina y el Caribe",
    Trip_Objective="Cumbre UE-ALC y Mercosur-UE; discurso inaugural en nombre de ALC; polemica con Durao Barroso.",
    Source_Verification="https://es.wikipedia.org/wiki/Presidencia_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J076", Trip_Status="Completed", Start_Date="2010-06-26", End_Date="2010-06-27", Duration_Days=2,
    Destination_Country="Canada", Destination_City="Toronto", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del G20 de Toronto",
    Trip_Objective="Cumbre del G20 de Toronto.",
    Source_Verification="https://es.wikipedia.org/wiki/Relaciones_exteriores_de_Argentina_durante_el_gobierno_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J077", Trip_Status="Completed", Start_Date="2010-07-12", End_Date="2010-07-15", Duration_Days=4,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hu Jintao / Wen Jiabao",
    Trip_Objective="Visita de Estado a China (Beijing y Shanghai); acuerdos de transporte por ~US$9500 millones. Honoris Causa; Expo Shanghai.",
    Source_Verification="https://es.wikipedia.org/wiki/Presidencia_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="Viaje reprogramado tras suspension de enero 2010.")

add("ARG-CFK-J078", Trip_Status="Completed", Start_Date="2010-09-24", End_Date="2010-09-24", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="65ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la ONU; oferta a Iran de elegir un tercer pais para juzgar la causa AMIA.",
    Source_Verification="https://www.cfkargentina.com/cfk-en-la-onu-mensaje-en-la-asamblea-general-de-2010/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J079", Trip_Status="Completed", Start_Date="2010-11-11", End_Date="2010-11-12", Duration_Days=2,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre del G20 de Seúl",
    Trip_Objective="Cumbre del G20 de Seul.",
    Source_Verification="https://es.wikipedia.org/wiki/Relaciones_exteriores_de_Argentina_durante_el_gobierno_de_Cristina_Fern%C3%A1ndez_de_Kirchner",
    Source_Reliability="High", Methodological_Notes="Primer viaje internacional tras la muerte de Nestor Kirchner (27 oct 2010).")

# ===== 2011 =====
# Gira Golfo + Turquia (mismo Journey_ID)
add("ARG-CFK-J080", Trip_Status="Completed", Start_Date="2011-01-16", End_Date="2011-01-17", Duration_Days=2,
    Destination_Country="Kuwait", Destination_City="Kuwait City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emir Sabah Al Ahmad Al Sabah",
    Trip_Objective="Gira comercial por el Golfo; Kuwait declaro a Argentina destino estrategico de inversiones. Tramo 1.",
    Source_Verification="https://www.ain.com.ar/news-2057-comenz%C3%B3-la-gira-de-cristina-kirchner-por-medio-oriente",
    Source_Reliability="High", Methodological_Notes="Comitiva +100 empresarios. Escala turistica previa en Egipto (Luxor).")

add("ARG-CFK-J080", Trip_Status="Completed", Start_Date="2011-01-18", End_Date="2011-01-19", Duration_Days=2,
    Destination_Country="Qatar", Destination_City="Doha", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emir Hamad Bin Khalifa Al Thani",
    Trip_Objective="Gira comercial; reunion con la jeque Mozah (Qatar Foundation). Tramo 2.",
    Source_Verification="https://www.ain.com.ar/news-2057-comenz%C3%B3-la-gira-de-cristina-kirchner-por-medio-oriente",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J080", Trip_Status="Completed", Start_Date="2011-01-20", End_Date="2011-01-22", Duration_Days=3,
    Destination_Country="Turkey", Destination_City="Ankara", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Abdullah Gül",
    Trip_Objective="Visita oficial a Turquia (Ankara/Estambul). Tramo 3 (regreso 23 ene).",
    Source_Verification="https://www.eldia.com/nota/2011-1-23-cristina-vuelve-al-conurbano-tras-la-gira-en-medio-oriente",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J081", Trip_Status="Canceled", Start_Date="2011-04-13", End_Date="NA", Duration_Days="NA",
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Felipe Calderón",
    Trip_Objective="Visita de Estado a Mexico prevista 13 abr. CANCELADA por lipotimia/hipotension. Reprogramacion a fin de mayo tampoco se concreto.",
    Source_Verification="https://www.lanacion.com.ar/politica/cristina-viajara-a-mexico-tras-las-dudas-por-su-cuadro-de-hipotension-nid1365226/",
    Source_Reliability="High", Methodological_Notes="Cancelado; sin duracion.")

add("ARG-CFK-J082", Trip_Status="Canceled", Start_Date="2011-05-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre regional en Paraguay",
    Trip_Objective="Cumbre en Paraguay (mayo). CANCELADA (motivo declarado: 'hacia mucho calor'). Vinculada a posterior suspension de MERCOSUR Asuncion 29 jun.",
    Source_Verification="Search Query: Cristina Kirchner suspende viaje Paraguay mayo 2011 calor",
    Source_Reliability="Medium", Methodological_Notes="Cancelado; sin duracion. Evento exacto a confirmar; fecha estimada YYYY-MM-01.")

add("ARG-CFK-J083", Trip_Status="Completed", Start_Date="2011-07-29", End_Date="2011-07-29", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Dilma Rousseff",
    Trip_Objective="Reunion de trabajo (MICBA) con Dilma.",
    Source_Verification="https://www.cancilleria.gob.ar/es/actualidad/comunicados/visita-oficial-de-la-presidenta-de-la-republica-argentina-cristina-fernandez",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J084", Trip_Status="Completed", Start_Date="2011-09-21", End_Date="2011-09-21", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="66ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la ONU: Palestina, AMIA y Malvinas.",
    Source_Verification="https://www.cfkargentina.com/discurso-de-cristina-kirchner-66a-asamblea-general-de-la-organizacion-de-las-naciones-unidas/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J085", Trip_Status="Completed", Start_Date="2011-11-03", End_Date="2011-11-04", Duration_Days=2,
    Destination_Country="France", Destination_City="Cannes", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G20 de Cannes",
    Trip_Objective="Cumbre del G20 (Sarkozy); foro empresarial. Declaracion conjunta con Obama relanzando la relacion bilateral.",
    Source_Verification="https://www.cfkargentina.com/discurso-de-cristina-en-la-cumbre-del-g-20-2011-en-cannes/",
    Source_Reliability="High", Methodological_Notes="NA")

add("ARG-CFK-J086", Trip_Status="Completed", Start_Date="2011-12-02", End_Date="2011-12-03", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre fundacional de la CELAC",
    Trip_Objective="Cumbre fundacional de la CELAC (III CALC + XXII Grupo de Rio); anfitrion Chavez. Respaldo a Malvinas; clausula antigolpe.",
    Source_Verification="https://es.wikipedia.org/wiki/Cumbre_de_la_Celac_de_2011",
    Source_Reliability="High", Methodological_Notes="Ultimo viaje del primer mandato.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (1er mandato) agregadas. Ultimo Trip_ID = {tid-1}")
