# Bitácora de desarrollo — M11

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M11)

- **Competencia estadística:** «detectar cambios en una serie, estimar deriva y decidir una acción con criterio de riesgo.»
- **B:** «causas comunes y especiales; carta de individuales y rango móvil con límites establecidos; límites de control frente a tolerancias; reglas de alarma y plan de acción.»
- **Práctica B fijada por prop_e:** «completar la carta de un historial preparado del Level 2 y decidir entre investigar, repetir, retener o recalibrar.»
- **I añade:** «construcción de línea base homogénea; dependencia; regresión de deriva; predicción e inclusión de la deriva en la incertidumbre de uso.»
- **Práctica evaluable I fijada por prop_e:** «con una serie docente homogénea, justificar inclusión/exclusión de observaciones en la línea base, estimar la deriva, evaluar su incertidumbre y predecir el efecto de prolongar el uso.»
- **A añade:** «EWMA y CUSUM; sensibilidad frente a falsas alarmas; intervalos de recalibración justificados.»
- **Práctica evaluable A fijada por prop_e:** «aplicar EWMA y CUSUM con parámetros declarados, comparar detección de un cambio definido y falsa alarma en un horizonte o longitud media de corrida, y proponer un intervalo de revisión bajo el modelo de riesgo especificado.»
- Condiciones de §5 M11: «El historial publicado por el NIST sirve para aprender el método en su propia serie; no es la línea base del Level 2. Los seis días de una calibración no son un historial de largo plazo. El caso C requiere una serie docente homogénea rotulada, con fase estable, cambios, deriva y eventos de mantenimiento identificados; los datos disponibles no acreditan por sí solos las decisiones de seguimiento ni un intervalo real del Level 2.»

### Escenas previstas

1. Ficha: competencia, prerrequisitos M2, M4 y M7; contenido acumulativo y aditivo por nivel; datos con rótulo de origen; referencias y remisiones a AX.12.
2. B1: para qué sirve el control estadístico; distinguir causas comunes de especiales, con ejemplo numérico ilustrativo.
3. B2: carta de individuales y rango móvil con límites suministrados; ejemplo simulado breve de lectura y señal, sin construir práctica; significado de línea central, límites de control y reglas de alarma.
4. B3: separación entre límites de control y tolerancias; interpretación y plan de acción escalonado para alarma, repetición, retención e investigación; marcador de práctica B y señales de escalamiento.
5. I1: construir una línea base homogénea y documentar fase estable, exclusiones justificadas y límites recalculados; contraste entre serie propia y NIST publicado.
6. I2: dependencia temporal, regresión lineal de deriva y diagnósticos; ejemplo docente simulado con pendiente, incertidumbre y predicción a futuro, sin confundir falta de significación con estabilidad.
7. I3: traslado de la deriva a incertidumbre de uso futuro, separada de ruido/repetibilidad; marcador de práctica I.
8. A1: EWMA y CUSUM con parámetros declarados; ejemplo simulado con pequeño cambio, decisión de alarma y falso aviso ilustrativo.
9. A2: sensibilidad de las falsas alarmas según parámetros/horizonte, longitud media de corrida como métrica, relación de riesgo con intervalo de recalibración; ningún intervalo real de CALAIRE; marcador de práctica A.
10. Cierre narrado: síntesis B/I/A, acción estadística versus decisión operacional aprobada, puente a M12.

### Datos y rótulo de origen

- Ejemplos didácticos por nivel: **simulados**, generados de forma determinista en `calc/M11_ejemplos.py`, con parámetros y modelo expresos; no son observaciones ni desempeño de CALAIRE.
- Referencia histórica: serie NIST de diez comparaciones SRP-0/SRP-2, **publicada**, NISTIR 6963 Tabla 4; solo ilustrará una serie ajena en su propio contexto, no será línea base de CALAIRE ni del Level 2.
- F-PSMT-01: conjunto **propio** de seis días, pero no se usarán sus seis días para fijar límites operativos ni como historial de largo plazo; se explicará esa limitación si se menciona.
- No usar datos simulados o publicados para recomendar el intervalo real de recalibración del Level 2.

### Cálculos previstos

