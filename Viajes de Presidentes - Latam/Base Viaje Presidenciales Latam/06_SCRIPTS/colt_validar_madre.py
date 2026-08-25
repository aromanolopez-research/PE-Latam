#!/usr/bin/env python3
"""
colt_validar_madre.py
=======================
QC liviano sobre 04_BASE_FINAL/base_colt_sudamerica_trabajo.csv (el CSV de trabajo del
archivo madre). Se corre DESPUES de colt_aplicar_workpacks.py y ANTES de
colt_importar_csv.py -si esto no da 0 errores, no volcar al xlsx-.

No reimplementa el validate.py del esquema anterior (ese valida columnas propias como
Visit_Category que ya no se usan). Este script chequea lo minimo indispensable para que
el archivo madre quede sano:
  - TripID unico (ni duplicado con otro TripID de COLT ni con otra fila PELATAM).
  - TripID con formato reconocido (el de COLT, o "PELATAM-<ISO3>-<n>").
  - TripStartDate <= TripEndDate cuando ambos estan presentes.
  - TripDuration entero positivo cuando esta presente.
  - Los 7 campos booleanos de micro-conducta solo pueden ser "Yes", "No" o blanco.
  - Filas PELATAM tienen LeaderID, CountryVisited y TripStartDate (lo minimo para que
    la fila sea usable en un analisis).

USO
---
    python colt_validar_madre.py
"""
import csv
import re
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
CSV_TRABAJO = PROJECT_ROOT / "04_BASE_FINAL" / "base_colt_sudamerica_trabajo.csv"

CAMPOS_YESNO = ["MetHostHoGS", "AttendedMultilatEvent", "AttendedMultilatMinisterialEvent",
                "MetNonhostHOGS", "PublicAddress", "SignedAgreement",
                "CulturalSiteOrCeremony", "BusinessLeaderOrForum", "MetIGOLeader"]

TRIPID_COLT_RE = re.compile(r"^\d+-[A-Z]{2,4}-[A-Z]{2,4}-\d+$")
TRIPID_PELATAM_RE = re.compile(r"^PELATAM-[A-Z]+-\d+$")


def parsear_fecha(s):
    if not s:
        return None
    try:
        y, m, d = (int(x) for x in str(s)[:10].split("-"))
        return date(y, m, d)
    except Exception:
        return "INVALIDA"


def main():
    with open(CSV_TRABAJO, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    errores = []
    vistos = {}

    for i, r in enumerate(rows, start=2):  # fila 1 = encabezado
        tid = r.get("TripID", "")
        if not tid:
            errores.append(f"[fila {i}] TripID vacio")
            continue
        if tid in vistos:
            errores.append(f"[fila {i}] TripID duplicado: '{tid}' (ya visto en fila {vistos[tid]})")
        vistos[tid] = i

        es_pelatam = tid.startswith("PELATAM-")
        if es_pelatam:
            if not TRIPID_PELATAM_RE.match(tid):
                errores.append(f"[fila {i}] TripID PELATAM con formato invalido: '{tid}' (esperado PELATAM-<ISO3>-<n>)")
            for campo in ["LeaderID", "CountryVisited", "TripStartDate"]:
                if not r.get(campo):
                    errores.append(f"[fila {i}] fila PELATAM sin {campo} (TripID {tid})")
        else:
            if not TRIPID_COLT_RE.match(tid):
                errores.append(f"[fila {i}] AVISO: TripID no matchea el formato tipico de COLT ni de PELATAM: '{tid}' (revisar a mano, puede ser un formato de COLT no visto antes)")

        start = parsear_fecha(r.get("TripStartDate"))
        end = parsear_fecha(r.get("TripEndDate"))
        if start == "INVALIDA":
            errores.append(f"[fila {i}] TripStartDate invalida: '{r.get('TripStartDate')}' (TripID {tid})")
        if end == "INVALIDA":
            errores.append(f"[fila {i}] TripEndDate invalida: '{r.get('TripEndDate')}' (TripID {tid})")
        if isinstance(start, date) and isinstance(end, date) and end < start:
            errores.append(f"[fila {i}] TripEndDate anterior a TripStartDate (TripID {tid})")

        dur = r.get("TripDuration")
        if dur:
            try:
                if int(float(dur)) <= 0:
                    errores.append(f"[fila {i}] TripDuration no positivo: '{dur}' (TripID {tid})")
            except (ValueError, TypeError):
                errores.append(f"[fila {i}] TripDuration no numerico: '{dur}' (TripID {tid})")

        for campo in CAMPOS_YESNO:
            v = r.get(campo, "")
            if v not in ("", "Yes", "No"):
                errores.append(f"[fila {i}] {campo} invalido: '{v}' (debe ser Yes/No/blanco) (TripID {tid})")

    print("=" * 60)
    print(f"QC archivo madre: {CSV_TRABAJO.name}")
    print("=" * 60)
    print(f"Filas: {len(rows)}")
    if errores:
        print(f"\nRESULTADO: {len(errores)} PROBLEMA(S) DETECTADO(S)")
        for e in errores[:200]:
            print("  -", e)
        if len(errores) > 200:
            print(f"  ... y {len(errores) - 200} mas")
    else:
        print("\nRESULTADO: OK - 0 errores.")
    print("=" * 60)
    return 1 if errores else 0


if __name__ == "__main__":
    raise SystemExit(main())
