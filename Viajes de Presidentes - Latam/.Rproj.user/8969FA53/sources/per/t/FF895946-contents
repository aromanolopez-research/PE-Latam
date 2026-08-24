# ================================================================================
# GRAFICOS EXPLORATORIOS - VIAJES PRESIDENCIALES DE SUDAMERICA (1994-2025)
# Fuente: 04_BASE_FINAL/Base_COLT_Sudamerica.xlsx, hoja "Datos_COLT_Sudamerica"
# ================================================================================
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
#
# Como usar: abrir este archivo en RStudio con el working directory en la
# carpeta que CONTIENE "Base Viaje Presidenciales Latam" (ver README.txt).
# Cada grafico/tabla se guarda como PNG (y algunas tambien como CSV) en
# 08_ANALISIS_R/outputs/.
# ================================================================================

## ---- 0. Setup ----------------------------------------------------------------

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

tema_paper <- function(base_size = 11) {
  theme_minimal(base_size = base_size, base_family = "") +
    theme(
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = gris_1, linewidth = 0.3),
      axis.line = element_line(color = gris_9, linewidth = 0.3),
      axis.ticks = element_line(color = gris_9, linewidth = 0.3),
      strip.background = element_rect(fill = gris_1, color = NA),
      strip.text = element_text(color = "black", face = "bold", size = rel(0.85)),
      plot.title = element_text(face = "bold", size = rel(1.05)),
      plot.subtitle = element_text(color = gris_6, size = rel(0.85)),
      plot.caption = element_text(color = gris_5, size = rel(0.7)),
      legend.position = "bottom",
      legend.title = element_text(size = rel(0.85)),
      panel.background = element_rect(fill = "white", color = NA),
      plot.background = element_rect(fill = "white", color = NA)
    )
}
theme_set(tema_paper())

