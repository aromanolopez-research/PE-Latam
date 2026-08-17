# -*- coding: utf-8 -*-
"""
schema.py — Esquema canónico del proyecto "Viajes Presidenciales de América (2000-2026)".

Este archivo es la ÚNICA fuente de verdad sobre:
  - el orden y nombre de las 19 columnas,
  - los dominios de valores permitidos,
  - el mapeo automático País -> Región (para evitar errores manuales),
  - las funciones de ayuda para construir y validar filas.

Cualquier script del proyecto debe importar desde aquí. No redefinir columnas en otro lado.
Formato de datos canónico: CSV UTF-8, minimalista (una fila de encabezado, sin formato),
pensado para cargar directo en R / Python / SPSS / Stata.
"""

# ──────────────────────────────────────────────────────────────────────────
# 1) COLUMNAS (orden definitivo). Journey_ID es la PRIMERA columna.
# ──────────────────────────────────────────────────────────────────────────
COLUMNS = [
    "Journey_ID",            # 1  Identificador del VIAJE FÍSICO (una salida del país). Agrupa las filas de una misma gira.
    "Trip_ID",               # 2  Entero secuencial global (1,2,3...). Identifica cada FILA (tramo/país).
    "President",             # 3  Nombre del mandatario.
    "Origin_Country",        # 4  País de origen (el del mandatario).
    "Trip_Status",           # 5  Completed | Canceled
    "Start_Date",            # 6  YYYY-MM-DD (de la estancia en ESTE país). NA si se desconoce.
    "End_Date",              # 7  YYYY-MM-DD (de la estancia en ESTE país). NA si se desconoce.
    "Duration_Days",         # 8  Entero: días en ESTE país (no el total de la gira). NA si Canceled.
    "Destination_Country",   # 9  País de destino (uno por fila).
    "Destination_Region",    # 10 Región del destino (ver REGION_MAP).
    "Destination_City",      # 11 Ciudad principal del tramo.
    "Visit_Category",        # 12 Bilateral | Multilateral | Other
    "Visit_Subtype",         # 13 State Visit | Working Visit | Regional Summit | Global Forum | Inauguration/Funeral | Transit/Medical
    "Sideline_Bilaterals",   # 14 TRUE | FALSE | NA
    "Counterpart_Event",     # 15 Nombre del funcionario visitado o de la cumbre/evento.
    "Counterpart_Type",      # 16 Naturaleza de la contraparte (taxonomía cerrada, ver DOM_COUNTERPART_TYPE).
                             #    SOLO para Visit_Category = Bilateral; en Multilateral/Other va "NA".
                             #    Agregado 2026-07-27 para distinguir la diplomacia presidencial "clásica"
                             #    (con el jefe de Estado/Gobierno en funciones) de una modalidad más nueva:
                             #    viajes a título personal/ideológico o para recibir premios/honores.
    "Trip_Objective",        # 17 Resumen factual (máx 30 palabras). Incluir motivo de cancelación si aplica.
    "Source_Verification",   # 18 URL real, link de Wayback Machine, o "Search Query: [términos exactos]".
    "Source_Reliability",    # 19 High | Medium | Low
    "Methodological_Notes",  # 20 Nota si la fecha es estimada (usar YYYY-MM-01) o si el dato es incompleto.
    "Tema_Foro",             # 21 Tema principal del foro multilateral (taxonomía cerrada, ver DOM_TEMA_FORO).
                             #    SOLO para Visit_Category = Multilateral; en Bilateral/Other va "NA".
    "Verificacion_Status",   # 22 Verificada-URL | Solo-Query | No-verificable (campaña de verificación 2026-07-07).
    # ── Columnas 23-31: variables de micro-conducta tomadas del esquema del dataset
    # externo Diplometrics COLT (Country and Organization Leader Travel, Pardee
    # Institute, U. Denver), agregadas 2026-08-03 a pedido del usuario para combinar
    # ambos esquemas. Complementan (no reemplazan) nuestra taxonomía propia: mientras
    # Visit_Category/Visit_Subtype/Tema_Foro/Counterpart_Type clasifican QUÉ TIPO de
    # visita fue, estas columnas registran QUÉ HIZO el mandatario durante la visita.
    # Dominio TRUE|FALSE|NA en las booleanas; NA significa "no investigado en esta
    # ronda" (rollout incremental, mismo criterio que Counterpart_Type/Tema_Foro).
    "MetHostHOGS",            # 23 TRUE|FALSE|NA. Reunión bilateral con el Jefe de Estado/Gobierno del país anfitrión.
    "MetNonHostHOGS",         # 24 TRUE|FALSE|NA. Reunión con un Jefe de Estado/Gobierno de un TERCER país (no el anfitrión).
    "NonHostHOGS_Name",       # 25 Nombre del/los Jefe/s de Estado/Gobierno de terceros países reunidos. NA si no aplica.
    "PublicAddress",          # 26 TRUE|FALSE|NA. Discurso público, alocución, entrevista no periodística, etc.
    "SignedAgreement",        # 27 TRUE|FALSE|NA. Firmó o presenció la firma de un acuerdo/tratado/memorándum.
    "CulturalSiteOrCeremony", # 28 TRUE|FALSE|NA. Visita a sitio cultural/religioso/histórico o ceremonia (incl. inauguraciones, actos militares).
    "BusinessLeaderOrForum",  # 29 TRUE|FALSE|NA. Reunión/foro con líderes del sector privado/empresarial.
    "MetIGOLeader",           # 30 TRUE|FALSE|NA. Reunión bilateral con el líder de un organismo internacional (ONU, FMI, BM, etc.).
    "IGOLeader_Name",         # 31 Nombre y cargo del líder de organismo internacional reunido. NA si no aplica.
]

