# -*- coding: utf-8 -*-
"""
URUGUAY — Luis Lacalle Pou (Partido Nacional, 2020-03-01 a 2025-03-01). Quinto bloque uruguayo.
Investigacion dedicada (modo investigador, 2026-07-08): 30 viajes (28 completados + 2 cancelados con destino).
Trip_ID 101-133 (32 journeys). Convencion: URU-LLP-JXXX. Anexa al CSV existente.
ES EL MAS VIAJERO de la serie uruguaya (>Vazquez I 24, Mujica 23, Batlle 20, Vazquez II 15).
Vacio pandemico total 2020-inicio 2021 (1er viaje 3-feb-2021 Brasil), luego explosion aperturista global.
Tramo final cerrado: MERCOSUR Asuncion jul-2024, bilateral Milei+AMIA jul-2024, AGNU 79 sep-2024 (ultimo).
Dudosos marcados No-verificable/Solo-Query. 2 cancelados: Lasso Ecuador may-2021, IX Cumbre Americas LA jun-2022.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "uruguay", "uruguay_viajes.csv")
P = "Luis Lacalle Pou"; O = "Uruguay"
rows = []; tid = 101

def add(jid, vs=None, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    r = new_row(**kw)
    if vs: r["Verificacion_Status"] = vs
    rows.append(r); tid += 1

add("URU-LLP-J001", Trip_Status="Completed", Start_Date="2021-02-03", End_Date="2021-02-03", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jair Bolsonaro",
    Trip_Objective="Primer viaje del mandato; agenda bilateral comercio MERCOSUR y pandemia.",
    Source_Verification="https://www.infobae.com/america/agencias/2021/02/03/lacalle-pou-visita-brasil-en-su-primer-viaje-al-exterior-como-presidente/",
    Source_Reliability="High", Methodological_Notes="Viaje en el dia (<48h); primer viaje tras el vacio pandemico.")

add("URU-LLP-J002", vs="No-verificable", Trip_Status="Completed", Start_Date="NA", End_Date="NA", Duration_Days="NA",
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Alberto Fernández",
    Trip_Objective="Encuentro bilateral con el presidente argentino.",
    Source_Verification="https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Luis_Lacalle_Pou",
    Source_Reliability="Low", Methodological_Notes="Fecha no verificable; listado en Wikipedia sin fecha. CONFIRMAR.")

add("URU-LLP-J003", Trip_Status="Completed", Start_Date="2021-09-16", End_Date="2021-09-18", Duration_Days=3,
    Destination_Country="Mexico", Destination_City="Mexico City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="VI Cumbre CELAC",
    Trip_Objective="Participacion en la Cumbre CELAC.",
    Source_Verification="https://ladiaria.com.uy/politica/articulo/2021/9/lacalle-pou-viajara-este-jueves-a-mexico-y-luego-a-estados-unidos-para-participar-de-dos-cumbres-internacionales/",
    Source_Reliability="High", Methodological_Notes="Fechas estimadas dentro de la gira.", Tema_Foro="Cooperación Política General")

add("URU-LLP-J003", Trip_Status="Completed", Start_Date="2021-09-20", End_Date="2021-09-24", Duration_Days=5,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="76ª Asamblea General ONU",
    Trip_Objective="Discurso en la AGNU 76; reunion bilateral con John Kerry.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/presidente-lacalle-pou-regreso-uruguay-tras-gira-oficial-mexico-estados",
    Source_Reliability="High", Methodological_Notes="Misma gira que Mexico; fechas estimadas.", Tema_Foro="Cooperación Política General")

add("URU-LLP-J004", Trip_Status="Completed", Start_Date="2021-12-12", End_Date="2021-12-13", Duration_Days=2,
    Destination_Country="Qatar", Destination_City="Doha", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emir Tamim bin Hamad Al Thani",
    Trip_Objective="Apertura comercial hacia Oriente Medio.",
    Source_Verification="https://www.montevideo.com.uy/Noticias/El-cuarto-viaje-de-Luis-Lacalle-Pou-como-presidente-de-Uruguay-sera-a-Qatar-uc803211",
    Source_Reliability="High")

add("URU-LLP-J005", vs="No-verificable", Trip_Status="Completed", Start_Date="2021-12-16", End_Date="2021-12-17", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre de presidentes del MERCOSUR",
    Trip_Objective="Cumbre semestral del MERCOSUR.",
    Source_Verification="https://www.elobservador.com.uy/nota/lacalle-pou-pasara-navidad-en-el-congo-junto-a-los-militares-uruguayos-y-el-ministro-garcia-202112120150",
    Source_Reliability="Low", Methodological_Notes="DUDOSO: fuente de planificacion en futuro; no en Wikipedia; posible virtual. CONFIRMAR.", Tema_Foro="Comercio/Integración Económica")

add("URU-LLP-J006", Trip_Status="Completed", Start_Date="2021-12-23", End_Date="2021-12-26", Duration_Days=4,
    Destination_Country="Democratic Republic of the Congo", Destination_City="Goma", Visit_Category="Other", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Contingente uruguayo MONUSCO",
    Trip_Objective="Navidad con el contingente uruguayo de cascos azules.",
    Source_Verification="https://mediospublicos.uy/lacalle-pou-viaja-al-congo-desde-el-23-al-26-de-diciembre/",
    Source_Reliability="High")

add("URU-LLP-J007", Trip_Status="Completed", Start_Date="2022-02-20", End_Date="2022-02-22", Duration_Days=3,
    Destination_Country="United Arab Emirates", Destination_City="Dubai", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Día Nacional en Expo 2020 Dubái",
    Trip_Objective="Promocion comercial; contactos con empresas y autoridades.",
    Source_Verification="https://www.subrayado.com.uy/lacalle-pou-viajo-dubai-junto-ministros-y-empresarios-n840128",
    Source_Reliability="Medium", Methodological_Notes="Fechas estimadas.", Tema_Foro="Comercio/Integración Económica")

add("URU-LLP-J008", Trip_Status="Completed", Start_Date="2022-03-11", End_Date="2022-03-11", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Gabriel Boric",
    Trip_Objective="Asistencia a la investidura presidencial.",
    Source_Verification="https://www.subrayado.com.uy/lacalle-pou-viajara-chile-la-asuncion-gabriel-boric-n836929",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-LLP-J009", Trip_Status="Completed", Start_Date="2022-05-13", End_Date="2022-05-15", Duration_Days=3,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Mario Abdo Benítez",
    Trip_Objective="211º aniversario de la independencia; bilateral; MERCOSUR y crimen organizado.",
    Source_Verification="https://www.subrayado.com.uy/mercosur-comercio-bilateral-y-crimen-organizado-la-agenda-lacalle-pou-y-abdo-benitez-n868065",
    Source_Reliability="High", Methodological_Notes="Venia del Senado aprobada 10-may-2022.")

add("URU-LLP-J010", Trip_Status="Completed", Start_Date="2022-05-21", End_Date="2022-05-25", Duration_Days=5,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Boris Johnson / Príncipe Carlos",
    Trip_Objective="Primera visita a Europa; comercio e inversiones.",
    Source_Verification="https://en.mercopress.com/2022/05/22/president-of-uruguay-left-for-the-uk-on-his-first-visit-to-europe-will-meet-with-prince-charles-boris-johnson",
    Source_Reliability="High")

add("URU-LLP-J011", Trip_Status="Completed", Start_Date="2022-07-01", End_Date="2022-07-02", Duration_Days=2,
    Destination_Country="Colombia", Destination_City="Bogotá", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Iván Duque",
    Trip_Objective="Bilateral; suscripcion de acuerdos.",
    Source_Verification="https://en.mercopress.com/2022/07/01/lacalle-arrives-in-colombia-to-meet-duque-but-not-petro",
    Source_Reliability="High", Methodological_Notes="Fecha fin estimada.")

add("URU-LLP-J012", Trip_Status="Completed", Start_Date="2022-10-27", End_Date="2022-10-29", Duration_Days=3,
    Destination_Country="Japan", Destination_City="Tokyo", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Fumio Kishida / Emperador Naruhito",
    Trip_Objective="Comercio e inversiones; exportacion de carne; consulta CPTPP.",
    Source_Verification="https://www.uy.emb-japan.go.jp/itpr_ja/11_000001_00246.html",
    Source_Reliability="High", Methodological_Notes="Solicito venia al Senado por 25-31-oct-2022.")

add("URU-LLP-J013", Trip_Status="Completed", Start_Date="2023-01-01", End_Date="2023-01-01", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Lula da Silva",
    Trip_Objective="Asistencia a la investidura presidencial.",
    Source_Verification="https://www.elpais.com.uy/informacion/politica/asumio-lula-da-silva-en-brasil-y-lacalle-pou-lo-invito-a-visitar-uruguay-a-fines-de-enero",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-LLP-J014", Trip_Status="Completed", Start_Date="2023-01-24", End_Date="2023-01-24", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="VII Cumbre CELAC",
    Trip_Objective="Participacion en la Cumbre CELAC.",
    Source_Verification="https://mediospublicos.uy/transmision-en-vivo-lacalle-pou-participa-de-la-cumbre-de-la-celac/",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-LLP-J015", Trip_Status="Completed", Start_Date="2023-03-24", End_Date="2023-03-25", Duration_Days=2,
    Destination_Country="Dominican Republic", Destination_City="Santo Domingo", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XXVIII Cumbre Iberoamericana",
    Trip_Objective="Cumbre; reuniones con Boric y el Rey Felipe VI.",
    Source_Verification="https://www.teledoce.com/telemundo/nacionales/lacalle-en-republica-dominicana-se-reunio-con-boric-y-hablaron-del-mundial-2030-tambien-se-encontro-con-el-rey-felipe-vi/",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-LLP-J016", Trip_Status="Completed", Start_Date="2023-05-30", End_Date="2023-05-30", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasilia", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre de presidentes sudamericanos",
    Trip_Objective="Reunion de presidentes de America del Sur.",
    Source_Verification="https://www.elobservador.com.uy/nota/gobierno-vuelve-de-brasil-satisfecho-por-cumbre-que-termino-con-una-declaracion-aceptable--20235302170",
    Source_Reliability="Medium", Tema_Foro="Cooperación Política General")

add("URU-LLP-J017", Trip_Status="Completed", Start_Date="2023-06-12", End_Date="2023-06-13", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York / Washington", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Council of the Americas / Joe Biden",
    Trip_Objective="Recibe insignia AS/COA; Biden lo recibio en la Casa Blanca.",
    Source_Verification="https://www.teledoce.com/telemundo/nacionales/biden-aplaudio-defensa-de-lacalle-de-libertades-en-venezuela-presidentes-exploraron-formas-de-expandir-la-relacion-economica-bilateral/",
    Source_Reliability="High", Methodological_Notes="Journey multi-ciudad (NY + Washington); fechas estimadas.")

add("URU-LLP-J018", Trip_Status="Completed", Start_Date="2023-07-03", End_Date="2023-07-04", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Puerto Iguazú", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre de presidentes del MERCOSUR",
    Trip_Objective="Cumbre semestral del MERCOSUR.",
    Source_Verification="https://www.elobservador.com.uy/nota/lacalle-pou-viajara-este-lunes-a-argentina-para-una-nueva-cumbre-del-mercosur-202372173046",
    Source_Reliability="High", Methodological_Notes="Fechas estimadas.", Tema_Foro="Comercio/Integración Económica")

add("URU-LLP-J019", Trip_Status="Completed", Start_Date="2023-07-17", End_Date="2023-07-18", Duration_Days=2,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre CELAC-UE / MERCOSUR-UE",
    Trip_Objective="Impulso al acuerdo MERCOSUR-UE.",
    Source_Verification="https://en.mercopress.com/2023/07/18/lacalle-pou-urges-swift-action-on-eu-mercosur-agreement-enough-of-25-years-of-negotiations",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

add("URU-LLP-J020", Trip_Status="Completed", Start_Date="2023-09-11", End_Date="2023-09-11", Duration_Days=1,
    Destination_Country="Chile", Destination_City="Santiago", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="50º aniversario del golpe de 1973",
    Trip_Objective="Acto conmemorativo invitado por Boric.",
    Source_Verification="https://www.infobae.com/america/agencias/2023/09/17/lacalle-pou-viaja-a-estados-unidos-para-asistir-a-la-asamblea-general-de-la-onu/",
    Source_Reliability="Medium", Tema_Foro="Cooperación Política General")

add("URU-LLP-J021", Trip_Status="Completed", Start_Date="2023-09-14", End_Date="2023-09-14", Duration_Days=1,
    Destination_Country="France", Destination_City="Lille", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Emmanuel Macron",
    Trip_Objective="Bilateral con Macron; debut de Los Teros en el Mundial de rugby.",
    Source_Verification="https://www.elobservador.com.uy/nota/lacalle-pou-viajara-a-francia-a-ver-el-debut-de-los-teros-en-el-mundial-de-rugby-invitado-por-emmanuel-macron-2023831175955",
    Source_Reliability="High", Methodological_Notes="Fecha estimada.")

add("URU-LLP-J022", Trip_Status="Completed", Start_Date="2023-09-17", End_Date="2023-09-21", Duration_Days=5,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="78ª Asamblea General ONU",
    Trip_Objective="Discurso en la AGNU 78.",
    Source_Verification="https://www.elobservador.com.uy/nota/lacalle-pou-viaja-a-nueva-york-para-participar-de-la-cumbre-de-las-naciones-unidas-2023917161254",
    Source_Reliability="High", Methodological_Notes="Fechas estimadas.", Tema_Foro="Cooperación Política General")

add("URU-LLP-J023", Trip_Status="Completed", Start_Date="2023-11-03", End_Date="2023-11-03", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre APEP / Joe Biden",
    Trip_Objective="Cumbre Alianza de las Americas; recibido por Biden en la Casa Blanca.",
    Source_Verification="https://www.elpais.com.uy/informacion/politica/joe-biden-recibio-a-lacalle-pou-en-la-casa-blanca-de-que-temas-hablaran-en-la-cumbre-con-otros-presidentes",
    Source_Reliability="High", Methodological_Notes="Fecha estimada.", Tema_Foro="Comercio/Integración Económica")

add("URU-LLP-J024", Trip_Status="Completed", Start_Date="2023-11-20", End_Date="2023-11-24", Duration_Days=5,
    Destination_Country="China", Destination_City="Beijing", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Xi Jinping",
    Trip_Objective="Mision oficial; asociacion estrategica integral y comercio agroalimentario (TLC).",
    Source_Verification="https://www.subrayado.com.uy/lacalle-pou-llega-china-mision-oficialla-reunion-xi-jinping-y-los-objetivos-comerciales-n931393",
    Source_Reliability="High", Methodological_Notes="Llego a Pekin el 18-nov.")

add("URU-LLP-J025", Trip_Status="Completed", Start_Date="2023-12-10", End_Date="2023-12-10", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Javier Milei",
    Trip_Objective="Asistencia a la investidura presidencial.",
    Source_Verification="https://www.montevideo.com.uy/Noticias/Lacalle-Pou-partio-hacia-Argentina-para-asistir-a-la-asuncion-de-Milei-este-domingo-uc873535",
    Source_Reliability="High", Tema_Foro="Cooperación Política General")

add("URU-LLP-J026", Trip_Status="Completed", Start_Date="2024-04-17", End_Date="2024-04-17", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Bariloche", Visit_Category="Other", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Foro Llao Llao",
    Trip_Objective="Foro empresarial exclusivo.",
    Source_Verification="https://www.elpais.com.uy/mundo/argentina/que-es-el-foro-llao-llao-el-exclusivo-evento-de-empresarios-en-bariloche-en-el-que-participa-lacalle-pou",
    Source_Reliability="High")

add("URU-LLP-J027", Trip_Status="Completed", Start_Date="2024-04-24", End_Date="2024-04-24", Duration_Days=1,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Other", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cena de la Fundación Libertad",
    Trip_Objective="Evento ideologico-empresarial; pidio permiso por motivos personales.",
    Source_Verification="https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Luis_Lacalle_Pou",
    Source_Reliability="Medium", Methodological_Notes="Segundo viaje a Argentina en una semana.")

add("URU-LLP-J028", Trip_Status="Completed", Start_Date="2024-07-07", End_Date="2024-07-08", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="LXIV Cumbre MERCOSUR",
    Trip_Objective="Asume la presidencia pro tempore; reclamo por la ausencia de Milei; cena con Lula y Pena.",
    Source_Verification="https://www.mercosur.int/64-cumbre-comunicado",
    Source_Reliability="High", Tema_Foro="Comercio/Integración Económica")

add("URU-LLP-J029", vs="Solo-Query", Trip_Status="Completed", Start_Date="2024-07-17", End_Date="2024-07-18", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Javier Milei / acto AMIA 30 años",
    Trip_Objective="Reunion en Casa Rosada; acto por el atentado a la AMIA.",
    Source_Verification="https://www.infobae.com/politica/2024/07/17/milei-se-reunira-con-luis-lacalle-pou-tras-la-polemica-por-la-ausencia-del-presidente-a-la-cumbre-del-mercosur/",
    Source_Reliability="Medium", Methodological_Notes="DUDOSO: no en Wikipedia; hallazgo de subagente; dia exacto (17 vs 18) a confirmar.")

add("URU-LLP-J030", Trip_Status="Completed", Start_Date="2024-09-25", End_Date="2024-09-27", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="79ª Asamblea General ONU",
    Trip_Objective="Ultimo viaje del mandato; discurso el jueves 26 y audiencia privada con Guterres.",
    Source_Verification="https://www.gub.uy/presidencia/comunicacion/noticias/presidente-lacalle-pou-regreso-pais-tras-participar-asamblea-general-onu",
    Source_Reliability="High", Methodological_Notes="Ultimo viaje internacional como presidente.", Tema_Foro="Cooperación Política General")

add("URU-LLP-J031", vs="Solo-Query", Trip_Status="Canceled", Start_Date="2021-05-24", End_Date="NA", Duration_Days="NA",
    Destination_Country="Ecuador", Destination_City="Quito", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Guillermo Lasso",
    Trip_Objective="Objetivo: investidura de Lasso. Cancelacion: muerte del ministro del Interior Jorge Larranaga.",
    Source_Verification="Search Query: Lacalle Pou suspende viaje Ecuador Lasso Larranaga mayo 2021",
    Source_Reliability="Low", Methodological_Notes="Destino anunciado y cancelado.", Tema_Foro="Cooperación Política General")

add("URU-LLP-J032", Trip_Status="Canceled", Start_Date="2022-06-07", End_Date="NA", Duration_Days="NA",
    Destination_Country="United States", Destination_City="Los Angeles", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="IX Cumbre de las Américas",
    Trip_Objective="Objetivo: IX Cumbre de las Americas. Cancelacion: positivo de COVID-19; dio discurso virtual; delegacion del canciller Bustillo.",
    Source_Verification="https://www.cronista.com/internacionales/el-presidente-de-uruguay-dio-positivo-de-covid-luis-lacalle-pou-no-viaja-a-la-cumbre-de-las-americas/",
    Source_Reliability="High", Methodological_Notes="Destino anunciado y cancelado; anuncio via Twitter el 6-jun-2022.", Tema_Foro="Cooperación Política General")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
print(f"OK: {len(rows)} filas de {P} anexadas. Ultimo Trip_ID = {tid-1}")
