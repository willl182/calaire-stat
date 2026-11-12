# Revisión autorizada de contenido — M11 y M12

Fecha: 26-10-2026. Alcance exclusivo: capítulos M11/M12 y sus cálculos. Trabajo directo, sin delegación. Directorio base: `/home/w182/w421/calaire-stat/curso/S3_comparacion_decision/`.

## 1. Dictamen y límites

Los dos capítulos cubren el contenido de prop_e por nivel y conservan exactamente **tres marcadores de práctica cada uno**, sin desarrollar prácticas, soluciones ni rúbricas. Los ejemplos numéricos resueltos son explicación docente, no paquetes de ejercicios. Los cálculos ejecutados coinciden con las cifras narradas. No se encontró un error numérico crítico vigente.

Se conservan las mejoras de la revisión interrumpida. Se ajusta una justificación incorrecta/incompleta del límite inferior MR, se corrige una explicación de colas y se completa un ejemplo cuantitativo de M12-A. No se revierte íntegramente ningún bloque: el contenido añadido pertinente está respaldado por los modelos declarados.

Esto NO declara los capítulos listos para impartirse: faltan los paquetes de ejercicios, datos y expedientes evaluables de la fase posterior; tampoco valida cartas ni intervalos reales de CALAIRE.

Archivos modificados en este encargo: `M11_libreto.md`, `M12_libreto.md`, `calc/M12_indicadores.py` y este informe. `calc/M11_ejemplos.py` fue leído y ejecutado, no modificado en esta revisión. Se respetaron los cambios preexistentes. No se editaron M09/M10, bitácoras históricas, Haiku, `S3_revision_sol.md`, índice, ficha común ni `S3_verificar_entrega.py`. No se ejecutaron verificadores comunes que pudieran escribir otros productos.

## 2. Lecturas y criterio de revisión

Lectura completa de `prop_e.md`, `curso/guia_libreto.md`, `curso/00_plan_maestro.md` y `revision_final_prop_e.md`; lectura completa de ambos libretos, ambas bitácoras y ambas revisiones Haiku. Lectura de los scripts M11/M12 y los auxiliares propios `calc/M11_verificacion_sol.out` y `calc/M12_evidencias_fuentes.md`. Esos auxiliares se trataron como registros históricos, no como prueba de ejecución presente.

Se localizaron y leyeron todos los bloques M11/M12 de `auditoria_interrupcion_sol_2/cambios_sol.diff` (líneas 242–457). El diff es de formato `--- previo/` / `+++ actual/`, no un diff con cabeceras `diff --git`. No contiene bloques de scripts M11/M12: los cambios de los scripts actuales se revisaron directamente, sin inventarles un origen en ese diff. Los bloques de otros capítulos no forman parte del dictamen exclusivo.

La revisión Haiku describe versiones anteriores. En particular, sus antiguas cifras I-MR y demoras censuradas no son defectos que sigan presentes: se cotejó el código actual, no se reaplicaron automáticamente las recomendaciones. Se mantiene la simulación de riesgos como resultado docente suministrado, sin adelantar la enseñanza de Monte Carlo de M13.

## 3. Fidelidad por nivel

| Capítulo/nivel | Cobertura comprobada | Resultado |
|---|---|---|
| M11-B | Causas comunes/especiales; lectura I-MR con límites dados; control frente a tolerancia; reglas y plan de acción | Conforme. La estimación de límites queda en I, no en B. Se completa el centro MR suministrado. |
| M11-I | Homogeneidad y exclusiones justificadas; dependencia; regresión de deriva, intervalos, predicción e incertidumbre de uso | Conforme. Se distingue media predicha, lectura futura e incremento de la misma recta. |
| M11-A | EWMA/CUSUM explícitos; falsa alarma y detección con horizonte; revisión bajo riesgo declarado | Conforme. Demora condicional no es ARL; el modelo normal de pendiente es suministrado, no inferencia exacta de siete datos. |
| M12-B | Diferencia relativa, denominador/signo; media absoluta frente a magnitud de media; cero y métrica absoluta | Conforme. No se impone meta EPA como tolerancia local. |
| M12-I | Chi-cuadrado/t; unilateral/bilateral; escala; dispersión del cero y umbral condicionado | Conforme tras aclarar la explicación de colas. No se promete cobertura exacta para magnitudes con n=4. |
| M12-A | Dependencia, periodos, trazabilidad común y discrepancia individual/agregado | Conforme; se añade contraste numérico resuelto, con criterios docentes separados. |

