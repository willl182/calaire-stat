# M07. Regresión y calibración inversa

## Ficha del capítulo

| Elemento | Contenido |
|---|---|
| Competencia estadística | Ajustar un modelo de calibración, diagnosticarlo y usarlo en sentido inverso con su incertidumbre. |
| Prerrequisitos | M3-B: varianza y distribuciones; para I, covarianza y correlación de M3-I; M4: inferencia y pruebas; M5: estructura de los datos; M6: componentes y residuos. Los niveles son acumulativos: I comprende B y A comprende B e I. |
| Nivel B | OLS con intercepto en condiciones adecuadas; pendiente, intercepto y residuos; límites de R²; intervalo de uso; inversión $\hat x = (y - a)/b$ y corrección $\hat x - y$. Se usa `s_res` para la desviación estándar residual del modelo. |
| Nivel I añade | Incertidumbre y covarianza de parámetros; bandas de confianza y predicción; incertidumbre de la predicción inversa; origen forzado; WLS y elección de pesos; falta de ajuste con réplicas verdaderas; límites del modelo con `x` fijo y escalamiento si la incertidumbre en referencia es relevante. |
| Nivel A añade | Regresión con incertidumbre en ambos ejes; GGMR con matriz conjunta de covarianza y abscisas ajustadas; diagnóstico por residuos ponderados y chi-cuadrado, dentro del alcance validado $V_{xy} = 0$. |
| Datos de ejemplo | Ejemplos estadísticos de regresión, inversión, ponderación, falta de ajuste y GGMR: **simulados**, fijados en `calc/M07_ejemplos.py`; no describen CALAIRE. Contraste de GGMR: **publicado**, ISO/TS 28037 §10.3, tablas 25–26, con datos y covarianzas sin modificar. Contexto del certificado F-PSMT-01: fuente **propia**, `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`; se usa únicamente para explicar por qué la referencia variable entre días impide la prueba convencional de falta de ajuste sin un modelo apropiado. |
| Anexos | AX.5: ecuaciones normales OLS/WLS y covarianza de `a` y `b`. AX.6: incertidumbre de la predicción inversa por linealización. AX.7: Welch–Satterthwaite y sus condiciones. AX.8: formulación matricial de GGMR con $V_{xy} = 0$ y chi-cuadrado de consistencia. |
| Referencias clave | Crowder 2020, cap. 10; ISO/TS 28037:2010; ISO 6143:2001; GUM G.4; Hahs-Vaughn, cap. 10 (solo asociación bivariada); Otto §6.1. Las citas de archivos PDF usan la paginación del archivo («PDF p.»); los numerales se verificaron con `pdftotext`, según referencias y bitácora. |

## Nivel B — ajustar y usar la recta en condiciones adecuadas

En el nivel básico damos por vistos los datos emparejados, el error con signo y la distinción entre una lectura y un promedio. Ahora vamos a ajustar una relación entre el valor de referencia, que llamaremos `x`, y la indicación, que llamaremos `y`. En todo el capítulo mantenemos esta orientación: `x` es referencia, `y` es indicación y el error es $e = y - x$. La recta de calibración se escribe $y = a + b\,x$. No inviertan los ejes al copiar la fórmula: la inversión se hará después, cuando tengamos una indicación y queramos obtener un valor de referencia estimado [prop_e §3; Crowder 2020 §10.1, PDF pp. 2–3].

### Escena B1. Una correlación alta no certifica una calibración

> **[DIAPOSITIVA]** Un diagrama de dispersión con `x` en el eje horizontal y `y` en el vertical. Añadir una recta ajustada, una nube pequeña de residuos bajo la línea y, a un lado, una segunda nube con asociación alta pero curvatura visible.
>
> **[MATERIAL]** Pares simulados (nmol/mol).

| Variable | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| `x` | 0 | 100 | 200 | 300 | 400 | 500 |
| `y` | 0,2 | 100,7 | 200,1 | 301,0 | 400,4 | 501,2 |

Vamos a empezar con una pregunta que suele aparecer al mirar una tabla: si referencia e indicación crecen casi perfectamente juntas, ¿ya sabemos que la calibración es buena? No. Esa asociación visual no nos dice por sí sola si la pendiente es uno, si el intercepto es cero, si los residuos son pequeños en unidades útiles, si el modelo es lineal en todo el intervalo ni si podemos usarlo fuera de los valores medidos [Hahs-Vaughn §10.1, PDF pp. 1–2; Crowder 2020 §10.1, PDF pp. 2–3].

En fotometría, `x` e `y` suelen crecer juntos porque ambos describen la misma concentración a distintos lados de una comparación. Esa asociación puede ser muy alta aunque haya un desplazamiento constante o una desviación de escala que importe. Si todas las indicaciones fueran sistemáticamente mayores que la referencia por una cantidad fija, la correlación podría seguir siendo casi perfecta. Si la pendiente fuese distinta de uno, el patrón todavía podría ser lineal. La correlación contesta si las dos variables varían linealmente juntas; la calibración exige evaluar una función con parámetros y residuos frente a un criterio de uso.

> **[PIZARRA]** $y=a+b x$; $e=y-x$.
>
> **[NOTA AL INSTRUCTOR]** Leer «y es igual al intercepto más la pendiente por x» y «el error con signo es indicación menos referencia». En B la asociación se motiva visualmente; no se calcula Pearson ni se exige covarianza de M3-I.

Para que vean la diferencia, usaré datos enteramente simulados, no resultados del Level 2. Fijé seis referencias, desde cero hasta quinientos nmol/mol, y seis indicaciones con pequeñas desviaciones en torno a una recta. El script `calc/M07_ejemplos.py` calcula cada cantidad que voy a decir. El coeficiente de determinación, que aquí llamaremos R², resulta casi uno (más de 0,99999), extraordinariamente próximo a uno. Sin embargo, la pendiente ajustada es `1,00143`, el intercepto es `0,243 nmol/mol` y el mayor residuo en valor absoluto es aproximadamente `0,429 nmol/mol`. Son números del ejemplo simulado; no son límites de aceptación ni mediciones de CALAIRE [script `calc/M07_ejemplos.py`].

¿Qué aprendemos? Primero, R² es un resumen relativo a la variabilidad vertical de los datos: en una regresión lineal con intercepto, expresa qué fracción de esa variabilidad queda asociada al ajuste lineal en el conjunto considerado [Otto §6.1, ec. (6.17)]. No informa si la escala del eje es correcta ni si el error residual es aceptable para el uso. Segundo, cuando se restringe el rango de una variable la correlación tiende a bajar [Hahs-Vaughn §10.1.1.5.2, restricción del rango]; por eso un R² calculado en un intervalo estrecho de `x` puede ser menor que en uno amplio, aunque el tamaño de los residuos en nmol/mol no cambie. Tercero, un solo R² no revela patrón temporal, curvatura, heterogeneidad de varianza ni un punto que determine excesivamente la pendiente. Por eso R² acompaña al diagnóstico de residuos; no lo sustituye [Crowder 2020 §10.4.1].

> **[ERROR CRÍTICO]** Una correlación o un R² cercanos a uno no constituyen por sí solos evidencia de que la calibración sea válida. No se declara aceptación sin revisar la recta, los residuos, el intervalo de uso y los criterios aplicables.

### Escena B2. Ajustar una recta por mínimos cuadrados ordinarios

> **[DIAPOSITIVA]** Proyectar una tabla con columnas `x`, `y`, `ŷ` y $r = y - \hat y$. Resaltar que el residuo de regresión `r` no es el error de medición $e = y - x$.

Cuando las incertidumbres de los valores de referencia son despreciables para el ajuste, las observaciones de `y` son independientes y tienen una varianza aproximadamente constante, podemos considerar mínimos cuadrados ordinarios, OLS, con intercepto. La regla es elegir `a` y `b` de modo que la suma de cuadrados de los residuos verticales sea mínima. Para cada pareja, el valor ajustado es $\hat y_i = a + b x_i$, y el residuo es $r_i = y_i - \hat y_i$. Digo «residuo vertical» porque el criterio OLS mide distancias en la dirección de `y`: trata `x` como conocido sin error relevante [Crowder 2020 §10.2.1, PDF p. 5; ISO 28037 §5.8].

No confundamos los dos errores. El error de indicación de una observación es $e = y - x$, comparada con la referencia. El residuo de regresión es $r = y - (a + bx)$, comparado con el valor que predice la recta. Si la recta tiene sesgo proporcional o un intercepto, el residuo puede ser pequeño y el error frente a la identidad $y=x$ no ser cero. La recta resume la tendencia de calibración; el residuo mide la desviación respecto de esa tendencia.

En la pizarra escribo las fórmulas de la solución OLS con intercepto. La pendiente es la covariación de `x` e `y` dividida por la variación de `x`, $b=S_{xy}/S_{xx}$; el intercepto es la media de `y` menos la pendiente por la media de `x`, $a=\bar y-b\bar x$. Aquí $S_{xy}=\sum_i(x_i-\bar x)(y_i-\bar y)$ y $S_{xx}=\sum_i(x_i-\bar x)^2$: son sumas de productos y cuadrados centrados, no un prerrequisito de covarianza. No vamos a presentar matrices ni deducir las ecuaciones normales en B: la formulación matricial y su deducción pertenecen al Anexo AX.5, para I [Crowder 2020 §10.2.1, PDF p. 5; AX.5].

