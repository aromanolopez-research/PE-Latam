# ================================================================================
# GRAFICOS EXPLORATORIOS - VIAJES PRESIDENCIALES DE AMERICA
# Fuente: 04_BASE_FINAL/Base_COLT_Sudamerica.xlsx, hoja "Datos_COLT_Sudamerica"
# ================================================================================
# Version 2 (2026-08-19): reemplaza la version anterior basada en
# base_consolidada.csv. Ahora usa directamente la hoja COLT+PE-Latam, que
# tiene mejor cobertura temporal (COLT nativo llega hasta 1990-1994 segun el
# pais, mientras nuestra base propia recien arranca en 2000 salvo Argentina).
#
# OJO - lo que se gana y lo que se pierde al cambiar de fuente:
#   (+) Mas anios de cobertura para Brasil y Chile (COLT nativo 1994-1999
#       esta presente en esta hoja aunque TODAVIA no lo verificamos/
#       enriquecimos nosotros -tareas pendientes #91/#92 de la bitacora-,
#       asi que esos anios son "tal cual los carga COLT", no con el mismo
#       nivel de revision que 2000+).
#   (+) Incluye los otros 7 paises sudamericanos que COLT cubre (Bolivia,
#       Colombia, Ecuador, Guyana, Peru, Suriname, Venezuela) por si en
#       algun momento se quiere comparar mas alla de los 5 paises foco.
#   (-) No existe una columna "Visit_Category" (Bilateral/Multilateral/
#       Other) como en nuestro propio esquema; se DERIVA mas abajo a partir
#       de AttendedMultilatEvent + MetHostHoGS (ver seccion 1.3, esta
#       derivacion es una decision metodologica nuestra, no viene de COLT).
#   (-) No tiene un equivalente a Trip_Status (Completed/Canceled): todas
#       las filas de esta hoja son viajes que se concretaron.
#
# Preguntas que este script responde (una seccion por pregunta):
#   1) Como cambio en general la cantidad/ritmo de viajes a lo largo del tiempo?
#   2) Que regiones se priorizan en cada epoca?
#   3) Cambio la duracion de los viajes?
#   4) Los viajes "Other" (ni bilateral ni multilateral) estan aumentando?
#   5) Aumentaron los viajes Bilaterales o los Multilaterales?
#   6) Que destinos prefiere cada mandatario?
#   7) La primera visita de cada mandatario, a que pais fue?
#
# Como usar: abrir este archivo en RStudio con el working directory en la raiz
# del proyecto ("Base Viaje Presidenciales Latam"), o ajustar RUTA_EXCEL abajo.
# Cada grafico se guarda como PNG en 08_ANALISIS_R/outputs/.
# ================================================================================

## ---- 0. Setup ----------------------------------------------------------------

paquetes <- c("readxl", "dplyr", "ggplot2", "lubridate", "scales", "forcats", "tidyr", "stringr")
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

RUTA_EXCEL   <- "Base Viaje Presidenciales Latam/04_BASE_FINAL/Base_COLT_Sudamerica.xlsx"
RUTA_OUTPUTS <- "Base Viaje Presidenciales Latam/08_ANALISIS_R/outputs"
dir.create(RUTA_OUTPUTS, showWarnings = FALSE, recursive = TRUE)

# Paises foco del proyecto (LeaderCountryOrIGO usa nombres en ingles en COLT).
# Cambiar/ampliar este vector si se quiere incluir el resto de Sudamerica
# (Bolivia, Colombia, Ecuador, Guyana, Peru, Suriname, Venezuela).
PAISES_FOCO <- c("Argentina", "Brazil", "Chile", "Paraguay", "Uruguay")

paleta_paises <- c(
  "Argentina" = "#6FA8DC",
  "Brazil"    = "#93C47D",
  "Chile"     = "#E06666",
  "Paraguay"  = "#FFD966",
  "Uruguay"   = "#8E7CC3"
)

# Etiquetas en espaniol solo para mostrar en los graficos (el filtro/join
# interno sigue usando el nombre en ingles, que es el que trae la planilla)
etiquetas_es <- c("Argentina" = "Argentina", "Brazil" = "Brasil", "Chile" = "Chile",
                   "Paraguay" = "Paraguay", "Uruguay" = "Uruguay")