No se introducen Allan, ISO 13528, promedios regulatorios ambientales, GGMR fuera de alcance ni temas excluidos. Las referencias al CFR son indicadores de controles de calidad, no valores de diseño ambiental. Los ejemplos de 100 nmol/mol no se presentan como una ejecución del diseño reglamentario de controles de O3.

## 4. Hallazgos y decisiones M11

Las severidades de los bloques conservados califican el problema que previenen, no un defecto todavía abierto. Estado «conservado/verificado» significa que no se necesitó nueva edición.

| ID | Ubicación | Severidad | Hallazgo, fundamento y corrección/decisión |
|---|---|---|---|
| S-11-01 | Ficha: anexos y ficha común | Menor | Conservar AX.2 y enlace a criterios: la propagación con covarianza está realmente utilizada en I3 y los criterios docentes no son operativos. |
| S-11-02 | B2 e I1: límites I-MR | Mayor | Conservar traslado de estimación a I. B debe aplicar límites suministrados; I construye la base. Factores 1,128, 2,66 y 3,267 cotejados con Crowder/NIST. |
| S-11-03 | I1: ejemplo de fases | Mayor | Conservar sustitución de la serie con deriva por dos fases explícitas de pendientes desplazadas. Medias 0,0001600 / 0,0011600 / 0,0006600 reproducidas. No acredita estabilidad con cinco puntos ni causa real de mantenimiento. |
| S-11-04 | I2: supuestos de inferencia | Mayor | Conservar normalidad, homocedasticidad, independencia, media lineal y tiempo conocido. El p pequeño no valida supuestos. |
| S-11-05 | I3: GUM y propagación de deriva | Mayor | Conservar corrección de GUM 5.1.2 a 5.2.2 para covarianzas; conservar incremento b·t y su incertidumbre. Cancelación del intercepto correcta para dos puntos de la misma recta; cuadratura inicial solo con independencia declarada. |
| S-11-06 | A1: estandarización y límites EWMA | Mayor | Conservar X adimensional, definición de sigma, inicialización y límites variables. NIST respalda recurrencia y límite estacionario; el límite finito se comprueba por suma de pesos, no se atribuye literalmente a esa página. |
| S-11-07 | A2: CUSUM | Mayor | Conservar inicialización en cero, umbral estricto y ejemplo constante: señal en 11 para ambos métodos. k de CUSUM no es factor de cobertura. Copia NIST respalda recurrencias tabulares. |
| S-11-08 | A2: demoras | Mayor | Conservar advertencia de censura. 8,324/9,306 son medias entre detecciones dentro del horizonte, condicionadas a supervivencia previa; no ARL fuera de control. Código excluye el centinela 50 de detectadas. |
| S-11-09 | A2: revisión bajo riesgo | Mayor | Conservar modelo B normal suministrado y condición inicial exactamente corregida. Para D(t)=Bt y techo positivo, cruce antes de T equivale a excedencia final; 60 días cumple el 5% entre los tres candidatos. No es intervalo del Level 2. |
| S-11-10 | Referencias finales | Menor | Conservar GUM 3.2.3/5.2.2 y claves NIST con URLs. Montgomery sigue identificado como fuente externa, edición no verificada; no se simula una consulta directa a ese libro. |
| S-11-11 | B2: frase sobre LIC-MR | Menor, corregido | Que un rango no pueda ser negativo no implica que toda carta R tenga LIC=0: NIST-R muestra D3 positivo para tamaños mayores. Se precisa que cero corresponde al diseño de pares; se añade el centro MR=0,0004250 suministrado. No cambia cifra ni algoritmo. |

## 5. Hallazgos y decisiones M12