> **[PIZARRA]** $\hat y_i = a+b x_i$; $r_i=y_i-\hat y_i$; $b=\dfrac{S_{xy}}{S_{xx}}$; $a=\bar y-b\bar x$.

> **[NOTA AL INSTRUCTOR]** Leer cada expresión en voz alta y aclarar que `S_xy` y `S_xx` son sumas centradas de productos y cuadrados. No escribir la derivación de las ecuaciones normales.

Miremos con calma el ejemplo simulado de la escena anterior. El ajuste da $a = 0{,}243 \ \mathrm{nmol/mol}$ y $b = 1{,}00143$. La lectura verbal es: dentro de estos datos simulados, la indicación ajustada aumenta alrededor de `1,00143 nmol/mol` por cada `1 nmol/mol` de referencia, y el intercepto estimado es alrededor de `0,243 nmol/mol`. El intercepto no se convierte automáticamente en una corrección del cero; es un parámetro estimado en el intervalo y las condiciones del ajuste. El código reproduce también los seis residuos: $-0{,}04286; 0{,}31429; -0{,}42857; 0{,}32857; -0{,}41429; 0{,}24286 \ \mathrm{nmol/mol}$ [script `calc/M07_ejemplos.py`].

La desviación estándar residual, que llamaremos `s_res` para no confundirla con el error de medición $e = y - x$, resume el tamaño residual global del ejemplo y vale `0,3946 nmol/mol`. Se calcula como la raíz cuadrada de la suma de cuadrados de los residuos dividida por sus grados de libertad residuales en el modelo lineal simple. En este nivel nos basta con interpretarlo como una escala de dispersión alrededor de la recta, bajo el modelo y sus supuestos. No lo llamamos automáticamente incertidumbre completa de una predicción inversa: para ese uso hay que considerar también los parámetros, la nueva observación y el modelo, que se tratará en I y en M8 [Crowder 2020 §10.2.1, PDF p. 5; Crowder 2020 §10.3, PDF pp. 7–8].

> **[PREGUNTA AL GRUPO]** En la columna de residuos, ¿qué resta se ha hecho: indicación menos referencia, o indicación menos valor calculado por la recta? — *Respuesta esperada:* indicación menos predicción de la recta; el error de medición se calcula como $y - x$.

La recta OLS no es adecuada por definición para cualquier conjunto. La independencia de las observaciones, la forma lineal en el intervalo estudiado, la variabilidad apropiadamente modelada y la incertidumbre de `x` son parte de la decisión. En B la usamos cuando la ficha del caso ya confirma condiciones adecuadas: incertidumbre de referencia pequeña frente a la de indicación para el propósito, dispersión de `y` aproximadamente constante, ausencia de dependencia no modelada y puntos dentro del ámbito previsto. Si esas condiciones no están establecidas, el cálculo puede ser aritméticamente correcto y metodológicamente inadecuado [Crowder 2020 §10.1, PDF pp. 2–3; ISO 28037 §5.2.2].

### Escena B3. Intervalo de uso, predicción inversa y signo de la corrección

> **[PIZARRA]** Escribir la orientación completa: `x` = referencia, `y` = indicación, $y = a + b\,x$; debajo, $\hat x = (y - a)/b$ y $\text{corrección aditiva}=\hat x-y$.

Una recta de calibración tiene un ámbito de aplicación. El intervalo de uso está determinado por los valores cubiertos por el diseño, la validez del modelo y el uso que se declara. No extrapolamos por el solo hecho de que la fórmula acepte cualquier número. Si el ajuste se construyó entre cero y quinientos nmol/mol, aplicar la misma recta por encima de quinientos supone que la relación conserva la misma forma fuera de los datos. Ese supuesto necesita respaldo independiente y autorización; no lo genera la ecuación [Crowder 2020 §10.1.2, PDF p. 3].

En una calibración directa calculamos `y` a partir de una referencia `x`. En el uso inverso tenemos una indicación nueva y estimamos qué referencia es coherente con ella. Partimos de $y = a + b x$ y despejamos: $\hat x = (y - a)/b$. Lo leo así: «la referencia estimada es la indicación menos el intercepto, dividido por la pendiente» [ISO 28037 §§5.7, 11.1]. La corrección aditiva para ajustar una indicación se define aquí como $\hat x - y$. No es $y - \hat x$. El signo es parte del resultado, no una convención decorativa [prop_e §3, convención del curso; VIM, definición de corrección (no disponible en docs/)].

Apliquemos la fórmula a un valor simulado de $y = 250{,}50 \ \mathrm{nmol/mol}$ y a la recta estimada en el ejemplo anterior. El cálculo reproducible da $\hat x = 249{,}900 \ \mathrm{nmol/mol}$; por tanto, $\hat x - y = -0{,}600 \ \mathrm{nmol/mol}$. Si alguien cambiara el orden y reportara $y - \hat x$, el número sería positivo y describiría la corrección opuesta. Mantengan en el reporte la definición, la unidad, el dato al que se aplica y el signo [script `calc/M07_ejemplos.py`].

La inversión algebraica de una recta ajustada de `y` sobre `x` ofrece una estimación puntual, pero no es una regresión nueva de `x` sobre `y`. Tampoco convierte automáticamente el residuo OLS en incertidumbre del valor estimado. La incertidumbre de la predicción inversa depende de la dispersión del modelo, de la incertidumbre de `a` y `b`, de su covarianza y de cómo se obtiene la indicación nueva. En el nivel básico no completamos ese presupuesto; en el intermedio añadiremos la linealización y su incertidumbre [ISO 28037 §11.1; AX.6].

> **[ERROR CRÍTICO]** No inviertan el signo de la corrección. Con la convención del curso, la corrección aditiva es $\hat x - y$, no $y - \hat x$. Tampoco llamen incertidumbre completa a la dispersión residual sin especificar el resultado de interés.

> **[PREGUNTA AL GRUPO]** Si la recta se ajustó entre cero y quinientos, ¿qué evidencia permite aplicar su inversión a una indicación por encima de ese intervalo? — *Respuesta esperada:* ninguna por el mero hecho de tener una fórmula; hace falta justificar el modelo y validar ese uso fuera del intervalo observado.

### Práctica B — Ajustar la recta, revisar residuos y comprobar la corrección

> **[PRÁCTICA]** Ustedes reciben seis parejas de referencia e indicación de una serie docente de puntos de calibración de un fotómetro de ozono. La indicación inversa de $250{,}50$ nmol/mol representa una respuesta dentro del intervalo de trabajo; el resultado estadístico alimenta una decisión de uso, no una aceptación del instrumento. Los números son **simulados**, no proceden del Level 2 ni describen a CALAIRE. Los valores están fijados en el enunciado y en `calc/M07_practicas_luna.py`; no proceden de un generador aleatorio. Fijé $x=0;100;200;300;400;500$ nmol/mol y $y=0{,}2;100{,}7;200{,}1;301{,}0;400{,}4;501{,}2$ nmol/mol. El interés es estimar la recta para describir estos datos y aplicar su inversa a una indicación. En esta práctica el enunciado declara que OLS con intercepto es el método apropiado y que las observaciones son independientes, la referencia puede tratarse como fija para el ajuste, la varianza es aproximadamente constante y no hay dependencia no modelada.
>
> | Pareja | $x$ referencia (nmol/mol) | $y$ indicación (nmol/mol) |
> |---:|---:|---:|
> | 1 | 0 | 0,2 |
> | 2 | 100 | 100,7 |
> | 3 | 200 | 200,1 |
> | 4 | 300 | 301,0 |
> | 5 | 400 | 400,4 |
> | 6 | 500 | 501,2 |
>
> Trabajen con la orientación $y=a+bx$. Calculen intercepto, pendiente, predicciones y residuos $r=y-\hat y$; tracen un gráfico de residuos frente a $x$, con línea de cero, unidades y marcas distinguibles, y describan el patrón sin borrar puntos. Comparen su trazado con la salida reproducible accesible `curso/logs/M07_B_residuos.html`. Interpreten R² sin usarlo como criterio de aceptación. Para $y=250{,}50$ nmol/mol, calculen $\hat x=(y-a)/b$ y la corrección $\hat x-y$, conservando su signo. Registren unidades e indiquen si ese uso queda dentro del intervalo observado.
>
> **Solución docente.** El script `calc/M07_practicas_luna.py` resuelve las ecuaciones OLS y comprueba los resultados; reproduce $a=0{,}242857$ nmol/mol y $b=1{,}001428571$. Por ejemplo, en $x=200$, $\hat y=0{,}242857+1{,}001428571(200)=200{,}528571$ nmol/mol, así que $r=200{,}1-200{,}528571=-0{,}428571$ nmol/mol. Los seis residuos, en orden, son $-0{,}042857;0{,}314286;-0{,}428571;0{,}328571;-0{,}414286;0{,}242857$ nmol/mol; suman cero salvo redondeo, y el máximo absoluto es $0{,}428571$ nmol/mol. $s_{res}=0{,}394606$ nmol/mol y $R²=0{,}99999645$. Ese R² resume el ajuste relativo a la variación vertical, pero no prueba escala correcta ni aceptación. La gráfica reproducible y su tabla accesible están en `curso/logs/M07_B_residuos.html`.
>
> Para $y=250{,}50$, $\hat x=(250{,}50-0{,}242857)/1{,}001428571=249{,}900143$ nmol/mol. La corrección es $\hat x-y=-0{,}599857$ nmol/mol: el signo negativo se comprueba directamente al restar. El valor está entre 0 y 500 nmol/mol, dentro del intervalo de referencias usado. Se informa como resultado didáctico, no como corrección autorizada de un fotómetro real.
>
> **Interpretación operativa.** El ajuste describe una relación casi lineal en este conjunto sintético; R² no es un umbral y los residuos alternan de signo sin base aquí para excluir observaciones. La inversa se usa solo dentro del intervalo y con las condiciones declaradas. Si en datos de operación aparecen curvatura, secuencia, varianza desigual, dependencia, referencia incierta o un punto inusual sin causa, se conserva la serie y se escala; no se fuerza el origen ni se elimina un dato para mejorar el ajuste.
>
> **Criterio de logro.** Presenta la recta con unidades y ejes correctos, obtiene los residuos sin confundirlos con $e=y-x$, limita la interpretación de R² y reporta $\hat x$ y la corrección aditiva con signo y unidad correctos.

