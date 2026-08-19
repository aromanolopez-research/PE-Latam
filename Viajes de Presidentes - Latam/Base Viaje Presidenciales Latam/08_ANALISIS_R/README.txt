================================================================================
08_ANALISIS_R — Graficos exploratorios en R / RStudio
================================================================================

QUE ES
  graficos_exploratorios.R: script que lee 04_BASE_FINAL/Base_COLT_Sudamerica.xlsx
  (hoja "Datos_COLT_Sudamerica") y genera los graficos/tablas para las
  preguntas de investigacion centrales del proyecto, mas una seccion
  descriptiva al principio y algunas extensiones inspiradas en la
  bibliografia del proyecto (carpeta /Bib).

  Version 4 (2026-08-19) — cambios respecto a la version anterior:
  - Ventana temporal: 1994-2025. Se deja 2026 afuera a proposito (todavia
    no esta tan mapeado/verificado como el resto de la base) — cuando se
    complete, alcanza con subir ANIO_HASTA al principio del script.
  - Nueva seccion 2 "Descriptivos generales" al principio del script:
    ficha resumen, total de viajes por pais, total de viajes por
    mandatario, y la tabla de estadisticos descriptivos — todo se guarda
    tambien como imagen PNG (antes solo CSV/consola).
  - Se sacaron todas las lineas de tendencia suavizada (loess): los
    graficos quedan solo con los datos, sin curva superpuesta.
  - Nuevo grafico combinado (03c): cantidad total de viajes (barras) +
    duracion promedio (linea), por anio, con eje secundario.
  - Se saco el boxplot de duracion por periodo (03b, no aportaba mucho).
  - Se aclara en el titulo/subtitulo de los graficos 04/04b que significa
    la categoria "Otro".
  - Se saco la linea de tiempo de primeras visitas (06b, tenia errores de
    lectura con tantos mandatarios superpuestos).
  - Se saco el grafico de duracion por "año de mandato" (no mostraba un
    patron claro).
  - El ranking de destinos mas visitados se dividio en dos graficos: uno
    para bilaterales (09a) y otro para multilaterales (09b).

  Preguntas originales (secciones 3 a 8 del script):
  1) Evolucion general de la cantidad de viajes en el tiempo
  2) Que regiones se priorizan en cada epoca
  3) Cambios en la duracion de los viajes (+ combinado con cantidad de viajes)
  4-5) Bilateral vs. Multilateral vs. Otro: participacion y volumen en el tiempo
  6) Destinos preferidos por cada mandatario
  7) Primera visita de cada mandatario (a que pais)

  Extensiones (seccion 9), inspiradas en la bibliografia:
  8) Estacionalidad: en que meses del año se concentran los viajes —
     inspirado en Ostrander & Rider (2018) "Presidents Abroad", quienes
     reportan que junio/noviembre/julio/diciembre son los meses mas
     frecuentes de salida en EE.UU. y lo vinculan al calendario legislativo.
  9) Ranking de los 20 paises destino mas visitados, separado en
     bilaterales y multilaterales — inspirado en la Figura 2 de Moyer et
     al. (2025) "When HOGS Fly" (el paper que presenta el propio dataset
     COLT) y en la Tabla 5 de Ostrander & Rider (2018).

  Estas preguntas y extensiones son un punto de partida, no una lista
  cerrada — el script esta pensado para que se agreguen o cambien secciones
  a medida que surjan nuevas ideas.

COMO CORRERLO
  1. Abrir RStudio.
  2. Setear el working directory en la carpeta que CONTIENE "Base Viaje
     Presidenciales Latam" (la carpeta "PE-Latam" o donde la tengan
     sincronizada). El script arma las rutas como
     "Base Viaje Presidenciales Latam/04_BASE_FINAL/...", igual que en el
     ejemplo de carga original:
       library(readxl)
       Base_COLT_Sudamerica <- read_excel("Base Viaje Presidenciales Latam/04_BASE_FINAL/Base_COLT_Sudamerica.xlsx",
           sheet = "Datos_COLT_Sudamerica")
     Si el working directory esta en otro nivel, ajustar RUTA_EXCEL y
     RUTA_OUTPUTS al principio del script.
  3. Abrir 08_ANALISIS_R/graficos_exploratorios.R y correrlo entero
     (Source, o Ctrl+Shift+Enter / Cmd+Shift+Enter).
  4. La primera vez va a instalar automaticamente los paquetes que falten
     (readxl, dplyr, ggplot2, lubridate, scales, forcats, tidyr, stringr,
     gridExtra -este ultimo nuevo en esta version, se usa para renderizar
     las tablas descriptivas como imagen-).
  5. Los graficos se muestran en el panel de Plots de RStudio Y ADEMAS se
     guardan como PNG (mas varias tablas en CSV y tambien como PNG) en
     08_ANALISIS_R/outputs/.

ACTUALIZAR A 2026
  Cuando se termine de mapear/verificar 2026, cambiar esta linea al
  principio del script:
    ANIO_HASTA <- 2025
  por:
    ANIO_HASTA <- 2026
  y volver a correr todo el script. No hace falta ningun otro cambio.

