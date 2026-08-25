#!/usr/bin/env python3
"""
colt_generar_workpacks.py
==========================
Paso 1 del pipeline REDISEÑADO (2026-08-24) de trabajo contra el archivo madre unico.

Reemplaza a colt_verificacion_triage.py para paises que NO tienen un modulo propio en
03_MODULOS_PAIS (Bolivia y los 6 nuevos: Colombia, Ecuador, Guyana, Peru, Surinam,
Venezuela). La diferencia clave con el flujo anterior: ya no hay un CSV propio contra el
cual comparar (discrepancia / colt_unico / nuestro_unico dejan de tener sentido como
categorias -no hay "nuestro" separado de COLT, todo vive en el mismo archivo-). En vez de
eso, este script arma, por LeaderID, un paquete con TODAS las filas que COLT ya tiene
cargadas para ese mandatario, para que un subagente:
  (a) las VERIFIQUE contra fuentes reales y proponga correcciones puntuales donde COLT
      este mal, y
  (b) investigue de forma independiente si hay viajes de ese mandato que COLT nunca
      capturo, para agregarlos como fila nueva (PELATAM-<ISO3>-<n>).

Para paises que YA tienen modulo propio y fueron verificados con el pipeline anterior
(Argentina, Brasil, Chile, Paraguay, Uruguay), no hace falta correr este script de nuevo
-esos paises ya estan consolidados en el archivo madre-. Si en el futuro se quiere hacer
una segunda pasada de verificacion sobre ellos, este mismo script sirve igual (simplemente
arma un workpack con lo que ya esta cargado para revisar de nuevo).

USO
---
    python colt_export_csv.py                          # (si no se corrio antes en esta sesion)
    python colt_generar_workpacks.py <pais_colt> [--items-por-tanda 20] [--anio-desde 1994] [--anio-hasta 2025]

Ejemplo:
    python colt_generar_workpacks.py Bolivia --items-por-tanda 25

<pais_colt> es el valor exacto de LeaderCountryOrIGO en la hoja madre (Argentina,
Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru, Suriname, Uruguay,
Venezuela -ojo, vocabulario en ingles de COLT, ej. "Brazil"/"Peru" sin tilde-).

Salida: 05_BITACORA/anexos_colt_sudamerica/tmp_<slug>/workpack_NN.json, uno por tanda de
LeaderID, listo para pasarle a un subagente de investigacion. No modifica ningun archivo
del proyecto -es de solo lectura sobre el csv de trabajo-.
"""
import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
CSV_TRABAJO = PROJECT_ROOT / "04_BASE_FINAL" / "base_colt_sudamerica_trabajo.csv"

ANIO_DESDE_DEFAULT = 1994
ANIO_HASTA_DEFAULT = 2025

# Campos que se le muestran al subagente por item (subconjunto legible del esquema de
# 76 columnas; los SourceLink1-33 se resumen a los que tengan valor, para no inundar el
# JSON con blancos).
CAMPOS_RESUMEN = [
    "TripID", "LeaderID", "LeaderFullName", "CountryVisited", "CityVisited",
    "TripYear", "TripStartDate", "TripEndDate", "TripDuration",
    "MetHostHoGS", "HostHOGSName", "AttendedMultilatEvent", "NameMultilatEvent",
    "MetNonhostHOGS", "NonhostHOGSNames", "PublicAddress", "SignedAgreement",
    "CulturalSiteOrCeremony", "BusinessLeaderOrForum", "MetIGOLeader", "IGOLeaderName",
    "Notes", "Confidence(1-5)",
]