`calc/M11_ejemplos.py`, ejecutado con `curso/.venv/bin/python`, reproducirá toda cifra calculada del capítulo: ejemplo B de carta I-MR (rangos móviles, límites establecidos y señal); ejemplo I simulado de regresión de deriva (pendiente, error estándar, intervalo, predicción e incertidumbre predictiva); y ejemplo A (estadísticos EWMA/CUSUM, momento de señal y probabilidad de falsa alarma en horizonte finito por simulación Monte Carlo determinista). El script imprimirá semilla, supuestos y resultados; no se incluirán números calculados sin salida reproducible. Las cifras de una fuente publicada se identificarán como tales y se verificarán documentalmente.

### Referencias a verificar en `docs/` con `pdftotext`

- *Introduction to Statistics in Metrology*, cap. 11, §11.2 y apartados de cartas X-MR; capítulos 10, §§10.8–10.9 sobre deriva y calibración futura/intervalo, solo con numerales comprobados.
- Otto, *Chemometrics: Statistics and Computer Application in Analytical Chemistry*, cap. 9 y tablas de cartas Shewhart, si se usa.
- ISO/IEC 17025:2017 §7.7, vigilancia de validez, tendencias y técnicas estadísticas.
- NISTIR 6963 Tabla 4 y sus cifras históricas, si se nombran cifras concretas.
- EPA TAD 2023 §4/Tabla 4-1 y SRP QAPP, solo si el libreto necesita mencionar periodicidades/criterios publicados; no tratarlos como intervalo estadístico del Level 2 ni como requisito automáticamente aplicable a CALAIRE.
- Todo numeral citado se comprobará con `pdftotext`; lo no verificable se citará sin numeral y se anotará pendiente. No usar prop_e ni temario como respaldo técnico.

### Anexos previstos

- **AX.12:** remisión a varianza del estadístico EWMA y longitud media de corrida EWMA/CUSUM; en el libreto se usan criterios y expresiones sin desarrollar deducciones.
- No se prevén otras remisiones a anexos.

## Ejecución

### Contenido escrito

- Se creó `M11_libreto.md` en partes, en formato de libreto narrado con acotaciones: ficha; B1–B3 y señales de escalamiento; I1–I3; A1–A2 y señales de escalamiento; cierre y referencias.
- Se dejaron exclusivamente los marcadores de práctica de B, I y A en sus ubicaciones; no se redactaron enunciados, soluciones, evidencias ni rúbricas.
- Se desarrollaron: causas comunes/especiales; cartas de individuales y rango móvil con límites dados; distinción de control/tolerancias; reglas y acciones ante alarma; línea base homogénea; dependencia temporal; regresión y predicción de deriva; transferencia a incertidumbre de uso; EWMA/CUSUM, falsas alarmas, longitud media de corrida e intervalo de revisión condicionado al riesgo.
- Se explicitaron los límites del conjunto propio F-PSMT-01 de seis días y del conjunto externo NIST: ninguno sustenta una línea base de largo plazo ni un intervalo real del Level 2. No se asignó una periodicidad a CALAIRE.

### Scripts y resultados

Script: `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M11_ejemplos.py` (ejecución correcta).

- **B, carta I-MR simulada:** serie de ocho desviaciones de pendiente; línea base de las cinco primeras; centro `0,000160000`; `MR̄=0,000425000`; límites I `LIC=−0,000970500`, `LSC=0,001290500`; límite superior MR `0,001388475`; señal I en la observación 6 y señal MR en la 7. Datos, diferencias y límites se imprimen en el script.
- **I, deriva simulada:** pendiente `0,0030238095 nmol/mol/día`; error estándar `0,0000922139`; IC 95 % `[0,0027867662; 0,0032608529]`; p `4,9567×10⁻⁷`; predicción al día 120 `0,4521428571 nmol/mol`; IC de la media `[0,4362415; 0,4680442]`; intervalo predictivo individual `[0,4112915; 0,4929942]`; cambio lineal estimado a 180 días `0,5442857 nmol/mol` (solo extrapolación pedagógica del modelo simulado).
- **A, riesgo simulado:** Monte Carlo con semilla 11026, 100 000 trayectorias iid normales estándar y horizonte 50: EWMA (`λ=0,2`, límites variables con `L=2,7`) alarmó bajo estabilidad en la proporción simulada `0,199090`; CUSUM bilateral (`k=0,5`, `h=5`) en `0,091770`. Con alternativa de desplazamiento `+1σ` desde ocasión 26, detección posterior condicional a no haber alarmado antes: EWMA `0,987946` (total `0,882700`), demora media entre señales detectadas `8,324` observaciones; CUSUM `0,983156` (total `0,944410`), demora media `9,306` observaciones. Son resultados Monte Carlo del modelo declarado, no tasas empíricas ni estimaciones de CALAIRE.

