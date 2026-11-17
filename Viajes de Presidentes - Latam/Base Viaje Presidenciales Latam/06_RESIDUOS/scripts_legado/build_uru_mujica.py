# -*- coding: utf-8 -*-
"""
URUGUAY — Jose "Pepe" Mujica (Frente Amplio, 2010-03-01 a 2015-03-01). Tercer bloque uruguayo.
Investigacion dedicada (modo investigador, 2026-07-08): 23 giras completadas (28 filas pais) + 2 canceladas por salud.
Trip_ID 55-84. Convencion: URU-JM-JXXX. Anexa al CSV existente.
HALLAZGO: perfil "alto perfil global / bajo volumen de largo alcance". 65 salidas totales (El Observador),
pero concentradas en vecinos (Brasil 17, Argentina 15, Venezuela 11). Fuera de la region: 1 gira europea (2011),
1 China (2013), 2 EEUU (AGNU 2013 + Obama 2014). Hablo en AGNU un solo anio (2013, "Soy del Sur").
2 cancelaciones por salud: Espania nov-2012 (trombosis) e Italia jun-2013 (reposo medico).
Venias recuperadas: 3 (Brasilia jul-2012, Brasilia dic-2012, EEUU may-2014).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "uruguay", "uruguay_viajes.csv")
P = "José Mujica"; O = "Uruguay"
rows = []; tid = 55

def add(jid, vs=None, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    r = new_row(**kw)
    if vs: r["Verificacion_Status"] = vs
    rows.append(r); tid += 1

add("URU-JM-J001", vs="Solo-Query", Trip_Status="Completed", Start_Date="2010-03-11", End_Date="2010-03-11", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Valparaiso", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Sebastián Piñera",
    Trip_Objective="Asistir a la transmision de mando presidencial de Piniera.",
    Source_Verification="Search Query: Mujica asuncion Pinera Chile marzo 2010",
    Source_Reliability="Low", Methodological_Notes="Reportado por EcuRed; sin URL primaria aislada; CONFIRMAR.", Tema_Foro="Cooperación Política General")

add("URU-JM-J002", Trip_Status="Completed", Start_Date="2011-01-01", End_Date="2011-01-01", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Dilma Rousseff",
    Trip_Objective="Asistir a la investidura de Rousseff; reunion bilateral el 2-ene.",
    Source_Verification="https://www.france24.com/en/20110101-dilma-rousseff-replaces-lula-silva-president-brazil-marxist-guerrilla-iron-lady",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-JM-J003", vs="Solo-Query", Trip_Status="Completed", Start_Date="2011-06-29", End_Date="2011-06-30", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Bicentenario de Paraguay / Cumbre MERCOSUR",
    Trip_Objective="Actos del bicentenario, integracion Urupabol y cumbre MERCOSUR.",
    Source_Verification="Search Query: Mujica Asuncion junio 2011 bicentenario Mercosur",
    Source_Reliability="Medium", Methodological_Notes="Fechas aproximadas; combina bicentenario y cumbre.", Tema_Foro="Comercio/Integración Económica")

add("URU-JM-J004", vs="Solo-Query", Trip_Status="Completed", Start_Date="2011-07-27", End_Date="2011-07-28", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Ollanta Humala",
    Trip_Objective="Asistir a la investidura de Humala.",
    Source_Verification="Search Query: Mujica asuncion Ollanta Humala julio 2011",
    Source_Reliability="Medium", Methodological_Notes="Reportado por EcuRed y listas de asistentes.", Tema_Foro="Cooperación Política General")

add("URU-JM-J005", vs="Solo-Query", Trip_Status="Completed", Start_Date="2011-10-11", End_Date="2011-10-20", Duration_Days=10,
    Destination_Country="Sweden", Destination_City="Stockholm", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gira comercial europea",
    Trip_Objective="Promocion comercial, inversiones y cooperacion cientifica.",
    Source_Verification="https://medios.presidencia.gub.uy/jm_portal/2012/mem_anual/rree/mrree.pdf",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas (EcuRed); gira multi-pais comparte Journey_ID.")

add("URU-JM-J005", vs="Solo-Query", Trip_Status="Completed", Start_Date="2011-10-11", End_Date="2011-10-20", Duration_Days=10,
    Destination_Country="Norway", Destination_City="Oslo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gira comercial europea",
    Trip_Objective="Promocion comercial e inversiones.",
    Source_Verification="https://medios.presidencia.gub.uy/jm_portal/2012/mem_anual/rree/mrree.pdf",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas; tramo de la gira europea.")

add("URU-JM-J005", Trip_Status="Completed", Start_Date="2011-10-11", End_Date="2011-10-20", Duration_Days=10,
    Destination_Country="Germany", Destination_City="Berlin", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Christian Wulff / Angela Merkel",
    Trip_Objective="Recibido con honores en el Palacio de Bellevue; busco apoyo cientifico e inversion.",
    Source_Verification="https://www.subrayado.com.uy/jose-mujica-se-reune-hoy-canciller-alemania-angela-merkel-n5285",
    Source_Reliability="Medium", Methodological_Notes="Reunion con Merkel confirmada; fecha exacta del tramo incierta.")

add("URU-JM-J005", vs="Solo-Query", Trip_Status="Completed", Start_Date="2011-10-11", End_Date="2011-10-20", Duration_Days=10,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gira comercial europea / relacion UE-MERCOSUR",
    Trip_Objective="Promocion comercial y dialogo UE-MERCOSUR.",
    Source_Verification="https://medios.presidencia.gub.uy/jm_portal/2012/mem_anual/rree/mrree.pdf",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas; tramo de la gira europea.")

add("URU-JM-J006", vs="Solo-Query", Trip_Status="Completed", Start_Date="2011-11-15", End_Date="2011-11-19", Duration_Days=5,
    Destination_Country="Brazil", Destination_City="Porto Alegre", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Encuentro Empresarial Rio Grande do Sul-Uruguay",
    Trip_Objective="Promocion comercial y fronteriza.",
    Source_Verification="Search Query: Mujica Porto Alegre noviembre 2011 empresarial",
    Source_Reliability="Low", Methodological_Notes="Tramo previo a Mexico; fechas aproximadas; CONFIRMAR.")

add("URU-JM-J006", Trip_Status="Completed", Start_Date="2011-11-15", End_Date="2011-11-19", Duration_Days=5,
    Destination_Country="Mexico", Destination_City="Guadalajara", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Felipe Calderón",
    Trip_Objective="Firma del Plan Estrategico de Cooperacion Mexico-Uruguay.",
    Source_Verification="https://politica.expansion.mx/mexico/2025/05/13/la-relacion-de-jose-mujica-con-mexico-y-sus-lideres-politicos",
    Source_Reliability="Medium", Methodological_Notes="Recibido en el Instituto Cultural Cabanias por Calderon.")

add("URU-JM-J007", vs="Solo-Query", Trip_Status="Completed", Start_Date="2012-04-13", End_Date="2012-04-15", Duration_Days=3,
    Destination_Country="Colombia", Destination_City="Cartagena", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VI Cumbre de las Américas",
    Trip_Objective="Participar en la cumbre; primer contacto con Obama.",
    Source_Verification="Search Query: Mujica Cumbre de las Americas Cartagena abril 2012",
    Source_Reliability="Medium", Methodological_Notes="Reportado por fuentes secundarias; CONFIRMAR fechas.", Tema_Foro="Cooperación Política General")

add("URU-JM-J008", vs="Solo-Query", Trip_Status="Completed", Start_Date="2012-06-29", End_Date="2012-06-29", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Mendoza", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="43ª Cumbre del MERCOSUR",
    Trip_Objective="Cumbre donde se suspendio a Paraguay y se aprobo el ingreso de Venezuela.",
    Source_Verification="Search Query: Mujica cumbre Mercosur Mendoza junio 2012",
    Source_Reliability="Medium", Methodological_Notes="Confirmado por prensa (La Nacion).", Tema_Foro="Comercio/Integración Económica")

add("URU-JM-J009", Trip_Status="Completed", Start_Date="2012-06-20", End_Date="2012-06-22", Duration_Days=3,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Conferencia ONU Desarrollo Sostenible (Río+20)",
    Trip_Objective="Discurso celebre contra el hiperconsumismo.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/audios/completos/presidente-jose-mujica-cumbre-rio20",
    Source_Reliability="High", Methodological_Notes="Intervencion el 20-jun-2012.", Tema_Foro="Medio Ambiente/Clima")

add("URU-JM-J010", Trip_Status="Completed", Start_Date="2012-07-30", End_Date="2012-07-31", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Reunión Extraordinaria CMC / Cumbre MERCOSUR",
    Trip_Objective="Incorporacion plena de Venezuela al MERCOSUR.",
    Source_Verification="https://legislativo.parlamento.gub.uy/temporales/20120726S0030_SSN2340038.html",
    Source_Reliability="High", Methodological_Notes="VENIA parlamentaria (sesion 26-jul-2012).", Tema_Foro="Comercio/Integración Económica")

add("URU-JM-J011", Trip_Status="Completed", Start_Date="2012-12-06", End_Date="2012-12-07", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XLIV Reunión del CMC / Cumbre MERCOSUR",
    Trip_Objective="Cumbre semestral de jefes de Estado del MERCOSUR.",
    Source_Verification="https://legislativo.parlamento.gub.uy/temporales/20121127S0055_SSN5157774.html",
    Source_Reliability="High", Methodological_Notes="VENIA parlamentaria (sesion 27-nov-2012).", Tema_Foro="Comercio/Integración Económica")

add("URU-JM-J012", Trip_Status="Completed", Start_Date="2013-01-26", End_Date="2013-01-28", Duration_Days=3,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="I Cumbre CELAC-UE y I Cumbre CELAC",
    Trip_Objective="Participar en ambas cumbres.",
    Source_Verification="https://www.elobservador.com.uy/nota/mujica-viaja-a-chile-para-participar-de-dos-cumbres--201312316240",
    Source_Reliability="High", Methodological_Notes="Cumbre CELAC-UE 26-27 ene; CELAC 27-28 ene.", Tema_Foro="Cooperación Política General")

add("URU-JM-J013", Trip_Status="Completed", Start_Date="2013-03-06", End_Date="2013-03-08", Duration_Days=3,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Funeral de Estado de Hugo Chávez",
    Trip_Objective="Asistir a las exequias de Chavez.",
    Source_Verification="https://cnnespanol.cnn.com/2013/03/06/comienzan-actos-funebres-en-honor-a-hugo-chavez-en-venezuela",
    Source_Reliability="High", Methodological_Notes="Llego a Caracas la madrugada del 6-mar junto a Cristina Fernandez.", Tema_Foro="Cooperación Política General")

add("URU-JM-J014", Trip_Status="Completed", Start_Date="2013-05-24", End_Date="2013-05-28", Duration_Days=5,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Xi Jinping",
    Trip_Objective="Visita de Estado; firma de 7 acuerdos; feria CIFTIS.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/visita-mujica-china-buscara-fortalecer-intercambio-bilateral-atraer",
    Source_Reliability="High", Methodological_Notes="Talks con Xi el 27-may-2013; gira multi-pais.")

add("URU-JM-J014", Trip_Status="Completed", Start_Date="2013-05-28", End_Date="2013-06-02", Duration_Days=6,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Rey Juan Carlos / Mariano Rajoy",
    Trip_Objective="Madrid, Cadiz y Bilbao; agenda comercial y politica.",
    Source_Verification="https://www.subrayado.com.uy/vuelve-mujica-su-gira-china-espana-y-el-vaticano-n24106",
    Source_Reliability="High", Methodological_Notes="Tramo Vaticano/Napoles/Roma suspendido; regreso el jueves.")

add("URU-JM-J015", Trip_Status="Completed", Start_Date="2013-08-15", End_Date="2013-08-15", Duration_Days=1,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Horacio Cartes",
    Trip_Objective="Asistir a la investidura de Cartes.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/mujica-partio-hacia-paraguay-para-asistir-asuncion-nuevas-autoridades",
    Source_Reliability="High", Methodological_Notes="Partio en la madrugada del 15-ago-2013.", Tema_Foro="Cooperación Política General")

add("URU-JM-J016", Trip_Status="Completed", Start_Date="2013-09-24", End_Date="2013-09-24", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="68º período de sesiones de la AGNU",
    Trip_Objective="Discurso 'Soy del Sur' ante la Asamblea General.",
    Source_Verification="https://www.swissinfo.ch/spa/soy-del-sur:-el-recordado-discurso-ante-la-onu-en-el-que-mujica-llam%C3%B3-a-%22salvar-la-vida%22/90038419",
    Source_Reliability="High", Methodological_Notes="Unico anio que Mujica hablo en la ONU; discurso el 24-sep.", Tema_Foro="Cooperación Política General")

add("URU-JM-J017", Trip_Status="Completed", Start_Date="2014-01-28", End_Date="2014-01-29", Duration_Days=2,
    Destination_Country="Cuba", Destination_City="Havana", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cumbre de la CELAC",
    Trip_Objective="Cumbre; encuentro con Fidel Castro y con negociadores de paz colombianos.",
    Source_Verification="http://www.cubadebate.cu/noticias/2014/01/29/fraternal-encuentro-de-fidel-con-evo-correa-y-daniel-fotos/",
    Source_Reliability="High", Methodological_Notes="Reunion con Fidel Castro confirmada.", Tema_Foro="Cooperación Política General")

add("URU-JM-J018", Trip_Status="Completed", Start_Date="2014-03-11", End_Date="2014-03-12", Duration_Days=2,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Michelle Bachelet",
    Trip_Objective="Investidura de Bachelet; seminario CEPAL sobre desigualdad.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/presidente-mujica-cerro-su-visita-chile-seminario-junto-michelle-bachelet",
    Source_Reliability="High", Methodological_Notes="Ceremonia en Valparaiso; seminario con Bachelet el dia siguiente.", Tema_Foro="Cooperación Política General")

add("URU-JM-J019", Trip_Status="Completed", Start_Date="2014-05-11", End_Date="2014-05-15", Duration_Days=5,
    Destination_Country="United States", Destination_City="Washington", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Barack Obama (Salón Oval)",
    Trip_Objective="Guantanamo, comercio, DDHH; diserto en American University, BID y OEA.",
    Source_Verification="https://legislativo.parlamento.gub.uy/temporales/20140506S0012_SSN2279983.html",
    Source_Reliability="High", Methodological_Notes="VENIA (sesion 6-may-2014); encuentro con Obama el 12-may.")

add("URU-JM-J020", Trip_Status="Completed", Start_Date="2014-07-18", End_Date="2014-07-19", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Horacio Cartes",
    Trip_Objective="Hidrovia, puertos y puerto de aguas profundas; discurso sobre la Triple Alianza.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/videos/visita-oficial-mujica-paraguay",
    Source_Reliability="High", Methodological_Notes="Se concreto la visita anunciada por Cartes en 2013.")

add("URU-JM-J021", vs="Solo-Query", Trip_Status="Completed", Start_Date="2014-07-29", End_Date="2014-07-29", Duration_Days=1,
    Destination_Country="Venezuela", Destination_City="Caracas", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XLVI Reunión del CMC / Cumbre MERCOSUR",
    Trip_Objective="Cumbre semestral; discurso 'Necesitamos al MERCOSUR como al pan'.",
    Source_Verification="Search Query: Mujica cumbre Mercosur Caracas julio 2014",
    Source_Reliability="Medium", Methodological_Notes="Confirmado por Parlamento MERCOSUR y prensa.", Tema_Foro="Comercio/Integración Económica")

add("URU-JM-J022", vs="Solo-Query", Trip_Status="Completed", Start_Date="2014-12-16", End_Date="2014-12-17", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Parana", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="47ª Cumbre del MERCOSUR",
    Trip_Objective="Cumbre de despedida; traspaso de presidencia pro tempore.",
    Source_Verification="Search Query: Mujica cumbre Mercosur Parana diciembre 2014",
    Source_Reliability="Medium", Methodological_Notes="Confirmado por Parlamento MERCOSUR; discurso de despedida.", Tema_Foro="Comercio/Integración Económica")

add("URU-JM-J023", vs="Solo-Query", Trip_Status="Completed", Start_Date="2014-12-08", End_Date="2014-12-09", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Veracruz", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XXIV Cumbre Iberoamericana",
    Trip_Objective="Participacion en la cumbre; actividades en Guadalajara (FIL).",
    Source_Verification="Search Query: Mujica Cumbre Iberoamericana Veracruz diciembre 2014",
    Source_Reliability="Low", Methodological_Notes="FUENTE-DEBIL: presencia no confirmada con URL primaria; CONFIRMAR.", Tema_Foro="Cooperación Política General")

add("URU-JM-J024", Trip_Status="Canceled", Start_Date="2012-11-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Transit/Medical",
    Sideline_Bilaterals="NA", Counterpart_Event="Viaje oficial a España",
    Trip_Objective="Objetivo: agenda oficial en Espania. Cancelacion: aparicion de coagulo en pierna derecha (compromiso venoso cronico).",
    Source_Verification="https://cnnespanol.cnn.com/2025/05/13/latinoamerica/pepe-mujica-problemas-salud-orix",
    Source_Reliability="High", Methodological_Notes="Fecha exacta desconocida (nov-2012); Start_Date estimada.")

add("URU-JM-J025", Trip_Status="Canceled", Start_Date="2013-06-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="Italy", Destination_City="Rome", Visit_Category="Bilateral", Visit_Subtype="Transit/Medical",
    Sideline_Bilaterals="NA", Counterpart_Event="Visita de Estado a Italia",
    Trip_Objective="Objetivo: visita de Estado (tramo final gira China-Espania). Cancelacion: recomendacion medica de reposo.",
    Source_Verification="https://www.infobae.com/america/agencias/2025/05/13/biografia-de-pepe-mujica/",
    Source_Reliability="High", Methodological_Notes="Fecha exacta desconocida (jun-2013); Start_Date estimada.")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
print(f"OK: {len(rows)} filas de {P} anexadas. Ultimo Trip_ID = {tid-1}")
