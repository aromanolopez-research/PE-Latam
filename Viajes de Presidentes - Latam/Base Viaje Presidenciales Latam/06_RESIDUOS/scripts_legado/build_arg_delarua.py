# -*- coding: utf-8 -*-
"""
Módulo de viajes: Fernando de la Rúa (Argentina), mandato 1999-12-10 a 2001-12-20.
Ventana del proyecto: se registran SOLO viajes desde 2000-01-01 (nada anterior, nada posterior a la renuncia).
Una fila por país de destino; Journey_ID agrupa cada salida física.
Fuentes: La Nación, Infobae, El Cronista, Cancillería Argentina, Scielo, ONU, OEA, Cumbre Iberoamericana, summit-americas.org.
NOTA: El acceso viaje-por-viaje al Boletín Oficial argentino (BORA) 2000-2001 no fue posible por web;
se usa prensa de referencia y fuentes multilaterales oficiales. Confiabilidad ajustada en consecuencia.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

P = "Fernando de la Rúa"
O = "Argentina"
rows = []

# J001 — Estocolmo (Foro Holocausto) + Davos (WEF). Gira de 2 países, ene 2000.
rows.append(new_row(Journey_ID="ARG-DLR-J001", Trip_ID=1, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2000-01-25", End_Date="2000-01-27", Duration_Days=3,
    Destination_Country="Sweden", Destination_City="Stockholm",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="Foro Internacional de Estocolmo sobre el Holocausto",
    Trip_Objective="Participacion en el Foro Internacional sobre el Holocausto en Estocolmo; primer viaje al exterior del mandato.",
    Source_Verification="https://www.cronista.com/economia-politica/Primeros-viajes-oficiales-que-destinos-eligieron-los-ex-presidentes-20200116-0035.html",
    Source_Reliability="Medium",
    Methodological_Notes="Fechas aproximadas; viajo en avion comercial via Frankfurt. Dia fin estimado por encadenar con Davos."))

rows.append(new_row(Journey_ID="ARG-DLR-J001", Trip_ID=2, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2000-01-27", End_Date="2000-01-30", Duration_Days=3,
    Destination_Country="Switzerland", Destination_City="Davos",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="Foro Económico Mundial (WEF) Davos 2000",
    Trip_Objective="Participacion en el Foro Economico Mundial de Davos, segundo tramo de la gira inaugural.",
    Source_Verification="https://www.lanacion.com.ar/politica/javier-milei-el-presidente-con-mas-viajes-internacionales-en-seis-meses-de-mandato-nid27052024/",
    Source_Reliability="Medium",
    Methodological_Notes="Fechas estimadas (YYYY-MM aprox). Tramo continuo con Estocolmo."))

# J002 — Berlín, Cumbre de la Tercera Vía (Schröder), junio 2000.
rows.append(new_row(Journey_ID="ARG-DLR-J002", Trip_ID=3, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2000-06-02", End_Date="2000-06-03", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Berlin",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="Cumbre de Líderes de la Tercera Vía (Gerhard Schröder)",
    Trip_Objective="Participacion en la Cumbre de la Tercera Via / gobernanza progresista organizada por el canciller aleman Schroder.",
    Source_Verification="Search Query: De la Rua Berlin Cumbre Tercera Via Schroder junio 2000",
    Source_Reliability="Low",
    Methodological_Notes="Fecha estimada YYYY-MM-01 ajustada a inicios de junio 2000; confirmar dia exacto en BORA."))

# J003 — Washington, visita de trabajo a Clinton, 12-14 junio 2000.
rows.append(new_row(Journey_ID="ARG-DLR-J003", Trip_ID=4, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2000-06-12", End_Date="2000-06-14", Duration_Days=3,
    Destination_Country="United States", Destination_City="Washington D.C.",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Bill Clinton",
    Trip_Objective="Visita de trabajo a la Casa Blanca; almuerzo con Clinton (13 jun) y exposicion ante 400 empresarios (14 jun).",
    Source_Verification="https://www.lanacion.com.ar/politica/javier-milei-el-presidente-con-mas-viajes-internacionales-en-seis-meses-de-mandato-nid27052024/",
    Source_Reliability="High",
    Methodological_Notes="Fecha 13-jun del almuerzo confirmada por prensa; rango 12-14 estimado por agenda."))

# J004 — Brasilia, I Cumbre Sudamericana, 31 ago - 1 sep 2000.
rows.append(new_row(Journey_ID="ARG-DLR-J004", Trip_ID=5, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2000-08-31", End_Date="2000-09-01", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasilia",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="I Cumbre Sudamericana (Brasilia)",
    Trip_Objective="Participacion en la I Cumbre Sudamericana; apoyo al gobierno constitucional de Colombia y a la no intervencion.",
    Source_Verification="http://www.scielo.br/j/spp/a/MbMFj5mfNjLyPJ7qmTYP3xS/?lang=es",
    Source_Reliability="High",
    Methodological_Notes="Cumbre de Brasilia 31-ago-2000 documentada (Scielo)."))

# J005 — Nueva York, Cumbre del Milenio ONU, 6-8 sep 2000.
rows.append(new_row(Journey_ID="ARG-DLR-J005", Trip_ID=6, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2000-09-06", End_Date="2000-09-08", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="Cumbre del Milenio de las Naciones Unidas",
    Trip_Objective="Participacion en la Cumbre del Milenio de la ONU (mayor reunion de jefes de Estado hasta entonces).",
    Source_Verification="https://www.un.org/es/conferences/environment/newyork2000",
    Source_Reliability="High",
    Methodological_Notes="Fechas oficiales de la Cumbre del Milenio (6-8 sep 2000); asistencia de De la Rua segun prensa."))

# J006 — Florianópolis, Cumbre MERCOSUR, dic 2000.
rows.append(new_row(Journey_ID="ARG-DLR-J006", Trip_ID=7, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2000-12-14", End_Date="2000-12-15", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Florianópolis",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="Cumbre de Jefes de Estado del MERCOSUR (Florianópolis)",
    Trip_Objective="Cumbre del MERCOSUR en Florianopolis; metas macroeconomicas comunes y solucion de controversias.",
    Source_Verification="http://www.scielo.br/j/spp/a/MbMFj5mfNjLyPJ7qmTYP3xS/?lang=es",
    Source_Reliability="Medium",
    Methodological_Notes="Cumbre de mediados de diciembre 2000 (Scielo); dia exacto estimado."))

# J007 — Quebec, III Cumbre de las Américas, 20-22 abr 2001.
rows.append(new_row(Journey_ID="ARG-DLR-J007", Trip_ID=8, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2001-04-20", End_Date="2001-04-22", Duration_Days=3,
    Destination_Country="Canada", Destination_City="Quebec City",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="III Cumbre de las Américas (Quebec)",
    Trip_Objective="Participacion en la III Cumbre de las Americas; agenda hemisferica y ALCA. De la Rua en la foto oficial de mandatarios.",
    Source_Verification="https://summit-americas.org/sas/Cumbres_previas_IIICumbre.html",
    Source_Reliability="High",
    Methodological_Notes="Fechas oficiales OEA (20-22 abr 2001); presencia de De la Rua confirmada."))

# J008 — Asunción, Cumbre MERCOSUR, 21-22 jun 2001.
rows.append(new_row(Journey_ID="ARG-DLR-J008", Trip_ID=9, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2001-06-21", End_Date="2001-06-22", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="XX Cumbre del MERCOSUR (Asunción)",
    Trip_Objective="XX Reunion del Consejo del Mercado Comun y Cumbre del MERCOSUR; 10 anios del Tratado de Asuncion.",
    Source_Verification="https://www.cancilleria.gob.ar/es/actualidad/comunicados/comunicado-de-los-presidentes-de-los-estados-partes-del-mercosur-sobre-los",
    Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (21-22 jun 2001) confirmadas por Cancilleria argentina."))

# J009 — Santiago, Cumbre del Grupo de Río, 17-18 ago 2001.
rows.append(new_row(Journey_ID="ARG-DLR-J009", Trip_ID=10, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2001-08-17", End_Date="2001-08-18", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Santiago",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="XV Cumbre del Grupo de Río (Santiago)",
    Trip_Objective="XV Cumbre de Jefes de Estado del Grupo de Rio en Santiago de Chile; articulacion de consensos regionales.",
    Source_Verification="https://www.cancilleria.gob.ar/es/actualidad/comunicados/comunicado-de-los-presidentes-de-los-estados-partes-del-mercosur-sobre-los",
    Source_Reliability="High",
    Methodological_Notes="Fechas (17-18 ago 2001) referidas en comunicado oficial MERCOSUR."))

# J010 — Nueva York, Asamblea General ONU (post 11-S), 10-11 nov 2001.
rows.append(new_row(Journey_ID="ARG-DLR-J010", Trip_ID=11, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2001-11-09", End_Date="2001-11-11", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="TRUE",
    Counterpart_Event="56ª Asamblea General de la ONU (debate post-11S)",
    Trip_Objective="Discurso ante la Asamblea General de la ONU sobre terrorismo internacional; bilaterales con Bush y Vicente Fox por apoyo economico.",
    Source_Verification="https://www.infobae.com/sociedad/2019/12/20/la-caida-de-fernando-de-la-rua-la-historia-secreta-de-la-tormenta-politica-perfecta-y-el-final-en-el-helicoptero/",
    Source_Reliability="High",
    Methodological_Notes="Llego el 9 nov; discurso 10 nov; bilateral con Bush 11 nov (Waldorf Astoria). Bilaterales al margen confirmados."))

# J011 — Lima, XI Cumbre Iberoamericana, 23-24 nov 2001.
rows.append(new_row(Journey_ID="ARG-DLR-J011", Trip_ID=12, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2001-11-23", End_Date="2001-11-24", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="XI Cumbre Iberoamericana (Lima)",
    Trip_Objective="XI Cumbre Iberoamericana; busco respaldo regional al canje de deuda argentino para evitar el default. Apoyo de pares.",
    Source_Verification="https://www.jornada.com.mx/2001/11/25/007n1mun.html",
    Source_Reliability="High",
    Methodological_Notes="Cumbre concluyo el 24 nov 2001 (La Jornada). Ultimo viaje internacional antes de la renuncia (20 dic 2001)."))

# Guardar
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    w.writeheader()
    w.writerows(rows)
print(f"OK: {len(rows)} filas escritas para {P} en {out}")
