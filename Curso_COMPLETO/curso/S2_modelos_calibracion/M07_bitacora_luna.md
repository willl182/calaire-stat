# Bitácora de desarrollo — M07

## Plan

### Alcance por nivel (tomado literalmente de `prop_e.md`, §5, M7)

- **B:** «mínimos cuadrados ordinarios (OLS) con intercepto en un caso con condiciones adecuadas; pendiente, intercepto, residuos; límites de R²; intervalo de uso; `x̂ = (y − a)/b` frente a la corrección `x̂ − y`.»
- **I añade:** «incertidumbres y covarianza de `a` y `b`; bandas de confianza y predicción; incertidumbre de la predicción inversa; origen forzado; mínimos cuadrados ponderados (WLS) y elección de pesos. La ficha de decisión indica cuándo la incertidumbre del eje de referencia es relevante: si lo es, I detiene el ajuste con `x` fijo y escala el caso a A. **Falta de ajuste:** la prueba convencional supone réplicas al mismo valor de referencia; si la referencia cambia entre repeticiones (caso: F-PSMT-01, donde cambia entre días) no se aplica tal cual; hacen falta réplicas reales o un modelo que trate la variación de la referencia.»
- **A añade:** «regresión con incertidumbre en ambos ejes y **GGMR** (regresión generalizada de Gauss-Markov, ISO/TS 28037: ajuste que estima los parámetros y las abscisas ajustadas mediante una suma cuadrática generalizada basada en la matriz conjunta de covarianza de `x` e `y`; no es WLS ordinario con `x` fijo); diagnóstico por residuos ponderados y chi-cuadrado (valores altos y anormalmente bajos). El curso trabaja en el alcance validado de la herramienta disponible: covarianza cruzada entre ejes nula (`V_xy = 0`).»

### Escenas previstas

1. Ficha del capítulo: competencia, prerrequisitos M3–M6, alcance aditivo B/I/A, origen de datos, anexos AX.5 y AX.6 y referencias clave.
2. B1: orientación de ejes, datos de calibración como pares referencia–indicación, covariación de Pearson y por qué no valida la recta; límites de interpretación de R².
3. B2: criterio OLS con intercepto; ecuaciones normales, pendiente e intercepto, residuo y error residual; ejemplo numérico simulado reproducible de recta adecuada.
4. B3: dominio/intervalo de uso, interpolación frente a extrapolación; inversión `x̂=(y−a)/b`, corrección aditiva `x̂−y` y signo; marcador práctica B y señales de escalamiento.
5. I1: supuestos, covarianza e incertidumbre de parámetros OLS, bandas de confianza/predicción; origen forzado y su condición; ejemplo numérico.
6. I2: WLS, elección de pesos a partir de incertidumbres de respuesta, comparación OLS/WLS y consecuencias de pesos mal justificados; ejemplo numérico reproducible.
7. I3: prueba de pendiente y falta de ajuste, error puro/residuo relativo por nivel; ejemplo que distingue réplicas reales de lecturas agrupadas y advertencia específica F-PSMT-01 con referencia variable entre días; validación WLS global ilustrativa y criterio individual ISO 6143 §5.2.2; calibración inversa y propagación lineal AX.6 con ejemplo. Marcador práctica I; ficha de escalamiento I a A cuando `u(x)` sea relevante.
8. A1: modelo de errores en ambos ejes, matriz conjunta de covarianza, diferencia entre OLS/WLS y GGMR; ajuste de parámetros y abscisas ajustadas, alcance validado `V_xy=0`.
9. A2: residuos ponderados y chi-cuadrado, interpretación de resultados altos y anormalmente bajos, límites del diagnóstico e implementación validada; marcador práctica A y cierre/transición a M8.

### Datos y rótulo de origen

