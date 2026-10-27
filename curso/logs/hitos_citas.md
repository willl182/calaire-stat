# Supervisión del cotejo bibliográfico — reanudación

Fecha: 2026-10-27. Supervisor: claude-sol. Se conservaron los entregables previos S1; este reporte estaba vacío al reanudar. Se leyeron `curso/guia_libreto.md`, `curso/revision_final.md`, el script previo y los registros existentes. La revisión S1 se invocó primero con Haiku y el entorno corregido (`env -u ANTHROPIC_BASE_URL -u ANTHROPIC_API_KEY -u CLAUDE_CODE_AUTO_MODE_SERVER`); no se repitió su ejecución inicial.

Alcance: 15 libretos, M00–M13 y AX, por lotes S1–S4. El recuento literal inicial del árbol vivo da 63 marcas «no disponible en docs/», frente a las 57 históricas de `revision_final.md`; no se considera ninguna de las dos cifras prueba de verificación. Se cotejan también citas sin esa marca. Hay otro supervisor desarrollando prácticas en paralelo: se preservarán esos cambios; las líneas de los inventarios deben entenderse respecto de la versión examinada.

No se harán commits. Ausencia local y falta de verificación se registrarán por separado. Un lote revisado puede cerrarse administrativamente sin que todas sus fuentes sean verificables; si quedan defectos o limitaciones que impidan declarar cerrado el pendiente 1, se señalarán expresamente.

## Incidencias de ejecución — 2026-10-27 14:11

Las ejecuciones iniciales S2 y S3 de esta reanudación alcanzaron el límite de 600 segundos del comando en segundo plano y fueron detenidas por el entorno. No se consideran entregas completas: conservaban inventarios parciales. Se reanudaron con un límite de 1800 segundos, prompts de continuidad y registros separados `citas_S2_luna_continuacion.out` y `citas_S3_luna_continuacion.out`, sin descartar los avances. S4 terminó con código 0 y se remitió a Haiku. S1 recibió 18 hallazgos; se remitieron a luna con decisión explícita de no retirar prácticas autorizadas por el usuario y de comprobar los hallazgos bibliográficos antes de aplicarlos.

## Hito 1 — Recuperación y revisión independiente de los avances — 2026-10-27 14:36

Se preservó la ejecución previa S1 y se obtuvo la revisión independiente que faltaba corrigiendo el entorno de Haiku en `curso/scripts/cotejo_citas_lotes.sh`. Se creó `curso/scripts/inventario_ocurrencias_sol.py` y su control literal inicial `curso/citas/ocurrencias_supervisor_inicial.tsv`; sus 650 corchetes no acotación no son un recuento semántico de fuentes verificadas. Se publicó el TSV S1 que había quedado solo en `/tmp/`.

Hallazgos Haiku y decisión: se rechazó retirar prácticas autorizadas; se contrastaron directamente ASQ PDF 605/impresa 572 y EN 14625 PDF 20/impresa 18, evitando adoptar páginas erróneas. La revisión final S1 confirmó la corrección causal S-01 de M01, pero detectó inventario parcial obsoleto, huellas desactualizadas y decisiones sobre frases ya ausentes; se remitieron F-01–F-09 a luna para armonizar los registros con el texto real sin reinsertar notas desaparecidas. La primera ejecución de ajustes S1 también alcanzó 600 segundos y requirió continuación; no se declara exitosa esa ejecución interrumpida.

Estado: **cerrado** el hito de recuperación y revisión pendiente; **no cerrado** el lote S1 ni el pendiente bibliográfico global. Las revisiones S2–S4 y sus decisiones se supervisan por separado. No se hicieron commits ni se descartaron cambios ajenos.
