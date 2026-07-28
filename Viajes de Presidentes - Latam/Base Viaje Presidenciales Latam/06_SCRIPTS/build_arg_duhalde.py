# -*- coding: utf-8 -*-
"""
Agrega los viajes de Eduardo Duhalde (2002-01-02 a 2003-05-25) al módulo de Argentina.
Rodríguez Saá (23-30 dic 2001): SIN viajes internacionales (registro negativo verificado, va en bitácora).
Continúa el Trip_ID después de De la Rúa (último Trip_ID = 12).
Fuentes: investigación verificada (Página/12, La Nación, Cancillería AR, ONU, SEGIB, Ámbito, Clarín, Infobae, Archivo Lagos/UDP).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")

P = "Eduardo Duhalde"
O = "Argentina"
rows = []

# J012 — Monterrey, México (Conferencia ONU Financiación para el Desarrollo) 18-22 mar 2002
rows.append(new_row(Journey_ID="ARG-EDU-J012", Trip_ID=13, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2002-03-21", End_Date="2002-03-22", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Monterrey",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="TRUE",
    Counterpart_Event="Conferencia Internacional sobre Financiación para el Desarrollo (Consenso de Monterrey)",
    Trip_Objective="Pedido de apoyo internacional y flexibilizacion del FMI ante la crisis. Bilateral al margen con Vicente Fox (cena).",
    Source_Verification="https://www.un.org/es/conf/ffd/2002/",
    Source_Reliability="High",
    Methodological_Notes="Conferencia 18-22 mar; segmento jefes de Estado 21-22 mar (estimado). EE.UU. bloqueo incluir la crisis argentina."))

# J013 — San José, Costa Rica (XVI Cumbre Grupo de Río) 11-12 abr 2002
rows.append(new_row(Journey_ID="ARG-EDU-J013", Trip_ID=14, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2002-04-11", End_Date="2002-04-12", Duration_Days=2,
    Destination_Country="Costa Rica", Destination_City="San José",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="XVI Cumbre del Grupo de Río",
    Trip_Objective="Concertacion politica regional; la cumbre condeno el golpe contra Chavez en Venezuela (Duhalde lo califico de golpe). Declaracion de San Jose.",
    Source_Verification="https://www.lanacion.com.ar/el-mundo/condeno-el-grupo-rio-la-ruptura-democratica-nid388447/",
    Source_Reliability="High",
    Methodological_Notes="Coincidio con el golpe contra Chavez (11-12 abr 2002)."))

# CANCELADO — Chile, 19 ago 2002
rows.append(new_row(Journey_ID="ARG-EDU-J014", Trip_ID=15, President=P, Origin_Country=O,
    Trip_Status="Canceled", Start_Date="2002-08-19", End_Date="NA", Duration_Days="NA",
    Destination_Country="Chile", Destination_City="Santiago",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Ricardo Lagos",
    Trip_Objective="Visita planificada a Chile / reunion con Lagos. CANCELADA por urgentes situaciones internas que requirieron su presencia en Argentina.",
    Source_Verification="https://www.ambito.com/politica/duhalde-el-dia-chile-n3195320",
    Source_Reliability="Medium",
    Methodological_Notes="Viaje cancelado; sin duracion. Fecha original 19 ago 2002."))

# J015 — Guayaquil, Ecuador (II Cumbre Sudamericana) 26-27 jul 2002
rows.append(new_row(Journey_ID="ARG-EDU-J015", Trip_ID=16, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2002-07-26", End_Date="2002-07-27", Duration_Days=2,
    Destination_Country="Ecuador", Destination_City="Guayaquil",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="II Cumbre de Presidentes de América del Sur (Consenso de Guayaquil)",
    Trip_Objective="Integracion sudamericana (IIRSA, zona de paz). Pidio a la region un reclamo conjunto al FMI. Compartio actividades con Lagos en la costa.",
    Source_Verification="https://www.eluniverso.com/2002/07/29/0001/8/2360CB0607654BD59F02662636F657CB.html/",
    Source_Reliability="High",
    Methodological_Notes="Consenso de Guayaquil firmado 26-27 jul 2002."))

# J016 — Brasilia, Brasil (visita oficial a Cardoso) 26 sep 2002
rows.append(new_row(Journey_ID="ARG-EDU-J016", Trip_ID=17, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2002-09-26", End_Date="2002-09-26", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Fernando Henrique Cardoso",
    Trip_Objective="Profundizar alianza estrategica y consolidar el MERCOSUR; Acuerdo Bilateral Automotor y Convenio de Pagos y Creditos Reciprocos; apoyo ante el FMI.",
    Source_Verification="https://www.cancilleria.gob.ar/es/actualidad/comunicados/los-presidentes-duhalde-y-cardoso-consolidan-el-mercosur",
    Source_Reliability="High",
    Methodological_Notes="Fecha exacta confirmada por comunicado de Cancilleria AR (115/2002)."))

# J017 — Santiago, Chile (visita de trabajo a Lagos) 29 oct 2002
rows.append(new_row(Journey_ID="ARG-EDU-J017", Trip_ID=18, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2002-10-29", End_Date="2002-10-29", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Santiago",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Ricardo Lagos",
    Trip_Objective="Agradecer la apertura del mercado chileno a la carne argentina; firma de convenios de cooperacion. Viaje de un dia.",
    Source_Verification="https://www.ambito.com/politica/duhalde-el-dia-chile-n3195320",
    Source_Reliability="Medium",
    Methodological_Notes="Viaje por el dia (29 oct 2002), con el canciller Ruckauf."))

# J018 — Bávaro, Rep. Dominicana (XII Cumbre Iberoamericana) 15-16 nov 2002
rows.append(new_row(Journey_ID="ARG-EDU-J018", Trip_ID=19, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2002-11-15", End_Date="2002-11-16", Duration_Days=2,
    Destination_Country="Dominican Republic", Destination_City="Bávaro",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="XII Cumbre Iberoamericana (Bávaro)",
    Trip_Objective="Respaldo regional a la negociacion con el FMI (Declaracion Especial). Bilaterales al margen probables con Aznar y Cardoso.",
    Source_Verification="https://segib.org/?summit=xii-cumbre-iberoamericana-bavaro-2002",
    Source_Reliability="High",
    Methodological_Notes="21 paises; Declaracion de Bavaro + declaracion especial sobre Argentina-FMI."))

# J019 — Brasilia, Brasil (XXIII Cumbre MERCOSUR) 5-6 dic 2002
rows.append(new_row(Journey_ID="ARG-EDU-J019", Trip_ID=20, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2002-12-05", End_Date="2002-12-06", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasilia",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="XXIII Cumbre del MERCOSUR",
    Trip_Objective="Relanzar el MERCOSUR; Acuerdo de Residencia para Nacionales del MERCOSUR (firmado 6 dic con Bolivia y Chile). Cardoso saliente y Lula electo.",
    Source_Verification="https://www.infobae.com/2002/12/07/35999-duhalde-neuquen/",
    Source_Reliability="High",
    Methodological_Notes="Tras la cumbre voló directo a Villa la Angostura."))

# J020 — Brasilia, Brasil (asunción de Lula) 1 ene 2003
rows.append(new_row(Journey_ID="ARG-EDU-J020", Trip_ID=21, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2003-01-01", End_Date="2003-01-01", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia",
    Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral", Sideline_Bilaterals="NA",
    Counterpart_Event="Asunción de Luiz Inácio Lula da Silva",
    Trip_Objective="Presencia en la transmision de mando de Lula; afianzar el vinculo con el nuevo gobierno brasileno.",
    Source_Verification="https://www.lanacion.com.ar/el-mundo/lula-asumio-la-presidencia-nid462975/",
    Source_Reliability="High",
    Methodological_Notes="Acto con multiples jefes de Estado de la region."))

# J021 — Brasilia, Brasil (visita oficial a Lula, Declaración de Brasilia) 14 ene 2003
rows.append(new_row(Journey_ID="ARG-EDU-J021", Trip_ID=22, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2003-01-14", End_Date="2003-01-14", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Lula da Silva",
    Trip_Objective="Declaracion de Brasilia; alianza estrategica; programas contra el hambre y la pobreza; idea de instituto monetario / moneda comun (Lavagna).",
    Source_Verification="https://www.clarin.com/politica/duhalde-lula-hablan-moneda-comun-plan-pobreza_0_BywzT2MlRYx.html",
    Source_Reliability="Medium",
    Methodological_Notes="Revisar contra Boletin Oficial fecha exacta de salida/regreso."))

# J022 — Davos, Suiza (Foro Económico Mundial) ~25-27 ene 2003
rows.append(new_row(Journey_ID="ARG-EDU-J022", Trip_ID=23, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2003-01-25", End_Date="2003-01-27", Duration_Days=3,
    Destination_Country="Switzerland", Destination_City="Davos",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="Foro Económico Mundial (WEF) 2003",
    Trip_Objective="Reclamo contra el proteccionismo de paises centrales y el 'doble estandar' del FMI; panel con Soros y Rogoff. Unico viaje a Europa del mandato.",
    Source_Verification="https://www.lanacion.com.ar/economia/duhalde-cuestiono-al-fmi-y-provoco-un-duro-debate-nid469268/",
    Source_Reliability="High",
    Methodological_Notes="WEF 23-28 ene 2003; intervencion de Duhalde ~25-27 ene (estimado)."))

# J023 — Santiago, Chile (despedida a Lagos) 23 abr 2003
rows.append(new_row(Journey_ID="ARG-EDU-J023", Trip_ID=24, President=P, Origin_Country=O,
    Trip_Status="Completed", Start_Date="2003-04-23", End_Date="2003-04-23", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Santiago",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Ricardo Lagos",
    Trip_Objective="Visita de despedida antes de entregar el mando; acuerdo para evitar la doble tributacion. Visita relampago (~3,5 horas).",
    Source_Verification="https://arle.udp.cl/index.php/visita-del-presidente-eduardo-duhalde-sintesis-informativa",
    Source_Reliability="High",
    Methodological_Notes="Fecha del Archivo oficial Presidencia de Chile (Lagos/UDP). Ultimo viaje del mandato."))

# Append al CSV existente
with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas a {CSV}")
