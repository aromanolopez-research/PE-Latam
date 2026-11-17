#!/usr/bin/env python3
"""Migracion puntual (2026-08-24, rediseno del proyecto): vuelca las filas 'nuestro_unico'
de Paraguay y Uruguay -viajes que investigamos nosotros y que COLT nunca tuvo- a la hoja
Datos_COLT_Sudamerica de Base_COLT_Sudamerica.xlsx, usando el mismo esquema/convencion de
TripID que ya se uso para Argentina/Brasil/Chile (PELATAM-<ISO3>-<numero>, ver esas 111
filas ya existentes). No toca ninguna fila existente, solo agrega filas nuevas al final.
"""
import csv
import json
import re
import unicodedata
from pathlib import Path

import openpyxl


def normalizar(nombre):
    """COLT escribe los nombres SIN acentos y a veces truncados (ej. 'Nicanor Duarte'
    en vez de 'Nicanor Duarte Frutos'). Sacamos acentos/mayusculas para poder cruzar
    contra nuestro 'President' (que si lleva acentos y a veces el nombre completo)."""
    n = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode("ascii")
    return n.lower().strip()


def buscar_leader(nombre_nuestro, leader_lookup_por_nombre_normalizado):
    """Matchea por igualdad normalizada primero; si no, por contencion de substring
    (subset de palabras) en cualquier direccion -cubre truncamientos tipo Duarte Frutos
    -> Duarte-."""
    norm = normalizar(nombre_nuestro)
    if norm in leader_lookup_por_nombre_normalizado:
        return leader_lookup_por_nombre_normalizado[norm]
    for cand_norm, info in leader_lookup_por_nombre_normalizado.items():
        if cand_norm in norm or norm in cand_norm:
            return info
    return None

PROJECT_ROOT = Path("/sessions/brave-vibrant-volta/mnt/PE Latam/Política Exterior Latam/Viajes de Presidentes - Latam/Base Viaje Presidenciales Latam")
XLSX_PATH = PROJECT_ROOT / "04_BASE_FINAL" / "Base_COLT_Sudamerica.xlsx"
ANEXOS = PROJECT_ROOT / "05_BITACORA" / "anexos_colt_sudamerica"

import sys
sys.path.insert(0, str(PROJECT_ROOT / "06_SCRIPTS"))
from colt_country_alias import COLT_COUNTRY_ALIAS  # nuestro nombre -> nombre de COLT

PAISES = {
    "paraguay": {"iso3": "PRY", "nuestro_unico": ANEXOS / "tmp_paraguay" / "nuestro_unico.json",
                 "csv": PROJECT_ROOT / "03_MODULOS_PAIS" / "paraguay" / "paraguay_viajes.csv"},
    "uruguay": {"iso3": "URY", "nuestro_unico": ANEXOS / "tmp_uruguay" / "nuestro_unico.json",
                "csv": PROJECT_ROOT / "03_MODULOS_PAIS" / "uruguay" / "uruguay_viajes.csv"},
}

YN = {"TRUE": "Yes", "FALSE": "No", "NA": None, "": None, None: None}


