# -*- coding: utf-8 -*-
"""
aplicar_verificacion_uruguay_tanda1.py — Campana de verificacion Solo-Query -> Verificada-URL,
Uruguay: Jorge Batlle, Tabare Vazquez (ambos mandatos), Jose Mujica, Luis Lacalle Pou, Yamandu Orsi.
Investigacion 2026-07-21. Idempotente.

CLAVE DE MATCH: Trip_ID (dentro de uruguay_viajes.csv, estable en este modulo).

Prioridad especial: gira europea de Mujica oct-2011 (Estocolmo/Oslo/Berlin/Bruselas), donde
las 4 filas compartian el mismo rango de fechas (2011-10-11 a 2011-10-20), copiado del total
de la gira. Se corrigen con las fechas reales de cada tramo (fuente: El Observador, 14-oct-2011,
que ubica el inicio en Suecia el miercoles 12-oct y Noruega jueves13/viernes14; ademas Merkel-Mujica
en Berlin el martes 18-oct tras Hamburgo el lunes17; y Belgica desde el miercoles19-oct, ultima etapa).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "uruguay", "uruguay_viajes.csv")

# Trip_ID -> (url, reliability)
VERIF = {
    # ---- Jorge Batlle ----
    "8": ("https://www.pagina12.com.ar/diario/elpais/1-5946-2002-06-05.html", "Medium"),
    "10": ("http://archivo.presidencia.gub.uy/noticias/archivo/2002/noviembre/2002112105.htm", "High"),
    # ---- Tabare Vazquez (T1 y T2) ----
    "33": ("https://www.infobae.com/teleshow/2023/07/07/lejos-de-la-teve-y-a-16-anos-de-su-historica-protesta-en-la-cumbre-de-viena-evangelina-carrozzo-se-lanza-a-la-politica/", "Medium"),
    "88": ("https://www.presidencia.gob.ec/tabare-vazquez-arribo-a-quito-para-la-reunion-con-presidentes-de-colombia-y-venezuela/", "High"),
    "89": ("https://www.gub.uy/presidencia/comunicacion/noticias/vazquez-partio-hacia-nueva-york-para-participar-70a-asamblea-general-onu", "High"),
    "93": ("https://www.gub.uy/presidencia/comunicacion/noticias/presidente-vazquez-comenzo-gira-oficial-austria-egipto-suiza", "High"),
    "94": ("https://www.gub.uy/presidencia/comunicacion/noticias/presidente-vazquez-comenzo-gira-oficial-austria-egipto-suiza", "High"),
    # ---- Jose Mujica ----
    "55": ("https://www.cnnchile.com/mundo/el-vinculo-transversal-de-mujica-con-chile_20250513/", "Medium"),
    "57": ("https://cancilleria.gob.ar/es/actualidad/comunicados/xli-cumbre-del-mercosur-comunicado-conjunto-de-los-presidentes-de-los-estados", "High"),
    "58": ("https://elcomercio.pe/politica/gobierno/ollanta-humala-juramento-como-presidente-republica-constitucion-79-noticia-948935/", "Medium"),
    "59": ("https://www.elobservador.com.uy/nota/merkel-definio-la-agenda-para-reunirse-con-mujica-2011101410560", "Medium"),
    "60": ("https://www.elobservador.com.uy/nota/merkel-definio-la-agenda-para-reunirse-con-mujica-2011101410560", "Medium"),
    "61": ("https://www.elobservador.com.uy/nota/merkel-definio-la-agenda-para-reunirse-con-mujica-2011101410560", "Medium"),  # bonus, ya estaba Verificada-URL
    "62": ("https://www.elobservador.com.uy/nota/merkel-definio-la-agenda-para-reunirse-con-mujica-2011101410560", "Medium"),
    "63": ("https://www.gub.uy/presidencia/comunicacion/noticias/presidente-mujica-fue-recibido-honores-porto-alegre-inicia-visita-trabajo", "High"),
    "65": ("https://es.wikipedia.org/wiki/VI_Cumbre_de_las_Am%C3%A9ricas", "Medium"),
    "66": ("https://www.cancilleria.gob.ar/es/actualidad/comunicados/cumbre-del-mercosur-mendoza-2012-decision-sobre-la-suspension-del-paraguay-en", "High"),
    "80": ("https://albaciudad.org/2014/07/en-video-el-impactante-discurso-de-jose-pepe-mujica-en-la-cumbre-de-mercosur/", "Medium"),
    "81": ("https://www.elonce.com/internacionales/discurso-de-mujica-en-la-cumbre-del-mercosur-realizada-en-parana-soy-apenas-un-luchador-social.htm", "Medium"),
    "82": ("https://segib.org/es/cumbre/xxiv-cumbre-iberoamericana/", "High"),
    # ---- Luis Lacalle Pou ----
    "130": ("https://www.infobae.com/politica/2024/07/17/javier-milei-recibio-a-lacalle-pou-en-la-casa-rosada-despues-de-las-tensiones-por-su-ausencia-en-la-cumbre-del-mercosur/", "Medium"),
    "132": ("https://www.teledoce.com/telemundo/nacionales/lacalle-pou-cancelo-su-viaje-a-ecuador-tras-fallecimiento-de-larranaga/", "Medium"),
    # ---- Yamandu Orsi (URL ya presente en el CSV; se confirma y se sube el status) ----
    "141": ("https://www.elobservador.com.uy/nacional/la-gira-orsi-europa-entrega-escultura-pablo-atchugarry-y-reuniones-el-papa-leon-xiv-rey-belgica-y-autoridades-union-europea-n6019236", "Medium"),
}

# Trip_ID -> dict de correcciones de fecha/duracion (y nota)
DATE_FIX = {
    "88": dict(Start_Date="2015-09-21", End_Date="2015-09-21", Duration_Days="1",
               nota="NOTA 2026-07-21: fuente oficial (Presidencia de Ecuador, 21-sep-2015) "
                    "confirma que Vazquez arribo a Quito el 21-sep-2015 (no el 1-sep como figuraba); "
                    "reunion Santos-Maduro-Correa-Vazquez el mismo dia. Se corrige Start_Date/End_Date/Duration_Days."),
    "93": dict(Start_Date="2017-05-31", End_Date="2017-06-01", Duration_Days="2",
               nota="NOTA 2026-07-21: itinerario oficial de la gira (gub.uy, 28-may-2017) ubica la "
                    "llegada a El Cairo el miercoles 31-may-2017 (no el 1-jun) y reuniones adicionales "
                    "el jueves 1-jun; se corrige Start_Date de 01-jun a 31-may y Duration_Days de 1 a 2. "
                    "HALLAZGO: la gira completa fue Austria-Egipto-Suiza (Viena/OIEA el 30-may no cargado "
                    "como tramo propio en este Journey_ID; candidato a alta futura)."),
    "59": dict(Start_Date="2011-10-12", End_Date="2011-10-12", Duration_Days="1",
               nota="NOTA 2026-07-21 (correccion prioritaria, fechas duplicadas de la gira): El Observador "
                    "(14-oct-2011) ubica el inicio de la gira europea 'el pasado miercoles [12-oct] en Suecia'; "
                    "se corrigen Start_Date/End_Date/Duration_Days (antes 11 al 20-oct, rango total de gira "
                    "copiado por error en las 4 filas de Estocolmo/Oslo/Berlin/Bruselas)."),
    "60": dict(Start_Date="2011-10-13", End_Date="2011-10-14", Duration_Days="2",
               nota="NOTA 2026-07-21: El Observador (14-oct-2011) indica que la gira 'prosiguio ayer [13-oct] "
                    "y este viernes [14-oct] en Noruega'; se corrigen fechas (antes 11 al 20-oct, duplicado)."),
    "61": dict(Start_Date="2011-10-17", End_Date="2011-10-18", Duration_Days="2",
               nota="NOTA 2026-07-21 (correccion complementaria, fuera de la tanda pedida pero mismo error de "
                    "fechas duplicadas del Journey): El Observador (14-oct-2011) precisa que Mujica llega a "
                    "Berlin el martes 18-oct procedente de Hamburgo, donde disertó el lunes 17-oct; agenda con "
                    "Wulff y Merkel el 18-oct. Se corrigen Start_Date/End_Date/Duration_Days (antes 11 al 20-oct)."),
    "62": dict(Start_Date="2011-10-19", End_Date="2011-10-20", Duration_Days="2",
               nota="NOTA 2026-07-21: El Observador (14-oct-2011) anticipa que 'Mujica viajara el proximo "
                    "miercoles [19-oct] a Belgica, ultima etapa de su gira europea'; se corrigen fechas "
                    "(antes 11 al 20-oct, rango total duplicado)."),
    "63": dict(Start_Date="2011-11-08", End_Date="2011-11-09", Duration_Days="2",
               nota="NOTA 2026-07-21: fuente oficial (Presidencia, 08-nov-2011) confirma arribo a Porto Alegre "
                    "el 8-nov-2011 e inicio de visita de trabajo de DOS dias (8-9 nov); se corrige de 15-19 nov "
                    "(fecha incorrecta, posible confusion con otro tramo). HALLAZGO: el Trip_ID 64 (Guadalajara, "
                    "mismo Journey_ID URU-JM-J006) sigue fechado 15-19 nov y no fue tocado en esta tanda (fuera "
                    "del alcance pedido); queda una inconsistencia interna de Journey a revisar."),
    "57": dict(nota="NOTA 2026-07-21: el Comunicado Conjunto de la XLI Cumbre del MERCOSUR (Cancilleria "
                    "Argentina) confirma la cumbre en Asuncion el 28-29-jun-2011 con Mujica presente (traspaso "
                    "de PPT Paraguay->Uruguay); fechas de la fila (29-30 jun) son consistentes. ACLARACION: la "
                    "mencion a 'bicentenario' en el objetivo corresponde a otro viaje de Mujica a Asuncion "
                    "(bicentenario de la independencia paraguaya, 14-15 mayo 2011, LR21) NO capturado en esta "
                    "fila ni con Trip_ID propio en el modulo; candidato a alta futura."),
    "141": dict(nota="NOTA 2026-07-21: confirmado post-facto (El Observador) que Orsi se reunio en Bruselas "
                     "el 15-oct-2025 con el presidente del Consejo Europeo (Costa), la presidenta del "
                     "Parlamento Europeo (Metsola) y autoridades belgas, dentro de la gira Bruselas-Roma-Vaticano; "
                     "se levanta la marca DUDOSO anterior."),
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
    print(f"uruguay (tanda1): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
