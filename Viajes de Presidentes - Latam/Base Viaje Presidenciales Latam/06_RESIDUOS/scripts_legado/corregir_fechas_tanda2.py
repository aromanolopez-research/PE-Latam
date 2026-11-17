# -*- coding: utf-8 -*-
"""
corregir_fechas_tanda2.py — Segunda tanda de la campaña de verificación (2026-07-08).
Match por (Journey_ID, Destination_City). Idempotente.

APLICA (fuente sólida):
  1) Bachelet-Correa Quito 15-01-2007: VERIFICADO tal cual (agrega URL CIDOB).
  2) Lagos-Megawati Indonesia: 2004-11-18 -> 2004-04-28/29 (error de mes; la APEC de
     la que Chile fue anfitrión fue en Santiago 20-21/11/2004). Fuente: Emol 25-04-2004.
  3) Boric-Trudeau Canadá: 2022-06-05 -> 2022-06-06, ciudad Ottawa (declaración
     conjunta oficial pm.gc.ca fechada 6-jun-2022). Fuente: La Tercera.
  4) CFK-Chávez La Habana: 2012-01-15 -> 2013-01-11/12 (error de año; visita "de luto
     con biblia", almuerzo con los Castro). Fuente: Los Andes 12-01-2013.

NO TOCA (requieren decisión del usuario, quedan marcados con nota):
  - CHL-RL-J020 Normandy (Día D 2004): sin evidencia de asistencia de Lagos.
  - CHL-SP1-J060 Montevideo 1-03-2011: sin evidencia; posible confusión.
  - CHL-SP2-J108 Singapore (abr-2019): la escala no existió; el viaje real a Singapur
    fue en nov-2018 (cumbre ASEAN), aún sin URL propia.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(ROOT, "03_MODULOS_PAIS")

FIXES = {
    ("chile", "CHL-MB1-J035", "Quito"): {
        "Source_Verification": "https://www.cidob.org/lider-politico/rafael-correa-delgado",
        "Source_Reliability": "Medium", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "VERIFICADO 2026-07-08: CIDOB confirma la asistencia presencial de Bachelet a la jura de Correa (Quito, 15-01-2007).",
    },
    ("chile", "CHL-RL-J021", "Jakarta"): {
        "Start_Date": "2004-04-28", "End_Date": "2004-04-29", "Duration_Days": "2",
        "Counterpart_Event": "Megawati Sukarnoputri",
        "Source_Verification": "https://www.emol.com/noticias/nacional/2004/04/25/145881/presidente-lagos-inicia-gira-internacional.html",
        "Source_Reliability": "Medium", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "Fecha CORREGIDA 2026-07-08 (era 2004-11-18, error de mes): la gira Sudafrica-Indonesia-Singapur-NZ fue en abril 2004; reunion con Megawati el 28-29/04. La APEC con Chile anfitrion fue en Santiago el 20-21/11/2004. Fuente: Emol 25-04-2004.",
    },
    ("chile", "CHL-GB-J121", "NA"): {
        "Start_Date": "2022-06-06", "End_Date": "2022-06-06", "Duration_Days": "1",
        "Destination_City": "Ottawa",
        "Source_Verification": "https://www.latercera.com/politica/noticia/boric-y-primer-ministro-de-canada-anuncian-que-defenderan-en-conjunto-la-proteccion-de-los-oceanos-en-la-cumbre-de-las-americas/KOA32R75LZDBDFPFF4UYGN7TVM/",
        "Source_Reliability": "High", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "CORREGIDO 2026-07-08: ciudad confirmada (Ottawa, Parliament Hill) y fecha 06-06-2022 (declaracion conjunta oficial pm.gc.ca). Antes: 2022-06-05, ciudad NA.",
    },
    ("argentina", "ARG-CFK-J088", "Havana"): {
        "Start_Date": "2013-01-11", "End_Date": "2013-01-12", "Duration_Days": "2",
        "Source_Verification": "https://www.losandes.com.ar/article/cristina-estuvo-clinica-dejo-biblia-690721",
        "Source_Reliability": "High", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "Fecha CORREGIDA 2026-07-08 (era 2012-01-15, error de anio): visita a Chavez convaleciente en La Habana el 11-12/01/2013, con almuerzo con Fidel y Raul Castro. Fuente: Los Andes 12-01-2013.",
    },
}

# Marcas de revisión (no se borra nada; se documenta la sospecha)
REVISAR = {
    ("chile", "CHL-RL-J020", "Normandy"):
        "REVISION 2026-07-08: sin evidencia de que Lagos asistiera al 60 aniversario del Dia D (Chile no fue beligerante; no figura entre los asistentes). Candidato a viaje INEXISTENTE. Pendiente decision del usuario.",
    ("chile", "CHL-SP1-J060", "Montevideo"):
        "REVISION 2026-07-08: sin evidencia de viaje a Montevideo el 01-03-2011 (Mujica asumio el 01-03-2010; en marzo 2011 Pinera hizo visita de Estado a Espania). Candidato a viaje INEXISTENTE o error de anio. Pendiente decision.",
    ("chile", "CHL-SP2-J108", "Singapore"):
        "REVISION 2026-07-08: la escala en Singapur NO ocurrio en la gira de abril 2019 (China 24-28/4 + Corea 29/4). El viaje real a Singapur fue en nov-2018 (33a cumbre ASEAN). Candidato a REUBICAR a nov-2018 o eliminar. Pendiente decision.",
}

def process(pais):
    path = os.path.join(MOD, pais, f"{pais}_viajes.csv")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    n = m = 0
    for r in rows:
        for (fp, jid, city), fields in FIXES.items():
            if fp == pais and r["Journey_ID"] == jid and r["Destination_City"] == city:
                r.update(fields); n += 1
        for (fp, jid, city), nota in REVISAR.items():
            if fp == pais and r["Journey_ID"] == jid and r["Destination_City"] == city:
                r["Verificacion_Status"] = "No-verificable"
                base = r["Methodological_Notes"].split(" REVISION 2026-07-08")[0].rstrip(".")
                r["Methodological_Notes"] = (nota if base == "NA" else base + ". " + nota)
                m += 1
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"{pais}: {n} correcciones | {m} marcados para revision")

if __name__ == "__main__":
    for p in ("argentina", "brasil", "chile"): process(p)