| ID | Ubicación | Severidad | Hallazgo, fundamento y corrección/decisión |
|---|---|---|---|
| S-12-01 | Ficha: anexos | Menor | Conservar AX.1: divisor n−1 y grados de libertad sí intervienen en I. |
| S-12-02 | I1: límite chi-cuadrado | Mayor | Conservar supuestos iid normales, población homogénea y varianza constante para exactitud. La serie determinista ilustra aritmética, no prueba cobertura. GUM define s; CFR fija el indicador y el cuantil inferior. |
| S-12-03 | I2: límite de magnitudes | Mayor | Conservar advertencia: valores absolutos de normales no son normales; la fórmula regulatoria con n=4 no acredita cobertura exacta del 95%. AS corresponde a magnitudes, no a diferencias firmadas. |
| S-12-04 | I2: intervalo bilateral y colas | Menor, corregido | Conservar sustitución de cita pendiente por GUM 4.2.2–4.2.3/G.3.2. Ajustar «cola de cobertura»: lo que se reparte entre colas es la probabilidad de no cobertura. No atribuir los diferentes cuantiles de precisión/sesgo solo a unilateralidad: ambos límites son superiores, con distribuciones y niveles distintos. |
| S-12-05 | I4: umbral del cero | Mayor | Conservar advertencia sobre sigma estimada con cinco respuestas: ±3s0 no garantiza falsa alarma de sigma conocida ni constituye LOD universal. EN usa 3,3 sr,z/B bajo su diseño propio. |
| S-12-06 | A1: unidades y lectura oral | Mayor | Conservar puntos porcentuales y covarianzas en puntos porcentuales cuadrados. Conservar corrección de «uno» a «uno y medio»: debe narrarse 1,5 para coincidir con datos, media y errores estándar. |
| S-12-07 | A2: componente común | Mayor | Conservar ejemplo cuantitativo ucom=0,8, uind=0,6: u(media)=0,9055/0,8276 para n=2/8. Matriz positiva definida; cuadratura independiente no elimina la componente común. |
| S-12-08 | A3: ficha y criterios | Mayor | Conservar consulta a ficha y distinción tolerancia/control/indicador. No se editaron ni validaron valores de la ficha común en este encargo. |
| S-12-09 | Referencias finales | Menor | Conservar GUM verificada y retirada de Crowder incompleto. El numeral NIST de chi-cuadrado permanece como referencia externa; no se logró renovar la comprobación web en esta sesión (véanse pendientes). |
| S-12-10 | A3 y calc/M12_indicadores.py | Mayor, corregido | Faltaba un contraste numérico explícito de discrepancia individual/agregado en la explicación. Se reutilizan cuatro verificaciones de B: última e=2, U=0,5, intervalo [1,5;2,5] dentro de tolerancia docente ±3; el límite agregado 4,1367% excede umbral docente 4%. Se declaran periodo, referencia, muestra, cobertura, regla, independencia y carácter inventado de criterios. Script reproduce ambos juicios y los comprueba con assert. No se desarrolla la práctica. |
| S-12-11 | Bitácora/evidencias históricas: localizador CFR | Menor, documentado | La meta §2.3.1.2 se encuentra en página PDF 5 (no 4 como registró la bitácora). Se verifica en extracción actual; no se edita el registro histórico. Similarmente ISO 17025 §7.7 comienza en PDF 21, pero d) está en PDF 22. El libreto no contiene esos localizadores PDF erróneos. |

## 6. Mapa exhaustivo del diff interrumpido

Identificador de bloque = archivo + cabecera `@@`; las líneas son del archivo de auditoría, no del libreto actual. Un bloque puede contener varios cambios, todos cubiertos por las decisiones que se indican.

### M11_libreto.md — 10 bloques

| Líneas diff / cabecera | Contenido completo del cambio | Decisión / hallazgos |
|---|---|---|
| 244–253 / `@@ -10,7 +10,8 @@` | AX.2 y enlace ficha común | Conservar, S-11-01. |
| 254–265 / `@@ -41,9 +42,9 @@` | Quitar construcción de límites de B; suministrar límites y preservar ejemplo | Ajustar parcialmente, S-11-02 y S-11-11: se conserva separación B/I; se precisa LIC-MR y centro. |
| 266–279 / `@@ -81,11 +82,11 @@` | Reemplazar ejemplo de fases; añadir estimación I-MR y dependencia de rangos | Conservar, S-11-02/03. |
| 280–288 / `@@ -101,7 +102,7 @@` | Supuestos adicionales de Student/p | Conservar, S-11-04. |
| 289–301 / `@@ -119,7 +120,11 @@` | GUM 5.2.2; pizarra de propagación; incremento/corrección y presupuesto | Conservar, S-11-05. |
| 302–319 / `@@ -135,13 +140,15 @@` | Estandarización; sigma; límites EWMA de arranque; dos pasos numéricos | Conservar, S-11-06. |
| 320–330 / `@@ -151,7 +158,9 @@` | Fuente NIST-CUSUM; inicialización; ejemplo de señal estricta | Conservar, S-11-07. |
| 331–339 / `@@ -159,6 +168,8 @@` | No confundir demora condicional/censurada con ARL | Conservar, S-11-08. |
| 340–352 / `@@ -171,6 +182,12 @@` | Modelo de pendiente normal; fórmula de cruce; riesgos 30/60/90 | Conservar, S-11-09. |
| 353–365 / `@@ -195,10 +212,11 @@` | Actualizar numerales GUM y añadir bibliografía NIST | Conservar, S-11-10. |

