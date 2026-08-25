#!/usr/bin/env python3
"""
colt_aplicar_workpacks.py
===========================
Paso 2 del pipeline REDISEÑADO (2026-08-24). Aplica los resultados de investigacion de
uno o mas workpacks (ver colt_generar_workpacks.py) sobre el CSV de trabajo
(04_BASE_FINAL/base_colt_sudamerica_trabajo.csv).

FORMATO ESPERADO de cada resultados_workpack_NN.json (lista de objetos, uno por
LeaderID investigado):
[
  {
    "LeaderID": "...",
    "correcciones": [
      {"TripID": "...", "campo": "TripDuration", "valor_correcto": "3",
       "fuente": "https://...", "justificacion": "..."}
      // UN item = UN campo, siempre. Si un mismo TripID tiene 2 campos mal, van 2
      // items separados (misma regla que el pipeline anterior -ver Errores conocidos
      // de la skill verificacion-colt-sudamerica-).
    ],
    "hallazgos_nuevos": [
      {"CountryVisited": "Brazil", "CityVisited": "Brasilia",
       "TripStartDate": "2010-03-15", "TripEndDate": "2010-03-16", "TripDuration": "2",
       "MetHostHoGS": "Yes", "HostHOGSName": "...",           // opcional, lo que se sepa
       "AttendedMultilatEvent": "No",                          // opcional
       "fuente": "https://...", "justificacion": "..."}
      // Viaje que COLT NO tiene. Se inserta como fila PELATAM-<ISO3>-<n>. Los campos
      // de micro-conducta que no se investigaron quedan en blanco (None) -nunca
      // asumir "No" sin evidencia-.
    ],
    "no_verificable": [
      {"TripID": "...", "campo": "...", "justificacion": "..."}
      // Se reviso pero no se pudo confirmar en ningun sentido. No se toca la celda,
      // solo se dejan constancia en el log y en Notes.
    ]
  },
  ...
]

USO
---
    python colt_aplicar_workpacks.py <pais_colt> <slug> resultados_workpack_01.json [...] [--aplicar]

Sin --aplicar corre en DRY RUN (solo imprime el resumen, no toca el csv de trabajo).

Despues de aplicar, correr colt_validar_madre.py y despues colt_importar_csv.py para
volcar los cambios al .xlsx.
"""
import argparse
import csv
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
CSV_TRABAJO = PROJECT_ROOT / "04_BASE_FINAL" / "base_colt_sudamerica_trabajo.csv"
ANEXOS = PROJECT_ROOT / "05_BITACORA" / "anexos_colt_sudamerica"
HOY = date.today().isoformat()

sys.path.insert(0, str(SCRIPT_DIR))
try:
    from colt_country_alias import COLT_COUNTRY_ALIAS
except ImportError:
    COLT_COUNTRY_ALIAS = {}


