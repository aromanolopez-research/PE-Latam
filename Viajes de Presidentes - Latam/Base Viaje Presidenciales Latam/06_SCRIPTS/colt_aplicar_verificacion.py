#!/usr/bin/env python3
"""
colt_aplicar_verificacion.py
=============================
Paso 3 del pipeline de verificacion COLT (ver skill "verificacion-colt-sudamerica").

Toma los JSON de veredictos que devuelven los subagentes de investigacion (uno por
tanda/workpack, ver colt_verificacion_triage.py) y los aplica de forma auditable:

  - Corrige la hoja Datos_COLT_Sudamerica cuando el veredicto dice que COLT esta mal
    (deja registrado el valor viejo y la fuente en la columna Notes, NUNCA borra la fila).
  - Corrige nuestro propio CSV de pais cuando el veredicto dice que COLT tiene razon
    (deja registrado el cambio en Methodological_Notes).
  - Inserta en la hoja COLT y (opcionalmente, con --insertar-en-nuestra-base) en nuestro
    CSV las filas "colt_unico" que el subagente marco como agregar_a_nuestra_base.
  - Escribe un CSV de log con cada cambio aplicado (para la bitacora y para que el
    usuario pueda revisar decision por decision despues).

Por defecto corre en modo DRY RUN (no escribe nada, solo imprime que haria). Pasar
--aplicar para que efectivamente modifique los archivos.

ESQUEMA ESPERADO DE CADA ITEM EN EL JSON DE VEREDICTOS
-------------------------------------------------------
Para discrepancias (matcheadas COLT <-> nuestra base), cada item de "resultados" trae:
{
  "colt_TripID": "...",
  "our_Trip_ID": "...",                 # puede faltar si el subagente no lo tenia
  "tipo": "discrepancia",
  "veredicto": "COLT_correcto" | "nuestro_correcto" | "ambos_correctos" | "No_verificable",
  "campo": "Start_Date" | "Duration_Days" | "Destination_City" | ...,
  "valor_correcto": "...",              # solo si hay un veredicto claro
  "fuente": "https://...",
  "justificacion": "..."
}

Para colt_unico (candidatas a agregar), cada item trae:
{
  "colt_TripID": "...",
  "tipo": "colt_unico",
  "decision": "agregar" | "descartar" | "No_verificable",
  "justificacion": "...",
  "fuente": "..."
}

USO
---
    python colt_aplicar_verificacion.py <slug_pais> <archivo1.json> [<archivo2.json> ...] [--aplicar] [--insertar-en-nuestra-base]

Ejemplo (dry run primero, siempre):
    python colt_aplicar_verificacion.py paraguay tmp_paraguay/resultados_workpack_01.json

Cuando el dry run se ve bien:
    python colt_aplicar_verificacion.py paraguay tmp_paraguay/resultados_workpack_01.json --aplicar
"""

import argparse
import csv
import datetime
import json
import sys
from pathlib import Path

import openpyxl

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
XLSX_PATH = PROJECT_ROOT / "04_BASE_FINAL" / "Base_COLT_Sudamerica.xlsx"
SHEET_NAME = "Datos_COLT_Sudamerica"

sys.path.insert(0, str(SCRIPT_DIR))
try:
    from colt_country_alias import COLT_COUNTRY_ALIAS
    _ALIAS_COLT_A_NUESTRO = {v: k for k, v in COLT_COUNTRY_ALIAS.items()}
except ImportError:
    _ALIAS_COLT_A_NUESTRO = {}

try:
    from schema import region_for, MISSING as SCHEMA_MISSING
except ImportError:
    def region_for(pais):
        return "NA"
    SCHEMA_MISSING = "NA"


def pais_colt_a_nuestro(nombre_colt):
    """Traduce el nombre de pais tal como lo escribe COLT (ej. 'Holy See') al nombre
    que usa nuestro esquema (ej. 'Vatican City', la clave real en REGION_MAP). Sin esto,
    las filas insertadas automaticamente desde COLT quedan con un nombre de pais que
    schema.py no reconoce y Destination_Region sale 'NA' en el QC."""
    if nombre_colt is None:
        return nombre_colt
    return _ALIAS_COLT_A_NUESTRO.get(nombre_colt, nombre_colt)


