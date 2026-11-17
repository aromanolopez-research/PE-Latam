# Prompts de dispatch — Venezuela (preparados 2026-09-04, para ejecutar en la próxima sesión)

Archivos de entrada ya extraídos y listos en esta misma carpeta:
`WP1..WP10_*.json`

Cobertura verificada: 494/494 TripID extraídos (100% de las filas Venezuela con fecha de inicio dentro del mandato respectivo). Excluidos del alcance (pre-1994-01-01, documentados pero sin workpack): Carlos Andrés Pérez (LeaderID 307, 37 filas, rango 1990-01-27 a 1992-10-18) y Ramón José Velásquez (LeaderID 815, 1 fila, 1993-10-15).

Cada bloque de abajo es un prompt listo para copiar/pegar en una llamada al Agent tool. Ejecutar los 11 en paralelo (un solo mensaje, múltiples tool calls), igual que en Ecuador/Guyana/Suriname.

---

## Contexto común (incluir en TODOS los prompts)

```
Estás colaborando en un proyecto académico de Relaciones Internacionales: "Viajes presidenciales como
indicador de política exterior en Sudamérica (1994-2025)" de Alejo Romanó López (UDESA). El proyecto
mantiene una base de datos maestra de viajes internacionales de presidentes sudamericanos (PELATAM),
construida sobre datos crudos del dataset académico COLT (Diplometrics Cross-National Leader Travels).

Tu tarea es VERIFICAR cada viaje (TripID) del archivo JSON adjunto contra fuentes independientes
(noticias, comunicados oficiales de presidencia/cancillería, archivos de prensa, Wikipedia solo como
punto de partida nunca como fuente final) y reportar:
- Si los datos de COLT son correctos → confirmarlo (confirmados_sin_cambios)
- Si algún campo está mal → corregirlo con fuente (correcciones)
- Si encontrás un viaje real que NO está en el archivo (en el rango de fechas del mandato) → agregarlo (hallazgos_nuevos)
- Si no podés verificar algo con confianza → decirlo honestamente (no_verificable), NUNCA inventar

REGLAS CRÍTICAS (violarlas invalida tu trabajo):
1. En cada corrección, "campo" debe ser el nombre EXACTO de una sola columna (nunca combines dos
   campos en un string, ej. mal: "TripStartDate y TripEndDate").
2. "valor_correcto" debe ser un valor limpio y directamente usable (una fecha YYYY-MM-DD, "Yes"/"No",
   un nombre propio) — NUNCA una oración explicando incertidumbre o alternativas. Si hay incertidumbre
   real, esa entrada va en "no_verificable", no en "correcciones" con una explicación disfrazada de valor.
3. Los campos Yes/No y de nombres deben ser valores limpios, nunca prosa.
4. Anti-alucinación: si no hay URL real, escribí "Search Query: [términos exactos que usarías]" en el
   campo fuente. NUNCA inventes una URL que no verificaste.
5. Cobertura completa obligatoria: debe haber una entrada (en correcciones, no_verificable o
   confirmados_sin_cambios) para CADA TripID del archivo de entrada, sin excepción.

FORMATO DE SALIDA — debe ser un ARRAY JSON (aunque sea un solo LeaderID), escrito en la ruta exacta
indicada abajo:
[
  {
    "LeaderID": "<id>",
    "correcciones": [
      {"TripID": "...", "campo": "...", "valor_correcto": "...", "justificacion": "...", "fuente": "..."}
    ],
    "hallazgos_nuevos": [
      {"TripID": "NUEVO-<algo único>", "TripStartDate": "...", "TripEndDate": "...", "CountryVisited": "...",
       "CityVisited": "...", "Visit_Category": "...", "Visit_Subtype": "...", "Counterpart_Event": "...",
       "justificacion": "...", "fuente": "..."}
    ],
    "no_verificable": [
      {"TripID": "...", "campo": "...", "motivo": "...", "fuente_intentada": "..."}
    ],
    "confirmados_sin_cambios": [
      {"TripID": "...", "campo": "...", "valor": "...", "justificacion": "...", "fuente": "..."}
    ]
  }
]

Al terminar, reportá un resumen numérico: cuántos TripID procesaste, cuántas correcciones, cuántos
hallazgos nuevos, cuántos no_verificable, cuántos confirmados sin cambios.
```

---

## WP1 — Rafael Caldera 2º mandato (LeaderID 898, 33 items, 1994-06-13 a 1998-10-17)

