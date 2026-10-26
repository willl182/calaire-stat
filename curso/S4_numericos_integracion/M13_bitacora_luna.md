# M13 — Bitácora de desarrollo (claude-luna)

## Plan

### Alcance curricular (tomado literalmente de `prop_e.md`)

La ficha sitúa M13 como «Métodos numéricos (solo nivel A)»; por tanto, no hay contenido asignado a B ni a I y el capítulo los declarará expresamente «no asignados» (no se crearán secciones B o I). Competencia: «contrastar la propagación lineal con métodos numéricos y decidir cuál usar».

Temas incluidos, sin añadir contenidos curriculares:

1. «Monte Carlo (GUM S1): propagar distribuciones conservando dependencias y comparar con la linealización en una calibración inversa».
2. «Salidas múltiples (GUM S2): obtener pendiente, intercepto y valores corregidos con su covarianza».
3. «Remuestreo: bootstrap con la unidad de remuestreo que exige el diseño, respetando bloques o agrupaciones».
4. «Robustez: regresión robusta de Huber como método definido, comparada con OLS ante una observación influyente; se explicitan sus supuestos y límites».

La práctica integradora evaluable de prop_e se conservará únicamente como marcador, con su título breve; no se escribirán consigna, datos, solución, evidencia ni rúbrica en esta fase. El capítulo distinguirá los ejemplos ilustrativos narrados de dicha práctica.

### Escenas previstas

- **Ficha del capítulo:** competencia estadística, prerrequisitos M3/M7/M8, alcance únicamente A, resumen de datos simulados con rótulo y notas sobre anexos/referencias.
- **Nivel A — lo que se añade:** explicar que B e I no tienen secciones en este módulo y que A integra sus prerrequisitos, sin volver a enseñar los módulos previos.
- **Escena A1, decisión entre propagación lineal y Monte Carlo:** calibración inversa recta; modelo con entradas correlacionadas, distribuciones explícitas, muestreo conjunto, cuantiles e incertidumbre; comparación didáctica con propagación lineal, diagnóstico de no linealidad y advertencia sobre conservación de dependencia. Remisión a AX.13.
- **Escena A2, varias salidas y covarianza:** parámetros de recta y resultados corregidos como vector de salidas; matriz de covarianza, covarianzas y correlaciones interpretadas en un ejemplo numérico. Remisión a AX.5 y AX.9 solo donde corresponda, sin deducirlos.
- **Escena A3, bootstrap acorde con el diseño:** distinguiremos remuestreo de observaciones independientes de remuestreo por día/bloque; ejemplo de campañas con lecturas agrupadas, interpretación del intervalo y limitaciones con pocos bloques. Sin usarlo como solución universal para dependencia.
- **Escena A4, regresión robusta de Huber frente a OLS:** conjunto simulado con punto influyente, definición operativa del estimador y función de pérdida/pesos, resultados comparados y límites; no presentar robustez como permiso para eliminar datos.
- **Práctica integradora evaluable:** solo marcador literal de la guía.
- **Cierre:** resumen de decisión estadística y transición al bloque de anexos.

### Datos y rótulo de origen

Todos los números de los ejemplos serán **simulados**, producidos determinísticamente por `calc/M13_ejemplos.py` con semilla fija. Se describirá que representan una calibración docente esquemática; no proceden del certificado F-PSMT-01 ni describen resultados de CALAIRE. El diseño simulado tendrá varios niveles de referencia y observaciones agrupadas por día; un valor influyente se incluirá deliberadamente solo en el ejemplo robusto y se identificará como alteración simulada para estudiar sensibilidad, no como dato real.

### Cálculos previstos

1. Propagación inversa mediante derivadas de primer orden y simulación conjunta de entradas con correlación no nula; cuantiles centrales, media, desviación y diferencia respecto de la aproximación lineal.
2. Ajuste lineal ilustrativo, matriz de covarianza conjunta de intercepto y pendiente; covarianzas/correlaciones de salidas corregidas en varios niveles; comparación con simulación Monte Carlo.
3. Bootstrap de pares completos de días, conservando dentro de cada día los niveles/lecturas; distribución de pendientes y de una corrección; percentiles y comparación explícita con el remuestreo ingenuo de filas cuando se incluya.
4. Ajustes OLS y Huber en la misma serie; estimaciones de pendiente/intercepto, predicciones y residuos relevantes antes/después del punto influyente.
5. Un script o scripts `M13_*.py` reproducirán cada valor citado; se ejecutarán con `curso/.venv/bin/python` y sus resultados quedarán registrados aquí.

### Referencias por verificar

