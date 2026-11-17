# -*- coding: utf-8 -*-
"""
BRASIL — Jair Bolsonaro (2019-01-01 a 2023-01-01, PSL/PL).
Continua Trip_ID tras Temer (ultimo=204). Journey continua en BRA-JB-J154.
Informe: ~25 desplazamientos (conteos discrepantes 23/24/29 segun fuente). EE.UU. destino dominante;
CERO viajes a Africa y Centroamerica. PARATE PANDEMICO de ~14 meses (mar 2020 - may 2021).
Politica exterior ideologizada: Trump/EE.UU., Israel, Golfo, Europa del Este (Hungria/Rusia);
evito a la Argentina de A. Fernandez. Giro pragmatico con China (oct 2019).
CASO ESPECIAL: salida a Orlando el 30/12/2022 (2 dias antes del fin del mandato, sin agenda oficial,
para no traspasar la banda a Lula) — cargada como Other con nota; permanece en EE.UU. tras el mandato.
CANCELADO cargado: Davos ene-2020. Declinados/virtuales sin anuncio formal de viaje: en pendientes.
Excluidos por ser en Brasil: BRICS Brasilia nov-2019, MERCOSUR Bento Goncalves dic-2019, cumbres virtuales.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Jair Bolsonaro"; O = "Brasil"
rows = []; tid = 205

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2019 =====
add("BRA-JB-J154", Trip_Status="Completed", Start_Date="2019-01-22", End_Date="2019-01-23", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Primer viaje del mandato: discurso breve en Davos presentando el 'nuevo Brasil' liberal.",
    Source_Verification="Search Query: Bolsonaro Davos janeiro 2019 discurso primeiro viagem",
    Source_Reliability="High", Methodological_Notes="Primer viaje internacional del mandato.")

add("BRA-JB-J155", Trip_Status="Completed", Start_Date="2019-03-18", End_Date="2019-03-19", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump (Casa Branca)",
    Trip_Objective="Primera bilateral con Trump; alineamiento estrategico, designacion de Brasil como aliado extra-OTAN.",
    Source_Verification="Search Query: Bolsonaro Trump Casa Branca 19 marco 2019",
    Source_Reliability="High", Methodological_Notes="18-19/03/2019.")

add("BRA-JB-J156", Trip_Status="Completed", Start_Date="2019-03-22", End_Date="2019-03-23", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do PROSUR + Sebastián Piñera",
    Trip_Objective="Cumbre fundacional del PROSUR (reemplazo de UNASUR) y bilateral con Pinera.",
    Source_Verification="Search Query: Bolsonaro PROSUR Santiago marco 2019 Pinera",
    Source_Reliability="Medium", Methodological_Notes="22/03/2019.")

add("BRA-JB-J157", Trip_Status="Completed", Start_Date="2019-03-31", End_Date="2019-04-02", Duration_Days=3,
    Destination_Country="Israel", Destination_City="Jerusalem", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Benjamin Netanyahu",
    Trip_Objective="Visita a Israel; Muro de los Lamentos con Netanyahu; abrio oficina comercial en Jerusalen (no mudo la embajada).",
    Source_Verification="Search Query: Bolsonaro Israel Netanyahu Muro Lamentacoes marco abril 2019",
    Source_Reliability="High", Methodological_Notes="31/3-2/4/2019.")

add("BRA-JB-J158", Trip_Status="Completed", Start_Date="2019-06-06", End_Date="2019-06-06", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mauricio Macri",
    Trip_Objective="Primera visita a Argentina; apoyo explicito a la reeleccion de Macri; moneda comun en agenda.",
    Source_Verification="Search Query: Bolsonaro Macri Buenos Aires 6 junho 2019",
    Source_Reliability="Medium", Methodological_Notes="6/06/2019. UNICA visita a Argentina del mandato (evito al gobierno de A. Fernandez).")

add("BRA-JB-J159", Trip_Status="Completed", Start_Date="2019-06-28", End_Date="2019-06-29", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Osaka", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Osaka",
    Trip_Objective="G20 de Osaka; anuncio del acuerdo Mercosur-UE (28/6); bilaterales con Trump y otros.",
    Source_Verification="Search Query: Bolsonaro G20 Osaka junho 2019",
    Source_Reliability="High", Methodological_Notes="28-29/06/2019.")

add("BRA-JB-J160", Trip_Status="Completed", Start_Date="2019-07-17", End_Date="2019-07-17", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Santa Fe", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="54ª Cúpula do MERCOSUL",
    Trip_Objective="Cumbre del Mercosur en Santa Fe; impulso al acuerdo con la UE y flexibilizacion del bloque.",
    Source_Verification="Search Query: Bolsonaro cupula Mercosul Santa Fe julho 2019",
    Source_Reliability="Medium", Methodological_Notes="17/07/2019. Confirmar asistencia/duracion.")

add("BRA-JB-J161", Trip_Status="Completed", Start_Date="2019-09-24", End_Date="2019-09-24", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="74ª AGNU",
    Trip_Objective="Apertura de la 74a AGNU; discurso defensivo sobre la Amazonia tras los incendios de agosto y la crisis con Macron.",
    Source_Verification="Search Query: Bolsonaro discurso ONU setembro 2019 Amazonia",
    Source_Reliability="High", Methodological_Notes="24/09/2019.")

# Gira Asia-Golfo oct-2019 (1 Journey_ID): Japon (entronizacion) + China + EAU + Qatar + Arabia Saudita
add("BRA-JB-J162", Trip_Status="Completed", Start_Date="2019-10-22", End_Date="2019-10-23", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Tokyo", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Entronização do imperador Naruhito",
    Trip_Objective="Ceremonia de entronizacion del emperador Naruhito. Tramo 1 de gira Asia-Golfo.",
    Source_Verification="Search Query: Bolsonaro entronizacao Naruhito Toquio outubro 2019",
    Source_Reliability="Medium", Methodological_Notes="Gira Asia-Golfo 22-30/10/2019; fechas de dia estimadas en tramos.")

add("BRA-JB-J162", Trip_Status="Completed", Start_Date="2019-10-24", End_Date="2019-10-26", Duration_Days=3,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Xi Jinping",
    Trip_Objective="Visita a Xi Jinping: giro pragmatico tras las criticas de campana ('China no compra en Brasil, compra Brasil'). Tramo 2.",
    Source_Verification="Search Query: Bolsonaro Xi Jinping Pequim outubro 2019",
    Source_Reliability="High", Methodological_Notes="NA")

add("BRA-JB-J162", Trip_Status="Completed", Start_Date="2019-10-26", End_Date="2019-10-27", Duration_Days=2,
    Destination_Country="United Arab Emirates", Destination_City="Abu Dhabi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mohammed bin Zayed",
    Trip_Objective="Inversiones del Golfo. Tramo 3.",
    Source_Verification="Search Query: Bolsonaro Emirados Abu Dhabi outubro 2019",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-JB-J162", Trip_Status="Completed", Start_Date="2019-10-28", End_Date="2019-10-28", Duration_Days=1,
    Destination_Country="Qatar", Destination_City="Doha", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emir Tamim bin Hamad Al Thani",
    Trip_Objective="Inversiones y comercio. Tramo 4.",
    Source_Verification="Search Query: Bolsonaro Catar Doha outubro 2019",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-JB-J162", Trip_Status="Completed", Start_Date="2019-10-29", End_Date="2019-10-30", Duration_Days=2,
    Destination_Country="Saudi Arabia", Destination_City="Riyadh", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Príncipe Mohammed bin Salman (Foro 'Davos do Deserto')",
    Trip_Objective="Foro de inversiones Future Investment Initiative; inversiones sauditas. Tramo 5 (final).",
    Source_Verification="Search Query: Bolsonaro Arabia Saudita Riade outubro 2019",
    Source_Reliability="Medium", Methodological_Notes="NA")

# ===== 2020 (pandemia desde marzo; parate ~14 meses) =====
add("BRA-JB-J163", Trip_Status="Completed", Start_Date="2020-01-24", End_Date="2020-01-27", Duration_Days=4,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Narendra Modi (convidado de honra do Dia da República)",
    Trip_Objective="Invitado de honor del Dia de la Republica de India (26/1); acuerdos de inversion y defensa.",
    Source_Verification="Search Query: Bolsonaro India Dia da Republica janeiro 2020 Modi",
    Source_Reliability="High", Methodological_Notes="24-27/01/2020.")

add("BRA-JB-J164", Trip_Status="Completed", Start_Date="2020-03-01", End_Date="2020-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Luis Lacalle Pou",
    Trip_Objective="Asuncion de Lacalle Pou; primer aliado ideologico en el Cono Sur.",
    Source_Verification="Search Query: Bolsonaro posse Lacalle Pou Montevideu 1 marco 2020",
    Source_Reliability="Medium", Methodological_Notes="1/03/2020.")

add("BRA-JB-J165", Trip_Status="Completed", Start_Date="2020-03-07", End_Date="2020-03-10", Duration_Days=4,
    Destination_Country="United States", Destination_City="Palm Beach", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Donald Trump (jantar em Mar-a-Lago)",
    Trip_Objective="Cena con Trump en Mar-a-Lago; la comitiva volvio con COVID (el famoso 'brote de Mar-a-Lago', +20 contagiados).",
    Source_Verification="Search Query: Bolsonaro Trump Mar-a-Lago marco 2020 comitiva covid",
    Source_Reliability="High", Methodological_Notes="7-10/03/2020. ULTIMO viaje pre-parate pandemico (~14 meses sin salir).")

# ===== 2021 (retoma tras ~14 meses) =====
add("BRA-JB-J166", Trip_Status="Completed", Start_Date="2021-05-24", End_Date="2021-05-24", Duration_Days=1,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Guillermo Lasso",
    Trip_Objective="Asuncion de Lasso; primer viaje tras ~14 meses de parate pandemico.",
    Source_Verification="Search Query: Bolsonaro posse Guillermo Lasso Quito maio 2021",
    Source_Reliability="Medium", Methodological_Notes="24/05/2021. Confirmar asistencia/fecha.")

add("BRA-JB-J167", Trip_Status="Completed", Start_Date="2021-09-19", End_Date="2021-09-21", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="76ª AGNU",
    Trip_Objective="Apertura de la 76a AGNU sin estar vacunado; episodio de la pizza en la vereda por las restricciones de NY.",
    Source_Verification="Search Query: Bolsonaro ONU 2021 nao vacinado pizza calcada Nova York",
    Source_Reliability="High", Methodological_Notes="19-21/09/2021.")

add("BRA-JB-J168", Trip_Status="Completed", Start_Date="2021-10-29", End_Date="2021-11-01", Duration_Days=4,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="FALSE", Counterpart_Event="Cúpula do G20 de Roma + Anguillara Veneta",
    Trip_Objective="G20 de Roma con participacion minima y aislamiento diplomatico; luego visito Anguillara Veneta (pueblo de sus ancestros, ciudadania honoraria) con incidentes.",
    Source_Verification="Search Query: Bolsonaro G20 Roma Anguillara Veneta outubro novembro 2021",
    Source_Reliability="High", Methodological_Notes="29/10-1/11/2021. NO fue a la COP26 de Glasgow (envio delegacion).")

# Gira Golfo nov 2021 (1 Journey_ID): EAU + Bahrein + Qatar
add("BRA-JB-J169", Trip_Status="Completed", Start_Date="2021-11-13", End_Date="2021-11-15", Duration_Days=3,
    Destination_Country="United Arab Emirates", Destination_City="Dubai", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Expo 2020 Dubai + governo emiratí",
    Trip_Objective="Gira por el Golfo: Expo Dubai e inversiones. Tramo 1.",
    Source_Verification="Search Query: Bolsonaro Dubai Expo novembro 2021",
    Source_Reliability="Medium", Methodological_Notes="Gira Golfo 13-18/11/2021; fechas de dia estimadas.")

add("BRA-JB-J169", Trip_Status="Completed", Start_Date="2021-11-15", End_Date="2021-11-16", Duration_Days=2,
    Destination_Country="Bahrain", Destination_City="Manama", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rei Hamad bin Isa Al Khalifa",
    Trip_Objective="Comercio e inversiones. Tramo 2.",
    Source_Verification="Search Query: Bolsonaro Bahrein novembro 2021",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("BRA-JB-J169", Trip_Status="Completed", Start_Date="2021-11-17", End_Date="2021-11-17", Duration_Days=1,
    Destination_Country="Qatar", Destination_City="Doha", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emir Tamim bin Hamad Al Thani",
    Trip_Objective="Comercio e inversiones. Tramo 3 (final).",
    Source_Verification="Search Query: Bolsonaro Catar novembro 2021",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

# ===== 2022 =====
# Gira Rusia + Hungria feb 2022 (1 Journey_ID)
add("BRA-JB-J170", Trip_Status="Completed", Start_Date="2022-02-15", End_Date="2022-02-16", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Vladímir Putin",
    Trip_Objective="Visita a Putin DIAS ANTES de la invasion a Ucrania; declaro que Brasil era 'solidario con Rusia'. Muy criticado. Tramo 1.",
    Source_Verification="Search Query: Bolsonaro Putin Moscou fevereiro 2022 solidarios",
    Source_Reliability="High", Methodological_Notes="15-16/02/2022; invasion rusa el 24/2.")

add("BRA-JB-J170", Trip_Status="Completed", Start_Date="2022-02-17", End_Date="2022-02-18", Duration_Days=2,
    Destination_Country="Hungary", Destination_City="Budapest", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Viktor Orbán",
    Trip_Objective="Visita a Orban; afinidad ideologica con la derecha europea. Tramo 2 (final).",
    Source_Verification="Search Query: Bolsonaro Orban Budapeste fevereiro 2022",
    Source_Reliability="High", Methodological_Notes="17-18/02/2022.")

add("BRA-JB-J171", Trip_Status="Completed", Start_Date="2022-06-08", End_Date="2022-06-10", Duration_Days=3,
    Destination_Country="United States", Destination_City="Los Angeles", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IX Cúpula das Américas (bilateral com Biden)",
    Trip_Objective="Cumbre de las Americas de Los Angeles tras gestiones de EE.UU.; su UNICA bilateral con Biden (9/6).",
    Source_Verification="Search Query: Bolsonaro Cupula das Americas Los Angeles Biden junho 2022",
    Source_Reliability="High", Methodological_Notes="8-10/06/2022.")

add("BRA-JB-J172", Trip_Status="Completed", Start_Date="2022-07-21", End_Date="2022-07-21", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="60ª Cúpula do MERCOSUL (Luque)",
    Trip_Objective="Cumbre del Mercosur en Paraguay.",
    Source_Verification="Search Query: Bolsonaro cupula Mercosul Paraguai Luque julho 2022",
    Source_Reliability="Medium", Methodological_Notes="21/07/2022. Confirmar asistencia.")

# Gira Londres (funeral Isabel II) + NY (AGNU) sep 2022 — 1 Journey_ID
add("BRA-JB-J173", Trip_Status="Completed", Start_Date="2022-09-18", End_Date="2022-09-19", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Funeral da rainha Elizabeth II",
    Trip_Objective="Funeral de Isabel II en plena campana electoral; discurso politico desde el balcon de la embajada brasilena. Tramo 1.",
    Source_Verification="Search Query: Bolsonaro funeral rainha Elizabeth Londres setembro 2022 sacada embaixada",
    Source_Reliability="High", Methodological_Notes="18-19/09/2022.")

add("BRA-JB-J173", Trip_Status="Completed", Start_Date="2022-09-20", End_Date="2022-09-20", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="77ª AGNU",
    Trip_Objective="Ultimo discurso ante la ONU, con tono de campana electoral. Tramo 2 (final).",
    Source_Verification="Search Query: Bolsonaro abertura 77 Assembleia ONU setembro 2022",
    Source_Reliability="High", Methodological_Notes="20/09/2022. NO fue al G20 de Bali (nov 2022) tras perder la eleccion.")

add("BRA-JB-J174", Trip_Status="Completed", Start_Date="2022-12-30", End_Date="2023-01-01", Duration_Days=3,
    Destination_Country="United States", Destination_City="Orlando", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Salida a Florida (sin agenda oficial)",
    Trip_Objective="Salio a Orlando el 30/12/2022, dos dias antes del fin del mandato, para no traspasar la banda a Lula. Sin agenda oficial de gobierno.",
    Source_Verification="Search Query: Bolsonaro viaja Orlando Florida 30 dezembro 2022 nao passa faixa",
    Source_Reliability="High", Methodological_Notes="CASO ATIPICO: viaje sin agenda oficial iniciado en ejercicio; permanecio en EE.UU. tras el 1/1/2023. Duracion computada hasta el fin del mandato.")

# ===== CANCELADO =====
add("BRA-JB-J175", Trip_Status="Canceled", Start_Date="2020-01-21", End_Date="NA", Duration_Days="NA",
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico Mundial 2020",
    Trip_Objective="Participacion prevista en Davos 2020. CANCELADA por decision del gobierno (razones de seguridad/conveniencia); fue Guedes.",
    Source_Verification="Search Query: Bolsonaro cancela Davos janeiro 2020 Guedes",
    Source_Reliability="Medium", Methodological_Notes="Cancelado; sin duracion. Motivo exacto a confirmar.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
