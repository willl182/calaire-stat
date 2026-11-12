# S3. Revisión de contenido y entrega — claude-sol / Opus 5.5 (sustituto)

Fecha: 25 de octubre de 2026. Alcance: exclusivamente `curso/S3_comparacion_decision/`; fase de contenido, no de ejercicios.

## Nota del supervisor

Supervisor actual: Opus 5.5 (claude-opus-5-5) con esfuerzo bajo, en sustitución de claude-sol (gpt-6.1-sol) por cuota agotada. Reanudación: 2026-10-26, hora indicada al pie de esta nota. Se conserva el plan existente, con la ampliación del punto 7. Las ediciones interrumpidas (36 bloques de `auditoria_interrupcion_sol_2/cambios_sol.diff`, identificados aquí como D01–D36 en el orden del diff, y 6 bloques de la ejecución del 2026-10-26 05:26, identificados R01–R06, que solo constan como diferencia entre `versiones/20261026_052610_antes_P4_sol/` y el libreto actual) se tratan como correcciones candidatas, con decisión y fundamento individual; no constituyen revisión aprobada por sí mismas. Entre las instantáneas `20261025_220040` y `20261026_052610` no hubo cambios de libretos. No existe en S3 auditoría C01–C27 (corresponde a S1).

Registro anterior: claude-sol (gpt-6.1-sol), reanudación 2026-10-26 05:26:26 −05:00, interrumpida antes de registrar hallazgos individuales.

Hora de inicio de esta reanudación: 2026-10-26 05:39:03 -0500.

## Plan de revisión

1. Leer íntegramente el plan maestro, la guía, `prop_e.md` y su revisión final; contrastar después, en orden M09 → M10 → M11 → M12, cada libreto con su bitácora y revisión Haiku.
2. Construir una comprobación por nivel acumulativo contra M9–M12 de prop_e: temas completos, sin ampliaciones, un marcador por práctica y ninguna práctica desarrollada; respetar las exclusiones de §6 y distinguir ejemplos narrados de actividades evaluables.
3. Revisar signos, unidades, incertidumbres estándar/expandidas, cobertura, dependencia, hipótesis de las decisiones y origen de los datos; comprobar errores críticos y escalamiento. Recalcular ejemplos clave y ejecutar todos los scripts con `curso/.venv/bin/python`; incorporar aserciones o cálculos adicionales cuando sean necesarios, sin modificar archivos fuera de S3.
4. Verificar las referencias y los numerales de las fuentes locales mediante `pdftotext`, conservando evidencias dentro de S3 si procede. Las fuentes externas ausentes se identificarán expresamente; no se darán por verificadas localmente. Una referencia curricular no sustituirá una fuente técnica.
5. Revisar formato oral, lectura de fórmulas, acotaciones, fichas, niveles, prerrequisitos, continuidad M09–M12 y remisiones AX. Consolidar en S3 una ficha común de criterios para evitar confundir tolerancias, límites de control y umbrales de indicadores.
6. Registrar hallazgos identificados S-…, su severidad, ubicación y corrección; aplicar los cambios y volver a ejecutar las comprobaciones afectadas. Entregar índice de escenas, prácticas pendientes, anexos, datos y estado. Declarar pendientes reales sin equiparar contenido revisado con curso listo para impartir.
7. (Opus 5.5, reanudación.) Decidir cada bloque D01–D36 y R01–R06 comparando versión previa (`versiones/20261025_202101_antes_P4_sol/`, `versiones/20261026_052610_antes_P4_sol/`) y actual: conservar, ajustar o revertir. Verificación de cálculos: ejecutar `calc/M09_ejemplos.py`, `calc/M10_ejemplos.py`, `calc/M11_ejemplos.py`, `calc/M12_indicadores.py`, `calc/M09_M10_verificacion.py`, `calc/S3_verificar_ficha.py` y `calc/S3_verificar_entrega.py` con `curso/.venv/bin/python` y cotejar las cifras citadas en libretos y ficha; recálculo independiente de E_n, u(Δ) con covarianza, riesgos de M10 B/I/A, límites I-MR, deriva de M11-I y límites chi-cuadrado/t de M12. Verificación de referencias: `pdftotext` sobre `docs/` en los numerales nuevos o modificados por las ediciones candidatas y en una muestra de cada capítulo; las fuentes no disponibles en docs/ deben ir marcadas.