def slug_de(pais_colt):
    s = unicodedata.normalize("NFKD", pais_colt).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pais_colt", help='Valor exacto de LeaderCountryOrIGO, ej. "Bolivia"')
    ap.add_argument("--items-por-tanda", type=int, default=20)
    ap.add_argument("--anio-desde", type=int, default=ANIO_DESDE_DEFAULT)
    ap.add_argument("--anio-hasta", type=int, default=ANIO_HASTA_DEFAULT)
    args = ap.parse_args()

    if not CSV_TRABAJO.exists():
        raise SystemExit(f"No existe {CSV_TRABAJO}. Correr colt_export_csv.py primero.")

    with open(CSV_TRABAJO, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    filas_pais = []
    fuera_de_rango = 0
    for row in rows:
        if row.get("LeaderCountryOrIGO") != args.pais_colt:
            continue
        anio = row.get("TripYear") or (row.get("TripStartDate") or "")[:4]
        try:
            anio_i = int(str(anio)[:4])
            if anio_i < args.anio_desde or anio_i > args.anio_hasta:
                fuera_de_rango += 1
                continue
        except (ValueError, TypeError):
            pass  # sin año parseable: se incluye igual, no se descarta en silencio
        filas_pais.append(row)

    if not filas_pais:
        raise SystemExit(
            f"0 filas encontradas para LeaderCountryOrIGO == '{args.pais_colt}'. "
            f"Revisar que el nombre sea EXACTO (vocabulario de COLT, en ingles)."
        )

    print(f"Alcance aplicado: {args.anio_desde}-{args.anio_hasta} ({fuera_de_rango} filas fuera de rango)")
    print(f"COLT: {len(filas_pais)} filas ya cargadas para {args.pais_colt}")

    por_leader = {}
    for row in filas_pais:
        lid = row.get("LeaderID")
        por_leader.setdefault(lid, []).append(row)

    resumen_leaders = []
    for lid, filas in sorted(por_leader.items(), key=lambda kv: str(kv[0])):
        fechas = sorted(f.get("TripStartDate", "") for f in filas if f.get("TripStartDate"))
        resumen_leaders.append({
            "LeaderID": lid,
            "LeaderFullName": filas[0].get("LeaderFullName"),
            "cantidad_filas_ya_cargadas": len(filas),
            "rango_fechas_ya_cargado": [fechas[0], fechas[-1]] if fechas else None,
        })

    slug = slug_de(args.pais_colt)
    outdir = PROJECT_ROOT / "05_BITACORA" / "anexos_colt_sudamerica" / f"tmp_{slug}"
    outdir.mkdir(parents=True, exist_ok=True)

    (outdir / "resumen_leaders.json").write_text(
        json.dumps(resumen_leaders, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    leader_ids_ordenados = sorted(por_leader.keys(), key=lambda x: str(x))
    tanda = []
    n_tanda = 1
    tandas_escritas = []
    for lid in leader_ids_ordenados:
        items = [{c: row.get(c, "") for c in CAMPOS_RESUMEN} for row in por_leader[lid]]
        tanda.append({"LeaderID": lid, "LeaderFullName": por_leader[lid][0].get("LeaderFullName"), "items_ya_en_COLT": items})
        if len(tanda) >= max(1, args.items_por_tanda // 10):
            # Nota: acá "tanda" agrupa LIDERES completos, no items sueltos -un mandato no
            # se corta a la mitad-. items_por_tanda actua como un tope aproximado de
            # volumen total de items dentro de la tanda, no un conteo exacto de lideres.
            total_items = sum(len(t["items_ya_en_COLT"]) for t in tanda)
            if total_items >= args.items_por_tanda or lid == leader_ids_ordenados[-1]:
                fname = outdir / f"workpack_{n_tanda:02d}.json"
                fname.write_text(json.dumps(tanda, ensure_ascii=False, indent=2), encoding="utf-8")
                tandas_escritas.append(str(fname))
                tanda = []
                n_tanda += 1
    if tanda:
        fname = outdir / f"workpack_{n_tanda:02d}.json"
        fname.write_text(json.dumps(tanda, ensure_ascii=False, indent=2), encoding="utf-8")
        tandas_escritas.append(str(fname))

    print(f"\nMandatarios (LeaderID) encontrados: {len(por_leader)}")
    print(f"Workpacks escritos ({len(tandas_escritas)}):")
    for t in tandas_escritas:
        print(" -", t)
    print(f"\nTodo guardado en: {outdir}")
    print(
        "\nCada item de workpack trae 'items_ya_en_COLT' (filas que YA existen para ese "
        "LeaderID, para verificar/corregir) pero el subagente tambien debe investigar de "
        "forma independiente si hubo viajes de ese mandato que COLT no capturo -no alcanza "
        "con revisar la lista, hay que buscar activamente huecos-. Formato de resultado "
        "esperado: ver docstring de colt_aplicar_workpacks.py."
    )


if __name__ == "__main__":
    main()