## ---- 1. Carga y preparacion de datos ------------------------------------------

colt_raw <- read_excel(RUTA_EXCEL, sheet = "Datos_COLT_Sudamerica")

# 1.1 Normalizar fechas: la columna llega con tipos mezclados (texto ISO con
#     "T00:00:00", texto ISO simple, y algunas fechas nativas de Excel) porque
#     se fue editando con distintas herramientas a lo largo del proyecto. La
#     forma robusta de manejarlo, sin importar que tipo trajo readxl: pasar
#     todo a texto y quedarse con los primeros 10 caracteres (YYYY-MM-DD).
parsear_fecha <- function(x) {
  x_txt <- as.character(x)
  ymd(substr(x_txt, 1, 10))
}

# 1.2 Normalizar nombres de mandatario: COLT trae versiones sin tilde
#     ("Alberto Fernandez") y nuestras propias filas agregadas (PELATAM)
#     traen version con tilde ("Alberto Fernández") -> sin normalizar,
#     cualquier agrupacion por presidente los cuenta como 2 personas
#     distintas. Se arma una clave sin tildes para agrupar, y se elige como
#     etiqueta la version mas frecuente de cada grupo.
quitar_tildes <- function(x) {
  iconv(x, from = "UTF-8", to = "ASCII//TRANSLIT")
}

colt <- colt_raw %>%
  filter(LeaderCountryOrIGO %in% PAISES_FOCO) %>%
  mutate(
    TripStartDate = parsear_fecha(TripStartDate),
    TripEndDate   = parsear_fecha(TripEndDate),
    TripDuration  = as.numeric(as.character(TripDuration)),
    Year          = year(TripStartDate),
    Periodo5      = (Year %/% 5) * 5,
    Pais_ES       = recode(LeaderCountryOrIGO, !!!etiquetas_es),
    Leader_key    = str_to_lower(quitar_tildes(LeaderFullName))
  )

# Etiqueta canonica por mandatario: la version (con tilde) mas frecuente
# dentro de cada Leader_key
etiqueta_por_leader <- colt %>%
  count(Leader_key, LeaderFullName, sort = TRUE) %>%
  group_by(Leader_key) %>%
  slice_max(n, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  select(Leader_key, Leader_nombre = LeaderFullName)

colt <- colt %>%
  left_join(etiqueta_por_leader, by = "Leader_key")

cat("Filas cargadas (paises foco):", nrow(colt),
    "| Rango de anios:", min(colt$Year, na.rm = TRUE), "-", max(colt$Year, na.rm = TRUE),
    "| Mandatarios distintos:", n_distinct(colt$Leader_key), "\n")

# 1.3 Derivar categoria de visita (Bilateral / Multilateral / Other / Sin dato)
#     NO es una columna nativa de COLT -es una construccion propia, ver nota
#     al inicio del script-. Multilateral tiene prioridad si se dan ambas
#     condiciones a la vez (ej. cumbre + reunion bilateral al margen).
colt <- colt %>%
  mutate(
    Visit_Category = case_when(
      AttendedMultilatEvent == "Yes" ~ "Multilateral",
      MetHostHoGS == "Yes" ~ "Bilateral",
      MetHostHoGS == "No" ~ "Other",
      TRUE ~ "Sin dato"
    )
  )


## ---- 2. Pregunta 1: evolucion general de la cantidad de viajes por anio -------

viajes_por_anio <- colt %>% count(Year, name = "n_viajes")

g1 <- ggplot(viajes_por_anio, aes(x = Year, y = n_viajes)) +
  geom_col(fill = "#4A86C8", alpha = 0.85) +
  geom_smooth(se = FALSE, color = "#B33951", linewidth = 1, method = "loess", span = 0.35) +
  scale_x_continuous(breaks = scales::breaks_pretty(n = 10)) +
  labs(
    title = "Cantidad de viajes presidenciales por anio",
    subtitle = paste("Paises:", paste(etiquetas_es[PAISES_FOCO], collapse = ", ")),
    x = NULL, y = "Cantidad de viajes",
    caption = "Fuente: Base_COLT_Sudamerica.xlsx (PE-Latam). Linea: tendencia suavizada (loess)."
  ) +
  theme_minimal(base_size = 12)

print(g1)
ggsave(file.path(RUTA_OUTPUTS, "01_viajes_por_anio.png"), g1, width = 10, height = 6, dpi = 150)

viajes_por_anio_pais <- colt %>% count(Year, Pais_ES, name = "n_viajes")

g1b <- ggplot(viajes_por_anio_pais, aes(x = Year, y = n_viajes, color = Pais_ES)) +
  geom_line(linewidth = 0.9) +
  geom_point(size = 1.2, alpha = 0.7) +
  scale_color_manual(values = setNames(paleta_paises, etiquetas_es[names(paleta_paises)])) +
  labs(title = "Cantidad de viajes por anio, por pais", x = NULL, y = "Cantidad de viajes", color = "Pais") +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom")

print(g1b)
ggsave(file.path(RUTA_OUTPUTS, "01b_viajes_por_anio_por_pais.png"), g1b, width = 10, height = 6, dpi = 150)


## ---- 3. Pregunta 2: que regiones se priorizan en cada epoca? -----------------

region_por_periodo <- colt %>%
  filter(!is.na(RegionVisited)) %>%
  count(Periodo5, RegionVisited) %>%
  group_by(Periodo5) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

g2 <- ggplot(region_por_periodo, aes(x = factor(Periodo5), y = participacion, fill = RegionVisited)) +
  geom_col(position = "stack") +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_brewer(palette = "Set3") +
  labs(
    title = "Prioridad regional de los viajes presidenciales, por periodo",
    subtitle = "Participacion (%) de cada region sobre el total de viajes del periodo",
    x = "Periodo (bloques de 5 anios)", y = "Participacion", fill = "Region de destino"
  ) +
  theme_minimal(base_size = 12) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), legend.position = "right")

