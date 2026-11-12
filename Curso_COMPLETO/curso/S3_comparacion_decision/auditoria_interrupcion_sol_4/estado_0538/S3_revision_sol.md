# S3. Revisión de contenido y entrega — claude-sol

Fecha: 25 de octubre de 2026. Alcance: exclusivamente `curso/S3_comparacion_decision/`; fase de contenido, no de ejercicios.

## Nota del supervisor

Supervisor: claude-sol (gpt-6.1-sol). Reanudación: 2026-10-26, 05:26:26 −05:00. Se conserva el plan existente. Las ediciones interrumpidas se tratarán como candidatas, con decisión y fundamento individual; no constituyen revisión aprobada por sí mismas.

## Plan de revisión

1. Leer íntegramente el plan maestro, la guía, `prop_e.md` y su revisión final; contrastar después, en orden M09 → M10 → M11 → M12, cada libreto con su bitácora y revisión Haiku.
2. Construir una comprobación por nivel acumulativo contra M9–M12 de prop_e: temas completos, sin ampliaciones, un marcador por práctica y ninguna práctica desarrollada; respetar las exclusiones de §6 y distinguir ejemplos narrados de actividades evaluables.
3. Revisar signos, unidades, incertidumbres estándar/expandidas, cobertura, dependencia, hipótesis de las decisiones y origen de los datos; comprobar errores críticos y escalamiento. Recalcular ejemplos clave y ejecutar todos los scripts con `curso/.venv/bin/python`; incorporar aserciones o cálculos adicionales cuando sean necesarios, sin modificar archivos fuera de S3.
4. Verificar las referencias y los numerales de las fuentes locales mediante `pdftotext`, conservando evidencias dentro de S3 si procede. Las fuentes externas ausentes se identificarán expresamente; no se darán por verificadas localmente. Una referencia curricular no sustituirá una fuente técnica.
5. Revisar formato oral, lectura de fórmulas, acotaciones, fichas, niveles, prerrequisitos, continuidad M09–M12 y remisiones AX. Consolidar en S3 una ficha común de criterios para evitar confundir tolerancias, límites de control y umbrales de indicadores.
6. Registrar hallazgos identificados S-…, su severidad, ubicación y corrección; aplicar los cambios y volver a ejecutar las comprobaciones afectadas. Entregar índice de escenas, prácticas pendientes, anexos, datos y estado. Declarar pendientes reales sin equiparar contenido revisado con curso listo para impartir.

## Hallazgos por capítulo

### Transversales

- **S-TR-01 — Menor — Ficha común, párrafo tras la tabla SRP/EPA.** La ruta `calc/fuentes_M09_M10/` no existe. Corregida a `calc/auditoria_M09_M10/`. Se conserva la ficha candidata por cumplir los campos exigidos por prop_e M10 y distinguir ámbitos de decisión. Evidencia: `calc/revision_ficha_actual.md` y extractos `calc/ficha_*_actual.txt`.
- **S-TR-02 — Documental — Recuperación de la interrupción.** S3 contiene una auditoría, `auditoria_interrupcion_sol_2/`, con 36 bloques (11 M09, 6 M10, 10 M11, 9 M12). No existe aquí auditoría C01–C27; el LEEME disponible la atribuye a S1. No se inventan identificadores ni se modifican S1 o registros del orquestador. Los bloques se identifican por capítulo y encabezado `@@`, además de la línea del diff. Las instantáneas en `versiones/` se conservan como evidencia histórica, no como material entregado.

- **S-TR-03 — Menor — Entrega documental.** Faltaba el índice de la sección. Corrección: crear `S3_00_indice.md` con capítulos, escenas por nivel, doce prácticas pendientes, anexos, datos rotulados, estado y pendientes de fase posterior.

### Revisión individual

En consolidación; los informes de cada capítulo documentarán aquí hallazgos y decisiones antes del cierre.

## Correcciones aplicadas

### Transversales

- **S-TR-01.** Cambio: ruta de evidencias corregida en `S3_01_ficha_criterios.md`; se conserva la ficha candidata con sus ámbitos diferenciados. Comprobación: extractos nuevos `calc/ficha_TAD_actual.txt`, `calc/ficha_CFR_actual.txt`, `calc/ficha_EN_actual.txt`; fuentes identificadas en `calc/ficha_fuentes_sha256.txt`; cifras reproducidas con `calc/S3_verificar_ficha.py`, salida `calc/ficha_recalculo_actual.out`.
- **S-TR-02.** Cambio: inventario y método de identificación explícitos en esta revisión y `calc/revision_ficha_actual.md`; auditorías e instantáneas conservadas sin reescribirlas. Los informes individuales se incorporan a continuación para no dejar decisiones candidatas implícitas.
- **S-TR-03 — Entrega documental.** Se crea `S3_00_indice.md`, con escenas por nivel, doce marcadores de prácticas pendientes, origen de datos, anexos, recursos compartidos y límites de entrega. Se comprobaron sus quince enlaces locales. No se crean ejercicios ni soluciones de prácticas.

### Verificación transversal

Se leyeron íntegramente `curso/00_plan_maestro.md`, `curso/guia_libreto.md`, `prop_e.md` y `revision_final_prop_e.md`. Se mantiene orden M09, M10, M11, M12. La revisión individual incluye cada libreto, su bitácora y la revisión Haiku; estas últimas son antecedentes, no sustitutos de verificar el texto final.

Los anexos AX.1, AX.2 y AX.8–AX.12 existen en S4 con los títulos de la guía; solo se comprueban destinos, sin modificar ni aprobar S4. La notación común conserva referencia/indicación, signo de la diferencia, u/U y cobertura; las variables locales de series, probabilidades e indicadores se definen en sus escenas. La reiteración breve de dependencia, cobertura y ámbitos responde a prerrequisitos acumulativos, sin repetir deducciones. Compatibilidad (M09), conformidad (M10), control (M11) e indicadores agregados (M12) se mantienen como preguntas diferentes.

El control `calc/S3_verificar_entrega.py` pasó inicialmente: seis escenas M09, seis M10, ocho M11, nueve M12; tres marcadores por capítulo, uno por nivel, etiquetas permitidas. No prueba semánticamente que no haya ejercicios desarrollados: esa comprobación pertenece también a la lectura individual. El cierre registrará la ejecución final.

## Estado de entrega

En revisión; plan confirmado antes de inspeccionar los capítulos en esta ejecución. Se contrastarán también las observaciones Haiku con el texto final, sin asumirlas correctas.
