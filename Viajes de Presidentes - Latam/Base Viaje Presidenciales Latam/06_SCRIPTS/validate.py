# -*- coding: utf-8 -*-
"""
validate.py — Control de calidad (QC) de un módulo de viajes en formato CSV.

Uso:
    python validate.py <ruta_al_csv>

Chequea:
  - Que estén las 19 columnas en el orden canónico.
  - Dominios de valores (Trip_Status, Region, Category, Subtype, Sideline, Reliability).
  - Coherencia País -> Región (contra REGION_MAP de schema.py).
  - Reglas de duración (NA si Canceled; entero >= 0 si Completed).
  - Sin comas en numéricos. Journey_ID/Trip_ID presentes. Fechas ISO o NA.
  - Coherencia interna de Journey_ID: filas con mismo Journey_ID deben compartir
    President, Origin_Country y Trip_Status.

Imprime un reporte y devuelve código de salida 0 (OK) o 1 (hay errores).
"""
import csv, sys, os
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, validate_row, MISSING


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows = list(reader)
    return header, rows


def main(path):
    if not os.path.exists(path):
        print(f"ERROR: no existe el archivo {path}")
        return 1

    header, rows = load_csv(path)
    errors = []

    # 1) encabezado exacto
    if header != COLUMNS:
        errors.append("Encabezado no coincide con el esquema canónico.")
        errors.append(f"  esperado: {COLUMNS}")
        errors.append(f"  recibido: {header}")
        # no seguimos si el encabezado está mal
        print("\n".join(errors))
        return 1

    # 2) validar fila por fila
    for i, row in enumerate(rows, start=1):
        errors.extend(validate_row(row, idx=i))

    # 2b) filas duplicadas (mismo President + Start_Date + Destination_Country + City + Subtype)
    dup_seen = defaultdict(list)
    for i, row in enumerate(rows, start=1):
        k = (row["President"], row["Start_Date"], row["Destination_Country"],
             row["Destination_City"], row["Visit_Subtype"])
        dup_seen[k].append(row["Trip_ID"])
    for k, ids in dup_seen.items():
        if len(ids) > 1:
            errors.append(f"Fila DUPLICADA (Trip_IDs {ids}): {k[0]} | {k[1]} | "
                          f"{k[2]} {k[3]} | {k[4]}")

    # 3) coherencia de Journey_ID
    by_journey = defaultdict(list)
    for i, row in enumerate(rows, start=1):
        by_journey[row["Journey_ID"]].append((i, row))
    for jid, items in by_journey.items():
        pres = {r["President"] for _, r in items}
        orig = {r["Origin_Country"] for _, r in items}
        stat = {r["Trip_Status"] for _, r in items}
        if len(pres) > 1:
            errors.append(f"[Journey {jid}] mezcla presidentes distintos: {pres}")
        if len(orig) > 1:
            errors.append(f"[Journey {jid}] mezcla paises de origen distintos: {orig}")
        if len(stat) > 1:
            errors.append(f"[Journey {jid}] mezcla estados (Completed/Canceled): {stat}")

    # 4) resumen
    n_rows = len(rows)
    n_journeys = len(by_journey)
    n_completed = sum(1 for r in rows if r["Trip_Status"] == "Completed")
    n_canceled = sum(1 for r in rows if r["Trip_Status"] == "Canceled")
    journeys_completed = len({r["Journey_ID"] for r in rows if r["Trip_Status"] == "Completed"})

    print("=" * 60)
    print(f"QC: {os.path.basename(path)}")
    print("=" * 60)
    print(f"Filas (tramos/país)        : {n_rows}")
    print(f"Viajes físicos (Journey_ID): {n_journeys}  (completados: {journeys_completed})")
    print(f"Tramos Completed / Canceled: {n_completed} / {n_canceled}")
    print("-" * 60)
    if errors:
        print(f"RESULTADO: {len(errors)} PROBLEMA(S) DETECTADO(S)")
        for e in errors:
            print("  - " + e)
        print("=" * 60)
        return 1
    else:
        print("RESULTADO: OK — 0 errores. El módulo cumple el esquema.")
        print("=" * 60)
        return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python validate.py <ruta_al_csv>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