### Referencias verificadas con `pdftotext`

| Clave y ubicación citada | Archivo | Página PDF comprobada | Comprobación |
|---|---|---:|---|
| Intro. Statistics in Metrology §11.2 (y §11.2.2) | `docs/intro_stats_metro_c11.pdf` | 2–3 | `pdftotext` muestra §11.2 “Statistical Process Control (SPC)” en las páginas 2–3; página 3 presenta §11.2.2 “Discussion” y cartas X-MR. |
| ISO/IEC 17025:2017 §7.7 | `docs/BS EN ISO_IEC 17025_2017.pdf` | 21 | `pdftotext` muestra §7.7 “Ensuring the validity of results” y §7.7.1: registro que permita detectar tendencias y aplicación de técnicas estadísticas cuando sea practicable. |
| NISTIR 6963, Tabla 4 | `docs/nistir6963.pdf` | 20 | `pdftotext -f 20 -l 20` muestra “Multiple comparisons of calibration runs for SRP-0 vs SRP-2” y las filas de corridas. |
| Otto 2017, cap. 9, §9.1 y Tabla 9.2 | `docs/Chemometrics Statistics and Computer Application.pdf` | §9.1, pp. 346–349; Tabla 9.2, p. 350 | La revisión comprobó que el capítulo trata validación y control de calidad; la tabla da 3,518 al 99 % para n=2, no el factor 3,267 de MR. El libreto no la usa para constantes I-MR. |

La revisión Haiku verificó los títulos y ubicaciones de Crowder 2020 §§10.8, 10.8.1 y 10.9; se actualizaron las citas del libreto. El contenido de §10.9 no se leyó en detalle. Montgomery se cita como 2013 según la bibliografía de Crowder, con edición no verificada y disponibilidad externa.

### Decisiones tomadas y pendientes

- Los números didácticos se generaron con conjuntos explícitos dentro del script y están rotulados como simulados. No se usó la serie publicada del NIST para fijar límites de CALAIRE.
- La carta B usa factores de límites dados por la convención de la ilustración; no enseña al nivel B a estimar una línea base. La adecuación del diseño y la validación corresponden a niveles posteriores/responsabilidad técnica.
- El ejemplo de regresión incluye intervalos bajo el modelo lineal con residuos independientes; se advierte sobre dependencia y extrapolación. No se atribuyen estos valores a una deriva del fotómetro real.
- EWMA/CUSUM se compararon bajo un modelo nulo común y bajo una alternativa declarada de desplazamiento de `+1σ` desde la ocasión 26, con horizonte 50; se distinguieron falsas alarmas previas y detecciones posteriores. La práctica prevista queda solo como marcador en esta fase.
- Pendiente preparar para una fase posterior el paquete de serie docente homogénea, con fases estable/cambiada y mantenimiento identificados, probar alternativas de varios tamaños y obtener datos largos propios antes de justificar un intervalo real.
- Pendiente para una revisión posterior: confirmar la edición de Montgomery y consultar el contenido de Crowder §10.9 con mayor detalle. Otto §9.1 y Tabla 9.2 se verificaron en la revisión, pero no respaldan el factor de rango móvil usado.

## Correcciones (revisión Haiku)

