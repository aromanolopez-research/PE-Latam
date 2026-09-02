# ================================================================================
# GRAFICOS EXPLORATORIOS - VIAJES PRESIDENCIALES DE SUDAMERICA (1994-2025)
# Fuente: 04_BASE_FINAL/Base_COLT_Sudamerica.xlsx, hoja "Datos_COLT_Sudamerica"
# ================================================================================
# Version 7 (2026-08-27) — 10 pedidos puntuales sobre las figuras del paper:
#   1) Ficha general (00a) ahora tambien se exporta a CSV -> en el paper pasa
#      de imagen a Cuadro (xtable).
#   2) Nueva tabla mandatos_presidenciales.csv (09_PAPER/), investigada y
#      verificada con fuentes (fechas de inicio/fin de mandato, incluyendo
#      mandatarios no consecutivos con mas de un periodo). Se usa para
#      etiquetar "Nombre (periodo)" tanto en el grafico de total de viajes
#      por mandatario (00c) como en la nueva tabla de destino favorito.
#   3) Tabla de estadisticos descriptivos (00d): se agrega la columna
#      "Unidad_n_obs" para aclarar que las primeras dos filas cuentan
#      combinaciones pais-anio y la fila de duracion cuenta viajes
#      individuales (son unidades de observacion distintas). El viaje de 91
#      dias es el de Bolsonaro a EE.UU. (dic-2022/mar-2023, tras perder la
#      eleccion) -dato real, no un error de carga.
#   4) 01b (viajes por anio y pais): se agrega una linea de promedio anual
#      por pais (geom_hline por panel).
#   5) 02 (regiones por periodo): se agregan etiquetas de dato solo para
#      America Latina y el Caribe, Europa y Norteamerica.
#   6) La tabla de destino favorito por presidente (antes Figura 05b, un
#      grafico) ahora se exporta como CSV para armarse como Cuadro en el
#      paper, con Mandatario (periodo) en vez de simplemente el nombre.
#   7-9) Tres graficos nuevos de evolucion 1994-2025 para tercias de paises
#      puntuales (ver secciones 8b, 9.2b y 9.2c).
#   10) 09d (composicion bilateral/multilateral por pais): se invierte el
#      orden de la leyenda para que coincida con el orden visual del stack.
#
# Version 6 (2026-08-27) — estetica tipo revista Q1:
#   - Se saco el titulo/subtitulo/caption DE ADENTRO de cada grafico: en el
#     paper esa informacion ya la da el \caption{} de LaTeX (ver
#     09_PAPER/ViajesPresidencialesSudamerica.Rnw), y las revistas de primer
#     nivel (ISQ, APSR, etc.) casi nunca ponen titulo dentro de la figura
#     misma -queda redundante y es la primera cosa que un editor pide sacar.
#     Los ejes y las leyendas SI quedan (esos no son redundantes).
#   - Nuevo tema tema_journal() (reemplaza a tema_paper()): tipografia serif
#     (combina con el cuerpo del documento en LaTeX), sin grilla vertical,
#     grilla horizontal apenas visible, ejes finos, menos "chartjunk" en
#     general. Sigue en escala de grises (decision del usuario: que se siga
#     viendo bien en una impresion en blanco y negro).
#
# Version 5 (2026-08-27) — ajustes sobre la version anterior:
#   - Bolivia sigue en investigacion activa (campaña COLT en curso, ver
#     bitacora.txt); cuando se cierre y se reimporte al xlsx, este script no
#     necesita cambios -toma automaticamente los 12 paises de la hoja madre.
#   - Se amplio la bibliografia priorizada del proyecto (carpeta /Bib) con 5
#     textos nuevos. Dos de ellos motivan las extensiones nuevas de la
#     seccion 9 (9.3 y 9.4): Peña (2005) sobre la "compleja red de cumbres"
#     y Lee & Kim (2024) sobre el analisis composicional de visitas
#     diplomaticas. Ver el detalle de cada extension en su seccion.
#
# Version 4 (2026-08-19) — ajustes pedidos sobre la version anterior:
#   - Ventana temporal: 1994-2025 (se deja 2026 afuera a proposito: todavia
#     no esta tan mapeado/verificado como el resto -> ANIO_HASTA mas abajo).
#   - Nueva seccion 2 "Descriptivos generales" al principio del script, con
#     una ficha resumen, totales por pais, totales por mandatario y la
#     tabla de estadisticos descriptivos -todo tambien en imagen, no solo
#     en CSV/consola-.
#   - Se sacaron las lineas de tendencia suavizada (loess) de todos los
#     graficos: quedan solo los datos, sin curva superpuesta.
#   - Nuevo grafico combinado: cantidad total de viajes (barras) superpuesta
#     con la duracion promedio (linea), por anio.
#   - Se saco el boxplot de duracion por periodo (no aportaba mucho).
#   - Se aclara en el titulo/subtitulo que significa la categoria "Otro" en
#     los graficos de Bilateral/Multilateral/Otro.
#   - Se saco la linea de tiempo de primeras visitas (tenia errores de
#     lectura con tantos mandatarios superpuestos).
#   - Se saco el grafico de duracion por "año de mandato" (no mostraba un
#     patron claro y no aportaba demasiado).
#   - El ranking de destinos mas visitados ahora esta dividido en dos
#     graficos: uno para viajes bilaterales y otro para multilaterales.
#
# Preguntas originales (siguen respondidas):
#   1) Evolucion general de la cantidad de viajes en el tiempo
#   2) Que regiones se priorizan en cada epoca
#   3) Cambios en la duracion de los viajes (+ combinado con cantidad de viajes)
#   4-5) Bilateral vs. Multilateral vs. Otro: participacion y volumen en el tiempo
#   6) Destinos preferidos por cada mandatario
#   7) Primera visita de cada mandatario (a que pais)
# Extensiones (inspiradas en la bibliografia del proyecto, carpeta /Bib):
#   8) Estacionalidad: en que meses del año se concentran los viajes
#   9) Ranking de destinos mas visitados, separado en bilaterales y multilaterales
#   9.3) Cantidad de foros/cumbres multilaterales distintos, por periodo (Peña 2005)
#   9.4) Composicion Bilateral/Multilateral/Otro por pais, no por año (Lee & Kim 2024)
#
# Como usar: abrir este archivo en RStudio con el working directory en la
# carpeta que CONTIENE "Base Viaje Presidenciales Latam" (ver README.txt).
# Cada grafico/tabla se guarda como PNG (y algunas tambien como CSV) en
# 08_ANALISIS_R/outputs/.
# ================================================================================

## ---- 0. Setup ----------------------------------------------------------------
setwd("C:/Users/alejo/OneDrive/Escritorio/PE Latam/Política Exterior Latam/Viajes de Presidentes - Latam")

paquetes <- c("readxl", "dplyr", "ggplot2", "lubridate", "scales", "forcats", "tidyr", "stringr", "gridExtra")
faltantes <- paquetes[!paquetes %in% installed.packages()[, "Package"]]
if (length(faltantes) > 0) install.packages(faltantes)

library(readxl)
library(dplyr)
library(ggplot2)
library(lubridate)
library(scales)
library(forcats)
library(tidyr)
library(stringr)
library(gridExtra)
library(grid)

RUTA_EXCEL   <- "Base Viaje Presidenciales Latam/04_BASE_FINAL/Base_COLT_Sudamerica.xlsx"
RUTA_OUTPUTS <- "Base Viaje Presidenciales Latam/08_ANALISIS_R/outputs"
dir.create(RUTA_OUTPUTS, showWarnings = FALSE, recursive = TRUE)

ANIO_DESDE <- 1994
ANIO_HASTA <- 2025  # 2026 se deja afuera a proposito: todavia no esta tan
                     # mapeado/verificado como el resto de la base. Cuando se
                     # complete, solo hay que subir este numero.

# Los 12 paises sudamericanos de la planilla (no hace falta filtrar por
# pais: el archivo ya esta recortado a Sudamerica). Se deja el vector solo
# para las etiquetas en espaniol usadas en los graficos.
etiquetas_es <- c(
  "Argentina" = "Argentina", "Bolivia" = "Bolivia", "Brazil" = "Brasil",
  "Chile" = "Chile", "Colombia" = "Colombia", "Ecuador" = "Ecuador",
  "Guyana" = "Guyana", "Paraguay" = "Paraguay", "Peru" = "Peru",
  "Suriname" = "Surinam", "Uruguay" = "Uruguay", "Venezuela" = "Venezuela"
)

# --------------------------------------------------------------------------
# PALETA: solo blanco / negro / grises, como suele verse en papers
# academicos impresos en blanco y negro. Se combina con linetype/shape
# donde hace falta distinguir series sin depender del color.
# --------------------------------------------------------------------------
gris_9   <- "#111111"  # casi negro
gris_7   <- "#404040"
gris_6   <- "#595959"
gris_5   <- "#737373"
gris_4   <- "#8C8C8C"
gris_3   <- "#A6A6A6"
gris_2   <- "#BFBFBF"
gris_1   <- "#D9D9D9"  # gris muy claro

# --------------------------------------------------------------------------
# tema_journal(): estetica pensada para figuras DENTRO de un paper LaTeX, en
# la linea de lo que se ve en revistas de Ciencia Politica/RRII de primer
# nivel (ISQ, APSR, LARR, etc.):
#   - Sin titulo/subtitulo/nota-fuente dentro de la imagen (eso va en el
#     \caption{} del documento -ver labs() de cada grafico, ya no llevan
#     title=/subtitle=/caption=).
#   - Tipografia serif, para que combine con el cuerpo del texto en LaTeX
#     (Computer Modern/Latin Modern por defecto en un articulo estandar).
#   - Sin grilla vertical; grilla horizontal apenas visible, solo como
#     referencia para leer valores del eje Y.
#   - Ejes finos, sin caja completa alrededor del grafico (menos "chartjunk").
#   - Leyenda abajo, chica y sin borde, para que no compita con los datos.
# --------------------------------------------------------------------------
FUENTE_BASE <- "serif"

tema_journal <- function(base_size = 12) {
  theme_minimal(base_size = base_size, base_family = FUENTE_BASE) +
    theme(
      panel.grid.minor = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.major.y = element_line(color = gris_1, linewidth = 0.25),
      axis.line.x = element_line(color = gris_9, linewidth = 0.35),
      axis.line.y = element_blank(),
      axis.ticks.x = element_line(color = gris_9, linewidth = 0.35),
      axis.ticks.y = element_blank(),
      axis.title = element_text(size = rel(0.9), color = gris_9),
      axis.text = element_text(size = rel(0.85), color = gris_7),
      strip.background = element_rect(fill = gris_1, color = NA),
      strip.text = element_text(color = "black", face = "bold", size = rel(0.8), family = FUENTE_BASE),
      plot.title = element_blank(),
      plot.subtitle = element_blank(),
      plot.caption = element_blank(),
      legend.position = "bottom",
      legend.title = element_text(size = rel(0.85)),
      legend.text = element_text(size = rel(0.8)),
      legend.key = element_blank(),
      legend.background = element_blank(),
      panel.background = element_rect(fill = "white", color = NA),
      plot.background = element_rect(fill = "white", color = NA),
      plot.margin = margin(8, 12, 8, 8)
    )
}
theme_set(tema_journal())
update_geom_defaults("text", list(family = FUENTE_BASE))

# Funcion reutilizable para guardar cualquier data.frame como imagen de
# tabla (ademas del CSV), en blanco/negro/grises, sin depender de paquetes
# externos de renderizado web (gt+webshot, etc.) que pueden no estar
# instalados.
## NOTA (Version 6): "titulo" ya no se usa en las llamadas de este script -el
## \caption{} de LaTeX en el .Rnw cumple ese rol- pero se deja como parametro
## opcional por si hace falta reutilizar la funcion fuera del paper.
guardar_tabla_imagen <- function(df, archivo, titulo = NULL, ancho = 9, alto = NULL) {
  if (is.null(alto)) alto <- 0.5 + 0.32 * (nrow(df) + 1)
  tema_tabla <- gridExtra::ttheme_minimal(
    core = list(bg_params = list(fill = rep(c("white", gris_1), length.out = nrow(df)), col = NA),
                fg_params = list(col = "black", fontsize = 10, fontfamily = FUENTE_BASE)),
    colhead = list(bg_params = list(fill = gris_7, col = NA),
                   fg_params = list(col = "white", fontsize = 10, fontface = "bold", fontfamily = FUENTE_BASE))
  )
  tabla_grob <- gridExtra::tableGrob(df, rows = NULL, theme = tema_tabla)
  if (!is.null(titulo)) {
    titulo_grob <- grid::textGrob(titulo, gp = grid::gpar(fontsize = 13, fontface = "bold", fontfamily = FUENTE_BASE), x = 0, hjust = 0)
    tabla_grob <- gridExtra::arrangeGrob(titulo_grob, tabla_grob, ncol = 1, heights = grid::unit(c(0.5, 1), "null"))
    alto <- alto + 0.5
  }
  png(file.path(RUTA_OUTPUTS, archivo), width = ancho, height = alto, units = "in", res = 150)
  grid::grid.draw(tabla_grob)
  dev.off()
}


## ---- 1. Carga y preparacion de datos ------------------------------------------

colt_raw <- read_excel(RUTA_EXCEL, sheet = "Datos_COLT_Sudamerica")

# 1.1 Fechas: la columna llega con tipos mezclados (texto ISO y fechas
#     nativas de Excel segun la fila) porque se fue editando con distintas
#     herramientas. Forma robusta: pasar todo a texto y quedarse con los
#     primeros 10 caracteres (YYYY-MM-DD).
parsear_fecha <- function(x) {
  x_txt <- as.character(x)
  ymd(substr(x_txt, 1, 10))
}

# 1.2 Nombres de mandatario: COLT trae versiones sin tilde ("Alberto
#     Fernandez") y las filas que agregamos nosotros (PELATAM) traen tilde
#     en espaniol ("Alberto Fernández") -> sin normalizar, cualquier
#     agrupacion por presidente cuenta a la misma persona dos veces.
quitar_tildes <- function(x) iconv(x, from = "UTF-8", to = "ASCII//TRANSLIT")

colt <- colt_raw %>%
  mutate(
    TripStartDate = parsear_fecha(TripStartDate),
    TripEndDate   = parsear_fecha(TripEndDate),
    TripDuration  = as.numeric(as.character(TripDuration)),
    Year          = year(TripStartDate),
    Periodo5      = (Year %/% 5) * 5,
    Mes           = month(TripStartDate, label = TRUE, abbr = TRUE, locale = "es_ES.UTF-8"),
    Pais_ES       = recode(LeaderCountryOrIGO, !!!etiquetas_es),
    Leader_key    = str_to_lower(quitar_tildes(LeaderFullName))
  ) %>%
  filter(!is.na(Year), Year >= ANIO_DESDE, Year <= ANIO_HASTA)

# Si el locale es_ES no esta disponible en la maquina, Mes puede quedar en
# blanco/NA -> fallback a numero de mes (1-12) para no romper el pipeline.
if (all(is.na(colt$Mes))) {
  colt <- colt %>% mutate(Mes = factor(month(TripStartDate), levels = 1:12))
}