### Señales de escalamiento

En B ustedes aplican una recta previamente declarada apropiada y registran su uso. Deténganse si no se ha especificado qué variable está en cada eje; si se quiere forzar el origen sin una justificación previa; si hay dependencia entre puntos que el modelo no contempla, cambio de escala, un valor atípico sin causa o residuos con estructura; si hay pocos grados de libertad o el resultado queda próximo a un límite de aceptación; si se pretende extrapolar; si la incertidumbre de referencia es relevante; o si la indicación que se invierte queda fuera del intervalo declarado. No intenten corregir esas señales cambiando el eje, eliminando un dato o seleccionando otra recta después de ver el resultado. Informen qué condición no se cumple y escalen al nivel intermedio o al responsable técnico [prop_e §2, §5 M7-B; Crowder 2020 §10.4, PDF pp. 9–10].

> **[ESCALAMIENTO]** El operador B conserva las parejas originales, la orientación de ejes, la recta autorizada, el intervalo y el resultado con unidades y signo. Si cualquiera de esos elementos no está disponible o el diagnóstico contradice el modelo, no emite una predicción como si fuera válida; consulta a quien prepara y firma el presupuesto o certificado.

## Nivel I — cuantificar la regresión y decidir si el modelo responde

Al comenzar el nivel intermedio damos por vistos el ajuste OLS con intercepto, la lectura de pendiente e intercepto, los residuos, el intervalo de uso y el signo de la corrección. Ahora añadimos la incertidumbre de los parámetros, la diferencia entre una banda para la recta media y otra para una observación futura, la evaluación de la predicción inversa, la posibilidad limitada de fijar el origen, los pesos WLS y la prueba de falta de ajuste. La decisión central sigue siendo estadística: qué magnitud modelamos, con qué estructura de incertidumbre y bajo qué supuestos [prop_e §5, M7-I].

### Escena I1. Parámetros inciertos, covarianza y bandas

> **[DIAPOSITIVA]** Mostrar una recta con una banda estrecha para la media y una banda de predicción más ancha para observaciones individuales. Dibujar los extremos ensanchándose al alejarse del centro de los valores de referencia.

En OLS no conocemos los verdaderos parámetros de la recta. Los valores `a` y `b` que calculamos son estimaciones; si repitiéramos un experimento comparable, variarían. Bajo el modelo lineal con errores independientes, de media cero y varianza común, los residuos estiman esa varianza, y la matriz de covarianza de los parámetros cuantifica la incertidumbre de `a` y `b`. En I usamos la notación de AX.5: cada fila de $X$ contiene un uno y el valor $x_i$, y $\hat\beta=(a,b)^T$. En forma matricial, la covarianza estimada de los parámetros es $s_{\mathrm{res}}^2(X^TX)^{-1}$. La incertidumbre estándar de `a` es la raíz del elemento correspondiente a la diagonal; la de `b` es la raíz del otro elemento diagonal. El elemento fuera de la diagonal es `cov(a,b)`, generalmente no nulo [Crowder 2020 §10.3.1, PDF pp. 7–8; AX.5].

La asociación lineal ya se describió en B. Aquí no añadimos una prueba de correlación: el objetivo es cuantificar los parámetros de calibración y su uso, no repetir la inferencia de M4. Una asociación fuerte no sustituye la revisión del modelo [Crowder 2020 §§10.3–10.4].

¿Por qué importa la covarianza? Porque los cambios del intercepto y la pendiente no son necesariamente independientes. En el ejemplo de seis pares simulados, el script entrega $u(a) = 0{,}2856 \ \mathrm{nmol/mol}$, $u(b) = 0{,}0009433$ y $\operatorname{cov}(a,b) = -0{,}0002224 \ \mathrm{nmol/mol}$, porque `a` tiene unidades de nmol/mol y `b` es adimensional. La pendiente y el intercepto suelen compensarse: una recta puede pivotar cerca del centro del intervalo, de modo que una pendiente ligeramente mayor se asocie con un intercepto ligeramente menor. Ignorar ese término puede dar una estimación incorrecta de la incertidumbre de la recta en un valor concreto [script `calc/M07_ejemplos.py`; Crowder 2020 §10.3.1, PDF pp. 7–8].

> **[PIZARRA]** $\widehat{\operatorname{Cov}}(\hat\beta)=s_{\mathrm{res}}^2(X^T X)^{-1}$; $u^2(\hat y_0)=u^2(a)+x_0^2u^2(b)+2x_0\,\operatorname{cov}(a,b)$.
>
> **[NOTA AL INSTRUCTOR]** Leer ambas expresiones. Decir que la segunda representa la incertidumbre de la respuesta media estimada en `x₀` bajo el modelo OLS; no es todavía la dispersión de una nueva observación.

Para dar un intervalo bilateral de confianza puntual del 95 % a la media de respuesta en un valor `x₀`, suponemos además errores normales y usamos la incertidumbre estimada de la recta en ese punto y un cuantil t con los grados de libertad residuales del modelo. En el ejemplo, para $x_0 = 250 \ \mathrm{nmol/mol}$, el valor ajustado es `250,600 nmol/mol` y la semiamplitud del intervalo de confianza de la media calculada por el script es `0,4473 nmol/mol`. Ese intervalo describe la incertidumbre de la media de la respuesta que predice la recta, conforme a los supuestos del modelo; no dice dónde caerá necesariamente la siguiente lectura [Crowder 2020 §10.3.2, PDF p. 8].

Para una lectura futura individual añadimos la variación aleatoria de una nueva observación alrededor de la media. La banda o intervalo de predicción es por ello más ancho. En el mismo punto, la semiamplitud del intervalo de predicción del 95 % es `1,183 nmol/mol`, frente a `0,4473` para la media. Las dos cifras son simuladas y específicas de este diseño. Son intervalos puntuales: no prometen cobertura simultánea del 95 % para todos los puntos de la banda. El cálculo no convierte por sí solo el resultado en el presupuesto de calibración completo; distingue el objetivo de una media ajustada del de una nueva respuesta [Crowder 2020 §10.3.3, PDF p. 8; script `calc/M07_ejemplos.py`].

> **[PREGUNTA AL GRUPO]** ¿Cuál de las dos bandas debe ser más ancha: la de confianza de la media o la de predicción de una nueva observación? — *Respuesta esperada:* la de predicción, porque incluye tanto la incertidumbre de la recta como la dispersión de la nueva observación.

Ahora invirtamos la predicción con la incertidumbre total de la nueva indicación y la covarianza de los parámetros. La deducción está en el Anexo AX.6; la fórmula técnica corresponde a ISO/TS 28037 §11.1.3. Para una nueva indicación independiente de los datos de calibración declaramos $u(y)=0{,}20\ \mathrm{nmol/mol}$, que ya representa toda su variación. No añadimos otra vez $s_{\mathrm{res}}$: hacerlo sin identificar una fuente adicional sería doble conteo. El script obtiene $u(\hat x)=0{,}2564\ \mathrm{nmol/mol}$ [ISO 28037 §§11.1.1–11.1.3].

> **[PIZARRA]** $u^2(\hat x)\approx\dfrac{u^2(y)+u^2(a)+\hat x^2u^2(b)+2\hat x\,\operatorname{cov}(a,b)}{b^2}$, con la nueva indicación independiente de los parámetros.

La leemos así: sumamos la varianza total de la nueva indicación y las contribuciones del intercepto, la pendiente y su covarianza; dividimos por la pendiente al cuadrado. Si la indicación es un promedio, su incertidumbre debe corresponder a ese promedio. Si es una lectura futura cuya dispersión se estima con el residual, esa dispersión entra dentro de $u(y)$ una sola vez. La independencia entre la nueva indicación y los parámetros no elimina la covarianza interna de estos [ISO 28037 §11.1.3; GUM 5.2].

