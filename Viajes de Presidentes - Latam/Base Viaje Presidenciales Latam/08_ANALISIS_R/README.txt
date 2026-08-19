================================================================================
08_ANALISIS_R — Graficos exploratorios en R / RStudio
================================================================================

QUE ES
  graficos_exploratorios.R: script que lee 04_BASE_FINAL/Base_COLT_Sudamerica.xlsx
  (hoja "Datos_COLT_Sudamerica") y genera los graficos/tablas para las
  preguntas de investigacion centrales del proyecto (ver encabezado del
  script para el detalle de cada pregunta):

  1) Evolucion general de la cantidad de viajes en el tiempo
  2) Que regiones se priorizan en cada epoca
  3) Cambios en la duracion de los viajes
  4-5) Bilateral vs. Multilateral vs. Otro: participacion y volumen en el tiempo
  6) Destinos preferidos por cada mandatario
  7) Primera visita de cada mandatario (a que pais)

  Version 2 (2026-08-19): antes este script leia 04_BASE_FINAL/base_consolidada.csv
  (nuestro esquema propio de 31 columnas, 5 paises, 2000+ salvo Argentina).
  Ahora lee directamente la planilla COLT (76 columnas, 12 paises, con
  cobertura nativa desde ~1994 segun el pais), que da mejor cobertura
  temporal sin esperar a que terminemos de verificar/enriquecer cada anio.

  Que se gana / que se pierde con este cambio:
  - (+) Mas anios de cobertura para Brasil y Chile: el dato nativo de COLT
    para 1994-1999 ya esta cargado en esta hoja, aunque todavia NO fue
    verificado/enriquecido por nosotros (tareas pendientes #91 y #92 de la
    bitacora). Esos anios se muestran "tal cual" los carga COLT.
  - (+) Quedan disponibles los otros 7 paises sudamericanos de COLT
    (Bolivia, Colombia, Ecuador, Guyana, Peru, Suriname, Venezuela) por si
    se quiere ampliar el analisis mas alla de los 5 paises foco — ver
    PAISES_FOCO al inicio del script para cambiar el filtro.
  - (-) COLT no tiene una columna "Visit_Category" (Bilateral/Multilateral/
    Other) como nuestro esquema propio; el script la DERIVA a partir de
    AttendedMultilatEvent + MetHostHoGS (ver seccion 1.3 del script — es
    una decision metodologica nuestra, no un dato nativo de COLT).
  - (-) No hay equivalente a Trip_Status: todas las filas de esta hoja son
    viajes concretados (los cancelados estan en la hoja aparte
    "Viajes_Cancelados", que este script no usa).

COMO CORRERLO
  1. Abrir RStudio.
  2. Setear el working directory en la carpeta que CONTIENE el proyecto,
     es decir un nivel arriba de "Base Viaje Presidenciales Latam"
     (la carpeta "PE-Latam" o donde la tengan sincronizada). El script arma
     las rutas como "Base Viaje Presidenciales Latam/04_BASE_FINAL/...",
     siguiendo el mismo formato que usaron para cargar los datos:
       library(readxl)
       Base_COLT_Sudamerica <- read_excel("Base Viaje Presidenciales Latam/04_BASE_FINAL/Base_COLT_Sudamerica.xlsx",
           sheet = "Datos_COLT_Sudamerica")
     Si el working directory esta en otro nivel, ajustar RUTA_EXCEL y
     RUTA_OUTPUTS al principio del script.
  3. Abrir 08_ANALISIS_R/graficos_exploratorios.R y correrlo entero
     (Source, o Ctrl+Shift+Enter / Cmd+Shift+Enter).
  4. La primera vez va a instalar automaticamente los paquetes que falten
     (readxl, dplyr, ggplot2, lubridate, scales, forcats, tidyr, stringr) -
     todos son parte del tidyverse estandar (mas readxl).
  5. Los graficos se muestran en el panel de Plots de RStudio Y ADEMAS se
     guardan como PNG (mas 2 tablas CSV) en 08_ANALISIS_R/outputs/.