# Etiqueta canonica por mandatario: la version (con tilde) mas frecuente
# dentro de cada Leader_key
etiqueta_por_leader <- colt %>%
  count(Leader_key, LeaderFullName, sort = TRUE) %>%
  group_by(Leader_key) %>%
  slice_max(n, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  select(Leader_key, Leader_nombre = LeaderFullName)

colt <- colt %>% left_join(etiqueta_por_leader, by = "Leader_key")

# 1.2b Periodos de mandato (investigacion verificada con fuentes, ver
#      09_PAPER/mandatos_presidenciales.csv). Se usa para etiquetar
#      "Nombre (periodo)" en los graficos/tablas donde el usuario lo pidio
#      (total de viajes por mandatario, destino favorito por presidente).
#      Mandatarios con mas de un periodo NO consecutivo (ej. Lula, Bachelet,
#      Piñera, Alan Garcia, Sanchez de Lozada, Sanguinetti, Tabare Vazquez,
#      Venetiaan) llevan ambos periodos separados por ";" en Periodo_label,
#      tal como vienen en el CSV -no se calculan a partir de los anios de
#      viaje, que quedarian truncados por ANIO_DESDE=1994 o mezclarian
#      mandatos separados en un solo rango.
RUTA_MANDATOS <- "Base Viaje Presidenciales Latam/04_BASE_FINAL/mandatos_presidenciales.csv"
mandatos <- tryCatch(read.csv(RUTA_MANDATOS, stringsAsFactors = FALSE), error = function(e) NULL)

# NOTA (pedido del usuario, correccion Figura 1): varios mandatos que siguen
# en curso al momento de escribir el paper se codifican con el placeholder
# "2099" (para que las reglas de filtrado "solo durante el mandato" los
# tomen como abiertos). Para que las ETIQUETAS que se muestran en cuadros y
# figuras no digan "(...-2099)", se reemplaza 2099 por 2025 SOLO en el texto
# de Periodo_label (no en las fechas MandateEnd_1/2 usadas para filtrar).
if (!is.null(mandatos)) {
  mandatos$Periodo_label <- gsub("2099", "2025", mandatos$Periodo_label, fixed = TRUE)
}

leaders_etiqueta <- etiqueta_por_leader
if (!is.null(mandatos)) {
  leaders_etiqueta <- leaders_etiqueta %>%
    left_join(mandatos %>% select(Leader_key, Pais_mandato = Pais, Periodo_label), by = "Leader_key") %>%
    mutate(Leader_etiqueta = if_else(!is.na(Periodo_label),
                                      paste0(Leader_nombre, " (", Periodo_label, ")"),
                                      Leader_nombre))
  sin_match <- leaders_etiqueta %>% filter(is.na(Periodo_label)) %>% pull(Leader_nombre)
  if (length(sin_match) > 0) {
    warning("Mandatarios sin fecha de mandato en mandatos_presidenciales.csv (se usa solo el nombre, sin periodo): ",
            paste(sin_match, collapse = "; "))
  }
} else {
  leaders_etiqueta <- leaders_etiqueta %>% mutate(Leader_etiqueta = Leader_nombre)
  warning("No se pudo leer ", RUTA_MANDATOS, " -> los graficos por mandatario van sin periodo entre parentesis.")
}

colt <- colt %>% left_join(leaders_etiqueta %>% select(Leader_key, Leader_etiqueta), by = "Leader_key")

# 1.2c REGLA: la base de trabajo del paper solo debe incluir viajes
#      realizados DURANTE el mandato del presidente (pedido del usuario,
#      2026-08-27). Ejemplo del problema que esto corrige: el viaje de Jair
#      Bolsonaro a EE.UU. (30-dic-2022 a 30-mar-2023) arranca 2 dias antes de
#      que termine su mandato (01-ene-2023) pero se extiende casi 3 meses
#      DESPUES de dejar el cargo -no deberia contarse como viaje
#      presidencial, aunque el dato en si sea real y este bien documentado.
#      La regla exige que TANTO el inicio COMO el fin del viaje esten dentro
#      del mandato (no alcanza con que arranque a tiempo). Si TripEndDate
#      esta vacio se usa TripStartDate como fin (mejor estimacion posible).
#      Verificado contra toda la base: en la ventana 1994-2025 esta regla
#      excluye exactamente 1 fila -el viaje de Bolsonaro-, lo que confirma
#      que no es un problema sistemico sino ese caso puntual.
#      Mandatarios sin dato de mandato verificado (no deberia haber ninguno,
#      pero por las dudas) NO se filtran -se avisa con un warning en vez de
#      borrar viajes reales por falta de informacion en la tabla de apoyo.
if (!is.null(mandatos)) {
  mandatos_fechas <- mandatos %>%
    mutate(
      MandateStart_1 = ymd(MandateStart_1),
      MandateEnd_1   = ymd(MandateEnd_1),
      MandateStart_2 = ymd(na_if(MandateStart_2, "")),
      MandateEnd_2   = ymd(na_if(MandateEnd_2, ""))
    ) %>%
    select(Leader_key, MandateStart_1, MandateEnd_1, MandateStart_2, MandateEnd_2)

  colt <- colt %>%
    left_join(mandatos_fechas, by = "Leader_key") %>%
    mutate(
      TripEndDate_efectivo = if_else(is.na(TripEndDate), TripStartDate, TripEndDate),
      en_periodo_1 = !is.na(MandateStart_1) & TripStartDate >= MandateStart_1 & TripEndDate_efectivo <= MandateEnd_1,
      en_periodo_2 = !is.na(MandateStart_2) & TripStartDate >= MandateStart_2 & TripEndDate_efectivo <= MandateEnd_2,
      dentro_del_mandato = case_when(
        is.na(MandateStart_1) ~ NA,
        TRUE ~ en_periodo_1 | en_periodo_2
      ),
      # Anio_mandato: "año 1", "año 2"... del mandato en curso al momento del
      # viaje (se conserva como columna de colt -no se dropea mas abajo- para
      # la seccion 11, "viajes por año de mandato").
      Anio_mandato = case_when(
        en_periodo_1 ~ floor(as.numeric(TripStartDate - MandateStart_1) / 365.25) + 1,
        en_periodo_2 ~ floor(as.numeric(TripStartDate - MandateStart_2) / 365.25) + 1,
        TRUE ~ NA_real_
      )
    )

  sin_dato_mandato <- colt %>% filter(is.na(dentro_del_mandato)) %>% distinct(Leader_nombre) %>% pull(Leader_nombre)
  if (length(sin_dato_mandato) > 0) {
    warning("Mandatarios SIN dato de mandato verificado -sus viajes NO se filtraron por la regla 'solo durante el mandato': ",
            paste(sin_dato_mandato, collapse = "; "))
  }

  viajes_excluidos_fuera_mandato <- colt %>% filter(dentro_del_mandato == FALSE)
  if (nrow(viajes_excluidos_fuera_mandato) > 0) {
    cat("\n--- Viajes EXCLUIDOS por la regla 'solo durante el mandato' (", nrow(viajes_excluidos_fuera_mandato), ") ---\n", sep = "")
    print(viajes_excluidos_fuera_mandato %>%
            select(Leader_nombre, LeaderCountryOrIGO, TripStartDate, TripEndDate, CountryVisited))
  }

  colt <- colt %>%
    filter(is.na(dentro_del_mandato) | dentro_del_mandato == TRUE) %>%
    select(-MandateStart_1, -MandateEnd_1, -MandateStart_2, -MandateEnd_2,
           -TripEndDate_efectivo, -dentro_del_mandato, -en_periodo_1, -en_periodo_2)
} else {
  warning("No se pudo aplicar la regla 'solo viajes durante el mandato' -falta mandatos_presidenciales.csv.")
}

# 1.2c-bis MANDATOS INDIVIDUALES (un mandato constitucional = un tramo),
#      distinto de mandatos_fechas de arriba (que junta reelecciones
#      consecutivas en un solo tramo, que es lo que corresponde para la
#      regla "durante el mandato"). Esta tabla se usa solo para separar,
#      dentro de un mismo presidente, el primer/segundo/tercer mandato en
#      el Cuadro de destino favorito y en el Cuadro de perfil regional
#      (pedido del usuario). Para los pares de mandatos NO consecutivos (con
#      un hueco en el medio, ej. Lula 2003-2011 y 2023-en curso; Bachelet;
#      Piñera) alcanza con mandatos_fechas -ya vienen en columnas separadas
#      MandateStart/End_1 y _2-. Para los presidentes reelectos de forma
#      CONSECUTIVA (sin hueco) mandatos_presidenciales.csv guarda un unico
#      tramo continuo (ej. CFK 2007-2015 en una sola fila), asi que hace
#      falta la fecha exacta de la reasuncion para partirlo. Esas fechas se
#      investigaron a mano (mismo criterio y mismas fuentes que el
#      crosswalk de Base_Ideologia_Presidencial; Jagdeo y Bouterse no estan
#      en esa base -no tienen puntaje de ideologia- y se investigaron de
#      nuevo especificamente para este punto).
if (!is.null(mandatos)) {
  mandato_terminos_manual <- tribble(
    ~Leader_key, ~term_n, ~term_start, ~term_end,
    "carlos saul menem", 1L, "1989-07-08", "1995-07-08",
    "carlos saul menem", 2L, "1995-07-08", "1999-12-10",
    "cristina fernandez de kirchner", 1L, "2007-12-10", "2011-12-10",
    "cristina fernandez de kirchner", 2L, "2011-12-10", "2015-12-10",
    "fernando henrique cardoso", 1L, "1995-01-01", "1999-01-01",
    "fernando henrique cardoso", 2L, "1999-01-01", "2003-01-01",
    "luiz inacio lula da silva", 1L, "2003-01-01", "2007-01-01",
    "luiz inacio lula da silva", 2L, "2007-01-01", "2011-01-01",
    "dilma rousseff", 1L, "2011-01-01", "2015-01-01",
    "dilma rousseff", 2L, "2015-01-01", "2016-08-31",
    "evo morales", 1L, "2006-01-22", "2010-01-22",
    "evo morales", 2L, "2010-01-22", "2015-01-22",
    "evo morales", 3L, "2015-01-22", "2019-11-10",
    "alvaro uribe", 1L, "2002-08-07", "2006-08-07",
    "alvaro uribe", 2L, "2006-08-07", "2010-08-07",
    "juan manuel santos", 1L, "2010-08-07", "2014-08-07",
    "juan manuel santos", 2L, "2014-08-07", "2018-08-07",
    "rafael correa", 1L, "2007-01-15", "2009-08-10",
    "rafael correa", 2L, "2009-08-10", "2013-05-24",
    "rafael correa", 3L, "2013-05-24", "2017-05-24",
    "alberto fujimori", 1L, "1990-07-28", "1995-07-28",
    "alberto fujimori", 2L, "1995-07-28", "2000-07-28",
    "alberto fujimori", 3L, "2000-07-28", "2000-11-21",
    "hugo chavez", 1L, "1999-02-02", "2000-08-19",
    "hugo chavez", 2L, "2000-08-19", "2007-01-10",
    "hugo chavez", 3L, "2007-01-10", "2013-03-05",
    "nicolas maduro", 1L, "2013-04-19", "2019-01-10",
    "nicolas maduro", 2L, "2019-01-10", "2099-12-31",
    "bharrat jagdeo", 1L, "1999-08-11", "2001-03-19",
    "bharrat jagdeo", 2L, "2001-03-19", "2006-09-02",
    "bharrat jagdeo", 3L, "2006-09-02", "2011-12-03",
    "desi bouterse", 1L, "2010-08-12", "2015-08-12",
    "desi bouterse", 2L, "2015-08-12", "2020-08-12"
  ) %>%
    mutate(term_start = ymd(term_start), term_end = ymd(term_end))

  leaders_multi_consecutivo <- unique(mandato_terminos_manual$Leader_key)

  mandato_terminos_auto <- mandatos_fechas %>%
    filter(!(Leader_key %in% leaders_multi_consecutivo)) %>%
    pivot_longer(
      cols = c(MandateStart_1, MandateEnd_1, MandateStart_2, MandateEnd_2),
      names_to = c(".value", "term_n"),
      names_pattern = "(MandateStart|MandateEnd)_(\\d)"
    ) %>%
    rename(term_start = MandateStart, term_end = MandateEnd) %>%
    filter(!is.na(term_start)) %>%
    mutate(term_n = as.integer(term_n))

  mandato_terminos <- bind_rows(mandato_terminos_auto, mandato_terminos_manual) %>%
    arrange(Leader_key, term_start) %>%
    mutate(
      # Etiqueta de periodo para cuadros: mismo criterio que Figura 1
      # (mandatos en curso, con placeholder 2099, se muestran como "2025").
      term_label = paste0(format(term_start, "%Y"), "-",
                           if_else(term_end >= ymd("2099-01-01"), "2025", format(term_end, "%Y")))
    )
} else {
  mandato_terminos <- NULL
  warning("No se pudo construir la tabla de mandatos individuales -falta mandatos_presidenciales.csv.")
}
# NOTA: el join de esta tabla contra "colt" (armando colt_con_termino) se
# hace mas abajo, DESPUES de limpiar CountryVisited=="Unknown" (1.2d) y de
# calcular Visit_Category (1.3) -los Cuadros 4 y 5 necesitan ambas columnas.

# 1.2d "Unknown" -> NA en los campos de destino. Algunas filas (viajes
#      privados sin informacion disponible sobre el destino, ej. Yamandu
#      Orsi dic-2025: "Private trip; No available information on activities
#      conducted during the trip") tienen CountryVisited/RegionVisited/
#      SubRegionVisited/CityVisited literalmente en texto "Unknown" -no es
#      un campo vacio (NA), es el string "Unknown"-. Sin este paso, esos
#      valores aparecen como una categoria fantasma "Unknown" en los
#      graficos por region/pais en vez de quedar afuera como el resto de
#      los datos faltantes (que sí se filtran con is.na() en todo el
#      script). Convertirlos a NA real ademas de este punto hace que todos
#      los filter(!is.na(...)) que ya existen mas abajo los excluyan solos,
#      sin tener que tocar cada grafico uno por uno. El viaje en si SIGUE
#      contando en los totales generales (ficha_general, viajes por anio) -
#      solo se excluye de los analisis que agrupan por destino/region.
n_unknown_antes <- sum(colt$CountryVisited == "Unknown", na.rm = TRUE)
if (n_unknown_antes > 0) {
  cat("\nViajes con destino 'Unknown' (se excluyen de graficos por pais/region, no de los totales):", n_unknown_antes, "\n")
  print(colt %>% filter(CountryVisited == "Unknown") %>%
          select(Leader_nombre, LeaderCountryOrIGO, TripStartDate, TripEndDate, Notes))
}
colt <- colt %>%
  mutate(across(c(CountryVisited, RegionVisited, SubRegionVisited, CityVisited),
                ~ na_if(str_trim(.), "Unknown")))

# 1.3 Categoria de visita derivada (NO es un campo nativo de COLT). Se
#     calcula aca -temprano- porque se usa tanto en la seccion descriptiva
#     como en las preguntas 4-5 y en el ranking de destinos.
#       Multilateral   si AttendedMultilatEvent == "Yes"  (tiene prioridad)
#       Bilateral      si no es Multilateral y MetHostHoGS == "Yes"
#       Other          si no es Multilateral y MetHostHoGS == "No"
#       Sin dato       si MetHostHoGS esta vacio
colt <- colt %>%
  mutate(
    Visit_Category = case_when(
      AttendedMultilatEvent == "Yes" ~ "Multilateral",
      MetHostHoGS == "Yes" ~ "Bilateral",
      MetHostHoGS == "No" ~ "Other",
      TRUE ~ "Sin dato"
    )
  )

cat("Filas cargadas (", ANIO_DESDE, "-", ANIO_HASTA, ", 12 paises):", nrow(colt),
    "| Paises:", n_distinct(colt$LeaderCountryOrIGO),
    "| Mandatarios distintos:", n_distinct(colt$Leader_key), "\n")

# 1.3b Asignar a cada viaje su termino/mandato individual (ver tabla
#      mandato_terminos, seccion 1.2c-bis). Se hace aca -ya con Unknown->NA
#      y Visit_Category calculados- porque los Cuadros 4 y 5 (destino
#      favorito y perfil regional POR MANDATO) necesitan ambas columnas.
if (!is.null(mandato_terminos)) {
  colt_con_termino <- colt %>%
    inner_join(mandato_terminos, by = "Leader_key") %>%
    filter(TripStartDate >= term_start, TripStartDate < term_end) %>%
    mutate(Leader_etiqueta_termino = paste0(Leader_nombre, " (", term_label, ")"))

  dup_terminos <- colt_con_termino %>% count(TripID) %>% filter(n > 1)
  if (nrow(dup_terminos) > 0) {
    warning(nrow(dup_terminos), " viajes cayeron en mas de un termino/mandato individual -revisar mandato_terminos_manual.")
  }
  colt_con_termino <- colt_con_termino %>% distinct(TripID, .keep_all = TRUE)

  sin_termino <- colt %>% filter(!(TripID %in% colt_con_termino$TripID)) %>% distinct(Leader_nombre) %>% pull(Leader_nombre)
  if (length(sin_termino) > 0) {
    warning("Mandatarios cuyos viajes no calzaron con ningun tramo de mandato_terminos (revisar): ",
            paste(sin_termino, collapse = "; "))
  }
} else {
  colt_con_termino <- colt %>% mutate(term_n = NA_integer_, term_label = NA_character_,
                                       Leader_etiqueta_termino = Leader_nombre)
}


## ---- 2. Descriptivos generales -------------------------------------------------
## Todo lo que sigue es puramente descriptivo (totales, no evolucion en el
## tiempo) y se deja al principio del script, con imagen ademas de CSV/consola.

# 2.1 Ficha general
ficha_general <- data.frame(
  Indicador = c("Total de viajes registrados", "Periodo cubierto", "Cantidad de paises",
                "Cantidad de mandatarios distintos", "Viajes bilaterales (%)",
                "Viajes multilaterales (%)", "Viajes 'Otro' (%)"),
  Valor = c(
    format(nrow(colt), big.mark = "."),
    paste0(ANIO_DESDE, "-", ANIO_HASTA),
    as.character(n_distinct(colt$LeaderCountryOrIGO)),
    as.character(n_distinct(colt$Leader_key)),
    scales::percent(mean(colt$Visit_Category == "Bilateral"), accuracy = 0.1),
    scales::percent(mean(colt$Visit_Category == "Multilateral"), accuracy = 0.1),
    scales::percent(mean(colt$Visit_Category == "Other"), accuracy = 0.1)
  )
)
print(ficha_general)
guardar_tabla_imagen(ficha_general, "00a_ficha_general.png", ancho = 7, alto = 2.6)
write.csv(ficha_general, file.path(RUTA_OUTPUTS, "00a_ficha_general.csv"), row.names = FALSE)
# Nota: se sigue guardando el PNG por compatibilidad, pero en el paper esta
# tabla ahora se arma como Cuadro (xtable) a partir del CSV, no como imagen.

# 2.1b Diferencias encontradas vs la Base COLT, por pais.
#
# A diferencia del resto de las tablas de esta seccion, esta NO se calcula a
# partir del data.frame `colt` en memoria: las 4 columnas resumen el trabajo
# de verificacion pais por pais (campaña "COLT-verificacion") y se recalcularon
# a mano, en una sola pasada uniforme, a partir de las fuentes primarias de
# cada campaña (05_BITACORA/anexos_colt_sudamerica/) el 2026-09-01:
#   - Agregados:  cantidad de filas TripID "PELATAM-<ISO3>-n" actualmente en
#     el archivo madre para ese pais -viajes que investigamos y agregamos
#     porque COLT no los tenia-. Es un conteo directo sobre la base final
#     (ground truth), no depende del formato de los logs de cada campaña.
#   - Modificados: cantidad de filas NATIVAS de COLT (no PELATAM) a las que
#     le corregimos al menos un campo, contando cada TripID una sola vez aunque
#     se le hayan corregido varios campos. Fuente: los archivos
#     resultados_*.json de cada campaña (categoria "correcciones"/
#     "Nuestro_correcto"/"Ninguno_exacto" segun la generacion del pipeline
#     que le toco a cada pais). Validado cruzando contra el tag "[PE-Latam...
#     corregido de" en la columna Notes del archivo madre para los 5 paises
#     cuyo pipeline lo escribe (Bolivia, Paraguay, Uruguay, Peru, Colombia):
#     coincide exactamente.
#   - Eliminados: candidatos propios (de una etapa temprana del proyecto,
#     "nuestro_unico" vs COLT) que se investigaron pero finalmente NO se
#     incorporaron a la base -veredicto "Descartado"/"descartar" en los logs
#     colt_unico de cada pais-. Solo aplica a los 5 paises que pasaron por esa
#     etapa (Argentina, Brasil, Chile, Paraguay, Uruguay); Bolivia/Peru/
#     Colombia se construyeron con el pipeline unificado posterior, que no
#     tiene esta etapa separada.
#   - Pendientes de validar: filas (nativas de COLT o de nuestra propia
#     investigacion temprana) que se revisaron pero para las que no se
#     encontro fuente independiente que permita confirmar NI corregir el
#     dato -quedan marcadas "no_verificable", el dato de COLT no se toca-.
#     Un TripID puede figurar en Modificados y en Pendientes a la vez si un
#     campo se pudo corregir y otro del mismo viaje no.
# Ecuador, Guyana y Surinam y Venezuela todavia no pasaron por esta
# verificacion (quedan con la cobertura original de COLT sin cruzar), se
# marcan "Sin iniciar" en las 4 columnas hasta que se investiguen.
diferencias_colt <- data.frame(
  Pais = c("Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador",
           "Guyana", "Paraguay", "Peru", "Surinam", "Uruguay", "Venezuela"),
  Agregados = c("25", "12", "27", "60", "7", "Sin iniciar",
                "Sin iniciar", "49", "5", "Sin iniciar", "29", "Sin iniciar"),
  Modificados = c("96", "14", "94", "101", "39", "Sin iniciar",
                  "Sin iniciar", "54", "25", "Sin iniciar", "56", "Sin iniciar"),
  Eliminados = c("4", "0", "5", "7", "0", "Sin iniciar",
                 "Sin iniciar", "16", "0", "Sin iniciar", "6", "Sin iniciar"),
  Pendientes_de_validar = c("75", "30", "49", "68", "50", "Sin iniciar",
                             "Sin iniciar", "120", "28", "Sin iniciar", "69", "Sin iniciar"),
  stringsAsFactors = FALSE
)
print(diferencias_colt)
guardar_tabla_imagen(diferencias_colt, "00a2_diferencias_colt.png", ancho = 9, alto = 4.2)
write.csv(diferencias_colt, file.path(RUTA_OUTPUTS, "00a2_diferencias_colt.csv"), row.names = FALSE)

# 2.2 Total de viajes por pais (todo el periodo)
viajes_totales_pais <- colt %>%
  count(Pais_ES, name = "n_viajes") %>%
  arrange(desc(n_viajes))

g0b <- ggplot(viajes_totales_pais, aes(x = fct_reorder(Pais_ES, n_viajes), y = n_viajes)) +
  geom_col(fill = gris_6) +
  geom_text(aes(label = n_viajes), hjust = -0.2, size = 3, family = FUENTE_BASE, color = "black") +
  coord_flip(clip = "off") +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(x = NULL, y = "Cantidad de viajes")

print(g0b)
ggsave(file.path(RUTA_OUTPUTS, "00b_viajes_totales_por_pais.png"), g0b, width = 9, height = 6, dpi = 150)
write.csv(viajes_totales_pais, file.path(RUTA_OUTPUTS, "00b_viajes_totales_por_pais.csv"), row.names = FALSE)

# 2.3 Total de viajes por mandatario (todos, ordenados). Etiqueta con el
#     periodo de mandato entre parentesis (ver 1.2b / mandatos_presidenciales.csv).
#     El grafico (00c) se limita a mandatarios con MAS DE 50 viajes -pedido
#     del usuario para que la figura sea legible-; la tabla completa (CSV)
#     se sigue exportando con todos los mandatarios, sin ese recorte.
viajes_totales_mandatario <- colt %>%
  count(Leader_etiqueta, LeaderCountryOrIGO, name = "n_viajes") %>%
  arrange(desc(n_viajes))

viajes_totales_mandatario_g0c <- viajes_totales_mandatario %>% filter(n_viajes > 50)

g0c <- ggplot(viajes_totales_mandatario_g0c, aes(x = fct_reorder(Leader_etiqueta, n_viajes), y = n_viajes)) +
  geom_col(fill = gris_6) +
  coord_flip() +
  labs(x = NULL, y = "Cantidad de viajes")

print(g0c)
ggsave(file.path(RUTA_OUTPUTS, "00c_viajes_totales_por_mandatario.png"), g0c,
       width = 9, height = 2 + 0.16 * nrow(viajes_totales_mandatario_g0c), dpi = 150)
write.csv(viajes_totales_mandatario, file.path(RUTA_OUTPUTS, "00c_viajes_totales_por_mandatario.csv"), row.names = FALSE)

# 2.4 Tabla de estadisticos descriptivos (estilo "Tabla 1" de un paper:
#     media/desvio/min/max de viajes por Mandatario-Anio y de duracion).
#     CAMBIO (pedido del usuario, correccion Cuadro 3): las filas de "viajes"
#     ahora agrupan por MANDATARIO-anio (Leader_key x Year), no por
#     pais-anio -asi la unidad de analisis coincide con la del resto del
#     paper (un mandatario por fila, no un pais). "Duracion del viaje" queda
#     igual que antes (pedido explicito del usuario: "el de Duracion del
#     viaje esta bien"), contando VIAJES INDIVIDUALES -son unidades de
#     observacion distintas de las filas de arriba, por eso n_obs difiere
#     tanto entre filas. Se deja explicito en la columna Unidad_n_obs para
#     que no se lea como un error.
#     El viaje de Jair Bolsonaro a Estados Unidos de 91 dias (30-dic-2022 a
#     30-mar-2023) YA NO esta en esta tabla: se excluyo con la regla de
#     seccion 1.2c (empezo 2 dias antes de terminar su mandato pero se
#     extendio casi 3 meses despues de dejar el cargo). El maximo actual de
#     "Duracion del viaje" corresponde a otro viaje real y bien documentado:
#     Hugo Chavez, Venezuela -> Cuba, 10-dic-2012 a 18-feb-2013 (71 dias,
#     tratamiento medico por su enfermedad; siguio siendo presidente en
#     ejercicio durante todo ese periodo -murio en el cargo el 05-mar-2013-,
#     por eso el viaje SI queda dentro de la regla de "durante el mandato").
resumen_estadisticos <- bind_rows(
  colt %>% count(Year, Leader_key, name = "viajes") %>%
    summarise(variable = "Viajes por Mandatario-Anio", media = round(mean(viajes), 1), de = round(sd(viajes), 1),
              minimo = min(viajes), maximo = max(viajes), n_obs = n(),
              Unidad_n_obs = "Combinaciones mandatario-anio"),
  colt %>% filter(!is.na(TripDuration)) %>%
    summarise(variable = "Duracion del viaje (dias)", media = round(mean(TripDuration), 1), de = round(sd(TripDuration), 1),
              minimo = min(TripDuration), maximo = max(TripDuration), n_obs = n(),
              Unidad_n_obs = "Viajes individuales"),
  colt %>% count(Year, Leader_key, Visit_Category) %>%
    filter(Visit_Category == "Bilateral") %>%
    summarise(variable = "Viajes Bilaterales por Mandatario-Anio", media = round(mean(n), 1), de = round(sd(n), 1),
              minimo = min(n), maximo = max(n), n_obs = n(),
              Unidad_n_obs = "Combinaciones mandatario-anio"),
  colt %>% count(Year, Leader_key, Visit_Category) %>%
    filter(Visit_Category == "Multilateral") %>%
    summarise(variable = "Viajes Multilaterales por Mandatario-Anio", media = round(mean(n), 1), de = round(sd(n), 1),
              minimo = min(n), maximo = max(n), n_obs = n(),
              Unidad_n_obs = "Combinaciones mandatario-anio")
)
print(resumen_estadisticos)
write.csv(resumen_estadisticos, file.path(RUTA_OUTPUTS, "00d_resumen_estadisticos_descriptivos.csv"), row.names = FALSE)
guardar_tabla_imagen(resumen_estadisticos, "00d_resumen_estadisticos_descriptivos.png", ancho = 10, alto = 2.6)


## ---- 3. Pregunta 1: evolucion general de la cantidad de viajes por anio -------

viajes_por_anio <- colt %>% count(Year, name = "n_viajes")
promedio_anual_viajes <- mean(viajes_por_anio$n_viajes, na.rm = TRUE)

g1 <- ggplot(viajes_por_anio, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_5) +
  geom_hline(yintercept = promedio_anual_viajes, linetype = "dashed", color = gris_9, linewidth = 0.5) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  labs(x = NULL, y = "Cantidad de viajes")

print(g1)
ggsave(file.path(RUTA_OUTPUTS, "01_viajes_por_anio.png"), g1, width = 10, height = 6, dpi = 150)

# Por pais: con 12 paises, usar color unico no distingue bien -> se factoriza
# en paneles (facet_wrap), todos en el mismo tono de gris.
viajes_por_anio_pais <- colt %>% count(Year, Pais_ES, name = "n_viajes")

# Promedio anual de viajes, calculado POR PAIS (un valor de referencia por
# panel), pedido del usuario para poder comparar cada anio contra su propio
# promedio historico.
promedio_anual_por_pais <- viajes_por_anio_pais %>%
  group_by(Pais_ES) %>%
  summarise(promedio = mean(n_viajes), .groups = "drop")

g1b <- ggplot(viajes_por_anio_pais, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_5) +
  geom_hline(data = promedio_anual_por_pais, aes(yintercept = promedio),
             color = gris_9, linetype = "dashed", linewidth = 0.4) +
  facet_wrap(~Pais_ES, ncol = 3) +
  labs(x = NULL, y = "Cantidad de viajes (linea punteada = promedio anual del pais)")

print(g1b)
ggsave(file.path(RUTA_OUTPUTS, "01b_viajes_por_anio_por_pais.png"), g1b, width = 11, height = 9, dpi = 150)


## ---- 4. Pregunta 2: que regiones se priorizan en cada epoca? -----------------

region_por_periodo <- colt %>%
  filter(!is.na(RegionVisited)) %>%
  count(Periodo5, RegionVisited) %>%
  group_by(Periodo5) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

n_regiones <- n_distinct(region_por_periodo$RegionVisited)
grises_regiones <- colorRampPalette(c(gris_9, gris_1))(n_regiones)

# Etiquetas de dato solo para las 3 regiones que pidio el usuario (dejar
# etiqueta en las 8 restantes satura el grafico). "Northern America" es el
# valor exacto que usa RegionVisited en la base (NO "North America": ese es
# un valor distinto y mucho menos frecuente).
# NOTA TECNICA: no se usa position_stack(vjust=0.5) en el geom_text porque,
# al pasarle solo un subconjunto de regiones (data= filtrada), ggplot
# apilaria SOLO esas 3 regiones entre si -no en su posicion real dentro del
# stack completo de 8 regiones-. Por eso el punto medio de cada segmento se
# calcula a mano, replicando el orden de apilado por defecto de ggplot
# (primer nivel del factor arriba de la barra -> para sumar desde abajo hay
# que ordenar en reversa, arrange(desc(RegionVisited))).
regiones_con_etiqueta <- c("Latin America and the Caribbean", "Europe", "Northern America")

region_por_periodo_stack <- region_por_periodo %>%
  arrange(Periodo5, desc(RegionVisited)) %>%
  group_by(Periodo5) %>%
  mutate(y_max = cumsum(participacion), y_min = y_max - participacion, y_mid = (y_min + y_max) / 2) %>%
  ungroup()

g2 <- ggplot(region_por_periodo, aes(x = factor(Periodo5), y = participacion, fill = RegionVisited)) +
  geom_col(position = "stack", color = "white", linewidth = 0.2) +
  geom_text(data = region_por_periodo_stack %>% filter(RegionVisited %in% regiones_con_etiqueta),
            aes(x = factor(Periodo5), y = y_mid, label = scales::percent(participacion, accuracy = 1)),
            inherit.aes = FALSE, size = 4, color = "white", family = FUENTE_BASE) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_manual(values = grises_regiones) +
  labs(x = "Periodo (bloques de 5 anios)", y = "Participacion", fill = "Region de destino") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

print(g2)
ggsave(file.path(RUTA_OUTPUTS, "02_regiones_por_periodo.png"), g2, width = 11, height = 6.5, dpi = 150)

region_por_anio <- colt %>%
  filter(!is.na(RegionVisited)) %>%
  count(Year, RegionVisited) %>%
  group_by(Year) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

g2b <- ggplot(region_por_anio, aes(x = Year, y = participacion, fill = RegionVisited)) +
  geom_area(position = "fill", color = "white", linewidth = 0.1) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_manual(values = grises_regiones) +
  labs(x = NULL, y = "Participacion", fill = "Region de destino")

print(g2b)
ggsave(file.path(RUTA_OUTPUTS, "02b_regiones_por_anio_area.png"), g2b, width = 11, height = 6.5, dpi = 150)


## ---- 5. Pregunta 3: cambio la duracion de los viajes? ------------------------

duracion_por_anio <- colt %>%
  filter(!is.na(TripDuration)) %>%
  group_by(Year) %>%
  summarise(duracion_media = mean(TripDuration), duracion_mediana = median(TripDuration), n = n())

g3 <- ggplot(duracion_por_anio, aes(x = Year, y = duracion_media)) +
  geom_line(color = gris_7, linewidth = 0.8) +
  geom_point(color = gris_9, size = 1.5) +
  labs(x = NULL, y = "Duracion promedio (dias)")

print(g3)
ggsave(file.path(RUTA_OUTPUTS, "03_duracion_por_anio.png"), g3, width = 10, height = 6, dpi = 150)

# 5c) Grafico combinado: cantidad total de viajes (barras) superpuesta con
#     la duracion promedio (linea), por anio. Eje izquierdo = cantidad de
#     viajes; eje derecho = duracion promedio en dias (misma escala visual,
#     reescalada con un factor para que ambas series se puedan leer juntas).
combo_anio <- viajes_por_anio %>% left_join(duracion_por_anio %>% select(Year, duracion_media), by = "Year")
factor_escala <- max(combo_anio$n_viajes, na.rm = TRUE) / max(combo_anio$duracion_media, na.rm = TRUE)

g3c <- ggplot(combo_anio, aes(x = Year)) +
  geom_col(aes(y = n_viajes), fill = gris_2) +
  geom_line(aes(y = duracion_media * factor_escala), color = "black", linewidth = 0.9) +
  geom_point(aes(y = duracion_media * factor_escala), color = "black", size = 1.6) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  scale_y_continuous(
    name = "Cantidad de viajes (barras)",
    sec.axis = sec_axis(~ . / factor_escala, name = "Duracion promedio en dias (linea)")
  ) +
  labs(x = NULL)

print(g3c)
ggsave(file.path(RUTA_OUTPUTS, "03c_viajes_y_duracion_combinado.png"), g3c, width = 11, height = 6.5, dpi = 150)


## ---- 6. Preguntas 4 y 5: Bilateral vs Multilateral vs Other, en el tiempo -----
## Que es "Other": viajes en los que el mandatario NO tuvo registrada una
## reunion con el jefe de Estado/Gobierno anfitrion (MetHostHoGS = "No") Y
## tampoco asistio a un evento multilateral (AttendedMultilatEvent = "No").
## En la practica suele tratarse de actos protocolares/ceremoniales,
## funerales, inauguraciones, escalas con agenda no bilateral, o visitas de
## trabajo sin una reunion de alto nivel documentada en la fuente.

## NOTA (pedido del usuario, correccion Figura 13): se excluye la categoria
## "Sin dato" (MetHostHoGS vacio, ver seccion 1.3) de estos dos graficos
## hasta que se resuelva ese problema de cobertura -antes se mostraba como
## una cuarta categoria "fantasma" sin poder explicarla. NO se excluyen esos
## viajes del resto del paper (ficha_general, totales, etc.), solo de estos
## dos graficos de categoria de visita.
categoria_por_anio <- colt %>%
  filter(Visit_Category != "Sin dato") %>%
  count(Year, Visit_Category) %>%
  group_by(Year) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

colores_categoria <- c("Bilateral" = gris_9, "Multilateral" = gris_5, "Other" = gris_2)

## Figura 12 (correccion pedida por el usuario): antes era un area apilada
## por anio; ahora se rehace como grafico de barras apiladas por periodo de
## 5 anios, con el mismo formato que la Figura 8 (region_por_periodo /
## seccion 4), para que ambos graficos de "participacion por periodo" se
## lean de forma consistente.
categoria_por_periodo <- colt %>%
  filter(Visit_Category != "Sin dato") %>%
  count(Periodo5, Visit_Category) %>%
  group_by(Periodo5) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

g4 <- ggplot(categoria_por_periodo, aes(x = factor(Periodo5), y = participacion, fill = Visit_Category)) +
  geom_col(position = "stack", color = "white", linewidth = 0.2) +
  geom_text(aes(label = scales::percent(participacion, accuracy = 1)),
            position = position_stack(vjust = 0.5), size = 3.2, color = "white", family = FUENTE_BASE) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_manual(values = colores_categoria) +
  labs(x = "Periodo (bloques de 5 anios)", y = "Participacion", fill = "Categoria de visita (derivada)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

print(g4)
ggsave(file.path(RUTA_OUTPUTS, "04_categoria_visita_por_anio.png"), g4, width = 10, height = 6.5, dpi = 150)
write.csv(categoria_por_periodo, file.path(RUTA_OUTPUTS, "04_categoria_visita_por_periodo.csv"), row.names = FALSE)

g4b <- ggplot(colt %>% filter(Visit_Category != "Sin dato") %>% count(Year, Visit_Category),
               aes(x = Year, y = n, color = Visit_Category, linetype = Visit_Category)) +
  geom_line(linewidth = 0.9) +
  geom_point(size = 1.2) +
  scale_color_manual(values = colores_categoria) +
  scale_linetype_manual(values = c("Bilateral" = "solid", "Multilateral" = "dashed", "Other" = "dotted")) +
  labs(x = NULL, y = "Cantidad de viajes", color = "Categoria de visita (derivada)",
       linetype = "Categoria de visita (derivada)")

print(g4b)
ggsave(file.path(RUTA_OUTPUTS, "04b_categoria_visita_absoluto.png"), g4b, width = 10, height = 6, dpi = 150)


## ---- 7. Pregunta 6: que destinos prefiere cada mandatario? -------------------

# 7a) Funcion reutilizable: top N destinos de un mandatario especifico.
#     Uso: graficar_top_destinos("Javier Milei")  (usar el nombre CON tilde,
#     tal como aparece en Leader_nombre; para ver los nombres disponibles:
#     sort(unique(colt$Leader_nombre)) )
graficar_top_destinos <- function(nombre_mandatario, top_n = 10, guardar = TRUE) {
  datos <- colt %>%
    filter(Leader_nombre == nombre_mandatario, !is.na(CountryVisited)) %>%
    count(CountryVisited, name = "n_viajes") %>%
    slice_max(n_viajes, n = top_n) %>%
    mutate(CountryVisited = fct_reorder(CountryVisited, n_viajes))

  if (nrow(datos) == 0) {
    warning("No se encontraron viajes para: ", nombre_mandatario,
            " (revisar sort(unique(colt$Leader_nombre)) para el nombre exacto)")
    return(invisible(NULL))
  }

  g <- ggplot(datos, aes(x = CountryVisited, y = n_viajes)) +
    geom_col(fill = gris_6) +
    coord_flip() +
    labs(x = NULL, y = "Cantidad de viajes")

  print(g)
  if (guardar) {
    nombre_archivo <- paste0("05_destinos_", str_replace_all(str_to_lower(quitar_tildes(nombre_mandatario)), "[^a-z0-9]+", "_"), ".png")
    ggsave(file.path(RUTA_OUTPUTS, nombre_archivo), g, width = 8, height = 6, dpi = 150)
  }
  g
}

# Ejemplo de uso (descomentar / cambiar el nombre para cualquier otro presidente):
# graficar_top_destinos("Javier Milei")
# graficar_top_destinos("Luiz Inácio Lula da Silva")

# 7a-bis) Funcion reutilizable para las evoluciones 1994-2025 de una terna de
#         paises puntual (items 7, 8 y 9 del pedido del usuario). Si
#         categoria = NULL usa TODOS los viajes; si se pasa "Bilateral" o
#         "Multilateral" filtra por Visit_Category. complete() rellena con 0
#         los anios sin viajes a ese destino, para que la linea no se corte.
graficar_evolucion_terna <- function(paises, categoria = NULL, archivo, alto = 6) {
  d <- colt %>% filter(CountryVisited %in% paises)
  if (!is.null(categoria)) d <- d %>% filter(Visit_Category == categoria)
  d <- d %>%
    count(Year, CountryVisited, name = "n_viajes") %>%
    complete(Year = ANIO_DESDE:ANIO_HASTA, CountryVisited = paises, fill = list(n_viajes = 0))

  colores_terna <- setNames(c(gris_9, gris_6, gris_3)[seq_along(paises)], paises)
  lineas_terna  <- setNames(c("solid", "dashed", "dotted")[seq_along(paises)], paises)

  g <- ggplot(d, aes(x = Year, y = n_viajes, color = CountryVisited, linetype = CountryVisited)) +
    geom_line(linewidth = 0.8) +
    geom_point(size = 1.3) +
    scale_color_manual(values = colores_terna) +
    scale_linetype_manual(values = lineas_terna) +
    scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
    labs(x = NULL, y = "Cantidad de viajes", color = "Pais destino", linetype = "Pais destino")

  print(g)
  ggsave(file.path(RUTA_OUTPUTS, archivo), g, width = 10, height = alto, dpi = 150)
  g
}

# 7b) Vista agregada: el destino #1 de CADA mandatario, todos juntos.
#     Version 7: en el paper esto ahora es un Cuadro (Pais | Mandatario
#     (periodo) | Destino favorito | Cantidad de viajes) en vez del grafico
#     facetado de 90+ paneles -mas facil de leer con tantos mandatarios.
#     Se deja tambien el grafico (g5/PNG) por si se necesita para otro uso,
#     pero ya no se referencia en el .Rnw.
destino_favorito_por_presidente <- colt %>%
  filter(!is.na(CountryVisited)) %>%
  count(Leader_nombre, Leader_etiqueta, LeaderCountryOrIGO, Pais_ES, CountryVisited, name = "n_viajes") %>%
  group_by(Leader_nombre) %>%
  slice_max(n_viajes, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  arrange(LeaderCountryOrIGO, desc(n_viajes))

g5 <- ggplot(destino_favorito_por_presidente,
             aes(x = fct_reorder(Leader_nombre, n_viajes), y = n_viajes)) +
  geom_col(fill = gris_6) +
  geom_text(aes(label = CountryVisited), hjust = -0.05, size = 2.8, family = FUENTE_BASE, color = "black") +
  facet_wrap(~LeaderCountryOrIGO, scales = "free_y", ncol = 3) +
  coord_flip(clip = "off") +
  scale_y_continuous(expand = expansion(mult = c(0.02, 0.35))) +
  labs(x = NULL, y = "Cantidad de viajes a ese destino")

print(g5)
ggsave(file.path(RUTA_OUTPUTS, "05b_destino_favorito_todos_los_presidentes.png"), g5,
       width = 12, height = ceiling(n_distinct(colt$Leader_key) / 3) * 1.1 + 3, dpi = 150)

# Tabla para el Cuadro del paper -- REHECHA (pedido del usuario, correccion
# Cuadro 4) con 3 cambios de metodologia respecto de la version anterior,
# documentados aca porque el usuario pidio dejar explicitas las decisiones:
#
#  (1) Se separa por MANDATO INDIVIDUAL, no por presidente. Antes CFK
#      apareceria en una sola fila con sus 2 mandatos mezclados; ahora
#      "Cristina Fernandez de Kirchner (2007-2011)" y "... (2011-2015)" son
#      2 filas independientes, para poder ver si el destino favorito se
#      mantuvo o cambio entre un mandato y el siguiente. Usa la tabla
#      mandato_terminos / colt_con_termino (seccion 1.2c-bis / 1.3b).
#
#  (2) El "destino favorito" ahora se calcula SOLO sobre viajes BILATERALES
#      (Visit_Category == "Bilateral"), no sobre el total de viajes. Motivo:
#      un pais puede acumular muchas visitas por ser sede recurrente de
#      cumbres multilaterales (ej. Brasil por el Mercosur) sin que eso
#      refleje una preferencia bilateral real del mandatario -mezclar
#      ambas cosas distorsionaba el resultado.
#
#  (3) Regla de DESEMPATE cuando 2+ paises quedan empatados en el maximo de
#      viajes bilaterales dentro de un mismo mandato (situacion frecuente
#      cuando el mandato tuvo pocos viajes, ej. un pais visitado 1 sola vez
#      y ningun otro pais repetido, o 2-3 paises con 2 o 3 visitas cada
#      uno): se prioriza el pais que ALCANZO ese conteo maximo PRIMERO en
#      el tiempo (fecha del viaje N-esimo mas temprana). Ejemplo: si un
#      mandatario visito a A y B dos veces cada uno, pero la 2da visita a A
#      fue antes que la 2da visita a B, gana A.
destino_favorito_bilateral_viajes <- colt_con_termino %>%
  filter(!is.na(CountryVisited), Visit_Category == "Bilateral") %>%
  arrange(Leader_key, term_n, CountryVisited, TripStartDate) %>%
  group_by(Leader_key, term_n, CountryVisited) %>%
  mutate(n_viajes_acumulado = row_number(), n_viajes_a_destino = n()) %>%
  filter(n_viajes_acumulado == n_viajes_a_destino) %>%  # fila del ultimo (=max) viaje a ese destino
  ungroup() %>%
  select(Leader_key, term_n, Leader_nombre, Leader_etiqueta_termino, LeaderCountryOrIGO, Pais_ES,
         CountryVisited, n_viajes = n_viajes_a_destino, fecha_del_max = TripStartDate)

destino_favorito_termino <- destino_favorito_bilateral_viajes %>%
  group_by(Leader_key, term_n) %>%
  slice_max(n_viajes, n = 1, with_ties = TRUE) %>%   # todos los paises empatados en el maximo
  slice_min(fecha_del_max, n = 1, with_ties = FALSE) %>%  # desempate (3): quien llego antes
  ungroup()

# Chequeo de integridad: un unico ganador por mandato.
chequeo_empates_destino <- destino_favorito_termino %>% count(Leader_key, term_n) %>% filter(n > 1)
if (nrow(chequeo_empates_destino) > 0) {
  warning(nrow(chequeo_empates_destino), " mandatos quedaron con mas de un 'destino favorito' tras el desempate -revisar destino_favorito_bilateral_viajes.")
}

# Orden: por pais alfabeticamente y, dentro de cada pais, por el inicio del
# mandato (cronologico) -mismo criterio pedido para el Cuadro 5.
mandato_inicio_por_termino <- mandato_terminos %>% select(Leader_key, term_n, term_start)

tabla_destino_favorito <- destino_favorito_termino %>%
  left_join(mandato_inicio_por_termino, by = c("Leader_key", "term_n")) %>%
  arrange(Pais_ES, term_start) %>%
  select(Pais = Pais_ES, `Mandatario (mandato)` = Leader_etiqueta_termino,
         `Destino favorito (bilateral)` = CountryVisited, `Cantidad de viajes` = n_viajes)

write.csv(tabla_destino_favorito, file.path(RUTA_OUTPUTS, "05c_destino_favorito_tabla.csv"), row.names = FALSE)

top5_por_presidente <- colt %>%
  filter(!is.na(CountryVisited)) %>%
  count(Leader_nombre, CountryVisited, name = "n_viajes") %>%
  group_by(Leader_nombre) %>%
  slice_max(n_viajes, n = 5, with_ties = FALSE) %>%
  arrange(Leader_nombre, desc(n_viajes)) %>%
  ungroup()

write.csv(top5_por_presidente, file.path(RUTA_OUTPUTS, "05_top5_destinos_por_presidente.csv"), row.names = FALSE)


## ---- 8. Pregunta 7: la primera visita de cada mandatario, a que pais fue? ----

primera_visita <- colt %>%
  filter(!is.na(TripStartDate), !is.na(CountryVisited)) %>%
  group_by(Leader_nombre) %>%
  slice_min(TripStartDate, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  select(Leader_nombre, LeaderCountryOrIGO, TripStartDate, CountryVisited, CityVisited, Visit_Category) %>%
  arrange(TripStartDate)

write.csv(primera_visita, file.path(RUTA_OUTPUTS, "06_primera_visita_por_presidente.csv"), row.names = FALSE)

# Nota metodologica (ver Ostrander & Rider 2018, Tabla 1: "First Foreign
# Visits of Modern Elected Presidents"): ellos encuentran que 7 de 10
# presidentes de EE.UU. eligieron un vecino (Mexico o Canada) como primer
# destino. La misma pregunta aplicada a Sudamerica -mas abajo- permite ver
# si existe un patron parecido de "empezar por la region".
primeros_destinos_frecuencia <- primera_visita %>%
  count(CountryVisited, name = "veces_elegido") %>%
  mutate(CountryVisited = fct_reorder(CountryVisited, veces_elegido))

g6 <- ggplot(primeros_destinos_frecuencia, aes(x = CountryVisited, y = veces_elegido)) +
  geom_col(fill = gris_7) +
  coord_flip() +
  scale_y_continuous(breaks = scales::breaks_pretty()) +
  labs(x = NULL, y = "Cantidad de mandatarios")

print(g6)
ggsave(file.path(RUTA_OUTPUTS, "06_primeros_destinos_frecuencia.png"), g6, width = 9, height = 7, dpi = 150)

# 8b) REHECHO (pedido del usuario, correccion Figura 17): antes mostraba la
#     evolucion de TODOS los viajes (cualquier categoria) a Estados Unidos,
#     Brasil y Argentina -sin relacion directa con "primer destino" mas
#     alla del titulo-. Ahora queda realmente conectado con la Figura 16
#     (primeros_destinos_frecuencia, arriba): en vez de contar todos los
#     viajes, cuenta EN QUE ANIO cada mandatario eligio a cada uno de estos
#     3 paises como su PRIMER destino (usa primera_visita, una fila por
#     mandatario). complete() rellena con 0 los anios sin ningun mandatario
#     que haya debutado en ese pais, para que la escala temporal quede
#     completa 1994-2025.
primeros_destinos_por_anio <- primera_visita %>%
  mutate(Year = year(TripStartDate)) %>%
  filter(CountryVisited %in% c("United States", "Brazil", "Argentina")) %>%
  count(Year, CountryVisited, name = "n_mandatarios") %>%
  complete(Year = ANIO_DESDE:ANIO_HASTA, CountryVisited = c("United States", "Brazil", "Argentina"),
           fill = list(n_mandatarios = 0))

colores_terna_primer_destino <- c("United States" = gris_9, "Brazil" = gris_6, "Argentina" = gris_3)
lineas_terna_primer_destino  <- c("United States" = "solid", "Brazil" = "dashed", "Argentina" = "dotted")

g6b <- ggplot(primeros_destinos_por_anio,
              aes(x = Year, y = n_mandatarios, color = CountryVisited, linetype = CountryVisited)) +
  geom_line(linewidth = 0.8) +
  geom_point(size = 1.6) +
  scale_color_manual(values = colores_terna_primer_destino) +
  scale_linetype_manual(values = lineas_terna_primer_destino) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  scale_y_continuous(breaks = scales::breaks_pretty()) +
  labs(x = NULL, y = "Cantidad de mandatarios que eligieron este pais como PRIMER destino",
       color = "Pais destino", linetype = "Pais destino")

print(g6b)
ggsave(file.path(RUTA_OUTPUTS, "06b_evolucion_top3_primeros_destinos.png"), g6b, width = 10, height = 6, dpi = 150)
write.csv(primeros_destinos_por_anio, file.path(RUTA_OUTPUTS, "06b_evolucion_top3_primeros_destinos.csv"), row.names = FALSE)


## ---- 9. Extensiones inspiradas en la bibliografia del proyecto ---------------
## Ver /Bib: Ostrander & Rider (2018) "Presidents Abroad" y Moyer et al.
## (2025) "When HOGS Fly" (el propio paper de introduccion del dataset COLT).

# 9.1 Estacionalidad: en que meses se concentran los viajes.
#     Idea tomada de Ostrander & Rider (2018), quienes reportan los meses
#     mas/menos frecuentes de salida (junio, noviembre, julio/diciembre en
#     su caso EE.UU.) y lo interpretan en relacion al calendario legislativo.
viajes_por_mes <- colt %>%
  filter(!is.na(Mes)) %>%
  count(Mes)

g8 <- ggplot(viajes_por_mes, aes(x = Mes, y = n)) +
  geom_col(fill = gris_6) +
  labs(x = NULL, y = "Cantidad de viajes")

print(g8)
ggsave(file.path(RUTA_OUTPUTS, "08_estacionalidad_mensual.png"), g8, width = 9, height = 6, dpi = 150)

# 9.2 Ranking de los paises destino mas visitados, separado en bilaterales
#     y multilaterales (para no mezclar "con quien se reunen" con "a que
#     cumbres van"). Idea tomada de Moyer et al. (2025) "When HOGS Fly",
#     Figura 2 (paises ranqueados de mayor a menor por visitas recibidas) y
#     Tabla 5 de Ostrander & Rider (2018) ("Top 10 Presidential Destinations").
top20_bilateral <- colt %>%
  filter(Visit_Category == "Bilateral") %>%
  count(CountryVisited, name = "n_viajes") %>%
  slice_max(n_viajes, n = 20) %>%
  mutate(CountryVisited = fct_reorder(CountryVisited, n_viajes))

g9a <- ggplot(top20_bilateral, aes(x = CountryVisited, y = n_viajes)) +
  geom_col(fill = gris_9) +
  coord_flip() +
  labs(x = NULL, y = "Cantidad de viajes bilaterales")

print(g9a)
ggsave(file.path(RUTA_OUTPUTS, "09a_ranking_destinos_bilaterales.png"), g9a, width = 9, height = 8, dpi = 150)

# 9.2b) Evolucion 1994-2025 de viajes BILATERALES a Brasil y Estados Unidos
#       (corregido: antes era Brasil/Argentina/Cuba; pedido del usuario,
#       correccion Figura 20 -"que sea solo una comparacion entre Brasil y
#       Estados Unidos"-).
g9a2 <- graficar_evolucion_terna(
  paises = c("Brazil", "United States"),
  categoria = "Bilateral",
  archivo = "09a2_evolucion_bilateral_brasil_eeuu.png"
)

top20_multilateral <- colt %>%
  filter(Visit_Category == "Multilateral") %>%
  count(CountryVisited, name = "n_viajes") %>%
  slice_max(n_viajes, n = 20) %>%
  mutate(CountryVisited = fct_reorder(CountryVisited, n_viajes))

g9b <- ggplot(top20_multilateral, aes(x = CountryVisited, y = n_viajes)) +
  geom_col(fill = gris_5) +
  coord_flip() +
  labs(x = NULL, y = "Cantidad de viajes multilaterales")

print(g9b)
ggsave(file.path(RUTA_OUTPUTS, "09b_ranking_destinos_multilaterales.png"), g9b, width = 9, height = 8, dpi = 150)

# 9.2c) Evolucion 1994-2025 de viajes MULTILATERALES a Estados Unidos, Brasil
#       y Argentina (item 9 del pedido, terna elegida por el usuario junto a
#       la Figura 16).
g9b2 <- graficar_evolucion_terna(
  paises = c("United States", "Brazil", "Argentina"),
  categoria = "Multilateral",
  archivo = "09b2_evolucion_multilateral_usa_bra_arg.png"
)


## ---- 9.3 y 9.4: extensiones nuevas (bibliografia ampliada, 2026-08-27) --------

# 9.3 Cantidad de foros/cumbres multilaterales DISTINTOS por periodo. Idea
#     tomada de Peña (2005), que reflexiona sobre la "compleja red" de
#     espacios de cumbre presidencial en Sudamerica (Mercosur, Grupo de Rio,
#     Cumbres Iberoamericanas, y despues UNASUR/CELAC). No es lo mismo que
#     el grafico 09b (que cuenta VIAJES a destinos multilaterales): esto
#     cuenta cuantos EVENTOS/FOROS distintos (NameMultilatEvent) aparecen
#     activos en cada periodo, como proxy de que tan "compleja" es la red
#     de cumbres en cada momento -y permite ver el quiebre que documentan
#     Nolte (2021) y Barros & Gonçalves (2021) tras el fin de la "epoca
#     dorada" de las cumbres (~2012-2017).
foros_por_periodo <- colt %>%
  filter(!is.na(NameMultilatEvent), NameMultilatEvent != "") %>%
  distinct(Periodo5, NameMultilatEvent) %>%
  count(Periodo5, name = "n_foros_distintos")

g9c <- ggplot(foros_por_periodo, aes(x = factor(Periodo5), y = n_foros_distintos)) +
  geom_col(fill = gris_6) +
  geom_text(aes(label = n_foros_distintos), vjust = -0.4, size = 3, family = FUENTE_BASE, color = "black") +
  labs(x = "Periodo (bloques de 5 años)", y = "Cantidad de foros distintos")

print(g9c)
ggsave(file.path(RUTA_OUTPUTS, "09c_foros_distintos_por_periodo.png"), g9c, width = 9, height = 6, dpi = 150)
write.csv(foros_por_periodo, file.path(RUTA_OUTPUTS, "09c_foros_distintos_por_periodo.csv"), row.names = FALSE)

# 9.4 Composicion Bilateral/Multilateral/Otro POR PAIS (no por año). Idea
#     tomada de Lee & Kim (2024), quienes proponen tratar las visitas
#     diplomaticas como datos composicionales -participaciones relativas de
#     un recurso politico escaso, que suman 100%- en vez de conteos
#     independientes. Aca se aplica esa misma logica para comparar, entre
#     los 12 paises, que porcentaje de sus viajes es bilateral vs.
#     multilateral vs. otro (en vez de mirar la evolucion en el tiempo,
#     como ya hace el grafico 04).
composicion_por_pais <- colt %>%
  count(Pais_ES, Visit_Category) %>%
  group_by(Pais_ES) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

orden_paises_bilateral <- composicion_por_pais %>%
  filter(Visit_Category == "Bilateral") %>%
  arrange(desc(participacion)) %>%
  pull(Pais_ES)

# Color de texto de las etiquetas de dato (pedido del usuario, correccion
# Figura 24): blanco sobre los segmentos oscuros (Bilateral/Multilateral),
# negro sobre "Other" -que usa un gris claro (gris_2) y quedaria ilegible
# en blanco-.
color_texto_categoria <- c("Bilateral" = "white", "Multilateral" = "white", "Other" = "black")

g9d <- ggplot(composicion_por_pais,
              aes(x = factor(Pais_ES, levels = rev(orden_paises_bilateral)),
                  y = participacion, fill = Visit_Category)) +
  geom_col(position = "stack", color = "white", linewidth = 0.3) +
  geom_text(aes(label = scales::percent(participacion, accuracy = 1), color = Visit_Category),
            position = position_stack(vjust = 0.5), size = 2.6, family = FUENTE_BASE, show.legend = FALSE) +
  coord_flip() +
  scale_y_continuous(labels = scales::percent_format()) +
  # guide_legend(reverse = TRUE): con coord_flip() + barras apiladas, el
  # orden por defecto de la leyenda queda invertido respecto del orden
  # visual del stack (de izquierda a derecha). Esto lo corrige (item 10).
  scale_fill_manual(values = colores_categoria, guide = guide_legend(reverse = TRUE)) +
  scale_color_manual(values = color_texto_categoria) +
  labs(x = NULL, y = "Participacion", fill = "Categoria de visita (derivada)")

print(g9d)
ggsave(file.path(RUTA_OUTPUTS, "09d_composicion_bilateral_multilateral_por_pais.png"), g9d, width = 10, height = 6.5, dpi = 150)
write.csv(composicion_por_pais, file.path(RUTA_OUTPUTS, "09d_composicion_bilateral_multilateral_por_pais.csv"), row.names = FALSE)


## ---- 11. Extension: viajes por "año de mandato" (normalizado) ----------------
## Idea: en vez de mirar el año calendario, mirar el año N del mandato de cada
## presidente (año 1, año 2, ...). Esto permite comparar presidentes entre si
## sin que alguien con un mandato mas corto parezca "viajar menos" solo por
## haber estado menos tiempo en el cargo -el sesgo que se discutio con el
## usuario antes de aplicar la regla de fechas de mandato-. Tambien permite
## ver si existe un patron sistematico de "luna de miel" (mas viajes el
## primer año) o "pato rengo" (menos viajes el ultimo), algo que Ostrander &
## Rider (2018) documentan para el caso de EE.UU.
##
## Para que el promedio no este sesgado por los años tardios (donde solo
## sobreviven mandatos largos, ej. 6 años en Argentina/Bolivia vs 4 en
## Uruguay/Chile), se calcula una "exposicion": cuantos mandatos (persona-
## periodo) llegaron a ese año N dentro de la ventana de datos 1994-2025.
## Los presidentes en ejercicio (mandato termina en 2099 en la tabla de
## apoyo, marcador de "sigue en el cargo") se cortan en ANIO_HASTA -todavia
## no tenemos sus viajes futuros-.
if (!is.null(mandatos) && "Anio_mandato" %in% names(colt)) {
  fecha_corte <- as.Date(paste0(ANIO_HASTA, "-12-31"))

  exposicion_mandato <- mandatos_fechas %>%
    mutate(
      fin_1_efectivo = pmin(MandateEnd_1, fecha_corte),
      anios_1 = pmax(0, floor(as.numeric(fin_1_efectivo - MandateStart_1) / 365.25) + 1),
      fin_2_efectivo = pmin(MandateEnd_2, fecha_corte),
      anios_2 = if_else(!is.na(MandateStart_2),
                         pmax(0, floor(as.numeric(fin_2_efectivo - MandateStart_2) / 365.25) + 1),
                         NA_real_)
    ) %>%
    select(Leader_key, anios_1, anios_2) %>%
    pivot_longer(cols = c(anios_1, anios_2), values_to = "anios_periodo") %>%
    filter(!is.na(anios_periodo), anios_periodo > 0) %>%
    select(Leader_key, anios_periodo)

  # Expande cada mandato a las filas 1..anios_periodo ("expuesto" ese año)
  exposicion_expandida <- exposicion_mandato %>%
    rowwise() %>%
    mutate(Anio_mandato = list(seq_len(anios_periodo))) %>%
    ungroup() %>%
    unnest(Anio_mandato) %>%
    count(Anio_mandato, name = "n_mandatos_expuestos")

  viajes_por_anio_mandato <- colt %>%
    filter(!is.na(Anio_mandato)) %>%
    count(Anio_mandato, name = "n_viajes_total") %>%
    left_join(exposicion_expandida, by = "Anio_mandato") %>%
    mutate(promedio_viajes = n_viajes_total / n_mandatos_expuestos) %>%
    # Se corta donde quedan pocos mandatos expuestos (< 5): un promedio con
    # 1 o 2 casos no es representativo y puede ser enganoso en el grafico.
    filter(n_mandatos_expuestos >= 5) %>%
    arrange(Anio_mandato)

  g11 <- ggplot(viajes_por_anio_mandato, aes(x = Anio_mandato, y = promedio_viajes)) +
    geom_col(fill = gris_6) +
    geom_text(aes(label = n_mandatos_expuestos), vjust = -0.4, size = 2.6, family = FUENTE_BASE, color = gris_5) +
    scale_x_continuous(breaks = scales::breaks_width(1)) +
    labs(x = "Año de mandato", y = "Promedio de viajes por presidente\n(etiqueta = cantidad de mandatos con datos ese año)")

  print(g11)
  ggsave(file.path(RUTA_OUTPUTS, "11_viajes_por_anio_de_mandato.png"), g11, width = 9, height = 6, dpi = 150)
  write.csv(viajes_por_anio_mandato, file.path(RUTA_OUTPUTS, "11_viajes_por_anio_de_mandato.csv"), row.names = FALSE)
} else {
  warning("No se pudo construir 'viajes por año de mandato' -falta mandatos_presidenciales.csv o Anio_mandato.")
}


## ---- 12. Extension: tipo de actividad de los viajes (Charnock, McCann & Tenpas 2009) --
## Cinco campos booleanos de COLT que hasta ahora no se habian usado en ningun
## grafico: si el viaje incluyo un discurso publico, la firma de un acuerdo,
## un sitio cultural/ceremonia, un foro de negocios, o una reunion con el
## lider de un organismo internacional. Parecido a como Charnock, McCann &
## Tenpas (2009) clasifican los viajes presidenciales de EE.UU. desde
## Eisenhower. Un viaje puede tener mas de una actividad a la vez (no son
## categorias excluyentes), por eso se muestra como "% de los viajes que
## incluyeron cada actividad" y no como participacion que suma 100%. El
## promedio se calcula solo sobre los viajes con dato (na.rm = TRUE) para no
## castigar la cifra por los campos que vienen vacios.
actividades <- c(
  "PublicAddress" = "Discurso publico",
  "SignedAgreement" = "Acuerdo firmado",
  "CulturalSiteOrCeremony" = "Sitio cultural / ceremonia",
  "BusinessLeaderOrForum" = "Foro de negocios",
  "MetIGOLeader" = "Reunion con lider de organismo internacional"
)

tipo_actividad <- colt %>%
  summarise(across(all_of(names(actividades)), ~ mean(. == "Yes", na.rm = TRUE))) %>%
  pivot_longer(everything(), names_to = "campo", values_to = "participacion") %>%
  mutate(Actividad = recode(campo, !!!actividades)) %>%
  select(Actividad, participacion)

g12 <- ggplot(tipo_actividad, aes(x = fct_reorder(Actividad, participacion), y = participacion)) +
  geom_col(fill = gris_6) +
  geom_text(aes(label = scales::percent(participacion, accuracy = 1)),
            hjust = -0.15, size = 3, family = FUENTE_BASE, color = "black") +
  coord_flip(clip = "off") +
  scale_y_continuous(labels = scales::percent_format(), expand = expansion(mult = c(0, 0.15))) +
  labs(x = NULL, y = "% de los viajes que incluyeron esta actividad")

print(g12)
ggsave(file.path(RUTA_OUTPUTS, "12_tipo_actividad_viajes.png"), g12, width = 9, height = 4.5, dpi = 150)
write.csv(tipo_actividad, file.path(RUTA_OUTPUTS, "12_tipo_actividad_viajes.csv"), row.names = FALSE)

## 12b. Version separada por categoria de visita (pedido del usuario,
##      correccion Figura 2): en vez de un solo grafico con todos los viajes
##      mezclados, tres graficos identicos en formato -uno para viajes
##      Bilaterales, uno para Multilaterales y uno para "Otro"- para poder
##      comparar que actividades predominan segun el motivo del viaje (ej.
##      es esperable que "Acuerdo firmado" y "Reunion con lider de organismo
##      internacional" sean mucho mas frecuentes en Multilaterales que en
##      Bilaterales). Se excluye la categoria "Sin dato" (ver seccion 6 y
##      correccion Figura 13: MetHostHoGS vacio, sin informacion suficiente
##      para clasificar el viaje).
tipo_actividad_por_categoria <- function(categoria) {
  colt %>%
    filter(Visit_Category == categoria) %>%
    summarise(across(all_of(names(actividades)), ~ mean(. == "Yes", na.rm = TRUE))) %>%
    pivot_longer(everything(), names_to = "campo", values_to = "participacion") %>%
    mutate(Actividad = recode(campo, !!!actividades)) %>%
    select(Actividad, participacion)
}

graficar_tipo_actividad <- function(datos, subtitulo_archivo) {
  ggplot(datos, aes(x = fct_reorder(Actividad, participacion), y = participacion)) +
    geom_col(fill = gris_6) +
    geom_text(aes(label = scales::percent(participacion, accuracy = 1)),
              hjust = -0.15, size = 3, family = FUENTE_BASE, color = "black") +
    coord_flip(clip = "off") +
    scale_y_continuous(labels = scales::percent_format(), expand = expansion(mult = c(0, 0.15))) +
    labs(x = NULL, y = "% de los viajes que incluyeron esta actividad")
}

tipo_actividad_bilateral <- tipo_actividad_por_categoria("Bilateral")
g12a <- graficar_tipo_actividad(tipo_actividad_bilateral)
print(g12a)
ggsave(file.path(RUTA_OUTPUTS, "12a_tipo_actividad_bilateral.png"), g12a, width = 9, height = 4.5, dpi = 150)
write.csv(tipo_actividad_bilateral, file.path(RUTA_OUTPUTS, "12a_tipo_actividad_bilateral.csv"), row.names = FALSE)

tipo_actividad_multilateral <- tipo_actividad_por_categoria("Multilateral")
g12b <- graficar_tipo_actividad(tipo_actividad_multilateral)
print(g12b)
ggsave(file.path(RUTA_OUTPUTS, "12b_tipo_actividad_multilateral.png"), g12b, width = 9, height = 4.5, dpi = 150)
write.csv(tipo_actividad_multilateral, file.path(RUTA_OUTPUTS, "12b_tipo_actividad_multilateral.csv"), row.names = FALSE)

tipo_actividad_otro <- tipo_actividad_por_categoria("Other")
g12c <- graficar_tipo_actividad(tipo_actividad_otro)
print(g12c)
ggsave(file.path(RUTA_OUTPUTS, "12c_tipo_actividad_otro.png"), g12c, width = 9, height = 4.5, dpi = 150)
write.csv(tipo_actividad_otro, file.path(RUTA_OUTPUTS, "12c_tipo_actividad_otro.csv"), row.names = FALSE)


## ---- 13. Extension: auge y caida del multilateralismo (Nolte 2021; Barros & Gonçalves 2021) --
## Toma la participacion de viajes MULTILATERALES por año (subconjunto de
## categoria_por_anio, seccion 6) y le agrega lineas de referencia en 2 hitos
## institucionales para visualizar de un vistazo el quiebre que documenta
## esta literatura: la fundacion de UNASUR (2008, "epoca dorada" del
## regionalismo sudamericano) y su crisis/vaciamiento posterior (desde 2018,
## varios paises suspenden o abandonan el bloque).
multilateral_por_anio <- categoria_por_anio %>% filter(Visit_Category == "Multilateral")

## Hitos de multilateralismo regional (pedido del usuario, correccion
## Figura 14: sumar mas hitos, consultando la bibliografia del proyecto -
## Nolte 2021 y Barros & Gonçalves 2021, ya citados en esta seccion, mas
## hechos institucionales de dominio publico). Se agregan 3 hitos nuevos a
## los 2 que ya estaban (fundacion y crisis de UNASUR): la Comunidad
## Sudamericana de Naciones/ALBA (2004, los antecedentes institucionales
## inmediatos de UNASUR), la fundacion de la CELAC (2011, el organismo
## regional mas amplio -incluye a Mexico, Centroamerica y el Caribe- que
## compite/convive con UNASUR), y la fundacion de PROSUR (2019, la
## iniciativa que un grupo de gobiernos de derecha impulsa como reemplazo
## de UNASUR tras su vaciamiento). La columna "nivel" solo se usa para
## escalonar la altura de las etiquetas de texto y que no se superpongan
## entre si (2018 y 2019 quedan a un anio de distancia).
hitos_multilateralismo <- tribble(
  ~anio, ~etiqueta, ~nivel,
  2004, "Comunidad Sudamericana de Naciones / ALBA (2004)", "A",
  2008, "Fundacion UNASUR (2008)", "B",
  2011, "Fundacion CELAC (2011)", "A",
  2018, "Crisis/vaciamiento UNASUR (desde 2018)", "B",
  2019, "Fundacion PROSUR (2019)", "A"
)
vjust_hitos <- c("A" = -0.6, "B" = -3.4)

g13 <- ggplot(multilateral_por_anio, aes(x = Year, y = participacion)) +
  geom_line(color = gris_9, linewidth = 0.9) +
  geom_point(color = gris_9, size = 1.4) +
  geom_vline(data = hitos_multilateralismo, aes(xintercept = anio),
             linetype = "dashed", color = gris_5, linewidth = 0.4, inherit.aes = FALSE) +
  geom_text(data = hitos_multilateralismo,
            aes(x = anio, y = Inf, label = etiqueta, vjust = vjust_hitos[nivel]),
            angle = 90, hjust = 1.05, size = 2.6, family = FUENTE_BASE, color = gris_7,
            inherit.aes = FALSE) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  labs(x = NULL, y = "Participacion de viajes multilaterales")

print(g13)
ggsave(file.path(RUTA_OUTPUTS, "13_auge_caida_multilateralismo.png"), g13, width = 10, height = 6.5, dpi = 150)


## ---- 14. Extension: sesgo hacia el vecino inmediato (Ostrander & Rider 2018) --
## Ostrander & Rider (2018) encuentran que 7 de 10 presidentes de EE.UU.
## eligieron un vecino (Mexico o Canada) como PRIMER destino (ya replicado en
## la seccion 8/Figura 14 para Sudamerica). Aca se extiende la pregunta a
## TODOS los viajes del mandato, no solo el primero: que porcentaje de los
## viajes de cada pais se queda en el vecindario inmediato (un pais con
## frontera terrestre) vs. va a un destino lejano. Las fronteras se
## codificaron a mano (fuente: geografia politica estandar, fronteras
## terrestres reconocidas; no incluye territorios no soberanos como Guayana
## Francesa).
vecinos_terrestres <- list(
  "Argentina" = c("Bolivia","Brazil","Chile","Paraguay","Uruguay"),
  "Bolivia"   = c("Argentina","Brazil","Chile","Paraguay","Peru"),
  "Brazil"    = c("Argentina","Bolivia","Colombia","Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela"),
  "Chile"     = c("Argentina","Bolivia","Peru"),
  "Colombia"  = c("Brazil","Ecuador","Panama","Peru","Venezuela"),
  "Ecuador"   = c("Colombia","Peru"),
  "Guyana"    = c("Brazil","Suriname","Venezuela"),
  "Paraguay"  = c("Argentina","Bolivia","Brazil"),
  "Peru"      = c("Bolivia","Brazil","Chile","Colombia","Ecuador"),
  "Suriname"  = c("Brazil","Guyana"),
  "Uruguay"   = c("Argentina","Brazil"),
  "Venezuela" = c("Brazil","Colombia","Guyana")
)

es_vecino_terrestre <- function(pais_origen, pais_destino) {
  mapply(function(o, d) !is.na(d) && d %in% vecinos_terrestres[[o]], pais_origen, pais_destino)
}

vecino_inmediato_por_pais <- colt %>%
  filter(!is.na(CountryVisited), LeaderCountryOrIGO %in% names(vecinos_terrestres)) %>%
  mutate(es_vecino = es_vecino_terrestre(LeaderCountryOrIGO, CountryVisited)) %>%
  group_by(Pais_ES) %>%
  summarise(participacion_vecino = mean(es_vecino), n_viajes = n(), .groups = "drop")

promedio_general_vecino <- weighted.mean(vecino_inmediato_por_pais$participacion_vecino,
                                          vecino_inmediato_por_pais$n_viajes)
cat("\n--- Sesgo hacia el vecino inmediato (Ostrander & Rider 2018), TODOS los viajes ---\n")
cat("Promedio general (los 12 paises juntos):", scales::percent(promedio_general_vecino, accuracy = 0.1), "\n")
print(vecino_inmediato_por_pais %>% arrange(desc(participacion_vecino)))

g14 <- ggplot(vecino_inmediato_por_pais, aes(x = fct_reorder(Pais_ES, participacion_vecino), y = participacion_vecino)) +
  geom_col(fill = gris_6) +
  geom_hline(yintercept = promedio_general_vecino, linetype = "dashed", color = gris_9, linewidth = 0.4) +
  geom_text(aes(label = scales::percent(participacion_vecino, accuracy = 1)),
            hjust = -0.15, size = 3, family = FUENTE_BASE, color = "black") +
  coord_flip(clip = "off") +
  scale_y_continuous(labels = scales::percent_format(), expand = expansion(mult = c(0, 0.15))) +
  labs(x = NULL, y = "% de todos los viajes a un pais con frontera terrestre\n(linea punteada = promedio de los 12 paises)")

print(g14)
ggsave(file.path(RUTA_OUTPUTS, "14_sesgo_vecino_inmediato.png"), g14, width = 9, height = 6, dpi = 150)
write.csv(vecino_inmediato_por_pais, file.path(RUTA_OUTPUTS, "14_sesgo_vecino_inmediato.csv"), row.names = FALSE)

## ---- 14b. Extension (pedido del usuario): vecino fronterizo vs. no-vecino, --
##      a lo LARGO DE TODA LA SERIE (no un solo valor agregado como en la
##      Figura 18/g14 de arriba). Se apoya en la misma diada Origen-Destino
##      que se exporto como referencia a 04_BASE_FINAL/Base_Diadas_Vecinos.xlsx
##      (Origen = los 12 paises de la base de viajes, Destino = los paises
##      efectivamente visitados; Es_Vecino_Fronterizo segun la misma lista
##      vecinos_terrestres de arriba). Aca se calcula, para cada anio, que
##      porcentaje de los viajes fue a un vecino fronterizo -para ver si ese
##      sesgo crecio, se mantuvo o cayo con el correr del tiempo, en vez de
##      un solo numero para todo 1994-2025.
vecino_por_anio <- colt %>%
  filter(!is.na(CountryVisited), LeaderCountryOrIGO %in% names(vecinos_terrestres)) %>%
  mutate(es_vecino = es_vecino_terrestre(LeaderCountryOrIGO, CountryVisited)) %>%
  count(Year, es_vecino) %>%
  group_by(Year) %>%
  mutate(participacion = n / sum(n), n_total_anio = sum(n)) %>%
  ungroup() %>%
  filter(es_vecino) %>%
  select(Year, n_viajes_vecino = n, n_total_anio, participacion_vecino = participacion)

# Correlacion simple entre el anio (tiempo) y la participacion de viajes a
# un vecino fronterizo -para el Cuadro Nuevo que pidio el usuario despues
# de la Figura 18-.
correlacion_vecino_tiempo <- cor.test(vecino_por_anio$Year, vecino_por_anio$participacion_vecino,
                                       method = "pearson")
tabla_correlacion_vecino <- tibble(
  Variable = "Anio (tiempo) vs. % de viajes a un vecino fronterizo",
  r = round(unname(correlacion_vecino_tiempo$estimate), 3),
  `p-valor` = signif(correlacion_vecino_tiempo$p.value, 3),
  n_anios = nrow(vecino_por_anio)
)
write.csv(tabla_correlacion_vecino, file.path(RUTA_OUTPUTS, "14b_correlacion_vecino_tiempo.csv"), row.names = FALSE)

g14b <- ggplot(vecino_por_anio, aes(x = Year, y = participacion_vecino)) +
  geom_line(color = gris_9, linewidth = 0.9) +
  geom_point(color = gris_9, size = 1.4) +
  geom_smooth(method = "lm", se = FALSE, color = gris_5, linetype = "dashed", linewidth = 0.6) +
  geom_hline(yintercept = promedio_general_vecino, linetype = "dotted", color = gris_5, linewidth = 0.4) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  labs(x = NULL, y = "% de los viajes del anio a un pais con frontera terrestre\n(linea de tendencia lineal; linea punteada fina = promedio 1994-2025)")

print(g14b)
ggsave(file.path(RUTA_OUTPUTS, "14b_vecino_fronterizo_a_lo_largo_del_tiempo.png"), g14b, width = 10, height = 6.5, dpi = 150)
write.csv(vecino_por_anio, file.path(RUTA_OUTPUTS, "14b_vecino_fronterizo_a_lo_largo_del_tiempo.csv"), row.names = FALSE)


## ---- 15. Extension: evolucion temporal por bloque de destino -----------------
## Pedido del usuario: 6 series de "cantidad total de viajes por año" a cada
## bloque de destino. Sudamerica y Latinoamerica se dejan A PROPOSITO
## superpuestas (Sudamerica es un subconjunto de Latinoamerica) porque son
## dos preguntas distintas ("cuanto se viaja dentro de la región mas cercana"
## vs. "cuanto se viaja dentro de America Latina en general, incluyendo
## Centroamerica/Caribe/Mexico") -no es un error, es intencional. Estados
## Unidos se cuenta aparte de "Norteamerica" porque el usuario pidio el pais
## especificamente, no toda la subregion (que tambien incluiria Canada).
bloques_destino <- list(
  "Sudamerica"    = quote(RegionVisited == "Latin America and the Caribbean" & SubRegionVisited == "South America"),
  "Latinoamerica" = quote(RegionVisited == "Latin America and the Caribbean"),
  "Estados Unidos" = quote(CountryVisited == "United States"),
  "Europa"        = quote(RegionVisited == "Europe"),
  "Africa"        = quote(RegionVisited == "Africa"),
  "Asia"          = quote(RegionVisited == "Asia")
)

viajes_por_bloque_anio <- bind_rows(lapply(names(bloques_destino), function(nombre) {
  colt %>%
    filter(!!bloques_destino[[nombre]]) %>%
    count(Year, name = "n_viajes") %>%
    mutate(Bloque = nombre)
})) %>%
  complete(Year = ANIO_DESDE:ANIO_HASTA, Bloque = names(bloques_destino), fill = list(n_viajes = 0)) %>%
  mutate(Bloque = factor(Bloque, levels = names(bloques_destino)))

# Promedio anual de cada bloque (linea de referencia punteada), calculado
# sobre la misma serie ya completada con ceros (ANIO_DESDE:ANIO_HASTA) para
# que el promedio sea comparable entre bloques con distinta cantidad de años
# con actividad.
promedio_anual_por_bloque <- viajes_por_bloque_anio %>%
  group_by(Bloque) %>%
  summarise(promedio = mean(n_viajes, na.rm = TRUE), .groups = "drop")

g15 <- ggplot(viajes_por_bloque_anio, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_6) +
  geom_hline(data = promedio_anual_por_bloque, aes(yintercept = promedio),
             linetype = "dashed", color = gris_9, linewidth = 0.5) +
  facet_wrap(~Bloque, ncol = 2, scales = "free_y") +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 6)) +
  labs(x = NULL, y = "Cantidad total de viajes")

print(g15)
ggsave(file.path(RUTA_OUTPUTS, "15_evolucion_por_bloque_destino.png"), g15, width = 11, height = 9, dpi = 150)
write.csv(viajes_por_bloque_anio, file.path(RUTA_OUTPUTS, "15_evolucion_por_bloque_destino.csv"), row.names = FALSE)


## ---- 16. Extension: "perfil" de destinos por presidente (todo el periodo) ----
## A diferencia de la seccion 15 (bloques que se superponen a proposito), aca
## se necesitan categorias MUTUAMENTE EXCLUYENTES para que el perfil de cada
## presidente sea una composicion que sume 100% -misma logica que
## composicion_por_pais (seccion 9.4, Lee & Kim 2024) pero a nivel mandatario
## y con estos 8 bloques de region en vez de Bilateral/Multilateral/Otro.
colt <- colt %>%
  mutate(
    Region_perfil = case_when(
      RegionVisited == "Latin America and the Caribbean" & SubRegionVisited == "South America" ~ "Sudamerica",
      RegionVisited == "Latin America and the Caribbean" ~ "Resto Latam y Caribe",
      CountryVisited == "United States" ~ "Estados Unidos",
      RegionVisited == "Northern America" ~ "Resto Norteamerica",
      RegionVisited == "Europe" ~ "Europa",
      RegionVisited == "Asia" ~ "Asia",
      RegionVisited == "Africa" ~ "Africa",
      TRUE ~ "Otras (Oceania, etc.)"
    )
  )

orden_regiones_perfil <- c("Sudamerica", "Resto Latam y Caribe", "Estados Unidos",
                            "Resto Norteamerica", "Europa", "Asia", "Africa", "Otras (Oceania, etc.)")

# REHECHO (pedido del usuario, correccion Cuadro 5): igual que el Cuadro 4,
# ahora separa por MANDATO INDIVIDUAL (colt_con_termino) en vez de por
# presidente completo. Region_perfil se recalcula sobre colt_con_termino
# porque esa tabla se armo (seccion 1.3b) antes de que "colt" tuviera esta
# columna.
colt_con_termino <- colt_con_termino %>%
  mutate(
    Region_perfil = case_when(
      RegionVisited == "Latin America and the Caribbean" & SubRegionVisited == "South America" ~ "Sudamerica",
      RegionVisited == "Latin America and the Caribbean" ~ "Resto Latam y Caribe",
      CountryVisited == "United States" ~ "Estados Unidos",
      RegionVisited == "Northern America" ~ "Resto Norteamerica",
      RegionVisited == "Europe" ~ "Europa",
      RegionVisited == "Asia" ~ "Asia",
      RegionVisited == "Africa" ~ "Africa",
      TRUE ~ "Otras (Oceania, etc.)"
    )
  )

perfil_regional_por_mandato <- colt_con_termino %>%
  filter(!is.na(Region_perfil)) %>%
  count(Leader_key, term_n, Leader_etiqueta_termino, Pais_ES, Region_perfil, name = "n") %>%
  group_by(Leader_key, term_n) %>%
  mutate(participacion = n / sum(n), total_viajes = sum(n)) %>%
  ungroup() %>%
  mutate(Region_perfil = factor(Region_perfil, levels = orden_regiones_perfil)) %>%
  complete(nesting(Leader_key, term_n, Leader_etiqueta_termino, Pais_ES), Region_perfil,
           fill = list(n = 0, participacion = 0)) %>%
  group_by(Leader_key, term_n) %>%
  fill(total_viajes, .direction = "downup") %>%
  ungroup()

# Version ancha para el Cuadro del paper: una fila por MANDATO, una columna
# por bloque de region (porcentaje). Orden pedido por el usuario: pais en
# orden alfabetico y, DENTRO de cada pais, los mandatos en orden
# cronologico (ej. Argentina: Menem 1 y 2, De la Rua, Duhalde, Nestor
# Kirchner, CFK 1 y 2, Macri, Alberto Fernandez, Milei -no alfabetico por
# nombre de mandatario-). Reutiliza mandato_inicio_por_termino (seccion 7 /
# Cuadro 4) para la fecha de inicio de cada mandato.
tabla_perfil_regional <- perfil_regional_por_mandato %>%
  mutate(valor = scales::percent(participacion, accuracy = 1)) %>%
  select(Pais_ES, Leader_etiqueta_termino, Region_perfil, valor, total_viajes, Leader_key, term_n) %>%
  pivot_wider(names_from = Region_perfil, values_from = valor) %>%
  left_join(mandato_inicio_por_termino, by = c("Leader_key", "term_n")) %>%
  arrange(Pais_ES, term_start) %>%
  select(-Leader_key, -term_n, -term_start) %>%
  rename(Pais = Pais_ES, `Mandatario (mandato)` = Leader_etiqueta_termino, `Total viajes` = total_viajes)

write.csv(tabla_perfil_regional, file.path(RUTA_OUTPUTS, "16_perfil_regional_por_presidente.csv"), row.names = FALSE)


## ---- 17. "Integracion regional en retirada" (recreacion con nuestros datos) --
## El usuario paso un grafico de estilo editorial (Diplometrics COLT crudo,
## 1990-2025: pico 64% en 2011, minimo 43.4% en 2025) y pidio recrearlo con
## nuestra base propia (verificada/corregida, con la regla "solo durante el
## mandato" ya aplicada). Esta version arranca en ANIO_DESDE (1994, no 1990):
## nuestra cobertura verificada de varios paises no llega de forma confiable
## a 1990-1993 -ver tareas pendientes "Build Brasil/Chile module 1994-1999"-,
## asi que estirar el rango habria significado mezclar años sin el mismo
## nivel de verificacion que el resto de la base. Con nuestros datos el
## patron se sostiene casi identico al original: pico y minimo caen en los
## mismos años (2011 / 2025), con valores muy cercanos (64.4% / 43.6%).
##
## A diferencia del resto de las figuras de este script (estetica Q1, sin
## titulo/subtitulo dentro de la imagen -eso lo pone el \caption{} de LaTeX-),
## este grafico puntual SI lleva titulo/subtitulo/fuente adentro de la
## imagen, replicando el estilo editorial del original que pidio el usuario.
viajes_latam_por_anio <- colt %>%
  mutate(es_latam = RegionVisited == "Latin America and the Caribbean") %>%
  group_by(Year) %>%
  summarise(participacion = mean(es_latam, na.rm = TRUE) * 100, .groups = "drop") %>%
  arrange(Year) %>%
  mutate(
    # Promedio movil centrado de 3 años (year-1, year, year+1), con ventana
    # parcial en los bordes (1994 y 2025 promedian solo 2 años).
    promedio_movil = sapply(seq_along(participacion), function(i) {
      mean(participacion[max(1, i - 1):min(length(participacion), i + 1)])
    })
  )

punto_pico <- viajes_latam_por_anio %>% slice_max(promedio_movil, n = 1, with_ties = FALSE)
punto_minimo <- viajes_latam_por_anio %>% slice_min(promedio_movil, n = 1, with_ties = FALSE)

g17 <- ggplot(viajes_latam_por_anio, aes(x = Year, y = promedio_movil)) +
  geom_area(fill = gris_1, alpha = 0.6) +
  geom_line(color = "black", linewidth = 0.9) +
  geom_point(data = bind_rows(punto_pico, punto_minimo), color = "black", size = 2) +
  annotate("text", x = punto_pico$Year, y = punto_pico$promedio_movil + 3,
           label = paste0("Pico: ", round(punto_pico$promedio_movil), "% (", punto_pico$Year, ")"),
           size = 3.2, family = FUENTE_BASE, fontface = "bold", color = "black") +
  annotate("text", x = punto_minimo$Year, y = punto_minimo$promedio_movil - 3,
           label = paste0("Mínimo: ", round(punto_minimo$promedio_movil, 1), "% (", punto_minimo$Year, ")"),
           size = 3.2, family = FUENTE_BASE, fontface = "bold", color = "black") +
  scale_x_continuous(breaks = scales::breaks_width(5)) +
  scale_y_continuous(labels = function(x) paste0(x, "%"), limits = c(min(viajes_latam_por_anio$promedio_movil) - 8, NA)) +
  labs(
    title = "Integración regional en retirada",
    subtitle = paste0("Viajes intra-latinoamericanos como % del total de viajes presidenciales sudamericanos\n",
                       "Promedio móvil de 3 años · ", ANIO_DESDE, "-", ANIO_HASTA),
    x = NULL, y = NULL,
    caption = paste0("Fuente: base propia (cruzada y verificada contra Diplometrics COLT Dataset, Frederick S. Pardee\n",
                      "Institute for International Futures, University of Denver), viajes de Jefes de Estado/Gobierno\n",
                      "de Argentina, Bolivia, Brasil, Chile, Colombia, Ecuador, Guyana, Paraguay, Perú, Surinam, Uruguay y Venezuela.")
  ) +
  theme_minimal(base_size = 12, base_family = FUENTE_BASE) +
  theme(
    plot.title = element_text(face = "bold", size = rel(1.3), color = "black"),
    plot.subtitle = element_text(size = rel(0.85), color = gris_6, margin = margin(b = 12)),
    plot.caption = element_text(size = rel(0.6), color = gris_5, hjust = 0, margin = margin(t = 12)),
    panel.grid.minor = element_blank(),
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_line(color = gris_1, linewidth = 0.3),
    axis.text = element_text(color = gris_6),
    plot.background = element_rect(fill = "white", color = gris_3, linewidth = 0.4),
    plot.margin = margin(16, 20, 12, 16)
  )

print(g17)
ggsave(file.path(RUTA_OUTPUTS, "17_integracion_regional_en_retirada.png"), g17, width = 9, height = 6, dpi = 150)
write.csv(viajes_latam_por_anio, file.path(RUTA_OUTPUTS, "17_integracion_regional_en_retirada.csv"), row.names = FALSE)


## ---- 17b. Viajes BILATERALES recibidos por cada pais sudamericano, de otros --
## paises sudamericanos (mismo estilo que la Figura 8/seccion 15: facet_wrap
## con geom_col + linea de promedio por panel). A diferencia de la seccion 15
## (que mira a DONDE viajan los presidentes sudamericanos), esta mira quien
## RECIBE esos viajes -permite ver, pais por pais, si gana o pierde peso como
## destino de sus vecinos a lo largo del tiempo (ej. Venezuela).
## Se restringe a Visit_Category == "Bilateral" (visita puntual dirigida a ese
## pais) para no mezclar "recibir una visita" con "ser sede de una cumbre
## multilateral" -son fenomenos distintos; decision del usuario, 2026-09-01-.
paises_sudamerica_en <- c("Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
                           "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela")
orden_pais_receptor <- unname(etiquetas_es[paises_sudamerica_en])  # ya alfabetico en es

viajes_recibidos_intra_sudamerica <- colt %>%
  filter(Visit_Category == "Bilateral",
         LeaderCountryOrIGO %in% paises_sudamerica_en,
         CountryVisited %in% paises_sudamerica_en,
         LeaderCountryOrIGO != CountryVisited) %>%
  mutate(Pais_receptor = recode(CountryVisited, !!!etiquetas_es)) %>%
  count(Year, Pais_receptor, name = "n_viajes") %>%
  complete(Year = ANIO_DESDE:ANIO_HASTA, Pais_receptor = orden_pais_receptor, fill = list(n_viajes = 0)) %>%
  mutate(Pais_receptor = factor(Pais_receptor, levels = orden_pais_receptor))

promedio_recibidos_por_pais <- viajes_recibidos_intra_sudamerica %>%
  group_by(Pais_receptor) %>%
  summarise(promedio = mean(n_viajes, na.rm = TRUE), .groups = "drop")

g17b <- ggplot(viajes_recibidos_intra_sudamerica, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_6) +
  geom_hline(data = promedio_recibidos_por_pais, aes(yintercept = promedio),
             linetype = "dashed", color = gris_9, linewidth = 0.5) +
  # Escala fija (NO free_y, pedido del usuario 2026-09-02): los 12 paneles
  # comparten el mismo eje Y para que se pueda comparar a simple vista
  # cuanto recibe cada pais frente a los demas, no solo su propia forma.
  facet_wrap(~Pais_receptor, ncol = 3) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 5)) +
  labs(x = NULL, y = "Cantidad de viajes bilaterales recibidos")

