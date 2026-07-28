# -*- coding: utf-8 -*-
"""
corregir_fechas_verificadas.py — Aplica las 4 correcciones de fecha/datos
confirmadas por verificación web directa (2026-07-08). Match por (Journey_ID,
Destination_City) — estable. Idempotente (revierte el estado previo si re-corre).

Correcciones (todas con fuente oficial o prensa contemporánea):
  1) Bachelet-Sarkozy Francia: 2007-05-16 -> 2009-05-29 (llegó 27, almuerzo Elíseo 29).
     Fuentes: Público/El Informador/Panamá América, mayo 2009.
  2) Bachelet-Widodo Indonesia: 2016-05-17 -> 2017-05-12 (llegó 11, bilateral 12).
     Fuentes: Emol 12-05-2017, La Tercera, Archivo Nacional de Chile.
  3) Bachelet-PPK Lima: 2018-01-21 -> 2017-07-07 (llegó 6, I Gabinete Binacional 7).
     Fuente oficial: Declaración de Lima, gob.pe (MRE Perú).
  4) Milei "CPAC Asunción" (viaje INEXISTENTE) -> corregido a su viaje REAL:
     CPAC Brasil en Balneário Camboriú, 2024-07-06/07. NO fue a Asunción (lo
     reemplazó Diana Mondino en la Cumbre Mercosur). Fuentes: PBS, Exame,
     Jovem Pan, Poder360, todas 6-7 julio 2024.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, region_for

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(ROOT, "03_MODULOS_PAIS")

# (pais, Journey_ID, City_actual) -> dict de campos a setear
FIXES = {
    ("chile", "CHL-MB1-J037", "Paris"): {
        "Start_Date": "2009-05-29", "End_Date": "2009-05-29", "Duration_Days": "1",
        "Source_Verification": "https://www.publico.es/actualidad/sarkozy-bachelet-estudian-llevar-cabo-asociacion-dos-paises.html",
        "Source_Reliability": "Medium", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "Fecha CORREGIDA el 2026-07-08 (era 2007-05-16, error de anio): almuerzo con Sarkozy en el Eliseo el 29-05-2009 (llego a Paris el 27). Fuente: Publico/El Informador mayo 2009.",
    },
    ("chile", "CHL-MB2-J090", "Jakarta"): {
        "Start_Date": "2017-05-12", "End_Date": "2017-05-12", "Duration_Days": "1",
        "Source_Verification": "https://www.emol.com/noticias/Nacional/2017/05/12/858024/Chile-e-Indonesia-firman-acuerdo-para-cerrar-negociaciones-del-TLC-entre-ambos-paises-durante-este-ano.html",
        "Source_Reliability": "High", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "Fecha CORREGIDA el 2026-07-08 (era 2016-05-17, error de anio): visita de Estado con Widodo el 12-05-2017 (llego a Yakarta el 11). Fuentes: Emol 12-05-2017, Archivo Nacional de Chile.",
    },
    ("chile", "CHL-MB2-J099", "Lima"): {
        "Start_Date": "2017-07-06", "End_Date": "2017-07-07", "Duration_Days": "2",
        "Source_Verification": "https://www.gob.pe/institucion/rree/noticias/4701-declaracion-de-lima",
        "Source_Reliability": "High", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "Fecha CORREGIDA el 2026-07-08 (era 2018-01-21, error): I Gabinete Binacional Peru-Chile con PPK el 07-07-2017 (llego el 6). Fuente oficial: Declaracion de Lima, gob.pe.",
    },
    ("argentina", "ARG-JM-J181", "Asunción"): {
        "Start_Date": "2024-07-06", "End_Date": "2024-07-07", "Duration_Days": "2",
        "Destination_Country": "Brazil", "Destination_City": "Balneário Camboriú",
        "Destination_Region": "South America",
        "Counterpart_Event": "CPAC Brasil 2024 (Conferência de Ação Política Conservadora)",
        "Trip_Objective": "Cierra la CPAC Brasil junto a Bolsonaro; discurso contra gobiernos socialistas. Desisti de la Cumbre Mercosur de Asuncion (lo reemplazo la canciller Mondino).",
        "Source_Verification": "https://www.pbs.org/newshour/world/argentine-president-milei-snubs-brazils-lula-and-heads-to-cpac-convention-alongside-bolsonaro",
        "Source_Reliability": "High", "Verificacion_Status": "Verificada-URL",
        "Methodological_Notes": "CORREGIDO el 2026-07-08: el registro original (Asuncion/Paraguay, 15-16 jul, CPAC) era ERRONEO. Milei NO fue a Asuncion; su viaje real fue a la CPAC Brasil en Balneario Camboriu (SC) el 6-7 jul 2024. Fuentes: PBS, Exame, Jovem Pan, Poder360.",
        # Tema_Foro se mantiene: CPAC -> Cooperación Política General (doctrina 5.7)
    },
}

def process(pais):
    path = os.path.join(MOD, pais, f"{pais}_viajes.csv")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    n = 0
    for r in rows:
        for (fp, jid, city), fields in FIXES.items():
            if fp == pais and r["Journey_ID"] == jid and r["Destination_City"] == city:
                r.update(fields)
                n += 1
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"{pais}: {n} correcciones aplicadas")

if __name__ == "__main__":
    for p in ("argentina", "brasil", "chile"): process(p)