- Ejemplos pequeños para OLS, inversión, WLS, bandas, pruebas y GGMR: **simulados**, con valores y regla generadora declarados; resultados no atribuibles a CALAIRE.
- El diseño y los conteos del Level 2 contra SRP 55 (F-PSMT-01, 12 puntos × 8 lecturas × 6 días) se identificarán como datos/documento **propios** conforme a `guia_libreto.md` §6. Se utilizará solo para contextualizar la limitación de falta de ajuste: la referencia cambia entre días; no se atribuirá a este hecho ninguna cifra calculada no obtenida del archivo.
- El ejemplo de QAPP SRP36 contra SRP7 solo se incluiría si se puede verificar de fuente y se requiere para ilustrar: **publicado**. No es necesario para cubrir el alcance M7 y no se planifica su uso como resultado del laboratorio.

### Cálculos previstos

- Un script `calc/M07_*.py` con conjuntos simulados fijados en código: Pearson, OLS, residuos, `s_e`, parámetros y covarianza, intervalos/bandas, predicción inversa/corrección, ajuste al origen, WLS, prueba de pendiente, falta de ajuste bajo réplicas válidas, residuo relativo por nivel, validación WLS con chi-cuadrado global y máximo residuo estandarizado por punto, y ejemplo numérico de GGMR con `V_xy=0` y diagnóstico ponderado/chi-cuadrado.
- Todos los resultados numéricos derivados de esos ejemplos se imprimirán desde el script; las constantes de datos simulados se explicarán allí. No se presentarán cifras de resultados CALAIRE en el libreto salvo conteos/diseño documental con cita explícita.

### Referencias a verificar en `docs/` con `pdftotext`

- `Intro. Statistics in Metrology`, capítulo 10: numerales sobre mínimos cuadrados, incertidumbre de parámetros, bandas, diagnósticos, ponderación y regresión con incertidumbre en ambos ejes.
- `ISO 28037.pdf`: alcance y apartados sobre OLS/WLS, GDR/GGMR y validación/diagnóstico.
- `ISO 6143 2001.pdf`: criterio de residuos ponderados, solo si se usa numeral.
- `statistical_concepts_c10.pdf`: correlación de Pearson e inferencia, solo si se usa numeral.
- `GUM` JCGM 100, Anexo H.3; `Otto` §§6.1–6.2; `SRP QAPP` Elemento 14.2: verificar solo los numerales que se decida citar y que estén disponibles en `docs/`.
- Si una ubicación no se confirma literalmente en el PDF, la cita quedará sin numeral y se anotará como pendiente. Referencias internas `prop_e`, guía y AX no requieren verificación bibliográfica externa.

### Anexos previstos

- **AX.5:** remitir para deducción de ecuaciones normales OLS/WLS y covarianza de `a` y `b`; usar las expresiones sin derivarlas en clase.
- **AX.6:** remitir para deducción de la incertidumbre de la predicción inversa por linealización; explicar y usar el resultado sin derivación.

## Ejecución

### Libreto y prácticas

Se escribió `M07_libreto.md` con ficha; escenas B1–B3, práctica B y señales de escalamiento; escenas I1–I4, práctica I y escalamiento explícito a A cuando la incertidumbre de `x` sea relevante; escenas A1–A2, práctica A y advertencia de alcance `V_xy = 0`; cierre y referencias. Se cubrieron los alcances B, I y A de `prop_e.md` §5, M7. Se narraron los errores críticos de correlación/R², inversión de corrección, origen forzado, pesos, falta de ajuste sin réplica real, validación global WLS y lectura de chi-cuadrado. Se añadieron el diagnóstico global WLS y la comprobación punto a punto de ISO 6143 §5.2.2, distinguiéndolos expresamente. Se dejaron exactamente tres marcadores de práctica en los niveles, sin enunciados, datos, solución, evidencias ni rúbricas.

Todos los ejemplos calculados se identifican como **simulados** y no se atribuyen a CALAIRE. El F-PSMT-01 se menciona como fuente **propia** solo para el límite de la prueba de falta de ajuste cuando la referencia varía entre días; no se publican resultados numéricos propios.

### Scripts y resultados reproducidos

Se creó y ejecutó con `curso/.venv/bin/python` el script `calc/M07_ejemplos.py`. Sus datos y estructuras son fijos y están descritos en el propio archivo. Resultados principales:

