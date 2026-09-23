# Diplomacia Presidencial en Sudamérica (1994–2026)

Base de datos y análisis cuantitativo de los viajes internacionales oficiales de los presidentes de los 12 países de Sudamérica, con foco en la diplomacia presidencial como indicador operacional de política exterior.

**5.426 viajes** verificados, 76 variables por viaje, 1994–2026, Argentina · Bolivia · Brasil · Chile · Colombia · Ecuador · Guyana · Paraguay · Perú · Surinam · Uruguay · Venezuela.

![Auge y caída del multilateralismo sudamericano](Viajes%20de%20Presidentes%20-%20Latam/Base%20Viaje%20Presidenciales%20Latam/08_ANALISIS_R/outputs/13_auge_caida_multilateralismo.png)

*Participación de viajes multilaterales sobre el total, con los hitos de fundación (y crisis) de los principales organismos regionales. Uno de ~30 gráficos del análisis exploratorio, en `08_ANALISIS_R/outputs/`.*

## Qué es

Un presidente que viaja está, casi por definición, haciendo política exterior: eligiendo con quién reunirse, a qué cumbre asistir y a qué región dedicarle tiempo. Este proyecto construye una base de datos verificada de esos viajes y la usa para responder preguntas de política comparada: ¿hacia dónde mira cada país de la región?, ¿varía la orientación regional con la ideología del presidente?, ¿se sostiene la homofilia ideológica en los destinos elegidos?, ¿qué pasó con el multilateralismo sudamericano desde la fundación de UNASUR hasta su vaciamiento?

El resultado es un dataset reutilizable, un pipeline de verificación documentado y un paper académico (LaTeX/Sweave) con el análisis completo.

## Fuentes de datos

- **[COLT (Country and Organization Leader Travel) Dataset](https://korbel.du.edu/pardee/country-organization-leader-travel/)**, del Pardee Institute for International Futures (Josef Korbel School, University of Denver) — dataset académico de referencia sobre viajes de jefes de Estado y de gobierno, usado aquí como archivo madre y benchmark metodológico ([Moyer et al., *ISQ* 2025](https://academic.oup.com/isq/article/69/2/sqaf013/8081642)).
- **Investigación propia**: cada fila de COLT para los 12 países se verificó contra fuentes primarias (comunicados de cancillería, agencias de noticias, archivos oficiales); se corrigieron errores, se completaron campos faltantes y se agregaron 264 viajes que COLT no tenía registrados, todo con fuente y nota de verificación.
- **[Global Leader Ideology Dataset](https://github.com/bastianherre/global-leader-ideologies)**, de Herre et al. (2023) — codificación izquierda/centro/derecha de líderes mundiales, usada para el análisis de ideología y homofilia en los destinos.
- Base propia de ideología presidencial sudamericana (Merke + CPE-Latinoamérica) y de mandatos presidenciales (fechas de inicio/fin verificadas por país).

## Método

1. **Verificación fila por fila** contra COLT: 12 campañas de país, cada una documentada en `05_BITACORA/` con su log de cambios aplicados, fuente por corrección y estado de verificación.
2. **Clasificación analítica**: cada viaje se tipifica como Bilateral/Multilateral/Otro, se le asigna región/subregión (esquema ONU) y bloque Norte Global/Sur Global, y se cruza con la ideología del presidente que viaja (y, para los viajes a Europa, con la del líder visitado).
3. **Análisis exploratorio en R** (`tidyverse`, `ggplot2`): ~30 figuras y cuadros, con tests estadísticos (correlación de Pearson, chi-cuadrado de independencia) donde corresponde.
4. **Paper** en Sweave (`.Rnw`, LaTeX + R embebido): cada gráfico y tabla del documento final se genera directamente desde el script de R, sin pasos manuales entre el dato y el output.

## Estructura del repositorio

```
Política Exterior Latam/
└── Viajes de Presidentes - Latam/
    ├── Base Viaje Presidenciales Latam/
    │   ├── 00_CODEBOOK/          Definición de variables y flujo de trabajo (leer primero)
    │   ├── 03_MODULOS_PAIS/      CSV legado por país (etapa previa al archivo madre único)
    │   ├── 04_BASE_FINAL/        Base_COLT_Sudamerica.xlsx — el archivo madre (5.426 filas)
    │   ├── 05_BITACORA/          Bitácora de trabajo + logs de verificación por campaña
    │   ├── 06_SCRIPTS/           Pipeline en Python (carga, validación, integración contra COLT)
    │   ├── 08_ANALISIS_R/        graficos_exploratorios.R — todo el análisis exploratorio
    │   └── 09_PAPER/             ViajesPresidencialesSudamerica.Rnw/.pdf — el paper
    └── Bib/                      Bibliografía académica (política exterior, diplomacia presidencial)
```

## Cómo reproducir el análisis

```r
# Desde Base Viaje Presidenciales Latam/08_ANALISIS_R/
source("graficos_exploratorios.R")
```

Genera todas las figuras y cuadros en `outputs/`, que después alimentan directamente el paper (`09_PAPER/ViajesPresidencialesSudamerica.Rnw`, compilable con `knitr`).

## Licencia

MIT — ver [LICENSE](LICENSE).
