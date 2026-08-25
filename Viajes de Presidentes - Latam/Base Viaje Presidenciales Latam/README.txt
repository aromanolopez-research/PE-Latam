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
  país (03_MODULOS_PAIS/<pais>/<pais>_viajes.csv) más un Excel de COLT
  aparte. Esto cambió: ahora hay UN SOLO archivo madre
  (04_BASE_FINAL/Base_COLT_Sudamerica.xlsx, hoja "Datos_COLT_Sudamerica"),
  con el esquema NATIVO de COLT (76 columnas), donde se corrige y se agrega
  todo. Las columnas propias que se habían inventado (Visit_Category,
  Visit_Subtype, Tema_Foro, Counterpart_Type, Journey_ID, Verificacion_Status)
  se dejaron de usar como parte del flujo de trabajo -COLT ya cubre esas
  dimensiones con su propio esquema (MetHostHoGS, AttendedMultilatEvent,
  etc.)-. Las carpetas 01_INSTRUCCIONES, 02_TABLA_MAESTRA y
  07_ARCHIVO_TRABAJO_PREVIO se eliminaron (respaldo en
  05_BITACORA/archivo_historico/backup_pre_rediseno_2026-08-24.zip).

CÓMO ESTÁ ORGANIZADO
  00_CODEBOOK/             -> LEER PRIMERO. Define variables, reglas y flujo.
  03_MODULOS_PAIS/         -> LEGADO, de solo lectura. CSV por país (Argentina,
                               Brasil, Chile, Paraguay, Uruguay, Bolivia) de la
                               etapa anterior al rediseño. No se crean archivos
                               nuevos acá; sirven de referencia/auditoría.
  04_BASE_FINAL/           -> Base_COLT_Sudamerica.xlsx es el ARCHIVO MADRE
                               único (hoja Datos_COLT_Sudamerica). Trabajar
                               siempre ahí. base_consolidada.csv es legado del
                               esquema anterior (ver Codebook antes de usarlo).
  05_BITACORA/             -> bitacora.txt (registro del trabajo),
                               PENDIENTES_VERIFICACION.txt, anexos_colt_sudamerica/
                               (logs de cada campaña), archivo_historico/ (backups).
  06_SCRIPTS/               -> schema.py, validate.py, integrate.py, y el
                               pipeline de verificación/carga contra COLT.
  08_ANALISIS_R/            -> análisis exploratorio en R sobre la base.

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
