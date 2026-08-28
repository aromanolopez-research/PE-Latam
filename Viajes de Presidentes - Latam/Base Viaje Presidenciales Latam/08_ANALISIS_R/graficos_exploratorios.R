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
RUTA_MANDATOS <- "Base Viaje Presidenciales Latam/09_PAPER/mandatos_presidenciales.csv"
mandatos <- tryCatch(read.csv(RUTA_MANDATOS, stringsAsFactors = FALSE), error = function(e) NULL)

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
#     media/desvio/min/max de viajes por pais-anio y de duracion).
#     IMPORTANTE (pedido del usuario, item 3A): las primeras filas cuentan
#     combinaciones pais-anio (una celda = un pais en un anio dado), mientras
#     que "Duracion del viaje" cuenta VIAJES INDIVIDUALES -son unidades de
#     observacion distintas, por eso n_obs difiere tanto entre filas. Se deja
#     explicito en la columna Unidad_n_obs para que no se lea como un error.
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
  colt %>% count(Year, LeaderCountryOrIGO, name = "viajes") %>%
    summarise(variable = "Viajes por pais-anio", media = round(mean(viajes), 1), de = round(sd(viajes), 1),
              minimo = min(viajes), maximo = max(viajes), n_obs = n(),
              Unidad_n_obs = "Combinaciones pais-anio"),
  colt %>% filter(!is.na(TripDuration)) %>%
    summarise(variable = "Duracion del viaje (dias)", media = round(mean(TripDuration), 1), de = round(sd(TripDuration), 1),
              minimo = min(TripDuration), maximo = max(TripDuration), n_obs = n(),
              Unidad_n_obs = "Viajes individuales"),
  colt %>% count(Year, LeaderCountryOrIGO, Visit_Category) %>%
    filter(Visit_Category == "Bilateral") %>%
    summarise(variable = "Viajes bilaterales por pais-anio", media = round(mean(n), 1), de = round(sd(n), 1),
              minimo = min(n), maximo = max(n), n_obs = n(),
              Unidad_n_obs = "Combinaciones pais-anio"),
  colt %>% count(Year, LeaderCountryOrIGO, Visit_Category) %>%
    filter(Visit_Category == "Multilateral") %>%
    summarise(variable = "Viajes multilaterales por pais-anio", media = round(mean(n), 1), de = round(sd(n), 1),
              minimo = min(n), maximo = max(n), n_obs = n(),
              Unidad_n_obs = "Combinaciones pais-anio")
)
print(resumen_estadisticos)
write.csv(resumen_estadisticos, file.path(RUTA_OUTPUTS, "00d_resumen_estadisticos_descriptivos.csv"), row.names = FALSE)
guardar_tabla_imagen(resumen_estadisticos, "00d_resumen_estadisticos_descriptivos.png", ancho = 10, alto = 2.6)


## ---- 3. Pregunta 1: evolucion general de la cantidad de viajes por anio -------

viajes_por_anio <- colt %>% count(Year, name = "n_viajes")

g1 <- ggplot(viajes_por_anio, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_5) +
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

categoria_por_anio <- colt %>%
  count(Year, Visit_Category) %>%
  group_by(Year) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

colores_categoria <- c("Bilateral" = gris_9, "Multilateral" = gris_5,
                        "Other" = gris_2, "Sin dato" = gris_1)

g4 <- ggplot(categoria_por_anio, aes(x = Year, y = participacion, fill = Visit_Category)) +
  geom_area(position = "fill", color = "white", linewidth = 0.1) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_manual(values = colores_categoria) +
  labs(x = NULL, y = "Participacion", fill = "Categoria de visita (derivada)")

print(g4)
ggsave(file.path(RUTA_OUTPUTS, "04_categoria_visita_por_anio.png"), g4, width = 11, height = 6.5, dpi = 150)

g4b <- ggplot(colt %>% count(Year, Visit_Category), aes(x = Year, y = n, color = Visit_Category, linetype = Visit_Category)) +
  geom_line(linewidth = 0.9) +
  geom_point(size = 1.2) +
  scale_color_manual(values = colores_categoria) +
  scale_linetype_manual(values = c("Bilateral" = "solid", "Multilateral" = "dashed",
                                    "Other" = "dotted", "Sin dato" = "dotdash")) +
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

# Tabla para el Cuadro del paper (ordenada por pais y, dentro de cada pais,
# por el anio de inicio del mandato -que sale de Periodo_label, primeros 4
# caracteres- para que quede en orden cronologico).
tabla_destino_favorito <- destino_favorito_por_presidente %>%
  mutate(Leader_key = str_to_lower(quitar_tildes(Leader_nombre))) %>%
  left_join(mandatos %>% select(Leader_key, Periodo_label), by = "Leader_key") %>%
  mutate(anio_inicio = suppressWarnings(as.integer(substr(Periodo_label, 1, 4)))) %>%
  arrange(Pais_ES, anio_inicio) %>%
  select(Pais = Pais_ES, `Mandatario (periodo)` = Leader_etiqueta,
         `Destino favorito` = CountryVisited, `Cantidad de viajes` = n_viajes)

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

# 8b) Evolucion 1994-2025 de la cantidad de viajes (todas las categorias) a
#     los 3 paises mas elegidos como primer destino (item 7 del pedido:
#     Estados Unidos, Brasil y Argentina, los primeros 3 de la Figura 14).
g6b <- graficar_evolucion_terna(
  paises = c("United States", "Brazil", "Argentina"),
  categoria = NULL,
  archivo = "06b_evolucion_top3_primeros_destinos.png"
)


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