## Hallazgos por capítulo

### Transversales

- **S-TR-01 — Menor — Ficha común, párrafo tras la tabla SRP/EPA.** La ruta `calc/fuentes_M09_M10/` no existe. Corregida a `calc/auditoria_M09_M10/`. Se conserva la ficha candidata por cumplir los campos exigidos por prop_e M10 y distinguir ámbitos de decisión. Evidencia: `calc/revision_ficha_actual.md` y extractos `calc/ficha_*_actual.txt`.
- **S-TR-02 — Documental — Recuperación de la interrupción.** S3 contiene una auditoría, `auditoria_interrupcion_sol_2/`, con 36 bloques (11 M09, 6 M10, 10 M11, 9 M12). No existe aquí auditoría C01–C27; el LEEME disponible la atribuye a S1. No se inventan identificadores ni se modifican S1 o registros del orquestador. Los bloques se identifican por capítulo y encabezado `@@`, además de la línea del diff. Las instantáneas en `versiones/` se conservan como evidencia histórica, no como material entregado.

- **S-TR-03 — Menor — Entrega documental.** Faltaba el índice de la sección. Corrección: crear `S3_00_indice.md` con capítulos, escenas por nivel, doce prácticas pendientes, anexos, datos rotulados, estado y pendientes de fase posterior.

### Revisión individual (Opus 5.5)

Identificación: D01–D36 son los bloques `@@` de `auditoria_interrupcion_sol_2/cambios_sol.diff` en su orden (D01–D11 M09, D12–D17 M10, D18–D27 M11, D28–D36 M12); R01–R06 son los bloques de la ejecución interrumpida del 2026-10-26 (`versiones/20261026_052610_antes_P4_sol/` → libreto). Severidad: crítica / mayor / menor / documental.

#### M09
- **S-M09-01 — Menor — Ficha, fila «Datos» (D01).** El rótulo no separaba el grado de equivalencia simulado de A del GGMR adaptado. Corrección candidata correcta: conservar.
- **S-M09-02 — Mayor — B2, cobertura de k=2 (D02).** Se presentaba k=2 sin hipótesis; con normalidad y u conocida da ≈95,45 %, no 95 % [GUM 6.3.3, verificado]. Conservar.
- **S-M09-03 — Menor — Marcador B (D03).** El título omitía la segunda parte de la práctica de prop_e (dos puntos y reconocimiento de la dependencia Level 2–SRP 55). Conservar.
- **S-M09-04 — Mayor — I1, covarianza por patrón compartido (D04, D05).** Faltaba ejemplo numérico del tema cuantitativo de I (guía §3). El ejemplo simulado (u(R)=0,15; c=1 y 0,8; cov=0,018; u(Δ)=0,162788; Δ/U(Δ)=1,0750) se recalculó: correcto, rotulado y con alcance de compatibilidad. Conservar.
- **S-M09-05 — Menor — I2, interpolación (D06).** Faltaba aclarar x0 nominal sin incertidumbre y predicción futura [GUM 5.2.2; ISO 28037 §5.7]. Conservar.
- **S-M09-06 — Menor — I2, compatibilidad frente a conformidad (D07).** Sin referencia técnica; se añadió GUM 5.2.2, ISO 6143 §6.1 e ISO 17025 §7.8.6 (verificados en `calc/auditoria_M09_M10/`). Conservar.
- **S-M09-07 — Mayor — A, alcance del grado de equivalencia (D08, D10, D11).** El texto previo describía el grado de equivalencia sin calcularlo, contra prop_e M9-A (debe enseñarse con números). D10 añade un ejemplo simulado (D=0,30, u(D)=0,25; D=0,80, u(D)=0,781025) frente a referencia común, que se recalculó. Una frase atribuía la covarianza a «entre ejes» y a GGMR, que no rige el cálculo de D. Ajustar esa frase; conservar el resto. D11 añade la entrada ISO 17025 de referencias: conservar.
- **S-M09-08 — Mayor — A1, construcción de matrices y validación (D09).** Se explicita U_x=diag(s²/12)+u_b²xxᵀ, hipótesis de independencia de lecturas, independencia entre ejes y contraste con ISO/TS 28037 Tablas 25–26 (el script reproduce a, b, u, cov y χ²=1,772 con atol 0,0002). Conservar.
- **S-M09-09 — Menor — A1, sensibilidad intraeje (D10 parcial; R01).** R01 precisa que al eliminar la contribución común se elimina también su aporte a la diagonal; coincide con `common=0.0` del script (u(D420)=0,048853). Conservar.