- OLS: Pearson `r = 0,99999823`; prueba `ρ = 0`: `t = 1061,63388878`, 4 g.l., `p = 4,7233441×10⁻¹²`; `R² = 0,99999645`; `a = 0,24285714`; `b = 1,0014285714`; residuos `−0,04285714; 0,31428571; −0,42857143; 0,32857143; −0,41428571; 0,24285714`; `s_res = 0,39460649` nmol/mol. Parámetros: `u(a) = 0,28559521`, `u(b) = 0,0009432899`, `cov(a,b) = −0,0002224490`.
- Prueba de pendiente `b = 1`: `t = 1,51445633`, 4 g.l., `p = 0,20447788`. Uso inverso para `y = 250,50`: `x̂ = 249,90014265`; corrección `x̂ − y = −0,59985735` nmol/mol. La propagación inversa didáctica, con `u(y)=0,20` nmol/mol, término residual e independencia declarada, dio `u(x̂)=0,47014327` nmol/mol; `t(0,975;4)=2,77644511`; `U=1,30532699` nmol/mol.
- En `x₀=250`, `ŷ=250,60000000`; semiamplitud IC95 de la media `0,44727816`; semiamplitud de predicción individual `1,18338678` nmol/mol. Recta forzada al origen: pendiente `1,0020909091`.
- WLS simulado: incertidumbres `0,25; 0,30; 0,40; 0,60; 0,90; 1,20`; pesos `16; 11,111111; 6,25; 2,777778; 1,234568; 0,694444`. OLS (`a=0,44761905`, `b=1,0007428571`) frente a WLS (`a=0,41685160`, `b=1,0009213402`). Validación WLS simulada con 12 puntos: `χ²_obs=1,27964725`, `ν=10`, `χ²₀,₉₅=18,30703805`; `max|residuo ponderado|=0,61604636`. Se registra el contraste global como diagnóstico ilustrativo, no como sustituto de la comprobación individual ISO 6143 §5.2.2; con `x` fijo, el criterio individual se reduce al residuo vertical estandarizado y el máximo es menor que 2.
- Falta de ajuste simulada con cuatro niveles y tres réplicas independientes por nivel: `SS_LOF=0,966`; `SS_PE=0,080`; `F(2,8)=48,3`; `p=0,00003422`. Se imprimen además residuos relativos por nivel; se advierte que el porcentaje en cero no sustituye el residuo absoluto.
- GGMR simulado con componente común en `V_x`, `V_y` diagonal y `V_xy=0`: `a=0,30472537`, `b=1,0013144319`; abscisas ajustadas `−0,00132811; 99,98983445; 200,0372091; 299,94405355; 400,04764027; 499,98259075`; `χ²=0,40890065`, 4 g.l. declarados para el ejemplo. Con datos generados prácticamente exactos sobre una recta, el mismo modelo dio `χ²=3,47860069642×10⁻²⁹`; al introducir una discrepancia simulada de 5 nmol/mol en una respuesta, dio `χ²=83,36173290`. Se usan para ilustrar valores muy bajos y altos, no para validar una herramienta de producción ni fijar un umbral universal.

### Referencias verificadas con `pdftotext`

| Clave | Numeral comprobado | Archivo de `docs/` | Página(s) PDF comprobadas |
|---|---|---|---|
| Intro | §§10.1–10.1.2 (asociación/alcance y extrapolación) | `intro_stats_metro_c10.pdf` | 2–3 |
| Intro | §10.2.1 (OLS lineal) | `intro_stats_metro_c10.pdf` | 5 |
| Intro | §10.2.3 (WLS) y §10.2.4 (incertidumbre en ambos ejes) | `intro_stats_metro_c10.pdf` | 6 |
| Intro | §§10.3.1–10.3.3 (parámetros, bandas de confianza y predicción) | `intro_stats_metro_c10.pdf` | 8 |
| Intro | §§10.4.1–10.4.3 (residuos, prueba de pendiente y diagnóstico cuantitativo) | `intro_stats_metro_c10.pdf` | 9–10 |
| ISO 28037 | §5.2.2 (incertidumbres), §5.7 (uso inverso), §5.8 (OLS) | `ISO 28037.pdf` | 14, 16–17 |
| ISO 28037 | §§6.1–6.3 (WLS y validación) | `ISO 28037.pdf` | 17–21 |
| ISO 28037 | §§7–9 (regresión con incertidumbre en ambos ejes y generalizaciones) | `ISO 28037.pdf` | 25–39 |
| ISO 28037 | §§10.1–10.3 (GGMR y validación) | `ISO 28037.pdf` | 39–44 |
| ISO 28037 | §11.1 (predicción) | `ISO 28037.pdf` | 45–46 |
| ISO 6143 | §5.2.2 (validación del modelo de respuesta; comprobación de bondad de ajuste por punto y criterio máximo 2) | `ISO 6143 2001.pdf` | 15; discusión de aplicación en 24 |
| Statistical Concepts | §10.1 (medidas de asociación de Pearson e inferencia) | `statistical_concepts_c10.pdf` | 2–7 |

