# -*- coding: utf-8 -*-
"""
aplicar_verificacion_af.py — Campana de verificacion, Alberto Fernandez (Argentina,
2019-2023), investigacion 2026-07-21. Idempotente.

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
    # ---- LOTE 1 (gira Europa feb-2020: Roma/Berlin/Madrid; gira Europa may-2021:
    #              Lisboa/Madrid/Paris/Roma) ----
    "176": ("https://www.ambito.com/politica/alberto-fernandez/alberto-fernandez-se-reunio-el-premier-y-el-presidente-italia-n5080199", "Medium"),
    "177": ("https://www.casarosada.gob.ar/informacion/conferencias/46697-declaracion-conjunta-del-presidente-alberto-fernandez-y-la-canciller-de-alemania-angela-merkel", "High"),
    "178": ("https://www.casarosada.gob.ar/9f6t0r/slider-principal/46701-el-presidente-alberto-fernandez-se-reunio-con-el-presidente-del-gobierno-espanol-pedro-sanchez", "High"),
    "180": ("https://www.casarosada.gob.ar/slider-principal/47745-el-presidente-fue-recibido-por-su-par-de-portugal-en-el-inicio-de-su-gira-por-europa", "High"),
    "181": ("https://www.casarosada.gob.ar/informacion/conferencias/47754-declaracion-conjunta-del-presidente-de-la-nacion-alberto-fernandez-y-el-presidente-de-espana-pedro-sanchez-perez-castejon-en-el-palacio-de-la-moncloa-madrid-espana", "High"),
    "182": ("https://www.casarosada.gob.ar/informacion/actividad-oficial/9-noticias/47756-el-presidente-alberto-fernandez-llego-a-paris", "High"),
    "183": ("https://www.telesurtv.net/news/italia-apoya-argentina-negociacion-deuda-externa--20210513-0036.html", "Medium"),
    # ---- LOTE 2 (G20 Roma oct-2021, COP26 Glasgow nov-2021; gira Espana-Alemania-
    #              Francia may-2022; G7 Elmau jun-2022; ONU sept-2022; G20 Bali nov-2022) ----
    "185": ("https://www.casarosada.gob.ar/slider-principal/48184-el-presidente-ya-llego-a-roma-donde-participara-de-la-cumbre-de-lideres-del-g20", "High"),
    "186": ("https://www.casarosada.gob.ar/slider-principal/48196-el-presidente-arribo-a-glasgow-escocia-donde-manana-iniciara-su-participacion-en-la-cumbre-cop26", "High"),
    "190": ("https://diariodecuyo.com.ar/argentina/En-Berlin-Fernandez-volvio-a-proponer-alimentos-y-energia-para-Europa-20220511-0041.html", "Medium"),
    "191": ("https://www.france24.com/es/europa/20220513-alberto-fern%C3%A1ndez-se-reuni%C3%B3-con-emmanuel-macron-en-par%C3%ADs-durante-su-gira-por-europa", "Medium"),
    "192": ("https://www.casarosada.gob.ar/slider-principal/48740-el-presidente-alberto-fernandez-ya-llego-a-espana-donde-se-reunira-hoy-con-su-par-pedro-sanchez-y-el-rey-felipe-vi", "High"),
    "193": ("https://www.casarosada.gob.ar/slider-principal/48898-el-presidente-alberto-fernandez-llego-a-alemania-para-participar-de-la-cumbre-del-g7", "High"),
    "194": ("https://www.casarosada.gob.ar/slider-principal/49131-el-presidente-arribo-a-nueva-york-para-exponer-ante-la-asamblea-general-de-la-onu", "High"),
    "195": ("https://www.casarosada.gob.ar/slider-principal/49364-el-presidente-llego-a-bali-para-participar-de-la-cumbre-del-g20", "High"),
    # ---- LOTE 3 (cumbre sudamericana Brasilia may-2023, G20 Nueva Delhi sep-2023,
    #              ultimo discurso ONU sep-2023) ----
    "198": ("https://www.casarosada.gob.ar/slider-principal/49928-alberto-fernandez-llego-a-brasilia-para-participar-del-encuentro-de-presidentes-de-los-paises-de-america-del-sur", "High"),
    "201": ("https://www.casarosada.gob.ar/slider-principal/50162-el-presidente-arribo-a-la-india-para-participar-de-la-cumbre-del-g20", "High"),
    "202": ("https://www.casarosada.gob.ar/informacion/discursos/50192-palabras-del-presidente-de-la-nacion-alberto-fernandez-en-la-sesion-de-debate-general-del-78-periodo-de-sesiones-de-la-asamblea-general-de-naciones-unidas-en-nueva-york-estados-unidos", "High"),
}

# Trip_ID -> dict de correcciones de fecha/duracion (y nota)
DATE_FIX = {
    "176": dict(Start_Date="2020-01-31", End_Date="2020-01-31",
                nota="NOTA 2026-07-21: prensa (Ambito, Infobae) fecha las reuniones con "
                     "el PM Giuseppe Conte (Palazzo Chigi) y el presidente Sergio Mattarella "
                     "(Palacio del Quirinal) el 31/1/2020 (mismo dia que la audiencia con el "
                     "Papa, tramo previo Vaticano); se corrige Start/End_Date de 1/2 a "
                     "31/1/2020 (la fila de Ciudad del Vaticano ya cubre esa fecha por separado)."),
    "178": dict(Start_Date="2020-02-04", End_Date="2020-02-04",
                nota="NOTA 2026-07-21: fuente oficial (Casa Rosada) y La Moncloa (gob. "
                     "España) fechan el encuentro Fernandez-Sanchez y la audiencia con el "
                     "Rey Felipe VI en Madrid el 4/2/2020 (no el 5/2); se corrige Start/"
                     "End_Date. ALERTA PARA REVISION: la gira de feb-2020 tambien incluyo "
                     "Paris (almuerzo con Macron en el Eliseo, 5/2/2020, discurso en "
                     "Sciences Po 6/2/2020) segun multiples fuentes (Infobae, LA NACION, "
                     "Casa Rosada); ese tramo NO figura como fila en el modulo (J154 salta "
                     "de Madrid a fin de gira). Posible fila faltante; no se agrega de "
                     "oficio, reportado para decision del usuario."),
    "180": dict(Start_Date="2021-05-09", End_Date="2021-05-10",
                nota="NOTA 2026-07-21: fuente oficial (Casa Rosada) fecha la llegada a "
                     "Portugal y el encuentro con Rebelo de Sousa el domingo 9/5/2021 "
                     "(no el 10/5); el almuerzo con Costa y la partida hacia España fueron "
                     "el lunes 10/5. Se corrige Start/End_Date (shift -1 dia)."),
    "181": dict(Start_Date="2021-05-10", End_Date="2021-05-11",
                nota="NOTA 2026-07-21: shift -1 dia por correccion del tramo Portugal "
                     "previo (llegada a Madrid lunes 10/5/2021; declaracion conjunta con "
                     "Sanchez fechada por Casa Rosada el martes 11/5/2021, previo a partir "
                     "hacia Paris esa misma tarde)."),
    "182": dict(Start_Date="2021-05-11", End_Date="2021-05-12",
                nota="NOTA 2026-07-21: fuente oficial (Casa Rosada) fecha la llegada a "
                     "Paris el martes 11/5/2021 18:05hs, con almuerzo de trabajo con Macron "
                     "al dia siguiente (miercoles 12/5). Se corrige Start/End_Date (shift "
                     "-1 dia)."),
    "190": dict(Start_Date="2022-05-11", End_Date="2022-05-11", Duration_Days="1",
                nota="NOTA 2026-07-21: CORRECCION MAYOR. Multiples fuentes de prensa "
                     "(Infobae, El Cronista, Ambito, ElDiarioAr, La Nacion) coinciden en "
                     "que la gira de mayo-2022 comenzo en MADRID (martes 10/5, Rey Felipe "
                     "VI + Sanchez), siguio en BERLIN (miercoles 11/5, Scholz) y cerro en "
                     "PARIS (jueves 12 a viernes 13/5, Macron) - orden inverso al que tenia "
                     "la fila original (Berlin 8-11/5, 4 dias). Se corrige Start/End_Date "
                     "de Berlin a 11/5/2022 (dia unico)."),
    "191": dict(Start_Date="2022-05-12", End_Date="2022-05-13", Duration_Days="2",
                nota="NOTA 2026-07-21: ver correccion mayor de orden de la gira may-2022 "
                     "en fila de Berlin (Trip 190). Paris fue el CIERRE de la gira, no el "
                     "tramo intermedio: llegada jueves 12/5 (prensa: France24, DiarioDeCuyo), "
                     "almuerzo y declaracion con Macron viernes 13/5, regreso a Bs.As. esa "
                     "noche. Se corrige Start/End_Date de 11-12/5 a 12-13/5/2022."),
    "192": dict(Start_Date="2022-05-10", End_Date="2022-05-10", Duration_Days="1",
                nota="NOTA 2026-07-21: ver correccion mayor de orden de la gira may-2022 "
                     "en fila de Berlin (Trip 190). Madrid fue el PRIMER tramo (no el "
                     "cierre): fuente oficial (Casa Rosada) fecha la llegada y los "
                     "encuentros con Felipe VI y Sanchez el martes 10/5/2022. Se corrige "
                     "Start/End_Date de 12-13/5 a 10/5/2022 (dia unico)."),
    "198": dict(Start_Date="2023-05-29", End_Date="2023-05-30", Duration_Days="2",
                nota="NOTA 2026-07-21: CORRECCION. La fila cargaba 2-3/5/2023, pero esa "
                     "fecha corresponde a OTRA visita de Fernandez a Lula (reunion sobre "
                     "estrategia de deuda, principios de mayo). El 'Encuentro de "
                     "Presidentes de America del Sur convocado por Lula' (Consenso de "
                     "Brasilia, relanzamiento de UNASUR) que describe el objetivo de esta "
                     "fila ocurrio el 29-30/5/2023 (fuente oficial Casa Rosada + prensa "
                     "coincidente). Se corrige Start/End_Date de 2-3/5 a 29-30/5/2023."),
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
    print(f"argentina (Alberto Fernandez): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
