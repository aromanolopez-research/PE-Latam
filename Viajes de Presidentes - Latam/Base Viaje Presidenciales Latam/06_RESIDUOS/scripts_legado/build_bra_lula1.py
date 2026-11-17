# -*- coding: utf-8 -*-
"""
BRASIL — Lula da Silva, PRIMER MANDATO (2003-01-01 a 2007-01-01). TRAMO 1 de 2 (el 2do mandato va aparte).
Continua Trip_ID tras Cardoso (ultimo=26). Journey continua en BRA-LU-J025.
Fuente primaria: Biblioteca da Presidencia da Republica (registro oficial de viajes, fechas exactas
via snippet de busqueda; la pagina bloquea fetch directo) + SEGIB/ONU/prensa.
Lula total 2003-2010: 139 giras / ~250 visitas-pais (dato oficial). Se carga el nucleo verificado
del 1er mandato; brecha documentada EN EL MOMENTO en PENDIENTES_VERIFICACION.txt.
Giras multipais = 1 Journey_ID. Cancelados de 2010 (Davos, G20 Toronto) van en el tramo 2.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Luiz Inácio Lula da Silva"; O = "Brasil"
rows = []; tid = 27

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

BIB = "https://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/viagens/viagens-1"

# ===== 2003 =====
add("BRA-LU-J025", Trip_Status="Completed", Start_Date="2003-01-15", End_Date="2003-01-16", Duration_Days=2,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Lucio Gutiérrez",
    Trip_Objective="Primer viaje del mandato: visita oficial a Ecuador por la asuncion de Lucio Gutierrez.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales Biblioteca da Presidencia (15-16/01/2003).")

# Gira Davos + Alemania + Francia (24-29 ene 2003), 1 Journey_ID
add("BRA-LU-J026", Trip_Status="Completed", Start_Date="2003-01-25", End_Date="2003-01-26", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Davos", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Foro Económico Mundial (WEF)",
    Trip_Objective="Davos tras asumir; llevo la agenda social (venia del Foro Social Mundial de Porto Alegre). Tramo 1.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Gira 24-29/01/2003: Davos (25-26), Alemania (27), Francia (28). Fechas oficiales.")

add("BRA-LU-J026", Trip_Status="Completed", Start_Date="2003-01-27", End_Date="2003-01-27", Duration_Days=1,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Johannes Rau / Gerhard Schröder",
    Trip_Objective="Visita al presidente Rau y reunion de trabajo con el canciller Schroder. Tramo 2.",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J026", Trip_Status="Completed", Start_Date="2003-01-28", End_Date="2003-01-28", Duration_Days=1,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jacques Chirac / Jean-Pierre Raffarin",
    Trip_Objective="Reunion con Chirac y Raffarin. Tramo 3 (final).",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J027", Trip_Status="Completed", Start_Date="2003-05-22", End_Date="2003-05-24", Duration_Days=3,
    Destination_Country="Peru", Destination_City="Cusco", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XVII Cúpula do Grupo do Rio",
    Trip_Objective="Cumbre del Grupo de Rio en Cusco; concertacion politica regional.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (22-24/05/2003).")

add("BRA-LU-J028", Trip_Status="Completed", Start_Date="2003-06-01", End_Date="2003-06-03", Duration_Days=3,
    Destination_Country="France", Destination_City="Évian-les-Bains", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G8 ampliada (Evian, convidado)",
    Trip_Objective="Invitado al dialogo ampliado del G8 en Evian; debut de Lula en el foro de las potencias.",
    Source_Verification="Search Query: Lula G8 Evian junho 2003 convidado",
    Source_Reliability="Medium", Methodological_Notes="G8 Evian 1-3 jun 2003; segmento ampliado 1/06 (estimado).")

add("BRA-LU-J029", Trip_Status="Completed", Start_Date="2003-06-20", End_Date="2003-06-20", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="George W. Bush",
    Trip_Objective="Primera visita de Lula a Bush en la Casa Blanca; comercio, ALCA y agenda social.",
    Source_Verification="Search Query: Lula Bush Casa Branca 20 junho 2003",
    Source_Reliability="Medium", Methodological_Notes="Reunion 20/06/2003.")

add("BRA-LU-J030", Trip_Status="Completed", Start_Date="2003-09-23", End_Date="2003-09-23", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="58ª Assembleia Geral da ONU",
    Trip_Objective="Discurso de apertura de la 58a AGNU (Brasil abre por tradicion); hambre y pobreza como agenda global. Bilateral con Putin.",
    Source_Verification="Search Query: Lula abertura 58 Assembleia Geral ONU setembro 2003",
    Source_Reliability="High", Methodological_Notes="Foto oficial con Putin en la AGNU 2003 (lista oficial).")

add("BRA-LU-J031", Trip_Status="Completed", Start_Date="2003-09-26", End_Date="2003-09-27", Duration_Days=2,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Fidel Castro",
    Trip_Objective="Visita oficial a Cuba; revista a las tropas con Fidel (foto oficial). Cooperacion y comercio.",
    Source_Verification="Search Query: Lula visita oficial Cuba Fidel setembro 2003",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas (fines sep 2003, tras AGNU).")

# Gira Africa nov 2003 (1 Journey_ID, 5 paises): Sao Tome, Angola, Mozambique, Namibia, Sudafrica
add("BRA-LU-J032", Trip_Status="Completed", Start_Date="2003-11-02", End_Date="2003-11-02", Duration_Days=1,
    Destination_Country="Sao Tome and Principe", Destination_City="São Tomé", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Fradique de Menezes",
    Trip_Objective="Primera gira africana del mandato; cooperacion lusofona (CPLP). Tramo 1.",
    Source_Verification="Search Query: Lula primeira viagem Africa novembro 2003 Sao Tome Angola Mocambique Namibia Africa do Sul",
    Source_Reliability="Medium", Methodological_Notes="Gira 1-8 nov 2003 (5 paises); fechas de dia estimadas.")

add("BRA-LU-J032", Trip_Status="Completed", Start_Date="2003-11-03", End_Date="2003-11-03", Duration_Days=1,
    Destination_Country="Angola", Destination_City="Luanda", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="José Eduardo dos Santos",
    Trip_Objective="Cooperacion, reconstruccion posguerra, comercio. Tramo 2.",
    Source_Verification="Search Query: Lula Angola novembro 2003",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J032", Trip_Status="Completed", Start_Date="2003-11-04", End_Date="2003-11-05", Duration_Days=2,
    Destination_Country="Mozambique", Destination_City="Maputo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Joaquim Chissano",
    Trip_Objective="Cooperacion lusofona; anuncio de fabrica de antirretrovirales. Tramo 3.",
    Source_Verification="Search Query: Lula Mocambique novembro 2003 antirretrovirais",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J032", Trip_Status="Completed", Start_Date="2003-11-06", End_Date="2003-11-06", Duration_Days=1,
    Destination_Country="Namibia", Destination_City="Windhoek", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Sam Nujoma",
    Trip_Objective="Cooperacion bilateral. Tramo 4.",
    Source_Verification="Search Query: Lula Namibia novembro 2003",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J032", Trip_Status="Completed", Start_Date="2003-11-07", End_Date="2003-11-08", Duration_Days=2,
    Destination_Country="South Africa", Destination_City="Pretoria", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Thabo Mbeki",
    Trip_Objective="Eje IBSA (India-Brasil-Sudafrica); comercio Sur-Sur. Tramo 5 (final).",
    Source_Verification="Search Query: Lula Africa do Sul Mbeki novembro 2003 IBSA",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J033", Trip_Status="Completed", Start_Date="2003-11-14", End_Date="2003-11-15", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Santa Cruz de la Sierra", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XIII Cúpula Ibero-Americana",
    Trip_Objective="Cumbre Iberoamericana 'inclusion social'.",
    Source_Verification="https://segib.org/?summit=xiii-cumbre-iberoamericana-santa-cruz-de-la-sierra-2003",
    Source_Reliability="High", Methodological_Notes="NA")

# Gira Medio Oriente dic 2003 (1 Journey_ID, 5 paises): Siria, Libano, EAU, Egipto, Libia
add("BRA-LU-J034", Trip_Status="Completed", Start_Date="2003-12-03", End_Date="2003-12-04", Duration_Days=2,
    Destination_Country="Syria", Destination_City="Damascus", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Bashar al-Assad",
    Trip_Objective="Primera gira de un presidente brasileno por el mundo arabe en decadas; semilla de la cumbre ASPA. Tramo 1.",
    Source_Verification="Search Query: Lula viagem Oriente Medio dezembro 2003 Siria Libano Emirados Egito Libia",
    Source_Reliability="Medium", Methodological_Notes="Gira 3-11 dic 2003 (5 paises); fechas de dia estimadas.")

add("BRA-LU-J034", Trip_Status="Completed", Start_Date="2003-12-05", End_Date="2003-12-05", Duration_Days=1,
    Destination_Country="Lebanon", Destination_City="Beirut", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Émile Lahoud",
    Trip_Objective="Vinculo con la diaspora libanesa en Brasil (la mayor del mundo). Tramo 2.",
    Source_Verification="Search Query: Lula Libano dezembro 2003",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J034", Trip_Status="Completed", Start_Date="2003-12-07", End_Date="2003-12-07", Duration_Days=1,
    Destination_Country="United Arab Emirates", Destination_City="Dubai", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Governo dos EAU",
    Trip_Objective="Comercio e inversiones. Tramo 3.",
    Source_Verification="Search Query: Lula Emirados Arabes dezembro 2003",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J034", Trip_Status="Completed", Start_Date="2003-12-08", End_Date="2003-12-09", Duration_Days=2,
    Destination_Country="Egypt", Destination_City="Cairo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hosni Mubarak",
    Trip_Objective="Comercio; acuerdo marco Mercosur-Egipto en agenda. Tramo 4.",
    Source_Verification="Search Query: Lula Egito Mubarak dezembro 2003",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J034", Trip_Status="Completed", Start_Date="2003-12-10", End_Date="2003-12-11", Duration_Days=2,
    Destination_Country="Libya", Destination_City="Tripoli", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Muammar Gadafi",
    Trip_Objective="Comercio y cooperacion. Tramo 5 (final).",
    Source_Verification="Search Query: Lula Libia Kadafi dezembro 2003",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J035", Trip_Status="Completed", Start_Date="2003-12-15", End_Date="2003-12-16", Duration_Days=2,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do MERCOSUL",
    Trip_Objective="Cumbre de jefes de Estado del Mercosur, Bolivia y Chile.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (15-16/12/2003).")

# ===== 2004 =====
add("BRA-LU-J036", Trip_Status="Completed", Start_Date="2004-01-11", End_Date="2004-01-14", Duration_Days=4,
    Destination_Country="Mexico", Destination_City="Monterrey", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula Extraordinária das Américas",
    Trip_Objective="Cumbre extraordinaria de las Americas en Monterrey.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (11-14/01/2004).")

# Gira India + Suiza (24-31 ene 2004), 1 Journey_ID
add("BRA-LU-J037", Trip_Status="Completed", Start_Date="2004-01-24", End_Date="2004-01-28", Duration_Days=5,
    Destination_Country="India", Destination_City="New Delhi", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="A.P.J. Abdul Kalam (convidado de honra do Dia da República)",
    Trip_Objective="Visita de Estado a India; invitado de honor del Dia de la Republica (26/1); eje IBSA y G20 comercial. Tramo 1.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Gira 24-31/01/2004; India visita de Estado 26/1.")

add("BRA-LU-J037", Trip_Status="Completed", Start_Date="2004-01-29", End_Date="2004-01-30", Duration_Days=2,
    Destination_Country="Switzerland", Destination_City="Geneva", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Seminário de investimentos + reunião com Chirac e Kofi Annan",
    Trip_Objective="Seminario sobre inversiones en Brasil (29/1); reunion con Chirac y Annan sobre la accion contra el hambre (30/1). Tramo 2.",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J038", Trip_Status="Completed", Start_Date="2004-02-26", End_Date="2004-02-28", Duration_Days=3,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XII Cúpula do G-15",
    Trip_Objective="Cumbre del G-15 en Caracas; cooperacion Sur-Sur.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (26-28/02/2004).")

# Gira China + Mexico (21-29 may 2004), 1 Journey_ID
add("BRA-LU-J039", Trip_Status="Completed", Start_Date="2004-05-21", End_Date="2004-05-27", Duration_Days=7,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hu Jintao",
    Trip_Objective="Visita de Estado a China con gran comitiva empresarial; alianza estrategica y comercio. Tramo 1.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Gira 21-29/05/2004; China 21-27/5.")

add("BRA-LU-J039", Trip_Status="Completed", Start_Date="2004-05-28", End_Date="2004-05-29", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Guadalajara", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="III Cúpula América Latina e Caribe - União Europeia",
    Trip_Objective="Cumbre ALC-UE en Guadalajara. Tramo 2 (final).",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J040", Trip_Status="Completed", Start_Date="2004-06-22", End_Date="2004-06-24", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do Global Compact + investidores",
    Trip_Objective="Encuentro de alto nivel con inversores y cumbre de lideres del Global Compact de la ONU.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (22-24/06/2004).")

# Gira Africa jul 2004 (1 Journey_ID): Sao Tome, Gabon, Cabo Verde
add("BRA-LU-J041", Trip_Status="Completed", Start_Date="2004-07-23", End_Date="2004-07-24", Duration_Days=2,
    Destination_Country="Sao Tome and Principe", Destination_City="São Tomé", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula da CPLP",
    Trip_Objective="Segunda gira africana: cumbre de la CPLP en Sao Tome. Tramo 1.",
    Source_Verification="Search Query: Lula Africa julho 2004 Sao Tome Gabao Cabo Verde CPLP",
    Source_Reliability="Medium", Methodological_Notes="Gira jul 2004; fechas de dia estimadas.")

add("BRA-LU-J041", Trip_Status="Completed", Start_Date="2004-07-26", End_Date="2004-07-26", Duration_Days=1,
    Destination_Country="Gabon", Destination_City="Libreville", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Omar Bongo",
    Trip_Objective="Cooperacion bilateral. Tramo 2.",
    Source_Verification="Search Query: Lula Gabao julho 2004",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J041", Trip_Status="Completed", Start_Date="2004-07-28", End_Date="2004-07-29", Duration_Days=2,
    Destination_Country="Cape Verde", Destination_City="Praia", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Pedro Pires",
    Trip_Objective="Cooperacion lusofona. Tramo 3 (final).",
    Source_Verification="Search Query: Lula Cabo Verde julho 2004",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J042", Trip_Status="Completed", Start_Date="2004-09-20", End_Date="2004-09-21", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="59ª AGNU + Cúpula da Ação contra a Fome e a Pobreza",
    Trip_Objective="Liderazgo de la Accion contra el Hambre (con Chirac, Zapatero, Lagos y Annan, 20/9) y apertura de la 59a AGNU (21/9).",
    Source_Verification="Search Query: Lula Acao contra Fome ONU setembro 2004 Chirac Zapatero",
    Source_Reliability="High", Methodological_Notes="Cumbre contra el hambre 20/09/2004.")

add("BRA-LU-J043", Trip_Status="Completed", Start_Date="2004-11-18", End_Date="2004-11-20", Duration_Days=3,
    Destination_Country="Costa Rica", Destination_City="San José", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XIV Cúpula Ibero-Americana",
    Trip_Objective="Cumbre Iberoamericana 'educar para progresar'.",
    Source_Verification="https://segib.org/?summit=xiv-cumbre-iberoamericana-san-jose-2004",
    Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J044", Trip_Status="Completed", Start_Date="2004-12-07", End_Date="2004-12-09", Duration_Days=3,
    Destination_Country="Peru", Destination_City="Cusco", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="III Cúpula Sul-Americana (criação da CASA/CSN)",
    Trip_Objective="Creacion de la Comunidad Sudamericana de Naciones (Declaracion de Cusco, 8/12); semilla de UNASUR.",
    Source_Verification="Search Query: Lula Cusco dezembro 2004 Comunidade Sul-Americana",
    Source_Reliability="High", Methodological_Notes="Declaracion de Cusco 8/12/2004.")

# ===== 2005 =====
add("BRA-LU-J045", Trip_Status="Completed", Start_Date="2005-03-01", End_Date="2005-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Posse de Tabaré Vázquez",
    Trip_Objective="Asuncion de Tabare Vazquez (primer gobierno de izquierda en Uruguay).",
    Source_Verification="Search Query: Lula posse Tabare Vazquez Montevideu 1 marco 2005",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J046", Trip_Status="Completed", Start_Date="2005-05-24", End_Date="2005-05-26", Duration_Days=3,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Roh Moo-hyun",
    Trip_Objective="Visita de Estado a Corea del Sur; desfile en auto abierto en Seul (24/5, foto oficial). Comercio y tecnologia.",
    Source_Verification="Search Query: Lula Coreia do Sul Roh Moo-hyun maio 2005",
    Source_Reliability="Medium", Methodological_Notes="Llegada 24/05/2005 (lista oficial); fin estimado. Verificar tramo Japon.")

# Mega-gira oct 2005: Portugal + Espana + Italia + Rusia (12-19 oct), 1 Journey_ID — fechas oficiales
add("BRA-LU-J047", Trip_Status="Completed", Start_Date="2005-10-13", End_Date="2005-10-13", Duration_Days=1,
    Destination_Country="Portugal", Destination_City="Porto", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="VII Cimeira Brasil-Portugal",
    Trip_Objective="VII Cumbre bilateral Brasil-Portugal en Porto. Tramo 1 de mega-gira europea.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Gira oficial 12-19/10/2005: Porto (13), Salamanca (14-15), Roma (16-17), Moscu (17-18).")

add("BRA-LU-J047", Trip_Status="Completed", Start_Date="2005-10-14", End_Date="2005-10-15", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Salamanca", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XV Cúpula Ibero-Americana",
    Trip_Objective="Cumbre Iberoamericana de Salamanca. Tramo 2.",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J047", Trip_Status="Completed", Start_Date="2005-10-16", End_Date="2005-10-17", Duration_Days=2,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Visita oficial à Itália",
    Trip_Objective="Visita oficial en Roma. Tramo 3.",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J047", Trip_Status="Completed", Start_Date="2005-10-17", End_Date="2005-10-18", Duration_Days=2,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Vladímir Putin",
    Trip_Objective="Visita oficial a Rusia; alianza estrategica y tecnologia. Tramo 4 (final).",
    Source_Verification=BIB, Source_Reliability="High", Methodological_Notes="NA")

add("BRA-LU-J048", Trip_Status="Completed", Start_Date="2005-11-04", End_Date="2005-11-05", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Mar del Plata", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IV Cúpula das Américas",
    Trip_Objective="IV Cumbre de las Americas; con Kirchner y Chavez enterro el ALCA tal como lo proponia EE.UU.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (4-5/11/2005).")

add("BRA-LU-J049", Trip_Status="Completed", Start_Date="2005-11-30", End_Date="2005-11-30", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Puerto Iguazú", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Néstor Kirchner (20 anos dos acordos de Foz do Iguaçu)",
    Trip_Objective="Encuentro con Kirchner por los 20 anos de los acuerdos de Foz de Iguazu (cooperacion nuclear).",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fecha oficial (30/11/2005).")

add("BRA-LU-J050", Trip_Status="Completed", Start_Date="2005-12-08", End_Date="2005-12-09", Duration_Days=2,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do MERCOSUL",
    Trip_Objective="Cumbre de jefes de Estado del Mercosur y asociados.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (8-9/12/2005).")

add("BRA-LU-J051", Trip_Status="Completed", Start_Date="2005-12-13", End_Date="2005-12-15", Duration_Days=3,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Álvaro Uribe",
    Trip_Objective="Visita de Estado a Colombia.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fechas oficiales (13-15/12/2005).")

# ===== 2006 (año electoral, agenda reducida) =====
add("BRA-LU-J052", Trip_Status="Completed", Start_Date="2006-01-22", End_Date="2006-01-22", Duration_Days=1,
    Destination_Country="Bolivia", Destination_City="La Paz", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Posse de Evo Morales",
    Trip_Objective="Asuncion de Evo Morales.",
    Source_Verification=BIB, Source_Reliability="High",
    Methodological_Notes="Fecha oficial (22/01/2006).")

add("BRA-LU-J053", Trip_Status="Completed", Start_Date="2006-05-11", End_Date="2006-05-13", Duration_Days=3,
    Destination_Country="Austria", Destination_City="Vienna", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IV Cúpula ALC-União Europeia (Viena)",
    Trip_Objective="Cumbre ALC-UE en Viena; tension regional por la nacionalizacion del gas boliviano (reunion con Evo y Kirchner).",
    Source_Verification="Search Query: Lula Cupula Viena ALC UE maio 2006 gas Bolivia",
    Source_Reliability="Medium", Methodological_Notes="Cumbre 11-13/05/2006.")

add("BRA-LU-J054", Trip_Status="Completed", Start_Date="2006-07-15", End_Date="2006-07-17", Duration_Days=3,
    Destination_Country="Russia", Destination_City="Saint Petersburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula do G8 ampliada (convidado)",
    Trip_Objective="Invitado al segmento ampliado del G8 de San Petersburgo.",
    Source_Verification="Search Query: Lula G8 Sao Petersburgo julho 2006 convidado",
    Source_Reliability="Medium", Methodological_Notes="G8 15-17/07/2006.")

add("BRA-LU-J055", Trip_Status="Completed", Start_Date="2006-09-19", End_Date="2006-09-19", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="61ª AGNU",
    Trip_Objective="Apertura de la 61a Asamblea General de la ONU.",
    Source_Verification="Search Query: Lula abertura 61 Assembleia Geral ONU setembro 2006",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-LU-J056", Trip_Status="Completed", Start_Date="2006-11-03", End_Date="2006-11-05", Duration_Days=3,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XVI Cúpula Ibero-Americana",
    Trip_Objective="Cumbre Iberoamericana de Montevideo (post-reeleccion).",
    Source_Verification="https://segib.org/?summit=xvi-cumbre-iberoamericana-montevideo-2006",
    Source_Reliability="Medium", Methodological_Notes="Verificar asistencia exacta (3-5/11/2006).")

add("BRA-LU-J057", Trip_Status="Completed", Start_Date="2006-11-30", End_Date="2006-11-30", Duration_Days=1,
    Destination_Country="Nigeria", Destination_City="Abuja", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="I Cúpula África-América do Sul (ASA)",
    Trip_Objective="Primera cumbre Africa-Sudamerica (ASA) en Abuja, iniciativa Brasil-Nigeria.",
    Source_Verification="Search Query: Lula Cupula Africa America do Sul Abuja novembro 2006",
    Source_Reliability="Medium", Methodological_Notes="ASA I: 30/11/2006.")

add("BRA-LU-J058", Trip_Status="Completed", Start_Date="2006-12-08", End_Date="2006-12-09", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Cochabamba", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="II Cúpula da Comunidade Sul-Americana de Nações",
    Trip_Objective="Cumbre de la CSN en Cochabamba; camino a UNASUR.",
    Source_Verification="Search Query: Lula Cupula Comunidade Sul-Americana Cochabamba dezembro 2006",
    Source_Reliability="Medium", Methodological_Notes="8-9/12/2006.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (1er mandato 2003-2006) agregadas. Ultimo Trip_ID = {tid-1}")