# Palabras clave para el fallback de Tema_Foro/Visit_Subtype cuando no hay evidencia
# mas especifica (ver "regla del mandato fundacional" en schema.py: agenda amplia ->
# Cooperacion Politica General; mandato economico-comercial -> Comercio/Integracion).
_REGIONAL_KEYWORDS = ["mercosur", "unasur", "celac", "oas", "organization of american states",
                       "iberoamerican", "ibero-american", "cumbre de las americas",
                       "summit of the americas", "andean", "alianza del pacifico",
                       "pacific alliance", "rio group", "grupo de rio", "prosur", "alba"]
_GLOBAL_KEYWORDS = ["united nations", "un general assembly", "unga", "g20", "g7", "davos",
                     "world economic forum", "cop", "climate", "wto", "world trade",
                     "imf", "world bank", "fmi", "bm "]


def _yn_to_bool(v):
    if v is None:
        return SCHEMA_MISSING
    v = str(v).strip().lower()
    if v == "yes":
        return "TRUE"
    if v == "no":
        return "FALSE"
    return SCHEMA_MISSING


def derivar_campos_desde_colt(ws, idx, excel_row, destino_traducido, trip_objective):
    """Deriva mecanicamente, a partir de las propias columnas de COLT, todos los campos
    de una fila nueva que SI tienen una regla ya establecida en el proyecto (no
    narrativa/subjetiva). Devuelve un dict listo para .update() sobre nueva_fila.

    - Visit_Category: regla ya usada en 08_ANALISIS_R (Multilateral si
      AttendedMultilatEvent=Yes; si no, Bilateral si MetHostHoGS=Yes; si no, Other).
    - Los 7 campos de micro-conducta: copiados directo de COLT (mismo criterio que la
      migracion de esquema del 2026-08-03: Yes/No -> TRUE/FALSE, MISSING si no hay dato).
    - Counterpart_Event: HostHOGSName (Bilateral) o NameMultilatEvent (Multilateral).
    - Counterpart_Type: "Jefe de Estado/Gobierno" si Bilateral (caso por defecto
      documentado en schema.py), MISSING si no.
    - Tema_Foro / Visit_Subtype: heuristica por palabras clave sobre NameMultilatEvent/
      Notes/Trip_Objective, con fallback documentado (Cooperacion Politica General /
      Working Visit) si no hay match especifico -- NO es narrativa fina, es un
      placeholder no bloqueante. Revisar a mano para pulir (ver PENDIENTES_VERIFICACION).
    """
    met_host = ws.cell(row=excel_row, column=idx["MetHostHoGS"]).value
    attended_multi = ws.cell(row=excel_row, column=idx["AttendedMultilatEvent"]).value
    name_multi = ws.cell(row=excel_row, column=idx["NameMultilatEvent"]).value or ""
    host_name = ws.cell(row=excel_row, column=idx["HostHOGSName"]).value or ""
    met_nonhost = ws.cell(row=excel_row, column=idx["MetNonhostHOGS"]).value
    nonhost_names = ws.cell(row=excel_row, column=idx["NonhostHOGSNames"]).value or ""
    public_addr = ws.cell(row=excel_row, column=idx["PublicAddress"]).value
    signed = ws.cell(row=excel_row, column=idx["SignedAgreement"]).value
    cultural = ws.cell(row=excel_row, column=idx["CulturalSiteOrCeremony"]).value
    biz = ws.cell(row=excel_row, column=idx["BusinessLeaderOrForum"]).value
    met_igo = ws.cell(row=excel_row, column=idx["MetIGOLeader"]).value
    igo_name = ws.cell(row=excel_row, column=idx["IGOLeaderName"]).value or ""
    notes = ws.cell(row=excel_row, column=idx["Notes"]).value or ""

    if str(attended_multi).strip().lower() == "yes":
        vcat = "Multilateral"
    elif str(met_host).strip().lower() == "yes":
        vcat = "Bilateral"
    elif str(met_host).strip().lower() == "no":
        vcat = "Other"
    else:
        vcat = "Other"  # fallback conservador: sin evidencia de reunion ni multilateral

    campos = {
        "Visit_Category": vcat,
        "Destination_Region": region_for(destino_traducido),
        "MetHostHOGS": _yn_to_bool(met_host),
        "MetNonHostHOGS": _yn_to_bool(met_nonhost),
        "PublicAddress": _yn_to_bool(public_addr),
        "SignedAgreement": _yn_to_bool(signed),
        "CulturalSiteOrCeremony": _yn_to_bool(cultural),
        "BusinessLeaderOrForum": _yn_to_bool(biz),
        "MetIGOLeader": _yn_to_bool(met_igo),
    }
    campos["NonHostHOGS_Name"] = nonhost_names.strip() if (campos["MetNonHostHOGS"] == "TRUE" and nonhost_names.strip()) else SCHEMA_MISSING
    campos["IGOLeader_Name"] = igo_name.strip() if (campos["MetIGOLeader"] == "TRUE" and igo_name.strip()) else SCHEMA_MISSING

    if vcat == "Bilateral" and host_name.strip():
        campos["Counterpart_Event"] = host_name.strip()
    elif vcat == "Multilateral" and name_multi.strip():
        campos["Counterpart_Event"] = name_multi.strip()
    elif notes.strip():
        campos["Counterpart_Event"] = notes.strip()[:200]
    else:
        campos["Counterpart_Event"] = SCHEMA_MISSING

    campos["Counterpart_Type"] = "Jefe de Estado/Gobierno" if vcat == "Bilateral" else SCHEMA_MISSING

    if vcat == "Multilateral":
        nm_low = name_multi.lower()
        if any(k in nm_low for k in ["clima", "climate", "cop"]):
            tema = "Medio Ambiente/Clima"
        elif any(k in nm_low for k in ["comercio", "trade", "economic", "economica", "integracion"]):
            tema = "Comercio/Integración Económica"
        elif any(k in nm_low for k in ["salud", "health"]):
            tema = "Salud"
        elif any(k in nm_low for k in ["seguridad", "security", "defensa"]):
            tema = "Seguridad"
        else:
            tema = "Cooperación Política General"  # fallback documentado en schema.py
        campos["Tema_Foro"] = tema
    else:
        campos["Tema_Foro"] = SCHEMA_MISSING

    combined_text = (name_multi + " " + notes + " " + (trip_objective or "")).lower()
    if vcat == "Multilateral":
        subtype = "Global Forum" if any(k in combined_text for k in _GLOBAL_KEYWORDS) else "Regional Summit"
    elif vcat == "Bilateral":
        if any(k in combined_text for k in ["asuncion", "asunción", "inaugura", "investidura", "funeral", "inauguration"]):
            subtype = "Inauguration/Funeral"
        elif any(k in combined_text for k in ["medic", "salud", "health", "hospital"]):
            subtype = "Transit/Medical"
        elif any(k in combined_text for k in ["visita de estado", "state visit"]):
            subtype = "State Visit"
        else:
            subtype = "Working Visit"  # default generico documentado
    else:  # Other
        subtype = "Working Visit"  # mismo criterio que los casos "Other" preexistentes
    campos["Visit_Subtype"] = subtype

    return campos

