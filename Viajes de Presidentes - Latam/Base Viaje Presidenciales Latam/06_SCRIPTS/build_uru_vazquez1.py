# -*- coding: utf-8 -*-
"""
URUGUAY — Tabare Vazquez, PRIMER mandato (Frente Amplio, 2005-03-01 a 2010-03-01). Segundo bloque uruguayo.
Investigacion dedicada (modo investigador, 2026-07-08): 24 giras (Journey_ID), 31 filas pais (Trip_ID 24-54).
Cierra la brecha previa (8 confirmados -> 24 giras) por el extremo alto.
Fuentes: venias art.170 (parlamento.gub.uy, 2 recuperadas), Memorias del MRREE (archivo.presidencia MEM_2007/2008/2009),
SEGIB, Summit-Americas, embajadas, prensa. El conflicto de las pasteras/Botnia reorienta la politica exterior
hacia EEUU (Bush may-2006) y diversificacion a Asia/Medio Oriente.
Trip_ID arranca en 24 (Batlle ocupo 1-23). Convencion: URU-TV1-JXXX.
Anexa al CSV existente del modulo uruguay.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "uruguay", "uruguay_viajes.csv")
P = "Tabaré Vázquez"; O = "Uruguay"
rows = []; tid = 24

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

add("URU-TV1-J001", Trip_Status="Completed", Start_Date="2005-03-29", End_Date="2005-03-30", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Lula da Silva",
    Trip_Objective="Primer viaje oficial del mandato; relanzar la relacion estrategica con Brasil.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/noticias/2005/03/2005032903.htm",
    Source_Reliability="High", Methodological_Notes="Fecha fin estimada.")

add("URU-TV1-J002", Trip_Status="Completed", Start_Date="2005-09-18", End_Date="2005-09-20", Duration_Days=3,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Álvaro Uribe",
    Trip_Objective="Profundizar el intercambio comercial; recibio el Gran Collar de la Orden de San Carlos el 19-sep-2005.",
    Source_Verification="https://archivo.presidencia.gub.uy/_web/noticias/2005/09/2005091909.htm",
    Source_Reliability="High", Methodological_Notes="Fechas inicio/fin estimadas.")

add("URU-TV1-J003", Trip_Status="Completed", Start_Date="2005-10-13", End_Date="2005-10-15", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Salamanca", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XV Cumbre Iberoamericana",
    Trip_Objective="Participar en la XV Cumbre Iberoamericana de Jefes de Estado.",
    Source_Verification="https://legislativo.parlamento.gub.uy:443/temporales/20051005S0049_SSN4156794.html",
    Source_Reliability="High", Methodological_Notes="Venia art.170 (salida 12-oct-2005) cubre la gira europea.", Tema_Foro="Cooperación Política General")

add("URU-TV1-J003", Trip_Status="Completed", Start_Date="2005-10-16", End_Date="2005-10-17", Duration_Days=2,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Alemania",
    Trip_Objective="Visita oficial dentro de la gira europea autorizada por venia.",
    Source_Verification="https://legislativo.parlamento.gub.uy:443/temporales/20051005S0049_SSN4156794.html",
    Source_Reliability="Medium", Methodological_Notes="Ciudad y fechas estimadas; venia menciona destino.")

add("URU-TV1-J003", Trip_Status="Completed", Start_Date="2005-10-18", End_Date="2005-10-19", Duration_Days=2,
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Italia",
    Trip_Objective="Visita oficial dentro de la gira europea autorizada por venia.",
    Source_Verification="https://legislativo.parlamento.gub.uy:443/temporales/20051005S0049_SSN4156794.html",
    Source_Reliability="Medium", Methodological_Notes="Ciudad y fechas estimadas; venia menciona destino.")

add("URU-TV1-J003", Trip_Status="Completed", Start_Date="2005-10-20", End_Date="2005-10-22", Duration_Days=3,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Francia",
    Trip_Objective="Visita oficial dentro de la gira europea autorizada por venia.",
    Source_Verification="https://legislativo.parlamento.gub.uy:443/temporales/20051005S0049_SSN4156794.html",
    Source_Reliability="Medium", Methodological_Notes="Ciudad y fechas estimadas; venia menciona destino.")

add("URU-TV1-J004", Trip_Status="Completed", Start_Date="2005-11-04", End_Date="2005-11-05", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Mar del Plata", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IV Cumbre de las Américas",
    Trip_Objective="IV Cumbre de las Americas; rechazo al ALCA junto al MERCOSUR.",
    Source_Verification="https://summit-americas.org/sas/Cumbres_previas_IVCumbre.html",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-TV1-J005", Trip_Status="Completed", Start_Date="2006-04-26", End_Date="2006-04-28", Duration_Days=3,
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Vicente Fox",
    Trip_Objective="Atraer inversiones y comercio; declaraciones sobre la inviabilidad del ALCA.",
    Source_Verification="https://www.infobae.com/2006/05/04/253240-bush-y-tabare-acuerdan-intensificar-la-relacion-comercial-sus-paises/",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas (fines de abril 2006).")

add("URU-TV1-J006", Trip_Status="Completed", Start_Date="2006-05-03", End_Date="2006-05-04", Duration_Days=2,
    Destination_Country="United States", Destination_City="Washington", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="George W. Bush",
    Trip_Objective="Reunion en la Casa Blanca el 4-may-2006; ampliar comercio (TIFA) y plantear el conflicto de las pasteras.",
    Source_Verification="https://www.infobae.com/2006/05/04/253240-bush-y-tabare-acuerdan-intensificar-la-relacion-comercial-sus-paises/",
    Source_Reliability="High", Methodological_Notes="Reunion con Bush confirmada 4-may-2006.")

add("URU-TV1-J007", Trip_Status="Completed", Start_Date="2006-05-11", End_Date="2006-05-13", Duration_Days=3,
    Destination_Country="Austria", Destination_City="Vienna", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IV Cumbre UE-ALC",
    Trip_Objective="Cumbre UE-America Latina y Caribe.",
    Source_Verification="Search Query: Tabare Vazquez Cumbre UE America Latina Viena mayo 2006",
    Source_Reliability="Medium", Methodological_Notes="Fuente enuncia el viaje en futuro (planificado); asistencia altamente probable (FUENTE-DEBIL).", Tema_Foro="Cooperación Política General")

add("URU-TV1-J008", Trip_Status="Completed", Start_Date="2006-07-20", End_Date="2006-07-21", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Córdoba", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XXX Cumbre MERCOSUR",
    Trip_Objective="Cumbre MERCOSUR; ingreso de Venezuela como miembro pleno.",
    Source_Verification="https://www.cancilleria.gob.ar/es/actualidad/comunicados/cumbre-de-presidentes-del-mercosur-en-cordoba",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

add("URU-TV1-J009", Trip_Status="Completed", Start_Date="2007-05-01", End_Date="2007-05-03", Duration_Days=3,
    Destination_Country="Qatar", Destination_City="Doha", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emir de Qatar",
    Trip_Objective="Visita de Estado; recibio la Orden del Merito el 2-may-2007.",
    Source_Verification="https://www.lr21.com.uy/politica/256412-vazquez-condecorado-por-principe-heredero-de-qatar",
    Source_Reliability="Medium", Methodological_Notes="Fechas de arribo/salida estimadas.")

add("URU-TV1-J010", Trip_Status="Completed", Start_Date="2007-06-28", End_Date="2007-06-29", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre MERCOSUR",
    Trip_Objective="Cumbre MERCOSUR; Uruguay asume la PPT del FCCP.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/audionet/2007/06/06_2007.htm",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas.", Tema_Foro="Comercio/Integración Económica")

add("URU-TV1-J011", Trip_Status="Completed", Start_Date="2007-09-18", End_Date="2007-09-20", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Congreso de los Diputados",
    Trip_Objective="Visita oficial a Espania; discurso en el Congreso el 19-sep-2007.",
    Source_Verification="https://www.congreso.es/en/cem/visituruguay2007",
    Source_Reliability="High", Methodological_Notes="Fechas inicio/fin estimadas.")

add("URU-TV1-J012", Trip_Status="Completed", Start_Date="2007-11-08", End_Date="2007-11-10", Duration_Days=3,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XVII Cumbre Iberoamericana",
    Trip_Objective="XVII Cumbre Iberoamericana (cohesion social).",
    Source_Verification="https://segib.org/?document=discurso-del-presidente-de-uruguay-tabare-vazquez",
    Source_Reliability="High", Methodological_Notes="Asistio en persona.", Tema_Foro="Cooperación Política General")

add("URU-TV1-J013", Trip_Status="Completed", Start_Date="2008-06-16", End_Date="2008-06-17", Duration_Days=2,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Martín Torrijos",
    Trip_Objective="Visita de Estado; recibio la Orden Omar Torrijos el 16-jun-2008.",
    Source_Verification="https://web.archive.org/web/20131024003757/http://archivo.presidencia.gub.uy/_Web/noticias/2008/06/2008061607.htm",
    Source_Reliability="High", Methodological_Notes="Parte de la gira Panama-Cuba-Mexico (jun 2008).")

add("URU-TV1-J013", Trip_Status="Completed", Start_Date="2008-06-18", End_Date="2008-06-20", Duration_Days=3,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Raúl Castro",
    Trip_Objective="Visita con amplia delegacion ministerial; cumbre con Raul Castro.",
    Source_Verification="https://en.mercopress.com/2009/01/05/cuba-s-raul-castro-scheduled-to-visit-uruguay-this-year",
    Source_Reliability="High", Methodological_Notes="Fechas estimadas; se reunio dos veces con Raul Castro.")

add("URU-TV1-J013", Trip_Status="Completed", Start_Date="2008-06-21", End_Date="2008-06-22", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Felipe Calderón",
    Trip_Objective="Tramo mexicano de la gira de junio 2008.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2008/MRREE.pdf",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas; MEM cita gira 'Panama, Cuba y Mexico'.")

add("URU-TV1-J014", Trip_Status="Completed", Start_Date="2008-09-01", End_Date="2008-09-03", Duration_Days=3,
    Destination_Country="South Korea", Destination_City="Seoul", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Lee Myung-bak",
    Trip_Objective="Primera visita de Estado de un presidente uruguayo a Corea del Sur.",
    Source_Verification="https://ury.mofa.go.kr/uy-es/brd/m_6507/view.do?seq=659079",
    Source_Reliability="Medium", Methodological_Notes="Mes confirmado (set 2008) por la Embajada de Corea; dias exactos estimados.")

add("URU-TV1-J014", Trip_Status="Completed", Start_Date="2008-09-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="New Zealand", Destination_City="Wellington", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Helen Clark",
    Trip_Objective="Primer presidente uruguayo en visitar Nueva Zelanda.",
    Source_Verification="Search Query: Tabare Vazquez visita Nueva Zelanda Helen Clark 2008",
    Source_Reliability="Low", Methodological_Notes="Hecho confirmado; sin fuente institucional para la fecha exacta; agrupada tentativamente con la gira asiatica 2008. Verificacion No-verificable.")

add("URU-TV1-J015", Trip_Status="Completed", Start_Date="2008-12-15", End_Date="2008-12-17", Duration_Days=3,
    Destination_Country="Brazil", Destination_City="Salvador", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre MERCOSUR/UNASUR/CALC",
    Trip_Objective="Cumbre MERCOSUR y UNASUR en Salvador de Bahia; I Cumbre America Latina y Caribe.",
    Source_Verification="https://legislativo.parlamento.gub.uy:443/temporales/20081209S0063_SSN5083377.html",
    Source_Reliability="High", Methodological_Notes="Venia art.170 (salida 15-dic-2008).", Tema_Foro="Comercio/Integración Económica")

add("URU-TV1-J015", Trip_Status="Completed", Start_Date="2008-12-19", End_Date="2008-12-21", Duration_Days=3,
    Destination_Country="Saudi Arabia", Destination_City="Riyadh", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rey de Arabia Saudita",
    Trip_Objective="Visita oficial a Arabia Saudita desde el 19-dic-2008.",
    Source_Verification="https://legislativo.parlamento.gub.uy:443/temporales/20081209S0063_SSN5083377.html",
    Source_Reliability="High", Methodological_Notes="Venia art.170 menciona destino; fecha fin estimada.")

add("URU-TV1-J016", Trip_Status="Completed", Start_Date="2009-03-10", End_Date="2009-03-10", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Lula da Silva",
    Trip_Objective="Firma de acuerdos (servicios aereos, interconexion electrica, ensenianza del portugues).",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="High")

add("URU-TV1-J017", Trip_Status="Completed", Start_Date="2009-03-19", End_Date="2009-03-23", Duration_Days=5,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Hu Jintao",
    Trip_Objective="Visita de Estado; firma de acuerdos economico-comerciales y de cooperacion.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="High", Methodological_Notes="Discrepancia: MEM lista tambien '21 al 26 de marzo' para la gira comercial.")

add("URU-TV1-J018", Trip_Status="Completed", Start_Date="2009-04-23", End_Date="2009-04-24", Duration_Days=2,
    Destination_Country="Costa Rica", Destination_City="San José", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Óscar Arias",
    Trip_Objective="Visita presidencial bilateral.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="Medium", Methodological_Notes="MEM (DIPCI) lista como visita presidencial.")

add("URU-TV1-J019", Trip_Status="Completed", Start_Date="2009-05-05", End_Date="2009-05-06", Duration_Days=2,
    Destination_Country="Iran", Destination_City="Tehran", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mahmud Ahmadineyad",
    Trip_Objective="Visita presidencial; agenda economico-comercial.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="Medium", Methodological_Notes="MEM (DIPCI): 'Visita Presidencial a Iran el 5 y 6 de mayo'.")

add("URU-TV1-J020", Trip_Status="Completed", Start_Date="2009-07-24", End_Date="2009-07-24", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre MERCOSUR",
    Trip_Objective="Cumbre de presidentes del MERCOSUR (PPT Paraguay).",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada de la cumbre presidencial (jul-2009).", Tema_Foro="Comercio/Integración Económica")

add("URU-TV1-J021", Trip_Status="Completed", Start_Date="2009-08-28", End_Date="2009-08-28", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="San Carlos de Bariloche", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="UNASUR (reunion extraordinaria)",
    Trip_Objective="Reunion extraordinaria de UNASUR sobre bases militares y zona de paz.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="High", Methodological_Notes="MEM 2009: asistio el presidente Vazquez.", Tema_Foro="Cooperación Política General")

add("URU-TV1-J022", Trip_Status="Completed", Start_Date="2009-09-12", End_Date="2009-09-18", Duration_Days=7,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="64ª Asamblea General ONU",
    Trip_Objective="Participacion en el 64º periodo de sesiones de la AGNU.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="High", Methodological_Notes="MEM (DIPCI): 'Estados Unidos (12 al 18 de setiembre)'.", Tema_Foro="Cooperación Política General")

add("URU-TV1-J023", Trip_Status="Completed", Start_Date="2009-09-27", End_Date="2009-09-28", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Isla Margarita", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="II Cumbre América del Sur-África",
    Trip_Objective="II Cumbre ASA; creacion del Banco del Sur.",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="High", Methodological_Notes="MEM 2009: participo el presidente.", Tema_Foro="Cooperación Política General")

add("URU-TV1-J024", Trip_Status="Completed", Start_Date="2009-12-11", End_Date="2009-12-15", Duration_Days=5,
    Destination_Country="Japan", Destination_City="Tokyo", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Japón",
    Trip_Objective="Visita a Japon; Notas Reversales de cooperacion (energia solar).",
    Source_Verification="http://archivo.presidencia.gub.uy/_web/MEM_2009/MRREE.pdf",
    Source_Reliability="High", Methodological_Notes="MEM 2009: 'visita a Japon (11 al 15 de diciembre)'.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
print(f"OK: {len(rows)} filas de {P} (1er mandato) anexadas. Ultimo Trip_ID = {tid-1}")