#### M10
- **S-M10-01 — Mayor — B1, cobertura con Student (D12).** La versión previa imponía t(0,975;ν_eff) con pocos grados de libertad sin justificar el modelo. Conservar la redacción condicionada [GUM §6.3, Anexo G].
- **S-M10-02 — Mayor — B2, regla de tres salidas y banda de guarda (D13).** Se llamaba «binaria» a una regla con zona de retención; ahora se da la zona de aceptación [99,2; 101,8] y de rechazo (y<96,8 o y>104,2), recalculadas; se añade ISO 17025 §7.1.3 (verificado). Conservar.
- **S-M10-03 — Menor — I1, TUR y k (D14).** Mismo criterio que S-M10-01. Conservar.
- **S-M10-04 — Mayor — I2, criterios QAPP/TAD (D15; R03).** La versión previa convertía «<+ 1 ppb» en una desigualdad absoluta no escrita en el QAPP y daba criterios TAD incompletos. Verificado con pdftotext: QAPP §6.2.1 («minimum of 12 concentration points», 10 puntos promediados, ≥3 ciclos) y TAD §4.4.1–4.4.2, ecs. 8–9 con divisor 3. R03 añade «al menos» doce: conforme al original. Conservar ambos.
- **S-M10-05 — Mayor — I2, U de lectura individual y certificado (D16).** Se nombra U_prec como contribución parcial (antes se presentaba como U de la lectura) y se añade ISO 17025 §§7.8.2, 7.8.4; sustituye la cita VIM sin numeral por GUM §5.2.2/ISO 17025 §7.8.6. Conservar.
- **S-M10-06 — Crítica — A1, riesgo específico (D17).** La versión previa definía el riesgo específico a valor verdadero fijo, lo que contradice JCGM 106 §9.3.2 (riesgo condicionado al resultado observado). Corregido con posterior uniforme truncada: P(conforme|y=9,5)=0,73466761, recalculada. JCGM 106 (no disponible en docs/) verificado en copia oficial `calc/auditoria_M09_M10/jcgm106_fuente/` (§§6.2, 7.1, 9.3.2, 9.4, 9.5, ecs. 17–18). Conservar.
- **S-M10-07 — Mayor — A2, hipótesis de normalidad conjunta (R02).** Las probabilidades de cola del promedio dependiente requieren distribución conjunta, no solo u y correlación. Conservar R02.