PALETA — SOLO BLANCO / NEGRO / GRISES
  A pedido, todos los graficos usan una paleta acromatica (variables
  gris_9 = casi negro ... gris_1 = gris muy claro, definidas al inicio del
  script) en vez de colores. Donde hace falta distinguir varias series en
  un mismo grafico sin depender del color:
  - Categorias chicas (Bilateral/Multilateral/Otro/Sin dato): distintos
    tonos de gris + distinto linetype (solido/rayado/punteado).
  - Muchas categorias (12 paises, ~50-60 mandatarios): en vez de decenas de
    colores imposibles de distinguir, se usa facet_wrap (un panel por
    pais/mandatario) con un unico tono de gris.
  Las tablas descriptivas (ficha general, totales, estadisticos) tambien
  se renderizan en blanco/negro/gris via la funcion guardar_tabla_imagen()
  (usa gridExtra::tableGrob, sin depender de paquetes de captura web).
  El tema general (tema_paper(), al inicio del script) usa fondo blanco,
  lineas de grilla gris muy claro, y tipografia simple sin decoracion.

FUNCION REUTILIZABLE
  graficar_top_destinos("Nombre del Presidente", top_n = 10)
  Genera y guarda el grafico de destinos mas visitados de CUALQUIER
  mandatario de la base (de los 12 paises). Usar el nombre CON tilde tal
  como aparece en la columna Leader_nombre (version normalizada que arma
  el script — ver nota sobre tildes mas abajo). Para ver los nombres
  disponibles:
    sort(unique(colt$Leader_nombre))
  Ejemplos ya comentados dentro del script.

NOTA METODOLOGICA — NOMBRES CON/SIN TILDE
  La columna LeaderFullName mezcla dos convenciones: las filas nativas de
  COLT vienen sin tilde ("Alberto Fernandez") y las filas que agregamos
  nosotros (PELATAM) vienen con tilde en espaniol ("Alberto Fernández").
  Sin corregir esto, cualquier agrupacion por presidente cuenta a la misma
  persona dos veces. El script arma una clave interna sin tildes
  (Leader_key) para agrupar correctamente, y elige como etiqueta visible
  (Leader_nombre) la version mas frecuente de cada grupo.

NOTA METODOLOGICA — VISIT_CATEGORY DERIVADA Y QUE SIGNIFICA "OTRO"
  Bilateral/Multilateral/Other no es un dato que traiga COLT: se construye
  con esta regla (seccion 1.3 del script):
    Multilateral   si AttendedMultilatEvent == "Yes"  (tiene prioridad)
    Bilateral      si no es Multilateral y MetHostHoGS == "Yes"
    Other          si no es Multilateral y MetHostHoGS == "No"
    Sin dato       si MetHostHoGS esta vacio
  "Otro" quiere decir: el mandatario viajo pero no hay registro de reunion
  con el jefe de Estado/Gobierno anfitrion NI de participacion en un
  evento multilateral. En la practica suele tratarse de actos
  protocolares/ceremoniales, funerales, inauguraciones, escalas con
  agenda no bilateral, o visitas de trabajo sin una reunion de alto nivel
  documentada en la fuente -no necesariamente significa que "no paso
  nada" en el viaje, sino que esa reunion puntual no quedo registrada-.

  Este script fue escrito y revisado sin poder ejecutar R en el entorno
  donde se genero (sandbox sin R instalado y sin acceso a CRAN) — se
  verifico la logica de cada agregacion explorando la planilla con Python/
  pandas y openpyxl (incluyendo la lista real de los 12 paises y el rango
  de años), pero la sintaxis de R en si no se corrio antes de entregarla.
  Puntos con mas riesgo de un error puntual al correrlo en RStudio:
    - TripStartDate/TripEndDate: tipos mezclados (texto ISO y fechas
      nativas de Excel segun la fila) — ya manejado, pero un formato de
      fecha no previsto puede dar NA puntual.
    - TripDuration: tambien mezcla texto y numero.
    - El locale "es_ES.UTF-8" usado para nombres de mes en español (grafico
      08) puede no estar disponible en todas las instalaciones de R/RStudio
      — el script ya tiene un fallback automatico a numero de mes (1-12)
      si detecta que el locale fallo, pero si el error persiste,
      reemplazar esa linea por locale = "es_AR.UTF-8" o quitar el
      argumento locale directamente.
    - guardar_tabla_imagen() es nueva en esta version: si gridExtra no
      se instala bien en la maquina, esa funcion puntual puede fallar sin
      afectar al resto del script (los graficos ggplot no dependen de ella).
  Si algo tira error, probablemente sea algo menor — avisen y se corrige
  al toque.

PROXIMOS PASOS SUGERIDOS (no incluidos todavia)
  - Desagregar alguna pregunta por Visit_Subtype si en algun momento se
    agrega esa columna al esquema COLT (hoy no existe como tal; lo mas
    cercano es AttendedMultilatEvent).
  - Cruzar duracion de viaje con Visit_Category (los multilaterales duran
    distinto que los bilaterales?).
  - Explorar mas ideas de /Bib: Balci et al. (2025) y Moyer et al. (2025)
    tienen modelos de regresion (PPML con efectos fijos) sobre los
    determinantes de los viajes -distancia, comercio, alianzas, tipo de
    regimen- que podrian adaptarse como una segunda etapa de este script
    si en algun momento se quiere ir mas alla de lo descriptivo.
  - Subir ANIO_HASTA a 2026 cuando ese año este mas mapeado/verificado
    (ver seccion "ACTUALIZAR A 2026" mas arriba).
  - Cuando se verifiquen/enriquezcan Brasil y Chile 1994-1999 (tareas
    pendientes #91/#92, ver 05_BITACORA/PENDIENTES_VERIFICACION.txt), los
    graficos ya van a reflejar la version mas revisada automaticamente
    (no hace falta tocar el script).
================================================================================