La cobertura no hereda automáticamente los cuatro grados de libertad residuales. Como anticipo del presupuesto de M8, el ejemplo supone $u(y)$ conocida con grados de libertad grandes y trata la contribución conjunta de los parámetros como un bloque con cuatro grados de libertad. La contribución de parámetros se agrupa como la única combinación escalar $a+\hat{x}b$, evaluada localmente en el valor estimado de $\hat{x}$: conserva $\operatorname{cov}(a,b)$ y su varianza depende de una sola escala residual. Esa combinación y la nueva indicación se suponen independientes. Así reducimos el presupuesto a dos componentes escalares independientes, dentro de la aproximación lineal; no aplicamos una fórmula diagonal a los parámetros correlacionados. Welch–Satterthwaite aplicado a esas dos componentes, no a $a$ y $b$ como si fueran independientes, da $\nu_{\mathrm{eff}}\approx25{,}83$, $k\approx2{,}056$ y $U\approx0{,}5273\ \mathrm{nmol/mol}$. Es una aproximación de cobertura, no un intervalo inverso exacto [GUM G.4.1; AX.7].

La convención del curso fija $k=t(0{,}975;\nu_{\mathrm{eff}})$ para un intervalo bilateral central del 95 % cuando corresponde. En las bandas de la recta, los grados de libertad son los residuales del modelo ajustado; en la predicción inversa con una `u(y)` externa, se combinan como acabamos de ver. No usen el símbolo `k` como si fuera siempre dos ni copien un cuantil sin registrar el nivel y los grados de libertad [prop_e §3; Crowder 2020 §10.3, PDF pp. 7–8]. La elección de cobertura y la integración de todas las contribuciones se completan en M8.

> **[ERROR CRÍTICO]** La semiamplitud $0{,}5273\ \mathrm{nmol/mol}$ es $U=k\,u$, no $u$. No reporten $u(\hat x)$ como incertidumbre expandida ni $U$ como estándar. No sumen el residual a una incertidumbre de nueva indicación que ya contiene esa misma dispersión.

### Escena I2. Intercepto libre o recta forzada al origen

> **[DIAPOSITIVA]** Comparar una recta con intercepto libre y una que pasa por el origen. Mostrar debajo los residuos de ambas, sin borrar ninguno.

Una recta forzada al origen fija $a = 0$ antes del ajuste y estima solo la pendiente. No es una manera de «limpiar» un intercepto incómodo. Es una hipótesis estructural: para todos los valores de referencia que entran en el ámbito declarado, cuando $x = 0$ la respuesta media debe ser cero conforme al modelo y a la definición de las magnitudes. Debe justificarse con conocimiento del proceso y con datos adecuados. La recta con intercepto libre tiene dos parámetros; la recta por el origen tiene uno. Al cambiar el modelo también cambian los valores predichos y la estructura de los residuos [ISO 28037 §5.8; Crowder 2020 §10.2.1, PDF p. 5].

Volvamos al conjunto simulado. La pendiente de la recta con intercepto libre es `1,00143`. Si fijamos el intercepto a cero, la pendiente se vuelve `1,00209`. El script reproduce ambos valores. La diferencia surge porque la restricción cambia la geometría del ajuste: el modelo sin intercepto no puede acomodar una desviación constante moviendo `a`, así que esa desviación repercute en la pendiente. Estos datos no justifican elegir uno u otro modelo para un instrumento real; ilustran por qué una restricción debe decidirse antes del ajuste y validarse, no activarse porque mejora una cifra [script `calc/M07_ejemplos.py`].

En una curva fotométrica, el cero inicial y final pueden compartir nivel nominal y, sin embargo, corresponder a momentos diferentes. No se eliminan ni se promedian automáticamente para forzar una recta por el origen: su orden puede aportar evidencia de deriva y forma parte del diseño. Si la línea pasa cerca del origen no basta con que el intercepto «no sea significativo» en una muestra pequeña. La decisión requiere la pregunta de medición, la incertidumbre pertinente y una validación de los residuos bajo el modelo elegido [prop_e §5, M7; Crowder 2020 §10.4, PDF pp. 9–10].

> **[ERROR CRÍTICO]** No fuercen el origen para obtener un intercepto igual a cero ni para cumplir un criterio. La restricción debe tener fundamento previo y el modelo resultante debe revisarse con sus residuos.

### Escena I3. Mínimos cuadrados ponderados y elección de los pesos

> **[PIZARRA]** Escribir $Q(a,b)=\sum_i w_i[y_i-(a+bx_i)]^2$ y, para observaciones independientes, $w_i=1/u^2(y_i)$ cuando esas incertidumbres son las que describen adecuadamente la dispersión.

OLS asigna el mismo peso a todas las observaciones. Si las incertidumbres estándar de `y` cambian entre puntos y esa diferencia está cuantificada, WLS da más influencia a la observación más precisa. Bajo observaciones independientes y varianzas conocidas proporcionales a $u^2(y_i)$, el peso relativo es $w_i = 1/u^2(y_i)$. La recta minimiza la suma ponderada de cuadrados [Crowder 2020 §10.2.3, PDF p. 6; ISO 28037 §§6.1–6.2].

> **[NOTA AL INSTRUCTOR]** ISO 28037 §6.1.3 llama peso a $1/u(y_i)$ y minimiza la suma con ese peso al cuadrado. Aquí llamamos peso a $1/u^2(y_i)$ y lo usamos sin elevarlo otra vez al cuadrado: ambas formulaciones son equivalentes.

El peso no es una preferencia ni una palanca para acercar el resultado al valor esperado. Antes de ajustar, identifiquen el origen de cada `u(yᵢ)` y verifiquen que las unidades sean compatibles. Comprueben también si hay componentes compartidas. Las incertidumbres deben describir el residuo modelado. Si solo se conocen hasta un factor común, multiplicar todos los pesos por una misma constante no cambia la estimación puntual de los parámetros. Si esas varianzas se toman como absolutas, sí cambia la covarianza calculada de los parámetros y el valor de chi-cuadrado. Si solo son pesos relativos y estimamos una escala común a partir del residuo, esa reestimación compensa el factor común y la covarianza final no cambia. No confundamos ambas convenciones [ISO 28037 §§5.8, 6.2; Crowder 2020 §10.2.3]. Finalmente, WLS con pesos diagonales no representa covarianza entre puntos.

> **[MATERIAL]** Comparación OLS/WLS, datos **simulados**, todas las magnitudes salvo pesos en nmol/mol.

| $x$ | $y$ | $u(y)$ |
|---:|---:|---:|
| 0 | 0,4 | 0,25 |
| 100 | 100,5 | 0,30 |
| 200 | 200,8 | 0,40 |
| 300 | 300,2 | 0,60 |
| 400 | 401,4 | 0,90 |
| 500 | 500,5 | 1,20 |

En este ejemplo simulado, las incertidumbres estándar de `y` aumentan con el nivel: desde `0,25` hasta `1,20 nmol/mol`, con valores intermedios `0,30; 0,40; 0,60; 0,90`. Los pesos inversos de varianza que imprime el script disminuyen desde `16,0` hasta aproximadamente `0,694444`. Con los datos fijados para comparar los métodos, OLS da $a = 0{,}4476$ y $b = 1{,}000743$; WLS da $a = 0{,}4169$ y $b = 1{,}000921$. No hay una regla de que WLS tenga que mover la pendiente en una dirección predeterminada. El resultado depende de los datos y de los pesos justificados [script `calc/M07_ejemplos.py`].

El diagnóstico ponderado con chi-cuadrado frente a las incertidumbres declaradas pertenece al nivel A y se desarrolla en la Escena A2. Aquí aprendemos a elegir y justificar los pesos y a revisar los residuos [Crowder 2020 §10.2.3, PDF p. 6].

> **[PREGUNTA AL GRUPO]** Si el peso es inverso a la varianza, ¿qué sucede con la influencia relativa de una respuesta cuya incertidumbre estándar se duplica? — *Respuesta esperada:* su peso queda dividido por cuatro, si la incertidumbre es la que corresponde al modelo y no hay covarianzas omitidas.

No confundamos «incertidumbre del punto» con «incertidumbre del eje de referencia». El WLS de esta escena sigue tratando `x` como fijo. Si el error de `x` es relevante, aumentar o cambiar los pesos de `y` no resuelve el problema de ambos ejes: hace falta un método que reconozca la incertidumbre de las referencias. El nivel intermedio detiene ese ajuste con `x` fijo y escala el caso a A [prop_e §5, M7-I; ISO 28037 §§7–10].

> **[ERROR CRÍTICO]** No usen pesos elegidos después de ver los residuos para mejorar la apariencia de la recta. Cada peso requiere una fuente, una unidad, un modelo de incertidumbre y una regla reproducible.

### Escena I4. Error puro y falta de ajuste

> **[DIAPOSITIVA]** Proyectar un gráfico de residuos frente a `x`: en un panel, puntos dispersos sin estructura; en otro, curvatura que alterna residuos positivos y negativos.

Una regresión no termina con la lista de parámetros. Revisamos el patrón de residuos frente a referencia, el orden de medición y la dispersión. Una curva sistemática, una forma de embudo o una secuencia temporal son avisos de que la recta y el supuesto de varianza constante podrían no describir los datos. El gráfico no certifica un modelo, pero ayuda a detectar estructura omitida. Una desviación aparente se interpreta junto con el diseño y con la incertidumbre de los datos, no como orden automática de eliminar puntos [Crowder 2020 §10.4.1, PDF pp. 9–10; ISO 28037 §6.3].