print(g2)
ggsave(file.path(RUTA_OUTPUTS, "02_regiones_por_periodo.png"), g2, width = 11, height = 6.5, dpi = 150)

region_por_anio <- colt %>%
  filter(!is.na(RegionVisited)) %>%
  count(Year, RegionVisited) %>%
  group_by(Year) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

g2b <- ggplot(region_por_anio, aes(x = Year, y = participacion, fill = RegionVisited)) +
  geom_area(position = "fill", alpha = 0.9) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_brewer(palette = "Set3") +
  labs(title = "Prioridad regional de los viajes presidenciales, por anio",
       x = NULL, y = "Participacion", fill = "Region de destino") +
  theme_minimal(base_size = 12)

print(g2b)
ggsave(file.path(RUTA_OUTPUTS, "02b_regiones_por_anio_area.png"), g2b, width = 11, height = 6.5, dpi = 150)


## ---- 4. Pregunta 3: cambio la duracion de los viajes? ------------------------

duracion_por_anio <- colt %>%
  filter(!is.na(TripDuration)) %>%
  group_by(Year) %>%
  summarise(duracion_media = mean(TripDuration), duracion_mediana = median(TripDuration), n = n())

g3 <- ggplot(duracion_por_anio, aes(x = Year, y = duracion_media)) +
  geom_line(color = "#4A86C8", linewidth = 1) +
  geom_point(color = "#4A86C8", size = 1.5) +
  geom_smooth(se = FALSE, color = "#B33951", linetype = "dashed", method = "loess", span = 0.35) +
  labs(title = "Duracion promedio de los viajes presidenciales, por anio",
       x = NULL, y = "Duracion promedio (dias)",
       caption = "Linea punteada: tendencia suavizada (loess).") +
  theme_minimal(base_size = 12)

print(g3)
ggsave(file.path(RUTA_OUTPUTS, "03_duracion_por_anio.png"), g3, width = 10, height = 6, dpi = 150)

g3b <- ggplot(colt %>% filter(!is.na(TripDuration), TripDuration <= 21),
              aes(x = factor(Periodo5), y = TripDuration)) +
  geom_boxplot(fill = "#93C47D", alpha = 0.7, outlier.alpha = 0.3) +
  labs(title = "Distribucion de la duracion de los viajes, por periodo",
       subtitle = "Excluye outliers > 21 dias (giras extraordinarias) para legibilidad",
       x = "Periodo (bloques de 5 anios)", y = "Duracion (dias)") +
  theme_minimal(base_size = 12) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

