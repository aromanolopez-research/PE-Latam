#!/usr/bin/env python3
"""
colt_export_csv.py
===================
Exporta la hoja "Datos_COLT_Sudamerica" de Base_COLT_Sudamerica.xlsx a un CSV de
trabajo (04_BASE_FINAL/base_colt_sudamerica_trabajo.csv).

Por que existe: a partir del rediseño del 2026-08-24, Base_COLT_Sudamerica.xlsx es el
archivo madre unico del proyecto, pero abrir/escribir un .xlsx de miles de filas con
openpyxl es lento y propenso a errores cuando se hace random-access celda por celda
(nos paso el 2026-08-24 con Uruguay, en el esquema anterior). La decision del usuario
fue: trabajar internamente contra un CSV (rapido, confiable, facil de auditar con
grep/pandas) y exportar/actualizar el .xlsx solo al principio y al final de cada
campaña -no en cada paso intermedio-.

Flujo tipico de una campaña:
    python colt_export_csv.py                     # 1. xlsx -> csv de trabajo
    python colt_generar_workpacks.py <Pais> ...    # 2. arma workpacks desde el csv
    ... (investigacion con subagentes) ...
    python colt_aplicar_workpacks.py <Pais> ...    # 3. aplica resultados AL CSV
    python colt_validar_madre.py                   # 4. QC sobre el csv
    python colt_importar_csv.py                    # 5. csv -> xlsx (vuelca a la hoja madre)

Este script es de solo lectura sobre el .xlsx.
"""
import csv
from pathlib import Path

import openpyxl

import re

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
XLSX_PATH = PROJECT_ROOT / "04_BASE_FINAL" / "Base_COLT_Sudamerica.xlsx"
SHEET_NAME = "Datos_COLT_Sudamerica"
CSV_TRABAJO = PROJECT_ROOT / "04_BASE_FINAL" / "base_colt_sudamerica_trabajo.csv"

_FECHA_CON_HORA_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})T00:00:00$")


def main():
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    ws = wb[SHEET_NAME]
    headers = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]

    n = 0
    with open(CSV_TRABAJO, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for row in ws.iter_rows(min_row=2, values_only=True):
            # Las fechas vienen como datetime en el xlsx; el csv de trabajo las guarda
            # como texto ISO (YYYY-MM-DD) para que sea texto plano portable.
            fila = []
            for v in row:
                if hasattr(v, "date") and not isinstance(v, str):
                    fila.append(v.date().isoformat())
                elif isinstance(v, str) and _FECHA_CON_HORA_RE.match(v):
                    # Muchas celdas de fecha de la hoja madre quedaron guardadas como
                    # TEXTO con hora "T00:00:00" pegada (arrastrado de reparaciones
                    # anteriores que usaron str(datetime) en vez de .date().isoformat()).
                    # Se limpia aca, asi el csv de trabajo queda con fecha simple
                    # YYYY-MM-DD y, al reimportar con colt_importar_csv.py, la celda
                    # vuelve a quedar tipada como fecha real en el xlsx.
                    fila.append(_FECHA_CON_HORA_RE.match(v).group(1))
                else:
                    fila.append(v if v is not None else "")
            w.writerow(fila)
            n += 1

    print(f"Exportado: {n} filas -> {CSV_TRABAJO}")


if __name__ == "__main__":
    main()