# 9.2b) Evolucion 1994-2025 de viajes BILATERALES a Brasil, Argentina y Cuba
#       (item 8 del pedido, terna elegida por el usuario junto a la Figura 15).
g9a2 <- graficar_evolucion_terna(
  paises = c("Brazil", "Argentina", "Cuba"),
  categoria = "Bilateral",
  archivo = "09a2_evolucion_bilateral_bra_arg_cuba.png"
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

g9d <- ggplot(composicion_por_pais,
              aes(x = factor(Pais_ES, levels = rev(orden_paises_bilateral)),
                  y = participacion, fill = Visit_Category)) +
  geom_col(position = "stack", color = "white", linewidth = 0.3) +
  coord_flip() +
  scale_y_continuous(labels = scales::percent_format()) +
  # guide_legend(reverse = TRUE): con coord_flip() + barras apiladas, el
  # orden por defecto de la leyenda queda invertido respecto del orden
  # visual del stack (de izquierda a derecha). Esto lo corrige (item 10).
  scale_fill_manual(values = colores_categoria, guide = guide_legend(reverse = TRUE)) +
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


## ---- 13. Extension: auge y caida del multilateralismo (Nolte 2021; Barros & Gonçalves 2021) --
## Toma la participacion de viajes MULTILATERALES por año (subconjunto de
## categoria_por_anio, seccion 6) y le agrega lineas de referencia en 2 hitos
## institucionales para visualizar de un vistazo el quiebre que documenta
## esta literatura: la fundacion de UNASUR (2008, "epoca dorada" del
## regionalismo sudamericano) y su crisis/vaciamiento posterior (desde 2018,
## varios paises suspenden o abandonan el bloque).
multilateral_por_anio <- categoria_por_anio %>% filter(Visit_Category == "Multilateral")

g13 <- ggplot(multilateral_por_anio, aes(x = Year, y = participacion)) +
  geom_line(color = gris_9, linewidth = 0.9) +
  geom_point(color = gris_9, size = 1.4) +
  geom_vline(xintercept = 2008, linetype = "dashed", color = gris_5, linewidth = 0.4) +
  geom_vline(xintercept = 2018, linetype = "dashed", color = gris_5, linewidth = 0.4) +
  annotate("text", x = 2008, y = Inf, label = "Fundacion UNASUR (2008)",
           angle = 90, vjust = -0.6, hjust = 1.05, size = 2.8, family = FUENTE_BASE, color = gris_7) +
  annotate("text", x = 2018, y = Inf, label = "Crisis/vaciamiento UNASUR (desde 2018)",
           angle = 90, vjust = -0.6, hjust = 1.05, size = 2.8, family = FUENTE_BASE, color = gris_7) +
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
cat("03_duracion_por_anio.png                        -> Pregunta 3 (duracion)\n")
cat("03c_viajes_y_duracion_combinado.png             -> Preguntas 1+3 combinadas (viajes y duracion)\n")
cat("04_categoria_visita_por_anio.png / 04b_...      -> Preguntas 4 y 5 (bi/multi/otro)\n")
cat("05_top5_destinos_por_presidente.csv             -> Pregunta 6 (tabla completa)\n")
cat("05b_destino_favorito_todos_los_presidentes.png  -> Pregunta 6 (grafico, ya no se usa en el paper)\n")
cat("05c_destino_favorito_tabla.csv                  -> Pregunta 6 (Cuadro del paper, con periodo de mandato)\n")
cat("   (usar graficar_top_destinos(\"Nombre\") para el detalle de un presidente puntual)\n")
cat("06_primera_visita_por_presidente.csv            -> Pregunta 7 (tabla completa)\n")
cat("06_primeros_destinos_frecuencia.png             -> Pregunta 7 (que paises se repiten)\n")
cat("06b_evolucion_top3_primeros_destinos.png        -> Extension: evolucion EE.UU./Brasil/Argentina 1994-2025\n")
cat("08_estacionalidad_mensual.png                   -> Extension: meses con mas viajes\n")
cat("09a_ranking_destinos_bilaterales.png            -> Extension: top 20 destinos bilaterales\n")
cat("09a2_evolucion_bilateral_bra_arg_cuba.png       -> Extension: evolucion bilateral Brasil/Argentina/Cuba\n")
cat("09b_ranking_destinos_multilaterales.png         -> Extension: top 20 destinos multilaterales\n")
cat("09b2_evolucion_multilateral_usa_bra_arg.png     -> Extension: evolucion multilateral EE.UU./Brasil/Argentina\n")
cat("09c_foros_distintos_por_periodo.png/.csv        -> Extension: foros/cumbres distintos por periodo (Peña 2005)\n")
cat("09d_composicion_bilateral_multilateral_por_pais.png/.csv -> Extension: composicion por pais (Lee & Kim 2024)\n")
cat("11_viajes_por_anio_de_mandato.png/.csv          -> Extension: viajes normalizados por año de mandato\n")
cat("12_tipo_actividad_viajes.png/.csv               -> Extension: tipo de actividad (Charnock et al. 2009)\n")
cat("13_auge_caida_multilateralismo.png              -> Extension: multilateralismo con hitos UNASUR (Nolte 2021)\n")
cat("14_sesgo_vecino_inmediato.png/.csv              -> Extension: sesgo hacia el vecino (Ostrander & Rider 2018)\n")