print(g17b)
ggsave(file.path(RUTA_OUTPUTS, "17b_viajes_recibidos_intra_sudamerica.png"), g17b, width = 11, height = 13, dpi = 150)
write.csv(viajes_recibidos_intra_sudamerica, file.path(RUTA_OUTPUTS, "17b_viajes_recibidos_intra_sudamerica.csv"), row.names = FALSE)

## Panel aparte, mas grande, para Cuba: no es un pais sudamericano (queda
## fuera de la grilla de 12 de arriba) pero el usuario pidio verlo aparte por
## su peso simbolico/historico como destino de la diplomacia sudamericana
## (cumbres del ALBA, relacion con Venezuela, giras medicas/de cooperacion,
## etc.) -mismo criterio Bilateral-only que el resto de esta seccion.
viajes_recibidos_cuba <- colt %>%
  filter(Visit_Category == "Bilateral",
         LeaderCountryOrIGO %in% paises_sudamerica_en,
         CountryVisited == "Cuba") %>%
  count(Year, name = "n_viajes") %>%
  complete(Year = ANIO_DESDE:ANIO_HASTA, fill = list(n_viajes = 0))

promedio_recibidos_cuba <- mean(viajes_recibidos_cuba$n_viajes, na.rm = TRUE)

g17c <- ggplot(viajes_recibidos_cuba, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_6) +
  geom_hline(yintercept = promedio_recibidos_cuba, linetype = "dashed", color = gris_9, linewidth = 0.5) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  labs(x = NULL, y = "Cantidad de viajes bilaterales recibidos")