La incertidumbre de pendiente no es un criterio de aceptación por sí sola. Aquí no añadimos otro contraste de hipótesis: las herramientas de M4 se aplican solo cuando la pregunta y el modelo lo justifican. En esta escena estudiamos si la forma lineal describe las medias de los niveles en relación con la variación de sus réplicas [Crowder 2020 §10.4.1, PDF pp. 9–10; Otto §6.1, tabla 6.1, p. 217].

La falta de ajuste separa dos fuentes que OLS agrupa en el residuo cuando hay réplicas al mismo valor de referencia. El **error puro** mide la variación entre réplicas dentro de un nivel; la **falta de ajuste** mide la discrepancia entre las medias observadas por nivel y la recta. La prueba convencional compara sus cuadrados medios, $F=\frac{SS_{\mathrm{LOF}}/(m-2)}{SS_{\mathrm{PE}}/(N-m)}$, donde `m` es el número de niveles distintos y `N` el total de observaciones. Esta descomposición exige réplicas reales bajo el mismo valor de referencia. Para la referencia F indicada suponemos errores independientes, normales y con varianza común; el número de niveles debe superar los dos parámetros y tiene que quedar información de error puro. Leemos la razón como «cuadrado medio de falta de ajuste dividido por cuadrado medio de error puro» [Otto §6.1, tabla 6.1, p. 217; prueba F de falta de ajuste, ecuación (6.20), p. 222].

> **[PIZARRA]** $F_{LOF}=\dfrac{SS_{LOF}/(m-2)}{SS_{PE}/(N-m)}$; distinguir «variación entre réplicas del mismo nivel» de «desviación de la media de nivel respecto de la recta».

> **[MATERIAL]** Falta de ajuste: datos **simulados**, nmol/mol. Cada columna de observación contiene una réplica independiente al mismo $x$.

| $x$ | $y_1$ | $y_2$ | $y_3$ |
|---:|---:|---:|---:|
| 0 | 0,1 | 0,2 | 0,3 |
| 100 | 100,2 | 100,1 | 100,3 |
| 200 | 200,0 | 200,1 | 200,2 |
| 300 | 301,0 | 301,1 | 301,2 |

En un conjunto simulado con cuatro niveles y tres observaciones independientes en cada nivel, el script separa $SS_{\mathrm{LOF}} = 0{,}966$ de $SS_{\mathrm{PE}} = 0{,}080$ y obtiene $F(2{,}8) = 48{,}3$, con $p = 3{,}422\times10^{-5}$. Este resultado significa que, en el ejemplo sintético y bajo los supuestos de la prueba, la discrepancia entre medias de nivel es grande en relación con la variación pura. No es una prueba sobre el certificado de CALAIRE, no identifica la causa de la discrepancia y no permite eliminar un nivel [script `calc/M07_ejemplos.py`].

La aplicación mecánica de esa prueba a las 48 lecturas de cada punto del F-PSMT-01 (ocho lecturas por día durante seis días) no queda justificada solo por el hecho de que el diseño tenga repeticiones. En el certificado, la referencia cambia entre días; esas repeticiones no son réplicas exactamente al mismo valor de `x`. Si se ignora esa variación de referencia, se podría atribuir al fotómetro una dispersión o una falta de ajuste que combina otras fuentes. Para usar una prueba convencional hacen falta réplicas verdaderas al mismo valor de referencia; si cambia la referencia, se necesita un modelo que trate esa variación. Este es un límite metodológico del procedimiento, no una acusación sobre el certificado ni sobre el instrumento [Otto §6.1, tabla 6.1, p. 217; F-PSMT-01, fuente propia del diseño].

> **[ERROR CRÍTICO]** No apliquen la prueba convencional de falta de ajuste a repeticiones en las que la referencia cambia para después interpretar la diferencia como error puro. Réplica significa misma condición de referencia conforme al modelo, no simplemente varias filas con el mismo nivel nominal.

El residuo relativo por nivel puede ayudar a ver la escala del desajuste en relación con la respuesta de ese nivel, pero cerca de cero el denominador hace inestable el porcentaje. En el ejemplo anterior el nivel cero arroja un porcentaje grande porque su media está próxima a cero; esa cifra no se debe leer como una discrepancia absoluta gigantesca. En la zona de cero se conserva y examina el residuo en unidades absolutas. El código presenta tanto la estimación de la media de nivel como su residuo para que la proporción no oculte la escala [Crowder 2020 §10.4.1, PDF pp. 9–10; script `calc/M07_ejemplos.py`].

### Práctica I — Elegir ponderación, cuantificar un uso y comprobar falta de ajuste

> **[PRÁCTICA]** Ahora ustedes preparan y justifican el modelo para un fotómetro de ozono: la indicación de $250{,}50$ nmol/mol que invertirán es una respuesta dentro del intervalo de trabajo y el resultado alimenta una decisión de uso, no una aceptación del instrumento. Todos los valores de este ejercicio son **simulados** mediante los datos fijados en `calc/M07_practicas_luna.py`; no son resultados de CALAIRE. La primera tabla representa seis niveles con incertidumbres estándar distintas en la indicación. El resultado de interés es la recta para describir los niveles; el enunciado establece independencia, `x` fijo y que $u(y_i)$ caracteriza las varianzas de las respuestas. No hay componentes compartidas. Comparen OLS, que da igual peso, con WLS usando $w_i=1/u^2(y_i)$.
>
> | $x$ (nmol/mol) | $y$ (nmol/mol) | $u(y)$ (nmol/mol) |
> |---:|---:|---:|
> | 0 | 0,4 | 0,25 |
> | 100 | 100,5 | 0,30 |
> | 200 | 200,8 | 0,40 |
> | 300 | 300,2 | 0,60 |
> | 400 | 401,4 | 0,90 |
> | 500 | 500,5 | 1,20 |
>
> Calculen ambas rectas y los pesos relativos. Después, para usar la recta B ya estimada en la práctica anterior en un fotómetro de ozono, tomen una indicación independiente $y=250{,}50$ nmol/mol, respuesta dentro del intervalo de trabajo, con incertidumbre estándar total $u(y)=0{,}20$ nmol/mol. El resultado alimenta una decisión de uso, no una aceptación del instrumento. Calculen $\hat x$, $u(\hat x)$ y $U$ para cobertura bilateral del 95 %, agrupando la incertidumbre conjunta de parámetros como un bloque con cuatro grados de libertad y declarando grande la contribución externa de $u(y)$. Para reproducir $\nu_{eff}$, traten $u(y)$ como de grados de libertad infinitos y el bloque de parámetros como de cuatro: $u_c^2=0{,}04+u_{param}^2$ y $\nu_{eff}=u_c^4/(u_{param}^4/4)$. No sumen otra vez $s_{res}$: la incertidumbre de la nueva indicación ya representa toda su variación.
>
> Calculen además las semiamplitudes de los intervalos puntuales del 95 % de confianza de la media y de predicción de una nueva respuesta en $x_0=250$ nmol/mol con la recta B. Comparen sus valores e indiquen qué variación adicional contiene la predicción. Los resultados de referencia son, aproximadamente, $0{,}447$ y $1{,}183$ nmol/mol.
>
> Por último, decidan si procede la prueba convencional de falta de ajuste para los siguientes datos. Cada columna contiene tres réplicas independientes al **mismo valor de referencia**, con errores normales independientes y varianza común según el modelo del ejercicio. Calculen error puro, falta de ajuste, estadístico F y decisión al 5 %.
>
> | $x$ (nmol/mol) | $y_1$ | $y_2$ | $y_3$ |
> |---:|---:|---:|---:|
> | 0 | 0,1 | 0,2 | 0,3 |
> | 100 | 100,2 | 100,1 | 100,3 |
> | 200 | 200,0 | 200,1 | 200,2 |
> | 300 | 301,0 | 301,1 | 301,2 |
>
> **Solución docente.** En la primera tabla, OLS resulta $a=0{,}447619$ nmol/mol, $b=1{,}000742857$; WLS da $a=0{,}416852$ nmol/mol, $b=1{,}000921340$. Los pesos $1/u²$ son $16;11{,}111111;6{,}25;2{,}777778;1{,}234568;0{,}694444$ (inversos de nmol/mol al cuadrado; son relativos para estimar la recta). La menor incertidumbre recibe mayor peso. La diferencia entre pendientes es pequeña y su dirección no es una regla general; manda el modelo de varianza justificado.
>
> Para la inversión, la práctica B entrega $\hat x=249{,}900143$ nmol/mol y corrección $-0{,}599857$ nmol/mol. La propagación lineal de la nueva indicación y de los parámetros da $u(\hat x)=0{,}256446$ nmol/mol; con el agrupamiento y cobertura declarados, $u_c^2=0{,}04+u_{param}^2$, tratando $u(y)$ con grados de libertad infinitos y el bloque de parámetros con cuatro; así, $\nu_{eff}=u_c^4/(u_{param}^4/4)=25{,}8325$, $k=t(0{,}975;\nu_{eff})=2{,}05618$ y $U=0{,}527298$ nmol/mol. Comprobación: $U=k u=2{,}05618\times0{,}256446$. Es una incertidumbre de uso bajo el modelo y los supuestos expresos, no un presupuesto universal ni una segunda suma del residual.
>
> Para $x_0=250$ nmol/mol, la banda puntual de confianza de la media tiene semiamplitud $0{,}4473$ nmol/mol y la de predicción de una nueva respuesta $1{,}183$ nmol/mol. La segunda incorpora la dispersión de una nueva observación, por eso es más ancha; no es una banda simultánea en todo el intervalo.
>
> En las réplicas al mismo $x$, el ajuste OLS da $a=0{,}01$ nmol/mol y $b=1{,}0026$. La suma de cuadrados de falta de ajuste es $SS_{LOF}=0{,}966$, con 2 grados de libertad; la de error puro $SS_{PE}=0{,}080$, con 8 grados de libertad. Por tanto $F=(0{,}966/2)/(0{,}080/8)=48{,}3$ y $p=0{,}0000342$. Se rechaza la adecuación de la recta bajo el modelo de prueba al 5 %; esto señala discrepancia de forma relativa al error puro, no identifica la causa ni autoriza a descartar un punto.
>
> **Interpretación y escalamiento.** La prueba solo es válida aquí porque se especifican réplicas verdaderas al mismo valor de referencia. No se trasladaría mecánicamente a ocho lecturas repartidas en días si la referencia cambia entre días: en ese diseño la variación de referencia no es error puro del fotómetro. Si $u(x)$ es relevante, si hay dependencia/covarianzas omitidas, pesos no sustentados o estructura residual, I detiene el ajuste con `x` fijo y eleva a A; no intenta resolverlo retocando pesos.
>
> **Criterio de logro.** Justifica OLS/WLS a partir de la estructura dada, calcula la incertidumbre de uso sin doble conteo y concluye sobre falta de ajuste solo tras verificar réplicas y grados de libertad.