- GUM-S1 (JCGM 101:2008), fundamentos y procedimiento de Monte Carlo; verificar numerales en el PDF de `docs/` con `pdftotext`.
- GUM-S2 (JCGM 102:2011), múltiples magnitudes de salida/covarianza; verificar numerales en el PDF de `docs/`.
- *Introduction to Statistics in Metrology*, cap. 8 y §7.6, para Monte Carlo y salidas múltiples; verificar libro/capítulos disponibles en `docs/`.
- ISO/TS 28037:2010, cláusula 10, para contexto de regresión con incertidumbres; verificar numeral en `docs/ISO 28037.pdf`.
- Milton et al. (2006), solo si se usa para contextualizar ajuste generalizado; no exceder el contenido M13.
- ISO 5725-5 y Brereton, cap. 6, como posibles apoyos a límites/robustez; numerales solo si se comprueban en `docs/`.
- Prop_e §5 M13 fija alcance, no se usará como fuente técnica.

### Anexos previstos

- AX.5: remisión para ecuaciones normales/covarianza de parámetros de regresión.
- AX.9: remisión pertinente al tratar diferencias de resultados con entradas compartidas, sin desarrollar su deducción.
- AX.13: remisión al fundamento de Monte Carlo y control del número de ensayos.

No se anticipa remitir a otros anexos salvo necesidad que no amplíe el temario.

## Ejecución

### Contenido escrito

- `M13_libreto.md` quedó redactado como libreto narrado en español, en cuatro escenas A1–A4: propagación lineal frente a Monte Carlo en calibración inversa; pendiente, intercepto y correcciones como salidas conjuntas; bootstrap por días completos; y Huber frente a OLS en un conjunto con una respuesta alterada deliberadamente.
- Se incluyó ficha con competencia, prerrequisitos, origen de datos y remisiones a AX.2, AX.5, AX.9 y AX.13; no hay secciones B ni I, conforme a la asignación literal de prop_e (M13 solo A).
- La práctica integradora evaluable aparece únicamente como marcador de fase de ejercicios; no se desarrollaron consigna, ejercicios, soluciones, evidencias ni rúbricas.
- Se narraron errores críticos y señales de escalamiento: dependencia omitida, simulación no estable, matriz de covarianza no admisible, unidades de remuestreo no justificadas, pocos bloques, ajuste sensible a observación influyente, escala Huber no sustentada y predicción fuera del rango validado.
- Todos los ejemplos son simulados, con semilla reproducible. El punto influyente se creó al añadir deliberadamente 8 nmol/mol a una respuesta simulada; no se atribuye ningún resultado a CALAIRE ni al certificado F-PSMT-01.

### Scripts y resultados

Script ejecutado con `curso/.venv/bin/python curso/S4_numericos_integracion/calc/M13_ejemplos.py`; resultado exitoso. Único script: `calc/M13_ejemplos.py` (semilla 13024; Monte Carlo con 400 000 ensayos; bootstrap por conglomerados con 20 000 réplicas). Reproduce todos los valores numéricos de los ejemplos.

- **A1, inversa y Monte Carlo:** entradas medias `[420; 0,40; 1,002]`, desviaciones `[0,80; 0,50; 0,002]`, correlación intercepto-pendiente `−0,60`. Sustitución de medias: `418,762475` nmol/mol; incertidumbre lineal `1,041437` nmol/mol. Monte Carlo: media `418,763825`, desviación `1,040327` nmol/mol e intervalo central del 95 % `[416,733012; 420,803052]` nmol/mol. Diferencia MC menos lineal para la incertidumbre: `−0,001110` nmol/mol.
- **A2, salidas múltiples:** seis días por seis niveles (`40, 100, 180, 260, 340, 440` nmol/mol; 36 observaciones). Ajuste `a=0,65184834` nmol/mol, `b=1,00151145`, `cov(a,b)=−0,0000228357`. Correcciones en 80, 250 y 420 nmol/mol: `−0,771598`, `−1,028158` y `−1,284717` nmol/mol; incertidumbres estándar respectivas `0,063775`, `0,043975` y `0,074756` nmol/mol. El script emite matrices conjuntas de covarianza y correlación; el libreto cita también las covarianzas seleccionadas y correlaciones directamente reproducibles.
- **A3, bootstrap agrupado:** remuestreo de seis días completos en cada réplica. Intervalo percentil del 95 % de la pendiente `[1,00143187; 1,00159362]`; para la corrección a 250 nmol/mol `[-1,21228848; −0,82985981]` nmol/mol.
- **A4, OLS-Huber:** observaciones simuladas en niveles de 20 a 370 nmol/mol; respuesta sin alterar en el nivel final `371,200000` y respuesta modificada `379,200000` nmol/mol. OLS sin alteración `(a=0,49971429; b=1,00201429)`; OLS alterado `(a=−1,10028571; b=1,01534762)`; Huber alterado, escala `0,35` nmol/mol `(a=0,36428572; b=1,00314286)`. Predicciones a 200 nmol/mol: OLS `201,969238` y Huber `200,992857` nmol/mol. Residuos en el punto influyente: OLS `4,621667` y Huber `7,672857` nmol/mol.