# Mapeo de campo "en lenguaje humano" que usan los subagentes -> columna real de
# cada lado. Agregar entradas nuevas aca si un subagente reporta un campo que no
# esta todavia mapeado (mejor que fallar en silencio).
CAMPO_A_COLUMNAS = {
    "Start_Date":       {"colt": "TripStartDate", "our": "Start_Date"},
    "End_Date":         {"colt": "TripEndDate", "our": "End_Date"},
    "Duration_Days":    {"colt": "TripDuration", "our": "Duration_Days"},
    "Destination_City": {"colt": "CityVisited", "our": "Destination_City"},
}

HOY = datetime.date.today().isoformat()


def cargar_json(paths):
    items = []
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        # aceptar tanto {"resultados": [...]} como una lista pelada
        items.extend(data.get("resultados", data) if isinstance(data, dict) else data)
    return items


def cargar_excel():
    wb = openpyxl.load_workbook(XLSX_PATH)
    ws = wb[SHEET_NAME]
    headers = [c.value for c in ws[1]]
    idx = {h: i + 1 for i, h in enumerate(headers)}
    tripid_row = {}
    for r in range(2, ws.max_row + 1):
        tid = ws.cell(row=r, column=idx["TripID"]).value
        if tid:
            tripid_row[str(tid)] = r
    return wb, ws, idx, tripid_row


