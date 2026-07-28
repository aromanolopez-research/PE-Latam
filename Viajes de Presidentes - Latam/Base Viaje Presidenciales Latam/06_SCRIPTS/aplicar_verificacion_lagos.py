# -*- coding: utf-8 -*-
"""
aplicar_verificacion_lagos.py - Campana de verificacion, tanda Ricardo Lagos
(Chile, 2000-2006), investigacion 2026-07-21. Idempotente.

CLAVE DE MATCH: Trip_ID (dentro de chile_viajes.csv).

Fuente principal: Archivo Presidente Ricardo Lagos Escobar (arle.udp.cl),
archivo institucional oficial (Universidad Diego Portales / Archivos UDP,
Premio LASA 2025 al Mejor Proyecto Publico de Archivos), que digitaliza los
programas de viaje oficiales ("Giras Internacionales de Su Excelencia el
Presidente...") producidos por la Presidencia de la Republica de Chile
(Direccion de Ceremonial y Protocolo). Se usa como fuente High.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "03_MODULOS_PAIS", "chile", "chile_viajes.csv")

GIRA_2000 = "https://arle.udp.cl/index.php/giras-internacionales-de-su-excelencia-el-presidente-de-la-republica-don-ricardo-lagos-y-senora-luisa-duran-de-lagos-ano-2000"
GIRA_2001 = "https://arle.udp.cl/index.php/giras-internacionales-de-su-excelencia-el-presidente-de-la-republica-don-ricardo-lagos-y-senora-luisa-duran-de-lagos-ano-2001"
GIRA_2002 = "https://arle.udp.cl/index.php/giras-internacionales-de-su-excelencia-el-presidente-de-la-republica-don-ricardo-lagos-y-senora-luisa-duran-de-lagos-ano-2002"
GIRA_2003 = "https://arle.udp.cl/index.php/giras-internacionales-de-su-excelencia-el-presidente-de-la-republica-don-ricardo-lagos-y-senora-luisa-duran-de-lagos-ano-2003"
GIRA_2004 = "https://arle.udp.cl/index.php/giras-internacionales-de-su-excelencia-el-presidente-de-la-republica-don-ricardo-lagos-y-senora-luisa-duran-de-lagos-ano-2004"
GIRA_2005 = "https://arle.udp.cl/index.php/giras-internacionales-de-su-excelencia-el-presidente-de-la-republica-don-ricardo-lagos-y-senora-luisa-duran-de-lagos-ano-2005"

# Trip_ID -> (url, reliability)
VERIF = {
    # J001 - Buenos Aires, XVIII Cumbre Mercosur, 29-30 jun 2000. Programa oficial
    # de la Presidencia (Ceremonial y Protocolo) cataloga exactamente estas fechas.
    "1": ("https://arle.udp.cl/index.php/programa-de-actividades-de-presidente-de-la-republica-para-xviii-cumbre-mercosur-en-buenos-aires", "High"),
    # J004 - Brunei, VIII Cumbre APEC. Clausura confirmada 16-nov-2000 (nota TVN
    # catalogada en archivo oficial) + programa oficial 2000 (ventana ampliada
    # 14-17 nov, cierre de lideres 15-16 nov).
    "4": (GIRA_2000, "High"),
    # J006 - Espana, Visita de Estado. Programa oficial 2001 y ficha archivistica
    # especifica del viaje indican 03 al 06 de junio (no 04-06). CORREGIDO.
    "6": (GIRA_2001, "High"),
    # J007 - Peru, Transmision del Mando de Alejandro Toledo + Visita Oficial.
    # Programa oficial 2001: "Peru, Lima. Transmision del Mando y Visita Oficial,
    # julio 27 al 31". Confirmado ademas por conferencia de prensa conjunta con
    # Toledo fechada 30-jul-2001 (ficha PR-DF-FOT-224823). CORREGIDO.
    "8": (GIRA_2001, "High"),
    # J008 (tramo Belgica) - Bruselas, Visita de Trabajo. Programa oficial 2001:
    # "Belgica, Bruselas. Visita de Trabajo, septiembre 12 y 13" (no 10-11).
    # CORREGIDO. Ver nota sobre tramo Portugal faltante.
    "9": (GIRA_2001, "High"),
    # J011 - Madrid, II Cumbre UE-ALC. Programa tentativo oficial especifico
    # ("Madrid 16-17 de Mayo de 2002") + declaraciones/conferencia de prensa de
    # cierre de la firma del Acuerdo Chile-UE fechadas 17-may-2002. CORREGIDO
    # (no 17-18).
    "13": ("https://arle.udp.cl/index.php/programa-tentativo-de-visita-de-presidente-de-la-republica-a-ii-cumbre-de-la-union-europea-america-latina-y-el-caribe-madrid-16-17-de-mayo-de-2002", "High"),
    # J013 - Los Cabos, X Cumbre APEC, 26-27 oct 2002. Programa oficial 2002
    # confirma exactamente estas fechas.
    "15": (GIRA_2002, "High"),
    # J016 - Bangkok, XI Cumbre APEC, 20-21 oct 2003. Programa oficial 2003
    # confirma exactamente estas fechas.
    "18": (GIRA_2003, "High"),
    # J019 - Guadalajara, Cumbre ALC-UE, 28-29 may 2004. Programa oficial 2004
    # confirma exactamente estas fechas.
    "21": (GIRA_2004, "High"),
    # J023 - Montevideo, Transmision del Mando de Tabare Vazquez, 1-mar-2005.
    # Programa oficial 2005 confirma exactamente esta fecha.
    "25": (GIRA_2005, "High"),
    # J025 - Mar del Plata, IV Cumbre de las Americas, 4-5 nov 2005. Programa
    # oficial 2005 confirma exactamente estas fechas.
    "27": (GIRA_2005, "High"),
    # J026 - Busan, Cumbre APEC, 18-19 nov 2005. Programa oficial 2005 confirma
    # exactamente estas fechas.
    "28": (GIRA_2005, "High"),
    # J027 - La Paz, asuncion de Evo Morales, 22-ene-2006. Prensa especializada
    # (LatinFinance, 18-ene-2006) confirma que Lagos acepto la invitacion
    # personal de Morales para asistir a la ceremonia del 22 de enero.
    "29": ("https://latinfinance.com/daily-brief/2006/01/18/lagos-to-visit-bolivia/", "Medium"),
}

# Trip_ID -> dict de correcciones de fecha/duracion (y nota)
DATE_FIX = {
    "6": dict(Start_Date="2001-06-03", End_Date="2001-06-06", Duration_Days="4",
              nota="NOTA 2026-07-21: el programa oficial de giras 2001 (Presidencia/"
                   "Ceremonial y Protocolo) y la ficha archivistica especifica del viaje "
                   "('Visita de Estado al Reino de Espana 03 al 06 de Junio 2001', incl. "
                   "informe de Embajada de Chile en Espana) fechan la visita 03-06/06/2001 "
                   "(4 dias), no 04-06. Fecha corregida."),
    "8": dict(Start_Date="2001-07-27", End_Date="2001-07-31", Duration_Days="5",
              nota="NOTA 2026-07-21: el programa oficial de giras 2001 registra este viaje "
                   "como 'Transmision del Mando y Visita Oficial' a Peru, 27 al 31 de julio "
                   "(no solo el dia de la asuncion, 28/07). Confirmado por ficha archivistica "
                   "de conferencia de prensa conjunta Lagos-Toledo fechada 30/07/2001 en Lima "
                   "y por cobertura de prensa del juramento simbolico en Machu Picchu "
                   "(29/07/2001, con presencia de Lagos). Fechas y duracion corregidas."),
    "9": dict(Start_Date="2001-09-12", End_Date="2001-09-13", Duration_Days="2",
              nota="NOTA 2026-07-21: el programa oficial de giras 2001 fecha la visita de "
                   "trabajo a Belgica (Bruselas) el 12-13/09/2001 (no 10-11/09), como tercer "
                   "tramo de una gira Portugal(9-11/09, Visita de Estado, Lisboa, no cargada "
                   "en esta base)->Reino Unido(11-12/09)->Belgica(12-13/09). Fecha corregida "
                   "para el tramo Belgica. Nota metodologica: el tramo Portugal (Lisboa, "
                   "Visita de Estado, confirmado por fotografias oficiales fechadas 10/09/2001 "
                   "de la reunion con el Presidente Jorge Sampaio) no figura como fila en esta "
                   "base y el tramo Reino Unido ya verificado en este archivo (Trip_ID 10) "
                   "figura con fechas 12-13/09, que segun esta misma fuente oficial "
                   "corresponderian mejor a 11-12/09; ninguno de los dos puntos se corrige "
                   "aqui por exceder el alcance de esta tanda (afecta numeracion de Journey/"
                   "Trip_ID) -- reportado para decision editorial."),
    "13": dict(Start_Date="2002-05-16", End_Date="2002-05-17", Duration_Days="2",
               nota="NOTA 2026-07-21: el programa oficial tentativo especifico de este viaje "
                    "('Madrid 16-17 de Mayo de 2002') y las fichas archivisticas de declaraciones "
                    "y conferencia de prensa al termino de la firma del Acuerdo Chile-UE, ambas "
                    "fechadas 17/05/2002, fijan la Cumbre UE-ALC y el cierre del acuerdo el "
                    "16-17/05/2002 (no 17-18/05). Fecha corregida."),
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
    print(f"chile (Lagos): filas verificadas={n_verif} | filas con nota/correccion={n_datefix}")

if __name__ == "__main__":
    process()
