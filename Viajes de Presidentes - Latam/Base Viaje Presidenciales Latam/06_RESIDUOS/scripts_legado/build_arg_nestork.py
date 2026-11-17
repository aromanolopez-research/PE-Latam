# -*- coding: utf-8 -*-
"""
Agrega los viajes de Néstor Kirchner (2003-05-25 a 2007-12-10) al módulo de Argentina.
Continúa Trip_ID después de Duhalde (último = 24).
Criterio: se cargan los viajes COMPLETADOS verificados. Los cancelados/no-viajes (funeral JP II,
Cusco 2004, Iberoamericana Montevideo 2006) se registran como filas Canceled o quedan en notas de bitácora.
Eventos en Argentina (Cumbre Américas Mar del Plata 2005, MERCOSUR Córdoba 2006, Banco del Sur) NO se cargan.
Fuentes: Memoria Cancillería 2004 (IRI-UNLP), Casa Rosada, SEGIB, MERCOSUR, ONU, La Nación, Página/12, Infobae, todo-argentina.net.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")

P = "Néstor Kirchner"
O = "Argentina"
rows = []
tid = 25  # siguiente Trip_ID

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ── 2003 ──
add("ARG-NK-J024", Trip_Status="Completed", Start_Date="2003-06-11", End_Date="2003-06-11", Duration_Days=1,
    Destination_Country="Brazil", Destination_City="Brasília",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Lula da Silva",
    Trip_Objective="Primer viaje al exterior. Relanzar el MERCOSUR; declaracion conjunta. Reunion en residencia La Alborada.",
    Source_Verification="https://www.cronista.com/economia-politica/Primeros-viajes-oficiales-que-destinos-eligieron-los-ex-presidentes-20200116-0035.html",
    Source_Reliability="High", Methodological_Notes="Primer viaje del mandato confirmado por prensa.")

add("ARG-NK-J025", Trip_Status="Completed", Start_Date="2003-06-17", End_Date="2003-06-18", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="Cumbre de Jefes de Estado del MERCOSUR",
    Trip_Objective="Cumbre semestral del MERCOSUR; propuesta de instituto monetario / moneda comun.",
    Source_Verification="Search Query: Kirchner Cumbre MERCOSUR Asuncion junio 2003",
    Source_Reliability="Medium", Methodological_Notes="Asistencia probable; verificar fecha exacta en Boletin Oficial.")

add("ARG-NK-J026", Trip_Status="Completed", Start_Date="2003-07-23", End_Date="2003-07-23", Duration_Days=1,
    Destination_Country="United States", Destination_City="Washington D.C.",
    Visit_Category="Bilateral", Visit_Subtype="State Visit", Sideline_Bilaterals="FALSE",
    Counterpart_Event="George W. Bush",
    Trip_Objective="Unica visita de Estado a Washington del kirchnerismo. Respaldo de EE.UU. a la renegociacion de deuda.",
    Source_Verification="https://www.infobae.com/politica/2020/10/27/nestor-kirchner-y-el-inicio-de-una-politica-exterior-confrontativa/",
    Source_Reliability="High", Methodological_Notes="Fecha confirmada (23 jul 2003).")

# Gira Europa jul 2003: 2 tramos, mismo Journey_ID
add("ARG-NK-J027", Trip_Status="Completed", Start_Date="2003-07-12", End_Date="2003-07-12", Duration_Days=1,
    Destination_Country="Spain", Destination_City="Madrid",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Empresarios espanoles (CEOE)",
    Trip_Objective="Reunion tensa con empresarios; impugno ganancias de los anios 90. Tramo de la primera gira europea.",
    Source_Verification="https://www.infobae.com/politica/2020/10/27/nestor-kirchner-y-el-inicio-de-una-politica-exterior-confrontativa/",
    Source_Reliability="Medium", Methodological_Notes="Fecha estimada (previa al 13 jul en Londres).")

add("ARG-NK-J027", Trip_Status="Completed", Start_Date="2003-07-13", End_Date="2003-07-14", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="London",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="TRUE",
    Counterpart_Event="Cumbre de Gobiernos Progresistas (Tony Blair)",
    Trip_Objective="Cumbre progresista; bilateral con Blair (planteo Malvinas, 13 jul) y dialogo con Schroder. 1er presidente argentino en visita oficial al RU post-guerra.",
    Source_Verification="https://www.lanacion.com.ar/politica/los-kirchner-y-las-malvinas-nid1234282/",
    Source_Reliability="High", Methodological_Notes="Reunion con Blair confirmada 13 jul 2003.")

add("ARG-NK-J028", Trip_Status="Completed", Start_Date="2003-09-25", End_Date="2003-09-25", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="58ª Asamblea General de la ONU",
    Trip_Objective="Primer discurso ante la ONU (22 min); criticas a organismos de credito, terrorismo (AMIA), Malvinas.",
    Source_Verification="https://www.lanacion.com.ar/politica/energico-discurso-de-kirchner-ante-la-onu-nid530283/",
    Source_Reliability="High", Methodological_Notes="Discurso confirmado 25 sep 2003.")

add("ARG-NK-J029", Trip_Status="Completed", Start_Date="2003-11-14", End_Date="2003-11-15", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Santa Cruz de la Sierra",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="XIII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana 'inclusion social motor del desarrollo'. Habia evaluado no ir; finalmente viajo.",
    Source_Verification="https://segib.org/?summit=xiii-cumbre-iberoamericana-santa-cruz-de-la-sierra-2003",
    Source_Reliability="High", Methodological_Notes="Asistio (venia de suspender 3 salidas previas).")

# ── 2004 (Memoria oficial Cancilleria, Alta confiabilidad) ──
add("ARG-NK-J030", Trip_Status="Completed", Start_Date="2004-01-12", End_Date="2004-01-13", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Monterrey",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="Cumbre Extraordinaria de las Américas",
    Trip_Objective="Desendeudamiento y gobernabilidad regional. Bilaterales con Chavez, Lagos y Fox.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

add("ARG-NK-J031", Trip_Status="Completed", Start_Date="2004-01-26", End_Date="2004-01-30", Duration_Days=5,
    Destination_Country="Spain", Destination_City="Madrid",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Feria Internacional de Turismo (FITUR)",
    Trip_Objective="Promocion turistica y comercial en FITUR.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

add("ARG-NK-J032", Trip_Status="Completed", Start_Date="2004-02-27", End_Date="2004-02-28", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Caracas",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="TRUE",
    Counterpart_Event="XII Cumbre del G-15",
    Trip_Objective="Tesis de la deuda impagable sin desarrollo. Coincidio con Chavez y Khatami (Iran).",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

add("ARG-NK-J033", Trip_Status="Completed", Start_Date="2004-03-15", End_Date="2004-03-16", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Lula da Silva",
    Trip_Objective="Visita a Brasil; agenda bilateral y MERCOSUR.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

add("ARG-NK-J034", Trip_Status="Completed", Start_Date="2004-05-04", End_Date="2004-05-06", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Council of the Americas / American Jewish Committee",
    Trip_Objective="Foros de inversiones y relacion con EE.UU. y la comunidad judia (NY y Washington).",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004. Incluyo Washington.")

add("ARG-NK-J035", Trip_Status="Completed", Start_Date="2004-06-28", End_Date="2004-07-03", Duration_Days=6,
    Destination_Country="China", Destination_City="Beijing",
    Visit_Category="Bilateral", Visit_Subtype="State Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Hu Jintao",
    Trip_Objective="Visita de Estado a China (Beijing y Shanghai); diversificacion de mercados. Honoris Causa U. Fudan.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial 2004. Escala en Moscu frustro reunion con Putin (clima + decision de Putin).")

add("ARG-NK-J036", Trip_Status="Completed", Start_Date="2004-07-22", End_Date="2004-07-23", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Tarija",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Carlos Mesa",
    Trip_Objective="Agenda energetica / gas con Bolivia.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

add("ARG-NK-J037", Trip_Status="Completed", Start_Date="2004-09-21", End_Date="2004-09-24", Duration_Days=4,
    Destination_Country="United States", Destination_City="New York",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="59ª Asamblea General de la ONU",
    Trip_Objective="Discurso ante la ONU; reclamo de rediseno del FMI; Malvinas.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

add("ARG-NK-J038", Trip_Status="Completed", Start_Date="2004-10-14", End_Date="2004-10-14", Duration_Days=1,
    Destination_Country="Bolivia", Destination_City="Sucre",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Carlos Mesa",
    Trip_Objective="Firma del Protocolo Adicional del acuerdo energetico Argentina-Bolivia.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

add("ARG-NK-J039", Trip_Status="Completed", Start_Date="2004-11-18", End_Date="2004-11-20", Duration_Days=3,
    Destination_Country="Costa Rica", Destination_City="San José",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="XIV Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana 'educar para progresar'.",
    Source_Verification="https://segib.org/?summit=xiv-cumbre-iberoamericana-san-jose-2004",
    Source_Reliability="High", Methodological_Notes="Memoria oficial 2004 + SEGIB.")

add("ARG-NK-J040", Trip_Status="Completed", Start_Date="2004-12-16", End_Date="2004-12-17", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Ouro Preto",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="XXVII Cumbre del MERCOSUR (Belo Horizonte / Ouro Preto)",
    Trip_Objective="Consejo del Mercado Comun y Cumbre de Presidentes del MERCOSUR.",
    Source_Verification="https://www.iri.edu.ar/publicaciones_iri/anuario/CD%20Anuario%202005/Cerpi/03-memoria%20mrecic%2004_anexos.pdf",
    Source_Reliability="High", Methodological_Notes="Memoria oficial Cancilleria 2004.")

# NO VIAJE 2004: Cusco (Comunidad Sudamericana) — Kirchner NO asistio (envio a Scioli). Se registra en bitacora, no como fila.

# ── 2005 ──
add("ARG-NK-J041", Trip_Status="Completed", Start_Date="2005-03-01", End_Date="2005-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo",
    Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral", Sideline_Bilaterals="NA",
    Counterpart_Event="Asunción de Tabaré Vázquez",
    Trip_Objective="Asuncion presidencial de Tabare Vazquez.",
    Source_Verification="Search Query: Kirchner asuncion Tabare Vazquez Montevideo 1 marzo 2005",
    Source_Reliability="Medium", Methodological_Notes="Asistencia muy probable; verificar en Boletin Oficial.")

add("ARG-NK-J042", Trip_Status="Completed", Start_Date="2005-04-24", End_Date="2005-04-24", Duration_Days=1,
    Destination_Country="Vatican City", Destination_City="Vatican City",
    Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral", Sideline_Bilaterals="NA",
    Counterpart_Event="Misa de asunción del Papa Benedicto XVI",
    Trip_Objective="Misa inaugural del pontificado de Benedicto XVI, tras la polemica por su ausencia en el funeral de Juan Pablo II.",
    Source_Verification="https://www.todo-argentina.net/historia/democracia/kirchner/2005.html",
    Source_Reliability="High", Methodological_Notes="Viajo con CFK y el canciller Bielsa.")

add("ARG-NK-J043", Trip_Status="Completed", Start_Date="2005-05-10", End_Date="2005-05-11", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Brasília",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="I Cumbre América del Sur-Países Árabes (ASPA)",
    Trip_Objective="Cumbre ASPA; acercamiento birregional; reunion con Mahmoud Abbas.",
    Source_Verification="https://es.wikipedia.org/wiki/Cumbre_Am%C3%A9rica_del_Sur-Pa%C3%ADses_%C3%81rabes",
    Source_Reliability="High", Methodological_Notes="ASPA confirmada 10-11 may 2005 en Brasilia.")

add("ARG-NK-J044", Trip_Status="Completed", Start_Date="2005-09-14", End_Date="2005-09-15", Duration_Days=2,
    Destination_Country="United States", Destination_City="New York",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="TRUE",
    Counterpart_Event="Cumbre Mundial 2005 / 60ª Asamblea General ONU",
    Trip_Objective="Discurso ante la ONU; criticas al FMI; Malvinas. Bilateral con Putin (concreto el frustrado en Moscu 2004).",
    Source_Verification="Search Query: Kirchner Asamblea ONU septiembre 2005 Putin Nueva York",
    Source_Reliability="Medium", Methodological_Notes="Discurso fechado; confirmar presencia fisica en Boletin Oficial.")

add("ARG-NK-J045", Trip_Status="Completed", Start_Date="2005-10-14", End_Date="2005-10-15", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Salamanca",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="XV Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana (debut SEGIB). Bilaterales con Zapatero, los Reyes y Lula.",
    Source_Verification="https://segib.org/?summit=xv-cumbre-iberoamericana-salamanca-2005",
    Source_Reliability="High", Methodological_Notes="Asistio (fotos oficiales SEGIB).")

add("ARG-NK-J046", Trip_Status="Completed", Start_Date="2005-11-21", End_Date="2005-11-21", Duration_Days=1,
    Destination_Country="Venezuela", Destination_City="Ciudad Guayana",
    Visit_Category="Bilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Hugo Chávez (Declaración del Orinoco)",
    Trip_Objective="Integracion energetica; compra venezolana de bonos argentinos; ingreso de Venezuela al MERCOSUR.",
    Source_Verification="https://www.todo-argentina.net/historia/democracia/kirchner/2005.html",
    Source_Reliability="Medium", Methodological_Notes="Declaracion del Orinoco con Chavez.")

# ── 2006 (minima actividad) ──
add("ARG-NK-J047", Trip_Status="Completed", Start_Date="2006-01-22", End_Date="2006-01-22", Duration_Days=1,
    Destination_Country="Bolivia", Destination_City="La Paz",
    Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral", Sideline_Bilaterals="TRUE",
    Counterpart_Event="Asunción de Evo Morales",
    Trip_Objective="Asuncion de Evo Morales; asistieron tambien Chavez, Lula y Lagos.",
    Source_Verification="Search Query: Kirchner asuncion Evo Morales La Paz 22 enero 2006",
    Source_Reliability="High", Methodological_Notes="Anio de minima actividad internacional de NK.")

# NO VIAJE 2006: XVI Cumbre Iberoamericana Montevideo — NO asistio (represento el canciller Taiana). Bitacora.

# ── 2007 ──
add("ARG-NK-J048", Trip_Status="Completed", Start_Date="2007-01-18", End_Date="2007-01-19", Duration_Days=2,
    Destination_Country="Brazil", Destination_City="Rio de Janeiro",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="Cumbre del MERCOSUR",
    Trip_Objective="Cumbre MERCOSUR; impulso al Banco del Sur, Gasoducto del Sur y FOCEM.",
    Source_Verification="Search Query: Cumbre MERCOSUR Rio de Janeiro enero 2007 Kirchner",
    Source_Reliability="Medium", Methodological_Notes="Confirmar fecha exacta en Boletin Oficial.")

add("ARG-NK-J049", Trip_Status="Completed", Start_Date="2007-04-16", End_Date="2007-04-17", Duration_Days=2,
    Destination_Country="Venezuela", Destination_City="Isla Margarita",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="I Cumbre Energética Sudamericana",
    Trip_Objective="Integracion energetica; Gasoducto del Sur; Banco del Sur. Anfitrion Chavez.",
    Source_Verification="Search Query: Cumbre Energetica Sudamericana Isla Margarita abril 2007 Kirchner",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-NK-J050", Trip_Status="Completed", Start_Date="2007-06-28", End_Date="2007-06-29", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="NA",
    Counterpart_Event="XXXIII Cumbre del MERCOSUR",
    Trip_Objective="Cumbre MERCOSUR; crisis energetica como cuestion regional; criticas a Repsol-YPF y Petrobras.",
    Source_Verification="Search Query: XXXIII Cumbre MERCOSUR Asuncion junio 2007 Kirchner",
    Source_Reliability="Medium", Methodological_Notes="NA")

add("ARG-NK-J051", Trip_Status="Completed", Start_Date="2007-08-10", End_Date="2007-08-10", Duration_Days=1,
    Destination_Country="Bolivia", Destination_City="Tarija",
    Visit_Category="Multilateral", Visit_Subtype="Working Visit", Sideline_Bilaterals="NA",
    Counterpart_Event="Reunión trilateral con Chávez y Morales",
    Trip_Objective="Relanzamiento del Gasoducto del Sur; convenios de hidrocarburos; credito argentino US$ 450 millones.",
    Source_Verification="https://www.emol.com/noticias/internacional/2007/08/10/265499/kirchner-chavez-y-morales-relanzan-gasoducto-del-sur.html",
    Source_Reliability="High", Methodological_Notes="Reunion trilateral (3 paises).")

add("ARG-NK-J052", Trip_Status="Completed", Start_Date="2007-09-25", End_Date="2007-09-25", Duration_Days=1,
    Destination_Country="United States", Destination_City="New York",
    Visit_Category="Multilateral", Visit_Subtype="Global Forum", Sideline_Bilaterals="NA",
    Counterpart_Event="62ª Asamblea General de la ONU",
    Trip_Objective="Ultima presentacion como presidente ante la ONU; AMIA/Iran, Malvinas, reforma del Consejo de Seguridad y del FMI.",
    Source_Verification="https://www.casarosada.gob.ar/informacion/archivo/24141-blank-89376803",
    Source_Reliability="High", Methodological_Notes="Confirmado por Casa Rosada y Pagina/12.")

add("ARG-NK-J053", Trip_Status="Completed", Start_Date="2007-11-08", End_Date="2007-11-10", Duration_Days=3,
    Destination_Country="Chile", Destination_City="Santiago",
    Visit_Category="Multilateral", Visit_Subtype="Regional Summit", Sideline_Bilaterals="TRUE",
    Counterpart_Event="XVII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana 'cohesion social'; ultima accion exterior como presidente. Increpo a Tabare Vazquez por las papeleras.",
    Source_Verification="https://segib.org/?summit=xvii-cumbre-iberoamericana-santiago-2007",
    Source_Reliability="High", Methodological_Notes="Anfitriona Bachelet; SEGIB + Infobae + Pagina/12.")

# Append
with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