print(g17c)
ggsave(file.path(RUTA_OUTPUTS, "17c_viajes_recibidos_cuba.png"), g17c, width = 9, height = 5, dpi = 150)
write.csv(viajes_recibidos_cuba, file.path(RUTA_OUTPUTS, "17c_viajes_recibidos_cuba.csv"), row.names = FALSE)


## ---- 18. Ideologia presidencial y viajes intra-latinoamericanos ---------------
## Cruza la base propia de ideologia presidencial (Merke, Reynoso & Schenoni 2020,
## actualizada con investigacion propia via "CPE - Latinoamerica"; ver
## 04_BASE_FINAL/Base_Ideologia_Presidencial.xlsx) contra los viajes, usando el
## crosswalk Leader_key + fecha exacta de mandato-tramo ya construido en esa
## planilla (columnas Leader_key, Mandato_asignado_inicio/fin). Deliberadamente
## NO se usa el "yearinoffice" propio de la base de ideologia como fecha de corte:
## en varios casos (Duhalde, N.Kirchner, CFK1, Menem2, Fujimori2/3, Correa2/3,
## Chavez2/3, Cartes, Maduro1) ese campo no coincide con la fecha real de
## asuncion -se investigo cada caso y se documento en la columna
## Nota_crosswalk de la planilla-.
##
## Pendiente (ver 05_BITACORA/PENDIENTES_VERIFICACION.txt, entrada 2026-08-28):
## Jeanine Añez (Bolivia) y Francisco Sagasti (Peru) estan en la base de
## ideologia pero no en mandatos_presidenciales.csv ni tienen viajes cargados
## en la base -quedan afuera de este cruce hasta que se investiguen desde cero-.
RUTA_IDEOLOGIA <- "Base Viaje Presidenciales Latam/04_BASE_FINAL/Base_Ideologia_Presidencial.xlsx"
ideologia <- tryCatch(read_excel(RUTA_IDEOLOGIA), error = function(e) NULL)