| Id del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado con cambios | Se mantuvo el cálculo de demora entre trayectorias detectadas; confirmé que el script ya excluía las censuradas y que da 8,324 y 9,306 observaciones. Actualicé el libreto y declaré que la ocasión 26 cuenta como 1. | `M11_libreto.md`, A2; `calc/M11_ejemplos.py`, lógica y salida A | La demora condicional a detección no debe asignar el horizonte completo a trayectorias sin señal. Corrí el script tras la revisión. |
| R02 | aplicado | Diferencié la probabilidad condicionada a no haber alarmado antes del cambio de las detecciones respecto del total: 98,795 %/88,270 % para EWMA y 98,316 %/94,441 % para CUSUM. | `M11_libreto.md`, A2 | El denominador debe declararse; la salida del script reproduce ambas probabilidades. |
| R03 | aplicado | Reemplacé la afirmación errónea por la equivalencia del cambio acumulado en días reales, distinguiendo la pendiente por día de la pendiente por número de observación. | `M11_libreto.md`, I2 | Con una deriva constante por día, el cambio depende del tiempo transcurrido, no del calendario de muestreo. |
| R04 | aplicado | Especifiqué que el primer valor corresponde al día 0 y los siguientes a 30, 60, 90, 120, 150 y 180. | `M11_libreto.md`, I2 | Fija el origen y permite reproducir el intercepto y las predicciones del script. |
| R05 | aplicado con cambios | Alineé B1 y B2 con la línea base de las primeras cinco observaciones; el punto 6 (0,0018) rebasa el LSC y el MR que termina en el punto 7 rebasa su límite. Corregí también el pie `[EJEMPLO]`. | `M11_libreto.md`, B1–B2 | La versión actual de `calc/M11_ejemplos.py` ya calculaba los límites con las cinco observaciones iniciales; la ejecución confirma centro 0,0001600, MR̄ 0,0004250, LSC 0,0012905 y LSC-MR 0,0013885. No recalculé un cambio que el script ya incorporaba. |
| R06 | aplicado con cambios | Dejé 1,128 respaldado por Crowder §11.2.1 (2,66 = 3/1,128 por cálculo, no dato de Crowder; corregido en la revisión Haiku H-06), atribuí D4 = 3,267 a Montgomery, no disponible en `docs/`, y limité Otto a la estructura general de control de calidad (§9.1), no a las constantes I-MR. | `M11_libreto.md`, B2 y Referencias | Otto cap. 9/Tabla 9.2 no respalda D4 = 3,267; según la revisión, su valor tabulado al 99 % para n=2 es 3,518. |
| R07 | aplicado | Verifiqué y conservé en la ficha M2, M3, M4, M7 y M8 como prerrequisitos. | `M11_libreto.md`, Ficha | La ficha ya incluía M3 (dependencia) y M8 (propagación), coherentes con I2–I3; no se requería cambio sustantivo. |
| R08 | aplicado con cambios | Añadí una nota al instructor: Monte Carlo se desarrolla en M13 y aquí se muestra solo el resultado numérico, sin enseñar el método ni asignarlo como competencia de M11. | `M11_libreto.md`, A1 | Mantiene el ejemplo de riesgo requerido sin adelantar el contenido metodológico de M13. |
| R09 | aplicado con cambios | Añadí a I1 un contraste numérico de medias (0,3614 frente a 0,4500 nmol/mol, diferencia 0,0886) condicionado explícitamente a una fase previa hipotética; en A2 incorporé cambios lineales estimados a 30/60/90 días (0,0907/0,1814/0,2721 nmol/mol) y advertí que no determinan un intervalo. Ajusté el script para imprimir la diferencia en el mismo sentido que la narración. | `M11_libreto.md`, I1 y A2; `calc/M11_ejemplos.py`, salida de medias y cambios | Los números se reproducen; la separación de fase es una hipótesis didáctica, no una conclusión sobre los datos. La pendiente y su incertidumbre por sí solas no determinan riesgo de recalibración. |
| R10 | aplicado | Uniformé las claves de cita como Crowder 2020, ISO 17025 y NISTIR 6963; cité ISO 17025 §7.7.1 d) al hablar del uso de cartas y eliminé la repetición «PDF p. 20». | `M11_libreto.md`, B3, I1 y Referencias | Se usa el numeral específico del control con cartas y se evita duplicar la página impresa/PDF. |
| R11 | aplicado | Completé las referencias de Crowder, ISO, NISTIR, Otto y Montgomery con los datos bibliográficos verificados; anoté la edición de Montgomery como no verificada. | `M11_libreto.md`, Referencias del capítulo | La bibliografía ahora identifica autoría, título, año y emisor/editorial; no se afirma una edición no comprobada. |
| R12 | aplicado | Retiré de la narración las notas de desarrollo «numeral pendiente» y «ubicación pendiente»; actualicé Crowder a §§10.8–10.9 y §10.8.1 donde corresponde. | `M11_libreto.md`, B1–A2, Referencias | Los numerales indicados constan en las comprobaciones documentales de la revisión; los datos bibliográficos incompletos que quedan se declaran en referencias/bitácora, no en el texto hablado. |
| R13 | aplicado | Definí $X_t=(x_t-\mu_0)/\sigma$ y aclaré que $k$ y $h$ se expresan en unidades de sigma. | `M11_libreto.md`, A1–A2 | Los parámetros de EWMA/CUSUM solo son interpretables con la escala estandarizada que usa el script. |
| R14 | aplicado | Eliminé «incertidumbre relevante en ambos ejes» de las señales de escalamiento B. | `M11_libreto.md`, Señales de escalamiento B | Esa condición de dos ejes corresponde a comparaciones, no a una carta de observaciones univariada. |
| R15 | aplicado | Reformulé como «ustedes separen al menos cuatro preguntas». | `M11_libreto.md`, B3 | Mantiene el tratamiento de ustedes y mejora la concordancia oral. |
| R16 | aplicado | Cambié la frase confusa por «Una lectura posterior que regresa al centro no permite decir “todo bien”». | `M11_libreto.md`, B3 | Expresa directamente que la recuperación posterior no invalida la alarma inicial. |
| R17 | aplicado | Reformulé la transición a tasas bajo estabilidad con «En el mismo horizonte…» y puntuación continua. | `M11_libreto.md`, A2 | El contraste se entiende al escuchar y evita mayúscula tras dos puntos. |
| R18 | aplicado | Quité «cerca de» antes de la proporción reproducible por semilla. | `M11_libreto.md`, A1 | La proporción se reporta como resultado reproducible de Monte Carlo para esa semilla, no como probabilidad teórica exacta ni como tasa poblacional. |
| R19 | aplicado | Sustituí «distinta orientación de ejes» por «regresión forzada por el origen en lugar de libre». | `M11_libreto.md`, I1 | La revisión de definición de respuesta debe referirse al modelo de regresión, no a la orientación gráfica. |
| R20 | aplicado | Reemplacé «C1» por «los seis días del certificado F-PSMT-01 (datos propios)». | `M11_libreto.md`, A2 | Evita una etiqueta interna desconocida para el alumno e identifica el origen del conjunto. |
| R21 | aplicado | Definí LIC como límite inferior de control y LSC como límite superior de control en la narración B1 y en la acotación de pizarra. | `M11_libreto.md`, B1 | Hace interpretables las abreviaturas cuando se proyectan. |
| R22 | aplicado | Cambié la recta de la pizarra a $y_t=a+b\,t+\varepsilon_t$ y nombré $b$ como pendiente. | `M11_libreto.md`, I2 | Mantiene la convención del curso para rectas. |

### Correcciones adicionales por iniciativa propia

- Unifiqué el ejemplo de B1 con la línea base y los límites recalculados de B2. El borrador anterior afirmaba que 0,0018 quedaba dentro de otros límites, en contradicción con la señal explicada en B2; ahora el mismo dato y límites describen la señal.
- Aclaré que el contraste numérico de I1 supone una fase previa hipotética, no identificada a partir de los siete datos simulados, para no presentar una exclusión sin evidencia.
- Especifiqué en B2 que el rango móvil de 0,0016 termina en la observación 7, no que sea el valor individual de dicha observación.
- Revisé la cita de ISO 17025 para ubicar §7.7.1 d) junto a la mención de cartas de control, y limité su alcance a lo que el apartado respalda.
- Añadí GUM §5.1.2 para la propagación de incertidumbre con covarianza en I3 y comprobé el numeral con `pdftotext` en el PDF de GUM disponible.
- Recalculé con `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M11_ejemplos.py`: confirmó los límites I-MR, medias, regresión, riesgos, probabilidades de detección y demoras consignados arriba. No modifiqué fuera de `curso/S3_comparacion_decision/`.
