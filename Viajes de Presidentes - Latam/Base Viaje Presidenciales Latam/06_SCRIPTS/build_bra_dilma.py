# -*- coding: utf-8 -*-
"""
BRASIL — Dilma Rousseff (2011-01-01 a 2016-05-12, suspension por impeachment; destitucion formal 31/8/2016).
Continua Trip_ID tras Lula (ultimo=144). Journey continua en BRA-DR-J098.
Mucho MENOS viajera que Lula ("retracao da diplomacia presidencial", Cornetet 2014: -31%/-55%).
Informe: ~60 desplazamientos / ~70 visitas-pais. Se carga el nucleo verificado (~30 giras ancladas);
brecha documentada EN EL MOMENTO en PENDIENTES_VERIFICACION.txt.
CANCELADO emblematico: visita de Estado a Washington prevista 23/10/2013, postergada el 17/9/2013
por el espionaje de la NSA (caso Snowden). ULTIMO viaje: NY 22/4/2016 (firma del Acuerdo de Paris),
5 dias despues de la votacion del impeachment en Diputados (17/4).
Excluidos por ser en Brasil: Rio+20 (jun 2012), BRICS Fortaleza (jul 2014), Copa 2014.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Dilma Rousseff"; O = "Brasil"
rows = []; tid = 145

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2011 =====
add("BRA-DR-J098", Trip_Status="Completed", Start_Date="2011-01-31", End_Date="2011-01-31", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cristina Fernández de Kirchner",
    Trip_Objective="Primer viaje internacional del mandato: relacion estrategica con Argentina.",
    Source_Verification="Search Query: Dilma primeira viagem internacional Argentina 31 janeiro 2011",
    Source_Reliability="Medium", Methodological_Notes="Primer viaje del mandato.")

add("BRA-DR-J099", Trip_Status="Completed", Start_Date="2011-04-11", End_Date="2011-04-14", Duration_Days=4,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Hu Jintao + III Cúpula BRICS (Sanya, 14/4)",
    Trip_Objective="Visita de Estado a China (Pekin 12-13/4) y III Cumbre BRICS en Sanya (14/4), primera con Sudafrica.",
    Source_Verification="Search Query: Dilma visita de Estado China BRICS Sanya abril 2011",
    Source_Reliability="High", Methodological_Notes="Una sola salida: visita de Estado + BRICS en el mismo pais.")

add("BRA-DR-J100", Trip_Status="Completed", Start_Date="2011-09-19", End_Date="2011-09-21", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="66ª AGNU",
    Trip_Objective="HITO: primera mujer en abrir el debate de la Asamblea General de la ONU (21/9/2011).",
    Source_Verification="Search Query: Dilma primeira mulher abrir Assembleia Geral ONU 21 setembro 2011",
    Source_Reliability="High", Methodological_Notes="Discurso de apertura 21/9/2011.")

# Gira Bruselas + Bulgaria oct 2011 — 1 Journey_ID
add("BRA-DR-J101", Trip_Status="Completed", Start_Date="2011-10-03", End_Date="2011-10-04", Duration_Days=2,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="V Cúpula Brasil-União Europeia",
    Trip_Objective="Cumbre Brasil-UE en Bruselas. Tramo 1.",
    Source_Verification="Search Query: Dilma cupula Brasil Uniao Europeia Bruxelas outubro 2011",
    Source_Reliability="Medium", Methodological_Notes="Gira Belgica-Bulgaria oct 2011.")

add("BRA-DR-J101", Trip_Status="Completed", Start_Date="2011-10-05", End_Date="2011-10-07", Duration_Days=3,
    Destination_Country="Bulgaria", Destination_City="Sofia", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Governo da Bulgária (terra paterna)",
    Trip_Objective="Visita oficial a Bulgaria, tierra de su padre Pedro Rousseff; visito Gabrovo. Tramo 2 (final).",
    Source_Verification="Search Query: Dilma Bulgaria Gabrovo outubro 2011 pai",
    Source_Reliability="High", Methodological_Notes="Fuerte carga simbolica personal.")

add("BRA-DR-J102", Trip_Status="Completed", Start_Date="2011-10-18", End_Date="2011-10-18", Duration_Days=1,
    Destination_Country="South Africa", Destination_City="Pretoria", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="V Cúpula IBSA",
    Trip_Objective="Cumbre IBSA en Pretoria.",
    Source_Verification="Search Query: Dilma cupula IBSA Pretoria outubro 2011",
    Source_Reliability="Medium", Methodological_Notes="18/10/2011.")

add("BRA-DR-J103", Trip_Status="Completed", Start_Date="2011-11-03", End_Date="2011-11-04", Duration_Days=2,
    Destination_Country="France", Destination_City="Cannes", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Cannes",
    Trip_Objective="G20 de Cannes; crisis del euro en agenda.",
    Source_Verification="Search Query: Dilma G20 Cannes novembro 2011",
    Source_Reliability="Medium", Methodological_Notes="3-4/11/2011.")

add("BRA-DR-J104", Trip_Status="Completed", Start_Date="2011-12-02", End_Date="2011-12-03", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula fundacional da CELAC",
    Trip_Objective="Cumbre fundacional de la CELAC en Caracas.",
    Source_Verification="Search Query: Dilma CELAC fundacional Caracas dezembro 2011",
    Source_Reliability="Medium", Methodological_Notes="2-3/12/2011.")

add("BRA-DR-J105", Trip_Status="Completed", Start_Date="2011-12-20", End_Date="2011-12-20", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do MERCOSUL",
    Trip_Objective="Cumbre del Mercosur en Montevideo.",
    Source_Verification="Search Query: Dilma cupula Mercosul Montevideu dezembro 2011",
    Source_Reliability="Medium", Methodological_Notes="20/12/2011.")

# ===== 2012 =====
add("BRA-DR-J106", Trip_Status="Completed", Start_Date="2012-03-05", End_Date="2012-03-06", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Hannover", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Angela Merkel (Feira de Hannover)",
    Trip_Objective="Apertura de la Feria de Hannover (Brasil pais socio) y reunion con Merkel.",
    Source_Verification="Search Query: Dilma Merkel feira Hannover marco 2012",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-DR-J107", Trip_Status="Completed", Start_Date="2012-03-28", End_Date="2012-03-29", Duration_Days=2,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IV Cúpula BRICS",
    Trip_Objective="Cumbre BRICS de Nueva Delhi.",
    Source_Verification="Search Query: Dilma cupula BRICS Nova Delhi marco 2012",
    Source_Reliability="Medium", Methodological_Notes="28-29/03/2012.")

add("BRA-DR-J108", Trip_Status="Completed", Start_Date="2012-04-09", End_Date="2012-04-10", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Barack Obama",
    Trip_Objective="Visita oficial (no de Estado) a Obama; luego Boston (Harvard/MIT, programa Ciencia sin Fronteras).",
    Source_Verification="Search Query: Dilma Obama Casa Branca 9 abril 2012",
    Source_Reliability="High", Methodological_Notes="9/4 Washington; 10/4 Boston.")

add("BRA-DR-J109", Trip_Status="Completed", Start_Date="2012-04-14", End_Date="2012-04-15", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VI Cúpula das Américas",
    Trip_Objective="VI Cumbre de las Americas en Cartagena.",
    Source_Verification="Search Query: Dilma VI Cupula das Americas Cartagena abril 2012",
    Source_Reliability="High", Methodological_Notes="14-15/04/2012.")

add("BRA-DR-J110", Trip_Status="Completed", Start_Date="2012-06-18", End_Date="2012-06-19", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Los Cabos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Los Cabos",
    Trip_Objective="G20 de Los Cabos.",
    Source_Verification="Search Query: Dilma G20 Los Cabos junho 2012",
    Source_Reliability="Medium", Methodological_Notes="18-19/06/2012.")

add("BRA-DR-J111", Trip_Status="Completed", Start_Date="2012-06-29", End_Date="2012-06-29", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Mendoza", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do MERCOSUL (suspensão do Paraguai)",
    Trip_Objective="Cumbre del Mercosur en Mendoza: suspension de Paraguay (caso Lugo) e ingreso de Venezuela.",
    Source_Verification="Search Query: Dilma Mercosul Mendoza junho 2012 suspensao Paraguai",
    Source_Reliability="High", Methodological_Notes="29/06/2012.")

add("BRA-DR-J112", Trip_Status="Completed", Start_Date="2012-09-25", End_Date="2012-09-25", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="67ª AGNU",
    Trip_Objective="Apertura de la 67a AGNU.",
    Source_Verification="Search Query: Dilma abertura 67 Assembleia Geral ONU setembro 2012",
    Source_Reliability="Medium", Methodological_Notes="25/09/2012.")

add("BRA-DR-J113", Trip_Status="Completed", Start_Date="2012-10-01", End_Date="2012-10-02", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="III Cúpula ASPA",
    Trip_Objective="III Cumbre America del Sur-Paises Arabes en Lima.",
    Source_Verification="Search Query: Dilma cupula ASPA Lima outubro 2012",
    Source_Reliability="Medium", Methodological_Notes="1-2/10/2012. Confirmar asistencia exacta.")

# ===== 2013 =====
add("BRA-DR-J114", Trip_Status="Completed", Start_Date="2013-01-26", End_Date="2013-01-28", Duration_Days=3,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="I Cúpula CELAC + Cúpula CELAC-UE",
    Trip_Objective="Primera cumbre CELAC y cumbre CELAC-UE en Santiago.",
    Source_Verification="Search Query: Dilma CELAC UE Santiago janeiro 2013",
    Source_Reliability="Medium", Methodological_Notes="26-28/01/2013.")

add("BRA-DR-J115", Trip_Status="Completed", Start_Date="2013-03-19", End_Date="2013-03-19", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Missa inaugural do Papa Francisco",
    Trip_Objective="Inicio del pontificado del Papa Francisco.",
    Source_Verification="Search Query: Dilma missa inaugural Papa Francisco 19 marco 2013",
    Source_Reliability="High", Methodological_Notes="19/03/2013.")

add("BRA-DR-J116", Trip_Status="Completed", Start_Date="2013-03-26", End_Date="2013-03-27", Duration_Days=2,
    Destination_Country="South Africa", Destination_City="Durban", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="V Cúpula BRICS",
    Trip_Objective="Cumbre BRICS de Durban; creacion del banco de los BRICS en agenda.",
    Source_Verification="Search Query: Dilma cupula BRICS Durban marco 2013",
    Source_Reliability="Medium", Methodological_Notes="26-27/03/2013.")

add("BRA-DR-J117", Trip_Status="Completed", Start_Date="2013-05-25", End_Date="2013-05-25", Duration_Days=1,
    Destination_Country="Ethiopia", Destination_City="Addis Ababa", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="50º aniversário da União Africana",
    Trip_Objective="Cumbre por los 50 anos de la OUA/Union Africana en Addis Abeba.",
    Source_Verification="Search Query: Dilma Uniao Africana 50 anos Addis Abeba maio 2013",
    Source_Reliability="Medium", Methodological_Notes="25/05/2013. Confirmar dias exactos.")

add("BRA-DR-J118", Trip_Status="Completed", Start_Date="2013-09-05", End_Date="2013-09-06", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Saint Petersburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de São Petersburgo",
    Trip_Objective="G20 de San Petersburgo; el espionaje de la NSA ya en agenda.",
    Source_Verification="Search Query: Dilma G20 Sao Petersburgo setembro 2013",
    Source_Reliability="High", Methodological_Notes="5-6/09/2013.")

add("BRA-DR-J119", Trip_Status="Completed", Start_Date="2013-09-24", End_Date="2013-09-24", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="68ª AGNU (discurso contra a espionagem da NSA)",
    Trip_Objective="Discurso historico de apertura contra el espionaje de la NSA sobre su gobierno y Petrobras.",
    Source_Verification="Search Query: Dilma discurso ONU espionagem NSA 24 setembro 2013",
    Source_Reliability="High", Methodological_Notes="24/09/2013.")

add("BRA-DR-J120", Trip_Status="Canceled", Start_Date="2013-10-23", End_Date="NA", Duration_Days="NA",
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Visita de Estado a Barack Obama",
    Trip_Objective="Visita de Estado prevista para el 23/10/2013. CANCELADA/postergada (anuncio 17/9/2013) por el espionaje de la NSA (caso Snowden) sobre Dilma y Petrobras.",
    Source_Verification="Search Query: Dilma cancela adia visita de Estado Washington 17 setembro 2013 NSA",
    Source_Reliability="High", Methodological_Notes="Cancelado emblematico; sin duracion. Unica visita de Estado a EE.UU. ofrecida ese anio a un lider extranjero.")

# ===== 2014 =====
add("BRA-DR-J121", Trip_Status="Completed", Start_Date="2014-01-27", End_Date="2014-01-29", Duration_Days=3,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cúpula CELAC + inauguração do porto de Mariel",
    Trip_Objective="Inauguracion del puerto de Mariel (financiado por el BNDES, 27/1) y II Cumbre CELAC (28-29/1).",
    Source_Verification="Search Query: Dilma Mariel CELAC Havana janeiro 2014",
    Source_Reliability="High", Methodological_Notes="27-29/01/2014.")

add("BRA-DR-J122", Trip_Status="Completed", Start_Date="2014-06-14", End_Date="2014-06-15", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Santa Cruz de la Sierra", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do G77+China (50 anos)",
    Trip_Objective="Cumbre extraordinaria del G77+China en Santa Cruz.",
    Source_Verification="Search Query: Dilma G77 China Santa Cruz junho 2014",
    Source_Reliability="Medium", Methodological_Notes="14-15/06/2014.")

add("BRA-DR-J123", Trip_Status="Completed", Start_Date="2014-09-24", End_Date="2014-09-24", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="69ª AGNU",
    Trip_Objective="Apertura de la 69a AGNU en plena campana electoral.",
    Source_Verification="Search Query: Dilma abertura 69 Assembleia ONU setembro 2014",
    Source_Reliability="Medium", Methodological_Notes="24/09/2014.")

add("BRA-DR-J124", Trip_Status="Completed", Start_Date="2014-11-15", End_Date="2014-11-16", Duration_Days=2,
    Destination_Country="Australia", Destination_City="Brisbane", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Brisbane",
    Trip_Objective="G20 de Brisbane, tras la reeleccion.",
    Source_Verification="Search Query: Dilma G20 Brisbane novembro 2014",
    Source_Reliability="Medium", Methodological_Notes="15-16/11/2014.")

add("BRA-DR-J125", Trip_Status="Completed", Start_Date="2014-12-17", End_Date="2014-12-17", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Paraná", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do MERCOSUL",
    Trip_Objective="Cumbre del Mercosur en Parana.",
    Source_Verification="Search Query: Dilma cupula Mercosul Parana dezembro 2014",
    Source_Reliability="Medium", Methodological_Notes="17/12/2014.")

# ===== 2015 =====
add("BRA-DR-J126", Trip_Status="Completed", Start_Date="2015-01-28", End_Date="2015-01-29", Duration_Days=2,
    Destination_Country="Costa Rica", Destination_City="Belén", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="III Cúpula CELAC",
    Trip_Objective="III Cumbre CELAC en Costa Rica.",
    Source_Verification="Search Query: Dilma CELAC Costa Rica Belen janeiro 2015",
    Source_Reliability="Medium", Methodological_Notes="28-29/01/2015.")

add("BRA-DR-J127", Trip_Status="Completed", Start_Date="2015-04-10", End_Date="2015-04-11", Duration_Days=2,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VII Cúpula das Américas",
    Trip_Objective="VII Cumbre de las Americas; historica por el deshielo Cuba-EE.UU. (Obama-Raul Castro).",
    Source_Verification="Search Query: Dilma VII Cupula das Americas Panama abril 2015",
    Source_Reliability="High", Methodological_Notes="10-11/04/2015.")

add("BRA-DR-J128", Trip_Status="Completed", Start_Date="2015-05-25", End_Date="2015-05-27", Duration_Days=3,
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Enrique Peña Nieto",
    Trip_Objective="Visita de Estado a Mexico; acuerdo de ampliacion comercial (ACE-53).",
    Source_Verification="Search Query: Dilma visita de Estado Mexico Pena Nieto maio 2015",
    Source_Reliability="Medium", Methodological_Notes="25-27/05/2015.")

add("BRA-DR-J129", Trip_Status="Completed", Start_Date="2015-06-27", End_Date="2015-07-01", Duration_Days=5,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Barack Obama (visita de 'reparação')",
    Trip_Objective="Visita oficial a EE.UU. finalmente realizada tras la cancelacion de 2013: NY (27-28/6), Washington con Obama (29-30/6) y San Francisco/Silicon Valley (1/7).",
    Source_Verification="Search Query: Dilma Obama visita Estados Unidos junho 2015 Silicon Valley",
    Source_Reliability="High", Methodological_Notes="Una salida multi-ciudad en un solo pais (NY, DC, SF).")

add("BRA-DR-J130", Trip_Status="Completed", Start_Date="2015-07-08", End_Date="2015-07-09", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Ufa", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VII Cúpula BRICS (Ufá)",
    Trip_Objective="Cumbre BRICS de Ufa; arranque del Nuevo Banco de Desarrollo.",
    Source_Verification="Search Query: Dilma cupula BRICS Ufa julho 2015",
    Source_Reliability="Medium", Methodological_Notes="8-9/07/2015.")

add("BRA-DR-J131", Trip_Status="Completed", Start_Date="2015-09-25", End_Date="2015-09-28", Duration_Days=4,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="70ª AGNU + Cúpula da Agenda 2030",
    Trip_Objective="Cumbre de Desarrollo Sostenible (Agenda 2030/ODS) y apertura de la 70a AGNU (28/9).",
    Source_Verification="Search Query: Dilma ONU Agenda 2030 setembro 2015",
    Source_Reliability="Medium", Methodological_Notes="25-28/09/2015.")

add("BRA-DR-J132", Trip_Status="Completed", Start_Date="2015-10-19", End_Date="2015-10-19", Duration_Days=1,
    Destination_Country="Sweden", Destination_City="Stockholm", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Stefan Löfven",
    Trip_Objective="Gira nordica: cooperacion (proyecto Gripen) e inversiones. Tramo 1.",
    Source_Verification="Search Query: Dilma Suecia Estocolmo outubro 2015 Gripen",
    Source_Reliability="Low", Methodological_Notes="Gira Suecia-Finlandia oct 2015; fechas estimadas.")

add("BRA-DR-J132", Trip_Status="Completed", Start_Date="2015-10-20", End_Date="2015-10-21", Duration_Days=2,
    Destination_Country="Finland", Destination_City="Helsinki", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Sauli Niinistö",
    Trip_Objective="Tramo 2 (final) de la gira nordica.",
    Source_Verification="Search Query: Dilma Finlandia Helsinki outubro 2015",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("BRA-DR-J133", Trip_Status="Completed", Start_Date="2015-11-15", End_Date="2015-11-16", Duration_Days=2,
    Destination_Country="Turkey", Destination_City="Antalya", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Antália",
    Trip_Objective="G20 de Antalya, marcado por los atentados de Paris.",
    Source_Verification="Search Query: Dilma G20 Antalia novembro 2015",
    Source_Reliability="Medium", Methodological_Notes="15-16/11/2015.")

add("BRA-DR-J134", Trip_Status="Completed", Start_Date="2015-11-30", End_Date="2015-11-30", Duration_Days=1,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="COP21 (Conferência do Clima)",
    Trip_Objective="Segmento de lideres de la COP21 que adopto el Acuerdo de Paris.",
    Source_Verification="Search Query: Dilma COP21 Paris 30 novembro 2015",
    Source_Reliability="High", Methodological_Notes="30/11/2015.")

add("BRA-DR-J135", Trip_Status="Completed", Start_Date="2015-12-21", End_Date="2015-12-21", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do MERCOSUL",
    Trip_Objective="Cumbre del Mercosur en Asuncion; primera con Macri.",
    Source_Verification="Search Query: Dilma cupula Mercosul Assuncao 21 dezembro 2015",
    Source_Reliability="Medium", Methodological_Notes="21/12/2015.")

# ===== 2016 (hasta la suspension del 12/5) =====
add("BRA-DR-J136", Trip_Status="Completed", Start_Date="2016-01-27", End_Date="2016-01-27", Duration_Days=1,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IV Cúpula CELAC",
    Trip_Objective="IV Cumbre CELAC en Quito, en plena crisis politica interna.",
    Source_Verification="Search Query: Dilma CELAC Quito janeiro 2016",
    Source_Reliability="Medium", Methodological_Notes="27/01/2016. Confirmar asistencia/duracion.")

add("BRA-DR-J137", Trip_Status="Completed", Start_Date="2016-04-22", End_Date="2016-04-22", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Assinatura do Acordo de Paris (ONU)",
    Trip_Objective="Firma del Acuerdo de Paris en la ONU, 5 dias despues de la votacion del impeachment en Diputados (17/4). ULTIMO viaje internacional antes de la suspension (12/5).",
    Source_Verification="Search Query: Dilma assina Acordo de Paris ONU 22 abril 2016",
    Source_Reliability="High", Methodological_Notes="Ultimo viaje del mandato efectivo.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
