# -*- coding: utf-8 -*-
"""
limpiar_filas_fantasma.py — Cierre de la campaña de verificación (2026-07-08).
Decisión del usuario: eliminar 3 filas sin sustento y reubicar 1 mal fechada.
Las eliminadas quedan registradas en PENDIENTES_VERIFICACION para rechequeo futuro.

ELIMINA (match por Journey_ID + City):
  1) ARG-CFK-J088 / Havana (2012-01-15): DUPLICADO del tramo Cuba de la gira J094
     (11-12/01/2013, ya cargado como Trip 101). Sin fuente propia.
  2) CHL-RL-J020 / Normandy (2004-06-05): sin evidencia de asistencia de Lagos al 60º
     aniversario del Día D. [DEJAR PARA RECHEQUEO]
  3) CHL-SP1-J060 / Montevideo (2011-03-01): sin evidencia; Mujica asumió en 2010 y en
     marzo 2011 Piñera hizo visita de Estado a España. [DEJAR PARA RECHEQUEO]

REUBICA:
  4) CHL-SP2-J108 / Singapore: la escala NO ocurrió en la gira de abril 2019 (China +
     Corea). El viaje real a Singapur fue en nov-2018 (33ª cumbre ASEAN). Se mueve a
     Journey propio CHL-SP2-J120, fechas 2018-11-12/15, pendiente de URL.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(ROOT, "03_MODULOS_PAIS")

ELIMINAR = {
    ("argentina", "ARG-CFK-J088", "Havana"),
    ("chile", "CHL-RL-J020", "Normandy"),
    ("chile", "CHL-SP1-J060", "Montevideo"),
}

REUBICAR = {
    ("chile", "CHL-SP2-J108", "Singapore"): {
        "Journey_ID": "CHL-SP2-J120",
        "Start_Date": "2018-11-12", "End_Date": "2018-11-15", "Duration_Days": "4",
        "Counterpart_Event": "33ª Cumbre de la ASEAN / Gobierno de Singapur",
        "Trip_Objective": "Visita a Singapur en el marco de la 33a Cumbre de la ASEAN; agenda de comercio e innovacion.",
        "Source_Verification": "Search Query: Pinera Singapur cumbre ASEAN noviembre 2018",
        "Source_Reliability": "Low", "Verificacion_Status": "Solo-Query",
        "Methodological_Notes": ("REUBICADO 2026-07-08: la escala en Singapur NO ocurrio en la gira de abril 2019 "
            "(esa gira fue China 24-28/4 + Corea 29/4). El viaje real a Singapur fue en nov-2018 (33a cumbre ASEAN, "
            "llegada la noche del 12/11 segun BCN). Fechas estimadas; PENDIENTE de URL y de confirmar si compartio "
            "viaje fisico con la APEC de Port Moresby (J104, 17-18/11/2018)."),
    },
}

def process(pais):
    path = os.path.join(MOD, pais, f"{pais}_viajes.csv")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    keep, borradas, reub = [], 0, 0
    for r in rows:
        key = (pais, r["Journey_ID"], r["Destination_City"])
        if key in ELIMINAR:
            borradas += 1
            continue
        if key in REUBICAR:
            r.update(REUBICAR[key]); reub += 1
        keep.append(r)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader()
        for r in keep: w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"{pais}: {borradas} eliminadas | {reub} reubicadas | quedan {len(keep)} filas")

if __name__ == "__main__":
    for p in ("argentina", "brasil", "chile"): process(p)
