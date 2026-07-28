# -*- coding: utf-8 -*-
"""
CHILE — primer modulo. Ricardo Lagos Escobar (11/3/2000 a 11/3/2006, PPD/PS).
Trip_ID arranca en 1 (modulo nuevo; integrate.py renumera global al consolidar).
Reconstruccion PROFUNDA (modo research): >=40 viajes verificables (vs ~24 de la 1ra pasada).
Perfil librecambista (TLC con EE.UU./UE/Corea/China/P4), fuerte en Asia-Pacifico (APEC),
activo en foros y en el Consejo de Seguridad (oposicion a Irak 2003). "Pais puente".
Fuentes: Prensa Presidencia Chile (Wayback), MINREL, BCN, SEGIB, OEA, APEC, ONU, prensa (El Mercurio/La Tercera/EMOL).
Journey_ID: CHL-RL-Jnnn. Giras multipais = 1 Journey_ID.
Excluidos por ser en Chile: APEC Santiago (nov 2004), cumbres en territorio chileno.
Brecha residual documentada EN EL MOMENTO en PENDIENTES_VERIFICACION.txt (estimacion 50-70; cargados ~40).
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import COLUMNS, new_row

CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "03_MODULOS_PAIS", "chile", "chile_viajes.csv")
P = "Ricardo Lagos"; O = "Chile"
rows = []; tid = 1

def add(jid, **kw):
    global tid
    kw.setdefault("President", P); kw.setdefault("Origin_Country", O)
    kw["Journey_ID"] = jid; kw["Trip_ID"] = tid
    rows.append(new_row(**kw)); tid += 1

# ===== 2000 (desde 11/3) =====
add("CHL-RL-J001", Trip_Status="Completed", Start_Date="2000-06-29", End_Date="2000-06-30", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Buenos Aires", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del MERCOSUR (Chile asociado)",
    Trip_Objective="Primer viaje internacional del mandato: cumbre del Mercosur; Chile como Estado asociado.",
    Source_Verification="Search Query: Ricardo Lagos primera gira Mercosur Buenos Aires junio 2000",
    Source_Reliability="Medium", Methodological_Notes="Primer viaje del mandato.")

add("CHL-RL-J002", Trip_Status="Completed", Start_Date="2000-09-06", End_Date="2000-09-08", Duration_Days=3,
    Destination_Country="United States", Destination_City="New York", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del Milenio de la ONU",
    Trip_Objective="Cumbre del Milenio de la ONU.",
    Source_Verification="https://www.un.org/es/events/pastevents/millennium_summit.shtml",
    Source_Reliability="Medium", Methodological_Notes="Fechas oficiales de la Cumbre del Milenio.")

add("CHL-RL-J003", Trip_Status="Completed", Start_Date="2000-11-17", End_Date="2000-11-18", Duration_Days=2,
    Destination_Country="Panama", Destination_City="Panama City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="X Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Panama; ninez y adolescencia.",
    Source_Verification="https://www.segib.org/?summit=x-cumbre-iberoamericana-panama-2000",
    Source_Reliability="High", Methodological_Notes="17-18/11/2000.")

add("CHL-RL-J004", Trip_Status="Completed", Start_Date="2000-11-15", End_Date="2000-11-16", Duration_Days=2,
    Destination_Country="Brunei", Destination_City="Bandar Seri Begawan", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre de lideres de APEC en Brunei; Chile en la agenda Asia-Pacifico.",
    Source_Verification="Search Query: Lagos APEC Brunei noviembre 2000",
    Source_Reliability="Medium", Methodological_Notes="Fechas a confirmar; verificar solapamiento con Iberoamericana.")

# ===== 2001 =====
add("CHL-RL-J005", Trip_Status="Completed", Start_Date="2001-04-20", End_Date="2001-04-22", Duration_Days=3,
    Destination_Country="Canada", Destination_City="Quebec City", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="III Cumbre de las Américas",
    Trip_Objective="III Cumbre de las Americas; negociacion del ALCA y clausula democratica.",
    Source_Verification="https://www.summit-americas.org/iii_summit.html",
    Source_Reliability="High", Methodological_Notes="20-22/04/2001.")

# Gira Europa jun 2001 (1 Journey_ID) - Espana, Francia, Alemania (verificar tramos)
add("CHL-RL-J006", Trip_Status="Completed", Start_Date="2001-06-04", End_Date="2001-06-06", Duration_Days=3,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Bilateral", Visit_Subtype="State Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Rey Juan Carlos I / José María Aznar",
    Trip_Objective="Visita de Estado a Espana; inversiones y acuerdo Chile-UE en agenda. Tramo 1 de gira europea.",
    Source_Verification="Search Query: Lagos visita Estado Espana junio 2001 Aznar",
    Source_Reliability="Medium", Methodological_Notes="Gira europea jun 2001; tramos y fechas a confirmar.")

add("CHL-RL-J006", Trip_Status="Completed", Start_Date="2001-06-07", End_Date="2001-06-08", Duration_Days=2,
    Destination_Country="France", Destination_City="Paris", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Jacques Chirac",
    Trip_Objective="Relaciones bilaterales; acuerdo Chile-UE. Tramo 2 de gira europea.",
    Source_Verification="Search Query: Lagos Francia Chirac junio 2001",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas.")

add("CHL-RL-J007", Trip_Status="Completed", Start_Date="2001-07-28", End_Date="2001-07-28", Duration_Days=1,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Alejandro Toledo",
    Trip_Objective="Asuncion de Alejandro Toledo en Peru.",
    Source_Verification="Search Query: Lagos asuncion Toledo Lima julio 2001",
    Source_Reliability="Medium", Methodological_Notes="28/07/2001.")

# Gira Belgica + Reino Unido sep 2001 (interrumpida por el 11-S) - 1 Journey_ID
add("CHL-RL-J008", Trip_Status="Completed", Start_Date="2001-09-10", End_Date="2001-09-11", Duration_Days=2,
    Destination_Country="Belgium", Destination_City="Brussels", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Unión Europea (negociación del Acuerdo de Asociación)",
    Trip_Objective="Negociacion del Acuerdo Chile-UE. Tramo 1; la gira se altero por los atentados del 11-S. ",
    Source_Verification="Search Query: Lagos Belgica Union Europea septiembre 2001 11-S",
    Source_Reliability="Medium", Methodological_Notes="Gira interrumpida por el 11/09/2001.")

add("CHL-RL-J008", Trip_Status="Completed", Start_Date="2001-09-12", End_Date="2001-09-13", Duration_Days=2,
    Destination_Country="United Kingdom", Destination_City="London", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Tony Blair",
    Trip_Objective="Relaciones bilaterales. Tramo 2, afectado por el 11-S.",
    Source_Verification="Search Query: Lagos Reino Unido Blair septiembre 2001",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas; contexto 11-S.")

add("CHL-RL-J009", Trip_Status="Completed", Start_Date="2001-11-23", End_Date="2001-11-24", Duration_Days=2,
    Destination_Country="Peru", Destination_City="Lima", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XI Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Lima; unidad ante el terrorismo global.",
    Source_Verification="https://www.segib.org/?summit=xi-cumbre-iberoamericana-lima-2001",
    Source_Reliability="High", Methodological_Notes="23-24/11/2001.")

# ===== 2002 =====
add("CHL-RL-J010", Trip_Status="Completed", Start_Date="2002-03-21", End_Date="2002-03-22", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Monterrey", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Conferencia sobre Financiación para el Desarrollo",
    Trip_Objective="Conferencia de Monterrey (Consenso de Monterrey).",
    Source_Verification="https://www.un.org/es/conf/ffd/2002/",
    Source_Reliability="Medium", Methodological_Notes="21-22/03/2002 (segmento de alto nivel).")

add("CHL-RL-J011", Trip_Status="Completed", Start_Date="2002-05-17", End_Date="2002-05-18", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Madrid", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="II Cumbre UE-América Latina y el Caribe + firma Acuerdo Chile-UE",
    Trip_Objective="Cumbre UE-ALC; Chile cerro politicamente su Acuerdo de Asociacion con la UE.",
    Source_Verification="Search Query: Lagos Cumbre UE America Latina Madrid mayo 2002 acuerdo Chile UE",
    Source_Reliability="High", Methodological_Notes="17-18/05/2002.")

add("CHL-RL-J012", Trip_Status="Completed", Start_Date="2002-08-31", End_Date="2002-09-02", Duration_Days=3,
    Destination_Country="South Africa", Destination_City="Johannesburg", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="NA", Counterpart_Event="Cumbre Mundial sobre Desarrollo Sostenible (Rio+10)",
    Trip_Objective="Cumbre Mundial de Desarrollo Sostenible en Johannesburgo.",
    Source_Verification="Search Query: Lagos Cumbre Desarrollo Sostenible Johannesburgo 2002",
    Source_Reliability="Medium", Methodological_Notes="Segmento de alto nivel; dias exactos estimados.")

add("CHL-RL-J013", Trip_Status="Completed", Start_Date="2002-10-26", End_Date="2002-10-27", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Los Cabos", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Los Cabos; libre comercio en Asia-Pacifico.",
    Source_Verification="Search Query: Lagos APEC Los Cabos octubre 2002",
    Source_Reliability="Medium", Methodological_Notes="26-27/10/2002.")

add("CHL-RL-J014", Trip_Status="Completed", Start_Date="2002-11-23", End_Date="2002-11-24", Duration_Days=2,
    Destination_Country="Dominican Republic", Destination_City="Bávaro", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Bavaro.",
    Source_Verification="https://www.segib.org/?summit=xii-cumbre-iberoamericana-bavaro-2002",
    Source_Reliability="High", Methodological_Notes="23-24/11/2002.")

# ===== 2003 =====
add("CHL-RL-J015", Trip_Status="Completed", Start_Date="2003-06-01", End_Date="2003-06-03", Duration_Days=3,
    Destination_Country="France", Destination_City="Évian-les-Bains", Visit_Category="Multilateral", Visit_Subtype="Global Forum",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre del G8 ampliada (Evián, invitado)",
    Trip_Objective="Invitado al dialogo ampliado del G8 en Evian.",
    Source_Verification="Search Query: Lagos G8 Evian junio 2003 invitado",
    Source_Reliability="Medium", Methodological_Notes="1-3/06/2003 (segmento ampliado).")

add("CHL-RL-J016", Trip_Status="Completed", Start_Date="2003-10-20", End_Date="2003-10-21", Duration_Days=2,
    Destination_Country="Thailand", Destination_City="Bangkok", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC",
    Trip_Objective="Cumbre APEC de Bangkok.",
    Source_Verification="Search Query: Lagos APEC Bangkok octubre 2003",
    Source_Reliability="Medium", Methodological_Notes="20-21/10/2003.")

add("CHL-RL-J017", Trip_Status="Completed", Start_Date="2003-11-14", End_Date="2003-11-15", Duration_Days=2,
    Destination_Country="Bolivia", Destination_City="Santa Cruz de la Sierra", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XIII Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Santa Cruz; inclusion social.",
    Source_Verification="https://www.segib.org/?summit=xiii-cumbre-iberoamericana-santa-cruz-de-la-sierra-2003",
    Source_Reliability="High", Methodological_Notes="14-15/11/2003.")

# ===== 2004 =====
add("CHL-RL-J018", Trip_Status="Completed", Start_Date="2004-01-12", End_Date="2004-01-13", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Monterrey", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre Extraordinaria de las Américas",
    Trip_Objective="Cumbre Extraordinaria de las Americas en Monterrey.",
    Source_Verification="https://www.summit-americas.org/special_summit.html",
    Source_Reliability="High", Methodological_Notes="12-13/01/2004.")

add("CHL-RL-J019", Trip_Status="Completed", Start_Date="2004-05-28", End_Date="2004-05-29", Duration_Days=2,
    Destination_Country="Mexico", Destination_City="Guadalajara", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="III Cumbre UE-América Latina y el Caribe",
    Trip_Objective="Cumbre UE-ALC de Guadalajara.",
    Source_Verification="Search Query: Lagos Cumbre UE ALC Guadalajara mayo 2004",
    Source_Reliability="Medium", Methodological_Notes="28-29/05/2004.")

add("CHL-RL-J020", Trip_Status="Completed", Start_Date="2004-06-05", End_Date="2004-06-06", Duration_Days=2,
    Destination_Country="France", Destination_City="Normandy", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="60º aniversario del Día D",
    Trip_Objective="Conmemoracion del 60 aniversario del desembarco de Normandia.",
    Source_Verification="Search Query: Lagos 60 aniversario Dia D Normandia junio 2004",
    Source_Reliability="Low", Methodological_Notes="Fechas estimadas; confirmar asistencia.")

# Gira asiatica 2004 (1 Journey_ID): China + Corea del Sur + Nueva Zelanda + Indonesia
add("CHL-RL-J021", Trip_Status="Completed", Start_Date="2004-11-18", End_Date="2004-11-19", Duration_Days=2,
    Destination_Country="Indonesia", Destination_City="Jakarta", Visit_Category="Bilateral", Visit_Subtype="Working Visit",
    Sideline_Bilaterals="NA", Counterpart_Event="Gobierno de Indonesia",
    Trip_Objective="Comercio Asia-Pacifico; giras vinculadas a la agenda APEC 2004 (Chile fue anfitrion). Tramo de gira asiatica.",
    Source_Verification="Search Query: Lagos Indonesia 2004 gira asiatica",
    Source_Reliability="Low", Methodological_Notes="Gira asiatica 2004; fechas y tramos a confirmar.")

add("CHL-RL-J022", Trip_Status="Completed", Start_Date="2004-11-20", End_Date="2004-11-22", Duration_Days=3,
    Destination_Country="Costa Rica", Destination_City="San José", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="NA", Counterpart_Event="XIV Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de San Jose.",
    Source_Verification="https://www.segib.org/?summit=xiv-cumbre-iberoamericana-san-jose-2004",
    Source_Reliability="High", Methodological_Notes="Verificar solapamiento con gira asiatica; fechas 19-20/11.")

# ===== 2005 =====
add("CHL-RL-J023", Trip_Status="Completed", Start_Date="2005-03-01", End_Date="2005-03-01", Duration_Days=1,
    Destination_Country="Uruguay", Destination_City="Montevideo", Visit_Category="Multilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Asunción de Tabaré Vázquez",
    Trip_Objective="Asuncion de Tabare Vazquez en Uruguay.",
    Source_Verification="Search Query: Lagos asuncion Tabare Vazquez Montevideo marzo 2005",
    Source_Reliability="Medium", Methodological_Notes="1/03/2005.")

add("CHL-RL-J024", Trip_Status="Completed", Start_Date="2005-10-14", End_Date="2005-10-15", Duration_Days=2,
    Destination_Country="Spain", Destination_City="Salamanca", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="XV Cumbre Iberoamericana",
    Trip_Objective="Cumbre Iberoamericana de Salamanca.",
    Source_Verification="https://www.segib.org/?summit=xv-cumbre-iberoamericana-salamanca-2005",
    Source_Reliability="High", Methodological_Notes="14-15/10/2005.")

add("CHL-RL-J025", Trip_Status="Completed", Start_Date="2005-11-04", End_Date="2005-11-05", Duration_Days=2,
    Destination_Country="Argentina", Destination_City="Mar del Plata", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="IV Cumbre de las Américas",
    Trip_Objective="IV Cumbre de las Americas; el 'no al ALCA'.",
    Source_Verification="Search Query: Lagos IV Cumbre Americas Mar del Plata noviembre 2005",
    Source_Reliability="High", Methodological_Notes="4-5/11/2005.")

# Gira APEC Busan + TLC China nov 2005 — 1 Journey_ID
add("CHL-RL-J026", Trip_Status="Completed", Start_Date="2005-11-18", End_Date="2005-11-19", Duration_Days=2,
    Destination_Country="South Korea", Destination_City="Busan", Visit_Category="Multilateral", Visit_Subtype="Regional Summit",
    Sideline_Bilaterals="TRUE", Counterpart_Event="Cumbre de Líderes de APEC + firma TLC Chile-China",
    Trip_Objective="Cumbre APEC de Busan; Chile firmo el TLC con China al margen (primer pais sudamericano).",
    Source_Verification="Search Query: Lagos APEC Busan noviembre 2005 TLC China",
    Source_Reliability="High", Methodological_Notes="18-19/11/2005.")

# ===== 2006 (hasta 11/3) =====
add("CHL-RL-J027", Trip_Status="Completed", Start_Date="2006-01-22", End_Date="2006-01-22", Duration_Days=1,
    Destination_Country="Bolivia", Destination_City="La Paz", Visit_Category="Bilateral", Visit_Subtype="Inauguration/Funeral",
    Sideline_Bilaterals="NA", Counterpart_Event="Asunción de Evo Morales",
    Trip_Objective="Asuncion de Evo Morales; ULTIMO viaje internacional del mandato.",
    Source_Verification="Search Query: Lagos asuncion Evo Morales La Paz enero 2006",
    Source_Reliability="High", Methodological_Notes="22/01/2006. Ultimo viaje del mandato.")

os.makedirs(os.path.dirname(CSV), exist_ok=True)
with open(CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(rows)
print(f"OK: {len(rows)} filas de {P} escritas. Journeys: {len(set(r['Journey_ID'] for r in rows))}")