### M12_libreto.md — 9 bloques

| Líneas diff / cabecera | Contenido completo del cambio | Decisión / hallazgos |
|---|---|---|
| 368–376 / `@@ -10,7 +10,7 @@` | Añadir AX.1 | Conservar, S-12-01. |
| 377–385 / `@@ -85,7 +85,7 @@` | Fuente s, supuestos chi-cuadrado, límites de datos deterministas | Conservar, S-12-02. |
| 386–394 / `@@ -105,7 +105,7 @@` | Condiciones y límites inferenciales de media absoluta/t | Conservar, S-12-03. |
| 395–408 / `@@ -123,11 +123,11 @@` | Cambiar cita bilateral y eliminar pendiente Crowder con GUM | Ajustar explicación de colas en su contexto; conservar reemplazo bibliográfico, S-12-04. |
| 409–417 / `@@ -153,7 +153,7 @@` | Incertidumbre de s0 y cobertura no garantizada | Conservar, S-12-05. |
| 418–429 / `@@ -177,9 +177,9 @@` | Unidades de porcentajes/covarianzas y corrección oral 1,5 | Conservar ambos cambios, S-12-06. |
| 430–438 / `@@ -198,6 +198,8 @@` | Modelo cuantitativo de trazabilidad común | Conservar, S-12-07. |
| 439–447 / `@@ -217,7 +219,7 @@` | Consulta ficha común antes de separar criterios | Conservar, S-12-08; completar explicación numérica adyacente por S-12-10. |
| 448–457 / `@@ -234,7 +236,6 @@` | GUM ampliada; quitar Crowder pendiente; NIST concreto | Conservar con pendiente de reconfirmación externa documentado, S-12-09. |

No hay bloques M11/M12 adicionales ni bloques de sus scripts en el diff entregado. «Conservar» no significa aceptar todas las afirmaciones de revisiones históricas: se decide sobre el contenido vigente comprobado.

## 7. Fuentes realmente comprobadas en esta revisión

Se usó `pdftotext -layout` sobre los PDF originales de `docs/`, no solo las extracciones heredadas. Los avisos de fuentes de Poppler en Crowder no impidieron leer los pasajes utilizados.