### Referencias verificadas con `pdftotext`

Las páginas indicadas son las páginas impresas en los documentos PDF; se verificaron también los textos de los numerales en `docs/`.

| Clave y numerales citados | Archivo comprobado | Página(s) impresa(s) verificada(s) |
|---|---|---|
| GUM-S1 5.3–5.6 | `docs/ISO_IEC Guide 98-3_2008 Suppl.1_2008 - libgen.li.pdf` | 10–14 (incluye 5.4, 5.5 y método de propagación) |
| GUM-S1 6.4.8.4 | mismo archivo | 25 (muestreo de entradas gaussianas multivariadas) |
| GUM-S1 5.10–5.11 | mismo archivo | 16–17 |
| GUM-S1 7.2–7.3 | mismo archivo | 29–30 (número de ensayos y muestreo) |
| GUM-S1 7.5 | mismo archivo | 30–31 (representación de distribución de salida) |
| GUM-S1 7.9.2–7.9.4 | mismo archivo | 33–35 (tolerancia numérica y procedimiento adaptativo; se cita para explicar estabilidad/control de ensayos) |
| GUM-S2 5.2–5.3 | `docs/ISO_IEC Guide 98-3_2008 Suppl.2_2011 - libgen.li.pdf` | 10–12 (etapas de evaluación y distribuciones de entrada) |
| GUM-S2 6.2 | mismo archivo | 15–16 (propagación multivariada explícita y matriz de covarianza) |
| GUM-S2 7.6 | mismo archivo | 27 (estimación de salida y matriz de covarianza asociada) |
| ISO 28037 5.8.1 | `docs/ISO 28037.pdf` | 9 (definición del ajuste OLS) |
| ISO 28037 10.1–10.2 | mismo archivo | 31–32 (modelo de incertidumbres/covarianzas y parámetros de calibración) |

**Pendientes bibliográficos:** Efron y Tibshirani, *An Introduction to the Bootstrap* (1993), y Huber, *Robust Statistics* (1981), se citan sin numeral y se marcan como no disponibles en `docs/`; no se verificó la ficha bibliográfica en el repositorio. No se inventaron numerales para estas fuentes. Prop_e se usa solo para delimitar el contenido, no como respaldo técnico.

### Decisiones tomadas y pendientes

- Se respetó el alcance vigente de `prop_e.md` §5 M13, no la lista de temas de M13 del `temario_curso.md`, que es anterior y más amplia. Por ello no se agregaron regresión no lineal, distancia ortogonal, implementación GGMR propia, ISO 5725-5, PCR/PLS ni uso de IA.
- La comparación Monte Carlo-lineal usa una inversa simulada con entradas correlacionadas; el ejemplo de salidas conjuntas usa la covarianza del ajuste y sensibilidades de las correcciones; el bootstrap conserva días completos; Huber se define por su función de pérdida y escala fija del script.
- AX.2 se añadió a las remisiones previstas al explicar la fórmula de propagación; las remisiones a AX.5, AX.9 y AX.13 quedaron limitadas a las deducciones no desarrolladas en el libreto.
- Queda pendiente la verificación bibliográfica externa de Efron–Tibshirani y Huber, y toda validación independiente del código de producción o de datos reales. El libreto y sus ejemplos no afirman que esos procesos se hayan realizado.

## Correcciones (revisión Haiku)