### Señales de escalamiento en I

Detengan el ajuste con `x` fijo cuando la incertidumbre de la referencia sea relevante para la pendiente, el intercepto o la predicción requerida; escalen a A para escoger un modelo que represente ambos ejes. También escalen si las incertidumbres de `y` no están disponibles o cambian por causas compartidas, si hay dependencia entre puntos, si los residuos muestran curvatura o estructura temporal, si los pesos no se pueden justificar, si se desea restringir el intercepto sin base previa, si una falta de ajuste se pretende probar sin réplicas válidas o si la referencia varía entre repeticiones. Una no significación no valida automáticamente la recta, y una significación no autoriza por sí sola a descartar observaciones [prop_e §2, §5 M7-I; ISO 28037 §§5.2.2, 6.3].

> **[ESCALAMIENTO]** En la ficha de decisión dejen asentado qué eje se considera conocido, qué incertidumbres se incluyen, qué estructura de covarianza se supone y por qué. Cuando la incertidumbre de `x` importa, I no intenta compensarla con WLS de `y`: detiene y consulta al responsable técnico de A.

## Nivel A — regresión con incertidumbre en ambos ejes

En el nivel avanzado damos por vistos OLS, WLS, el análisis de residuos, la incertidumbre de los parámetros y las limitaciones de la inversión. Añadimos el caso en que la incertidumbre de referencia `x` no es despreciable y debe entrar junto con la de indicación `y`, así como una estructura de covarianza que puede relacionar distintos puntos. La meta no es reemplazar siempre OLS, sino elegir un ajuste coherente con la información de incertidumbre y validar la herramienta dentro de su alcance [prop_e §5, M7-A].

### Escena A1. Ambos ejes son inciertos: distinguir WLS de GGMR

> **[DIAPOSITIVA]** Representar cada punto como una elipse de incertidumbre, y dibujar una recta que se ajusta considerando desplazamientos tanto horizontales como verticales. Al costado, mostrar una matriz de covarianza en bloques para `x` e `y`.

En OLS y en el WLS que vimos en I, el ajuste minimiza discrepancias verticales y trata las referencias como conocidas. Si cada referencia tiene una incertidumbre relevante, mover el punto solo en vertical no representa el problema. Hace falta un método que considere las incertidumbres de ambos ejes. La regresión generalizada de Gauss–Markov, GGMR según la terminología de este curso, estima los parámetros de la función y las abscisas ajustadas. La función objetivo es una suma cuadrática generalizada basada en la matriz conjunta de covarianza de las observaciones `x` e `y` [ISO 28037 §§10.1–10.3; prop_e §5, M7-A].

Digo «generalizada» porque no se supone que cada punto aporte dos errores independientes de cualquier otro punto. La matriz de covarianza puede incluir incertidumbres distintas y componentes compartidas entre puntos. Los bloques describen la covarianza dentro de `x`, dentro de `y` y entre los dos ejes. En el alcance curricular de la herramienta que usamos en este curso, el bloque cruzado entre ejes se fija en cero: $V_{xy}=0$. El script docente se contrasta más adelante con un ejemplo publicado dentro de ese alcance; no lo presentamos como herramienta autorizada para producción. Aun con ese bloque nulo, las matrices `V_x` y `V_y` pueden incluir correlaciones entre puntos. Este alcance restringido no autoriza a afirmar que cualquier problema real tenga $V_{xy} = 0$; si la estructura cruzada es distinta, se escala y no se fuerza la entrada a la herramienta disponible. La formulación matricial está en el Anexo AX.8; aquí la usamos [ISO 28037 §§5.2.2, 10.1–10.3; AX.8].

> **[PIZARRA]** $\min_{a,b,\,x^*}\;\begin{bmatrix}x-x^*\\y-(a+bx^*)\end{bmatrix}^{T}V^{-1}\begin{bmatrix}x-x^*\\y-(a+bx^*)\end{bmatrix}$, con $V=\begin{bmatrix}V_x&V_{xy}\\V_{yx}&V_y\end{bmatrix}$; para el alcance validado del ejemplo, $V_{xy}=0$.
>
> **[NOTA AL INSTRUCTOR]** Leer la expresión como «se eligen el intercepto, la pendiente y las abscisas ajustadas para minimizar la discrepancia conjunta ponderada por la inversa de la matriz de covarianza». No derivar el algoritmo ni presentar esta expresión como un ejercicio manual.

Las abscisas ajustadas son estimaciones de los valores de referencia compatibles con el modelo y las incertidumbres reportadas. No equivalen a reemplazar `x` por un promedio simple ni a cambiar la orientación de la función. El método mantiene `y` como indicación modelada por una función de `x`, mientras reconoce que ambos ejes tienen error. Por eso no es «WLS con un peso adicional»: WLS con `x` fijo no estima las referencias ajustadas y no trata la matriz conjunta de incertidumbre [ISO 28037 §§9–10; prop_e §5, M7-A].

> **[ERROR CRÍTICO]** No llamen GGMR a un ajuste ordinario de `y` sobre `x` que solo incorpora pesos verticales. Tampoco introduzcan correlación cruzada no nula entre ejes en una herramienta validada únicamente con $V_{xy} = 0$.

Veamos un ejemplo sintético para leer la salida, no para validar una implementación de producción. Usamos seis referencias observadas $x = 0; 100; 200; 300; 400; 500 \ \mathrm{nmol/mol}$ y seis indicaciones simuladas $y = 0{,}3; 100{,}4; 200{,}7; 300{,}5; 401{,}0; 500{,}9 \ \mathrm{nmol/mol}$. A una componente independiente de cada referencia, $u(x_i) = 0{,}25 \ \mathrm{nmol/mol}$, añadimos una componente común a todas de `0,12 nmol/mol`; $u(y_i) = 0{,}40 \ \mathrm{nmol/mol}$ y $V_{xy} = 0$. La matriz `V_x` contiene una contribución independiente por punto y otra componente común entre puntos; `V_y` es diagonal; la covarianza cruzada es nula. El script minimiza la suma cuadrática generalizada y entrega $a \approx 0{,}3047 \ \mathrm{nmol/mol}$, $b = 1{,}001314$ y las seis abscisas ajustadas, aproximadamente `0,00; 99,99; 200,04; 299,94; 400,05; 499,98 nmol/mol`. Los datos y la covarianza se fijaron para enseñar cómo se organiza la entrada; no representan el SRP 55, el Level 2 ni CALAIRE [script `calc/M07_ejemplos.py`; datos simulados].

En este ejemplo el valor de chi-cuadrado ponderado es `0,4089`. La salida y sus grados de libertad deben interpretarse conforme a la definición del modelo implementado y al protocolo de validación; no se infiere que un chi-cuadrado pequeño siempre sea bueno. Para esta demostración hay doce coordenadas observadas y ocho parámetros ajustados: seis abscisas, intercepto y pendiente. Con matrices conocidas y definidas positivas, errores conjuntamente normales y aproximación local válida, quedan cuatro grados de libertad. La distribución chi-cuadrado es aquí una referencia aproximada, no una certificación de conformidad del ajuste real [script `calc/M07_ejemplos.py`; ISO 28037 §10.3].

Antes del diagnóstico, comparemos los tres métodos sobre esos mismos seis pares simulados, siempre con referencia en el eje horizontal. OLS y WLS coinciden aquí porque todas las incertidumbres verticales valen lo mismo: dan $a\approx0{,}3048\ \mathrm{nmol/mol}$ y $b\approx1{,}001314$. GGMR da valores muy próximos, pero además estima las abscisas. La componente común aditiva de referencia no se reduce al añadir puntos: en GGMR, $u(a)$ pasa de $0{,}342$ sin componente común a $0{,}362\ \mathrm{nmol/mol}$; no cambia apreciablemente la pendiente ni su incertidumbre. Esto ilustra su efecto en la incertidumbre, aunque el ajuste puntual apenas se mueva [ISO 28037 §§10.1–10.2; script `calc/M07_ejemplos.py`].