if (is.null(ideologia)) {

  warning("No se pudo leer Base_Ideologia_Presidencial.xlsx -se omite la seccion 18 (ideologia y viajes).")

} else {

  ideologia_cw <- ideologia %>%
    filter(!is.na(Leader_key)) %>%
    mutate(
      Mandato_asignado_inicio = ymd(Mandato_asignado_inicio),
      Mandato_asignado_fin    = ymd(Mandato_asignado_fin)
    ) %>%
    select(Leader_key, presidents, country, Pais_base_viajes, Mandato_asignado_inicio, Mandato_asignado_fin,
           ideology, economy, geopolitics, style, usa, sovereignty, development, reputation)

  # Join por Leader_key (puede traer varios tramos candidatos por presidente
  # reelegido) y despues se filtra por la fecha exacta del viaje dentro del
  # tramo correspondiente.
  viajes_ideologia <- colt %>%
    filter(!is.na(CountryVisited)) %>%
    inner_join(ideologia_cw, by = "Leader_key") %>%
    filter(TripStartDate >= Mandato_asignado_inicio, TripStartDate < Mandato_asignado_fin) %>%
    mutate(
      es_latam  = RegionVisited == "Latin America and the Caribbean",
      es_usa    = CountryVisited == "United States",
      es_china  = CountryVisited == "China",
      es_europa = RegionVisited == "Europe"
    )

  # Chequeo de sanidad: cada viaje deberia matchear un unico tramo de ideologia
  # (si el crosswalk tuviera fechas superpuestas, apareceria aca duplicado).
  chequeo_dup_ideologia <- viajes_ideologia %>% count(TripID) %>% filter(n > 1)
  if (nrow(chequeo_dup_ideologia) > 0) {
    warning(nrow(chequeo_dup_ideologia), " viajes matchean mas de un tramo de ideologia -revisar Mandato_asignado_inicio/fin en Base_Ideologia_Presidencial.xlsx-.")
  }

  # Tabla maestra: una fila por mandato-tramo, con las 8 dimensiones de
  # ideologia y la intensidad/composicion de sus viajes.
  resumen_ideologia_presidente <- viajes_ideologia %>%
    group_by(Leader_key, presidents, country, Mandato_asignado_inicio, Mandato_asignado_fin,
             ideology, economy, geopolitics, style, usa, sovereignty, development, reputation) %>%
    summarise(
      n_viajes             = n(),
      n_viajes_intralatam  = sum(es_latam, na.rm = TRUE),
      pct_intralatam       = 100 * n_viajes_intralatam / n_viajes,
      n_viajes_usa         = sum(es_usa, na.rm = TRUE),
      pct_usa              = 100 * n_viajes_usa / n_viajes,
      n_viajes_china       = sum(es_china, na.rm = TRUE),
      pct_china            = 100 * n_viajes_china / n_viajes,
      n_viajes_europa      = sum(es_europa, na.rm = TRUE),
      pct_europa           = 100 * n_viajes_europa / n_viajes,
      .groups = "drop"
    ) %>%
    # Exigimos un minimo de viajes para que el % no sea ruido de muestras chicas
    # (ej. un mandato-tramo con 1 solo viaje no dice nada sobre su perfil).
    filter(n_viajes >= 5) %>%
    mutate(
      bloque_ideologico = cut(ideology, breaks = c(0, 3, 5, 7.01),
                               labels = c("Izquierda (1-3)", "Centro (3-5)", "Derecha (5-7)"),
                               right = FALSE)
    )

  write.csv(resumen_ideologia_presidente,
            file.path(RUTA_OUTPUTS, "18a_ideologia_y_viajes_por_mandato.csv"), row.names = FALSE)

  # --- Cuadro: correlacion de Pearson entre cada dimension de ideologia y el
  # % de viajes intra-latinoamericanos, un mandato-tramo = una observacion. ---
  dimensiones <- c("ideology", "economy", "geopolitics", "style", "usa",
                    "sovereignty", "development", "reputation")
  etiquetas_dimensiones <- c(
    ideology    = "Ideologia general (1=izq., 7=der.)",
    economy     = "Politica economica",
    geopolitics = "Geopolitica",
    style       = "Estilo diplomatico",
    usa         = "Relacion con EE.UU.",
    sovereignty = "Soberania / autonomia",
    development = "Modelo de desarrollo",
    reputation  = "Reputacion internacional"
  )

  correlacion_ideologia_viajes <- lapply(dimensiones, function(dim) {
    x <- resumen_ideologia_presidente[[dim]]
    y <- resumen_ideologia_presidente$pct_intralatam
    ok <- complete.cases(x, y)
    test <- suppressWarnings(cor.test(x[ok], y[ok], method = "pearson"))
    data.frame(
      Dimension  = etiquetas_dimensiones[[dim]],
      r_pearson  = round(unname(test$estimate), 3),
      valor_p    = round(test$p.value, 4),
      n_mandatos = sum(ok)
    )
  }) %>% bind_rows()

  write.csv(correlacion_ideologia_viajes,
            file.path(RUTA_OUTPUTS, "18b_correlacion_ideologia_viajes_intralatam.csv"), row.names = FALSE)

  # --- Figura A: ideologia general vs. % de viajes intra-latinoamericanos ---
  # (el hallazgo central de Merke, Reynoso & Schenoni 2020 es que la ideologia
  # presidencial es la variable que mas explica el cambio de politica exterior;
  # este grafico prueba si eso se sostiene especificamente para el enfoque
  # regional de los viajes en Sudamerica).
  fila_r_ideology <- correlacion_ideologia_viajes[correlacion_ideologia_viajes$Dimension == etiquetas_dimensiones[["ideology"]], ]
  etiqueta_r_ideology <- paste0("r = ", format(fila_r_ideology$r_pearson, nsmall = 2),
                                 "  (p = ", format(fila_r_ideology$valor_p, nsmall = 3),
                                 ", n = ", fila_r_ideology$n_mandatos, ")")

  g18a <- ggplot(resumen_ideologia_presidente, aes(x = ideology, y = pct_intralatam)) +
    geom_smooth(method = "lm", se = TRUE, color = gris_6, fill = gris_1, linewidth = 0.6) +
    geom_point(aes(size = n_viajes), color = gris_9, alpha = 0.75) +
    annotate("text", x = 1, y = 102, label = etiqueta_r_ideology, hjust = 0, vjust = 1,
             size = 3.2, family = FUENTE_BASE, color = gris_7) +
    scale_size_continuous(name = "Cantidad de\nviajes", range = c(1.5, 6)) +
    scale_x_continuous(breaks = 1:7, limits = c(1, 7)) +
    scale_y_continuous(limits = c(0, 105), breaks = seq(0, 100, 25)) +
    labs(x = "Ideologia presidencial (1 = izquierda, 7 = derecha)",
         y = "% de viajes intra-latinoamericanos")

  print(g18a)
  ggsave(file.path(RUTA_OUTPUTS, "18c_ideologia_vs_intralatam.png"), g18a, width = 8, height = 6, dpi = 150)

  # --- Figura B: las 8 dimensiones a la vez, misma variable Y (grilla) ---
  resumen_largo_ideologia <- resumen_ideologia_presidente %>%
    select(presidents, pct_intralatam, all_of(dimensiones)) %>%
    pivot_longer(cols = all_of(dimensiones), names_to = "dimension", values_to = "valor") %>%
    mutate(
      dimension = recode(dimension, !!!etiquetas_dimensiones),
      dimension = factor(dimension, levels = unname(etiquetas_dimensiones))
    )

  g18b <- ggplot(resumen_largo_ideologia, aes(x = valor, y = pct_intralatam)) +
    geom_smooth(method = "lm", se = FALSE, color = gris_6, linewidth = 0.5) +
    geom_point(color = gris_9, alpha = 0.6, size = 1.4) +
    facet_wrap(~dimension, scales = "free_x", ncol = 4) +
    labs(x = "Valor de la dimension (escala 1-7)", y = "% de viajes intra-latinoamericanos")

  print(g18b)
  ggsave(file.path(RUTA_OUTPUTS, "18d_todas_dimensiones_vs_intralatam.png"), g18b, width = 12, height = 7, dpi = 150)

  # --- Figuras E, F y G (pedido del usuario): 3 variantes de la Figura B/18d
  # de arriba, filtrando el universo de mandato-tramos en vez de usar todos.
  # Se factoriza la logica de graficado en una funcion para no repetir
  # codigo 3 veces. ---
  graficar_todas_dimensiones <- function(datos_resumen) {
    datos_largo <- datos_resumen %>%
      select(presidents, pct_intralatam, all_of(dimensiones)) %>%
      pivot_longer(cols = all_of(dimensiones), names_to = "dimension", values_to = "valor") %>%
      mutate(
        dimension = recode(dimension, !!!etiquetas_dimensiones),
        dimension = factor(dimension, levels = unname(etiquetas_dimensiones))
      )

    ggplot(datos_largo, aes(x = valor, y = pct_intralatam)) +
      geom_smooth(method = "lm", se = FALSE, color = gris_6, linewidth = 0.5) +
      geom_point(color = gris_9, alpha = 0.6, size = 1.4) +
      facet_wrap(~dimension, scales = "free_x", ncol = 4) +
      labs(x = "Valor de la dimension (escala 1-7)", y = "% de viajes intra-latinoamericanos")
  }

  # Figuras E/F: mismo grafico que 18d, pero separando mandato-tramos de
  # ideologia general BAJA (<=3, izquierda) y ALTA (>=5, derecha) -para ver
  # si el patron de las 8 dimensiones difiere segun el bloque ideologico.
  resumen_ideologia_izquierda <- resumen_ideologia_presidente %>% filter(ideology <= 3)
  g18i <- graficar_todas_dimensiones(resumen_ideologia_izquierda)
  print(g18i)
  ggsave(file.path(RUTA_OUTPUTS, "18i_todas_dimensiones_izquierda.png"), g18i, width = 12, height = 7, dpi = 150)

  resumen_ideologia_derecha <- resumen_ideologia_presidente %>% filter(ideology >= 5)
  g18j <- graficar_todas_dimensiones(resumen_ideologia_derecha)
  print(g18j)
  ggsave(file.path(RUTA_OUTPUTS, "18j_todas_dimensiones_derecha.png"), g18j, width = 12, height = 7, dpi = 150)

  # Figura G: mismo grafico que 18d, pero restringido a los mandato-tramos
  # que se SOLAPAN con la ventana 2012-2022 (los ultimos 10 anios con dato
  # de ideologia disponible) -se usa solapamiento de rango, no que el
  # mandato entero caiga adentro, para no perder tramos que arrancan o
  # terminan cerca del borde de la ventana.
  resumen_ideologia_2012_2022 <- resumen_ideologia_presidente %>%
    filter(Mandato_asignado_inicio <= as.Date("2022-12-31"),
           Mandato_asignado_fin   >= as.Date("2012-01-01"))
  g18k <- graficar_todas_dimensiones(resumen_ideologia_2012_2022)
  print(g18k)
  ggsave(file.path(RUTA_OUTPUTS, "18k_todas_dimensiones_2012_2022.png"), g18k, width = 12, height = 7, dpi = 150)

  # --- Figura C: validacion cruzada -- dimension "usa" vs. % de viajes a
  # Estados Unidos especificamente (a diferencia de las figuras A/B, que usan
  # el % intra-latinoamericano como variable dependiente en todos los casos,
  # esta compara cada dimension con la variable de viajes que mas deberia
  # explicar segun su propia definicion). ---
  g18c <- ggplot(resumen_ideologia_presidente, aes(x = usa, y = pct_usa)) +
    geom_smooth(method = "lm", se = TRUE, color = gris_6, fill = gris_1, linewidth = 0.6) +
    geom_point(aes(size = n_viajes), color = gris_9, alpha = 0.75) +
    scale_size_continuous(name = "Cantidad de\nviajes", range = c(1.5, 6)) +
    scale_x_continuous(breaks = 1:7, limits = c(1, 7)) +
    labs(x = "Orientacion hacia EE.UU. (1 = distante/autonomista, 7 = alineado)",
         y = "% de viajes a Estados Unidos")

  print(g18c)
  ggsave(file.path(RUTA_OUTPUTS, "18e_usa_vs_pct_viajes_eeuu.png"), g18c, width = 8, height = 6, dpi = 150)

  # --- Figura D: comparacion por bloque ideologico (izquierda/centro/derecha) ---
  g18d <- ggplot(resumen_ideologia_presidente, aes(x = bloque_ideologico, y = pct_intralatam)) +
    geom_boxplot(fill = gris_1, color = gris_7, outlier.shape = NA) +
    geom_jitter(width = 0.15, size = 1.6, color = gris_9, alpha = 0.7) +
    labs(x = NULL, y = "% de viajes intra-latinoamericanos")

  print(g18d)
  ggsave(file.path(RUTA_OUTPUTS, "18f_bloque_ideologico_vs_intralatam.png"), g18d, width = 7, height = 6, dpi = 150)

  # --- Cuadro: ideologia general (no la dimension "usa") vs. % de viajes a
  # Estados Unidos, China y Europa -tres destinos extra-regionales de interes
  # geopolitico. A diferencia de la Figura C (que usaba la dimension "usa"
  # especificamente), aca se usa siempre la misma variable X (ideology, 1=izq,
  # 7=der.) para las tres, de forma comparable entre si. ---
  destinos_extra <- c(pct_usa = "Estados Unidos", pct_china = "China", pct_europa = "Europa")

  correlacion_ideologia_destinos <- lapply(names(destinos_extra), function(var) {
    x <- resumen_ideologia_presidente$ideology
    y <- resumen_ideologia_presidente[[var]]
    ok <- complete.cases(x, y)
    test <- suppressWarnings(cor.test(x[ok], y[ok], method = "pearson"))
    data.frame(
      Destino    = destinos_extra[[var]],
      r_pearson  = round(unname(test$estimate), 3),
      valor_p    = round(test$p.value, 4),
      n_mandatos = sum(ok)
    )
  }) %>% bind_rows()

  write.csv(correlacion_ideologia_destinos,
            file.path(RUTA_OUTPUTS, "18g_correlacion_ideologia_usa_china_europa.csv"), row.names = FALSE)

  # --- Figura E: ideologia general vs. % de viajes a EE.UU./China/Europa (grilla) ---
  resumen_largo_destinos <- resumen_ideologia_presidente %>%
    select(presidents, ideology, n_viajes, all_of(names(destinos_extra))) %>%
    pivot_longer(cols = all_of(names(destinos_extra)), names_to = "destino", values_to = "pct") %>%
    mutate(
      destino = recode(destino, !!!destinos_extra),
      destino = factor(destino, levels = unname(destinos_extra))
    )

  g18e <- ggplot(resumen_largo_destinos, aes(x = ideology, y = pct)) +
    geom_smooth(method = "lm", se = TRUE, color = gris_6, fill = gris_1, linewidth = 0.6) +
    geom_point(aes(size = n_viajes), color = gris_9, alpha = 0.7) +
    facet_wrap(~destino, scales = "free_y", ncol = 3) +
    scale_x_continuous(breaks = 1:7, limits = c(1, 7)) +
    scale_size_continuous(name = "Cantidad de\nviajes", range = c(1, 5)) +
    labs(x = "Ideologia presidencial (1 = izquierda, 7 = derecha)",
         y = "% de viajes al destino")

  print(g18e)
  ggsave(file.path(RUTA_OUTPUTS, "18h_ideologia_vs_eeuu_china_europa.png"), g18e, width = 12, height = 5, dpi = 150)

  cat("\n[Seccion 18] Ideologia y viajes:", nrow(resumen_ideologia_presidente),
      "mandatos-tramo (con >=5 viajes) cruzados contra las 8 dimensiones de ideologia.\n")
}


