#!/usr/bin/env python3
"""
colt_verificacion_triage.py
============================
Paso 0 del pipeline de verificacion COLT (ver skill "verificacion-colt-sudamerica").

Compara automaticamente el modulo propio de un pais (03_MODULOS_PAIS/{pais}/{pais}_viajes.csv)
contra las filas de ese mismo pais en la hoja Datos_COLT_Sudamerica, y arma:

  - discrepancias.json   : pares (nuestra fila, fila COLT) que matchean por lider+destino+fecha
                            aproximada pero difieren en algun campo -> requieren que un
                            subagente decida cual version es correcta.
  - colt_unico.json      : filas de COLT para ese pais que no encontramos en nuestra base
                            -> candidatas a agregar (o a descartar si son ruido).
  - nuestro_unico.json   : filas de nuestra base que no encontramos en COLT
                            -> normalmente no requieren accion (COLT no es exhaustivo),
                            pero se listan por si aparece algo raro (fecha mal cargada, etc).
  - workpacks_<n>.json   : los items de discrepancias.json + colt_unico.json divididos en
                            tandas por LeaderID de COLT (evita el bug de bucketing por año:
                            un corte por año puede partir el mandato de un presidente a la
                            mitad si asumio en un mes distinto a enero). Cada tanda queda
                            lista para pasarle a un subagente de investigacion.

USO
---
    python colt_verificacion_triage.py <pais_en_ingles_COLT> <slug_pais_propio> [--items-por-tanda 20]
        [--anio-desde 1994] [--anio-hasta 2025]

Ejemplo:
    python colt_verificacion_triage.py Paraguay paraguay --items-por-tanda 20

<pais_en_ingles_COLT> es el valor exacto de LeaderCountryOrIGO en la planilla
(Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru,
Suriname, Uruguay, Venezuela).
<slug_pais_propio> es el nombre de carpeta en 03_MODULOS_PAIS/ (minusculas, sin tildes).

COLT no tiene una unica ventana temporal: cada pais arranca en un año distinto (ej. Brazil
desde 1948, Uruguay desde 1986, la mayoria del resto desde 1990) y llega hasta 2025 o 2026
segun el pais. Nuestro proyecto tiene su propio alcance fijo -1994 a 2025, el mismo rango que
usa 08_ANALISIS_R/graficos_exploratorios.R-, asi que este script filtra las filas de COLT a
ese rango (ANIO_DESDE/ANIO_HASTA mas abajo) antes de compararlas. Sin este filtro, colt_unico
sale contaminado con filas anteriores a 1994 que no queremos agregar. Cuando el proyecto
actualice su alcance a 2026 (ver nota en el README de 08_ANALISIS_R), subir ANIO_HASTA aca
tambien, o pasar --anio-hasta 2026 en la linea de comandos.

Los resultados se escriben en:
    05_BITACORA/anexos_colt_sudamerica/tmp_<slug_pais_propio>/

No modifica ningun archivo del proyecto -es de solo lectura sobre el Excel y el CSV-.
"""

import argparse
import json
import re
import sys
import unicodedata
from datetime import date, timedelta
from pathlib import Path

import openpyxl

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
XLSX_PATH = PROJECT_ROOT / "04_BASE_FINAL" / "Base_COLT_Sudamerica.xlsx"
SHEET_NAME = "Datos_COLT_Sudamerica"

sys.path.insert(0, str(SCRIPT_DIR))
try:
    from colt_country_alias import COLT_COUNTRY_ALIAS
except ImportError:
    COLT_COUNTRY_ALIAS = {}

# Ventana de tolerancia para considerar que dos fechas "son el mismo viaje".
# COLT y nuestra base a veces difieren en 1-2 dias por como cada fuente cuenta
# llegada/salida -no es necesariamente un error, el subagente lo termina de resolver-.
FECHA_TOLERANCIA_DIAS = 3

# Alcance temporal del proyecto (no de COLT: COLT arranca distinto por pais, ej. Brazil
# desde 1948, Uruguay desde 1986, la mayoria desde 1990). Mismo rango que usa
# 08_ANALISIS_R/graficos_exploratorios.R. Subir ANIO_HASTA a 2026 cuando ese año este
# mas mapeado, o pasar --anio-hasta en la linea de comandos.
ANIO_DESDE_DEFAULT = 1994
ANIO_HASTA_DEFAULT = 2025


def normalizar_texto(s):
    if not s:
        return ""
    s = str(s)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return s


def normalizar_pais(nombre, direccion="a_colt"):
    """direccion='a_colt': nuestro nombre -> vocabulario COLT. 'a_nuestro': al reves."""
    if direccion == "a_colt":
        return COLT_COUNTRY_ALIAS.get(nombre, nombre)
    else:
        inverso = {v: k for k, v in COLT_COUNTRY_ALIAS.items()}
        return inverso.get(nombre, nombre)