Vamos ahora a comprobar el programa con datos **publicados**, no simulados ni propios: ISO/TS 28037 §10.3, tablas 25 y 26, pp. 35–36 impresas (PDF pp. 43–44). Son siete pares, con covarianzas entre referencias y entre respuestas, y bloque cruzado nulo. El script conserva los valores y matrices publicados, sin cambiar unidades ni orientación. Obtiene $a\approx0{,}3424$, $b\approx1{,}001231$ y $\chi^2\approx1{,}772$. La norma publica $0{,}3424$, $1{,}0012$ y $1{,}772$: coinciden al redondeo publicado. También concuerdan las siete abscisas ajustadas, $u(a)\approx2{,}0569$, $u(b)\approx0{,}0090$ y $\operatorname{cov}(a,b)\approx-0{,}0129$, en las unidades del ejemplo normativo. Comprobar este caso aporta evidencia reproducible del cálculo, no una validación universal de cualquier implementación o estructura de covarianza [ISO 28037 §10.3, tablas 25–26].

### Escena A2. Residuos ponderados y coherencia del ajuste

> **[DIAPOSITIVA]** Mostrar residuos ponderados por punto y una distribución de chi-cuadrado de referencia con una región central y colas. Rotular «diagnóstico condicionado al modelo, covarianza y grados de libertad».

En el ajuste generalizado, los residuos se interpretan después de considerar la matriz de covarianza. Un residuo ponderado representa la discrepancia en relación con la incertidumbre y la dependencia que el modelo declara; no es simplemente un residuo bruto dividido por una desviación cualquiera. En el script blanqueamos los desplazamientos de cada eje con su factor de Cholesky: $z_x=L_x^{-1}(x-x^*)$ y $z_y=L_y^{-1}[y-a-bx^*]$, donde $V_x=L_xL_x^T$ y $V_y=L_yL_y^T$. Lo leemos como transformar las discrepancias por la estructura de covarianza; la suma de sus cuadrados es el objetivo $Q$. Sus componentes no son pruebas independientes después de ajustar ni residuos studentizados por su varianza residual: el ajuste consume grados de libertad. Con correlación entre puntos, tampoco conservan una interpretación estrictamente local por punto, pues la transformación mezcla información. La validación puede resumir la discrepancia conjunta con un estadístico chi-cuadrado y contrastarlo con la distribución o el criterio que corresponde al procedimiento. También se examinan los residuos por punto, porque un único resumen puede ocultar un patrón local [ISO 28037 §10.3].

> **[MATERIAL]** Diagnóstico WLS: datos **simulados**, nmol/mol. Generación: $y_i=0{,}3+1{,}001x_i+\delta_i$, con desviaciones fijadas en el script.

| $x$ | $y$ | $u(y)$ |
|---:|---:|---:|
| 0 | 0,40 | 0,30 |
| 50 | 50,15 | 0,35 |
| 100 | 100,55 | 0,40 |
| 150 | 150,35 | 0,45 |
| 200 | 200,75 | 0,50 |
| 250 | 250,40 | 0,55 |
| 300 | 300,80 | 0,60 |
| 350 | 350,40 | 0,65 |
| 400 | 400,80 | 0,70 |
| 450 | 450,65 | 0,75 |
| 500 | 500,95 | 0,80 |
| 550 | 550,80 | 0,85 |

Empecemos por el caso más simple, todavía con `x` fijo, para separar el diagnóstico global de la validación punto a punto. En un ejemplo **simulado** ponderado de 12 niveles entre `0` y `550 nmol/mol`, con `u(y)` de `0,30; 0,35; 0,40; 0,45; 0,50; 0,55; 0,60; 0,65; 0,70; 0,75; 0,80; 0,85 nmol/mol`, en ese orden, el script calcula $\chi^2_{\mathrm{obs}} = 1{,}280$ con $\nu = n - 2 = 10$ grados de libertad. Aquí $\nu = n - 2$ porque la recta tiene dos parámetros y suponemos errores normales independientes con las varianzas absolutas suministradas, sin reestimar una escala residual; si cambia el modelo o hay dependencia, se revisan los grados de libertad. Como diagnóstico global superior, se compara con $\chi^2_{0{,}95;10}=18{,}31$; el estadístico no excede ese cuantil. Esto no demuestra que el modelo sea correcto ni constituye por sí solo una aceptación de la calibración. Por separado, ISO 6143 §5.2.2 pide que cada punto cumpla $|\hat x_i - x_i| \le  2u(x_i)$ y $|\hat y_i - y_i| \le  2u(y_i)$; su nota relaciona el factor 2 con $k = 2$. En este ejemplo WLS mantiene `x` fijo, así que la primera diferencia es cero y la segunda se reduce a $|\hat y_i - y_i|/u(y_i)$; el máximo simulado es `0,6160`, menor que 2. En un ajuste que también estima `x`, se comprueban ambas coordenadas [script `calc/M07_ejemplos.py`; ISO 6143 §5.2.2].

Un valor alto de chi-cuadrado puede indicar que la dispersión observada es grande en relación con las incertidumbres declaradas, que la función no representa la forma de los datos o que se omitió una dependencia. No identifica por sí mismo cuál explicación es correcta. Un valor anormalmente bajo tampoco es una medalla automática: puede señalar incertidumbres sobreestimadas, dependencias omitidas, datos excesivamente ajustados o una incompatibilidad entre la matriz declarada y el proceso. El diagnóstico se contrasta con los residuos, el diseño, las unidades de cada matriz y la revisión de entradas; no se corrigen incertidumbres para obtener un chi-cuadrado «bonito» [ISO 28037 §§5.2.2, 10.3; prop_e §5, M7-A].

El ejemplo GGMR anterior arroja $\chi^2 = 0{,}4089$ con cuatro grados de libertad del ejercicio, un valor pequeño respecto de esa escala. El mismo script construye un segundo conjunto sintético casi exactamente lineal con las mismas covarianzas; su chi-cuadrado es del orden de $10^{-29}$; el último dígito depende de la plataforma de cálculo. Esa cifra extrema surge porque los datos fueron generados directamente sobre una recta y no contienen variación coherente con las incertidumbres declaradas. Para mostrar el otro extremo, al añadir cinco nmol/mol a una respuesta simulada del conjunto inicial, el estadístico sube a `83,36`. La cola inferior del caso inicial es aproximadamente $0{,}01826$: también merece investigación por resultar pequeño. En el caso perturbado, la cola superior es aproximadamente $3{,}38\times10^{-17}$. Son diagnósticos de extremos, no un nuevo criterio normativo bilateral. Esto alerta de una discrepancia muy grande respecto del modelo y de las incertidumbres fijadas, pero no identifica su causa ni autoriza a excluir el punto. Los tres cálculos son ilustraciones sintéticas; no inferimos de ellos un umbral universal ni una regla de aceptación para cualquier calibración [script `calc/M07_ejemplos.py`].

> **[PREGUNTA AL GRUPO]** Si chi-cuadrado es mucho menor de lo esperado, ¿se concluye directamente que el ajuste es excelente? — *Respuesta esperada:* no; revisamos si las incertidumbres están sobreestimadas, si hay dependencia no modelada, si los datos fueron generados o filtrados de forma que elimine variación y si los grados de libertad corresponden al modelo.

> **[ERROR CRÍTICO]** No interpreten un chi-cuadrado alto como permiso para borrar el punto que más contribuye ni un chi-cuadrado bajo como prueba automática de calidad. La respuesta es revisar modelo, estructura de covarianza, datos y cálculo, conservando los registros originales.

La matriz conjunta debe cumplir las propiedades numéricas y metrológicas que el modelo requiere. Antes de confiar en una salida, el responsable técnico verifica simetría, unidades, componentes compartidas, método numérico y comportamiento frente a ejemplos de referencia dentro del alcance validado. El cálculo docente de este capítulo trabaja con $V_{xy} = 0$. Lo contrastamos con el ejemplo publicado que acabamos de resolver, pero ese contraste no valida todas las matrices posibles ni autoriza uso de producción. Cualquier necesidad de covarianza cruzada no nula, estructura que el programa no admita o resultado sensible a una hipótesis no comprobada se escala. No se sustituye ese análisis por la selección del ajuste que produzca una recta más cercana a la identidad [prop_e §5, M7-A; ISO 28037 §§5.2.2, 10.1–10.3].

### Práctica A — Contrastar OLS, WLS y GGMR y validar el cálculo

