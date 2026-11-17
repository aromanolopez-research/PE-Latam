# -*- coding: utf-8 -*-
"""
integrate.py — Consolida los módulos de país (ya validados) en la base final única.

Uso:
    python integrate.py

Qué hace:
  1) Recorre 03_MODULOS_PAIS/<pais>/<pais>_viajes.csv
  2) Valida cada módulo (reusa validate.py). Si alguno falla, ABORTA (no integra basura).
  3) Concatena todos en 04_BASE_FINAL/base_consolidada.csv
  4) Re-numera Trip_ID de forma global y secuencial (1..N) preservando Journey_ID.
  5) Imprime un resumen por país y registra la operación en la bitácora.

Sólo integra países cuyo control (QC) dio 0 errores, replicando la regla del proyecto:
"primero se completan y controlan todos los mandatarios de un país; recién ahí se integra".
"""
import csv, sys, os, glob, datetime
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from schema import COLUMNS, MISSING
import validate as V

MODULES_DIR = os.path.join(ROOT, "03_MODULOS_PAIS")
FINAL_CSV   = os.path.join(ROOT, "04_BASE_FINAL", "base_consolidada.csv")
BITACORA    = os.path.join(ROOT, "05_BITACORA", "bitacora.txt")


def log_bitacora(linea):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(BITACORA, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] INTEGRACION | {linea}\n")


def main():
    module_csvs = sorted(glob.glob(os.path.join(MODULES_DIR, "*", "*_viajes.csv")))
    if not module_csvs:
        print("No se encontraron módulos en 03_MODULOS_PAIS/<pais>/<pais>_viajes.csv")
        return 1

    all_rows = []
    resumen = defaultdict(lambda: {"filas": 0, "journeys": set()})

    for path in module_csvs:
        print(f"\n>>> Validando {os.path.relpath(path, ROOT)}")
        rc = V.main(path)
        if rc != 0:
            print(f"ABORTADO: el módulo {path} no pasó el control. Corregir antes de integrar.")
            return 1
        _, rows = V.load_csv(path)
        for r in rows:
            all_rows.append(r)
            pais = r["Origin_Country"]
            resumen[pais]["filas"] += 1
            resumen[pais]["journeys"].add(r["Journey_ID"])

    # re-numerar Trip_ID global
    for i, r in enumerate(all_rows, start=1):
        r["Trip_ID"] = str(i)

    # escribir base consolidada
    os.makedirs(os.path.dirname(FINAL_CSV), exist_ok=True)
    with open(FINAL_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(all_rows)

    # resumen
    print("\n" + "=" * 60)
    print("BASE FINAL CONSOLIDADA")
    print("=" * 60)
    total_filas = len(all_rows)
    total_journeys = len({r["Journey_ID"] for r in all_rows})
    for pais in sorted(resumen):
        d = resumen[pais]
        print(f"  {pais:20} | filas: {d['filas']:4} | viajes físicos: {len(d['journeys']):4}")
    print("-" * 60)
    print(f"  {'TOTAL':20} | filas: {total_filas:4} | viajes físicos: {total_journeys:4}")
    print(f"\nGuardado en: {os.path.relpath(FINAL_CSV, ROOT)}")
    print("=" * 60)

    log_bitacora(f"Base consolidada: {total_filas} filas / {total_journeys} viajes físicos / "
                 f"{len(resumen)} país(es): {', '.join(sorted(resumen))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