def cargar_nuestro_csv(slug_pais):
    ruta = PROJECT_ROOT / "03_MODULOS_PAIS" / slug_pais / f"{slug_pais}_viajes.csv"
    with open(ruta, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    by_id = {r["Trip_ID"]: r for r in rows}
    return ruta, fieldnames, rows, by_id


def guardar_nuestro_csv(ruta, fieldnames, rows):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def anotar_nota_excel(ws, idx, row, texto):
    actual = ws.cell(row=row, column=idx["Notes"]).value or ""
    ws.cell(row=row, column=idx["Notes"]).value = (actual + f" [PE-Latam {HOY}: {texto}]").strip()


def anotar_nota_csv(row_dict, texto):
    actual = row_dict.get("Methodological_Notes") or ""
    row_dict["Methodological_Notes"] = (actual + f" [PE-Latam {HOY}: {texto}]").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug_pais")
    ap.add_argument("json_files", nargs="+")
    ap.add_argument("--aplicar", action="store_true", help="Si no se pasa, corre en dry run (no escribe nada).")
    ap.add_argument("--insertar-en-nuestra-base", action="store_true",
                     help="Ademas de corregir COLT, inserta en nuestro CSV las colt_unico marcadas 'agregar'. "
                          "Revisar el resultado a mano: la insercion automatica arma Journey_ID/Trip_ID nuevos "
                          "pero varios campos narrativos (Trip_Objective, Counterpart_Event, Source_Verification) "
                          "se completan solo con lo que haya en 'justificacion'/'fuente' del subagente.")
    args = ap.parse_args()

    items = cargar_json(args.json_files)
    print(f"Items cargados: {len(items)}  |  Modo: {'APLICAR' if args.aplicar else 'DRY RUN (no se escribe nada)'}")

    wb, ws, idx, tripid_row = cargar_excel()
    csv_ruta, fieldnames, csv_rows, csv_by_id = cargar_nuestro_csv(args.slug_pais)

    log_rows = []
    n_colt_corregido = 0
    n_nuestro_corregido = 0
    n_no_verificable = 0
    n_colt_unico_agregar = 0
    n_colt_unico_descartar = 0
    no_encontrados = []

    max_trip_id = max((int(r["Trip_ID"]) for r in csv_rows if str(r["Trip_ID"]).isdigit()), default=0)

    for item in items:
        tipo = item.get("tipo", "discrepancia" if "veredicto" in item else "colt_unico")
        colt_tid = str(item.get("colt_TripID", ""))
        excel_row = tripid_row.get(colt_tid)

        if tipo == "discrepancia":
            veredicto = item.get("veredicto")
            campo = item.get("campo", "")
            cols = CAMPO_A_COLUMNAS.get(campo.split("/")[0].strip())
            if excel_row is None:
                no_encontrados.append(colt_tid)
                continue

            if veredicto in ("No_verificable", None):
                n_no_verificable += 1
                if args.aplicar:
                    anotar_nota_excel(ws, idx, excel_row, f"campo {campo} queda en revision -{item.get('justificacion','')[:150]}-")
                log_rows.append([colt_tid, item.get("our_Trip_ID"), tipo, veredicto, campo, "", item.get("fuente"), item.get("justificacion")])
                continue

            if veredicto == "nuestro_correcto" and cols:
                valor = item.get("valor_correcto")
                if args.aplicar:
                    valor_viejo = ws.cell(row=excel_row, column=idx[cols["colt"]]).value
                    ws.cell(row=excel_row, column=idx[cols["colt"]]).value = valor
                    anotar_nota_excel(ws, idx, excel_row, f"{cols['colt']} corregido de '{valor_viejo}' a '{valor}' (nuestra investigacion). Fuente: {item.get('fuente','')[:150]}")
                n_colt_corregido += 1

            elif veredicto == "COLT_correcto" and cols:
                our_tid = str(item.get("our_Trip_ID", ""))
                row_dict = csv_by_id.get(our_tid)
                if row_dict is not None:
                    valor = item.get("valor_correcto")
                    if args.aplicar:
                        valor_viejo = row_dict.get(cols["our"])
                        row_dict[cols["our"]] = valor
                        anotar_nota_csv(row_dict, f"{cols['our']} corregido de '{valor_viejo}' a '{valor}' (COLT tenia razon). Fuente: {item.get('fuente','')[:150]}")
                    n_nuestro_corregido += 1
                else:
                    no_encontrados.append(f"our_Trip_ID={our_tid}")

            log_rows.append([colt_tid, item.get("our_Trip_ID"), tipo, veredicto, campo, item.get("valor_correcto"), item.get("fuente"), item.get("justificacion")])

        elif tipo == "colt_unico":
            decision = item.get("decision")
            if decision == "descartar":
                n_colt_unico_descartar += 1
                if args.aplicar and excel_row:
                    anotar_nota_excel(ws, idx, excel_row, f"Revisado, no corresponde agregarlo a nuestra base -{item.get('justificacion','')[:150]}-")
            elif decision == "agregar":
                n_colt_unico_agregar += 1
                if args.aplicar and args.insertar_en_nuestra_base and excel_row:
                    max_trip_id += 1
                    destino = pais_colt_a_nuestro(ws.cell(row=excel_row, column=idx["CountryVisited"]).value)
                    # Default "NA" (MISSING) en vez de "" para respetar la convencion del
                    # proyecto (schema.py) -las columnas narrativas/de clasificacion cerrada
                    # (Visit_Category, Visit_Subtype, Counterpart_Event, Counterpart_Type,
                    # Tema_Foro) quedan explicitamente pendientes de revision manual, ver nota.
                    # Origin_Country: no viene de COLT (es el pais del mandatario, no del
                    # destino) -se toma del resto de filas ya cargadas del mismo modulo,
                    # ya que todo el CSV comparte un unico Origin_Country por diseño.
                    origin_country = next((r.get("Origin_Country") for r in csv_rows if r.get("Origin_Country")), "NA")
                    trip_objective_txt = item.get("justificacion", "")[:250]
                    fuente_txt = item.get("fuente", "")
                    # Verificacion_Status es un dominio cerrado (schema.py DOM_VERIF_STATUS:
                    # Verificada-URL | Solo-Query | No-verificable) -NO admite texto narrativo
                    # libre-. Se deriva con el mismo criterio que usa schema.py en otros
                    # lugares del proyecto (línea "auto-Verificacion_Status" de new_row()):
                    # URL real -> Verificada-URL, si no -> Solo-Query. El detalle narrativo
                    # (que campos quedaron con heuristica de fallback) va en Methodological_Notes.
                    verif_status = "Verificada-URL" if fuente_txt.strip().lower().startswith("http") else "Solo-Query"
                    nueva_fila = {fn: "NA" for fn in fieldnames}
                    nueva_fila.update({
                        "Trip_ID": str(max_trip_id),
                        "Journey_ID": f"COLT-{colt_tid}",
                        "President": ws.cell(row=excel_row, column=idx["LeaderFullName"]).value,
                        "Origin_Country": origin_country,
                        "Trip_Status": "Completed",
                        "Start_Date": str(ws.cell(row=excel_row, column=idx["TripStartDate"]).value)[:10],
                        "End_Date": str(ws.cell(row=excel_row, column=idx["TripEndDate"]).value)[:10],
                        "Duration_Days": ws.cell(row=excel_row, column=idx["TripDuration"]).value,
                        "Destination_Country": destino,
                        "Destination_City": ws.cell(row=excel_row, column=idx["CityVisited"]).value,
                        "Trip_Objective": trip_objective_txt,
                        "Source_Verification": fuente_txt,
                        "Source_Reliability": "Medium",
                        "Verificacion_Status": verif_status,
                        "Methodological_Notes": f"[PE-Latam {HOY}: fila insertada automaticamente desde COLT TripID {colt_tid} via colt_aplicar_verificacion.py. Visit_Category/Destination_Region/micro-conducta derivados mecanicamente de COLT; Tema_Foro/Visit_Subtype/Counterpart_Event con heuristica de fallback -revisar a mano, ver PENDIENTES_VERIFICACION.txt-.]",
                    })
                    # Derivacion mecanica (fix permanente 2026-08-24: antes esto solo se hacia
                    # a mano en un script de reparacion aparte para Paraguay; ahora queda
                    # integrado en el pipeline para que no haga falta repetirlo cada pais).
                    nueva_fila.update(derivar_campos_desde_colt(ws, idx, excel_row, destino, trip_objective_txt))
                    csv_rows.append(nueva_fila)
                    anotar_nota_excel(ws, idx, excel_row, f"Agregada a nuestra base como Trip_ID {max_trip_id}")
            elif decision in ("No_verificable", None):
                n_no_verificable += 1
                if args.aplicar and excel_row:
                    anotar_nota_excel(ws, idx, excel_row, f"Pendiente de decision -{item.get('justificacion','')[:150]}-")
            log_rows.append([colt_tid, "", tipo, decision, "", "", item.get("fuente"), item.get("justificacion")])

    print(f"\nResumen:")
    print(f"  Discrepancias -> COLT corregido:      {n_colt_corregido}")
    print(f"  Discrepancias -> nuestra base corregida: {n_nuestro_corregido}")
    print(f"  colt_unico -> marcadas para agregar:  {n_colt_unico_agregar}  (insertadas en CSV: {'si' if args.insertar_en_nuestra_base else 'NO -pasar --insertar-en-nuestra-base-'})")
    print(f"  colt_unico -> descartadas:            {n_colt_unico_descartar}")
    print(f"  No_verificable / pendientes:          {n_no_verificable}")
    if no_encontrados:
        print(f"  TripID/Trip_ID no encontrados (revisar a mano): {no_encontrados[:20]}{' ...' if len(no_encontrados) > 20 else ''}")

    if args.aplicar:
        wb.save(XLSX_PATH)
        guardar_nuestro_csv(csv_ruta, fieldnames, csv_rows)
        outdir = PROJECT_ROOT / "05_BITACORA" / "anexos_colt_sudamerica"
        outdir.mkdir(parents=True, exist_ok=True)
        log_path = outdir / f"cambios_aplicados_{args.slug_pais}_{HOY}.csv"
        with open(log_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["colt_TripID", "our_Trip_ID", "tipo", "veredicto_o_decision", "campo", "valor_correcto", "fuente", "justificacion"])
            w.writerows(log_rows)
        print(f"\nGuardado. Log de cambios: {log_path}")
        print("Recordatorio: actualizar bitacora.txt y PENDIENTES_VERIFICACION.txt a mano con un resumen de esta tanda.")
    else:
        print("\nDRY RUN: no se modifico ningun archivo. Revisar el resumen de arriba y volver a correr con --aplicar.")


if __name__ == "__main__":
    main()