> **[PRÁCTICA]** Ustedes reciben el mismo conjunto sintético para los tres métodos, con la orientación común $x$ referencia y $y$ indicación en un punto de calibración de un fotómetro de ozono; el ajuste informa una decisión estadística sobre el uso, no una aceptación del instrumento. Los seis pares son **simulados**, con regla reproducible: se fijaron las referencias indicadas y las respuestas, y se declararon incertidumbres estándar independientes de $0{,}25$ nmol/mol por punto en $x$ y $0{,}40$ nmol/mol por punto en $y$. A $x$ se añade una componente común de $0{,}12$ nmol/mol para todos los puntos, por lo que $V_x=0{,}25²I+0{,}12²11^T$; $V_y=0{,}40²I$ y $V_{xy}=0$. La respuesta de interés es la recta con referencias ajustadas bajo GGMR; se asumen matrices conocidas y definidas positivas, errores conjuntos normales y alcance validado de la herramienta con covarianza cruzada nula. Estos datos no describen SRP 55, Level 2 ni CALAIRE.
>
> | Punto | $x$ referencia (nmol/mol) | $y$ indicación (nmol/mol) |
> |---:|---:|---:|
> | 1 | 0 | 0,3 |
> | 2 | 100 | 100,4 |
> | 3 | 200 | 200,7 |
> | 4 | 300 | 300,5 |
> | 5 | 400 | 401,0 |
> | 6 | 500 | 500,9 |
>
> Ajusten el mismo conjunto por OLS, WLS con los errores verticales indicados y GGMR con $V_x,V_y,V_{xy}$ declaradas. No cambien los ejes entre métodos. Informen pendiente e intercepto, y para GGMR las seis abscisas ajustadas, el objetivo cuadrático $Q$ y los grados de libertad del ejemplo. Comparen el efecto de incluir la componente común en $u(a)$ y expliquen por qué añadir puntos no promedia esa fuente compartida. Calculen los residuos ponderados blanqueados $z_x$ y $z_y$ definidos en la Escena A2, comprueben que la suma de sus cuadrados es $Q$, comparen $Q$ con la distribución de chi-cuadrado de cuatro grados de libertad e informen la cola superior; expliquen por qué ese p-valor no prueba por sí solo la validez del modelo. Como comprobación independiente de implementación, ejecuten `calc/M07_practicas_luna.py`, que contrasta el ajuste con los datos y matrices **publicados sin modificar** de ISO/TS 28037:2010 §10.3, tablas 25–26. No presenten el contraste como validación universal ni como aprobación para producción.
>
> **Solución docente.** En los seis pares sintéticos, OLS y WLS coinciden porque todos los $u(y_i)$ son iguales: $a=0{,}304762$ nmol/mol y $b=1{,}00131429$. GGMR da $a=0{,}304725$ nmol/mol y $b=1{,}00131443$, con abscisas ajustadas $-0{,}00133;99{,}98983;200{,}03721;299{,}94405;400{,}04764;499{,}98259$ nmol/mol. El objetivo es $Q=0{,}408901$. Los residuos blanqueados son $z_x=(0{,}004789;0{,}036405;-0{,}145066;0{,}223088;-0{,}193772;0{,}073270)$ y $z_y=(-0{,}008489;-0{,}064974;0{,}237826;-0{,}357587;0{,}304498;-0{,}111273)$, redondeados; la suma de sus cuadrados reproduce $Q$. Para las doce coordenadas observadas, el ejemplo declara ocho parámetros ajustados (seis abscisas, intercepto y pendiente), de modo que quedan cuatro grados de libertad. La cola superior es $p=0{,}98174$: no hay señal de discrepancia grande bajo el modelo, pero este p-valor no demuestra que la estructura, las covarianzas o los supuestos sean verdaderos. La cifra pequeña no certifica bondad por sí sola: se interpreta con las matrices, el modelo y la validación.
>
> Al omitir la componente común, el error estándar calculado de $a$ es $0{,}341517$ nmol/mol; al incluirla sube a $0{,}362038$ nmol/mol, mientras que $u(b)=0{,}001128$. La componente común desplaza conjuntamente las referencias y no se reduce como si fueran seis fuentes independientes. La simetría de cada matriz, sus unidades cuadradas de nmol/mol y la forma de componente común deben comprobarse antes de ajustar; las matrices declaradas son simétricas y definidas positivas. GGMR estima referencias ajustadas y considera ambos ejes; no equivale a WLS vertical.
>
> En el contraste publicado, el script obtiene $a=0{,}3424009$, $b=1{,}0012308$ y $Q=1{,}771847$, frente a los valores publicados $0{,}3424$, $1{,}0012$ y $1{,}772$. También comprueba $u(a)=2{,}0569$, $u(b)=0{,}0090$, $cov(a,b)=-0{,}0129$ y las abscisas ajustadas contra tablas 25–26; las aserciones del script terminan en PASS al redondeo publicado. Los datos y covarianzas de esa verificación se mantienen tal como aparecen en la norma. El resultado ofrece una comprobación reproducible de este caso, no demuestra que cualquier estructura de covarianza o cualquier código sea correcto.
>
> **Interpretación operativa y escalamiento.** Los métodos OLS/WLS dejan $x$ fijo y coinciden en este conjunto por pesos verticales iguales; GGMR cambia el planteamiento al incorporar $u(x)$ y la dependencia común. Si $V_{xy}$ no es cero, no se fuerza la matriz a este procedimiento: se detiene y se consulta al responsable técnico. También se escala ante matrices no reconstruibles desde sus fuentes, unidades incompatibles, falta de simetría/definición positiva, resultado sensible a hipótesis no verificadas o discrepancia con el ejemplo publicado. Nada de esta práctica autoriza un uso de producción.
>
> **Criterio de logro.** Mantiene la misma orientación para los tres métodos, configura y comprueba las matrices declaradas, interpreta la componente común y reproduce los valores de referencia ISO dentro del redondeo publicado sin atribuirlos a CALAIRE.

> **[ESCALAMIENTO]** Si la covarianza cruzada entre `x` e `y` puede ser distinta de cero, si no se puede reconstruir la matriz de incertidumbre desde sus causas o si la herramienta no ha sido contrastada para la estructura del caso, se detiene el ajuste y se solicita revisión técnica. El alcance de esta formación no cubre GGMR con $V_{xy} \ne  0$.

## Cierre del capítulo

En el nivel básico ustedes aprendieron a leer una recta OLS en la orientación acordada, a distinguir correlación y R² de validación, a conservar el intervalo de uso y a invertir la recta con la corrección $\hat x - y$ en el signo correcto. En el intermedio añadimos la incertidumbre y covarianza de los parámetros, la diferencia entre bandas de confianza y predicción, el origen forzado, WLS y la prueba de falta de ajuste cuando hay réplicas válidas. También fijamos una señal clara: si la incertidumbre de la referencia importa, no la ocultamos dentro de pesos verticales; detenemos el ajuste con `x` fijo y escalamos. En el avanzado consideramos ambos ejes y las covarianzas admitidas por GGMR, y examinamos tanto valores altos como anormalmente bajos de chi-cuadrado.

La regresión entrega una función y una predicción; todavía falta expresar qué incertidumbre corresponde al resultado que ustedes reportan y cómo se propaga a un valor de uso. Ese será el siguiente paso. En M8 construiremos el presupuesto de incertidumbre, combinaremos contribuciones conforme al modelo y distinguiremos el resultado de calibración del uso futuro [prop_e §5, M7–M8].

## Referencias del capítulo

- **Crowder 2020** — Crowder, S.; Delker, C.; Forrest, E.; Martin, N. *Introduction to Statistics in Metrology*. Springer, Cham, 2020, capítulo 10, especialmente §§10.1–10.4. Archivo: `docs/intro_stats_metro_c10.pdf`.
- **ISO 28037** — ISO/TS 28037:2010, *Determination and use of straight-line calibration functions*. International Organization for Standardization. Archivo: `docs/ISO 28037.pdf`.
- **ISO 6143** — ISO 6143:2001, *Gas analysis — Comparison methods for determining and checking the composition of calibration gas mixtures*. International Organization for Standardization, §5.2.2. Archivo: `docs/ISO 6143 2001.pdf`.
- **Hahs-Vaughn** — Hahs-Vaughn, D. L.; Lomax, R. G. *Statistical Concepts: A First Course*. Routledge, primera publicación 2020 (selección de los diez primeros capítulos de *An Introduction to Statistical Concepts*, 4.ª ed.), capítulo 10 (asociación bivariada; no regresión). Archivos: `docs/statistical_concepts_c10.pdf` y `docs/Statistical Concepts – A First Course.pdf`; §10.1.1.5.2, restricción del intervalo (verificado en el libro completo).
- **Otto** — Otto, M. *Chemometrics: Statistics and Computer Application in Analytical Chemistry*, 3.ª ed. Wiley-VCH, 2017. Archivo: `docs/Chemometrics Statistics and Computer Application.pdf`; §6.1, tabla 6.1 (descomposición de sumas de cuadrados con falta de ajuste y error puro), p. 217 del libro.
- **GUM** — JCGM 100:2008 (ISO/IEC Guide 98-3:2008), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, 5.2 y G.4. Archivo: `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **F-PSMT-01** — CALAIRE, certificado G1 S/N 59756-324. Archivo propio: `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm` (solo estructura del diseño).
- **prop_e** — Propuesta E: curso de estadística aplicada a la fotometría de ozono, §3 y §5, módulo M7. Documento curricular del curso.
- **AX.5, AX.6, AX.7 y AX.8** — Anexos de deducciones del curso: ecuaciones normales y covarianza de parámetros; incertidumbre de predicción inversa por linealización; Welch–Satterthwaite; formulación matricial de GGMR con $V_{xy} = 0$.

- **VIM** — JCGM 200:2012, *International vocabulary of metrology — Basic and general concepts and associated terms*, 3.ª ed. (no disponible en docs/; definición de corrección, sin numeral).
