# -*- coding: utf-8 -*-
"""
aplicar_verificacion_nk.py - Campana de verificacion, tanda Nestor Kirchner
(Argentina, 2003-2007), investigacion 2026-07-21.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")

VERIF = {
    "26": ("https://cancilleria.gob.ar/en/node/34001", "High"),
    "43": ("http://archivo.presidencia.gub.uy/_web/noticias/2005/03/2005030111.htm", "High"),
    "46": ("https://www.cfkargentina.com/nestor-kirchner-en-las-naciones-unidas-en-2005/", "High"),
    "49": ("https://www.lanacion.com.ar/politica/al-final-morales-visitara-a-kirchner-nid770255/", "Medium"),
    "50": ("https://nacionalypopular.com/2007/01/19/cumbre-mercosur-kirchner-pide-un-banco-del-sur/", "Medium"),
    "51": ("https://www.pagina12.com.ar/diario/economia/2-83587-2007-04-18.html", "Medium"),
    "52": ("https://www.casarosada.gob.ar/informacion/archivo/24237-blank-64020423", "High"),
}

NOTES = {
    "26": "Fuente oficial (Cancilleria) confirma discurso de Kirchner en la XXIV Cumbre del MERCOSUR en Asuncion, 18-jun-2003, con la propuesta del Instituto Monetario/moneda comun.",
    "43": "Fuente oficial (Presidencia de Uruguay, transcripcion del discurso de asuncion de Vazquez, 1-mar-2005) menciona explicitamente a Kirchner y confirma la firma de un acuerdo bilateral de DDHH al dia siguiente, lo que acredita su presencia fisica en Montevideo.",
    "46": "Fuente oficial (transcripcion del discurso, sitio institucional cfkargentina.com) confirma fecha exacta 14-set-2005 y contenido (FMI, Malvinas). No se hallo fuente que confirme el bilateral puntual con Putin mencionado en Trip_Objective; se mantiene sin corregir por falta de evidencia en contra.",
    "49": "La Nacion (6-ene-2006) confirma el anuncio oficial del gobierno argentino de que Kirchner asistiria a la asuncion de Evo Morales en La Paz el 22-ene-2006; cobertura internacional (Deseret News/AP) confirma su presencia efectiva en la ceremonia.",
    "50": "Cobertura de agencias (ANSA/EFE, republicada) confirma presencia de Kirchner en la Cumbre del MERCOSUR en Rio de Janeiro, 18-19 ene-2007, con pedido de Banco del Sur, Gasoducto del Sur y moneda unica.",
    "51": "Pagina/12 (enviado especial a Isla Margarita) confirma presencia de Kirchner en la I Cumbre Energetica Suramericana, 16-17 abr-2007 (aunque se retiro unas horas antes del cierre de las deliberaciones).",
    "52": "Fuente oficial (Casa Rosada, archivo de discursos) transcribe las palabras de Kirchner en la Cumbre del MERCOSUR en Asuncion, viernes 29-jun-2007.",
}

def append_note(existing, nota):
    if existing in ("NA", "", None):
        return nota
    return existing.rstrip(".") + ". " + nota

def process():
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    n_verif = 0
    for r in rows:
        tid = r["Trip_ID"]
        if r.get("President") != "Néstor Kirchner":
            continue
        if tid not in VERIF:
            continue
        url, rel = VERIF[tid]
        r["Source_Verification"] = url
        r["Source_Reliability"] = rel
        r["Verificacion_Status"] = "Verificada-URL"
        if tid in NOTES:
            r["Methodological_Notes"] = append_note(r["Methodological_Notes"], NOTES[tid])
        n_verif += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"argentina (Nestor Kirchner): filas verificadas={n_verif}")

if __name__ == "__main__":
    process()