def parsear_fecha_colt(valor):
    """Las celdas de fecha en el Excel COLT llegan mezcladas: datetime nativo o texto ISO."""
    if valor is None:
        return None
    if hasattr(valor, "date"):
        return valor.date()
    s = str(valor)[:10]
    try:
        y, m, d = (int(x) for x in s.split("-"))
        return date(y, m, d)
    except Exception:
        return None


def parsear_fecha_csv(valor):
    if not valor:
        return None
    s = str(valor).strip()[:10]
    try:
        y, m, d = (int(x) for x in s.split("-"))
        return date(y, m, d)
    except Exception:
        return None


def cargar_colt(pais_colt, anio_desde, anio_hasta):
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    ws = wb[SHEET_NAME]
    headers = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]
    idx = {h: i for i, h in enumerate(headers)}
    filas = []
    fuera_de_rango = 0
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[idx["LeaderCountryOrIGO"]] != pais_colt:
            continue
        fecha_inicio = parsear_fecha_colt(row[idx["TripStartDate"]])
        # TripYear es el campo mas confiable para el filtro de alcance; si falta,
        # se cae a la fecha de inicio ya parseada. Si tampoco hay fecha, se incluye
        # igual (no se descarta en silencio una fila sin dato de año).
        anio = row[idx["TripYear"]]
        if anio is None and fecha_inicio is not None:
            anio = fecha_inicio.year
        if anio is not None:
            try:
                anio = int(anio)
                if anio < anio_desde or anio > anio_hasta:
                    fuera_de_rango += 1
                    continue
            except (ValueError, TypeError):
                pass
        filas.append({
            "TripID": row[idx["TripID"]],
            "LeaderID": row[idx["LeaderID"]],
            "LeaderFullName": row[idx["LeaderFullName"]],
            "CountryVisited": row[idx["CountryVisited"]],
            "CityVisited": row[idx["CityVisited"]],
            "TripStartDate": fecha_inicio,
            "TripEndDate": parsear_fecha_colt(row[idx["TripEndDate"]]),
            "TripDuration": row[idx["TripDuration"]],
            "Notes": row[idx["Notes"]],
        })
    if fuera_de_rango:
        print(f"({fuera_de_rango} filas de COLT para {pais_colt} quedaron fuera de "
              f"{anio_desde}-{anio_hasta} y no se cargaron)")
    return filas


