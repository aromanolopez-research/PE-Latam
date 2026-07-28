# -*- coding: utf-8 -*-
"""
BRASIL — Lula da Silva, TERCER MANDATO (2023-01-01 a corte 2026-06-28, PT). Mandato EN CURSO.
Continua Trip_ID tras Bolsonaro (ultimo=234). Journey continua en BRA-LU3-J176.
"Brasil esta de volta": retorno de la diplomacia presidencial intensa tras el aislamiento de Bolsonaro.
Informe: ~46 viajes / 41 paises / 158 dias fuera hasta el corte. Se carga el nucleo verificado;
brecha y pendientes de 2026 documentados EN EL MOMENTO en PENDIENTES_VERIFICACION.txt.
CANCELADO clave: BRICS Kazan (oct-2024) por lesion craneal (participacion virtual).
Excluidos por ser en Brasil: cumbre sudamericana Brasilia (may23), Amazonia/OTCA Belem (ago23),
MERCOSUR Iguazu (jul23) y Rio (dic23), G20 Rio (nov24), BRICS Rio (jul25), COP30 Belem (nov25).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Luiz Inácio Lula da Silva"; O = "Brasil"
rows = []; tid = 235

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2023 =====
# Gira Argentina (CELAC) + Uruguay ene 2023 — 1 Journey_ID
add("BRA-LU3-J176", Trip_Status="Completed", Start_Date="2023-01-23", End_Date="2023-01-24", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VII Cúpula da CELAC + Alberto Fernández",
    Trip_Objective="Primer viaje del mandato: retorno de Brasil a la CELAC y bilateral con Alberto Fernandez. Tramo 1.",
    Source_Verification="Search Query: Lula primeiro viagem CELAC Buenos Aires janeiro 2023",
    Source_Reliability="High", Methodological_Notes="Primer viaje del 3er mandato.")

add("BRA-LU3-J176", Trip_Status="Completed", Start_Date="2023-01-25", End_Date="2023-01-25", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Luis Lacalle Pou",
    Trip_Objective="Bilateral con Lacalle Pou; Mercosur y acuerdo UE. Tramo 2 (final).",
    Source_Verification="Search Query: Lula Lacalle Pou Montevideu 25 janeiro 2023",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU3-J177", Trip_Status="Completed", Start_Date="2023-02-10", End_Date="2023-02-10", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Joe Biden (Casa Branca)",
    Trip_Objective="Bilateral con Biden; defensa de la democracia tras el 8/1 y el 6/1; medio ambiente.",
    Source_Verification="Search Query: Lula Biden Casa Branca 10 fevereiro 2023",
    Source_Reliability="High", Methodological_Notes="10/02/2023.")

# Gira China + EAU abr 2023 — 1 Journey_ID
add("BRA-LU3-J178", Trip_Status="Completed", Start_Date="2023-04-12", End_Date="2023-04-15", Duration_Days=4,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Xi Jinping + posse de Dilma no Novo Banco de Desenvolvimento (Xangai)",
    Trip_Objective="Visita de Estado a China; Dilma asume el Banco de los BRICS en Shanghai; propuesta del 'club de la paz' por Ucrania. Tramo 1.",
    Source_Verification="Search Query: Lula visita Estado China Xi Jinping abril 2023 Dilma banco BRICS",
    Source_Reliability="High", Methodological_Notes="Viaje pospuesto desde marzo por neumonia; 12-15/04/2023.")

add("BRA-LU3-J178", Trip_Status="Completed", Start_Date="2023-04-15", End_Date="2023-04-16", Duration_Days=2,
    Destination_Country="United Arab Emirates", Destination_City="Abu Dhabi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mohammed bin Zayed",
    Trip_Objective="Escala oficial de regreso; comercio e inversiones. Tramo 2 (final).",
    Source_Verification="Search Query: Lula Emirados Abu Dhabi abril 2023",
    Source_Reliability="Medium", Methodological_Notes="NA")

# Gira Portugal + Espana abr 2023 — 1 Journey_ID
add("BRA-LU3-J179", Trip_Status="Completed", Start_Date="2023-04-22", End_Date="2023-04-24", Duration_Days=3,
    Destination_Country="Portugal", Destination_City="Lisbon", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Marcelo Rebelo de Sousa + Prêmio Camões a Chico Buarque",
    Trip_Objective="Cumbre Brasil-Portugal; discurso en la Asamblea con protestas de Chega; premio Camoes. Tramo 1.",
    Source_Verification="Search Query: Lula Portugal abril 2023 Chico Buarque Camoes",
    Source_Reliability="High", Methodological_Notes="Gira Portugal-Espana 22-26/04/2023.")

add("BRA-LU3-J179", Trip_Status="Completed", Start_Date="2023-04-25", End_Date="2023-04-26", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Pedro Sánchez",
    Trip_Objective="Impulso al acuerdo Mercosur-UE con la presidencia espanola en puertas. Tramo 2 (final).",
    Source_Verification="Search Query: Lula Espanha Sanchez Madri abril 2023",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU3-J180", Trip_Status="Completed", Start_Date="2023-05-05", End_Date="2023-05-07", Duration_Days=3,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Coroação de Carlos III",
    Trip_Objective="Coronacion del rey Carlos III; bilaterales al margen.",
    Source_Verification="Search Query: Lula coroacao Carlos III Londres maio 2023",
    Source_Reliability="High", Methodological_Notes="5-7/05/2023.")

add("BRA-LU3-J181", Trip_Status="Completed", Start_Date="2023-05-19", End_Date="2023-05-21", Duration_Days=3,
    Destination_Country="Japan", Destination_City="Hiroshima", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G7 (convidado)",
    Trip_Objective="Invitado al G7 de Hiroshima; el encuentro previsto con Zelenski no se concreto.",
    Source_Verification="Search Query: Lula G7 Hiroshima maio 2023 Zelenski",
    Source_Reliability="High", Methodological_Notes="19-21/05/2023.")

# Gira Italia/Vaticano + Francia jun 2023 — 1 Journey_ID
add("BRA-LU3-J182", Trip_Status="Completed", Start_Date="2023-06-21", End_Date="2023-06-21", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Papa Francisco (+ Meloni e Mattarella em Roma)",
    Trip_Objective="Audiencia con el Papa Francisco sobre la paz en Ucrania; en Roma vio a Meloni y Mattarella. Tramo 1.",
    Source_Verification="Search Query: Lula Papa Francisco Vaticano junho 2023 Meloni",
    Source_Reliability="High", Methodological_Notes="Gira Italia-Francia 21-23/06/2023.")

add("BRA-LU3-J182", Trip_Status="Completed", Start_Date="2023-06-22", End_Date="2023-06-23", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula por um Novo Pacto Financeiro Global (Macron)",
    Trip_Objective="Cumbre por un Nuevo Pacto Financiero Global convocada por Macron. Tramo 2 (final).",
    Source_Verification="Search Query: Lula Paris Novo Pacto Financeiro Global junho 2023",
    Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU3-J183", Trip_Status="Completed", Start_Date="2023-07-17", End_Date="2023-07-18", Duration_Days=2,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula CELAC-União Europeia",
    Trip_Objective="Cumbre CELAC-UE en Bruselas tras 8 anos; negociacion del acuerdo Mercosur-UE.",
    Source_Verification="Search Query: Lula cupula CELAC UE Bruxelas julho 2023",
    Source_Reliability="High", Methodological_Notes="17-18/07/2023.")

add("BRA-LU3-J184", Trip_Status="Completed", Start_Date="2023-08-22", End_Date="2023-08-24", Duration_Days=3,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XV Cúpula BRICS (ampliação do bloco)",
    Trip_Objective="Cumbre BRICS de Johannesburgo; ampliacion del bloque a 6 nuevos miembros.",
    Source_Verification="Search Query: Lula cupula BRICS Joanesburgo agosto 2023 ampliacao",
    Source_Reliability="High", Methodological_Notes="22-24/08/2023.")

add("BRA-LU3-J185", Trip_Status="Completed", Start_Date="2023-09-08", End_Date="2023-09-11", Duration_Days=4,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Nova Délhi",
    Trip_Objective="G20 de Nueva Delhi; Brasil recibe la presidencia del G20 para 2024.",
    Source_Verification="Search Query: Lula G20 Nova Delhi setembro 2023 presidencia",
    Source_Reliability="High", Methodological_Notes="8-11/09/2023.")

# Gira Cuba (G77) + EE.UU. (AGNU) sep 2023 — 1 Journey_ID
add("BRA-LU3-J186", Trip_Status="Completed", Start_Date="2023-09-15", End_Date="2023-09-16", Duration_Days=2,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G77+China",
    Trip_Objective="Cumbre del G77+China en La Habana; agenda del Sur Global. Tramo 1.",
    Source_Verification="Search Query: Lula G77 Havana setembro 2023",
    Source_Reliability="Medium", Methodological_Notes="Gira Cuba-NY 15-20/09/2023.")

add("BRA-LU3-J186", Trip_Status="Completed", Start_Date="2023-09-18", End_Date="2023-09-20", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="78ª AGNU (+ Biden, Lançamento parceria trabalhista)",
    Trip_Objective="Apertura de la 78a AGNU; lanzamiento con Biden de la alianza por los derechos laborales. Tramo 2 (final).",
    Source_Verification="Search Query: Lula abertura 78 Assembleia ONU setembro 2023 Biden",
    Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU3-J187", Trip_Status="Completed", Start_Date="2023-11-21", End_Date="2023-11-23", Duration_Days=3,
    Destination_Country="Saudi Arabia", Destination_City="Riyadh", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Príncipe Mohammed bin Salman",
    Trip_Objective="Visita a Arabia Saudita; inversiones y OPEP+.",
    Source_Verification="Search Query: Lula Arabia Saudita novembro 2023",
    Source_Reliability="Medium", Methodological_Notes="21-23/11/2023. Confirmar fechas exactas.")

add("BRA-LU3-J188", Trip_Status="Completed", Start_Date="2023-11-30", End_Date="2023-12-02", Duration_Days=3,
    Destination_Country="United Arab Emirates", Destination_City="Dubai", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="COP28",
    Trip_Objective="Cumbre climatica COP28 en Dubai; Brasil anuncio candidatura de Belem para la COP30.",
    Source_Verification="Search Query: Lula COP28 Dubai dezembro 2023",
    Source_Reliability="High", Methodological_Notes="30/11-2/12/2023. Cirugia de cadera fue despues (posterior).")

add("BRA-LU3-J189", Trip_Status="Completed", Start_Date="2023-12-04", End_Date="2023-12-05", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Consultas intergovernamentais (Olaf Scholz)",
    Trip_Objective="Consultas intergubernamentales germano-brasilenas; industria e inversiones.",
    Source_Verification="Search Query: Lula Alemanha Scholz Berlim dezembro 2023",
    Source_Reliability="Medium", Methodological_Notes="4-5/12/2023. Verificar (cirugia de cadera a fin de mes).")

# ===== 2024 =====
# Gira Egipto + Etiopia (UA) feb 2024 — 1 Journey_ID
add("BRA-LU3-J190", Trip_Status="Completed", Start_Date="2024-02-14", End_Date="2024-02-15", Duration_Days=2,
    Destination_Country="Egypt", Destination_City="Cairo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Abdel Fattah al-Sisi",
    Trip_Objective="Visita a Egipto; canal de Suez, BRICS y Gaza. Tramo 1.",
    Source_Verification="Search Query: Lula Egito Al-Sisi fevereiro 2024",
    Source_Reliability="Medium", Methodological_Notes="Gira Egipto-Etiopia 14-18/02/2024.")

add("BRA-LU3-J190", Trip_Status="Completed", Start_Date="2024-02-17", End_Date="2024-02-18", Duration_Days=2,
    Destination_Country="Ethiopia", Destination_City="Addis Ababa", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula da União Africana",
    Trip_Objective="Cumbre de la UA; la comparacion de Gaza con el Holocausto desato crisis con Israel (declarado persona non grata). Tramo 2 (final).",
    Source_Verification="Search Query: Lula Uniao Africana Adis Abeba fevereiro 2024 Gaza Holocausto Israel",
    Source_Reliability="High", Methodological_Notes="Crisis diplomatica con Israel.")

# Gira Guyana (CARICOM) + San Vicente (CELAC) feb-mar 2024 — 1 Journey_ID
add("BRA-LU3-J191", Trip_Status="Completed", Start_Date="2024-02-28", End_Date="2024-02-29", Duration_Days=2,
    Destination_Country="Guyana", Destination_City="Georgetown", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula da CARICOM",
    Trip_Objective="Cumbre de la CARICOM; tension Guyana-Venezuela por el Esequibo. Tramo 1.",
    Source_Verification="Search Query: Lula CARICOM Georgetown Guiana fevereiro 2024",
    Source_Reliability="Medium", Methodological_Notes="Gira 28/2-1/3/2024.")

add("BRA-LU3-J191", Trip_Status="Completed", Start_Date="2024-03-01", End_Date="2024-03-01", Duration_Days=1,
    Destination_Country="Saint Vincent and the Grenadines", Destination_City="Kingstown", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="VIII Cúpula da CELAC",
    Trip_Objective="Cumbre CELAC en Kingstown. Tramo 2 (final).",
    Source_Verification="Search Query: Lula CELAC Kingstown Sao Vicente marco 2024",
    Source_Reliability="Medium", Methodological_Notes="1/03/2024.")

add("BRA-LU3-J192", Trip_Status="Completed", Start_Date="2024-07-08", End_Date="2024-07-09", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Santa Cruz de la Sierra", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do MERCOSUL",
    Trip_Objective="Cumbre del Mercosur en Bolivia (ingreso pleno de Bolivia al bloque).",
    Source_Verification="Search Query: Lula cupula Mercosul Santa Cruz Bolivia julho 2024",
    Source_Reliability="Medium", Methodological_Notes="8-9/07/2024. Confirmar sede/fecha.")

add("BRA-LU3-J193", Trip_Status="Completed", Start_Date="2024-08-05", End_Date="2024-08-06", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gabriel Boric",
    Trip_Objective="Visita de Estado a Chile; integracion regional y democracia.",
    Source_Verification="Search Query: Lula visita Estado Chile Boric agosto 2024",
    Source_Reliability="Medium", Methodological_Notes="5-6/08/2024. Confirmar fechas.")

add("BRA-LU3-J194", Trip_Status="Completed", Start_Date="2024-09-22", End_Date="2024-09-24", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="79ª AGNU",
    Trip_Objective="Apertura de la 79a AGNU; Cumbre del Futuro.",
    Source_Verification="Search Query: Lula abertura 79 Assembleia ONU setembro 2024",
    Source_Reliability="High", Methodological_Notes="22-24/09/2024.")

add("BRA-LU3-J195", Trip_Status="Canceled", Start_Date="2024-10-22", End_Date="NA", Duration_Days="NA",
    Destination_Country="Russia", Destination_City="Kazan", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="XVI Cúpula BRICS (Kazan)",
    Trip_Objective="Cumbre BRICS de Kazan. CANCELADO tras una caida domestica con traumatismo craneal (19/10/2024); participo por videoconferencia.",
    Source_Verification="Search Query: Lula cancela BRICS Kazan outubro 2024 queda cabeca video",
    Source_Reliability="High", Methodological_Notes="Cancelado por salud; sin duracion. Participacion virtual.")

# ===== 2025 =====
add("BRA-LU3-J196", Trip_Status="Completed", Start_Date="2025-03-01", End_Date="2025-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Yamandú Orsi",
    Trip_Objective="Asuncion de Yamandu Orsi en Uruguay; regreso de la izquierda al gobierno.",
    Source_Verification="Search Query: Lula posse Yamandu Orsi Montevideu marco 2025",
    Source_Reliability="Medium", Methodological_Notes="1/03/2025. Confirmar.")

# Gira Japon + Vietnam mar 2025 — 1 Journey_ID
add("BRA-LU3-J197", Trip_Status="Completed", Start_Date="2025-03-24", End_Date="2025-03-27", Duration_Days=4,
    Destination_Country="Japan", Destination_City="Tokyo", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Imperador Naruhito / Shigeru Ishiba",
    Trip_Objective="Visita de Estado a Japon; comercio e inversiones. Tramo 1.",
    Source_Verification="Search Query: Lula visita Estado Japao marco 2025",
    Source_Reliability="Medium", Methodological_Notes="Gira Asia mar 2025; fechas a confirmar (pendiente).")

add("BRA-LU3-J197", Trip_Status="Completed", Start_Date="2025-03-27", End_Date="2025-03-29", Duration_Days=3,
    Destination_Country="Vietnam", Destination_City="Hanoi", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Governo do Vietnã",
    Trip_Objective="Visita de Estado a Vietnam; comercio Sur-Sur. Tramo 2 (final).",
    Source_Verification="Search Query: Lula Vietna Hanoi marco 2025",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas (pendiente de confirmar).")

add("BRA-LU3-J198", Trip_Status="Completed", Start_Date="2025-04-09", End_Date="2025-04-09", Duration_Days=1,
    Destination_Country="Honduras", Destination_City="Tegucigalpa", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IX Cúpula da CELAC",
    Trip_Objective="Cumbre CELAC en Tegucigalpa.",
    Source_Verification="Search Query: Lula CELAC Tegucigalpa Honduras abril 2025",
    Source_Reliability="Medium", Methodological_Notes="9/04/2025. Confirmar.")

# Gira Rusia (Dia de la Victoria) + China (Foro CELAC-China) may 2025 — 1 Journey_ID
add("BRA-LU3-J199", Trip_Status="Completed", Start_Date="2025-05-09", End_Date="2025-05-10", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Vladímir Putin (desfile dos 80 anos da vitória)",
    Trip_Objective="Desfile del Dia de la Victoria (80 anos) en Moscu; bilateral con Putin; muy comentado. Tramo 1.",
    Source_Verification="Search Query: Lula Moscou Putin Dia da Vitoria maio 2025 80 anos",
    Source_Reliability="High", Methodological_Notes="Gira Rusia-China 9-13/05/2025.")

add("BRA-LU3-J199", Trip_Status="Completed", Start_Date="2025-05-12", End_Date="2025-05-13", Duration_Days=2,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Fórum CELAC-China + Xi Jinping",
    Trip_Objective="Foro CELAC-China en Beijing y bilateral con Xi; inversiones y Franja y la Ruta. Tramo 2 (final).",
    Source_Verification="Search Query: Lula Forum CELAC China Pequim maio 2025 Xi",
    Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU3-J200", Trip_Status="Completed", Start_Date="2025-06-05", End_Date="2025-06-06", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Visita de Estado a Francia; acuerdo Mercosur-UE y medio ambiente rumbo a la COP30.",
    Source_Verification="Search Query: Lula visita Estado Franca Macron junho 2025",
    Source_Reliability="Medium", Methodological_Notes="5-6/06/2025. Confirmar.")

add("BRA-LU3-J201", Trip_Status="Completed", Start_Date="2025-09-23", End_Date="2025-09-24", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="80ª AGNU (+ encontro breve com Trump)",
    Trip_Objective="Apertura de la 80a AGNU; contexto de tension con Trump por aranceles del 50%; breve encuentro/saludo.",
    Source_Verification="Search Query: Lula abertura 80 Assembleia ONU setembro 2025 Trump tarifas",
    Source_Reliability="High", Methodological_Notes="23-24/09/2025.")

add("BRA-LU3-J202", Trip_Status="Completed", Start_Date="2025-10-26", End_Date="2025-10-27", Duration_Days=2,
    Destination_Country="Malaysia", Destination_City="Kuala Lumpur", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula da ASEAN (+ reunião com Trump)",
    Trip_Objective="Cumbre ASEAN en Kuala Lumpur; reunion con Trump que descomprimio la crisis arancelaria.",
    Source_Verification="Search Query: Lula ASEAN Kuala Lumpur outubro 2025 Trump reuniao",
    Source_Reliability="Medium", Methodological_Notes="26-27/10/2025. Confirmar fechas.")

add("BRA-LU3-J203", Trip_Status="Completed", Start_Date="2025-11-09", End_Date="2025-11-10", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Santa Marta", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IV Cúpula CELAC-União Europeia",
    Trip_Objective="Cumbre CELAC-UE en Santa Marta.",
    Source_Verification="Search Query: Lula cupula CELAC UE Santa Marta Colombia novembro 2025",
    Source_Reliability="Medium", Methodological_Notes="9-10/11/2025. Confirmar.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (3er mandato 2023-2026) agregadas. Ultimo Trip_ID = {tid-1}")