La verificación fue una extracción con `pdftotext` y búsqueda del numeral/texto en las páginas indicadas; los capítulos de Intro también se comprobaron con sus encabezados y texto de cada página. No se citan numerales de referencias no confirmadas.

### Decisiones y pendientes

- No se usó el ejemplo publicado del QAPP SRP36/SRP7: no era necesario para el alcance M7 y se evitó importar cifras ajenas al ejemplo preparado.
- Se citaron Otto y Brereton sin numeral, con cita bibliográfica completa, para la descomposición de falta de ajuste. **Pendiente**: verificar con `pdftotext` los numerales específicos de esos libros si una revisión posterior decide incorporarlos.
- ISO 6143 se incorporó para el criterio de validación punto a punto, con §5.2.2 verificado en `pdftotext`; GUM H.3 y SRP QAPP se consideraron en el plan, pero no se usaron en el libreto ni se les atribuye contenido.
- La inversión y su incertidumbre se presentan en ejemplos simulados; las contribuciones de cobertura son ilustrativas y se remite a AX.6. La incertidumbre inversa numérica declara la independencia asumida y no se ofrece como presupuesto completo.
- En GGMR se explica y ejemplifica el alcance `V_xy=0`; no se enseña GGMR con covarianza cruzada no nula ni se afirma validación operativa de la implementación numérica del ejemplo.
- Prácticas B, I y A: desarrolladas en la fase de ejercicios. Su bitácora autorizada es `curso/logs/M07_practicas_luna.md` (plan, ejecución, correcciones y ronda de cierre); esta bitácora no las recoge.
- Pendientes: revisiones de sección y material evaluativo (rúbricas, evidencias, taller), fuera de esta sección. La revisión Haiku se atendió en la sección de correcciones.

## Correcciones (revisión Haiku)