print(g3b)
ggsave(file.path(RUTA_OUTPUTS, "03b_duracion_boxplot_periodo.png"), g3b, width = 10, height = 6, dpi = 150)


## ---- 5. Preguntas 4 y 5: Bilateral vs Multilateral vs Other, en el tiempo -----

categoria_por_anio <- colt %>%
  count(Year, Visit_Category) %>%
  group_by(Year) %>%
  mutate(participacion = n / sum(n)) %>%
  ungroup()

colores_categoria <- c("Bilateral" = "#4A86C8", "Multilateral" = "#E06666",
                        "Other" = "#B7B7B7", "Sin dato" = "#444444")

g4 <- ggplot(categoria_por_anio, aes(x = Year, y = participacion, fill = Visit_Category)) +
  geom_area(position = "fill", alpha = 0.9) +
  scale_y_continuous(labels = scales::percent_format()) +
  scale_fill_manual(values = colores_categoria) +
  labs(
    title = "Bilateral vs. Multilateral vs. Otro, participacion por anio",
    subtitle = "Otro = ni bilateral (no se reunio con el anfitrion) ni multilateral (cumbre/foro). Derivado de MetHostHoGS + AttendedMultilatEvent.",
    x = NULL, y = "Participacion", fill = "Categoria de visita (derivada)"
  ) +
  theme_minimal(base_size = 12)

print(g4)
ggsave(file.path(RUTA_OUTPUTS, "04_categoria_visita_por_anio.png"), g4, width = 11, height = 6.5, dpi = 150)

g4b <- ggplot(colt %>% count(Year, Visit_Category), aes(x = Year, y = n, color = Visit_Category)) +
  geom_line(linewidth = 1) +
  geom_point(size = 1.3) +
  scale_color_manual(values = colores_categoria) +
  labs(title = "Cantidad absoluta de viajes por categoria, por anio",
       x = NULL, y = "Cantidad de viajes", color = "Categoria de visita (derivada)") +
  theme_minimal(base_size = 12)

print(g4b)
ggsave(file.path(RUTA_OUTPUTS, "04b_categoria_visita_absoluto.png"), g4b, width = 10, height = 6, dpi = 150)


## ---- 6. Pregunta 6: que destinos prefiere cada mandatario? -------------------

# 6a) Funcion reutilizable: top N destinos de un mandatario especifico.
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
    geom_col(fill = "#6FA8DC") +
    coord_flip() +
    labs(title = paste("Destinos mas visitados -", nombre_mandatario), x = NULL, y = "Cantidad de viajes") +
    theme_minimal(base_size = 12)

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