N_COLUMNS = len(COLUMNS)  # 31

# ──────────────────────────────────────────────────────────────────────────
# 2) DOMINIOS DE VALORES PERMITIDOS
# ──────────────────────────────────────────────────────────────────────────
DOM_TRIP_STATUS   = {"Completed", "Canceled"}
DOM_REGION        = {
    "South America", "Central America", "North America", "Caribbean",
    "Europe", "Asia-Pacific", "Africa", "Middle East", "Antarctica",
}
DOM_CATEGORY      = {"Bilateral", "Multilateral", "Other"}
DOM_SUBTYPE       = {
    "State Visit", "Working Visit", "Regional Summit",
    "Global Forum", "Inauguration/Funeral", "Transit/Medical",
}
DOM_SIDELINE      = {"TRUE", "FALSE", "NA"}
DOM_RELIABILITY   = {"High", "Medium", "Low"}
DOM_VERIF_STATUS  = {"Verificada-URL", "Solo-Query", "No-verificable"}
# Taxonomía cerrada de temas de foros multilaterales (decisión 2026-07-06).
# Regla del "mandato fundacional": foros de agenda amplia -> Cooperación Política General;
# foros de mandato económico-comercial -> Comercio/Integración Económica. Ver CODEBOOK 5.7.
DOM_TEMA_FORO     = {
    "Comercio/Integración Económica",
    "Seguridad",
    "Medio Ambiente/Clima",
    "Derechos Humanos",
    "Salud",
    "Energía",
    "Cooperación Política General",
    "Otro",
    "NA",   # obligatorio si Visit_Category != Multilateral
}
# Taxonomía cerrada de Counterpart_Type (decisión 2026-07-27, a pedido del usuario).
# Distingue la diplomacia bilateral "clásica" (con el jefe de Estado/Gobierno en
# funciones) de una modalidad de diplomacia presidencial más nueva: viajes que
# formalmente son Bilateral pero cuyo motivo real NO es una relación Estado-a-Estado
# (ej.: Lula visitando a Cristina Fernández de Kirchner presa/ex-presidenta; Milei
# viajando a España a recibir un premio). Solo aplica a Visit_Category = Bilateral.
DOM_COUNTERPART_TYPE = {
    "Jefe de Estado/Gobierno",           # caso por defecto: la contraparte oficial en funciones
    "Ex-mandatario/Opositor",            # ex-presidente, dirigente opositor o líder partidario que no gobierna
    "Premio/Distinción/Honor académico", # premio, título honoris causa, distinción cultural o académica
    "Movimiento partidario/ideológico",  # evento de un partido/movimiento, no un acto de Estado
    "Otro actor no estatal",             # empresa, ONG, institución religiosa (no jefe de Estado), think tank, etc.
    "NA",   # obligatorio si Visit_Category != Bilateral
}

MISSING = "NA"  # valor único para dato faltante en TODAS las columnas

