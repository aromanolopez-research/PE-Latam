# -*- coding: utf-8 -*-
"""
URUGUAY — Tabare Vazquez, SEGUNDO mandato (Frente Amplio, 2015-03-01 a 2020-03-01). Cuarto bloque uruguayo.
Investigacion dedicada (modo investigador, 2026-07-08): 14 completados + 1 cancelado/delegado (AGNU 2019 por cancer).
Trip_ID 85-100. Convencion: URU-TV2-JXXX. Anexa al CSV existente.
Perfil austero (viajo mucho menos que en su 1er mandato: 24 giras). Hito: Visita de Estado a China (oct-2016).
Cancer de pulmon (ago-2019) trunca el tramo final: delego la AGNU 2019 en el canciller Nin Novoa.
Sin confusion con el 1er mandato (todo dentro de 2015-2020).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "uruguay", "uruguay_viajes.csv")
P = "Tabaré Vázquez"; O = "Uruguay"
rows = []; tid = 85

def add(jid, vs=None, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    r = new_row(**kw)
    if vs: r["Verificacion_Status"] = vs
    rows.append(r); tid += 1

add("URU-TV2-J001", Trip_Status="Completed", Start_Date="2015-04-10", End_Date="2015-04-11", Duration_Days=2,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VII Cumbre de las Américas",
    Trip_Objective="Primer foro internacional del mandato; contactos con Obama y Maduro.",
    Source_Verification="https://www.oas.org/es/centro_noticias/comunicado_prensa.asp?sCodigo=C-131/15",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-TV2-J002", Trip_Status="Completed", Start_Date="2015-05-21", End_Date="2015-05-21", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Dilma Rousseff",
    Trip_Objective="Primera visita bilateral del mandato; integracion Brasil-Uruguay y agenda MERCOSUR-UE.",
    Source_Verification="https://www.gov.br/mre/en/contact-us/press-area/press-releases/joint-presidential-statement-state-visit-of-the-president-of-uruguay-tabare-vazquez-to-brazil-brasilia-may-21-2015",
    Source_Reliability="High")

add("URU-TV2-J003", Trip_Status="Completed", Start_Date="2015-07-16", End_Date="2015-07-17", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="48ª Cumbre del MERCOSUR",
    Trip_Objective="Cumbre semestral MERCOSUR; bilateral con Maduro por acuerdo de exportacion de alimentos.",
    Source_Verification="https://www.celag.org/cumbre-del-mercosur-en-brasilia-informe/",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

add("URU-TV2-J004", vs="Solo-Query", Trip_Status="Completed", Start_Date="2015-09-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Mediación UNASUR crisis Colombia-Venezuela",
    Trip_Objective="Como presidente pro tempore de UNASUR, mediar en la crisis fronteriza Colombia-Venezuela.",
    Source_Verification="Search Query: Vazquez Quito UNASUR mediacion Santos Maduro septiembre 2015",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; reportado por El Tiempo, no verificado en fuente primaria; posible confusion con AGNU. CONFIRMAR.", Tema_Foro="Cooperación Política General")

add("URU-TV2-J005", vs="Solo-Query", Trip_Status="Completed", Start_Date="2015-09-25", End_Date="2015-09-28", Duration_Days=4,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="70ª Asamblea General de la ONU",
    Trip_Objective="70ª AGNU y Cumbre de Operaciones de Paz; reunion bilateral con Obama (28-sep).",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/vazquez-partio-hacia-nueva-york-para-participar-70a-asamblea-general-onu",
    Source_Reliability="Medium", Methodological_Notes="Fechas de estadia estimadas; reunion con Obama confirmada 28-sep-2015.", Tema_Foro="Cooperación Política General")

add("URU-TV2-J006", Trip_Status="Completed", Start_Date="2015-12-10", End_Date="2015-12-10", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Mauricio Macri",
    Trip_Objective="Asistir a la investidura de Macri; regreso inmediato a Montevideo.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/vazquez-asistio-acto-asuncion-macri-presidente-argentina",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-TV2-J007", Trip_Status="Completed", Start_Date="2016-09-19", End_Date="2016-09-21", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="71ª Asamblea General de la ONU",
    Trip_Objective="Disertar en la 71ª AGNU; alianza mundial por la salud, politica antitabaco y Acuerdo de Paris.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/videos/discurso-del-presidente-tabare-vazquez-ante-asamblea-general-naciones-unidas",
    Source_Reliability="High", Methodological_Notes="Discurso confirmado 20-sep-2016.", Tema_Foro="Cooperación Política General")

add("URU-TV2-J008", Trip_Status="Completed", Start_Date="2016-10-10", End_Date="2016-10-20", Duration_Days=11,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Xi Jinping",
    Trip_Objective="Visita de Estado; Asociacion Estrategica y lanzamiento de negociaciones TLC; Cumbre Empresarial China-LAC en Tangshan.",
    Source_Verification="https://www.uruguayxxi.gub.uy/en/news/article/uruguay-xxi-acompana-mision-oficial-a-china-encabezada-por-el-sr-presidente-de-la-republica/",
    Source_Reliability="High", Methodological_Notes="Gira multiciudad: Beijing, Tangshan, Guangzhou; reunion Xi 18-oct-2016.")

add("URU-TV2-J009", vs="Solo-Query", Trip_Status="Completed", Start_Date="2017-06-01", End_Date="2017-06-01", Duration_Days=1,
    Destination_Country="Egypt", Destination_City="Cairo", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Escala oficial en El Cairo",
    Trip_Objective="Escala oficial en El Cairo previa a la gira europea; relaciones con el mundo arabe.",
    Source_Verification="Search Query: Vazquez El Cairo Egipto junio 2017 gira",
    Source_Reliability="Low", Methodological_Notes="Fecha estimada; reportado por La Diaria como parte de la gira Egipto-Suiza; CONFIRMAR.", Tema_Foro="Cooperación Política General")

add("URU-TV2-J009", vs="Solo-Query", Trip_Status="Completed", Start_Date="2017-06-03", End_Date="2017-06-06", Duration_Days=4,
    Destination_Country="Switzerland", Destination_City="Geneva", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="106ª Conferencia Internacional del Trabajo (OIT)",
    Trip_Objective="Discurso ante la 106ª CIT de la OIT (5-jun); reuniones con Guy Ryder (OIT) y Tedros (OMS).",
    Source_Verification="https://www.france24.com/es/am%C3%A9rica-latina/20201206-uruguay-expresidente-tabare-vazquez-muere-cancer-pulmon",
    Source_Reliability="Medium", Methodological_Notes="Fechas de estadia estimadas; discurso confirmado 5-jun-2017; misma gira que Egipto.", Tema_Foro="Cooperación Política General")

add("URU-TV2-J010", Trip_Status="Completed", Start_Date="2017-07-21", End_Date="2017-07-21", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Mendoza", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del MERCOSUR",
    Trip_Objective="Cumbre semestral MERCOSUR; discurso por 'sinceramiento' del bloque; bilateral con Macri; Honoris Causa UNCuyo.",
    Source_Verification="https://www.infobae.com/politica/2017/07/21/cumbre-del-mercosur-mauricio-macri-se-reunion-con-tabare-vazquez-y-evo-morales-antes-de-la-apertura-oficial/",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

add("URU-TV2-J011", Trip_Status="Completed", Start_Date="2017-11-14", End_Date="2017-11-14", Duration_Days=1,
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Enrique Peña Nieto",
    Trip_Objective="Visita Oficial; firma de instrumentos aduaneros, academico-diplomaticos y de innovacion; Orden del Aguila Azteca.",
    Source_Verification="https://www.gob.mx/epn/articulos/visita-oficial-del-presidente-de-la-republica-oriental-del-uruguay-tabare-vazquez",
    Source_Reliability="High", Methodological_Notes="Visita de un dia; posible llegada la vispera.")

add("URU-TV2-J012", Trip_Status="Completed", Start_Date="2018-04-13", End_Date="2018-04-14", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="VIII Cumbre de las Américas",
    Trip_Objective="VIII Cumbre de las Americas; bilaterales con Temer, Macri, Pena Nieto y Alvarado.",
    Source_Verification="https://www.subrayado.com.uy/vazquez-se-reunio-temer-y-hay-compromiso-mejorar-la-seguridad-el-chuy-n502588",
    Source_Reliability="High", Methodological_Notes="Arribo la noche del 13-abr; no hablo en plenaria.", Tema_Foro="Cooperación Política General")

add("URU-TV2-J013", Trip_Status="Completed", Start_Date="2019-01-01", End_Date="2019-01-01", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Jair Bolsonaro",
    Trip_Objective="Asistir a la investidura de Bolsonaro; viajo por la maniana y regreso por la noche; entre 10 jefes de Estado.",
    Source_Verification="https://www.elobservador.com.uy/nota/tabare-vazquez-uno-de-los-10-mandatarios-que-asistieron-a-la-asuncion-de-bolsonaro-20191117368",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-TV2-J014", Trip_Status="Canceled", Start_Date="2019-09-01", End_Date="NA", Duration_Days="NA",
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="74ª Asamblea General de la ONU",
    Trip_Objective="Objetivo: disertar en la 74ª AGNU. Cancelacion: delego en el canciller Nin Novoa por el tratamiento de su cancer de pulmon.",
    Source_Verification="https://www.elobservador.com.uy/nota/tabare-vazquez-termino-la-radioterapia-contra-el-cancer-de-pulmon-2019920141425",
    Source_Reliability="High", Methodological_Notes="Fecha estimada; delegacion formal en canciller; Nin Novoa anuncio alli la salida del TIAR.", Tema_Foro="Cooperación Política General")

add("URU-TV2-J015", Trip_Status="Completed", Start_Date="2019-12-10", End_Date="2019-12-10", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Alberto Fernández",
    Trip_Objective="Asistir a la investidura de Alberto Fernandez; viajo con el presidente electo Lacalle Pou; uno de sus ultimos viajes.",
    Source_Verification="https://www.montevideo.com.uy/Noticias/Lacalle-Pou-y-Tabare-Vazquez-viajaron-juntos-a-la-asuncion-de-Alberto-Fernandez-uc738164",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
print(f"OK: {len(rows)} filas de {P} (2do mandato) anexadas. Ultimo Trip_ID = {tid-1}")