def cargar_nuestro(slug_pais):
    import csv
    ruta = PROJECT_ROOT / "03_MODULOS_PAIS" / slug_pais / f"{slug_pais}_viajes.csv"
    if not ruta.exists():
        sys.exit(f"No encuentro {ruta}")
    filas = []
    with open(ruta, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("Trip_Status") == "Canceled":
                continue  # COLT no registra los cancelados en esta hoja
            filas.append({
                "Trip_ID": row["Trip_ID"],
                "President": row["President"],
                "Destination_Country": row["Destination_Country"],
                "Destination_City": row.get("Destination_City"),
                "Start_Date": parsear_fecha_csv(row["Start_Date"]),
                "End_Date": parsear_fecha_csv(row.get("End_Date")),
                "Duration_Days": row.get("Duration_Days"),
            })
    return filas


def coinciden(colt_row, our_row):
    if colt_row["TripStartDate"] is None or our_row["Start_Date"] is None:
        return False
    lider_colt = normalizar_texto(colt_row["LeaderFullName"])
    lider_our = normalizar_texto(our_row["President"])
    if not lider_colt or not lider_our:
        return False
    # match de apellido: alcanza con que compartan al menos una palabra de 4+ letras
    palabras_colt = {w for w in lider_colt.split() if len(w) >= 4}
    palabras_our = {w for w in lider_our.split() if len(w) >= 4}
    if not (palabras_colt & palabras_our):
        return False
    pais_colt = normalizar_texto(colt_row["CountryVisited"])
    pais_our_a_colt = normalizar_texto(normalizar_pais(our_row["Destination_Country"], "a_colt"))
    if pais_colt != pais_our_a_colt:
        return False
    delta = abs((colt_row["TripStartDate"] - our_row["Start_Date"]).days)
    return delta <= FECHA_TOLERANCIA_DIAS


def comparar_campos(colt_row, our_row):
    """Devuelve lista de diferencias relevantes entre un par ya matcheado."""
    diffs = []
    if colt_row["TripStartDate"] != our_row["Start_Date"]:
        diffs.append({
            "campo": "Start_Date/TripStartDate",
            "nuestro": str(our_row["Start_Date"]),
            "colt": str(colt_row["TripStartDate"]),
        })
    try:
        dur_our = int(our_row["Duration_Days"]) if our_row["Duration_Days"] else None
    except ValueError:
        dur_our = None
    if colt_row["TripDuration"] is not None and dur_our is not None:
        try:
            dur_colt = int(colt_row["TripDuration"])
            if dur_colt != dur_our:
                diffs.append({"campo": "Duration_Days/TripDuration", "nuestro": dur_our, "colt": dur_colt})
        except (ValueError, TypeError):
            pass
    if colt_row["CityVisited"] and our_row["Destination_City"]:
        if normalizar_texto(colt_row["CityVisited"]) != normalizar_texto(our_row["Destination_City"]):
            diffs.append({
                "campo": "Destination_City/CityVisited",
                "nuestro": our_row["Destination_City"],
                "colt": colt_row["CityVisited"],
            })
    return diffs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pais_colt", help='Valor exacto de LeaderCountryOrIGO, ej. "Paraguay"')
    ap.add_argument("slug_pais", help='Carpeta en 03_MODULOS_PAIS/, ej. "paraguay"')
    ap.add_argument("--items-por-tanda", type=int, default=20)
    ap.add_argument("--anio-desde", type=int, default=ANIO_DESDE_DEFAULT,
                     help=f"Default {ANIO_DESDE_DEFAULT}. Alcance del proyecto, no de COLT.")
    ap.add_argument("--anio-hasta", type=int, default=ANIO_HASTA_DEFAULT,
                     help=f"Default {ANIO_HASTA_DEFAULT}. Subir a 2026 cuando ese año este mapeado.")
    args = ap.parse_args()

    colt_rows = cargar_colt(args.pais_colt, args.anio_desde, args.anio_hasta)
    our_rows = cargar_nuestro(args.slug_pais)
    print(f"Alcance aplicado a COLT: {args.anio_desde}-{args.anio_hasta}")
    print(f"COLT: {len(colt_rows)} filas de {args.pais_colt} | Nuestra base: {len(our_rows)} filas ({args.slug_pais})")

    matched_colt_idx = set()
    matched_our_idx = set()
    discrepancias = []

    for i, cr in enumerate(colt_rows):
        for j, orow in enumerate(our_rows):
            if j in matched_our_idx:
                continue
            if coinciden(cr, orow):
                matched_colt_idx.add(i)
                matched_our_idx.add(j)
                diffs = comparar_campos(cr, orow)
                if diffs:
                    discrepancias.append({
                        "colt_TripID": cr["TripID"],
                        "colt_LeaderID": cr["LeaderID"],
                        "our_Trip_ID": orow["Trip_ID"],
                        "President": orow["President"],
                        "diferencias": diffs,
                    })
                break

    colt_unico = [
        {"colt_TripID": cr["TripID"], "colt_LeaderID": cr["LeaderID"], "LeaderFullName": cr["LeaderFullName"],
         "CountryVisited": cr["CountryVisited"], "CityVisited": cr["CityVisited"],
         "TripStartDate": str(cr["TripStartDate"]), "TripDuration": cr["TripDuration"], "Notes": cr["Notes"]}
        for i, cr in enumerate(colt_rows) if i not in matched_colt_idx
    ]
    nuestro_unico = [
        {"our_Trip_ID": orow["Trip_ID"], "President": orow["President"],
         "Destination_Country": orow["Destination_Country"], "Start_Date": str(orow["Start_Date"])}
        for j, orow in enumerate(our_rows) if j not in matched_our_idx
    ]

    outdir = PROJECT_ROOT / "05_BITACORA" / "anexos_colt_sudamerica" / f"tmp_{args.slug_pais}"
    outdir.mkdir(parents=True, exist_ok=True)

    (outdir / "discrepancias.json").write_text(json.dumps(discrepancias, ensure_ascii=False, indent=2), encoding="utf-8")
    (outdir / "colt_unico.json").write_text(json.dumps(colt_unico, ensure_ascii=False, indent=2), encoding="utf-8")
    (outdir / "nuestro_unico.json").write_text(json.dumps(nuestro_unico, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Discrepancias (matcheados con diferencias): {len(discrepancias)}")
    print(f"COLT unico (posibles filas a agregar):       {len(colt_unico)}")
    print(f"Nuestro unico (no encontrados en COLT):        {len(nuestro_unico)}")

    # --- Workpacks por LeaderID (evita el bug de bucketing por año) ---
    por_leader = {}
    for item in discrepancias + colt_unico:
        lid = item["colt_LeaderID"]
        por_leader.setdefault(lid, []).append(item)

    leader_ids_ordenados = sorted(por_leader.keys(), key=lambda x: (str(x)))
    tanda = []
    n_tanda = 1
    tandas_escritas = []
    for lid in leader_ids_ordenados:
        tanda.extend(por_leader[lid])
        if len(tanda) >= args.items_por_tanda:
            fname = outdir / f"workpack_{n_tanda:02d}.json"
            fname.write_text(json.dumps(tanda, ensure_ascii=False, indent=2), encoding="utf-8")
            tandas_escritas.append(str(fname))
            tanda = []
            n_tanda += 1
    if tanda:
        fname = outdir / f"workpack_{n_tanda:02d}.json"
        fname.write_text(json.dumps(tanda, ensure_ascii=False, indent=2), encoding="utf-8")
        tandas_escritas.append(str(fname))

    print(f"\nWorkpacks escritos ({len(tandas_escritas)}):")
    for t in tandas_escritas:
        print(" -", t)
    print(f"\nTodo guardado en: {outdir}")
    print("Revisar nuestro_unico.json a mano (no requiere subagente en la mayoria de los casos).")


if __name__ == "__main__":
    main()
