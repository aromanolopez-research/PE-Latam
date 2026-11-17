================================================================================
PROYECTO: VIAJES PRESIDENCIALES DE SUDAMÉRICA (1994–2025, luego 2026)
================================================================================
Inicio rápido. La documentación completa está en 00_CODEBOOK/CODEBOOK.txt

QUÉ ES
  Base de datos consolidada de los viajes internacionales oficiales de los
  presidentes de los 12 países de Sudamérica (Argentina, Bolivia, Brasil,
  Chile, Colombia, Ecuador, Guyana, Paraguay, Perú, Surinam, Uruguay,
  Venezuela), 1994-2025. Se construye sobre el dataset académico COLT
  (Moyer et al.) como archivo madre: se corrige lo que COLT tiene mal, se
  agrega lo que investigamos y COLT no tiene, y se deja todo trazable para
  un paper académico sobre política exterior sudamericana.

REDISEÑO 2026-08-24 (leer si venís de una versión anterior del proyecto)
  El proyecto originalmente mantenía un esquema propio de 31 columnas por
  país (06_RESIDUOS/modulos_pais/<pais>/<pais>_viajes.csv) más un Excel de COLT
  aparte. Esto cambió: ahora hay UN SOLO archivo madre
  (01_BASE_FINAL/Base_COLT_Sudamerica.xlsx, hoja "Datos_COLT_Sudamerica"),
  con el esquema NATIVO de COLT (76 columnas), donde se corrige y se agrega
  todo. Las columnas propias que se habían inventado (Visit_Category,
  Visit_Subtype, Tema_Foro, Counterpart_Type, Journey_ID, Verificacion_Status)
  se dejaron de usar como parte del flujo de trabajo -COLT ya cubre esas
  dimensiones con su propio esquema (MetHostHoGS, AttendedMultilatEvent,
  etc.)-. Las carpetas 01_INSTRUCCIONES, 02_TABLA_MAESTRA y
  07_ARCHIVO_TRABAJO_PREVIO se eliminaron (respaldo en
  02_BITACORA/archivo_historico/backup_pre_rediseno_2026-08-24.zip).

CÓMO ESTÁ ORGANIZADO (reordenado 2026-11-15: numeración consecutiva)
  00_CODEBOOK/     -> LEER PRIMERO. Define variables, reglas y flujo.
  01_BASE_FINAL/   -> BASES DEFINITIVAS (solo esto):
                        Base_COLT_Sudamerica.xlsx  = ARCHIVO MADRE único: COLT +
                          nuestro trabajo (hojas Datos_COLT_Sudamerica,
                          Viajes_Cancelados, Leame). Trabajar siempre ahí.
                        base_colt_sudamerica_trabajo.csv = espejo de trabajo de
                          la hoja Datos (los scripts operan sobre él).
                        Base_Diadas_Vecinos.xlsx = díadas de vecindad, solo los
                          12 países de Sudamérica (132 díadas).
                        Base_Ideologia_Presidencial.xlsx = ideología presidencial.
                        Mandatos_Presidenciales.xlsx = fechas de mandato (lo lee R).
  02_BITACORA/     -> bitacora.txt, PENDIENTES_VERIFICACION.txt,
                      anexos_colt_sudamerica/ (logs de campañas), archivo_historico/.
  03_SCRIPTS/      -> scripts activos del flujo (colt_*.py).
  04_ANALISIS_R/   -> análisis exploratorio en R (graficos_exploratorios.R).
  05_PAPER/        -> .Rnw / .bib / PDF del paper.
  06_RESIDUOS/     -> TODO lo que ya no se usa (no borrar, solo referencia):
                        modulos_pais/ (CSV por país de la etapa previa),
                        bases_y_backups/ (backups de la base, base_consolidada.csv,
                        mandatos_presidenciales.csv viejo), scripts_legado/
                        (build_*, aplicar_verificacion_*, etc.),
                        paper_archivos_auxiliares/ (.log/.bbl/...), otros/.
  Equivalencias con los nombres anteriores: 03_MODULOS_PAIS -> 06_RESIDUOS/modulos_pais;
  04_BASE_FINAL -> 01_BASE_FINAL; 05_BITACORA -> 02_BITACORA; 06_SCRIPTS -> 03_SCRIPTS;
  08_ANALISIS_R -> 04_ANALISIS_R; 09_PAPER -> 05_PAPER.

CÓMO TRABAJAR (resumen; detalle en el CODEBOOK)
  1) Tomar el siguiente país/mandatario a investigar o verificar.
  2) Comparar contra las filas de COLT ya cargadas en Datos_COLT_Sudamerica
     para ese país/LeaderID: corregir celdas donde COLT esté mal (con fuente
     y nota), marcar donde nuestra hipótesis esté mal, agregar filas nuevas
     con TripID "PELATAM-<ISO3>-<n>" para lo que investigamos y COLT no tiene.
  3) Registrar en bitácora.txt y PENDIENTES_VERIFICACION.txt.

REQUISITOS TÉCNICOS
  Python 3 + openpyxl (para leer/escribir el .xlsx). Los scripts trabajan
  internamente contra un CSV espejo de la hoja madre por velocidad, y
  exportan/actualizan el .xlsx al final de cada campaña.
================================================================================
