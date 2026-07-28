# -*- coding: utf-8 -*-
"""
aplicar_verificacion_milei.py - Campana de verificacion, tanda Javier Milei
(Argentina, 2023-en curso), investigacion 2026-07-21.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "argentina", "argentina_viajes.csv")

# Trip_ID -> (url, reliability)
VERIF = {
    "208": ("https://www.argentina.gob.ar/noticias/el-presidente-milei-se-reunio-con-el-cofundador-y-director-de-tesla-elon-musk", "High"),
    "209": ("https://www.lanacion.com.ar/politica/javier-milei-en-espana-gran-expectativa-por-su-discurso-publico-en-madrid-nid19052024/", "High"),
    "211": ("https://www.lanacion.com.ar/politica/aguardan-con-expectativa-a-milei-en-la-cumbre-del-g7-su-agenda-la-coincidencia-con-el-papa-y-un-mano-nid13062024/", "High"),
    "213": ("https://www.casarosada.gob.ar/informacion/discursos/50566-palabras-del-presidente-javier-milei-en-la-conferencia-politica-de-accion-conservadora-cpac-camboriu-brasil", "High"),
    "215": ("https://www.infobae.com/politica/2024/09/21/milei-aterrizo-en-new-york-para-hablar-en-la-onu-describir-su-programa-economico-en-wall-street-y-avanzar-en-las-conversaciones-con-musk/", "Medium"),
    "216": ("https://www.infobae.com/politica/2024/11/17/milei-llego-a-rio-de-janeiro-para-participar-en-el-g20-y-ratificar-sus-diferencias-ideologicas-con-lula-da-silva/", "Medium"),
    "217": ("https://www.batimes.com.ar/news/argentina/president-milei-praises-trump-at-mar-a-lago-event.phtml", "Medium"),
    "218": ("https://www.casarosada.gob.ar/informacion/discursos/50811-palabras-del-presidente-de-la-nacion-javier-milei-en-la-lxv-cumbre-del-mercosur-en-montevideo-uruguay", "High"),
    "220": ("https://www.casarosada.gob.ar/informacion/discursos/50848-discurso-del-presidente-de-la-nacion-javier-milei-desde-el-foro-de-davos-suiza", "High"),
    "221": ("https://www.casarosada.gob.ar/slider-principal/50868-discurso-del-presidente-javier-milei-en-el-cpac-de-washington-d-c-2025", "High"),
    "222": ("https://www.infobae.com/politica/2025/04/02/javier-milei-viaja-esta-noche-a-eeuu-el-posible-encuentro-con-trump-en-el-tramo-final-de-la-negociacion-con-el-fmi/", "Medium"),
    "223": ("https://www.lanacion.com.ar/politica/la-despedida-de-milei-ante-el-feretro-el-pedido-de-perdon-y-un-almuerzo-con-meloni-nid26042025/", "High"),
    # "224" (Leo XIV) NO se verifica -- ver DUDOSO abajo, se deja Solo-Query.
    "225": ("https://www.lanacion.com.ar/politica/javier-milei-confirmo-en-israel-que-mudara-la-embajada-argentina-de-tel-aviv-a-jerusalen-nid11062025/", "High"),
    "226": ("https://www.casarosada.gob.ar/slider-principal/51081-discurso-del-presidente-de-la-nacion-javier-milei-en-la-80-sesion-de-la-asamblea-general-de-la-onu-nueva-york", "High"),
}

# Trip_ID -> dict de correcciones de fecha/duracion + nota
DATE_FIX = {
    "208": dict(Start_Date="2024-04-12", Duration_Days="1",
                nota="NOTA 2026-07-21: fuente oficial (argentina.gob.ar, 12-abr-2024, 'hoy') confirma que la "
                     "visita a la planta de Tesla y el encuentro con Musk ocurrieron el mismo dia 12-abr-2024 "
                     "(Chequeado confirma el traslado Miami-Austin ese mismo dia); se corrige Start_Date de "
                     "11 a 12-abr-2024 (viaje de un solo dia en Texas)."),
    "213": dict(Start_Date="2024-07-06", End_Date="2024-07-07",
                nota="NOTA 2026-07-21: Chequeado (pedidos de acceso a informacion publica) e Infobae confirman "
                     "que el viaje a Camboriu fue del 6 al 7 de julio de 2024 (Milei llego la noche del sabado "
                     "6 y disertó el domingo 7), no 8-9 como figuraba. Se corrigen Start_Date y End_Date. "
                     "Ese mismo 8-jul se realizaba la Cumbre de Mercosur en Asuncion (a la que Milei NO "
                     "asistio, represento la canciller Mondino), posible origen de la confusion de fechas."),
    "215": dict(Start_Date="2024-09-21", Duration_Days="4",
                nota="NOTA 2026-07-21: Infobae confirma que Milei aterrizo en Nueva York el sabado 21-set-2024 "
                     "por la noche (vuelo especial); se corrige Start_Date de 22 a 21-set-2024. Discurso ante "
                     "la 79 AGNU el 24-set confirmado por Casa Rosada."),
    "216": dict(Start_Date="2024-11-17", Duration_Days="3",
                nota="NOTA 2026-07-21: Infobae y La Nacion (17-nov-2024) confirman que Milei aterrizo en Rio "
                     "de Janeiro la tarde/noche del 17-nov, previo al inicio formal de la Cumbre (18-19 nov); "
                     "se corrige Start_Date de 18 a 17-nov. Fuentes secundarias (Chequeado) resumen el viaje "
                     "oficial como '18 y 19 de noviembre' (fechas de la cumbre en si); se prioriza el reporte "
                     "periodistico puntual y fechado del dia de arribo."),
    "218": dict(Start_Date="2024-12-06", Duration_Days="1",
                nota="NOTA 2026-07-21: cobertura de prensa (El Chubut/Noticias Argentinas, 6-dic-2024) confirma "
                     "que Milei arribo a Montevideo la manana del 6-dic-2024 (7:32 hs) y participo de la cumbre "
                     "ese mismo dia; no hay evidencia de estadia previa el 5-dic. Se corrige Start_Date de 5 a "
                     "6-dic-2024 (viaje de un solo dia)."),
    "222": dict(Start_Date="2025-04-03", End_Date="2025-04-03", Duration_Days="1",
                nota="NOTA 2026-07-21 (CORRECCION MAYOR): Infobae (2-abr-2025) confirma que Milei partio de "
                     "Ezeiza la noche del miercoles 2-abr-2025, aterrizo en Florida la manana del jueves 3-abr "
                     "(gala 'American Patriots' en Mar-a-Lago, premio 'Leon de la Libertad') y regreso esa "
                     "misma noche del 3-abr para retomar agenda en Buenos Aires el viernes 4-abr. Las fechas "
                     "originales (7-8 abril) eran erroneas; se corrigen a 3-abr-2025 (viaje de un solo dia)."),
}

NOTE_224 = ("HALLAZGO 2026-07-21 (fila dudosa, NO verificada -- se deja Solo-Query): La Nacion "
            "(15-may-2025, 'Javier Milei no viajaria a la asuncion del papa Leon IV y se quedaria para "
            "votar en la eleccion') confirma que Milei decidio NO viajar a la misa de inicio de pontificado "
            "de Leon XIV (18-may-2025) para quedarse a votar en las legislativas porteñas; la delegacion "
            "argentina fue encabezada por el canciller Werthein y la ministra Pettovello. El primer "
            "encuentro de Milei con Leon XIV ocurrio recien el 7-jun-2025 en Roma, en un viaje distinto no "
            "incluido en este lote. Este viaje (ARG-JM-J191, 18-19 may-2025) parece NO HABERSE REALIZADO "
            "segun lo descripto; se reporta para revision del usuario (posible eliminacion de la fila o "
            "recodificacion con las fechas reales de junio 2025). NO se marca Verificada-URL.")

def append_note(existing, nota):
    if existing in ("NA", "", None):
        return nota
    return existing.rstrip(".") + ". " + nota

def process():
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    n_verif = n_datefix = n_flag = 0
    for r in rows:
        if r.get("President") != "Javier Milei":
            continue
        tid = r["Trip_ID"]

        if tid == "224":
            r["Methodological_Notes"] = append_note(r["Methodological_Notes"], NOTE_224)
            n_flag += 1
            continue

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
    print(f"argentina (Milei): filas verificadas={n_verif} | filas con correccion de fecha={n_datefix} | filas marcadas dudosas={n_flag}")

if __name__ == "__main__":
    process()
