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

## Hito 2 — Revisión final Haiku de S2 y S3 — 2026-10-28 16:10

Supervisor: Opus 5.5 (reemplaza a claude-sol). Al reanudar, S1 y S4 ya tenían revisión final Haiku y respuesta de luna; S2 y S3 tenían decisiones de luna (27-10 16:39) posteriores a la primera revisión, sin revisión final. Se lanzaron dos corridas Haiku separadas (solo lectura, salvo su archivo).

Archivos creados: `curso/citas/S2_revision_final_haiku.md`, `curso/citas/S3_revision_final_haiku.md`; registros `curso/logs/citas_S{2,3}_haiku_final.out`.

Hallazgos: S2 F-01–F-09 (F-01 alta: decisiones 2–3 conservan una corrección ya refutada; F-02–F-05 páginas/citas no reproducibles en Otto, ISO 13964; F-06 evidencia en /tmp). S3 F-01–F-09 (F-01/F-02 etiqueta y edición de Montgomery = H-02 de O-02; F-04 sub-claves NIST sin catálogo; F-05/F-06 ISO 17025 numerales y página PDF 24 vs 19; F-07 evidencia NIST web no reproducible; F-08 ASQ p. 366 vs 367–368).

Decisión: todos remitidos al ejecutor para aplicar o rechazar con evidencia de docs/; S3 asume además F-02/F-03 sobre AX e inventario.

Estado: **cerrado** (revisión obtenida); la respuesta se registra en el hito 3.

## Hito 3 — Respuesta del ejecutor a las revisiones finales S2 y S3 — 2026-10-28 16:40

Qué se hizo: dos corridas separadas del ejecutor (continúa a luna) respondieron F-xx con sección «Ronda final» en `S2_decisiones_luna.md` y `S3_decisiones_luna.md`.

Archivos tocados: `M06_libreto.md` (cita :219 NIST → Hahs-Vaughn y Lomax §8.2.1, PDF p. 332), `M10_libreto.md` (:195 retira §7.8.2), `M11_libreto.md` (etiqueta Montgomery), `AX_libreto.md:366` (Montgomery 2013 sin 7.ª ed./ISBN; respaldo Crowder 2020 PDF pp. 96, 145), `curso/citas/inventario.md` (NIST-I/R/EWMA/CUSUM, Hahs-Vaughn 2020), `S2_cotejo.md`, `S3_cotejo.md`, extractos nuevos en `curso/citas/extractos/` (script `s2_ronda_final.sh`).

Verificación del supervisor (pdftotext sobre docs/): Hahs-Vaughn PDF p. 332 contiene Bonferroni; ISO 17025 PDF p. 24 contiene 7.8.4.1; ASQ TUR en PDF pp. 2–3; AX:366 coherente con M11. Correcto.

Decisión: aceptadas. Rechazos/diferidos admitidos: S2 F-07 (anclas de línea; requiere regenerar inventario), F-09 (manifest fuera de alcance); S3 F-07 NIST §1.3.5.8 sin copia local → queda «no verificable (copia local pendiente)».

Estado: **cerrado** para S2 y S3 con limitaciones declaradas.

## Hito 4 — Unificación de claves entre capítulos (incluye H-02 de O-02) — 2026-10-28 17:45

Qué se hizo: el ejecutor unificó claves en M00–M13 y AX y creó `curso/citas/unificacion_claves.md` (variante → clave final → archivo:línea, recuento de marcas). Montgomery queda en dos claves para dos obras: «Montgomery 2013» (*Introduction to Statistical Quality Control*, etiqueta única «clave bibliográfica; contenido no cotejado») y «Montgomery DAE» (*Design and Analysis of Experiments*, 9.ª ed., Wiley, 2017). El supervisor comprobó en `docs/Introduction to Statistics in Metrology.pdf` (bibliografía, pdftotext l. 13751 y 20527–20528) ambas fichas. Esto sustituye la «10.ª ed., 2020» no verificable de M05:309. También se unificaron: Hahs-Vaughn, Crowder 2020, EPA-TAD, SRP-QAPP y SRP-SOP.

Archivos tocados: libretos M05, M06, M11 y AX (solo citas); `curso/citas/inventario.md` (Montgomery DAE, Searle–Casella–McCulloch, Efron–Tibshirani 1993); `curso/guia_libreto.md` §5 (4 filas nuevas); `curso/citas/unificacion_claves.md`; revisión `curso/citas/unificacion_revision_haiku.md`; registros `curso/logs/citas_unificacion_{luna,haiku,luna2}.out`.

Hallazgos de Haiku (U-01–U-06) y decisión:
- U-01: la cita NIST en M06:219 se había sustituido. Se restituyó NIST §7.4.7.3 y se mantuvo Hahs-Vaughn §8.2.1 (PDF p. 332, Bonferroni) como apoyo. La descripción quedó corregida.
- U-02: cambios de cifras en M02/M06. Quedan **fuera de alcance**: son obra del supervisor de prácticas en paralelo y no se tocaron.
- U-03: recuento corregido. Hay 63 líneas y 69 ocurrencias de «no disponible en docs/».
- U-04/U-06: aplicados.
- U-05: aplicado en las citas de M05.

Estado: **cerrado con limitaciones**. Las claves Huber 1981, CIPM MRA-G-13, ILAC-P14, ILAC-G8, JCGM 106, Milton 2006, CALAIRE R&R, F-PSMT-01 y Johnson et al. aún no tienen fila en el inventario o la guía.

## Cierre — 2026-10-28 17:50

- Los lotes S1–S4 quedaron inventariados y cotejados. Cada uno tiene revisión Haiku, revisión final y respuesta del ejecutor.
- Los estados están en `curso/citas/S{1..4}_cotejo.md`. Las decisiones están en `S{1..4}_decisiones_luna.md`. La evidencia reproducible está en `curso/citas/extractos/`.
- H-02 de O-02 (Montgomery) quedó resuelto como dos claves distintas, ambas verificadas por ficha bibliográfica en docs/. Su contenido técnico no está cotejado y así se declara en el texto.
- Las marcas «no disponible en docs/» son ahora 69 ocurrencias en 63 líneas. Son ausencias declaradas, no errores. No se inventaron páginas.
- Pendientes que impiden dar por cerrado del todo el pendiente 1 de `revision_final.md`:
  - (a) catalogar las claves listadas en el hito 4;
  - (b) NIST §1.3.5.8 sin copia local;
  - (c) anclas de línea del inventario S2 obsoletas (S2 F-07);
  - (d) manifest con rutas no portables (S2 F-09);
  - (e) las fuentes externas (Montgomery, Huber, Efron–Tibshirani) siguen «no verificable» en su contenido.
- No se hicieron commits.