```
[Contexto común arriba] +

Archivo de entrada: WP1_caldera.json (esta carpeta)
Archivo de salida: resultados_leader_898.json (esta carpeta)

Contexto histórico específico: Rafael Caldera gobernó Venezuela 1994-1999 (2º mandato, tras ganar como
candidato independiente post-golpes de 1992). Fue un período de crisis bancaria doméstica (1994) y
diplomacia relativamente convencional dentro de la región (Grupo de Río, Cumbres Iberoamericanas,
relación con EEUU sin mayores sobresaltos). Prestá atención a cumbres regionales (Cumbre de las
Américas de Miami, dic-1994; Grupo de Río) y visitas bilaterales a Colombia (relación fronteriza
siempre sensible) y EEUU.
```

## WP2 — Hugo Chávez, parte 1/6 (LeaderID 1383, 48 items, 1999-02-02 a 2000-12-31)

```
[Contexto común arriba] +

Archivo de entrada: WP2_chavez_p1_1999_2000.json (esta carpeta)
Archivo de salida: resultados_leader_1383_p1.json (esta carpeta)

Contexto histórico específico: primeros dos años de Hugo Chávez (asumió 1999-02-02). Proceso
constituyente (nueva Constitución de 1999), giras diplomáticas activas de "diversificación" fuera de
la órbita tradicional EEUU (visitas a Libia, Irak bajo sanciones -viaje polémico y muy cubierto por
prensa-, Cuba). Fundación de la línea de política exterior "multipolar". Prestá especial atención a la
gira por países de la OPEP en 2000 (incluida la visita a Bagdad, la primera de un jefe de Estado desde
la Guerra del Golfo) y a la relación con Cuba (Fidel Castro).
```

## WP3 — Hugo Chávez, parte 2/6 (LeaderID 1383, 59 items, 2001-01-01 a 2002-12-31)

```
[Contexto común arriba] +

Archivo de entrada: WP3_chavez_p2_2001_2002.json (esta carpeta)
Archivo de salida: resultados_leader_1383_p2.json (esta carpeta)

Contexto histórico específico: incluye el golpe de Estado de abril de 2002 (Chávez fue depuesto
brevemente el 11-13 de abril de 2002 y luego restituido). ESTO ES CRÍTICO: durante esos días Chávez no
estaba en condiciones de viajar (detenido); verificá con cuidado que no haya ningún TripID mal fechado
alrededor del 11-14 de abril de 2002. También el paro petrolero de fines de 2002 pudo haber afectado
la agenda de viajes de diciembre. Además, este período incluye giras activas a Medio Oriente y Asia
buscando diversificar mercados petroleros.
```

## WP4 — Hugo Chávez, parte 3/6 (LeaderID 1383, 61 items, 2003-01-01 a 2005-12-31)

```
[Contexto común arriba] +

Archivo de entrada: WP4_chavez_p3_2003_2005.json (esta carpeta)
Archivo de salida: resultados_leader_1383_p3.json (esta carpeta)

Contexto histórico específico: post-paro petrolero, consolidación del "Socialismo del Siglo XXI".
Lanzamiento de Petrocaribe (2005) y profundización de la alianza con Cuba (convenios de petróleo por
médicos). Fundación de Telesur (2005). Fuerte activismo en cumbres del ALBA y Mercosur (Venezuela
solicitó adhesión a Mercosur en 2005-2006). Tensión creciente con EEUU bajo la administración Bush.
```

## WP5 — Hugo Chávez, parte 4/6 (LeaderID 1383, 71 items, 2006-01-01 a 2007-12-31)

```
[Contexto común arriba] +

Archivo de entrada: WP5_chavez_p4_2006_2007.json (esta carpeta)
Archivo de salida: resultados_leader_1383_p4.json (esta carpeta)

Contexto histórico específico: ingreso formal de Venezuela a Mercosur (firmado jul-2006). Campaña por
un puesto no permanente en el Consejo de Seguridad de la ONU (2006, perdida ante Guatemala tras
empate prolongado — implicó múltiples giras diplomáticas de lobby). Fundación del Banco del Sur y
UNASUR (2007-2008, primeras reuniones). Cumbres iberoamericanas (incluido el incidente "por qué no te
callas" con el Rey Juan Carlos en la Cumbre de Santiago de Chile, nov-2007).
```

## WP6 — Hugo Chávez, parte 5/6 (LeaderID 1383, 57 items, 2008-01-01 a 2009-12-31)