def main():
    wb = openpyxl.load_workbook(XLSX_PATH)
    ws = wb["Datos_COLT_Sudamerica"]
    headers = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]
    idx = {h: i for i, h in enumerate(headers)}

    # Lookups construidos UNA vez recorriendo la hoja entera (secuencial, rapido).
    leader_lookup = {}  # LeaderFullName -> dict de campos fijos del mandatario
    country_lookup = {}  # CountryVisited -> dict de campos fijos del pais destino
    max_num_por_pais = {}  # ISO3 -> maximo numero de sufijo PELATAM ya usado

    leader_fields = ["LeaderID", "LeaderCountryOrIGO", "LeaderCountryISO", "LeaderRegion",
                      "LeaderSubregion", "PriorityLeader", "LeaderRole", "LeaderTitle",
                      "LeaderSurname", "LeaderFullName"]
    country_fields = ["CountryVisitedISO", "RegionVisited", "SubRegionVisited",
                       "DisputedTerritory", "SemiAutoTerritory"]

    for row in ws.iter_rows(min_row=2, values_only=True):
        rd = dict(zip(headers, row))
        lname = rd.get("LeaderFullName")
        if lname:
            norm = normalizar(lname)
            if norm not in leader_lookup:
                leader_lookup[norm] = {f: rd.get(f) for f in leader_fields}
        cvis = rd.get("CountryVisited")
        if cvis and cvis not in country_lookup:
            country_lookup[cvis] = {f: rd.get(f) for f in country_fields}
        tid = rd.get("TripID")
        if tid and str(tid).startswith("PELATAM-"):
            m = re.match(r"PELATAM-([A-Z]+)-(\d+)", str(tid))
            if m:
                iso3, num = m.group(1), int(m.group(2))
                max_num_por_pais[iso3] = max(max_num_por_pais.get(iso3, 0), num)

    total_agregadas = 0
    reporte = []

    for slug, cfg in PAISES.items():
        iso3 = cfg["iso3"]
        nuestro_unico = json.load(open(cfg["nuestro_unico"], encoding="utf-8"))
        with open(cfg["csv"], newline="", encoding="utf-8") as f:
            csv_rows = {r["Trip_ID"]: r for r in csv.DictReader(f)}

        agregadas_pais = 0
        no_encontradas = []

        for item in nuestro_unico:
            tid_our = str(item["our_Trip_ID"])
            row = csv_rows.get(tid_our)
            if not row:
                no_encontradas.append(tid_our)
                continue

            lname = row.get("President")
            leader_info = buscar_leader(lname, leader_lookup) or {}
            if not leader_info:
                print(f"  AVISO [{slug}]: no encontre a '{lname}' en ninguna fila existente de COLT "
                      f"para copiar sus campos Leader* -queda incompleto, revisar a mano-.")

            dest = row.get("Destination_Country")
            dest_colt = COLT_COUNTRY_ALIAS.get(dest, dest)
            country_info = country_lookup.get(dest_colt, {})
            if not country_info:
                print(f"  AVISO [{slug}]: no encontre '{dest}' (buscado como '{dest_colt}') en ninguna "
                      f"fila existente de COLT para copiar CountryVisitedISO/Region -queda vacio, "
                      f"revisar a mano (posible pais fuera del vocabulario de COLT, ver "
                      f"colt_country_alias.py)-.")

            start = row.get("Start_Date", "") or ""
            year = start[:4] if len(start) >= 4 and start[:4].isdigit() else None

            fuente = row.get("Source_Verification", "") or ""
            notas = (
                f"[PE-Latam: viaje investigado por el proyecto, NO presente en COLT. "
                f"Trip_Objective original: {row.get('Trip_Objective', '')} "
                f"Fuente: {fuente} "
                f"Migrado desde 03_MODULOS_PAIS/{slug}/{slug}_viajes.csv Trip_ID {tid_our} "
                f"el 2026-08-24 durante el rediseño del proyecto a archivo madre unico.]"
            )

            max_num_por_pais[iso3] = max_num_por_pais.get(iso3, 0) + 0  # noop, keep key
            nuevo_tripid = f"PELATAM-{iso3}-{tid_our}"

            nueva_fila = {h: None for h in headers}
            nueva_fila["TripID"] = nuevo_tripid
            nueva_fila.update(leader_info)  # incluye LeaderFullName con la grafia de COLT
            # (sin acentos), asi el LeaderID/LeaderFullName agrupan bien con el resto de
            # las filas del mismo mandatario en cualquier analisis agregado. Si no hubo
            # match (leader_info vacio), guardamos nuestro propio nombre como fallback
            # para no perder el dato, aunque quede inconsistente -flaggeado en el aviso-.
            if not leader_info:
                nueva_fila["LeaderFullName"] = lname
            nueva_fila["CountryVisited"] = dest_colt  # vocabulario de COLT, consistente con el resto de la hoja
            nueva_fila.update(country_info)
            nueva_fila["CityVisited"] = row.get("Destination_City") if row.get("Destination_City") not in ("NA", "", None) else None
            nueva_fila["TripYear"] = int(year) if year else None
            nueva_fila["TripStartDate"] = row.get("Start_Date") or None
            nueva_fila["TripEndDate"] = row.get("End_Date") if row.get("End_Date") not in ("NA", "") else None
            dur = row.get("Duration_Days")
            nueva_fila["TripDuration"] = int(dur) if dur and str(dur).isdigit() else None
            nueva_fila["MetHostHoGS"] = YN.get(row.get("MetHostHOGS"))
            nueva_fila["MetNonhostHOGS"] = YN.get(row.get("MetNonHostHOGS"))
            nnh = row.get("NonHostHOGS_Name")
            nueva_fila["NonhostHOGSNames"] = nnh if nnh not in ("NA", "", None) else None
            nueva_fila["PublicAddress"] = YN.get(row.get("PublicAddress"))
            nueva_fila["SignedAgreement"] = YN.get(row.get("SignedAgreement"))
            nueva_fila["CulturalSiteOrCeremony"] = YN.get(row.get("CulturalSiteOrCeremony"))
            nueva_fila["BusinessLeaderOrForum"] = YN.get(row.get("BusinessLeaderOrForum"))
            nueva_fila["MetIGOLeader"] = YN.get(row.get("MetIGOLeader"))
            igo = row.get("IGOLeader_Name")
            nueva_fila["IGOLeaderName"] = igo if igo not in ("NA", "", None) else None
            ce = row.get("Counterpart_Event")
            if ce and ce not in ("NA", ""):
                if row.get("Visit_Category") == "Multilateral":
                    nueva_fila["NameMultilatEvent"] = ce
                    nueva_fila["AttendedMultilatEvent"] = "Yes"
                else:
                    nueva_fila["HostHOGSName"] = ce
            nueva_fila["Notes"] = notas
            nueva_fila["SourceLink1"] = fuente if fuente else None

            ws.append([nueva_fila.get(h) for h in headers])
            agregadas_pais += 1
            total_agregadas += 1

        reporte.append((slug, agregadas_pais, no_encontradas))

    wb.save(XLSX_PATH)

    print("\n=== Migracion completa ===")
    for slug, n, no_enc in reporte:
        print(f"  {slug}: {n} filas agregadas" + (f" | NO encontradas en el CSV: {no_enc}" if no_enc else ""))
    print(f"  Total: {total_agregadas} filas nuevas en Datos_COLT_Sudamerica")


if __name__ == "__main__":
    main()