# ──────────────────────────────────────────────────────────────────────────
# 3) MAPEO AUTOMÁTICO País -> Región
#    Objetivo analítico: medir cómo varía en el tiempo el peso de cada región
#    en la agenda de viajes (Sudamérica vs Centroamérica vs Norteamérica vs
#    Caribe vs Europa vs Asia-Pacífico vs África vs Medio Oriente).
#    EE.UU. se aísla siempre por Destination_Country == "United States".
#    Notas de criterio (casos transcontinentales):
#      - Rusia -> Europe ; Turquía -> Middle East ; Egipto -> Africa ;
#        Kazajistán -> Asia-Pacific ; Israel/Palestina -> Middle East.
#    Países usados en el inglés del codebook (Destination_Country en inglés).
# ──────────────────────────────────────────────────────────────────────────
REGION_MAP = {
    # South America
    "Argentina":"South America","Bolivia":"South America","Brazil":"South America",
    "Chile":"South America","Colombia":"South America","Ecuador":"South America",
    "Guyana":"South America","Paraguay":"South America","Peru":"South America",
    "Suriname":"South America","Uruguay":"South America","Venezuela":"South America",
    "French Guiana":"South America",
    # Central America
    "Guatemala":"Central America","Belize":"Central America","Honduras":"Central America",
    "El Salvador":"Central America","Nicaragua":"Central America","Costa Rica":"Central America",
    "Panama":"Central America",
    # North America (EE.UU. se aísla por país)
    "United States":"North America","Canada":"North America","Mexico":"North America",
    # Caribbean
    "Cuba":"Caribbean","Dominican Republic":"Caribbean","Haiti":"Caribbean","Jamaica":"Caribbean",
    "Puerto Rico":"Caribbean",
    "Trinidad and Tobago":"Caribbean","Bahamas":"Caribbean","Barbados":"Caribbean",
    "Antigua and Barbuda":"Caribbean","Dominica":"Caribbean","Grenada":"Caribbean",
    "Saint Kitts and Nevis":"Caribbean","Saint Lucia":"Caribbean",
    "Saint Vincent and the Grenadines":"Caribbean",
    # Europe
    "Spain":"Europe","Portugal":"Europe","France":"Europe","Germany":"Europe","Italy":"Europe",
    "United Kingdom":"Europe","Belgium":"Europe","Netherlands":"Europe","Switzerland":"Europe",
    "Austria":"Europe","Russia":"Europe","Vatican City":"Europe","Sweden":"Europe",
    "Norway":"Europe","Finland":"Europe","Denmark":"Europe","Czechia":"Europe","Ukraine":"Europe",
    "Monaco":"Europe","Ireland":"Europe","Poland":"Europe","Greece":"Europe","Bulgaria":"Europe",
    "Slovakia":"Europe","Slovenia":"Europe","Croatia":"Europe","Romania":"Europe","Hungary":"Europe",
    "Serbia":"Europe","Luxembourg":"Europe","Iceland":"Europe","Lithuania":"Europe","Latvia":"Europe","Estonia":"Europe",
    "Scotland":"Europe","Azerbaijan":"Europe",
    # Armenia agregado 2026-08-03 (extension Menem/COLT): mismo criterio que Azerbaijan
    # (estado del Caucaso, ya mapeado a Europe en este proyecto por consistencia interna).
    "Armenia":"Europe",
    # Africa
    "Democratic Republic of Congo":"Africa",
    # Asia-Pacific (incluye Oceanía y Asia Central)
    "Papua New Guinea":"Asia-Pacific",
    "China":"Asia-Pacific","Japan":"Asia-Pacific","South Korea":"Asia-Pacific","India":"Asia-Pacific",
    "Taiwan":"Asia-Pacific",
    "Vietnam":"Asia-Pacific","Indonesia":"Asia-Pacific","Malaysia":"Asia-Pacific",
    "Singapore":"Asia-Pacific","Thailand":"Asia-Pacific","Philippines":"Asia-Pacific","Brunei":"Asia-Pacific",
    "Timor-Leste":"Asia-Pacific","Australia":"Asia-Pacific","New Zealand":"Asia-Pacific",
    "Kazakhstan":"Asia-Pacific","Taiwan":"Asia-Pacific",
    # Africa
    "South Africa":"Africa","Angola":"Africa","Mozambique":"Africa","Namibia":"Africa",
    "Nigeria":"Africa","Ghana":"Africa","Senegal":"Africa","Guinea-Bissau":"Africa",
    "Cameroon":"Africa","Sao Tome and Principe":"Africa","Egypt":"Africa","Ethiopia":"Africa",
    "Cape Verde":"Africa","Equatorial Guinea":"Africa","Gabon":"Africa","Congo":"Africa",
    "Algeria":"Africa","Botswana":"Africa","Burkina Faso":"Africa","Kenya":"Africa","Benin":"Africa",
    "Republic of the Congo":"Africa","Democratic Republic of the Congo":"Africa","East Timor":"Asia-Pacific",
    "Tanzania":"Africa","Zambia":"Africa","Libya":"Africa","Morocco":"Africa",
    # Middle East
    "Saudi Arabia":"Middle East","Qatar":"Middle East","United Arab Emirates":"Middle East",
    "Israel":"Middle East","Palestine":"Middle East","Jordan":"Middle East","Lebanon":"Middle East",
    "Syria":"Middle East","Iran":"Middle East","Turkey":"Middle East","Kuwait":"Middle East",
    "Bahrain":"Middle East","Oman":"Middle East","Yemen":"Middle East","Iraq":"Middle East",
    # Africa (adicionales)
    "Tunisia":"Africa","Sudan":"Africa","Ivory Coast":"Africa","Rwanda":"Africa",
    "Democratic Republic of the Congo":"Africa","Tanzania":"Africa","Uganda":"Africa",
    # Antarctica
    "Antarctica":"Antarctica",
}

