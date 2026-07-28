# -*- coding: utf-8 -*-
"""
build_module_template.py — PLANTILLA para construir el módulo de viajes de UN mandatario.

Patrón de uso (se copia este archivo por país y se va agregando mandatario por mandatario):
  1) Definir las filas con new_row(...). Una fila por PAÍS de destino.
  2) Las filas de una misma salida física comparten el mismo Journey_ID.
  3) Duration_Days = días en ESE país (NA si Canceled).
  4) La región se completa sola desde Destination_Country (no hace falta escribirla).
  5) Guardar como 03_MODULOS_PAIS/<pais>/<pais>_viajes.csv (acumulando todos los mandatarios del país).
  6) Correr:  python validate.py <csv>   -> debe dar 0 errores.

Convención de Journey_ID:  {COD_PAIS}-{COD_PRESIDENTE}-J{NNN}
  Ej.: ARG-DLR-J001  (Argentina, De la Rúa, viaje físico 001)
Convención de Trip_ID: entero secuencial; al integrar se renumera global, así que
  dentro del módulo basta con que sea único y creciente.

Este archivo incluye 2 filas de EJEMPLO reales (De la Rúa) sólo para ilustrar el formato.
Al trabajar en serio, se reemplazan/expanden con la investigación completa del mandatario.
"""
import csv, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

# ──────────────────────────────────────────────────────────────────────────
# EJEMPLO: Fernando de la Rúa (Argentina). SOLO ilustrativo del formato.
# ──────────────────────────────────────────────────────────────────────────
rows = []

# --- Viaje físico J001: visita de trabajo a EE.UU. (un solo país => 1 fila) ---
rows.append(new_row(
    Journey_ID="ARG-DLR-J001",
    Trip_ID=1,
    President="Fernando de la Rúa",
    Origin_Country="Argentina",
    Trip_Status="Completed",
    Start_Date="2000-06-12",
    End_Date="2000-06-13",
    Duration_Days=2,
    Destination_Country="United States",   # la región (North America) se completa sola
    Destination_City="Washington D.C.",
    Visit_Category="Bilateral",
    Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA",
    Counterpart_Event="Bill Clinton",
    Trip_Objective="Visita de trabajo a la Casa Blanca; agenda economica y relacion bilateral.",
    Source_Verification="Search Query: De la Rua visita Clinton Washington junio 2000",
    Source_Reliability="Medium",
    Methodological_Notes="Fecha verificada con prensa; ejemplo ilustrativo de la plantilla.",
))

# --- Viaje físico J002: gira de 2 países => 2 filas con el MISMO Journey_ID ---
rows.append(new_row(
    Journey_ID="ARG-DLR-J002",
    Trip_ID=2,
    President="Fernando de la Rúa",
    Origin_Country="Argentina",
    Trip_Status="Completed",
    Start_Date="2000-06-25",
    End_Date="2000-06-26",
    Duration_Days=2,
    Destination_Country="Germany",
    Destination_City="Berlin",
    Visit_Category="Bilateral",
    Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA",
    Counterpart_Event="Gerhard Schroder",
    Trip_Objective="Tramo 1 de gira europea (ejemplo). Agenda de inversiones.",
    Source_Verification="Search Query: De la Rua Berlin junio 2000",
    Source_Reliability="Low",
    Methodological_Notes="EJEMPLO ilustrativo; verificar fechas reales al trabajar el mandatario.",
))

# ──────────────────────────────────────────────────────────────────────────
# GUARDAR
# ──────────────────────────────────────────────────────────────────────────
def save(rows, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    print(f"OK: {len(rows)} filas escritas en {out_path}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "03_MODULOS_PAIS", "argentina", "_EJEMPLO_formato.csv")
    save(rows, out)
    print("Esto es solo un EJEMPLO de formato. Correr validate.py para verlo pasar el QC.")