#### M11
- **S-M11-01 — Menor — Ficha, anexos y ficha común (D18).** Conservar.
- **S-M11-02 — Mayor — B2, límites establecidos frente a construcción (D19, D20; R04).** prop_e M11-B da límites establecidos; la construcción (1,128; 2,66; 3,267) pertenece a la línea base de I. Se movió a I1 con fuentes NIST (constantes verificadas en `calc/fuentes_M11/NIST_*.html`) y Crowder §11.2.1 (verificado). R04 aclara que el límite inferior cero de MR proviene del diseño n=2 (D3=0), no de la no negatividad. Conservar.
- **S-M11-03 — Mayor — I1, ejemplo de mezcla de fases (D21, D22).** El ejemplo previo mezclaba la serie de deriva en nmol/mol con la idea de línea base y separaba fases «a conveniencia». El nuevo (medias 0,00016, 0,00116, mezcla 0,00066) se recalculó. Conservar.
- **S-M11-04 — Mayor — I2/I3, supuestos de regresión y deriva en la incertidumbre de uso (D23, D24).** Faltaban supuestos Student y el ejemplo numérico de incertidumbre de uso: Δ(120)=0,36286, u=0,01107, u_uso=0,02286 recalculados; referencias GUM 3.2.3/5.2.2 y Crowder §10.8 verificadas (GUM 5.1.2 reemplazado por 5.2.2, que trata covarianza). Conservar.
- **S-M11-05 — Mayor — A1, EWMA (D25, D26).** Se añaden límites de arranque, unidades adimensionales y cuenta determinista (Z=0,20; 0,36; límites 0,5400; 0,6915), recalculada; NIST-EWMA (web, marcado no disponible en docs/). Conservar.
- **S-M11-06 — Crítica — A2, demoras y riesgo del intervalo (D26, D27).** Las demoras se declaran condicionales y no ARL (hallazgo R01 Haiku); se añade ejemplo numérico de intervalo de revisión bajo riesgo (60 días: 0,00039456), tema A de prop_e que carecía de cifras. Se recalculó con 1−Φ((0,2/T−μ_B)/u_B). Crowder §10.9 (Calibration Interval Analysis) verificado. No resuelve la práctica A: usa otra serie y el marcador sigue sin desarrollar. Conservar, junto con la entrada NIST de referencias (D27).

#### M12
- **S-M12-01 — Menor — Ficha, AX.1 (D28).** Conservar.
- **S-M12-02 — Mayor — I1/I2, hipótesis de los límites y referencias (D29–D32; R05).** Faltaban hipótesis de normalidad/independencia, la advertencia de que t sobre |d| no es exacta y referencias con numeral (Crowder sin numeral sustituido por GUM 4.2.2–4.2.3 y G.3.2, verificados; NIST 1.3.5.8 web). R05 corrige la explicación del cambio de cuantil (parámetro y nivel, no solo número de colas). Conservar.
- **S-M12-03 — Menor — I4, umbral 3s0 con s estimada (D33).** Conservar.
- **S-M12-04 — Menor — A1, unidades en puntos porcentuales (D34).** Conservar.
- **S-M12-05 — Mayor — A3, error numérico en la serie de dos periodos (D35).** La versión previa daba valores 0,5; 1; 2,5; 3,5 cuya media no es 2 % y cuyas medias de periodo no son 1 y 3 %. Con 1,5 todo cuadra (SE 0,6455; 1,000), recalculado. Conservar.
- **S-M12-06 — Mayor — A2, ejemplo cuantitativo de trazabilidad común (D35).** Faltaba cuantificar el efecto común: u(media)=0,9055 (n=2), 0,8276 (n=8), límite 0,80; recalculado. Conservar.
- **S-M12-07 — Menor — A3, remisión a ficha común y referencias (D36).** Conservar.
- **S-M12-08 — Mayor — A3, ejemplo de discrepancia resuelto (R06).** R06 añade, junto al marcador A, la resolución numérica de la misma discrepancia que fija la práctica A de prop_e (conformidad individual frente a desempeño agregado y evidencia necesaria). Ese contenido es la práctica, no un tema de A (los temas son dependencia, mezcla de periodos y trazabilidad común). La guía §1 prohíbe desarrollar el marcador. Revertir a la versión previa y retirar el bloque A3 añadido a `calc/M12_indicadores.py`.