def normalizar(nombre):
    n = unicodedata.normalize("NFKD", str(nombre)).encode("ascii", "ignore").decode("ascii")
    return n.lower().strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pais_colt", help='Para logging, ej. "Bolivia"')
    ap.add_argument("slug", help="Para nombrar el log, ej. bolivia")
    ap.add_argument("json_files", nargs="+")
    ap.add_argument("--aplicar", action="store_true")
    args = ap.parse_args()

    with open(CSV_TRABAJO, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)

    by_tripid = {r["TripID"]: r for r in rows}

    # Lookups para armar filas PELATAM nuevas (Leader*/Country* copiados de filas
    # existentes, nunca inventados -mismo criterio que migrar_nuestro_unico.py-).
    leader_lookup = {}
    country_lookup = {}
    leader_fields = ["LeaderID", "LeaderCountryOrIGO", "LeaderCountryISO", "LeaderRegion",
                      "LeaderSubregion", "PriorityLeader", "LeaderRole", "LeaderTitle",
                      "LeaderSurname", "LeaderFullName"]
    country_fields = ["CountryVisitedISO", "RegionVisited", "SubRegionVisited",
                       "DisputedTerritory", "SemiAutoTerritory"]
    max_num_por_iso3 = {}
    for r in rows:
        lid = r.get("LeaderID")
        if lid and lid not in leader_lookup:
            leader_lookup[lid] = {f: r.get(f) for f in leader_fields}
        cvis = r.get("CountryVisited")
        if cvis and cvis not in country_lookup:
            country_lookup[cvis] = {f: r.get(f) for f in country_fields}
        tid = r.get("TripID", "")
        m = re.match(r"PELATAM-([A-Z]+)-(\d+)", tid)
        if m:
            iso3, num = m.group(1), int(m.group(2))
            max_num_por_iso3[iso3] = max(max_num_por_iso3.get(iso3, 0), num)

    iso3_pais = None
    for r in rows:
        if r.get("LeaderCountryOrIGO") == args.pais_colt:
            iso3_pais = r.get("LeaderCountryISO")
            break
    if not iso3_pais:
        print(f"AVISO: no encontre LeaderCountryISO para '{args.pais_colt}' en el csv "
              f"-hace falta para nombrar TripID de hallazgos nuevos-.")

    log_rows = []
    n_correcciones = n_no_verificable = n_hallazgos = 0
    no_encontrados = []

    for jf in args.json_files:
        data = json.load(open(jf, encoding="utf-8"))
        for bloque in data:
            for item in bloque.get("correcciones", []):
                tid = item.get("TripID")
                campo = item.get("campo")
                valor = item.get("valor_correcto")
                fila = by_tripid.get(tid)
                if not fila:
                    no_encontrados.append(tid)
                    continue
                if campo not in headers:
                    print(f"  AVISO: campo '{campo}' no existe en el esquema, item ignorado (TripID {tid})")
                    continue
                valor_viejo = fila.get(campo)
                if args.aplicar:
                    fila[campo] = valor
                    nota_vieja = fila.get("Notes") or ""
                    fila["Notes"] = (
                        nota_vieja + f" [PE-Latam {HOY}: {campo} corregido de "
                        f"'{valor_viejo}' a '{valor}'. Fuente: {(item.get('fuente') or '')[:150]}]"
                    ).strip()
                n_correcciones += 1
                log_rows.append([tid, "correccion", campo, valor_viejo, valor, item.get("fuente"), item.get("justificacion")])

            for item in bloque.get("no_verificable", []):
                tid = item.get("TripID")
                fila = by_tripid.get(tid)
                if fila and args.aplicar:
                    nota_vieja = fila.get("Notes") or ""
                    fila["Notes"] = (
                        nota_vieja + f" [PE-Latam {HOY}: revisado, {item.get('campo','')} "
                        f"queda No_verificable -{(item.get('justificacion') or '')[:150]}-]"
                    ).strip()
                n_no_verificable += 1
                log_rows.append([tid, "no_verificable", item.get("campo"), "", "", "", item.get("justificacion")])

            for item in bloque.get("hallazgos_nuevos", []):
                if not iso3_pais:
                    print("  AVISO: hallazgo nuevo ignorado, no hay ISO3 de pais para nombrar el TripID.")
                    continue
                lid = bloque.get("LeaderID")
                leader_info = leader_lookup.get(lid, {})
                dest = item.get("CountryVisited")
                dest_colt = COLT_COUNTRY_ALIAS.get(dest, dest)
                country_info = country_lookup.get(dest_colt, {})
                if not country_info:
                    print(f"  AVISO: '{dest}' (buscado como '{dest_colt}') no tiene fila de "
                          f"referencia en COLT para copiar CountryVisitedISO/Region -queda vacio-.")

                max_num_por_iso3[iso3_pais] = max_num_por_iso3.get(iso3_pais, 0) + 1
                nuevo_tid = f"PELATAM-{iso3_pais}-{max_num_por_iso3[iso3_pais]}"

                nueva_fila = {h: "" for h in headers}
                nueva_fila["TripID"] = nuevo_tid
                nueva_fila.update(leader_info)
                nueva_fila["CountryVisited"] = dest_colt
                nueva_fila.update(country_info)
                for campo in ["CityVisited", "TripStartDate", "TripEndDate", "TripDuration",
                              "MetHostHoGS", "HostHOGSName", "AttendedMultilatEvent", "NameMultilatEvent",
                              "MetNonhostHOGS", "NonhostHOGSNames", "PublicAddress", "SignedAgreement",
                              "CulturalSiteOrCeremony", "BusinessLeaderOrForum", "MetIGOLeader", "IGOLeaderName"]:
                    if item.get(campo) not in (None, ""):
                        nueva_fila[campo] = item[campo]
                start = nueva_fila.get("TripStartDate", "")
                nueva_fila["TripYear"] = start[:4] if start else ""
                nueva_fila["Notes"] = (
                    f"[PE-Latam {HOY}: viaje investigado por el proyecto, NO presente en COLT. "
                    f"{item.get('justificacion','')} Fuente: {item.get('fuente','')}]"
                )
                nueva_fila["SourceLink1"] = item.get("fuente", "")

                if args.aplicar:
                    rows.append(nueva_fila)
                    by_tripid[nuevo_tid] = nueva_fila
                n_hallazgos += 1
                log_rows.append([nuevo_tid, "hallazgo_nuevo", "", "", dest, item.get("fuente"), item.get("justificacion")])

    print(f"\nResumen:")
    print(f"  Correcciones aplicadas:     {n_correcciones}  ({'aplicado' if args.aplicar else 'DRY RUN'})")
    print(f"  No_verificable:             {n_no_verificable}")
    print(f"  Hallazgos nuevos (PELATAM): {n_hallazgos}  ({'aplicado' if args.aplicar else 'DRY RUN'})")
    if no_encontrados:
        print(f"  TripID no encontrados en el csv de trabajo (revisar a mano): {no_encontrados[:20]}")

    if args.aplicar:
        with open(CSV_TRABAJO, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=headers)
            w.writeheader()
            w.writerows(rows)
        outdir = ANEXOS
        outdir.mkdir(parents=True, exist_ok=True)
        log_path = outdir / f"cambios_aplicados_{args.slug}_{HOY}.csv"
        with open(log_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["TripID", "tipo", "campo", "valor_viejo", "valor_nuevo_o_destino", "fuente", "justificacion"])
            w.writerows(log_rows)
        print(f"\nGuardado en {CSV_TRABAJO}. Log: {log_path}")
        print("Siguiente paso: python colt_validar_madre.py, despues python colt_importar_csv.py")
    else:
        print("\nDRY RUN: no se modifico el csv de trabajo. Revisar y volver a correr con --aplicar.")


if __name__ == "__main__":
    main()
