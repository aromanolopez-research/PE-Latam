# -*- coding: utf-8 -*-
"""
CHILE — Jose Antonio Kast (asumido 11/3/2026; corte de base 2026-07-07). Septimo bloque chileno. MANDATO EN CURSO.
Continua Trip_ID tras Boric (ultimo=185). Journey continua en CHL-JAK-J152.
Modo research (2026-07-07, busqueda web activa — eventos posteriores al limite de conocimiento del modelo):
2 viajes fisicos (3 filas pais). Asuncion verificada: gano balotaje 14/12/2025 (58,16% Servel) y asumio 11/3/2026.
Perfil inicial: moderado y estrictamente sudamericano ("gobierno de emergencia" centrado en seguridad/migracion).
Mantuvo la tradicion chilena del primer viaje a Argentina (afinidad ideologica con Milei).
Excluido: viaje a Miami "Escudo de las Americas" (5-7/3/2026), PRE-asuncion.
CORRECCION vs informe research: Duration_Days recalculadas con regla "extremos incluidos" (CODEBOOK):
Argentina 5-6/4 = 2 dias (informe decia 1); Paraguay 29-30/6 = 2 dias (informe decia 1).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "chile", "chile_viajes.csv")
P = "José Antonio Kast"; O = "Chile"
rows = []; tid = 186

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

add("CHL-JAK-J152", Trip_Status="Completed", Start_Date="2026-04-05", End_Date="2026-04-06", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Javier Milei",
    Trip_Objective="Primer viaje internacional; comercio, energia, seguridad, mineria e integracion fronteriza; apoyo a soberania argentina sobre Malvinas.",
    Source_Verification="https://www.gob.cl/noticias/presidente-jose-antonio-kast-realiza-primer-viaje-internacional-reunion-trabajo-presidente-argentina-javier-milei/",
    Source_Reliability="High", Methodological_Notes="Llego la noche del 5/4; actividades el 6/4. Duracion recalculada (extremos incluidos).")

add("CHL-JAK-J153", Trip_Status="Completed", Start_Date="2026-06-29", End_Date="2026-06-30", Duration_Days=2,
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="LXVIII Cumbre del MERCOSUR",
    Trip_Objective="Debut en cumbre regional; lucha coordinada contra el crimen organizado y comercio seguro; bilaterales con Penia, Lula y el canciller aleman Wadephul.",
    Source_Verification="https://prensa.presidencia.cl/fotonoticia.aspx?id=333191",
    Source_Reliability="High", Methodological_Notes="Gira Paraguay-Uruguay (J153). Duracion recalculada (extremos incluidos).",
    Tema_Foro="Comercio/Integración Económica")

add("CHL-JAK-J153", Trip_Status="Completed", Start_Date="2026-07-01", End_Date="2026-07-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Yamandú Orsi",
    Trip_Objective="Visita oficial; firma de dos acuerdos (firma digital; MOU Instituto Artigas-Academia Andres Bello); invitacion al Compromiso de Santiago.",
    Source_Verification="https://prensa.presidencia.cl/fotonoticia.aspx?id=333293",
    Source_Reliability="High", Methodological_Notes="Segunda etapa de J153; confirmar pernocte entre Paraguay y Uruguay (pendientes).")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} agregadas. Ultimo Trip_ID = {tid-1}")
