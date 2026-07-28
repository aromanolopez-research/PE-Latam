# -*- coding: utf-8 -*-
"""
aplicar_verificacion_cfk.py — Campana de verificacion, tanda Cristina Fernandez de
Kirchner (Argentina, ambos mandatos 2007-2015), investigacion 2026-07-21. Idempotente.

CLAVE DE MATCH: Trip_ID (dentro de argentina_viajes.csv, estable en este modulo;
el Trip_ID del modulo NO es el mismo que en la base consolidada).

Se ejecuta en LOTES INCREMENTALES: cada corrida agrega entradas nuevas a los
diccionarios VERIF / DATE_FIX y se corre de nuevo sobre el CSV ya parcialmente
actualizado.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")

# Trip_ID -> (url, reliability)
VERIF = {
    # ---- LOTE 1 (2008-2013: Moscu, Cuba cancelado, Vina del Mar, Londres G20,
    #              Montevideo Mujica, Valparaiso Pinera, Asuncion cancelado,
    #              Montevideo Mercosur dic-2011, Montevideo Mercosur jul-2013) ----
    "65": ("https://www.ambito.com/politica/en-rusia-cristina-firmo-acuerdos-hablo-un-mundo-multipolar-y-pidio-afianzar-relaciones-n3531724", "Medium"),
    "67": ("https://www.infobae.com/2013/10/06/1513995-los-antecedentes-medicos-cristina-kirchner/", "Medium"),
    "68": ("https://www.nuevatribuna.es/articulo/mundo/zapatero-aborda-en-chile-la-respuesta-progresista-comn-a-la-crisis/20090328134625025310.html", "Medium"),
    "69": ("https://www.cfkargentina.com/homenaje-de-cristina-a-caidos-en-malvinas-londres-2009/", "High"),
    "76": ("https://www.casarosada.gob.ar/informacion/archivo/21966-blank-50795743", "High"),
    "77": ("https://www.infobae.com/2010/03/12/505349-chile-los-presidentes-y-las-fotos-del-momento-del-temblor-inesperado/", "Medium"),
    "89": ("https://www.lanacion.com.ar/politica/a-cristina-le-sienta-bien-el-negro-nid1386802/", "Medium"),
    "94": ("https://informatesalta.com.ar/nacional/cumbre-del-mercosur--cristina-kirchner-asume-la-presidencia-pro-tempore_a695d4dff583e698128b1b13a", "Medium"),
    "109": ("https://www.cfkargentina.com/cristina-cumbre-mercosur-uruguay/", "High"),
    "110": ("https://www.lanacion.com.ar/el-mundo/cristina-kirchner-participa-de-la-misa-del-papa-francisco-nid1605241/", "Medium"),
    # ---- LOTE 2 (2012-2013: Angola, G20 Los Cabos, Mercosur Brasilia, ONU 67,
    #              gira Asia Abu Dhabi/Yakarta/Hanoi, CELAC-UE Santiago) ----
    "97": ("https://www.infobae.com/2012/05/16/647893-la-presidente-llego-angola-encabezar-una-mision-comercial/", "Medium"),
    "98": ("https://www.casarosada.gob.ar/informacion/archivo/25924-la-presidenta-reitero-ante-el-primer-ministro-britanico-el-pedido-de-dialogo-sobre-malvinas", "High"),
    "99": ("https://www.perfil.com/noticias/politica/cristina-ya-esta-en-brasil-para-participar-de-la-cumbre-del-mercosur-20120731-0005.phtml", "Medium"),
    "100": ("https://enaun.cancilleria.gob.ar/es/content/discurso-de-la-presidenta-cristina-fernandez-de-kirchner", "High"),
    "102": ("https://www.lanacion.com.ar/politica/tras-dejar-emiratos-arabes-cristina-kirchner-llego-a-indonesia-nid1546143/", "Medium"),
    "103": ("https://www.lanacion.com.ar/politica/tras-dejar-emiratos-arabes-cristina-kirchner-llego-a-indonesia-nid1546143/", "Medium"),
    "104": ("https://www.lanacion.com.ar/politica/cristina-cierra-su-gira-con-la-visita-al-presidente-de-vietnam-nid1547492/", "Medium"),
    "105": ("https://www.cfkargentina.com/primera-cumbre-celac-ue-en-santiago-de-chile/", "High"),
    # ---- LOTE 3 (2013-2015: G20 San Petersburgo, ONU 68, G77+China Bolivia,
    #              BRICS Fortaleza, Mercosur Caracas, visita Estado Rusia, misa Papa Asuncion) ----
    "111": ("https://www.cfkargentina.com/cristina-cumbre-g20-rusia-san-petersburgo/", "High"),
    "112": ("https://www.cfkargentina.com/cristina-68-asamblea-onu/", "High"),
    "116": ("https://www.cfkargentina.com/g77china-hacia-un-nuevo-orden-mundial-para-vivir-bien/", "High"),
    "117": ("https://www.casarosada.gob.ar/informacion/archivo/27716-cumbre-de-paises-del-brics-y-unasur-en-brasilia-palabras-de-la-presidenta-de-la-nacion", "High"),
    "118": ("https://www.cfkargentina.com/discurso-cristina-kirchner-en-la-46a-cumbre-de-jefes-y-jefas-de-estado-del-mercosur/", "High"),
    "122": ("https://www.infobae.com/2015/04/23/1724160-cristina-kirchner-se-reunio-putin/", "Medium"),
    "123": ("https://www.casarosada.gob.ar/informacion/archivo/28857-la-presidenta-asiste-a-la-misa-que-ofrece-el-papa-francisco-en-asuncion-paraguay", "High"),
}

# Trip_ID -> dict de correcciones de fecha/duracion (y nota)
DATE_FIX = {
    "104": dict(End_Date="2013-01-21", Duration_Days="3",
                nota="NOTA 2026-07-21: LA NACION (21-ene-2013) ubica la llegada a Hanoi "
                     "la noche del 20/01 (tras pasar por Ciudad Ho Chi Minh) y la agenda "
                     "oficial (mausoleo Ho Chi Minh, bilateral con el presidente Truong Tan "
                     "Sang y el PM Nguyen Tan Dung) el 21/01; se corrige End_Date de 20 a "
                     "21-ene-2013 y Duration_Days de 2 a 3."),
}

def append_note(existing, nota):
    if existing in ("NA", "", None):
        return nota
    return existing.rstrip(".") + ". " + nota

def process():
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    n_verif = n_datefix = 0
    for r in rows:
        tid = r["Trip_ID"]
        if tid not in VERIF:
            continue
        url, rel = VERIF[tid]
        r["Source_Verification"] = url
        r["Source_Reliability"] = rel
        r["Verificacion_Status"] = "Verificada-URL"
        n_verif += 1

        if tid in DATE_FIX:
            fix = DATE_FIX[tid]
            for k in ("Start_Date", "End_Date", "Duration_Days"):
                if k in fix:
                    r[k] = fix[k]
            r["Methodological_Notes"] = append_note(r["Methodological_Notes"], fix["nota"])
            n_datefix += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "NA") for c in COLUMNS})
    print(f"argentina (CFK): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