| Fuente | Ubicación realmente leída | Qué respalda / límites |
|---|---|---|
| Crowder, intro_stats_metro_c11.pdf | §11.2, §11.2.1, §11.2.2; pp. impresas 269, 273–274 | Centro/base histórica, sigma=MR/1,128, seguimiento con base congelada y sensibilidad de alternativas EWMA/CUSUM. No se atribuye D4 a Otto. |
| Crowder, intro_stats_metro_c10.pdf | §10.8, inicio de §10.8.1 y §10.9 completo | Deriva, predicción durante uso y análisis de intervalos con probabilidad/costos/datos históricos. §10.9 va más allá de un título: se leyó su método de variables, deltas as-found/as-left y cruce de banda. El modelo normal de pendiente de M11 sigue siendo docente, no fórmula literal tomada de Crowder. |
| ISO/IEC 17025:2017 | PDF 21–22, §7.7.1 y d), §7.7.3 | Vigilancia, cartas y actuación frente a criterios predefinidos. No prescribe las reglas numéricas de alarma ni una recalibración automática. |
| NISTIR 6963 | PDF/impresa 20, Tabla 4 | Diez comparaciones SRP-0/SRP-2; confirma identidad externa. No se recalcula ni se usa como base Level 2. |
| Otto 2017 | Copyright Wiley-VCH 2017; §9.1, texto de control de calidad, pp. impresas 347–348 | Respaldo general de cartas; no respaldo de D4=3,267. No se afirma aquí haber revalidado su Tabla 9.2 completa. |
| GUM | PDF 13, §3.2.3; PDF 18, §§4.2.2–4.2.3; PDF 29, §§5.2.1–5.2.2; PDF 80, G.3.2 | Corrección ≠ incertidumbre; divisor n−1; incertidumbre del promedio; covarianzas; Student con normalidad e independencia. |
| CFR58-A | §2.3.1.2 en PDF 5; §3.1.1 en PDF 7; §§4.1.1–4.1.3.2 en PDF 18–20 | Metas O3 7% con coberturas diferentes; diseño original; meas/audit; indicador de precisión y sesgo; signo por percentiles. Las ecuaciones son imágenes: cotejadas visualmente con `calc/verificacion_fuentes_agente/CFR_p18.png` y `CFR_p19.png`, además del texto original extraído. |
| EN 14625:2012 | PDF 10 §3.12; PDF 19 Tabla 1; PDF 25–26 §8.4.5, ecuación 5 | LOD=3,3 sr,z/B, repetibilidad en cero y diseño de veinte mediciones. El ejemplo de cinco ceros no pretende cumplir ese ensayo. |
| NIST e-Handbook | Copias HTML locales completas `calc/fuentes_M11/NIST_IMR.html`, `NIST_constants.html`, `NIST_EWMA.html`, `NIST_CUSUM.html`, leídas como texto | Numerales 6.3.2.2, .1, .4 y .3: rango móvil, 1,128; fila n=2, D3=0/D4=3,267; recurrencia/varianza estacionaria EWMA; CUSUM tabular y umbral excedido. No se ejecutaron scripts de los HTML. No es una nueva consulta web. |

## 8. Cálculos ejecutados y contraste

Intérprete solicitado: `/home/w182/w421/calaire-stat/curso/.venv/bin/python`. Ejecuciones de ambos scripts completas, terminadas sin error; M12 vuelto a ejecutar después de su modificación. Comprobaciones auxiliares con el mismo intérprete en modo `-I`. Entorno observado: NumPy 2.4.6, SciPy 1.17.1.

Comandos principales (desde la raíz del repositorio):

```sh
curso/.venv/bin/python curso/S3_comparacion_decision/calc/M11_ejemplos.py
curso/.venv/bin/python curso/S3_comparacion_decision/calc/M12_indicadores.py
```

| Cálculo | Resultado comprobado |
|---|---|
| M11 I-MR | Centro 0,000160000; MR medio 0,000425000; LIC −0,000970500; LSC 0,001290500; LSC-MR 0,001388475; señales I=[6], MR=[7]. |
| M11 fases | Medias 0,000160000 / 0,001160000; mezcla 0,000660000. |
| M11 OLS | a=0,0892857143; b=0,00302380952; u(b)=0,0000922138892; IC95 b=[0,00278676618;0,00326085287]; p=4,95673469e−7; residual=0,0146385011. |
| M11 predicción día120 | 0,452142857; IC media=[0,436241506;0,468044208]; IP individual=[0,411291546;0,492994168] nmol/mol. |
| M11 incremento/presupuesto | Incremento120=0,362857143; u=0,011065667; combinado con inicial 0,020=0,022857143 nmol/mol. Cambio180=0,544285714. |
| M11 recurrencias | EWMA: Z1=0,2, Z2=0,36; límites 0,54/0,691537. CUSUM superior 0,5/1,0. Primeras señales de serie constante +1: 11/11. |
| M11 falsa alarma | Semilla11026, 100000 series, 50 ocasiones: EWMA=0,199090; CUSUM=0,091770. |
| M11 cambio +1 desde26 | Detección condicional=0,987946/0,983156; detección total=0,882700/0,944410; demora entre detectadas=8,324/9,306. |
| M11 revisión | Riesgo60=0,000394556495; riesgo30 subdesborda a 0 en salida numérica; riesgo90 redondea a 1. Son aproximaciones de máquina, no probabilidades matemáticamente idénticas a cero/uno. |
| M12 diferencias | d=[−2;1;−1;2]%; media=0; media absoluta=1,5%; s=1,825741858; SE=0,912870929. Cero cercano: 0,3 nmol/mol y 150%. |
| M12 intervalos | chi²(0,10;3)=0,584374; L90=4,136703735%; AS=0,577350269; t(0,95;3)=2,353363435; L95(AB)=2,179357506%; IC95 media=[−2,905163;2,905163]%. |
| M12 escala/cero | 1%→2,01%; s0=0,158113883; 3s0=0,474341649 nmol/mol. |
| M12 periodos/común | Medias1/3%; SE iid=0,645497; SE periodos=1; desplazamiento común0,8 invariable; u media n2=0,905539, n8=0,827647 puntos porcentuales. |
| M12 discrepancia nueva | Intervalo [1,5;2,5] dentro de ±3: acepta=True; L90=4,136704% frente a 4%: satisface=False. |

