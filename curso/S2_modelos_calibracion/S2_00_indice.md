# S2. Modelos de la calibración — índice de entrega

Supervisor del cierre tras Opus: claude-sol (gpt-6.1-sol), esfuerzo bajo. Fecha: 27 de octubre de 2026. Cierre previo de Opus y auditorías conservados. Fase: **solo contenido**. Los niveles son acumulativos: I incluye B; A incluye B e I. La revisión y sus decisiones se documentan en [S2_revision_sol.md](S2_revision_sol.md).

## Capítulos y escenas por nivel

### [M05. Diseño de experimentos](M05_libreto.md)

- **B:** B1, pregunta estadística y diseño; B2, bloques y jerarquía; B3, diseño 12 × 8 × 6 del Level 2; B4, diseños publicados; señales de escalamiento.
- **I:** I1, aleatorización y bloqueo; I2, factoriales e interacciones; I3, robustez y reparto del esfuerzo, relación con potencia.
- **A:** A1, anidación y escalonamiento; A2, planificación R&R; A3, comparación por componentes identificables.
- **Anexo:** AX.4, únicamente fundamentos del modelo de un factor y precisión del promedio. Los modelos multifactor requieren sus fuentes técnicas externas; no se presume que AX.4 los deduzca.

### [M06. ANOVA y componentes de varianza](M06_libreto.md)

- **B:** B1, repetibilidad y precisión intermedia; B2, contribución de precisión al promedio con componentes entregadas; señales de escalamiento. B no ejecuta ANOVA.
- **I:** I1, tabla ANOVA; I2, componentes y su incertidumbre; I3, dos factores e interacción; I4, residuos, heterogeneidad y Cochran; I5, alcance de ISO 5725.
- **A:** A1, analista × campaña y días anidados, limitaciones de los bloques reales; A2, estimaciones negativas, alternativas y sesgo de laboratorio; señales de escalamiento.
- **Anexo:** AX.4, un factor aleatorio y contribución al promedio. AX.11 corresponde a indicadores de M12, no a deducciones de componentes ANOVA.

### [M07. Regresión y calibración inversa](M07_libreto.md)

- **B:** B1, correlación y límites de R²; B2, OLS con intercepto y residuos; B3, intervalo de uso, inversión y signo de corrección; señales de escalamiento.
- **I:** I1, incertidumbre y covarianza de parámetros, intervalos y predicción inversa; I2, origen forzado; I3, WLS y pesos; I4, error puro y falta de ajuste; escalamiento ante incertidumbre relevante en referencia.
- **A:** A1, ambos ejes inciertos y GGMR; A2, residuos ponderados y chi-cuadrado alto o anormalmente bajo. Exclusión expresa de covarianza cruzada no nula.
- **Anexos:** AX.5, OLS/WLS y covarianza de parámetros; AX.6, inversión; AX.7, cobertura aproximada bajo condiciones de independencia; AX.8, GGMR con V_xy = 0.

### [M08. Propagación de incertidumbre](M08_libreto.md)

- **B:** B1, resultado, modelo y tipos A/B; B2, conversiones y dispersión frente a incertidumbre del promedio; B3, presupuesto numérico para entradas independientes y expansión; señales de escalamiento.
- **I:** I1, sensibilidades analíticas y covarianzas; I2, grados de libertad, cobertura y límites de Student; I3, presupuesto completo del promedio de M06 (6 × 8), resultado individual y uso futuro, doble conteo de dispersión residual; I4, cadena SRP 55–Level 2–cliente, inversión y transferencia con sensibilidades y covarianza de parámetros.
- **A:** A1, fuentes comunes en absolutos y diferencias; A2, límites de linealización y función de incertidumbre frente a CMC en todo el intervalo; señales de escalamiento.
- **Anexos:** AX.2, propagación con covarianza; AX.3, distribuciones; AX.7, Welch–Satterthwaite. Monte Carlo se remite a M13, sin desarrollarlo aquí.

Los anexos pertenecen a [AX_libreto.md](../S4_numericos_integracion/AX_libreto.md); no se modificaron durante esta revisión.

## Marcadores de prácticas pendientes

Cada entrada corresponde a un único marcador **[PRÁCTICA — fase de ejercicios]**. No se entregan enunciados, soluciones ni rúbricas.

- **M05-B:** representar diseño 12 puntos × 8 lecturas × 6 días, variación observada y confusión.
- **M05-I:** diseñar factorial de robustez con respuesta, factores, orden y criterio.
- **M05-A:** diseñar R&R para lectura, ciclo, día y analista, efectos, interacciones y denominadores.
- **M06-B:** contribución expandida parcial de precisión del promedio, con y sin componente entre días y k declarado.
- **M06-I:** ANOVA de días en un nivel, errores con signo, componentes y justificación del modelo.
- **M06-A:** R&R, modelos admisibles, interacción y multiplicidad.
- **M07-B:** recta del Level 2, residuos y signo de corrección.
- **M07-I:** comparar OLS/WLS, incertidumbre de uso y validez de falta de ajuste.
- **M07-A:** comparar OLS/WLS/GGMR, componente común y contraste con ISO/TS 28037 en alcance V_xy = 0.
- **M08-B:** presupuesto de un punto y explicación del divisor incorrecto √576.
- **M08-I:** presupuestos individual, promedio y futuro; cadena al cliente; cobertura, grados de libertad y límites.
- **M08-A:** verificar función de incertidumbre punto a punto y en intervalo, máximo puntual con CMC compatible.

