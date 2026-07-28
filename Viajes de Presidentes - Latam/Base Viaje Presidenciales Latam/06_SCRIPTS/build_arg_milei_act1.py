# -*- coding: utf-8 -*-
"""
ARGENTINA — Javier Milei, ACTUALIZACION INCREMENTAL 1 (2026-07-07). Corte de base extendido a 2026-07-07.
Diff contra lo cargado: ultima fila previa = Davos (J194, 20-21/1/2026). La re-verificacion (research
2026-07-07, busqueda web activa) confirmo 3 viajes ejecutados abr-jun 2026 + 2 cancelados con destino
anunciado (ventana del corte). Journeys J195-J199; Trip_ID 228-232 (continua max del modulo=227).
BRECHA DETECTADA Y NO CARGADA (anti-alucinacion): feb-mar 2026 sin cobertura verificada; candidatos
nombrados por prensa (Washington/Junta de la Paz feb; Miami/NY mar; Chile/asuncion Kast mar;
Espania-Hungria mar) y Asuncion ene-2026 (firma Mercosur-UE) — registrados en PENDIENTES para
investigacion complementaria. NO se cargan filas sin fuente verificable.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")
P = "Javier Milei"; O = "Argentina"
rows = []; tid = 228

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

add("ARG-JM-J195", Trip_Status="Completed", Start_Date="2026-04-19", End_Date="2026-04-21", Duration_Days=3,
    Destination_Country="Israel", Destination_City="Jerusalem", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Benjamin Netanyahu / Isaac Herzog",
    Trip_Objective="Tercera visita a Israel; firma de los Acuerdos de Isaac; vuelos directos El Al; Medalla Presidencial del Honor; ratifica traslado de embajada.",
    Source_Verification="https://www.argentina.gob.ar/noticias/el-presidente-javier-milei-mantuvo-una-reunion-con-el-primer-ministro-del-estado-de-israel",
    Source_Reliability="High", Methodological_Notes="Encendio antorcha en ceremonia de Yom Haatzmaut. Duracion 19-21/4 extremos incluidos.")

add("ARG-JM-J196", Trip_Status="Completed", Start_Date="2026-05-06", End_Date="2026-05-07", Duration_Days=2,
    Destination_Country="United States", Destination_City="Los Angeles", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="29ª Conferencia Global del Instituto Milken",
    Trip_Objective="Disertacion ante lideres de finanzas y tecnologia; busqueda de inversiones; cuarto viaje a EEUU en 2026.",
    Source_Verification="https://www.infobae.com/politica/2026/05/01/javier-milei-vuelve-a-viajar-a-estados-unidos-participara-de-la-conferencia-global-del-instituto-milken/",
    Source_Reliability="High", Methodological_Notes="Foro empresarial-financiero: tema Comercio (analogo a Davos, doctrina 5.7).",
    Tema_Foro="Comercio/Integración Económica")

add("ARG-JM-J197", Trip_Status="Completed", Start_Date="2026-06-25", End_Date="2026-06-27", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Clase magistral en Universidad CEU San Pablo / empresarios",
    Trip_Objective="Sexta visita a Espania; charla y reuniones con empresarios (Santander, BBVA, Telefonica, Iberia); sin agenda institucional con autoridades.",
    Source_Verification="https://www.infobae.com/politica/2026/06/24/javier-milei-inicia-el-primero-de-tres-viajes-internacionales-e-ira-a-espana-a-dar-una-charla-y-mantener-reuniones-con-empresarios/",
    Source_Reliability="High", Methodological_Notes="Sin encuentros institucionales oficiales.")

add("ARG-JM-J198", Trip_Status="Canceled", Start_Date="2026-06-30", End_Date="NA", Duration_Days="NA",
    Destination_Country="Paraguay", Destination_City="Asunción", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="LXVIII Cumbre del MERCOSUR",
    Trip_Objective="Participar de la Cumbre del MERCOSUR; cancelado por priorizar agenda interna tras crisis de gabinete (salida de Adorni, jura de Santilli).",
    Source_Verification="https://www.infobae.com/politica/2026/07/01/finalmente-javier-milei-no-viajara-a-estados-unidos-por-el-dia-de-la-independencia/",
    Source_Reliability="Medium", Methodological_Notes="Argentina representada por el canciller Quirno.",
    Tema_Foro="Comercio/Integración Económica")

add("ARG-JM-J199", Trip_Status="Canceled", Start_Date="2026-07-04", End_Date="NA", Duration_Days="NA",
    Destination_Country="United States", Destination_City="New York", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Festejos del 250° aniversario de la Independencia de EEUU (Donald Trump)",
    Trip_Objective="Participar de los actos del 4 de julio junto a Trump; cancelado por agenda interna y actos del 9 de julio en Tucuman.",
    Source_Verification="https://www.losandes.com.ar/politica/javier-milei-no-viajara-estados-unidos-los-festejos-del-4-julio-organizados-trump-n5996962",
    Source_Reliability="Medium", Methodological_Notes="Anunciado el 29/5 (Casa Rosada) y cancelado el 1/7; versiones oficiales contradictorias (FUENTE-DEBIL en pendientes).")

with open(CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} (actualizacion 2026-07-07) agregadas. Ultimo Trip_ID = {tid-1}")
