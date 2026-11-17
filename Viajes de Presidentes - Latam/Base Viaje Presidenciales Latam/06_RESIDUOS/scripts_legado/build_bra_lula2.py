# -*- coding: utf-8 -*-
"""
BRASIL — Lula da Silva, SEGUNDO MANDATO (2007-01-01 a 2011-01-01). TRAMO 2 de 2.
Continua Trip_ID tras tramo 1 (ultimo=77). Journey continua en BRA-LU-J059.
El mandato mas denso: ~66 giras / 146 visitas-pais / 276 dias fuera (2009 record: 92 dias).
Se carga el nucleo verificado (fechas oficiales Biblioteca da Presidencia para 2008; hitos anclados
para 2007/2009/2010) + 2 CANCELADOS documentados (Davos ene-2010, G20 Toronto jun-2010).
Brecha vs ~66 giras documentada EN EL MOMENTO en PENDIENTES_VERIFICACION.txt.
Giras multipais = 1 Journey_ID. Excluidos por ser en Brasil: MERCOSUR Rio ene07, UNASUR Brasilia may08,
CALC Sauipe dic08, BRIC Brasilia abr10, MERCOSUR Foz dic10.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Luiz Inácio Lula da Silva"; O = "Brasil"
rows = []; tid = 78

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

BIB = "https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/viagens/viagens-1"

# ===== 2007 =====
add("BRA-LU-J059", Trip_Status="Completed", Start_Date="2007-01-15", End_Date="2007-01-15", Duration_Days=1,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Rafael Correa",
    Trip_Objective="Asuncion de Rafael Correa en Ecuador.",
    Source_Verification="Search Query: Lula posse Rafael Correa Quito 15 janeiro 2007",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J060", Trip_Status="Completed", Start_Date="2007-03-31", End_Date="2007-03-31", Duration_Days=1,
    Destination_Country="United States", Destination_City="Camp David", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="George W. Bush (acordo do etanol)",
    Trip_Objective="Reunion en Camp David con Bush; alianza de biocombustibles/etanol.",
    Source_Verification="Search Query: Lula Bush Camp David etanol 31 marco 2007",
    Source_Reliability="Medium", Methodological_Notes="Primer presidente brasileno en Camp David.")

# Gira India + G8 Heiligendamm (jun 2007), 1 Journey_ID
add("BRA-LU-J061", Trip_Status="Completed", Start_Date="2007-06-03", End_Date="2007-06-05", Duration_Days=3,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="A.P.J. Abdul Kalam / Manmohan Singh",
    Trip_Objective="Visita a India; banquete oficial en Nova Delhi (4/6) y seminario empresarial Brasil-India. Tramo 1.",
    Source_Verification="https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva",
    Source_Reliability="High", Methodological_Notes="Discursos oficiales fechados 04/06/2007 en Nova Delhi (Biblioteca). Marruecos estaba en agenda y fue POSPUESTO (Itamaraty 30/05/2007).")

add("BRA-LU-J061", Trip_Status="Completed", Start_Date="2007-06-07", End_Date="2007-06-08", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Heiligendamm", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G8 ampliada (G8+5)",
    Trip_Objective="Segmento ampliado del G8 (G8+5) en Heiligendamm. Tramo 2 (final).",
    Source_Verification="Search Query: Lula G8 Heiligendamm junho 2007 G8+5",
    Source_Reliability="Medium", Methodological_Notes="G8 6-8/06/2007; segmento ampliado 8/6.")

add("BRA-LU-J062", Trip_Status="Completed", Start_Date="2007-07-04", End_Date="2007-07-04", Duration_Days=1,
    Destination_Country="Portugal", Destination_City="Lisbon", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="I Cúpula Brasil-União Europeia",
    Trip_Objective="Primera cumbre estrategica Brasil-UE, en Lisboa (presidencia portuguesa de la UE).",
    Source_Verification="Search Query: Lula primeira cupula Brasil Uniao Europeia Lisboa julho 2007",
    Source_Reliability="Medium", Methodological_Notes="4/07/2007.")

# Gira nordica sep 2007 (1 Journey_ID): Suecia, Dinamarca, Noruega
add("BRA-LU-J063", Trip_Status="Completed", Start_Date="2007-09-11", End_Date="2007-09-11", Duration_Days=1,
    Destination_Country="Sweden", Destination_City="Stockholm", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Governo da Suécia",
    Trip_Objective="Gira nordica (primera de un presidente brasileno): biocombustibles y tecnologia. Tramo 1.",
    Source_Verification="Search Query: Lula gira paises nordicos Suecia Dinamarca Noruega setembro 2007",
    Source_Reliability="Low", Methodological_Notes="Gira nordica sep 2007; fechas estimadas.")

add("BRA-LU-J063", Trip_Status="Completed", Start_Date="2007-09-12", End_Date="2007-09-12", Duration_Days=1,
    Destination_Country="Denmark", Destination_City="Copenhagen", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Governo da Dinamarca",
    Trip_Objective="Tramo 2 de la gira nordica.",
    Source_Verification="Search Query: Lula Dinamarca setembro 2007",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("BRA-LU-J063", Trip_Status="Completed", Start_Date="2007-09-13", End_Date="2007-09-13", Duration_Days=1,
    Destination_Country="Norway", Destination_City="Oslo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Governo da Noruega",
    Trip_Objective="Tramo 3 (final) de la gira nordica.",
    Source_Verification="Search Query: Lula Noruega setembro 2007",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada.")

add("BRA-LU-J064", Trip_Status="Completed", Start_Date="2007-09-25", End_Date="2007-09-25", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="62ª AGNU",
    Trip_Objective="Apertura de la 62a Asamblea General de la ONU.",
    Source_Verification="Search Query: Lula abertura 62 Assembleia Geral ONU setembro 2007",
    Source_Reliability="Medium", Methodological_Notes="NA")

# Gira Africa oct 2007 (1 Journey_ID): Burkina Faso, Congo, Sudafrica, Angola
add("BRA-LU-J065", Trip_Status="Completed", Start_Date="2007-10-15", End_Date="2007-10-15", Duration_Days=1,
    Destination_Country="Burkina Faso", Destination_City="Ouagadougou", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Blaise Compaoré",
    Trip_Objective="Gira africana: biocombustibles y cooperacion. Tramo 1.",
    Source_Verification="Search Query: Lula viagem Africa outubro 2007 Burkina Faso Congo Africa do Sul Angola",
    Source_Reliability="Medium", Methodological_Notes="Gira 14-19 oct 2007; fechas de dia estimadas.")

add("BRA-LU-J065", Trip_Status="Completed", Start_Date="2007-10-16", End_Date="2007-10-16", Duration_Days=1,
    Destination_Country="Republic of the Congo", Destination_City="Brazzaville", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Denis Sassou-Nguesso",
    Trip_Objective="Tramo 2 de la gira africana.",
    Source_Verification="Search Query: Lula Congo Brazzaville outubro 2007",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J065", Trip_Status="Completed", Start_Date="2007-10-17", End_Date="2007-10-17", Duration_Days=1,
    Destination_Country="South Africa", Destination_City="Pretoria", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cúpula IBSA (Índia-Brasil-África do Sul)",
    Trip_Objective="Cumbre IBSA en Pretoria. Tramo 3.",
    Source_Verification="Search Query: Lula cupula IBSA Pretoria outubro 2007",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J065", Trip_Status="Completed", Start_Date="2007-10-18", End_Date="2007-10-18", Duration_Days=1,
    Destination_Country="Angola", Destination_City="Luanda", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="José Eduardo dos Santos",
    Trip_Objective="Tramo 4 (final) de la gira africana.",
    Source_Verification="Search Query: Lula Angola outubro 2007",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J066", Trip_Status="Completed", Start_Date="2007-11-08", End_Date="2007-11-10", Duration_Days=3,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XVII Cúpula Ibero-Americana",
    Trip_Objective="Cumbre Iberoamericana de Santiago (la del 'por que no te callas').",
    Source_Verification="https://segib.org/?summit=xvii-cumbre-iberoamericana-santiago-2007",
    Source_Reliability="High", Methodological_Notes="NA")

# ===== 2008 (bloque con fechas oficiales de la Biblioteca) =====
add("BRA-LU-J067", Trip_Status="Completed", Start_Date="2008-07-08", End_Date="2008-07-09", Duration_Days=2,
    Destination_Country="Japan", Destination_City="Toyako", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G8 ampliada (Toyako/Hokkaido)",
    Trip_Objective="Segmento ampliado del G8 en Japon. Tramo 1 de gira asiatica oficial 05-13/07/2008.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales Biblioteca: Japon 8-9, Vietnam 9-10, Timor 11, Indonesia 11-12.")

add("BRA-LU-J067", Trip_Status="Completed", Start_Date="2008-07-09", End_Date="2008-07-10", Duration_Days=2,
    Destination_Country="Vietnam", Destination_City="Hanoi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Nguyen Minh Triet",
    Trip_Objective="Visita oficial a Vietnam. Tramo 2.",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J067", Trip_Status="Completed", Start_Date="2008-07-11", End_Date="2008-07-11", Duration_Days=1,
    Destination_Country="East Timor", Destination_City="Dili", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="José Ramos-Horta",
    Trip_Objective="Visita al Timor Oriental (CPLP). Tramo 3.",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J067", Trip_Status="Completed", Start_Date="2008-07-11", End_Date="2008-07-12", Duration_Days=2,
    Destination_Country="Indonesia", Destination_City="Jakarta", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Susilo Bambang Yudhoyono",
    Trip_Objective="Visita oficial a Indonesia. Tramo 4 (final).",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J068", Trip_Status="Completed", Start_Date="2008-07-18", End_Date="2008-07-18", Duration_Days=1,
    Destination_Country="Bolivia", Destination_City="La Paz", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Evo Morales",
    Trip_Objective="Visita oficial a Bolivia. Tramo 1.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales: Bolivia 18/07, Colombia 19-20/07.")

add("BRA-LU-J068", Trip_Status="Completed", Start_Date="2008-07-19", End_Date="2008-07-20", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Álvaro Uribe",
    Trip_Objective="Visita oficial a Colombia. Tramo 2 (final).",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J069", Trip_Status="Completed", Start_Date="2008-07-24", End_Date="2008-07-25", Duration_Days=2,
    Destination_Country="Portugal", Destination_City="Lisbon", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Visita oficial a Lisboa",
    Trip_Objective="Visita oficial a Portugal; acuerdo ortografico CPLP en agenda.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (24-25/07/2008).")

add("BRA-LU-J070", Trip_Status="Completed", Start_Date="2008-08-03", End_Date="2008-08-04", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cristina Fernández de Kirchner",
    Trip_Objective="Visita oficial a Argentina. Tramo 1.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales: Argentina 3-4/08, China 5-8/08.")

add("BRA-LU-J070", Trip_Status="Completed", Start_Date="2008-08-05", End_Date="2008-08-08", Duration_Days=4,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Hu Jintao (abertura dos JJOO de Pequim)",
    Trip_Objective="Visita a China y apertura de los JJOO de Beijing (8/8). Tramo 2 (final).",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J071", Trip_Status="Completed", Start_Date="2008-08-14", End_Date="2008-08-15", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Fernando Lugo",
    Trip_Objective="Asuncion de Fernando Lugo en Paraguay.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (14-15/08/2008).")

add("BRA-LU-J072", Trip_Status="Completed", Start_Date="2008-09-15", End_Date="2008-09-15", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Reunião extraordinária da UNASUL (crise boliviana)",
    Trip_Objective="Cumbre extraordinaria de UNASUR en Santiago por la crisis de Pando; respaldo a Evo.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fecha oficial (15/09/2008).")

add("BRA-LU-J073", Trip_Status="Completed", Start_Date="2008-09-21", End_Date="2008-09-25", Duration_Days=5,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="63ª AGNU",
    Trip_Objective="Apertura de la 63a AGNU en plena crisis financiera global.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (21-25/09/2008).")

add("BRA-LU-J074", Trip_Status="Completed", Start_Date="2008-10-12", End_Date="2008-10-14", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Juan Carlos I / José Luis Rodríguez Zapatero",
    Trip_Objective="Visita oficial a Espana. Tramo 1 de gira oficial 12-17/10/2008.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales: Espana 12-14, India 14-15, Mozambique 16-17.")

add("BRA-LU-J074", Trip_Status="Completed", Start_Date="2008-10-14", End_Date="2008-10-15", Duration_Days=2,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="III Cúpula IBSA",
    Trip_Objective="Cumbre IBSA en Nueva Delhi. Tramo 2.",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J074", Trip_Status="Completed", Start_Date="2008-10-16", End_Date="2008-10-17", Duration_Days=2,
    Destination_Country="Mozambique", Destination_City="Maputo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Armando Guebuza",
    Trip_Objective="Visita oficial a Mozambique. Tramo 3 (final).",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J075", Trip_Status="Completed", Start_Date="2008-10-29", End_Date="2008-10-31", Duration_Days=3,
    Destination_Country="El Salvador", Destination_City="San Salvador", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XVIII Cúpula Ibero-Americana",
    Trip_Objective="Cumbre Iberoamericana de San Salvador; siguio a Cuba.",
    Source_Verification="https://segib.org/es/cumbres-iberoamericanas/",
    Source_Reliability="Medium", Methodological_Notes="Verificar dias exactos; el informe indica gira San Salvador + La Habana (30/10-1/11).")

add("BRA-LU-J076", Trip_Status="Completed", Start_Date="2008-11-14", End_Date="2008-11-15", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="I Cúpula do G20 financeiro",
    Trip_Objective="Primera cumbre de lideres del G20 (crisis financiera); Brasil protagonista del nuevo foro.",
    Source_Verification="Search Query: Lula primeira cupula G20 Washington novembro 2008",
    Source_Reliability="High", Methodological_Notes="14-15/11/2008. Precedida por visita de Estado a Italia (8-13/11, a cargar al completar).")

# ===== 2009 (año récord: 92 días fuera) =====
add("BRA-LU-J077", Trip_Status="Completed", Start_Date="2009-03-14", End_Date="2009-03-14", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Barack Obama (Casa Branca)",
    Trip_Objective="Primera reunion con Obama en el Salon Oval; crisis global y agenda bilateral.",
    Source_Verification="Search Query: Lula Obama Casa Branca 14 marco 2009",
    Source_Reliability="High", Methodological_Notes="14/03/2009.")

add("BRA-LU-J078", Trip_Status="Completed", Start_Date="2009-03-30", End_Date="2009-03-31", Duration_Days=2,
    Destination_Country="Qatar", Destination_City="Doha", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cúpula América do Sul-Países Árabes (ASPA)",
    Trip_Objective="II Cumbre ASPA en Doha (proceso iniciado por Brasil en 2005). Tramo 1.",
    Source_Verification="Search Query: Lula cupula ASPA Doha marco 2009",
    Source_Reliability="Medium", Methodological_Notes="ASPA II: 31/03/2009. Gira previa por Chile (27-28/3, a completar).")

add("BRA-LU-J078", Trip_Status="Completed", Start_Date="2009-04-01", End_Date="2009-04-02", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Londres",
    Trip_Objective="G20 de Londres; Gordon Brown y la frase 'este e o cara'. Tramo 2 (final).",
    Source_Verification="Search Query: Lula G20 Londres abril 2009 Gordon Brown",
    Source_Reliability="High", Methodological_Notes="1-2/04/2009. Incluyo escala en Francia (1/4).")

add("BRA-LU-J079", Trip_Status="Completed", Start_Date="2009-04-17", End_Date="2009-04-19", Duration_Days=3,
    Destination_Country="Trinidad and Tobago", Destination_City="Port of Spain", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="V Cúpula das Américas",
    Trip_Objective="V Cumbre de las Americas; debut regional de Obama.",
    Source_Verification="Search Query: Lula V Cupula das Americas Trinidad abril 2009",
    Source_Reliability="High", Methodological_Notes="17-19/04/2009.")

add("BRA-LU-J080", Trip_Status="Completed", Start_Date="2009-05-16", End_Date="2009-05-17", Duration_Days=2,
    Destination_Country="Saudi Arabia", Destination_City="Riyadh", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rei Abdullah",
    Trip_Objective="Gira Medio Oriente-Asia: comercio e inversiones. Tramo 1.",
    Source_Verification="Search Query: Lula Arabia Saudita maio 2009",
    Source_Reliability="Low", Methodological_Notes="Gira may 2009 (Arabia Saudita-China-Turquia); fechas estimadas.")

add("BRA-LU-J080", Trip_Status="Completed", Start_Date="2009-05-18", End_Date="2009-05-20", Duration_Days=3,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hu Jintao",
    Trip_Objective="Visita a China en plena crisis global; China ya primer socio comercial de Brasil. Tramo 2.",
    Source_Verification="Search Query: Lula China maio 2009 Hu Jintao",
    Source_Reliability="Medium", Methodological_Notes="18-20/05/2009.")

add("BRA-LU-J080", Trip_Status="Completed", Start_Date="2009-05-21", End_Date="2009-05-22", Duration_Days=2,
    Destination_Country="Turkey", Destination_City="Ankara", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Abdullah Gül / Recep Tayyip Erdoğan",
    Trip_Objective="Visita oficial a Turquia; semilla de la mediacion conjunta sobre Iran. Tramo 3 (final).",
    Source_Verification="Search Query: Lula Turquia maio 2009 visita oficial",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("BRA-LU-J081", Trip_Status="Completed", Start_Date="2009-06-15", End_Date="2009-06-15", Duration_Days=1,
    Destination_Country="Switzerland", Destination_City="Geneva", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Conferência da OIT (Pacto Mundial pelo Emprego)",
    Trip_Objective="Discurso en la Conferencia de la OIT en Ginebra; empleo y crisis. Tramo 1.",
    Source_Verification="Search Query: Lula OIT Genebra junho 2009 discurso",
    Source_Reliability="Medium", Methodological_Notes="15/06/2009.")

add("BRA-LU-J081", Trip_Status="Completed", Start_Date="2009-06-16", End_Date="2009-06-16", Duration_Days=1,
    Destination_Country="Russia", Destination_City="Yekaterinburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="I Cúpula dos BRIC",
    Trip_Objective="Primera cumbre de los BRIC en Ekaterimburgo; institucionalizacion del bloque. Tramo 2.",
    Source_Verification="Search Query: Lula primeira cupula BRIC Ecaterimburgo 16 junho 2009",
    Source_Reliability="High", Methodological_Notes="16/06/2009. Informe indica tramo Kazajistan (17/6) a completar.")

add("BRA-LU-J082", Trip_Status="Completed", Start_Date="2009-07-08", End_Date="2009-07-10", Duration_Days=3,
    Destination_Country="Italy", Destination_City="L'Aquila", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G8+5 (L'Aquila)",
    Trip_Objective="Cumbre del G8+5 en L'Aquila; clima y crisis. Precedida por Francia (Paris 4-7/7, Sarkozy).",
    Source_Verification="Search Query: Lula G8 L'Aquila julho 2009",
    Source_Reliability="Medium", Methodological_Notes="8-10/07/2009; tramo Francia de la misma gira a completar.")

add("BRA-LU-J083", Trip_Status="Completed", Start_Date="2009-09-23", End_Date="2009-09-25", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="64ª AGNU + Cúpula do G20 de Pittsburgh",
    Trip_Objective="Apertura de la 64a AGNU (23/9) y cumbre del G20 en Pittsburgh (24-25/9), una sola salida.",
    Source_Verification="Search Query: Lula AGNU G20 Pittsburgh setembro 2009",
    Source_Reliability="High", Methodological_Notes="Salida oficial 21-25/09/2009 (NY + Pittsburgh).")

add("BRA-LU-J084", Trip_Status="Completed", Start_Date="2009-09-26", End_Date="2009-09-27", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Isla Margarita", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cúpula América do Sul-África (ASA)",
    Trip_Objective="II Cumbre ASA en Isla Margarita; anfitrion Chavez.",
    Source_Verification="Search Query: Lula cupula ASA Ilha Margarita setembro 2009",
    Source_Reliability="Medium", Methodological_Notes="26-27/09/2009.")

add("BRA-LU-J085", Trip_Status="Completed", Start_Date="2009-10-01", End_Date="2009-10-02", Duration_Days=2,
    Destination_Country="Denmark", Destination_City="Copenhagen", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Sessão do COI (eleição olímpica)",
    Trip_Objective="Defensa de la candidatura de Rio 2016 ante el COI; Rio electa sede olimpica (2/10).",
    Source_Verification="Search Query: Lula COI Copenhague outubro 2009 Rio 2016 eleicao",
    Source_Reliability="High", Methodological_Notes="Eleccion 2/10/2009. Hito. Informe: la salida oficial siguio a Belgica y Suecia (4-6/10), a completar.")

add("BRA-LU-J086", Trip_Status="Completed", Start_Date="2009-12-17", End_Date="2009-12-18", Duration_Days=2,
    Destination_Country="Denmark", Destination_City="Copenhagen", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="COP15 (Conferência do Clima da ONU)",
    Trip_Objective="Segmento de jefes de Estado de la COP15; Brasil actor central de la negociacion climatica.",
    Source_Verification="Search Query: Lula COP15 Copenhague dezembro 2009",
    Source_Reliability="Medium", Methodological_Notes="17-18/12/2009.")

# ===== 2010 =====
add("BRA-LU-J087", Trip_Status="Canceled", Start_Date="2010-01-28", End_Date="NA", Duration_Days="NA",
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Económico Mundial (premio 'Estadista Global')",
    Trip_Objective="Davos 2010: iba a recibir el premio Estadista Global. CANCELADO; el discurso lo leyo el canciller Amorim (29/1). Motivo reportado: lluvias/inundaciones en el Sudeste (fuentes del tramo 2) vs crisis hipertensiva (informe general); a confirmar.",
    Source_Verification="Search Query: Lula cancela Davos janeiro 2010 Amorim discurso",
    Source_Reliability="Medium", Methodological_Notes="Cancelado; sin duracion. DISCREPANCIA de motivo entre fuentes: registrar y verificar.")

add("BRA-LU-J088", Trip_Status="Completed", Start_Date="2010-02-22", End_Date="2010-02-23", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Cancún", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula da Unidade da América Latina e Caribe (criação da CELAC)",
    Trip_Objective="Cumbre de la Unidad ALC en Cancun; acuerdo para crear la CELAC. Siguio a Cuba (23-24/2).",
    Source_Verification="Search Query: Lula cupula unidade America Latina Cancun fevereiro 2010",
    Source_Reliability="High", Methodological_Notes="Gira oficial 21-27/02: Cancun, Cuba, Haiti, El Salvador. Tramos Cuba y El Salvador a completar.")

add("BRA-LU-J088", Trip_Status="Completed", Start_Date="2010-02-25", End_Date="2010-02-25", Duration_Days=1,
    Destination_Country="Haiti", Destination_City="Port-au-Prince", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="René Préval (pós-terremoto)",
    Trip_Objective="Visita a Haiti tras el terremoto del 12/1; Brasil lideraba la MINUSTAH. Tramo de la gira de Cancun.",
    Source_Verification="Search Query: Lula Haiti pos terremoto 25 fevereiro 2010",
    Source_Reliability="Medium", Methodological_Notes="25/02/2010.")

add("BRA-LU-J089", Trip_Status="Completed", Start_Date="2010-03-15", End_Date="2010-03-16", Duration_Days=2,
    Destination_Country="Israel", Destination_City="Jerusalem", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Shimon Peres / Benjamin Netanyahu",
    Trip_Objective="PRIMERA visita de un presidente brasileno a Israel; discurso en la Knesset (15/3). Tramo 1.",
    Source_Verification="Search Query: Lula visita Israel marco 2010 Knesset primeira",
    Source_Reliability="High", Methodological_Notes="Gira Israel-Palestina-Jordania 14-18/03/2010 (llegada 14/3).")

add("BRA-LU-J089", Trip_Status="Completed", Start_Date="2010-03-17", End_Date="2010-03-17", Duration_Days=1,
    Destination_Country="Palestine", Destination_City="Ramallah", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mahmoud Abbas",
    Trip_Objective="Visita a la Autoridad Palestina; tumba de Arafat y 'Rua Brasil'. Tramo 2.",
    Source_Verification="Search Query: Lula Ramallah Abbas marco 2010",
    Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J089", Trip_Status="Completed", Start_Date="2010-03-17", End_Date="2010-03-18", Duration_Days=2,
    Destination_Country="Jordan", Destination_City="Amman", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rei Abdullah II",
    Trip_Objective="Visita a Jordania (Aman y Petra). Tramo 3 (final).",
    Source_Verification="Search Query: Lula Jordania marco 2010",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J090", Trip_Status="Completed", Start_Date="2010-04-12", End_Date="2010-04-13", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula de Segurança Nuclear",
    Trip_Objective="Cumbre de Seguridad Nuclear convocada por Obama; bilateral con Hatoyama.",
    Source_Verification="Search Query: Lula cupula seguranca nuclear Washington abril 2010",
    Source_Reliability="High", Methodological_Notes="12-13/04/2010.")

add("BRA-LU-J091", Trip_Status="Completed", Start_Date="2010-05-13", End_Date="2010-05-14", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Dmitri Medvédev",
    Trip_Objective="Visita a Moscu camino a Teheran; coordinacion sobre el dossier nuclear irani. Tramo 1.",
    Source_Verification="Search Query: Lula Moscou Medvedev maio 2010",
    Source_Reliability="Medium", Methodological_Notes="Gira oficial 12-20/05: Rusia (12-14), Qatar (14-15), Iran (16-17), Espana (17-19), Portugal (19). Tramos Qatar y Portugal a completar.")

add("BRA-LU-J091", Trip_Status="Completed", Start_Date="2010-05-16", End_Date="2010-05-17", Duration_Days=2,
    Destination_Country="Iran", Destination_City="Tehran", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Mahmoud Ahmadinejad / Recep Tayyip Erdoğan (Declaração de Teerã)",
    Trip_Objective="Mediacion nuclear Brasil-Turquia-Iran; firma de la Declaracion de Teheran (17/5) sobre canje de uranio. Hito del mandato. Tramo 2.",
    Source_Verification="Search Query: Lula Declaracao de Teera 17 maio 2010 Erdogan Ahmadinejad",
    Source_Reliability="High", Methodological_Notes="16-17/05/2010.")

add("BRA-LU-J091", Trip_Status="Completed", Start_Date="2010-05-18", End_Date="2010-05-18", Duration_Days=1,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="VI Cúpula UE-América Latina e Caribe / Cúpula Mercosul-UE",
    Trip_Objective="Cumbre UE-ALC en Madrid, directo desde Teheran. Tramo 3 (final).",
    Source_Verification="Search Query: Lula cupula UE America Latina Madri 18 maio 2010",
    Source_Reliability="Medium", Methodological_Notes="17-18/05/2010; asistencia 18/5.")

add("BRA-LU-J092", Trip_Status="Completed", Start_Date="2010-05-25", End_Date="2010-05-25", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Bicentenário da Revolução de Maio (CFK)",
    Trip_Objective="Bicentenario argentino en Buenos Aires, invitado por Cristina Fernandez.",
    Source_Verification="Search Query: Lula Bicentenario Buenos Aires 25 maio 2010",
    Source_Reliability="Medium", Methodological_Notes="25/05/2010.")

add("BRA-LU-J093", Trip_Status="Canceled", Start_Date="2010-06-26", End_Date="NA", Duration_Days="NA",
    Destination_Country="Canada", Destination_City="Toronto", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do G20 de Toronto",
    Trip_Objective="G20 de Toronto (26-27/6). CANCELADO por las inundaciones en Pernambuco y Alagoas (~40 muertos); envio a Mantega. Anuncio de Amorim el 25/6.",
    Source_Verification="Search Query: Lula cancela G20 Toronto junho 2010 enchentes Pernambuco Alagoas Mantega",
    Source_Reliability="High", Methodological_Notes="Cancelado; sin duracion.")

# Gira Africa jul 2010 (1 Journey_ID): Cabo Verde, Guinea Ecuatorial, Kenia, Tanzania, Zambia, Sudafrica
add("BRA-LU-J094", Trip_Status="Completed", Start_Date="2010-07-02", End_Date="2010-07-04", Duration_Days=3,
    Destination_Country="Cape Verde", Destination_City="Sal", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="I Cúpula Brasil-CEDEAO",
    Trip_Objective="Ultima gran gira africana del mandato: I cumbre Brasil-CEDEAO en Isla del Sal. Tramo 1.",
    Source_Verification="Search Query: Lula cupula Brasil CEDEAO Cabo Verde julho 2010",
    Source_Reliability="High", Methodological_Notes="Gira oficial 2-10/07/2010 (Itamaraty Resenha 107): Cabo Verde 2-4, Guinea Ec. 4-5, Kenia 6, Tanzania 6-7, Zambia 7-8, Sudafrica 9-10.")

add("BRA-LU-J094", Trip_Status="Completed", Start_Date="2010-07-04", End_Date="2010-07-05", Duration_Days=2,
    Destination_Country="Equatorial Guinea", Destination_City="Malabo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Teodoro Obiang",
    Trip_Objective="Tramo 2 de la gira africana.",
    Source_Verification="Search Query: Lula Guine Equatorial julho 2010",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J094", Trip_Status="Completed", Start_Date="2010-07-06", End_Date="2010-07-06", Duration_Days=1,
    Destination_Country="Kenya", Destination_City="Nairobi", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mwai Kibaki",
    Trip_Objective="Tramo 3.",
    Source_Verification="Search Query: Lula Quenia Nairobi julho 2010",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J094", Trip_Status="Completed", Start_Date="2010-07-06", End_Date="2010-07-07", Duration_Days=2,
    Destination_Country="Tanzania", Destination_City="Dar es Salaam", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jakaya Kikwete",
    Trip_Objective="Tramo 4.",
    Source_Verification="Search Query: Lula Tanzania julho 2010",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J094", Trip_Status="Completed", Start_Date="2010-07-07", End_Date="2010-07-08", Duration_Days=2,
    Destination_Country="Zambia", Destination_City="Lusaka", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rupiah Banda",
    Trip_Objective="Tramo 5.",
    Source_Verification="Search Query: Lula Zambia julho 2010",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J094", Trip_Status="Completed", Start_Date="2010-07-09", End_Date="2010-07-10", Duration_Days=2,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jacob Zuma (Copa do Mundo)",
    Trip_Objective="Cierre de la gira en Sudafrica durante el Mundial 2010; traspaso simbolico hacia Brasil 2014. Tramo 6 (final).",
    Source_Verification="Search Query: Lula Africa do Sul Copa do Mundo julho 2010",
    Source_Reliability="Medium", Methodological_Notes="9-10/07/2010.")

# Mozambique + G20 Seul nov 2010 — 1 Journey_ID
add("BRA-LU-J095", Trip_Status="Completed", Start_Date="2010-11-09", End_Date="2010-11-10", Duration_Days=2,
    Destination_Country="Mozambique", Destination_City="Maputo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Armando Guebuza (visita de despedida)",
    Trip_Objective="Visita de despedida a Mozambique camino a Seul. Tramo 1.",
    Source_Verification="Search Query: Lula Mocambique novembro 2010 despedida",
    Source_Reliability="Medium", Methodological_Notes="Gira 9-12/11/2010 (Mozambique + Corea).")

add("BRA-LU-J095", Trip_Status="Completed", Start_Date="2010-11-11", End_Date="2010-11-12", Duration_Days=2,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G20 de Seul",
    Trip_Objective="Ultima cumbre del G20 de Lula; guerra cambiaria en agenda. Tramo 2 (final).",
    Source_Verification="Search Query: Lula G20 Seul novembro 2010",
    Source_Reliability="High", Methodological_Notes="11-12/11/2010.")

add("BRA-LU-J096", Trip_Status="Completed", Start_Date="2010-11-25", End_Date="2010-11-26", Duration_Days=2,
    Destination_Country="Guyana", Destination_City="Georgetown", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula da UNASUL",
    Trip_Objective="Cumbre de UNASUR en Georgetown.",
    Source_Verification="Search Query: Lula cupula UNASUL Georgetown Guiana novembro 2010",
    Source_Reliability="Medium", Methodological_Notes="25-26/11/2010.")

add("BRA-LU-J097", Trip_Status="Completed", Start_Date="2010-12-03", End_Date="2010-12-04", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Mar del Plata", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XX Cúpula Ibero-Americana",
    Trip_Objective="Cumbre Iberoamericana de Mar del Plata; ultima gira internacional del mandato (homenaje a Kirchner).",
    Source_Verification="Search Query: Lula Cupula Ibero-Americana Mar del Plata dezembro 2010",
    Source_Reliability="Medium", Methodological_Notes="3-4/12/2010. NO asistio a la 65a AGNU sep-2010 (delego en Amorim) ni consta COP16.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (2do mandato 2007-2010) agregadas. Ultimo Trip_ID = {tid-1}")
