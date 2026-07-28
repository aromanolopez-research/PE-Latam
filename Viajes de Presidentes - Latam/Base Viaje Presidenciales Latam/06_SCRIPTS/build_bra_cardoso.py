# -*- coding: utf-8 -*-
"""
BRASIL — primer modulo. Fernando Henrique Cardoso (FHC), 2do mandato, VENTANA 2000-01-01 a 2003-01-01.
FHC gobernó 1995-2003; SOLO se cargan viajes desde 2000-01-01. Su viaje nº99 total fue en dic 2002 (BBC);
en la ventana 2000-2002 entran del ~nº60 al ~nº99 aprox. Se cargan los VERIFICADOS con fuente primaria/prensa.
Fuente primaria: Biblioteca da Presidência da República + Itamaraty (via referencias de la lista oficial de viajes).
Journey_ID: BRA-FHC-Jnnn. Trip_ID arranca en 1 (modulo nuevo; integrate.py renumera global al consolidar).
Registro de pendientes EN EL MOMENTO (metodo mejorado): ver PENDIENTES_VERIFICACION.txt seccion Brasil.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "brasil", "brasil_viajes.csv")
P = "Fernando Henrique Cardoso"; O = "Brasil"
rows = []; tid = 1

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2000 =====
add("BRA-FHC-J001", Trip_Status="Completed", Start_Date="2000-03-07", End_Date="2000-03-08", Duration_Days=2,
    Destination_Country="Portugal", Destination_City="Lisbon", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jorge Sampaio / Cúpula (avião fretado)",
    Trip_Objective="Visita a Portugal; relaciones bilaterales y comerciales. Condecoracion Ordem do Infante D. Henrique (07/03).",
    Source_Verification="Search Query: FHC viagem Portugal março 2000 Folha aviao fretado",
    Source_Reliability="Medium", Methodological_Notes="Ordem do Infante 07/03/2000 (ABL). Fechas de dia estimadas.")

add("BRA-FHC-J002", Trip_Status="Completed", Start_Date="2000-03-11", End_Date="2000-03-11", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Ricardo Lagos",
    Trip_Objective="Asuncion de Ricardo Lagos como presidente de Chile.",
    Source_Verification="https://www1.folha.uol.com.br/fol/pol/ult10032000028.htm",
    Source_Reliability="High", Methodological_Notes="Folha 10/03/2000; posse 11/03.")

add("BRA-FHC-J003", Trip_Status="Completed", Start_Date="2000-03-29", End_Date="2000-03-30", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hugo Chávez",
    Trip_Objective="Visita a Venezuela; integracion sudamericana y energia. Condecoracion Orden Francisco de Miranda (29/03).",
    Source_Verification="Search Query: FHC visita Venezuela Chavez março 2000 Itamaraty",
    Source_Reliability="Medium", Methodological_Notes="Fecha por condecoracion (ABL, 29/03/2000).")

add("BRA-FHC-J004", Trip_Status="Completed", Start_Date="2000-06-15", End_Date="2000-06-17", Duration_Days=3,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do Grupo do Rio (Cartagena)",
    Trip_Objective="Cumbre del Grupo de Rio en Cartagena. FHC 'dançou porro' en la fiesta de la cumbre (Folha 17/06).",
    Source_Verification="https://www1.folha.uol.com.br/fsp/brasil/fc1706200010.htm",
    Source_Reliability="High", Methodological_Notes="Folha 17/06/2000.")

add("BRA-FHC-J005", Trip_Status="Completed", Start_Date="2000-05-31", End_Date="2000-06-02", Duration_Days=3,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cúpula da Governança Progressiva (Terceira Via)",
    Trip_Objective="Cumbre progresista (Terceira Via) con Schroder, Jospin, Blair; desempleo. FHC-Jospin (Folha 05/06).",
    Source_Verification="https://www1.folha.uol.com.br/fsp/brasil/fc0506200006.htm",
    Source_Reliability="Medium", Methodological_Notes="FHC viajo a Alemania (DGABC 30/05); tema desempleo con Jospin.")

add("BRA-FHC-J006", Trip_Status="Completed", Start_Date="2000-09-06", End_Date="2000-09-08", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula do Milênio da ONU",
    Trip_Objective="Cumbre del Milenio de la ONU (mayor reunion de jefes de Estado hasta entonces).",
    Source_Verification="https://www.un.org/en/conferences/environment/newyork2000",
    Source_Reliability="High", Methodological_Notes="Fechas oficiales de la Cumbre del Milenio (6-8 sep 2000).")

add("BRA-FHC-J007", Trip_Status="Completed", Start_Date="2000-10-02", End_Date="2000-10-05", Duration_Days=4,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Busca de investimentos europeus",
    Trip_Objective="Gira europea en busca de inversiones (Folha 03/10/2000).",
    Source_Verification="https://www1.folha.uol.com.br/fsp/brasil/fc0310200007.htm",
    Source_Reliability="Medium", Methodological_Notes="Destino/ciudad exacta a confirmar; 'investimentos europeus'.")

add("BRA-FHC-J008", Trip_Status="Completed", Start_Date="2000-11-30", End_Date="2000-12-01", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Vicente Fox",
    Trip_Objective="Asuncion de Vicente Fox como presidente de Mexico (fin de 71 anios del PRI).",
    Source_Verification="https://www1.folha.uol.com.br/folha/mundo/ult94u13800.shtml",
    Source_Reliability="High", Methodological_Notes="Folha 29/11/2000; posse 01/12.")

# ===== 2001 =====
add("BRA-FHC-J009", Trip_Status="Completed", Start_Date="2001-01-19", End_Date="2001-01-21", Duration_Days=3,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Kim Dae-jung",
    Trip_Objective="Visita de Estado a Corea del Sur; FHC 'pregou reconciliacao entre coreanos' (Folha 20/01).",
    Source_Verification="https://www1.folha.uol.com.br/fsp/brasil/fc2001200109.htm",
    Source_Reliability="Medium", Methodological_Notes="Posible tramo de gira asiatica; verificar otros destinos.")

add("BRA-FHC-J010", Trip_Status="Completed", Start_Date="2001-03-29", End_Date="2001-03-31", Duration_Days=3,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="George W. Bush",
    Trip_Objective="Primera reunion con Bush; ALCA y comercio. Planalto divulgo agenda (Folha 27/03).",
    Source_Verification="https://www1.folha.uol.com.br/folha/brasil/ult96u17636.shtml",
    Source_Reliability="Medium", Methodological_Notes="Fechas de dia estimadas.")

add("BRA-FHC-J011", Trip_Status="Completed", Start_Date="2001-04-20", End_Date="2001-04-22", Duration_Days=3,
    Destination_Country="Canada", Destination_City="Quebec City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="III Cúpula das Américas (Quebec)",
    Trip_Objective="III Cumbre de las Americas; negociacion del ALCA (Brasil con estrategia obstruccionista).",
    Source_Verification="https://summit-americas.org/sas/Cumbres_previas_IIICumbre.html",
    Source_Reliability="High", Methodological_Notes="Fechas oficiales OEA (20-22 abr 2001).")

# NOTA: en mayo 2001, por la crisis energética (apagão), FHC canceló viajes al exterior
# ('Refém do apagão, FHC cancela viagens', Folha 29/05/2001). No se registra como fila porque
# las fuentes no especifican un destino concreto (una fila necesita país/región válidos).
# Queda documentado en PENDIENTES_VERIFICACION.txt y bitácora.

add("BRA-FHC-J013", Trip_Status="Completed", Start_Date="2001-07-28", End_Date="2001-07-29", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Posse de Alejandro Toledo",
    Trip_Objective="Asuncion de Alejandro Toledo como presidente de Peru (Folha 26/07).",
    Source_Verification="https://www1.folha.uol.com.br/folha/brasil/ult96u22800.shtml",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-FHC-J014", Trip_Status="Completed", Start_Date="2001-08-12", End_Date="2001-08-13", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Hugo Chávez / Fidel Castro",
    Trip_Objective="Inauguracion de interconexion electrica Brasil-Venezuela; encuentro con Chavez y Fidel (Estado/Folha 12-13/08).",
    Source_Verification="https://www1.folha.uol.com.br/fsp/brasil/fc1308200120.htm",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-FHC-J015", Trip_Status="Completed", Start_Date="2001-09-27", End_Date="2001-09-28", Duration_Days=2,
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gustavo Noboa",
    Trip_Objective="Visita oficial a Ecuador (Folha 13/09 anuncio 'final do mes').",
    Source_Verification="https://www1.folha.uol.com.br/folha/brasil/ult96u24678.shtml",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada (fin de septiembre 2001).")

# Gira Espana + Francia oct 2001 (1 Journey_ID)
add("BRA-FHC-J016", Trip_Status="Completed", Start_Date="2001-10-25", End_Date="2001-10-27", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="José María Aznar",
    Trip_Objective="Viaje a Espana y Francia (Estado 25/10). Tramo 1: Espana.",
    Source_Verification="Search Query: FHC viagem Espanha Franca outubro 2001 Estadao",
    Source_Reliability="Medium", Methodological_Notes="Gira Espana-Francia oct 2001.")

add("BRA-FHC-J016", Trip_Status="Completed", Start_Date="2001-10-27", End_Date="2001-10-29", Duration_Days=3,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jacques Chirac",
    Trip_Objective="Tramo 2 de la gira: Francia.",
    Source_Verification="Search Query: FHC viagem Espanha Franca outubro 2001 Estadao",
    Source_Reliability="Low", Methodological_Notes="Fechas de dia estimadas.")

add("BRA-FHC-J017", Trip_Status="Completed", Start_Date="2001-11-08", End_Date="2001-11-09", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington D.C.", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="George W. Bush",
    Trip_Objective="Reunion con Bush; discutieron Argentina y ONU. Post-11S (Estado 08/11).",
    Source_Verification="https://politica.estadao.com.br/noticias/geral,fhc-e-bush-discutiram-argentina-e-onu,20011108p40917",
    Source_Reliability="Medium", Methodological_Notes="FHC tambien 'cobrou na ONU ordem mais solidaria' (Folha 10/11): posible tramo NY.")

# ===== 2002 =====
add("BRA-FHC-J018", Trip_Status="Completed", Start_Date="2002-01-13", End_Date="2002-01-15", Duration_Days=3,
    Destination_Country="Russia", Destination_City="Moscow", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Vladímir Putin",
    Trip_Objective="Visita de Estado a Rusia; 'FHC embarca para a Russia em sua 85a viagem ao exterior' (Estado 11/01).",
    Source_Verification="https://politica.estadao.com.br/noticias/geral,fhc-embarca-para-a-russia-em-sua-85-viagem-ao-exterior,20020111p54670",
    Source_Reliability="High", Methodological_Notes="Dato ancla: era su viaje nº85 al exterior (ene 2002).")

# Gira Europa fev 2002 (Suecia, Polonia, Eslovaquia) — 1 Journey_ID
add("BRA-FHC-J019", Trip_Status="Completed", Start_Date="2002-02-20", End_Date="2002-02-21", Duration_Days=2,
    Destination_Country="Sweden", Destination_City="Stockholm", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Comércio e 'terceira via'",
    Trip_Objective="FHC 'discute comercio e terceira via na Suecia' (21/02). Tramo 1 de gira europea.",
    Source_Verification="http://www.lourivalsantanna.com/paises/europa/suecia/fhc-discute-comercio-e-terceira-via-na-suecia/",
    Source_Reliability="Medium", Methodological_Notes="Gira Suecia-Polonia-Eslovaquia feb 2002.")

add("BRA-FHC-J019", Trip_Status="Completed", Start_Date="2002-02-25", End_Date="2002-02-25", Duration_Days=1,
    Destination_Country="Poland", Destination_City="Warsaw", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Relação econômica com a Polônia",
    Trip_Objective="FHC 'quer relacao economica estreita com a Polonia' (BBC 25/02). Tramo 2.",
    Source_Verification="https://www.bbc.com/portuguese/economia/020225_fhcag1.shtml",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-FHC-J019", Trip_Status="Completed", Start_Date="2002-02-26", End_Date="2002-02-26", Duration_Days=1,
    Destination_Country="Slovakia", Destination_City="Bratislava", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Visita à Eslováquia",
    Trip_Objective="Presidente brasileno en Bratislava (BBC 26/02). Tramo 3 (final).",
    Source_Verification="https://www.bbc.com/portuguese/noticias/2002/020226_brtislava.shtml",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("BRA-FHC-J020", Trip_Status="Completed", Start_Date="2002-03-17", End_Date="2002-03-20", Duration_Days=4,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Ricardo Lagos",
    Trip_Objective="Visita oficial a Chile (Itamaraty: 17-20 mar 2002).",
    Source_Verification="https://web.archive.org/web/20150112210145/http://kitplone.itamaraty.gov.br/sala-de-imprensa/notas-a-imprensa/2002/03/05/viagem-do-presidente-fernando-henrique-cardoso-ao",
    Source_Reliability="High", Methodological_Notes="Itamaraty (Wayback). Fechas oficiales 17-20/03/2002.")

add("BRA-FHC-J021", Trip_Status="Completed", Start_Date="2002-03-21", End_Date="2002-03-22", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Monterrey", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Conferência da ONU sobre Financiamento para o Desenvolvimento",
    Trip_Objective="Conferencia de Monterrey (Consenso de Monterrey) sobre financiamiento al desarrollo.",
    Source_Verification="https://www.un.org/es/conf/ffd/2002/",
    Source_Reliability="Medium", Methodological_Notes="Segmento de jefes de Estado 21-22 mar (estimado).")

add("BRA-FHC-J022", Trip_Status="Completed", Start_Date="2002-08-31", End_Date="2002-09-02", Duration_Days=3,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cúpula Mundial sobre Desenvolvimento Sustentável (Rio+10)",
    Trip_Objective="Cumbre Mundial de Desarrollo Sostenible (Rio+10). La cumbre fue 26 ago-4 sep 2002.",
    Source_Verification="https://pt.wikipedia.org/wiki/Rio%2B10",
    Source_Reliability="Medium", Methodological_Notes="Segmento de alto nivel de jefes de Estado (fin ago-inicio sep); dias exactos de FHC estimados.")

add("BRA-FHC-J023", Trip_Status="Completed", Start_Date="2002-11-11", End_Date="2002-11-12", Duration_Days=2,
    Destination_Country="Portugal", Destination_City="Lisbon", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Visita a Lisboa (sem compromissos oficiais)",
    Trip_Objective="FHC 'chega a Lisboa sem compromissos oficiais' (Agencia Brasil 10/11). Ultima gira internacional como jefe de Estado.",
    Source_Verification="http://memoria.ebc.com.br/agenciabrasil/node/573336",
    Source_Reliability="Medium", Methodological_Notes="'FHC faz ultima viagem como chefe de Estado' (DGABC 09/11/2002).")

add("BRA-FHC-J024", Trip_Status="Completed", Start_Date="2002-12-08", End_Date="2002-12-10", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Prêmio em Nova York",
    Trip_Objective="Viaje a NY a recibir un premio; fue su 99a viagem al exterior (BBC 08/12/2002).",
    Source_Verification="http://www.bbc.co.uk/portuguese/noticias/2002/021208_fhcebc.shtml",
    Source_Reliability="Medium", Methodological_Notes="Dato ancla: 99a y ultima viagem al exterior de FHC. Ciudad exacta a confirmar (NY probable).")

os.makedirs(os.path.dirname(CSV), exist_ok=True)
with open(CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} escritas. Journeys: {len(set(r['Journey_ID'] for r in rows))}")