## ---- 19. Homofilia ideologica en los destinos (viajes Sudamerica -> Sudamerica) ----
## Responde la pregunta: los gobiernos de un bloque ideologico, tienen mas
## chances de visitar a un par de la MISMA ideologia que las que tendrian por
## puro azar, dada la composicion ideologica de la region en cada momento?
## Se arman DOS versiones a proposito, pedidas explicitamente:
##  - "sin controlar": el % crudo de viajes a la misma ideologia, por bloque de
##    origen. Este numero esta confundido por la oferta -si en un periodo dado
##    la mayoria de los gobiernos de la region son de un mismo bloque (ej. la
##    "marea rosa" 2004-2015), ese bloque va a mostrar mas "viajes a la misma
##    ideologia" solo porque hay mas destinos de ese tipo disponibles, no
##    necesariamente porque haya una preferencia real por visitar pares-.
##  - "controlando": un indice observado/esperado, donde el esperado se calcula
##    con la composicion ideologica real de los destinos disponibles EN CADA
##    PERIODO de 5 anios (no un promedio general de todo 1994-2025) -asi se
##    aisla la preferencia de la oferta cambiante. Un indice > 1 indica mas
##    visitas "propias" de las esperadas por azar; = 1, exactamente lo
##    esperado; < 1, menos de lo esperado.
## Requiere que la Seccion 18 se haya corrido antes (usa viajes_ideologia e
## ideologia_cw ya construidos ahi).
if (exists("ideologia_cw") && exists("viajes_ideologia")) {

  destino_lookup <- ideologia_cw %>%
    filter(!is.na(Pais_base_viajes)) %>%
    select(Pais_base_viajes, Mandato_asignado_inicio, Mandato_asignado_fin,
           ideology_destino = ideology, presidente_destino = presidents)

  dyadico <- viajes_ideologia %>%
    select(TripID, TripStartDate, Periodo5, CountryVisited, presidents, ideology) %>%
    rename(ideology_origen = ideology, presidente_origen = presidents) %>%
    inner_join(destino_lookup, by = c("CountryVisited" = "Pais_base_viajes")) %>%
    filter(TripStartDate >= Mandato_asignado_inicio, TripStartDate < Mandato_asignado_fin) %>%
    mutate(
      bloque_origen = cut(ideology_origen, breaks = c(0, 3, 5, 7.01),
                           labels = c("Izquierda", "Centro", "Derecha"), right = FALSE),
      bloque_destino = cut(ideology_destino, breaks = c(0, 3, 5, 7.01),
                            labels = c("Izquierda", "Centro", "Derecha"), right = FALSE),
      misma_ideologia = bloque_origen == bloque_destino
    )

  # Chequeo de sanidad: un viaje no deberia matchear mas de un tramo de destino.
  chequeo_dup_dyadico <- dyadico %>% count(TripID) %>% filter(n > 1)
  if (nrow(chequeo_dup_dyadico) > 0) {
    warning(nrow(chequeo_dup_dyadico), " viajes matchean mas de un tramo de destino en el analisis diadico -revisar Base_Ideologia_Presidencial.xlsx-.")
  }

  write.csv(dyadico, file.path(RUTA_OUTPUTS, "19a_homofilia_ideologica_diadico.csv"), row.names = FALSE)

  # --- Cuadro: test de independencia chi-cuadrado + indice de homofilia total (1994-2025) ---
  tabla_contingencia <- table(dyadico$bloque_origen, dyadico$bloque_destino)
  test_chi2 <- suppressWarnings(chisq.test(tabla_contingencia))
  esperado <- test_chi2$expected

  indice_homofilia_total <- data.frame(
    Bloque            = rownames(tabla_contingencia),
    Viajes_observados = diag(tabla_contingencia[, rownames(tabla_contingencia)]),
    Viajes_esperados  = round(diag(esperado[, rownames(tabla_contingencia)]), 1),
    Indice_homofilia  = round(diag(tabla_contingencia[, rownames(tabla_contingencia)]) / diag(esperado[, rownames(tabla_contingencia)]), 2)
  )

  write.csv(indice_homofilia_total, file.path(RUTA_OUTPUTS, "19b_indice_homofilia_total.csv"), row.names = FALSE)
  cat("\n[Seccion 19] Test chi-cuadrado (bloque origen x bloque destino): chi2 =",
      round(unname(test_chi2$statistic), 2), ", df =", unname(test_chi2$parameter),
      ", p =", format.pval(test_chi2$p.value, digits = 3), ", n =", nrow(dyadico), "\n")

  # --- Figura F: SIN controlar -- % de viajes a la misma ideologia, por periodo ---
  sin_controlar <- dyadico %>%
    group_by(Periodo5, bloque_origen) %>%
    summarise(pct_misma = 100 * mean(misma_ideologia, na.rm = TRUE), n = n(), .groups = "drop")

  g19f <- ggplot(sin_controlar, aes(x = Periodo5, y = pct_misma, color = bloque_origen, linetype = bloque_origen)) +
    geom_line(linewidth = 0.8) +
    geom_point(aes(size = n)) +
    scale_color_manual(values = c(Izquierda = gris_9, Centro = gris_5, Derecha = gris_3), name = "Bloque de origen") +
    scale_linetype_manual(values = c(Izquierda = "solid", Centro = "dashed", Derecha = "dotted"), name = "Bloque de origen") +
    scale_size_continuous(name = "Cantidad de\nviajes", range = c(1, 5)) +
    scale_x_continuous(breaks = unique(sin_controlar$Periodo5)) +
    scale_y_continuous(limits = c(0, 100)) +
    labs(x = NULL, y = "% de viajes a un presidente de la misma ideologia\n(SIN controlar por oferta)")

  print(g19f)
  ggsave(file.path(RUTA_OUTPUTS, "19c_homofilia_sin_controlar.png"), g19f, width = 9, height = 6, dpi = 150)

  # --- Figura G: CONTROLANDO -- indice observado/esperado, por periodo ---
  # El esperado de cada periodo usa la composicion ideologica real de TODOS los
  # destinos disponibles en ESE periodo (no un promedio general de 1994-2025),
  # para no confundir preferencia con oferta cambiante.
  oferta_por_periodo <- dyadico %>%
    count(Periodo5, bloque_destino) %>%
    group_by(Periodo5) %>%
    mutate(pct_oferta = n / sum(n)) %>%
    ungroup() %>%
    select(Periodo5, bloque_destino, pct_oferta)

  controlando <- sin_controlar %>%
    left_join(oferta_por_periodo, by = c("Periodo5", "bloque_origen" = "bloque_destino")) %>%
    mutate(
      pct_esperado      = 100 * pct_oferta,
      indice_homofilia  = pct_misma / pct_esperado
    )

  write.csv(controlando, file.path(RUTA_OUTPUTS, "19d_homofilia_controlando_por_periodo.csv"), row.names = FALSE)

  g19g <- ggplot(controlando, aes(x = Periodo5, y = indice_homofilia, color = bloque_origen, linetype = bloque_origen)) +
    geom_hline(yintercept = 1, color = gris_3, linewidth = 0.5) +
    geom_line(linewidth = 0.8) +
    geom_point(aes(size = n)) +
    scale_color_manual(values = c(Izquierda = gris_9, Centro = gris_5, Derecha = gris_3), name = "Bloque de origen") +
    scale_linetype_manual(values = c(Izquierda = "solid", Centro = "dashed", Derecha = "dotted"), name = "Bloque de origen") +
    scale_size_continuous(name = "Cantidad de\nviajes", range = c(1, 5)) +
    scale_x_continuous(breaks = unique(controlando$Periodo5)) +
    labs(x = NULL, y = "Indice de homofilia\n(observado / esperado segun oferta ideologica del periodo)")

  print(g19g)
  ggsave(file.path(RUTA_OUTPUTS, "19e_homofilia_controlando.png"), g19g, width = 9, height = 6, dpi = 150)

  # --- Figura H: matriz origen x destino, % de fila, todo el periodo junto ---
  matriz_pct <- as.data.frame(prop.table(tabla_contingencia, margin = 1) * 100) %>%
    rename(bloque_origen = Var1, bloque_destino = Var2, pct = Freq) %>%
    mutate(color_texto = if_else(pct > 40, "white", "black"))

  g19h <- ggplot(matriz_pct, aes(x = bloque_destino, y = bloque_origen, fill = pct)) +
    geom_tile(color = "white") +
    geom_text(aes(label = paste0(round(pct), "%"), color = color_texto), family = FUENTE_BASE, size = 4.5) +
    scale_color_identity() +
    scale_fill_gradient(low = gris_2, high = gris_9, name = "% de\nfila") +
    labs(x = "Bloque ideologico del destino", y = "Bloque ideologico del origen")

  print(g19h)
  ggsave(file.path(RUTA_OUTPUTS, "19f_matriz_origen_destino.png"), g19h, width = 7, height = 6, dpi = 150)

  cat("[Seccion 19] Homofilia ideologica:", nrow(dyadico), "viajes Sudamerica->Sudamerica con origen y destino matcheados a ideologia.\n")

} else {
  warning("No se pudo construir el analisis de homofilia ideologica (seccion 19) -falta ideologia_cw o viajes_ideologia de la seccion 18-.")
}