FUNCION REUTILIZABLE
  graficar_top_destinos("Nombre del Presidente", top_n = 10)
  Genera y guarda el grafico de destinos mas visitados de CUALQUIER
  mandatario de la base. Usar el nombre CON tilde tal como aparece en la
  columna Leader_nombre (version normalizada que arma el script — ver nota
  sobre tildes mas abajo). Para ver los nombres disponibles:
    sort(unique(colt$Leader_nombre))
  Ejemplos ya comentados dentro del script.

NOTA METODOLOGICA — NOMBRES CON/SIN TILDE
  La columna LeaderFullName de la planilla mezcla dos convenciones: las
  filas nativas de COLT vienen sin tilde ("Alberto Fernandez", "Cristina
  Fernandez de Kirchner") y las filas que agregamos nosotros (PELATAM)
  vienen con tilde en espaniol ("Alberto Fernández", "Cristina Fernández
  de Kirchner"). Sin corregir esto, cualquier agrupacion por presidente
  (destinos preferidos, primera visita) cuenta a la misma persona dos
  veces. El script arma una clave interna sin tildes (Leader_key) para
  agrupar correctamente, y elige como etiqueta visible (Leader_nombre) la
  version mas frecuente de cada grupo. No hace falta tocar nada a mano,
  pero si agregan un presidente nuevo a la base conviene revisar que las
  dos grafias no queden como "personas" separadas en los graficos de
  destinos/primera visita.

NOTA METODOLOGICA — VISIT_CATEGORY DERIVADA
  Bilateral/Multilateral/Other no es un dato que traiga COLT: se
  construye con esta regla (ver seccion 1.3 del script):
    Multilateral   si AttendedMultilatEvent == "Yes"  (tiene prioridad)
    Bilateral      si no es Multilateral y MetHostHoGS == "Yes"
    Other          si no es Multilateral y MetHostHoGS == "No"
    Sin dato       si MetHostHoGS esta vacio
  Es una decision metodologica del proyecto, no un campo nativo de COLT —
  si se quiere otro criterio (por ejemplo dar prioridad a MetHostHoGS por
  sobre AttendedMultilatEvent), cambiar el case_when correspondiente.

  Este script fue escrito y revisado sin poder ejecutar R en el entorno
  donde se genero (sandbox sin R instalado y sin acceso a CRAN) — se
  verifico la logica de cada agregacion explorando la planilla con Python/
  pandas y openpyxl para confirmar tipos de columna y valores, pero la
  sintaxis de R en si no se corrio antes de entregarla. Los puntos con mas
  riesgo de un error puntual al correrlo en RStudio son:
    - TripStartDate/TripEndDate: la columna tiene tipos mezclados (texto
      ISO y fechas nativas de Excel segun la fila) — el script ya maneja
      esto pasando todo a texto y parseando los primeros 10 caracteres,
      pero si aparece algun formato de fecha no previsto puede dar NA.
    - TripDuration: tambien mezcla texto y numero en distintas filas.
  Si algo tira error, probablemente sea algo menor (nombre de argumento,
  version de paquete, algun caso de fecha no previsto) — avisen y se
  corrige al toque.

PROXIMOS PASOS SUGERIDOS (no incluidos todavia)
  - Desagregar alguna pregunta por Visit_Subtype si en algun momento se
    agrega esa columna al esquema COLT (hoy no existe como tal en la
    planilla; lo mas cercano es AttendedMultilatEvent).
  - Cruzar duracion de viaje con Visit_Category (los multilaterales duran
    distinto que los bilaterales?).
  - Cuando se verifiquen/enriquezcan Brasil y Chile 1994-1999 (tareas
    pendientes #91/#92, ver 05_BITACORA/PENDIENTES_VERIFICACION.txt),
    re-correr este script — los datos nativos de COLT para esos anios ya
    estan en la planilla, asi que los graficos de "evolucion en el
    tiempo" YA arrancan en 1994 para esos 2 paises, pero con menor nivel
    de verificacion que el resto de la base hasta que se complete esa tarea.
  - Ampliar PAISES_FOCO al resto de Sudamerica (Bolivia, Colombia, Ecuador,
    Guyana, Peru, Suriname, Venezuela) si se quiere un analisis regional
    mas amplio — la planilla ya tiene esos datos cargados.
================================================================================