def region_for(country: str) -> str:
    """Devuelve la región canónica de un país de destino, o 'NA' si no está mapeado.
    Si devuelve 'NA', hay que agregar el país a REGION_MAP (no inventar región a mano)."""
    return REGION_MAP.get(country, MISSING)

# ──────────────────────────────────────────────────────────────────────────
# 4) VALIDACIÓN DE FILAS
# ──────────────────────────────────────────────────────────────────────────
def validate_row(row: dict, idx=None) -> list:
    """Valida una fila (dict con las 19 claves). Devuelve lista de errores (vacía si OK)."""
    errs = []
    tag = f"[fila {idx}] " if idx is not None else ""

    # 4.1 columnas completas
    for col in COLUMNS:
        if col not in row:
            errs.append(f"{tag}falta la columna '{col}'")
    if errs:
        return errs  # sin columnas no tiene sentido seguir

    # 4.2 dominios
    if row["Trip_Status"] not in DOM_TRIP_STATUS:
        errs.append(f"{tag}Trip_Status invalido: '{row['Trip_Status']}'")
    if row["Destination_Region"] not in DOM_REGION:
        errs.append(f"{tag}Destination_Region invalida: '{row['Destination_Region']}'")
    if row["Visit_Category"] not in DOM_CATEGORY:
        errs.append(f"{tag}Visit_Category invalida: '{row['Visit_Category']}'")
    if row["Visit_Subtype"] not in DOM_SUBTYPE:
        errs.append(f"{tag}Visit_Subtype invalido: '{row['Visit_Subtype']}'")
    if str(row["Sideline_Bilaterals"]) not in DOM_SIDELINE:
        errs.append(f"{tag}Sideline_Bilaterals invalido: '{row['Sideline_Bilaterals']}'")
    if row["Source_Reliability"] not in DOM_RELIABILITY:
        errs.append(f"{tag}Source_Reliability invalida: '{row['Source_Reliability']}'")
    if row["Verificacion_Status"] not in DOM_VERIF_STATUS:
        errs.append(f"{tag}Verificacion_Status invalido: '{row['Verificacion_Status']}'")
    if row["Tema_Foro"] not in DOM_TEMA_FORO:
        errs.append(f"{tag}Tema_Foro invalido: '{row['Tema_Foro']}'")
    # Tema_Foro solo aplica a Multilateral; en Bilateral/Other debe ser NA.
    if row["Visit_Category"] != "Multilateral" and row["Tema_Foro"] != MISSING:
        errs.append(f"{tag}Tema_Foro debe ser NA cuando Visit_Category != Multilateral "
                    f"(hallado '{row['Tema_Foro']}')")
    if row["Visit_Category"] == "Multilateral" and row["Tema_Foro"] == MISSING:
        errs.append(f"{tag}Tema_Foro faltante: fila Multilateral requiere una categoría temática")
    if row["Counterpart_Type"] not in DOM_COUNTERPART_TYPE:
        errs.append(f"{tag}Counterpart_Type invalido: '{row['Counterpart_Type']}'")
    # Counterpart_Type solo aplica a Bilateral; en Multilateral/Other debe ser NA.
    if row["Visit_Category"] != "Bilateral" and row["Counterpart_Type"] != MISSING:
        errs.append(f"{tag}Counterpart_Type debe ser NA cuando Visit_Category != Bilateral "
                    f"(hallado '{row['Counterpart_Type']}')")
    if row["Visit_Category"] == "Bilateral" and row["Counterpart_Type"] == MISSING:
        errs.append(f"{tag}Counterpart_Type faltante: fila Bilateral requiere clasificar la contraparte")

    # 4.2b columnas de micro-conducta estilo COLT (agregadas 2026-08-03)
    for col in ("MetHostHOGS", "MetNonHostHOGS", "PublicAddress", "SignedAgreement",
                "CulturalSiteOrCeremony", "BusinessLeaderOrForum", "MetIGOLeader"):
        if str(row[col]) not in DOM_SIDELINE:  # mismo dominio TRUE|FALSE|NA
            errs.append(f"{tag}{col} invalido: '{row[col]}' (debe ser TRUE, FALSE o NA)")
    # los campos de nombre deben ser NA si el booleano asociado no es TRUE
    if row["MetNonHostHOGS"] != "TRUE" and row["NonHostHOGS_Name"] != MISSING:
        errs.append(f"{tag}NonHostHOGS_Name debe ser NA cuando MetNonHostHOGS != TRUE")
    if row["MetIGOLeader"] != "TRUE" and row["IGOLeader_Name"] != MISSING:
        errs.append(f"{tag}IGOLeader_Name debe ser NA cuando MetIGOLeader != TRUE")

    # 4.3 region coherente con país (si el país está mapeado)
    auto = region_for(row["Destination_Country"])
    if auto != MISSING and row["Destination_Region"] != auto:
        errs.append(f"{tag}Region '{row['Destination_Region']}' no coincide con el mapeo "
                    f"de '{row['Destination_Country']}' (esperado '{auto}')")

    # 4.4 reglas de duración / cancelados
    dur = row["Duration_Days"]
    if row["Trip_Status"] == "Canceled":
        if dur != MISSING:
            errs.append(f"{tag}un viaje Canceled debe tener Duration_Days = NA")
    else:  # Completed
        if dur != MISSING:
            try:
                d = int(dur)
                if d < 0:
                    errs.append(f"{tag}Duration_Days negativo: {dur}")
            except (ValueError, TypeError):
                errs.append(f"{tag}Duration_Days no es entero ni NA: '{dur}'")

    # 4.5 sin comas en numéricos
    for col in ("Trip_ID", "Duration_Days"):
        if "," in str(row[col]):
            errs.append(f"{tag}'{col}' contiene coma: '{row[col]}'")

    # 4.6 Journey_ID y Trip_ID presentes
    if not str(row["Journey_ID"]).strip() or row["Journey_ID"] == MISSING:
        errs.append(f"{tag}Journey_ID vacio")
    if not str(row["Trip_ID"]).strip() or row["Trip_ID"] == MISSING:
        errs.append(f"{tag}Trip_ID vacio")

    # 4.7 fechas ISO o NA
    for col in ("Start_Date", "End_Date"):
        v = row[col]
        if v != MISSING:
            ok = (len(v) == 10 and v[4] == "-" and v[7] == "-")
            if not ok:
                errs.append(f"{tag}{col} no es YYYY-MM-DD ni NA: '{v}'")

    return errs


def new_row(**kwargs) -> dict:
    """Crea una fila con todas las columnas, default NA, y aplica auto-región si falta.
    Uso: new_row(Journey_ID=..., Trip_ID=..., President=..., ...)."""
    row = {col: MISSING for col in COLUMNS}
    row.update(kwargs)
    # auto-región si no se especificó o vino NA
    if row.get("Destination_Region", MISSING) in (MISSING, "", None):
        row["Destination_Region"] = region_for(row.get("Destination_Country", MISSING))
    # auto-Verificacion_Status si no se especificó: derivar de Source_Verification
    if row.get("Verificacion_Status", MISSING) in (MISSING, "", None):
        sv = str(row.get("Source_Verification", ""))
        row["Verificacion_Status"] = "Verificada-URL" if sv.startswith("http") else "Solo-Query"
    return row