## ---- 10. Resumen final en consola ----------------------------------------------

cat("\n================================================================\n")
cat("Graficos y tablas guardados en:", RUTA_OUTPUTS, "\n")
cat("================================================================\n")
cat("00a_ficha_general.png/.csv                      -> Descriptivos: ficha general (Cuadro en el paper)\n")
cat("00b_viajes_totales_por_pais.png/.csv            -> Descriptivos: total de viajes por pais\n")
cat("00c_viajes_totales_por_mandatario.png/.csv       -> Descriptivos: total por mandatario (con periodo)\n")
cat("00d_resumen_estadisticos_descriptivos.png/.csv   -> Descriptivos: tabla tipo 'Tabla 1' (Cuadro en el paper)\n")
cat("01_viajes_por_anio.png / 01b_...pais.png        -> Pregunta 1 (evolucion general; 01b con linea de promedio)\n")
cat("02_regiones_por_periodo.png / 02b_...area.png   -> Pregunta 2 (prioridad regional; 02 con etiquetas LAC/Europa/Norteam.)\n")
cat("03_duracion_por_anio.png                        -> Pregunta 3 (duracion; ELIMINADA del paper, ver 03c)\n")
cat("03c_viajes_y_duracion_combinado.png             -> Preguntas 1+3 combinadas (viajes y duracion)\n")
cat("04_categoria_visita_por_anio.png (barras x periodo) / 04b_...(linea x anio) -> Preguntas 4 y 5 (bi/multi/otro, sin 'Sin dato')\n")
cat("05_top5_destinos_por_presidente.csv             -> Pregunta 6 (tabla completa)\n")
cat("05b_destino_favorito_todos_los_presidentes.png  -> Pregunta 6 (grafico, ya no se usa en el paper)\n")
cat("05c_destino_favorito_tabla.csv                  -> Pregunta 6 (Cuadro del paper: por MANDATO, solo Bilaterales)\n")
cat("   (usar graficar_top_destinos(\"Nombre\") para el detalle de un presidente puntual)\n")
cat("06_primera_visita_por_presidente.csv            -> Pregunta 7 (tabla completa)\n")
cat("06_primeros_destinos_frecuencia.png             -> Pregunta 7 (que paises se repiten)\n")
cat("06b_evolucion_top3_primeros_destinos.png        -> Extension: en que anio EEUU/Brasil/Argentina fueron elegidos PRIMER destino\n")
cat("08_estacionalidad_mensual.png                   -> Extension: meses con mas viajes\n")
cat("09a_ranking_destinos_bilaterales.png            -> Extension: top 20 destinos bilaterales\n")
cat("09a2_evolucion_bilateral_brasil_eeuu.png        -> Extension: evolucion bilateral Brasil/Estados Unidos\n")
cat("09b_ranking_destinos_multilaterales.png         -> Extension: top 20 destinos multilaterales\n")
cat("09b2_evolucion_multilateral_usa_bra_arg.png     -> Extension: evolucion multilateral EE.UU./Brasil/Argentina\n")
cat("09c_foros_distintos_por_periodo.png/.csv        -> Extension: foros/cumbres distintos por periodo (Peña 2005)\n")
cat("09d_composicion_bilateral_multilateral_por_pais.png/.csv -> Extension: composicion por pais (Lee & Kim 2024)\n")
cat("11_viajes_por_anio_de_mandato.png/.csv          -> Extension: viajes normalizados por año de mandato\n")
cat("12_tipo_actividad_viajes.png/.csv               -> Extension: tipo de actividad, TODOS los viajes juntos (ya no se usa en el paper, ver 12a/12b/12c)\n")
cat("12a/12b/12c_tipo_actividad_....png/.csv         -> Extension: tipo de actividad, separado por Bilateral/Multilateral/Otro\n")
cat("13_auge_caida_multilateralismo.png              -> Extension: multilateralismo con hitos regionales (2004/2008/2011/2018/2019)\n")
cat("14_sesgo_vecino_inmediato.png/.csv              -> Extension: sesgo hacia el vecino (Ostrander & Rider 2018), valor agregado 1994-2025\n")
cat("14b_vecino_fronterizo_a_lo_largo_del_tiempo.png/.csv -> Extension: el sesgo hacia el vecino, evolucion anio a anio\n")
cat("14b_correlacion_vecino_tiempo.csv               -> Extension: correlacion tiempo vs. % viajes a vecino (Cuadro en el paper)\n")
cat("15_evolucion_por_bloque_destino.png/.csv        -> Extension: evolucion por bloque (Sudamerica/Latam/EEUU/Europa/Africa/Asia)\n")
cat("16_perfil_regional_por_presidente.csv           -> Extension: perfil regional por MANDATO individual (Cuadro en el paper)\n")
cat("17_integracion_regional_en_retirada.png/.csv    -> Extension: recreacion propia del grafico editorial de referencia\n")
cat("18a_ideologia_y_viajes_por_mandato.csv           -> Ideologia y viajes: tabla maestra por mandato-tramo\n")
cat("18b_correlacion_ideologia_viajes_intralatam.csv  -> Ideologia y viajes: Cuadro de correlaciones (Cuadro en el paper)\n")
cat("18c_ideologia_vs_intralatam.png                  -> Ideologia y viajes: ideologia general vs. % intra-latinoamericano\n")
cat("18d_todas_dimensiones_vs_intralatam.png          -> Ideologia y viajes: las 8 dimensiones vs. % intra-latinoamericano\n")
cat("18e_usa_vs_pct_viajes_eeuu.png                   -> Ideologia y viajes: dimension 'usa' vs. % de viajes a EE.UU.\n")
cat("18f_bloque_ideologico_vs_intralatam.png          -> Ideologia y viajes: boxplot por bloque (ELIMINADA del paper)\n")
cat("18g_correlacion_ideologia_usa_china_europa.csv   -> Ideologia y viajes: correlacion ideologia vs. EEUU/China/Europa\n")
cat("18h_ideologia_vs_eeuu_china_europa.png           -> Ideologia y viajes: ideologia general vs. % a EEUU/China/Europa\n")
cat("18i_todas_dimensiones_izquierda.png              -> Ideologia y viajes: 8 dimensiones, solo ideologia<=3 (izquierda)\n")
cat("18j_todas_dimensiones_derecha.png                -> Ideologia y viajes: 8 dimensiones, solo ideologia>=5 (derecha)\n")
cat("18k_todas_dimensiones_2012_2022.png              -> Ideologia y viajes: 8 dimensiones, solo mandatos 2012-2022\n")
cat("19a_homofilia_ideologica_diadico.csv             -> Homofilia ideologica: tabla diadica origen-destino, viaje a viaje\n")
cat("19b_indice_homofilia_total.csv                   -> Homofilia ideologica: indice observado/esperado total (Cuadro en el paper)\n")
cat("19c_homofilia_sin_controlar.png                  -> Homofilia ideologica: % misma ideologia por periodo (SIN controlar)\n")
cat("19d_homofilia_controlando_por_periodo.csv        -> Homofilia ideologica: indice observado/esperado por periodo\n")
cat("19e_homofilia_controlando.png                    -> Homofilia ideologica: indice observado/esperado por periodo (CONTROLANDO)\n")
cat("19f_matriz_origen_destino.png                    -> Homofilia ideologica: matriz origen x destino (% de fila)\n")