## Datos usados y rótulos

- **Propios, solo estructura:** `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`. Doce puntos, diez de concentración y dos de cero; ocho lecturas por punto y día; seis días. No se atribuyen a este certificado los presupuestos ni rectas simulados.
- **Propios, extracción analítica condicionada:** `docs/Resultados R&r_2022 2023 (1).xlsx`, diez hojas por nivel, tres bloques de seis días por analista. Falta confirmar correspondencia bloque–campaña y selección de registros. Las cifras extraídas no constituyen evaluación operativa nueva del laboratorio.
- **Simulados:** valores y reglas explícitos en `calc/M05_diseno.py`, `calc/M06_ejemplos.py`, `calc/M07_ejemplos.py` y `calc/M08_ejemplos.py`. Incluyen factorial, componentes, regresión, covarianzas, presupuestos, cadena y funciones U/CMC. No describen desempeño real de CALAIRE.
- **Publicados, datos numéricos de contraste:** siete pares y matrices de covarianza de ISO/TS 28037:2010 §10.3, tablas 25–26, sin modificar valores ni orientación de ejes; usados en M07-A para comprobar GGMR con `V_xy = 0`, no como resultados de CALAIRE.
- **Publicados, estructuras de diseño:** SRP QAPP, SRP SOP, EPA TAD, EN 14625 e ISO 13964 en M05, y patrón totalmente anidado/escalonado de ISO 5725-3. La adaptación de una jerarquía publicada a un estudio interno se identifica como adaptación, no como diseño normativo ejecutado. GUM, ISO y textos de `docs/` son fuentes técnicas; no se confunden con conjuntos de datos del laboratorio.

## Cálculos y evidencia

Intérprete: `curso/.venv/bin/python`. Scripts bajo `calc/`; informes de comprobación del supervisor y salidas conservados allí. [LEEME de cálculo y evidencia](calc/LEEME_revision_sol.md) distingue scripts docentes, verificadores, extractos y salidas históricas. `calc/ajustes_sol.py` es un registro histórico deshabilitado, no un cálculo que deba ejecutarse. Los extractos de fuentes, respaldos y diffs son evidencia de revisión, no material de clase ni paquetes de ejercicios.

La continuidad de los cuatro diffs con sus instantáneas se verifica sin alterar respaldos mediante `calc/continuidad_auditorias_sol.py`. `calc/inventario_bloques_sol.json` identifica 94 bloques candidatos (M05: 21; M06: 21; M07: 30; M08: 22); a ellos se suman 2 bloques de `auditoria_respaldo_20261026_201411/cambios.diff` (M07 y M08). Los 96 tienen decisión registrada en `S2_revision_sol.md` (todos conservados). `calc/auditoria_entrega_sol.py` comprueba tres marcadores por capítulo, uno en cada nivel, además de cierres, escenas, rutas documentales y huellas heredadas.

## Estado y pendientes

**Estado: corregida tras la revisión Opus y entregada para la fase de contenido** (2026-10-27; ver «Correcciones tras la revisión Opus» y «Estado de entrega» en `S2_revision_sol.md`). Atendidos O-01–O-18: 3 mayores y 15 menores, sin rechazos. Hay 12 marcadores de práctica y 37 escenas. Cinco scripts docentes y controles de entrega y continuidad ejecutados sin error. Salidas actuales: `calc/*_salida_tras_opus_sol.txt`. Nuevos cálculos de promedio, doble conteo y transferencia en `calc/M08_ejemplos.py`. Referencias de R² cotejadas con pdftotext. No existen respaldos posteriores al informe Opus; decisiones históricas permanecen registradas.

La relación con CMC incluye interpretación y acción: piso de declaración cuando sea aplicable una CMC publicada; por encima del cruce simulado de 81,35 nmol/mol, revisar el respaldo de la función propuesta, no reducir la incertidumbre del presupuesto. Esto no aprueba una CMC.

Pendientes: (1) desarrollar las 12 prácticas (fase de ejercicios); (2) confirmar signo, fechas y correspondencia de bloques del libro R&R antes de inferencia; (3) obtener o cotejar las fuentes externas no disponibles en `docs/`, incluidas CIPM MRA-G-13 e ILAC-P14, citadas sin numerales. Revisión Opus del paso 5 completada; este cierre no equivale a nueva aprobación externa. Entregar estos libretos no autoriza a impartir el curso, firmar certificados, aprobar CMC ni usar las herramientas en operación.