Contrastes adicionales efectivamente hechos: el script M11 compara OLS con `numpy.linalg.lstsq` y covarianza matricial; compara EWMA constante con 1−0,8^t y CUSUM con 0,5t; verifica señales y riesgo. M12 compara varianza matricial con ucom²+uind²/n y comprueba autovalores positivos. Un cálculo auxiliar independiente reprodujo las ecuaciones originales CFR mediante sumas nΣd²−(Σd)², no mediante `np.std`: L90=4,136703735091946 y L95=2,1793575062919275. Se comprobó cobertura normal de k=2: 0,9544997361. No se realizó una segunda simulación Monte Carlo independiente ni validación con datos instrumentales reales.

`git diff --check` para los capítulos y script editados no detectó errores. Conteo programático de marcadores: M11=3, M12=3.

Salidas finales conservadas en `calc/revision_M11_actual.out` y `calc/revision_M12_actual.out`, generadas mediante ejecuciones completas con `PYTHONDONTWRITEBYTECODE=1`. Son dos productos adicionales de evidencia, dentro de S3. Las primeras ejecuciones no importaron módulos locales del repositorio ni escribieron bytecode mediante compilación explícita; las ejecuciones finales desactivan expresamente su escritura.

Decisiones sobre auxiliares heredados: **conservar sin sobrescribir** `calc/M11_verificacion_sol.out` como registro anterior (no contiene la línea de fases que ya imprime el script vigente); **conservar sin sobrescribir** `calc/M12_evidencias_fuentes.md` y `calc/fuentes_M11/*` como evidencia histórica, con los límites de verificación y localizadores corregidos consignados en este informe. Las nuevas salidas no sustituyen silenciosamente registros anteriores. `calc/verificacion_fuentes_agente/CFR_p18.png` y `CFR_p19.png` se conservaron y se usaron para cotejo visual de ecuaciones. No se eliminaron auxiliares ni se tocó la ficha común. El mapa de decisiones contiene exactamente 10 bloques M11 y 9 M12, 19 en total.

## 9. Pendientes explícitos

1. Preparar en la fase de ejercicios las series homogéneas con eventos, paquetes, plantillas y rúbricas; conservar solo marcadores ahora. No usar cinco puntos ni seis días como validación de largo plazo.
2. Validación operativa futura: datos propios del mismo patrón y método, independencia/dependencia, estabilidad, revisión de parámetros estimados, cobertura y riesgo aprobados. Los riesgos docentes no autorizan intervalo real.
3. Montgomery: edición y lectura directa no verificadas; el libro no está en docs/. Las fórmulas concretas examinadas se sostienen además en Crowder/GUM/NIST local.
4. NIST 1.3.5.8 de M12: la evidencia histórica afirma una consulta previa. En esta revisión se intentó `curl` con tiempo máximo de 30 s, sin obtener un pasaje verificable en la salida. No se declara reconfirmación web. La fórmula regulatoria se cotejó visualmente y la inversión chi-cuadrado se recalculó; queda pendiente reconfirmar la página externa como respaldo estadístico documental puntual.
5. Las páginas PDF históricas equivocadas se documentan en S-12-11, sin reescribir bitácoras ni evidencias de otras sesiones.
6. No se auditó la ficha común ni los verificadores de entrega, por exclusión expresa del encargo. Tampoco se revisó la implementación de AX.2/AX.11/AX.12: aquí se verificaron las remisiones y fórmulas usadas, no el contenido del anexo.