```
[Contexto común arriba] +

Archivo de entrada: WP6_chavez_p5_2008_2009.json (esta carpeta)
Archivo de salida: resultados_leader_1383_p5.json (esta carpeta)

Contexto histórico específico: crisis diplomática con Colombia por el bombardeo a un campamento de
las FARC en Ecuador (Operación Fénix, marzo 2008) — Venezuela movilizó tropas a la frontera y rompió
relaciones brevemente. Firma del tratado constitutivo de UNASUR (mayo 2008, Brasilia). Fundación
formal de UNASUR (2008). Crisis de Honduras 2009 (golpe contra Zelaya) — Venezuela muy activa
diplomáticamente en su rechazo.
```

## WP7 — Hugo Chávez, parte 6/6 (LeaderID 1383, 48 items, 2010-01-01 a 2013-03-05)

```
[Contexto común arriba] +

Archivo de entrada: WP7_chavez_p6_2010_2012.json (esta carpeta)
Archivo de salida: resultados_leader_1383_p6.json (esta carpeta)

Contexto histórico específico: fundación de la CELAC (cumbre constitutiva, Caracas, dic-2011 — evento
que Venezuela organizó y por tanto NO implicó viaje de Chávez, prestá atención a no confundir esto con
un TripID). Este período coincide con el diagnóstico y tratamiento de cáncer de Chávez (desde jun-2011,
múltiples viajes médicos a La Habana, Cuba, que en COLT pueden estar categorizados de forma
inconsistente — verificá si deberían marcarse como Visit_Subtype "Transit/Medical" en vez de otra
categoría). El corte de este workpack termina el 2013-03-05, fecha de la muerte de Chávez (el archivo
crudo no debería tener TripStartDate posterior, pero verificalo).
```

## WP8 — Nicolás Maduro, parte 1/3 (LeaderID 2179, 57 items, 2013-04-19 a 2015-12-31)

```
[Contexto común arriba] +

Archivo de entrada: WP8_maduro_p1_2013_2015.json (esta carpeta)
Archivo de salida: resultados_leader_2179_p1.json (esta carpeta)

Contexto histórico específico: primeros años de Nicolás Maduro (asumió 2013-04-19 tras elección
estrecha post-muerte de Chávez). Continuidad de la política de alianzas ALBA/Petrocaribe/CELAC.
Inicio de la crisis económica (control de cambios, escasez) que fue reduciendo el margen de maniobra
diplomática. Prestá atención a cumbres de UNASUR/CELAC/Mercosur (Venezuela asumió la presidencia pro
tempore de Mercosur en 2013).
```

## WP9 — Nicolás Maduro, parte 2/3 (LeaderID 2179, 36 items, 2016-01-01 a 2019-12-31)

```
[Contexto común arriba] +

Archivo de entrada: WP9_maduro_p2_2016_2019.json (esta carpeta)
Archivo de salida: resultados_leader_2179_p2.json (esta carpeta)

Contexto histórico específico: período de aislamiento internacional creciente. Suspensión de
Venezuela del Mercosur (dic-2016, invocando la cláusula democrática) y salida formal de la OEA
(anunciada 2017, efectiva 2019) — esto reduce drásticamente el número de cumbres regionales a las que
Maduro pudo asistir legítimamente como jefe de Estado reconocido por esos bloques. Crisis de
reconocimiento internacional desde ene-2019 (Juan Guaidó autoproclamado "presidente encargado",
reconocido por EEUU y buena parte de la región) — MUY IMPORTANTE: a partir de 2019 verificá con
cuidado cuáles países seguían recibiendo a Maduro como jefe de Estado legítimo (Rusia, China, Cuba,
Turquía, algunos países no alineados) vs. cuáles ya no. La cobertura de COLT es notablemente escasa
en este tramo (solo 36 registros en 4 años) — es razonable esperar que haya viajes reales no
capturados por COLT; buscá activamente hallazgos_nuevos, especialmente a Rusia, China, Turquía, Cuba.
```

## WP10 — Nicolás Maduro, parte 3/3 (LeaderID 2179, 24 items, 2020-01-01 a 2026-01-03)