#### Transversal adicional
- **S-TR-04 — Documental — Scripts y auxiliares de `calc/`.** Los cambios en `M09_ejemplos.py`, `M10_ejemplos.py`, `M11_ejemplos.py` y `M12_indicadores.py` respecto de `437e8bf` respaldan cifras de las ediciones conservadas, salvo el bloque A3 de M12 (S-M12-08). Los auxiliares (`M09_M10_verificacion.py`, `S3_verificar_ficha.py`, `S3_verificar_entrega.py`, extractos de fuentes en `auditoria_M09_M10/` y `fuentes_M11/`, `M12_evidencias_fuentes.md`, salidas `.out` y `.txt`) son evidencia de verificación: se conservan. Los extractos de terceros (PDF/TXT/HTML) son copias de trabajo, no material del curso para distribuir.

## Correcciones aplicadas

### Transversales

- **S-TR-01.** Cambio: ruta de evidencias corregida en `S3_01_ficha_criterios.md`; se conserva la ficha candidata con sus ámbitos diferenciados. Comprobación: extractos nuevos `calc/ficha_TAD_actual.txt`, `calc/ficha_CFR_actual.txt`, `calc/ficha_EN_actual.txt`; fuentes identificadas en `calc/ficha_fuentes_sha256.txt`; cifras reproducidas con `calc/S3_verificar_ficha.py`, salida `calc/ficha_recalculo_actual.out`.
- **S-TR-02.** Cambio: inventario y método de identificación explícitos en esta revisión y `calc/revision_ficha_actual.md`; auditorías e instantáneas conservadas sin reescribirlas. Los informes individuales se incorporan a continuación para no dejar decisiones candidatas implícitas.
- **S-TR-03 — Entrega documental.** Se crea `S3_00_indice.md`, con escenas por nivel, doce marcadores de prácticas pendientes, origen de datos, anexos, recursos compartidos y límites de entrega. Se comprobaron sus quince enlaces locales. No se crean ejercicios ni soluciones de prácticas.

### Por capítulo (Opus 5.5)

| Hallazgo | Edición | Decisión y cambio | Ubicación |
|---|---|---|---|
| S-M09-01 | D01 | Conservada | M09, ficha |
| S-M09-02 | D02 | Conservada | M09 B2 |
| S-M09-03 | D03 | Conservada | M09 marcador B |
| S-M09-04 | D04, D05 | Conservadas | M09 I1 |
| S-M09-05 | D06 | Conservada | M09 I2 |
| S-M09-06 | D07 | Conservada | M09 I2 |
| S-M09-07 | D08, D10, D11 | Conservadas; en D10 se ajusta la frase final del grado de equivalencia: «Si participante y referencia compartieran contribuciones relevantes, habría que incluir su covarianza en u(D) [GUM 5.2.2; AX.9]; no la anulamos por conveniencia.» | M09 A2 |
| S-M09-08 | D09 | Conservada | M09 A1 |
| S-M09-09 | D10 (sensibilidad), R01 | Conservadas | M09 A2, párrafo de sensibilidad |
| S-M10-01 | D12 | Conservada | M10 B1 |
| S-M10-02 | D13 | Conservada | M10 B2 |
| S-M10-03 | D14 | Conservada | M10 I1 |
| S-M10-04 | D15, R03 | Conservadas | M10 I2 |
| S-M10-05 | D16 | Conservada | M10 I2 y referencias |
| S-M10-06 | D17 | Conservada | M10 A1 y referencias |
| S-M10-07 | R02 | Conservada | M10 A2 |
| S-M11-01 | D18 | Conservada | M11 ficha |
| S-M11-02 | D19, D20, R04 | Conservadas | M11 B2, I1 |
| S-M11-03 | D21, D22 | Conservadas | M11 I1 |
| S-M11-04 | D23, D24 | Conservadas | M11 I2, I3 |
| S-M11-05 | D25, D26 (EWMA) | Conservadas | M11 A1 |
| S-M11-06 | D26 (CUSUM/demoras), D27 | Conservadas | M11 A2 y referencias |
| S-M12-01 | D28 | Conservada | M12 ficha |
| S-M12-02 | D29–D32, R05 | Conservadas | M12 I1, I2 |
| S-M12-03 | D33 | Conservada | M12 I4 |
| S-M12-04 | D34 | Conservada | M12 A1 |
| S-M12-05, S-M12-06 | D35 | Conservada | M12 A2, A3 |
| S-M12-07 | D36 | Conservada | M12 A3 y referencias |
| S-M12-08 | R06 | Revertida al texto de `versiones/20261026_052610_antes_P4_sol/M12_libreto.md` (párrafo eliminado); retirado el bloque «Discrepancia docente A3» de `calc/M12_indicadores.py` | M12 A3, antes del marcador A; script |
| S-TR-04 | scripts `calc/` | Conservados salvo S-M12-08; reejecución completa en `calc/revision_opus_final.out` (7 scripts, rc=0) | `calc/` |

