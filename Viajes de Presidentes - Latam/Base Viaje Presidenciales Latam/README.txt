================================================================================
PROYECTO: VIAJES PRESIDENCIALES DE AMÉRICA (2000–2026)
================================================================================
Inicio rápido. La documentación completa está en 00_CODEBOOK/CODEBOOK.txt

QUÉ ES
  Base de datos exhaustiva y reproducible de los viajes internacionales oficiales
  de los jefes de gobierno de América, durante su mandato, 2000-2026.

CÓMO ESTÁ ORGANIZADO
  00_CODEBOOK/             -> LEER PRIMERO. Define variables, reglas y flujo.
  01_INSTRUCCIONES/        -> Encargo original.
  02_TABLA_MAESTRA/        -> Lista de mandatarios (esqueleto del proyecto).
  03_MODULOS_PAIS/         -> Datos de viajes por país (CSV: <pais>_viajes.csv).
  04_BASE_FINAL/           -> base_consolidada.csv (resultado integrado).
  05_BITACORA/             -> bitacora.txt (registro del trabajo).
  06_SCRIPTS/              -> schema.py, validate.py, integrate.py, build_module_template.py
  07_ARCHIVO_TRABAJO_PREVIO/ -> Versiones anteriores (formato viejo) como insumo.

CÓMO TRABAJAR (resumen; detalle en el CODEBOOK, sección 6)
  1) Tomar el siguiente mandatario de la tabla maestra (por país, cronológico).
  2) Investigar sus viajes (fuente oficial + cruces).
  3) Cargar en formato de 19 columnas (una fila por país de destino; Journey_ID por salida).
  4) python 06_SCRIPTS/validate.py 03_MODULOS_PAIS/<pais>/<pais>_viajes.csv   (debe dar 0 errores)
  5) Chequeo de completitud (segunda fuente) y registro en la bitácora.
  6) Al terminar el país: python 06_SCRIPTS/integrate.py

CÓMO REPLICAR PARA OTRA REGIÓN (Europa, Asia, etc.)
  Copiar esta carpeta; vaciar 03 y 04; reemplazar la tabla maestra por los
  mandatarios de la nueva región; ajustar REGION_MAP en schema.py si hay países
  nuevos; seguir el mismo flujo. El andamiaje (formato, validación, integración,
  bitácora) es agnóstico de la región.

REQUISITOS TÉCNICOS
  Python 3 (sin librerías externas para validar/integrar; solo csv estándar).
  Formato de datos: CSV UTF-8, minimalista, listo para R / Python / SPSS / Stata.
================================================================================