# Funcion reutilizable para guardar cualquier data.frame como imagen de
# tabla (ademas del CSV), en blanco/negro/grises, sin depender de paquetes
# externos de renderizado web (gt+webshot, etc.) que pueden no estar
# instalados.
guardar_tabla_imagen <- function(df, archivo, titulo = NULL, ancho = 9, alto = NULL) {
  if (is.null(alto)) alto <- 1.2 + 0.32 * (nrow(df) + 1)
  tema_tabla <- gridExtra::ttheme_minimal(
    core = list(bg_params = list(fill = rep(c("white", gris_1), length.out = nrow(df)), col = NA),
                fg_params = list(col = "black", fontsize = 10)),
    colhead = list(bg_params = list(fill = gris_7, col = NA),
                   fg_params = list(col = "white", fontsize = 10, fontface = "bold"))
  )
  tabla_grob <- gridExtra::tableGrob(df, rows = NULL, theme = tema_tabla)
  if (!is.null(titulo)) {
    titulo_grob <- grid::textGrob(titulo, gp = grid::gpar(fontsize = 13, fontface = "bold"), x = 0, hjust = 0)
    tabla_grob <- gridExtra::arrangeGrob(titulo_grob, tabla_grob, ncol = 1, heights = grid::unit(c(0.5, 1), "null"))
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
guardar_tabla_imagen(ficha_general, "00a_ficha_general.png",
                      titulo = paste0("Viajes presidenciales de Sudamerica - Ficha general (", ANIO_DESDE, "-", ANIO_HASTA, ")"),
                      ancho = 7, alto = 3)

# 2.2 Total de viajes por pais (todo el periodo)
viajes_totales_pais <- colt %>%
  count(Pais_ES, name = "n_viajes") %>%
  arrange(desc(n_viajes))

g0b <- ggplot(viajes_totales_pais, aes(x = fct_reorder(Pais_ES, n_viajes), y = n_viajes)) +
  geom_col(fill = gris_6) +
  geom_text(aes(label = n_viajes), hjust = -0.2, size = 3, color = "black") +
  coord_flip(clip = "off") +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(title = "Total de viajes registrados por pais",
       subtitle = paste0(ANIO_DESDE, "-", ANIO_HASTA, ", todos los mandatarios de cada pais"),
       x = NULL, y = "Cantidad de viajes")

print(g0b)
ggsave(file.path(RUTA_OUTPUTS, "00b_viajes_totales_por_pais.png"), g0b, width = 9, height = 6, dpi = 150)
write.csv(viajes_totales_pais, file.path(RUTA_OUTPUTS, "00b_viajes_totales_por_pais.csv"), row.names = FALSE)

# 2.3 Total de viajes por mandatario (todos, ordenados)
viajes_totales_mandatario <- colt %>%
  count(Leader_nombre, LeaderCountryOrIGO, name = "n_viajes") %>%
  arrange(desc(n_viajes))

g0c <- ggplot(viajes_totales_mandatario, aes(x = fct_reorder(Leader_nombre, n_viajes), y = n_viajes)) +
  geom_col(fill = gris_6) +
  coord_flip() +
  labs(title = "Total de viajes registrados por mandatario",
       subtitle = paste0(ANIO_DESDE, "-", ANIO_HASTA),
       x = NULL, y = "Cantidad de viajes")

print(g0c)
ggsave(file.path(RUTA_OUTPUTS, "00c_viajes_totales_por_mandatario.png"), g0c,
       width = 9, height = 2 + 0.16 * nrow(viajes_totales_mandatario), dpi = 150)
write.csv(viajes_totales_mandatario, file.path(RUTA_OUTPUTS, "00c_viajes_totales_por_mandatario.csv"), row.names = FALSE)

# 2.4 Tabla de estadisticos descriptivos (estilo "Tabla 1" de un paper:
#     media/desvio/min/max de viajes por pais-anio y de duracion)
resumen_estadisticos <- bind_rows(
  colt %>% count(Year, LeaderCountryOrIGO, name = "viajes") %>%
    summarise(variable = "Viajes por pais-anio", media = round(mean(viajes), 1), de = round(sd(viajes), 1),
              minimo = min(viajes), maximo = max(viajes), n_obs = n()),
  colt %>% filter(!is.na(TripDuration)) %>%
    summarise(variable = "Duracion del viaje (dias)", media = round(mean(TripDuration), 1), de = round(sd(TripDuration), 1),
              minimo = min(TripDuration), maximo = max(TripDuration), n_obs = n()),
  colt %>% count(Year, LeaderCountryOrIGO, Visit_Category) %>%
    filter(Visit_Category == "Bilateral") %>%
    summarise(variable = "Viajes bilaterales por pais-anio", media = round(mean(n), 1), de = round(sd(n), 1),
              minimo = min(n), maximo = max(n), n_obs = n()),
  colt %>% count(Year, LeaderCountryOrIGO, Visit_Category) %>%
    filter(Visit_Category == "Multilateral") %>%
    summarise(variable = "Viajes multilaterales por pais-anio", media = round(mean(n), 1), de = round(sd(n), 1),
              minimo = min(n), maximo = max(n), n_obs = n())
)
print(resumen_estadisticos)
write.csv(resumen_estadisticos, file.path(RUTA_OUTPUTS, "00d_resumen_estadisticos_descriptivos.csv"), row.names = FALSE)
guardar_tabla_imagen(resumen_estadisticos, "00d_resumen_estadisticos_descriptivos.png",
                      titulo = "Estadisticos descriptivos", ancho = 10, alto = 3)


## ---- 3. Pregunta 1: evolucion general de la cantidad de viajes por anio -------

viajes_por_anio <- colt %>% count(Year, name = "n_viajes")

g1 <- ggplot(viajes_por_anio, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_5) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  labs(
    title = "Cantidad de viajes presidenciales por anio",
    subtitle = paste0("Sudamerica, ", ANIO_DESDE, "-", ANIO_HASTA),
    x = NULL, y = "Cantidad de viajes",
    caption = "Fuente: Base_COLT_Sudamerica.xlsx (PE-Latam)."
  )

print(g1)
ggsave(file.path(RUTA_OUTPUTS, "01_viajes_por_anio.png"), g1, width = 10, height = 6, dpi = 150)

# Por pais: con 12 paises, usar color unico no distingue bien -> se factoriza
# en paneles (facet_wrap), todos en el mismo tono de gris.
viajes_por_anio_pais <- colt %>% count(Year, Pais_ES, name = "n_viajes")

g1b <- ggplot(viajes_por_anio_pais, aes(x = Year, y = n_viajes)) +
  geom_col(fill = gris_5) +
  facet_wrap(~Pais_ES, ncol = 3) +
  labs(title = "Cantidad de viajes por anio, por pais", x = NULL, y = "Cantidad de viajes")

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

g2 <- ggplot(region_por_periodo, aes(x = factor(Periodo5), y = participacion, fill = RegionVisited)) +
  geom_col(position = "stack", color = "white", linewidth = 0.2) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_manual(values = grises_regiones) +
  labs(
    title = "Prioridad regional de los viajes presidenciales, por periodo",
    subtitle = "Participacion (%) de cada region sobre el total de viajes del periodo",
    x = "Periodo (bloques de 5 anios)", y = "Participacion", fill = "Region de destino"
  ) +
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
  labs(title = "Prioridad regional de los viajes presidenciales, por anio",
       x = NULL, y = "Participacion", fill = "Region de destino")

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
  labs(title = "Duracion promedio de los viajes presidenciales, por anio",
       x = NULL, y = "Duracion promedio (dias)")

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
  labs(title = "Cantidad de viajes y duracion promedio, por anio",
       subtitle = "Barras = cantidad total de viajes (eje izquierdo). Linea = duracion promedio en dias (eje derecho).",
       x = NULL)

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
  labs(
    title = "Bilateral vs. Multilateral vs. Otro, participacion por anio",
    subtitle = "\"Otro\" = sin reunion registrada con el anfitrion ni asistencia a un evento multilateral (p. ej. actos protocolares, ceremonias, escalas sin agenda bilateral)",
    x = NULL, y = "Participacion", fill = "Categoria de visita (derivada)"
  )

print(g4)
ggsave(file.path(RUTA_OUTPUTS, "04_categoria_visita_por_anio.png"), g4, width = 11, height = 6.5, dpi = 150)

g4b <- ggplot(colt %>% count(Year, Visit_Category), aes(x = Year, y = n, color = Visit_Category, linetype = Visit_Category)) +
  geom_line(linewidth = 0.9) +
  geom_point(size = 1.2) +
  scale_color_manual(values = colores_categoria) +
  scale_linetype_manual(values = c("Bilateral" = "solid", "Multilateral" = "dashed",
                                    "Other" = "dotted", "Sin dato" = "dotdash")) +
  labs(title = "Cantidad absoluta de viajes por categoria, por anio",
       subtitle = "\"Otro\" = sin reunion registrada con el anfitrion ni asistencia a un evento multilateral",
       x = NULL, y = "Cantidad de viajes", color = "Categoria de visita (derivada)",
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
    filter(Leader_nombre == nombre_mandatario) %>%
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
    labs(title = paste("Destinos mas visitados -", nombre_mandatario), x = NULL, y = "Cantidad de viajes")

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

# 7b) Vista agregada: el destino #1 de CADA mandatario, todos juntos.
destino_favorito_por_presidente <- colt %>%
  count(Leader_nombre, LeaderCountryOrIGO, CountryVisited, name = "n_viajes") %>%
  group_by(Leader_nombre) %>%
  slice_max(n_viajes, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  arrange(LeaderCountryOrIGO, desc(n_viajes))

g5 <- ggplot(destino_favorito_por_presidente,
             aes(x = fct_reorder(Leader_nombre, n_viajes), y = n_viajes)) +
  geom_col(fill = gris_6) +
  geom_text(aes(label = CountryVisited), hjust = -0.05, size = 2.8, color = "black") +
  facet_wrap(~LeaderCountryOrIGO, scales = "free_y", ncol = 3) +
  coord_flip(clip = "off") +
  scale_y_continuous(expand = expansion(mult = c(0.02, 0.35))) +
  labs(title = "Destino mas visitado por cada mandatario",
       subtitle = "Cantidad de viajes al destino #1 de cada presidente, agrupado por pais de origen",
       x = NULL, y = "Cantidad de viajes a ese destino")

print(g5)
ggsave(file.path(RUTA_OUTPUTS, "05b_destino_favorito_todos_los_presidentes.png"), g5,
       width = 12, height = ceiling(n_distinct(colt$Leader_key) / 3) * 1.1 + 3, dpi = 150)

top5_por_presidente <- colt %>%
  count(Leader_nombre, CountryVisited, name = "n_viajes") %>%
  group_by(Leader_nombre) %>%
  slice_max(n_viajes, n = 5, with_ties = FALSE) %>%
  arrange(Leader_nombre, desc(n_viajes)) %>%
  ungroup()

write.csv(top5_por_presidente, file.path(RUTA_OUTPUTS, "05_top5_destinos_por_presidente.csv"), row.names = FALSE)


## ---- 8. Pregunta 7: la primera visita de cada mandatario, a que pais fue? ----

primera_visita <- colt %>%
  filter(!is.na(TripStartDate)) %>%
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
  labs(title = "Pais elegido como primer viaje al exterior del mandato",
       subtitle = paste0("Cuantas veces cada pais fue el destino del primer viaje presidencial (",
                          n_distinct(colt$Leader_key), " mandatos, ", ANIO_DESDE, "-", ANIO_HASTA, ")"),
       x = NULL, y = "Cantidad de mandatarios")

print(g6)
ggsave(file.path(RUTA_OUTPUTS, "06_primeros_destinos_frecuencia.png"), g6, width = 9, height = 7, dpi = 150)


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
  labs(title = "En que meses se concentran los viajes presidenciales",
       subtitle = "Mes de inicio del viaje, todos los mandatarios y anios juntos",
       x = NULL, y = "Cantidad de viajes")

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
  labs(title = "Los 20 destinos bilaterales mas visitados",
       subtitle = paste0("Viajes con reunion registrada con el anfitrion (MetHostHoGS = Yes), ", ANIO_DESDE, "-", ANIO_HASTA),
       x = NULL, y = "Cantidad de viajes bilaterales")

print(g9a)
ggsave(file.path(RUTA_OUTPUTS, "09a_ranking_destinos_bilaterales.png"), g9a, width = 9, height = 8, dpi = 150)

top20_multilateral <- colt %>%
  filter(Visit_Category == "Multilateral") %>%
  count(CountryVisited, name = "n_viajes") %>%
  slice_max(n_viajes, n = 20) %>%
  mutate(CountryVisited = fct_reorder(CountryVisited, n_viajes))

g9b <- ggplot(top20_multilateral, aes(x = CountryVisited, y = n_viajes)) +
  geom_col(fill = gris_5) +
  coord_flip() +
  labs(title = "Los 20 destinos multilaterales mas visitados",
       subtitle = paste0("Viajes con asistencia a un evento multilateral (AttendedMultilatEvent = Yes), ", ANIO_DESDE, "-", ANIO_HASTA),
       x = NULL, y = "Cantidad de viajes multilaterales")

print(g9b)
ggsave(file.path(RUTA_OUTPUTS, "09b_ranking_destinos_multilaterales.png"), g9b, width = 9, height = 8, dpi = 150)


## ---- 10. Resumen final en consola ----------------------------------------------

cat("\n================================================================\n")
cat("Graficos y tablas guardados en:", RUTA_OUTPUTS, "\n")
cat("================================================================\n")
cat("00a_ficha_general.png                          -> Descriptivos: ficha general\n")
cat("00b_viajes_totales_por_pais.png/.csv            -> Descriptivos: total de viajes por pais\n")
cat("00c_viajes_totales_por_mandatario.png/.csv       -> Descriptivos: total de viajes por mandatario\n")
cat("00d_resumen_estadisticos_descriptivos.png/.csv   -> Descriptivos: tabla tipo 'Tabla 1' de un paper\n")
cat("01_viajes_por_anio.png / 01b_...pais.png        -> Pregunta 1 (evolucion general)\n")
cat("02_regiones_por_periodo.png / 02b_...area.png   -> Pregunta 2 (prioridad regional)\n")
cat("03_duracion_por_anio.png                        -> Pregunta 3 (duracion)\n")
cat("03c_viajes_y_duracion_combinado.png             -> Preguntas 1+3 combinadas (viajes y duracion)\n")
cat("04_categoria_visita_por_anio.png / 04b_...      -> Preguntas 4 y 5 (bi/multi/otro)\n")
cat("05_top5_destinos_por_presidente.csv             -> Pregunta 6 (tabla completa)\n")
cat("05b_destino_favorito_todos_los_presidentes.png  -> Pregunta 6 (resumen visual)\n")
cat("   (usar graficar_top_destinos(\"Nombre\") para el detalle de un presidente puntual)\n")
cat("06_primera_visita_por_presidente.csv            -> Pregunta 7 (tabla completa)\n")
cat("06_primeros_destinos_frecuencia.png             -> Pregunta 7 (que paises se repiten)\n")
cat("08_estacionalidad_mensual.png                   -> Extension: meses con mas viajes\n")
cat("09a_ranking_destinos_bilaterales.png            -> Extension: top 20 destinos bilaterales\n")
cat("09b_ranking_destinos_multilaterales.png         -> Extension: top 20 destinos multilaterales\n")