| Id del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado con cambios | Se sustituyeron las cifras de covarianzas, varianzas, incertidumbres y correlaciones de A2 por las de la matriz agrupada por día que calcula el script. Se declara que solo hay seis conglomerados y que la estimación es poco estable; se actualizaron los signos e interpretaciones de las correlaciones. Se aumentó la precisión impresa del script y se recalculó todo el ejemplo. | `M13_libreto.md`, escena A2 y cierre; `calc/M13_ejemplos.py` | El texto ahora concuerda con `cluster_fit` y el diseño agrupado descrito en A2/A3. La inferencia de covarianza agrupada con seis días es cautelosa, no una estimación precisa entre días. Reejecución con `curso/.venv/bin/python -I`: `var(a)=0,011836755914`, `var(b)=0,000000002191`, `cov(a,b)=−0,000000026130`; `u(c80/c250/c420)=0,108677/0,109195/0,110283`; correlaciones c80–c250, c250–c420 y c80–c420 = `0,9974/0,9974/0,9896`. |
| R02 | aplicado | Se declaró la distribución normal conjunta de entradas, medias, desviaciones y dependencias, y se sustituyó la referencia genérica a distribuciones por la normal declarada. | `M13_libreto.md`, escena A1 | El script usa `rng.multivariate_normal`; describir familia y correlaciones documenta el supuesto efectivo y permite juzgarlo [GUM-S1 6.4.8.4]. |
| R03 | aplicado | Se eliminaron las etiquetas no permitidas «NARRACIÓN DEL INSTRUCTOR» y se separaron los rótulos de error crítico/escalamiento de la prosa narrada. | `M13_libreto.md`, capítulo completo | La guía del libreto §1 delimita las etiquetas de acotación; la narración es prosa dirigida al grupo y no debe quedar en el bloque de cita. |
| R04 | aplicado | Se añadió la cita GUM 5.1.2 a la propagación lineal y sus derivadas, y la referencia bibliográfica completa a la ficha y lista final. | `M13_libreto.md`, ficha, escena A1 y referencias | La GUM 5.1.2 respalda la varianza combinada con coeficientes de sensibilidad y covarianzas; referencia comprobada según el informe de revisión. |
| R05 | aplicado | Se añadió AX.2 a la fila de anexos de la ficha. | `M13_libreto.md`, ficha | La ficha ahora registra la remisión efectivamente usada en A1. |
| R06 | aplicado | Se normalizaron las citas a Efron–Tibshirani y Huber con la marca «no disponible en docs/», quitando notas internas de verificación de la voz del instructor. | `M13_libreto.md`, escenas A3 y A4 | Cumple la forma de citas externas de la guía §5 y mantiene la incertidumbre bibliográfica documentada aquí en la bitácora. |
| R07 | aplicado | «Término aleatorio común» se cambió por «desplazamiento común» fijado en el script; también se aclaró que las variaciones puntuales están fijadas. | `M13_libreto.md`, escena A2 | El script asigna arreglos deterministas; no genera esos efectos al azar. |
| R08 | aplicado | Se añadió el criterio inicial de ensayos de GUM-S1: `10⁴/(1−p)`; para 95 % equivale a 200 000, frente a 400 000 usados, y se conservó la advertencia de revisar estabilidad. | `M13_libreto.md`, escena A1 | El numeral 7.2.2 citado establece ese criterio; evita presentar solo un número de ensayos sin referencia ni base. |
| R09 | aplicado | Se dividieron los pasajes largos de A1, A3 y A4 en párrafos más breves, separando conceptos y decisiones para facilitar la exposición oral. | `M13_libreto.md`, escenas A1, A3 y A4 | La guía §1 pide frases cortas y ritmo oral; la separación no cambia el alcance. |
| R10 | aplicado | Se precisó que la diferencia de incertidumbres es 0,001110 nmol/mol, se reemplazó «resampleamos» por «remuestreamos» y se distinguieron «ensayos» Monte Carlo de «réplicas» bootstrap. | `M13_libreto.md`, escenas A1 y A3 | Corrige la magnitud verbal y emplea terminología española consistente. |
| R11 | aplicado | Se añadió una frase de transición al taller integrador de nivel A, sin describir ni desarrollar su contenido. | `M13_libreto.md`, cierre | Atiende la secuencia curricular posterior a M13 sin salir de la fase de contenido. |
| R12 | aplicado | Las expresiones de las pizarras matemáticas identificadas se pasaron a delimitadores `$$…$$`. | `M13_libreto.md`, escenas A1, A2 y A4 | Sigue la notación matemática de la guía §4 para fórmulas en acotaciones. |
| R13 | rechazado | No se cambió el marcador. | `M13_libreto.md`, marcador de práctica | El archivo ya contenía `> **[PRÁCTICA — fase de ejercicios]**` en negrita, exactamente como exige la guía §1; el hallazgo no procede. |

**Correcciones adicionales por iniciativa propia**

- Se precisó que la matriz agrupada por día, con solo seis días, no permite tratar su varianza estimada como exacta; el script ahora imprime 12 cifras decimales para no mostrar `var(b)` redondeada falsamente a cero. Se recalcularon los resultados y se actualizaron las cifras de A2.
- Se separó en párrafos más cortos otro pasaje largo sobre los límites de Huber, para mantener el ritmo oral.
- Se revisó la afirmación final de reproducibilidad: los ejemplos numéricos del libreto se contrastaron de nuevo con la salida actualizada del script, incluido el intervalo Monte Carlo y las matrices completas de A2.