# 6b) Vista agregada: el destino #1 de CADA mandatario, todos juntos ------------
destino_favorito_por_presidente <- colt %>%
  count(Leader_nombre, LeaderCountryOrIGO, CountryVisited, name = "n_viajes") %>%
  group_by(Leader_nombre) %>%
  slice_max(n_viajes, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  arrange(LeaderCountryOrIGO, desc(n_viajes))

g5 <- ggplot(destino_favorito_por_presidente,
             aes(x = fct_reorder(Leader_nombre, n_viajes), y = n_viajes, fill = LeaderCountryOrIGO)) +
  geom_col() +
  geom_text(aes(label = CountryVisited), hjust = -0.05, size = 3) +
  coord_flip(clip = "off") +
  scale_fill_manual(values = paleta_paises) +
  scale_y_continuous(expand = expansion(mult = c(0.02, 0.25))) +
  labs(title = "Destino mas visitado por cada mandatario",
       subtitle = "Cantidad de viajes al destino #1 de cada presidente",
       x = NULL, y = "Cantidad de viajes a ese destino", fill = "Pais") +
  theme_minimal(base_size = 11) +
  theme(legend.position = "bottom")

print(g5)
ggsave(file.path(RUTA_OUTPUTS, "05b_destino_favorito_todos_los_presidentes.png"), g5, width = 9, height = 12, dpi = 150)

top5_por_presidente <- colt %>%
  count(Leader_nombre, CountryVisited, name = "n_viajes") %>%
  group_by(Leader_nombre) %>%
  slice_max(n_viajes, n = 5, with_ties = FALSE) %>%
  arrange(Leader_nombre, desc(n_viajes)) %>%
  ungroup()

write.csv(top5_por_presidente, file.path(RUTA_OUTPUTS, "05_top5_destinos_por_presidente.csv"), row.names = FALSE)


## ---- 7. Pregunta 7: la primera visita de cada mandatario, a que pais fue? ----

primera_visita <- colt %>%
  filter(!is.na(TripStartDate)) %>%
  group_by(Leader_nombre) %>%
  slice_min(TripStartDate, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  select(Leader_nombre, LeaderCountryOrIGO, TripStartDate, CountryVisited, CityVisited, Visit_Category) %>%
  arrange(TripStartDate)

write.csv(primera_visita, file.path(RUTA_OUTPUTS, "06_primera_visita_por_presidente.csv"), row.names = FALSE)

primeros_destinos_frecuencia <- primera_visita %>%
  count(CountryVisited, name = "veces_elegido") %>%
  mutate(CountryVisited = fct_reorder(CountryVisited, veces_elegido))

g6 <- ggplot(primeros_destinos_frecuencia, aes(x = CountryVisited, y = veces_elegido)) +
  geom_col(fill = "#B33951") +
  coord_flip() +
  scale_y_continuous(breaks = scales::breaks_pretty()) +
  labs(title = "Pais elegido como primer viaje al exterior del mandato",
       subtitle = paste("Cuantas veces cada pais fue el destino del primer viaje presidencial (",
                         n_distinct(colt$Leader_key), " mandatos)", sep = ""),
       x = NULL, y = "Cantidad de mandatarios") +
  theme_minimal(base_size = 12)

print(g6)
ggsave(file.path(RUTA_OUTPUTS, "06_primeros_destinos_frecuencia.png"), g6, width = 9, height = 7, dpi = 150)

g6b <- ggplot(primera_visita,
              aes(x = TripStartDate, y = fct_reorder(Leader_nombre, TripStartDate), color = LeaderCountryOrIGO)) +
  geom_point(size = 2.5) +
  geom_text(aes(label = CountryVisited), hjust = -0.1, size = 2.8, show.legend = FALSE) +
  scale_color_manual(values = paleta_paises) +
  scale_x_date(date_breaks = "2 years", date_labels = "%Y") +
  labs(title = "Primer viaje de cada mandatario, en orden cronologico", x = NULL, y = NULL, color = "Pais") +
  theme_minimal(base_size = 10) +
  theme(legend.position = "bottom")

print(g6b)
ggsave(file.path(RUTA_OUTPUTS, "06b_primera_visita_linea_tiempo.png"), g6b, width = 10, height = 12, dpi = 150)


## ---- 8. Resumen final en consola ----------------------------------------------

cat("\n================================================================\n")
cat("Graficos y tablas guardados en:", RUTA_OUTPUTS, "\n")
cat("================================================================\n")
cat("01_viajes_por_anio.png / 01b_...pais.png       -> Pregunta 1 (evolucion general)\n")
cat("02_regiones_por_periodo.png / 02b_...area.png  -> Pregunta 2 (prioridad regional)\n")
cat("03_duracion_por_anio.png / 03b_...boxplot.png  -> Pregunta 3 (duracion)\n")
cat("04_categoria_visita_por_anio.png / 04b_...     -> Preguntas 4 y 5 (bi/multi/otro)\n")
cat("05_top5_destinos_por_presidente.csv            -> Pregunta 6 (tabla completa)\n")
cat("05b_destino_favorito_todos_los_presidentes.png -> Pregunta 6 (resumen visual)\n")
cat("   (usar graficar_top_destinos(\"Nombre\") para el detalle de un presidente puntual)\n")
cat("06_primera_visita_por_presidente.csv           -> Pregunta 7 (tabla completa)\n")
cat("06_primeros_destinos_frecuencia.png            -> Pregunta 7 (que paises se repiten)\n")
cat("06b_primera_visita_linea_tiempo.png             -> Pregunta 7 (linea de tiempo)\n")