### Verificación transversal

Se leyeron íntegramente `curso/00_plan_maestro.md`, `curso/guia_libreto.md`, `prop_e.md` y `revision_final_prop_e.md`. Se mantiene orden M09, M10, M11, M12. La revisión individual incluye cada libreto, su bitácora y la revisión Haiku; estas últimas son antecedentes, no sustitutos de verificar el texto final.

Los anexos AX.1, AX.2 y AX.8–AX.12 existen en S4 con los títulos de la guía; solo se comprueban destinos, sin modificar ni aprobar S4. La notación común conserva referencia/indicación, signo de la diferencia, u/U y cobertura; las variables locales de series, probabilidades e indicadores se definen en sus escenas. La reiteración breve de dependencia, cobertura y ámbitos responde a prerrequisitos acumulativos, sin repetir deducciones. Compatibilidad (M09), conformidad (M10), control (M11) e indicadores agregados (M12) se mantienen como preguntas diferentes.

El control `calc/S3_verificar_entrega.py` pasó inicialmente: seis escenas M09, seis M10, ocho M11, nueve M12; tres marcadores por capítulo, uno por nivel, etiquetas permitidas. No prueba semánticamente que no haya ejercicios desarrollados: esa comprobación pertenece también a la lectura individual. El cierre registrará la ejecución final.

## Estado de entrega

Opus 5.5 (sustituto de claude-sol), 2026-10-26. **Sección S3 entregada en fase de contenido.** Las 42 ediciones interrumpidas (D01–D36, R01–R06) tienen decisión: 40 conservadas, 1 ajustada (D10) y 1 revertida (R06). Scripts reejecutados con `curso/.venv/bin/python` (Python 3.11.15, NumPy 2.4.6, SciPy 1.17.1), todos sin error, con aserciones y contraste ISO/TS 28037 superados (`calc/revision_opus_final.out`). Se verificaron con pdftotext los numerales nuevos o modificados: QAPP §6.2.1/Tabla 7-1; TAD §4.4.1–4.4.2 y ecs. 8–9; ISO 17025 §§7.1.3, 7.8.2, 7.8.4, 7.8.6; Crowder §§10.8, 10.9, 11.2.1; JCGM 106 en copia oficial. Las fuentes web (NIST/SEMATECH, JCGM 106, ILAC-G8, Montgomery) quedan marcadas como no disponibles en docs/. Hay doce marcadores de práctica (tres por capítulo, uno por nivel), sin desarrollo. Índice: `S3_00_indice.md`.

Pendientes que no bloquean esta fase: la interpretación autorizada de la grafía «<+ 1 ppb» del QAPP; los paquetes de práctica B/C/D (datos, enunciados, soluciones, rúbricas) de la fase de ejercicios; la comprobación por Opus (paso 5). La revisión es de contenido; no declara el curso listo para impartir (prop_e §10).
