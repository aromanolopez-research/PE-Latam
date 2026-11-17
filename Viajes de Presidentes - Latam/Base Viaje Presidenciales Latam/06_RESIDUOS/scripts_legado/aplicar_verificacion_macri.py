# -*- coding: utf-8 -*-
"""
aplicar_verificacion_macri.py — Campana de verificacion, tanda Mauricio Macri
(Argentina, 2015-2019), investigacion 2026-07-20. Idempotente.

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
    # ---- LOTE 1 (2016: Colonia, Vaticano, Washington NSS, Bogota, Puerto Varas,
    #               Lima, Rio, Doha, Hangzhou) ----
    "128": ("https://www.casarosada.gob.ar/slider-principal/44781-los-presidentes-mauricio-macri-y-tabare-vazquez-se-reunieron-en-colonia", "High"),
    "130": ("https://www.cronista.com/economia-politica/El-papa-Francisco-recibio-a-Mauricio-Macri-en-el-Vaticano-20160227-0001.html", "Medium"),
    "131": ("https://www.lanacion.com.ar/politica/desde-un-avion-rumbo-a-washington-mauricio-macri-publico-un-mensaje-sobre-usos-nucleares-nid1884825", "Medium"),
    "132": ("https://www.casarosada.gob.ar/informacion/conferencias/36574-conferencia-de-prensa-del-presidente-mauricio-macri-y-su-par-colombiano-juan-manuel-santos-en-bogota", "High"),
    "133": ("https://www.lanacion.com.ar/politica/giro-estrategico-macri-participa-hoy-de-la-cumbre-de-la-alianza-del-pacifico-nid1913920/", "Medium"),
    "138": ("https://www.casarosada.gob.ar/informacion/eventos-destacados-presi/36868-el-presidente-mauricio-macri-se-reunio-con-su-par-electo-de-peru-pedro-kuczynski", "High"),
    "139": ("https://www.infobae.com/juegos-olimpicos-rio-2016/2016/08/05/juegos-de-rio-2016-ceremonia-de-apertura/", "Medium"),
    "140": ("https://www.ambito.com/politica/en-el-inicio-su-gira-macri-se-reunio-el-emir-qatar-n3953317", "Medium"),
    "141": ("https://www.lanacion.com.ar/politica/mauricio-macri-llego-a-china-donde-participara-de-la-cumbre-del-g20-nid1933996", "Medium"),
    "143": ("https://www.lanacion.com.ar/politica/mauricio-macri-papa-francisco-reunion-el-vaticano-nid1947392/", "Medium"),
    # ---- LOTE 2 (2017: Madrid, Asuncion, Amsterdam, Washington-Trump, Dubai, Beijing OBOR, Tokio) ----
    "144": ("https://www.infobae.com/politica/2017/02/20/macri-en-espana-los-desafios-de-un-viaje-inedito-para-el-gobierno/", "Medium"),
    "145": ("https://www.lanacion.com.ar/politica/narcotrafico-macri-acordo-mas-controles-con-su-colega-paraguayo-nid1994486/", "Medium"),
    "146": ("https://www.lanacion.com.ar/politica/mauricio-macri-holanda-reina-maxima-juliana-awada-nid1999671/", "Medium"),
    "147": ("https://www.casarosada.gob.ar/slider-principal/39392-macri-fue-recibido-en-la-casa-blanca-por-el-presidente-de-los-estados-unidos", "High"),
    "148": ("https://www.casarosada.gob.ar/informacion/actividad-oficial/9-noticias/39544-el-presidente-se-reunio-con-funcionarios-y-empresarios-de-emiratos-arabes-unidos", "High"),
    "149": ("https://www.casarosada.gob.ar/slider-principal/39552-el-presidente-expuso-en-el-foro-una-franja-y-una-ruta-para-la-cooperacion-internacional", "High"),
    "150": ("https://www.casarosada.gob.ar/informacion/actividad-oficial/39653-comunicado-de-prensa-conjunto-por-la-visita-del-presidente-macri-a-japon", "High"),
    # ---- LOTE 3 (2017-2018: Quito, Santiago, Hamburgo G20, Valparaiso, Lima Cumbre
    #               de las Americas, La Malbaie G7, Nueva York AGNU/FMI/Global Citizen) ----
    "151": ("https://www.infobae.com/politica/2017/05/24/mauricio-macri-sufrio-una-leve-descompensacion-en-ecuador/", "Medium"),
    "152": ("https://www.casarosada.gob.ar/informacion/conferencias/40703-conferencia-conjunta-del-presidente-mauricio-macri-y-su-par-de-chile-michelle-bachelet", "High"),
    "153": ("https://www.infobae.com/politica/2017/07/05/mauricio-macri-partio-rumbo-a-alemania-para-participar-de-la-cumbre-del-g20/", "Medium"),
    "157": ("https://www.infobae.com/politica/2018/03/11/mauricio-macri-viajara-hoy-a-chile-para-la-asuncion-presidencial-de-sebastian-pinera/", "Medium"),
    "158": ("https://www.lanacion.com.ar/politica/mauricio-macri-en-la-cumbre-de-las-americas-la-crisis-humanitaria-en-venezuela-se-ha-vuelto-insostenible-nid2125646/", "Medium"),
    "159": ("https://www.lanacion.com.ar/politica/cumbre-del-g-7-la-foto-de-christine-lagarde-y-mauricio-macri-antes-de-su-reunion-en-canada-nid2142447/", "Medium"),
    "162": ("https://www.infobae.com/politica/2018/09/09/macri-viaja-a-nueva-york-para-hablar-en-la-onu-reunirse-con-trump-convencer-a-inversores-y-recibir-un-premio/", "Medium"),
    # ---- LOTE 4 (2019: Yakarta, Osaka G20, cancelados Paris/Bruselas y Chile APEC/COP25) ----
    "167": ("https://www.infobae.com/politica/2019/06/26/en-la-previa-del-g20-mauricio-macri-se-reunio-con-el-presidente-de-indonesia/", "Medium"),
    "168": ("https://www.batimes.com.ar/news/argentina/historic-eu-mercosur-trade-deal-gives-macri-a-g20-victory.phtml", "Medium"),
    "171": ("https://www.infobae.com/politica/2019/04/16/mauricio-macri-anuncia-el-nuevo-paquete-de-medidas-economicas-y-suspende-el-viaje-a-paris-bruselas-y-zurich-para-seguirlo-de-cerca/", "Medium"),
    "172": ("https://www.latercera.com/politica/noticia/presidente-pinera-informa-chile-ya-no-realizara-la-apec-la-cop-25/883655/", "Medium"),
}

# Trip_ID -> dict de correcciones de fecha/duracion (y nota)
DATE_FIX = {
    "146": dict(nota="NOTA 2026-07-20: fuentes de prensa (LA NACION, Cancilleria) ubican la "
                     "visita de Estado completa a los Paises Bajos entre el 24 y el 28 de marzo "
                     "de 2017 (varias ciudades/actividades); el Foro de Negocios e Inversiones "
                     "'Socios del Siglo XXI' en Amsterdam se realizo puntualmente el 27/03. "
                     "Fecha cargada (27-28) se mantiene por corresponder al tramo especifico en "
                     "Amsterdam, sin evidencia de error."),
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
    print(f"argentina (Macri): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