```
[Contexto común arriba] +

Archivo de entrada: WP10_maduro_p3_2020_2026.json (esta carpeta)
Archivo de salida: resultados_leader_2179_p3.json (esta carpeta)

Contexto histórico específico y TAREA ESPECIAL: este es el tramo final del mandato de Maduro, hasta su
captura por EEUU el 2026-01-03 (Operación "Absolute Resolve") y su consecuente fin de gestión (verificado
independientemente en investigación previa del proyecto). El archivo de entrada tiene su último registro
COLT en 2025-05-06 — hay una BRECHA DOCUMENTAL de facto entre esa fecha y el 2026-01-03 que necesita
investigación activa: buscá específicamente si Maduro realizó algún viaje internacional entre mayo de
2025 y enero de 2026 (por ejemplo, cumbres de la CELAC, viajes a Rusia/China/Cuba, o cualquier
desplazamiento reportado por prensa internacional en el contexto de la escalada de tensión con EEUU que
precedió a su captura). Reportá cualquier hallazgo en "hallazgos_nuevos"; si tras una búsqueda genuina no
encontrás evidencia de viajes en ese tramo, documentalo explícitamente como tal (no lo dejes en silencio).
También verificá con cuidado la fecha y las circunstancias exactas de la Operación Absolute Resolve
(3-ene-2026) como referencia de contexto, aunque la captura en sí no sea un "viaje" a cargar en la base.
```

## WP11 — Delcy Rodríguez, presidenta encargada (LeaderID sintético 90007, SIN cobertura COLT — investigar desde cero)

```
[Contexto común arriba, adaptado: no hay archivo de entrada, investigación desde cero] +

NO hay archivo de entrada JSON (Delcy Rodríguez no tiene registros en COLT bajo ningún LeaderID).
Archivo de salida: resultados_leader_90007.json (esta carpeta)

Tu tarea es investigar DESDE CERO todos los viajes internacionales oficiales de Delcy Rodríguez como
Presidenta encargada de Venezuela, desde su asunción (2026-01-05, tras la captura de Maduro el
2026-01-03 y la invocación de la sucesión vicepresidencial por el TSJ) hasta 2026-09-04 (fecha de
corte de esta investigación). Es un caso análogo a Jeanine Áñez (Bolivia) y Abelardo de la Espriella
(Colombia) trabajados antes en este mismo proyecto: sin fila base de COLT, hay que generar los
"hallazgos_nuevos" completos con TripID nuevo para cada viaje real encontrado (formato TripID sugerido:
"90007-VEN-<PAIS3>-<n>").

Dado el contexto de aislamiento internacional que ya tenía Venezuela bajo Maduro y la situación
excepcionalmente inestable/contestada de la sucesión (con el reclamo rival de legitimidad de María
Corina Machado / Edmundo González, que este proyecto decidió NO tratar como jefatura de Estado en
ejercicio, siguiendo la convención de trackear solo mandatarios con capacidad de gobierno efectiva), es
razonable esperar POCOS o NINGÚN viaje internacional documentable de Delcy Rodríguez en este período.
Si no encontrás evidencia de viajes reales, documentalo explícitamente (LeaderID 90007 con arrays
vacíos y una nota aclaratoria) en vez de forzar hallazgos dudosos. Verificá también, como parte de esta
investigación, si Rodríguez ha participado (presencial o virtualmente) en alguna cumbre regional
(CELAC, ALBA) desde su asunción, y si algún país la ha recibido en visita bilateral formal reconociéndola
como jefa de Estado.
```

---

## Después del dispatch (próxima sesión, no hacer ahora)

1. Verificar cobertura programática: 494 TripID esperados (WP1-WP10) deben aparecer 100% cubiertos
   entre correcciones+no_verificable+confirmados_sin_cambios de los 10 archivos de resultado.
2. QC de esquema (igual que Ecuador/Guyana/Suriname): archivo top-level debe ser lista; todo campo
   debe ser columna real; todo correccion debe tener valor_correcto; escanear valores sospechosamente
   largos en valor_correcto.
3. Aplicar con `colt_aplicar_workpacks.py Venezuela <slug> <json...>` — dry-run primero, luego
   `--aplicar`. Incluir el resultado de WP11 (Delcy Rodríguez, LeaderID sintético 90007) como
   hallazgos_nuevos puros (nuevas filas PELATAM), no como correcciones.
4. Validar con `colt_validar_madre.py`.
5. Backup pre-merge: `Base_COLT_Sudamerica_backup_pre_venezuela_merge.xlsx`.
6. Recalcular Agregados/Modificados/Eliminados/Pendientes_de_validar para Venezuela y reemplazar el
   placeholder "Sin iniciar" en `diferencias_colt` (graficos_exploratorios.R, ~línea 591-612).
7. Documentar en `PENDIENTES_VERIFICACION.txt` (sección `## VENEZUELA — VERIFICACION COLT COMPLETA`)
   y en `bitacora.txt`, cerrando así el país 12 de 12 del proyecto.
8. Actualizar `mandatos_presidenciales.csv` si aparece nueva información sobre fecha de fin de mandato
   de Delcy Rodríguez o llamado a elecciones (al 2026-09-04 no había fecha fijada).
```