| Id del hallazgo | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado con cambios | Se precisó que el capítulo 10 de Hahs-Vaughn trata asociación bivariada; se mantuvo §10.2.1, pp. 3–5 PDF, para la prueba y se dejó explícito que la fórmula de `t` no aparece ahí y requiere fuente específica. | Libreto, ficha y escena I1 | La fuente respalda la interpretación de la prueba, no la fórmula expresada ni regresión en general. |
| R02 | aplicado | Se conservó la cita a §10.4.2, PDF p. 9, y la separación explícita entre prueba de pendiente nula y contraste didáctico `b = 1`. | Libreto, escena I4 | El texto vigente ya corregía página y alcance; la fuente no se usa como respaldo del contraste frente a uno. |
| R03 | aplicado | Se especificaron 48 lecturas por punto y el desglose de ocho lecturas por día durante seis días. | Libreto, escena I4 | `12 × 8 × 6 = 576`; son 48 lecturas por punto, no ocho en total. |
| R04 | aplicado | Se conservaron las señales de pocos grados de libertad, dependencia no contemplada y proximidad a límite de aceptación. | Libreto, señales de escalamiento B | Son señales expresas de prop_e §2; la redacción vigente las cubre. |
| R05 | aplicado | Se expresa `cov(a,b)` en nmol/mol y se explica que `a` tiene esas unidades y `b` es adimensional. | Libreto, escena I1 | Las unidades de covarianza son el producto de las unidades de las variables; en este caso coincide con nmol/mol. |
| R06 | aplicado | Se mantiene la explicación de que escalar todos los pesos por una constante no altera la estimación puntual, pero sí la escala de incertidumbres y chi-cuadrado. | Libreto, escena I3 | Propiedad de WLS: la solución de los parámetros es invariante ante un factor común de los pesos; las magnitudes de escala no lo son. |
| R07 | aplicado | Se conserva la condición explícita para `ν = n − 2`: dos parámetros y observaciones independientes; se advierte revisar los grados de libertad si cambia el modelo o hay dependencia. | Libreto, escena I3 | `n − p` no es una regla automática fuera de los supuestos declarados. |
| R08 | aplicado | Se mantiene el criterio completo por punto para ambos ejes, y se aclara que la discrepancia de `x` es cero cuando se fija `x`. | Libreto, escena I3 | ISO 6143 §5.2.2 requiere comprobar ambas coordenadas; la simplificación solo aplica a este WLS con `x` fijo. |
| R09 | aplicado con cambios | Se añadió una tabla de pares `x,y` para B1. Los datos de incertidumbre de los 12 niveles en I3 y las magnitudes de incertidumbre de A1 ya estaban enunciados y se conservaron. | Libreto, escenas B1, I3 y A1 | La tabla permite presentar B1 sin abrir el script; los otros ejemplos ya incluyen sus datos necesarios para reproducirlos. |
| R10 | aplicado | Se conserva la aclaración de que la nueva indicación se supone independiente de los parámetros, mientras el término de covarianza de `a,b` sí se incluye. | Libreto, pizarra de I1 | La independencia no debe atribuirse al término de covarianza incorporado en la expresión. |
| R11 | aplicado | Se usa `s_res` para la desviación estándar residual y se define en su primera aparición; también se registra en la ficha. | Libreto, ficha y escenas B2/I1 | Evita confusión con `e = y − x` y mantiene notación distinta de la repetibilidad `s_r`. |
| R12 | aplicado | Se conservan en plural las advertencias críticas dirigidas al grupo. | Libreto, escenas I2–A2 | Es coherente con la narración a «ustedes» y el tratamiento plural de la guía. |
| R13 | aplicado | Se mantuvo la clave Hahs-Vaughn indicada por la guía y se ordenó la referencia bibliográfica como Lomax; Hahs-Vaughn. | Libreto, ficha y referencias | El capítulo 10 se limita a asociación; el orden de autores se ajusta a la comprobación consignada en la revisión. |
| R14 | aplicado | Se especifica en la ficha que las citas PDF usan paginación del archivo («PDF p.»). | Libreto, ficha | Distingue de forma uniforme la paginación del archivo de la impresa. |
| R15 | rechazado | No se quitó encabezado: la versión vigente no contiene `### Práctica B`; el marcador aparece directamente después de la escena B3. | Libreto, transición B3 | El hallazgo no aplica al archivo actual; ya respeta la estructura de la guía §2. |
| R16 | aplicado | Se conservó el título completo «Ajustar la recta de un conjunto del Level 2…». | Libreto, marcador de práctica B | El marcador coincide con el título fijado por prop_e §5 M7-B. |
| R17 | aplicado con cambios | Se dividió el párrafo de WLS para separar componentes compartidas, adecuación de incertidumbres, invariancia de pesos y limitación de la matriz diagonal. | Libreto, escena I3 | Mejora el ritmo oral sin cambiar el contenido técnico. |
| R18 | aplicado | Se conserva la advertencia crítica que diferencia `U = k·u` de `u(x̂)`. | Libreto, escena I1 | La semiamplitud expandida no debe confundirse con la incertidumbre estándar. |

Correcciones adicionales por iniciativa propia:

- Añadí a la ficha la definición de `s_res` para que la notación quede disponible antes de la primera fórmula y no dependa de localizar la escena B2.
- En el primer ejemplo de B1, organicé los seis pares simulados en una tabla de datos utilizable directamente en clase.
