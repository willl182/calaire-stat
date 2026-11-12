# M04. Inferencia: estimación y contraste

## Sesión 3 (120 min)

| Bloque | Minutos |
|---|---:|
| Revisión de la tarea de la sesión anterior | 15 |
| Narración B + I (≈25 min a 130 palabras/min) | 25 |
| Ejemplos en pizarra, lectura de gráficos y discusión guiada | 20 |
| Práctica B — en clase | 25 |
| Práctica I — en clase → tarea | 15 |
| Preguntas y cierre | 20 |
| **Total** | **120** |

## Revisión de la tarea de la sesión anterior (15 min)

**Guion de revisión de la práctica I de M03.** Pidan que presenten los seis pares del gráfico normal y cómo calcularon las posiciones de Blom; lean los pares teóricos y errores ordenados, sin volver a estimarlos. Revisen la secuencia bajo–centro–alto como señal descriptiva de posible dependencia temporal, no como prueba de normalidad ni autocorrelación. Cierren distinguiendo covarianza declarada, forma marginal y orden temporal, y recuerden que chi-cuadrado y F se reconocieron en M03 pero sus pruebas se aplican en esta sesión.

## Ficha del capítulo

| Elemento | Alcance |
|---|---|
| Competencia estadística | Estimar un efecto con su intervalo y contrastar hipótesis, distinguiendo significación estadística de relevancia metrológica. |
| Prerrequisitos | M2: descripción, dispersión y elección de la respuesta. M3-B: distribución t, cuantiles y grados de libertad. M3-I: covarianza, chi-cuadrado y F. |
| Nivel B | Grados de libertad; intervalo de confianza con t; hipótesis, valor p y errores de decisión; prueba t de un error medio en un nivel, con la unidad de repetición justificada en el enunciado. |
| Nivel I añade | t pareada y Welch; intervalos y pruebas sobre varianzas (chi-cuadrado, F); potencia y tamaño de muestra según el diseño (media, pareadas, dos grupos); incertidumbre de una desviación estimada; pruebas de Grubbs y Dixon solo bajo sus condiciones de aplicación. |
| Datos de ejemplos | **Simulados** y generados por `calc/M04_ejemplos.py`; ilustran cálculos y no describen resultados de CALAIRE. El certificado F-PSMT-01, Level 2 Thermo 49C frente al SRP 55, aporta el contexto del caso, no datos atribuibles a los ejemplos. |
| Deducciones | Divisor de la varianza muestral y Welch–Satterthwaite: fuera del alcance de este curso. |
| Referencias clave | Hahs-Vaughn §§5.2, 6.1, 6.4–6.5, 7.1–7.2, 7.8 y 9.1–9.3; GUM §§4.3.2 y E.4.3; Otto §2.2. |

## Nivel B — estimar y contrastar una media

> **[NOTA AL INSTRUCTOR]** Cifras reproducibles con `calc/M04_ejemplos.py`.

Al comenzar, les digo que en este nivel ya damos por vistas la forma de describir una muestra y la diferencia entre dispersión de las lecturas y error estándar. También damos por vistas las distribuciones y los cuantiles de M3. Hoy usaremos esas herramientas para contestar una pregunta concreta del laboratorio: ¿qué tan grande puede ser el error medio de un fotómetro en un nivel, y qué evidencia tenemos para decir que difiere de cero o de un valor que sí importe? No vamos a convertir una falta de evidencia en una afirmación de igualdad. [Hahs-Vaughn §5.2; §6.1]

### Escena B1. De la muestra al estimador

> **[DIAPOSITIVA]** Una población de errores posibles, una muestra seleccionada y la media muestral que se calcula.

Para empezar, fijamos qué media queremos estimar. En el caso del laboratorio, usamos el error con signo $e=y-x$: la indicación menos el valor de referencia. La respuesta de interés es el error medio en un nivel de concentración y bajo las condiciones declaradas. Con una muestra calculamos una media, pero el resultado de otra muestra no sería necesariamente idéntico. Por eso el valor puntual debe acompañarse de un intervalo que refleje la variación del procedimiento de estimación. [Hahs-Vaughn §5.2; §6.1]

La media muestral y su error estándar resumen, respectivamente, el centro estimado y su variación debida al muestreo bajo el modelo. El error estándar no describe la amplitud de las lecturas individuales. En este capítulo nos concentramos en esa media y su inferencia; no estamos estimando aquí la dispersión de futuras lecturas ni introduciendo otros modelos de población. [Hahs-Vaughn §5.2; §6.1]

> **[PIZARRA]** Para observaciones independientes $e_1,\ldots,e_n$, escribimos $\bar e=\frac{1}{n}\sum_{i=1}^n e_i$ y $SE(\bar e)=s/\sqrt n$. La desviación estándar muestral $s$ se recupera de M2; hoy usamos su relación con la media. La última expresión se lee: «el error estándar de la media es la desviación estándar muestral dividida por la raíz cuadrada del número de observaciones».

La desviación estándar $s$ describe la variación entre observaciones; el error estándar describe la variación del estimador de la media. Si $s$ mide cuánto fluctúan las lecturas, $SE(\bar e)$ mide cuánto esperamos que fluctúe el promedio bajo las hipótesis de independencia y muestreo común. Si la unidad de repetición no es independiente, sustituir el número de filas por $n$ no arregla el problema. Las lecturas consecutivas pueden compartir condiciones y deriva. En tal caso, el denominador debe reflejar las unidades independientes del diseño o necesitamos otro modelo. [Hahs-Vaughn §5.2; §6.1]

Los grados de libertad expresan cuánta información independiente queda para estimar una variabilidad después de ajustar los parámetros correspondientes. Para una muestra simple, al calcular $s$ usamos la media de esa misma muestra, y queda un grado de libertad menos que el número de observaciones. No haremos aquí la deducción del divisor: queda fuera del alcance de este curso. En la prueba de una media de esta escena, esos grados de libertad determinan qué distribución t usar. [Hahs-Vaughn §5.2; Otto §2.2]

> **[EJEMPLO]** La unidad independiente es una jornada: se toma una pareja referencia–indicación por jornada en ocho jornadas de un único nivel nominal. Para este ejemplo se suponen errores independientes de una misma población normal, sin deriva ni componente común no modelado. No son ocho lecturas consecutivas. El vector de errores del ejemplo ilustrativo B es $[-0,8;\ 0,1;\ 0,4;\ -0,2;\ 0,7;\ 0,0;\ -0,5;\ 0,6]$ nmol/mol. La media es $0,0375$ nmol/mol y la desviación estándar, $0,5263$ nmol/mol. Esa dispersión no debe confundirse con el error estándar, que el mismo cálculo da como $0,1861$ nmol/mol bajo la hipótesis de observaciones independientes. En el libreto estos datos son **simulados**; no son las lecturas de CALAIRE ni una estimación del desempeño real del Level 2. [Hahs-Vaughn §5.2; §6.1]

Al leer el ejemplo, subrayo que los valores negativos no son «lecturas imposibles» que debamos borrar: son errores con signo en un conjunto de ejemplo. El signo conserva la dirección de la diferencia. La media pequeña no significa que cada error sea pequeño, como muestra la desviación muestral. Y el error estándar no es el rango de futuras lecturas; cuantifica la precisión de la media estimada bajo el muestreo declarado. [Hahs-Vaughn §5.2; §6.1]

### Escena B2. La media tiene una distribución muestral

Para construir el intervalo de la media con t, usamos el error estándar estimado y los grados de libertad de la muestra. En el modelo de observaciones independientes de una población normal, si la media planteada es la verdadera media poblacional, la diferencia entre la media observada y esa media, dividida por el error estándar, sigue una distribución t [Hahs-Vaughn §6.1]. La validez del intervalo depende de que el diseño y los supuestos correspondan a los datos. No confundimos la distribución de referencia t con la forma del histograma de lecturas. Este intervalo describe la inferencia de la media bajo el muestreo declarado; no es el presupuesto completo de incertidumbre de calibración. Una incertidumbre común de la referencia no queda estimada por la dispersión de estos errores ni se reduce al repetir jornadas; si existe, se modela por separado en el presupuesto de incertidumbre, fuera del alcance de este curso.

> **[PIZARRA]** $\displaystyle \bar e\ \pm\ t_{0,975;\,\nu}\,\frac{s}{\sqrt n}$; decimos: «para el noventa y cinco por ciento, la media observada más o menos el cuantil t de 0,975 con $\nu$ grados de libertad, multiplicado por su error estándar».

El intervalo de confianza se construye con un procedimiento que, si se repitiera muchas veces bajo las mismas condiciones, cubriría el parámetro en la proporción establecida por su nivel. Una vez calculado un intervalo particular, no decimos que haya una probabilidad frecuentista de que el parámetro fijo esté dentro de este intervalo concreto. Decimos que el intervalo es compatible con los valores del parámetro que no quedan descartados por esos datos y ese modelo, al nivel elegido. Tampoco afirmamos que el intervalo cubra observaciones futuras: ese sería otro tipo de intervalo. [Hahs-Vaughn §6.1]

Volvamos al ejemplo ilustrativo. Los datos son simulados. Para un intervalo bilateral del noventa y cinco por ciento, con siete grados de libertad, el cuantil t es $2,3646$. El error estándar es $0,1861$ nmol/mol. El intervalo para el error medio queda entre $-0,4025$ y $0,4775$ nmol/mol. Explico cada parte: centro en la media de $0,0375$, semiancho cercano a $0,4400$, y extremos expresados en la misma unidad del error. El intervalo incluye cero, pero por sí solo no prueba que el efecto sea exactamente cero. Más adelante usaremos el contraste para expresar esa conclusión con claridad. [Hahs-Vaughn §6.1]

> **[PREGUNTA AL GRUPO]** Si duplicáramos el número de filas copiando cada lectura, ¿se estrecharía legítimamente el intervalo? — *Respuesta esperada:* no; filas duplicadas no agregan unidades independientes de información. Si se tratan como nuevas réplicas, el error estándar se reduce artificialmente.

Al escoger el intervalo, definimos primero qué respuesta queremos estimar. Para el ejemplo, es el error medio de un solo nivel de concentración bajo una unidad de repetición independiente declarada. Si la pregunta fuera cuánto varía una lectura individual, o cuál será el error en el uso futuro, este intervalo no respondería la pregunta. Tampoco debemos agrupar varios niveles de concentración para ganar tamaño muestral: el error puede cambiar con el nivel, así que mezclar niveles cambia el parámetro que estamos estimando. [Hahs-Vaughn §6.1]

### Escena B3. Contrastar una media sin confundir evidencia con importancia

Un contraste empieza con una pregunta expresada antes de mirar el resultado. La hipótesis nula, $H_0$, representa el valor de referencia contra el que comparamos. Para preguntar si el error medio del nivel de concentración difiere de cero, escribimos $H_0:\mu_e=0$. La alternativa bilateral es $H_1:\mu_e\ne0$ [Hahs-Vaughn §6.1]. Si la decisión técnica solo tuviera sentido en una dirección, la alternativa unilateral tendría que justificarse por el problema antes de analizar los datos; no se escoge después de ver hacia dónde apuntó la media.

> **[PIZARRA]** $t_{obs}=\dfrac{\bar e-\mu_0}{s/\sqrt n}$. Se lee: «la media observada menos la media planteada por la hipótesis nula, dividido por el error estándar». Para una prueba bilateral, comparamos la magnitud del estadístico con los cuantiles de t, o calculamos el valor p bilateral.

El nivel de significación $\alpha$ es la probabilidad máxima, bajo el modelo y si $H_0$ es cierta, de rechazarla mediante la regla que se fijó [Hahs-Vaughn §6.1]. El valor p [Hahs-Vaughn §6.1] es la probabilidad, bajo $H_0$ y los supuestos del contraste, de obtener un estadístico tan extremo o más extremo que el observado. No es la probabilidad de que $H_0$ sea cierta; tampoco mide el tamaño del efecto ni la probabilidad de que el resultado se repita. Un valor p pequeño indica incompatibilidad de los datos con $H_0$ en el marco del modelo, no importancia metrológica automática.

En el ejemplo, el estadístico t vale $0,2015$ y el valor p bilateral es $0,8460$. Con el nivel de significación del cinco por ciento que fijamos de antemano, no rechazamos la hipótesis de media cero. La forma correcta de decirlo es: «los datos no proporcionan evidencia estadística suficiente para concluir que el error medio difiera de cero bajo este modelo». No decimos «se probó que el error es cero». El intervalo incluye cero, de manera coherente con esa conclusión. [Hahs-Vaughn §6.1]

Ahora distingo los errores de decisión. Un error de tipo I consiste en rechazar $H_0$ cuando es cierta; el procedimiento limita su probabilidad nominal mediante $\alpha$, si se cumplen las condiciones. Un error de tipo II consiste en no rechazar $H_0$ cuando una alternativa concreta es cierta. Su probabilidad depende de cuál sea esa alternativa, la dispersión, el diseño y el tamaño muestral. Sin especificar el efecto que importa no queda definida la probabilidad de detectar esa alternativa. La potencia, es decir, la probabilidad de detectar un efecto concreto, la veremos en el nivel I. [Hahs-Vaughn §6.1]

La relevancia metrológica es una pregunta distinta de la significación. Antes de calcular, el responsable puede fijar una magnitud de error que sería importante para el uso, con unidades, signo si procede y justificación técnica. Si el intervalo es ancho y cubre efectos relevantes tanto positivos como negativos, un valor p grande solo nos dice que no distinguimos el efecto de cero con precisión suficiente; no demuestra que el equipo sea adecuado. Si el intervalo es estrecho, puede excluir cero y aun así quedar enteramente dentro de una banda de efecto pequeño que no cambia la decisión de uso. El contraste estadístico no decide por sí mismo la aptitud del instrumento. En nuestro ejemplo, si fijamos de antemano una magnitud relevante de $0,30$ nmol/mol en cualquiera de los dos sentidos, el intervalo del 95 % incluye tanto $-0,30$ como $+0,30$: no descarta efectos de esa magnitud aunque no rechacemos cero. Es un criterio didáctico, no una tolerancia del laboratorio; la equivalencia formal con márgenes definidos queda fuera del alcance de esta sesión. [Hahs-Vaughn §6.1]

> **[ERROR CRÍTICO]** No conviertan «no rechazar cero» en «aceptar que el sesgo es cero» o «demostrar que el error es despreciable». Y no confundan significación estadística con relevancia metrológica: son afirmaciones distintas y requieren criterios distintos.

En el caso del Level 2 frente al SRP 55, lo que estimamos es el intervalo del error medio en un nivel de concentración, y lo contrastamos con cero y con una magnitud relevante. Para cada análisis se debe decir qué resultado se estima, cuál es la unidad de repetición y qué comparación se hará. El ejemplo ilustrativo de esta escena no sustituye ese análisis con el certificado. En la práctica siguiente ustedes aplican el intervalo y el contraste a otro vector simulado. [Hahs-Vaughn §6.1]

### Práctica B — en clase (25 min). Intervalo y contraste del error medio
>
> **Enunciado.** Ustedes reciben ocho pares referencia–indicación, uno por jornada independiente, todos en un mismo nivel nominal. Para este ejercicio, el error de cada jornada ya fue calculado como $e=y-x$; la respuesta de interés es la media del error entre jornadas, no una lectura futura. Los datos son **simulados** mediante un vector fijo declarado en `calc/M04_practicas_luna.py`; no son mediciones ni resultados de CALAIRE. Los errores, en nmol/mol, son $[-0,4; 0,2; 0,1; 0,5; -0,1; 0,3; 0,0; 0,6]$. El modelo supone jornadas independientes, una misma población normal, sin deriva ni componente común omitida. Antes de empezar, dejamos fijada como magnitud didácticamente relevante $0,30$ nmol/mol en cualquiera de los sentidos; no es tolerancia del laboratorio.
>
> **Tareas.** Calculen $n$, media, desviación estándar muestral, error estándar e intervalo bilateral del 95 % con t. Contrasten $H_0:\mu_e=0$ frente a una alternativa bilateral con $\alpha=0,05$ e informen estadístico y valor p. Interpreten por separado el contraste con cero y si el intervalo descarta efectos de magnitud $0,30$ nmol/mol. Indiquen qué harían si las ocho filas fueran lecturas consecutivas de una sola jornada en vez de jornadas independientes.
>
> **Solución docente.** Hay ocho jornadas, por tanto $n=8$ y $\nu=7$. La media es $\bar e=0,1500$ nmol/mol; la desviación muestral es $s=0,3251$ nmol/mol y el error estándar, $s/\sqrt{8}=0,1150$ nmol/mol. Con $t_{0,975;7}=2,3646$, el intervalo es $0,1500\pm2,3646(0,1150)$, es decir, $[-0,1218; 0,4218]$ nmol/mol. La comprobación es que el intervalo está centrado en $0,1500$ y tiene semiancho aproximado $0,2718$.
>
> El estadístico es $t=0,1500/0,1150=1,3049$ y el valor p bilateral es $0,2332$. No rechazamos media cero al 5 %: los datos no muestran evidencia suficiente de diferencia respecto de cero bajo el modelo, pero no prueban que el error sea cero. El intervalo incluye $+0,30$ nmol/mol, aunque excluye $-0,30$; por ello no descarta una magnitud relevante de ese tamaño y no demuestra precisión suficiente respecto de ese criterio. Si fueran lecturas consecutivas de una jornada, no las contaríamos automáticamente como ocho unidades independientes: se detiene la inferencia y se escala para representar dependencia temporal y jornada. La ejecución reproducible y las comprobaciones numéricas están en `calc/M04_practicas_luna.py`.
>
> **Interpretación y decisión operativa.** Este resultado simulado sirve para practicar la inferencia de una media entre jornadas bajo supuestos declarados; no certifica el desempeño del Level 2. Para un análisis real se verificarían emparejamiento, nivel, jornada y trazabilidad del resultado, y el responsable definiría la relevancia metrológica aplicable. Si hay dependencia, deriva, nivel mezclado o intervalo próximo a una regla de uso no suministrada, no se firma la conclusión con esta t simple: se escala al responsable técnico.
>
> **Criterio de logro.** Calcula y reporta media, intervalo, t y valor p con unidades; distingue no rechazo de igualdad y reconoce que el intervalo contiene $+0,30$ pero excluye $-0,30$ nmol/mol, por lo que no descarta magnitudes relevantes en ambos sentidos; identifica el fallo de independencia.

### Señales de escalamiento

Antes de cerrar el nivel básico, les indico cuándo detener el cálculo automático y consultar. Si las observaciones que se van a promediar comparten día, ciclo, deriva o patrón de una forma no recogida en el modelo, no declaren independencia sin justificación. Si al agrupar cambia la escala de concentración o se mezclan niveles con comportamientos distintos, detengan la prueba de una única media. Si hay un dato inusual sin causa identificada, no lo eliminen para hacer que el resultado «pase». Revisen los datos, el gráfico y el registro, y escalen el caso. [Hahs-Vaughn §6.1; §6.4]

También se escala cuando hay pocos grados de libertad para una cobertura confiable, cuando el intervalo queda cerca de un límite que gobierna una decisión, o cuando la relevancia depende de un margen que nadie definió. Pocos grados de libertad no invalidan por sí solos el intervalo o la prueba t si se cumplen sus supuestos; la consulta se requiere si la cobertura o el modelo no están justificados. En esos casos no improvisen otro umbral ni cambien de prueba tras ver el resultado. Soliciten apoyo para definir la unidad experimental, el modelo, la cobertura o la regla de decisión antes de emitir una conclusión. [Hahs-Vaughn §6.1]

## Nivel I — lo que se añade: elegir y justificar métodos

> **[NOTA AL INSTRUCTOR]** Cifras reproducibles con `calc/M04_ejemplos.py`.

En el nivel intermedio conservamos todo lo anterior: estimadores, intervalos, pruebas, supuestos y lectura metrológica. Ahora ustedes eligen entre métodos que corresponden a diseños distintos y justifican por qué las observaciones se consideran independientes o emparejadas. También aprenderán a inferir sobre varianzas, planear potencia, expresar la incertidumbre de una desviación estimada y evaluar ciertos valores extremos solo cuando las condiciones de esas pruebas se cumplen. [Hahs-Vaughn §§6.1, 7.1–7.2, 9.1–9.3; Otto §2.2]

### Escena I1. Pareadas o independientes: la estructura manda

Para comparar dos resultados, primero observen cómo se obtuvieron. Si cada resultado de un equipo tiene una pareja natural del otro equipo tomada bajo la misma condición, y la pareja es la unidad independiente, analizamos las diferencias dentro de cada pareja. La prueba t pareada es una prueba de una media aplicada a esas diferencias. La variación común a los dos miembros de cada pareja queda reflejada en la diferencia, no se trata como si fueran dos grupos sin relación. En el laboratorio, dos instrumentos que miden el mismo gas en secuencia coordinada pueden producir datos pareados si el protocolo, los tiempos y la asignación de las mediciones sostienen ese emparejamiento. No junten concentraciones distintas en una sola prueba t pareada: cada nivel plantea su propio efecto, salvo que un modelo explícito justifique otra pregunta. [Hahs-Vaughn §7.2]

> **[PIZARRA]** Definimos $\Delta_i=A_i-B_i$; reservamos $d$ para el número de días. Después calculamos $t=\bar\Delta/(s_\Delta/\sqrt n)$, con $n-1$ grados de libertad para la prueba de una media de diferencias. La fórmula se lee: «media de las diferencias dividida por su error estándar».

En el ejemplo ilustrativo construimos ocho pares de indicaciones simuladas de un único nivel nominal de concentración; cada par representa una jornada distinta y se suponen diferencias independientes de una misma población normal, sin deriva. La respuesta de interés es la diferencia $A-B$. Obtenemos ocho diferencias, con media $0,1625$ nmol/mol y desviación estándar $0,1188$ nmol/mol. El error estándar es $0,0420$ nmol/mol, y el intervalo bilateral del noventa y cinco por ciento va de $0,0632$ a $0,2618$ nmol/mol. El estadístico es $3,8697$ y el valor p bilateral es $0,0061$. Bajo las hipótesis declaradas, la media de las diferencias es incompatible con cero al nivel del cinco por ciento. No afirmo por ello que cada pareja difiera en la misma cantidad: inferimos la media de las diferencias independientes. **Datos simulados**, no mediciones CALAIRE. [Hahs-Vaughn §7.2]

Ahora supongan que tenemos dos grupos que no forman parejas. Por ejemplo, dos conjuntos de jornadas del mismo nivel nominal de concentración con unidades independientes, sin una correspondencia uno a uno defendible. Si no hay base para asumir varianzas poblacionales iguales, la prueba de Welch compara las medias usando el error estándar que combina la variabilidad estimada en cada grupo y calcula grados de libertad aproximados. No debemos fabricar parejas por el orden de las filas, ni asumir varianzas iguales solo porque las desviaciones muestrales se ven parecidas. [Hahs-Vaughn §§7.3.1 y 7.5.3]

> **[PIZARRA]** $SE(\bar X_1-\bar X_2)=\sqrt{s_1^2/n_1+s_2^2/n_2}$; $\displaystyle\nu_W=\frac{(s_1^2/n_1+s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1)+(s_2^2/n_2)^2/(n_2-1)}$.

El error estándar es la raíz de la suma de las varianzas estimadas de las medias. Los grados de libertad son el cuadrado de esa suma, dividido por la suma de cada varianza de media al cuadrado sobre sus grados de libertad. Usamos $t=(\bar X_1-\bar X_2-\Delta_0)/SE$, que se lee diferencia observada menos diferencia nula, dividida por su error estándar; el intervalo es la diferencia observada más o menos $t_{0,975;\nu_W}SE$. Conservamos los grados de libertad fraccionarios al calcular cuantiles. La deducción queda fuera del alcance de este curso; aquí nos ocupa la regla operativa. [Hahs-Vaughn §§7.3.1 y 7.5.3]

En el ejemplo ilustrativo de dos grupos independientes de un mismo nivel nominal de concentración, cada observación representa una jornada distinta. Suponemos normalidad dentro de cada grupo e independencia dentro y entre grupos, sin fuentes comunes omitidas. El primero tiene seis observaciones y el segundo siete. Sus medias son $10,0167$ y $10,9571$ nmol/mol. La diferencia estimada, grupo primero menos grupo segundo, es $-0,9405$ nmol/mol. Welch produce un error estándar de $0,1531$, aproximadamente $10,9272$ grados de libertad, estadístico $-6,1418$ y valor p bilateral $0,000075$. El intervalo del noventa y cinco por ciento para la diferencia es de $-1,2778$ a $-0,6032$ nmol/mol. El signo negativo expresa que la media del primer grupo es menor en este orden de resta. Cambiar el orden invierte el signo, pero no la conclusión bilateral. **Datos simulados**. [Hahs-Vaughn §§7.3.1 y 7.5.3]

Para escoger, pregunto: ¿hay una relación de pareja establecida por el diseño, o hay dos muestras independientes? Si hay una correspondencia real, se analiza la diferencia; si no, no se fuerza el emparejamiento. Para Welch se justifica independencia entre grupos y dentro de cada grupo, se revisa la forma de las distribuciones y se informa que la inferencia es sobre la diferencia de medias. Si el conjunto contiene mediciones repetidas de un mismo día, lote o nivel, la independencia puede no cumplirse y el problema se escala a un modelo que represente esa agrupación. [Hahs-Vaughn §§7.1–7.2]

> **[ERROR CRÍTICO]** No traten mediciones correlacionadas como dos muestras independientes por comodidad. Tampoco conviertan ocho lecturas consecutivas en ocho parejas o réplicas independientes si el diseño no sostiene esa unidad de repetición.

### Escena I2. Inferir sobre la variabilidad

Una pregunta sobre la media no responde si la dispersión cambió. Si asumimos observaciones independientes de una población normal, la distribución chi-cuadrado permite construir un intervalo de confianza para la varianza de una población y contrastar una varianza propuesta. El estadístico es el producto de los grados de libertad por la varianza muestral, dividido por la varianza que plantea la hipótesis; se llama chi-cuadrado. Como la distribución chi-cuadrado no es simétrica, los límites inferior y superior usan cuantiles distintos. [Hahs-Vaughn §§9.1–9.2]

> **[PIZARRA]** Bajo $H_0:\sigma^2=\sigma_0^2$, el estadístico es $\chi^2=(n-1)s^2/\sigma_0^2$. El intervalo bilateral del 95 % para $\sigma^2$ es $[\nu s^2/\chi^2_{0,975;\nu};\ \nu s^2/\chi^2_{0,025;\nu}]$, con $\nu=n-1$. Decimos: «dividimos la suma de cuadrados por el cuantil alto para el límite inferior, y por el cuantil bajo para el superior». El pivote antes de fijar la hipótesis contiene la varianza poblacional desconocida $\sigma^2$, no un valor nulo supuesto. [Hahs-Vaughn §9.1]

Usamos la varianza de la muestra del ejemplo ilustrativo de B, con datos simulados, no como evidencia de una calibración. La varianza muestral es $0,2770$ $(\mathrm{nmol/mol})^2$, con siete grados de libertad. El intervalo bilateral del noventa y cinco por ciento para la varianza poblacional va de $0,1211$ a $1,1473$ $(\mathrm{nmol/mol})^2$. Si la hipótesis nula propone una varianza de $0,25$ $(\mathrm{nmol/mol})^2$, el estadístico es $7,7550$ y el valor p bilateral es $0,7094$. No rechazamos esa varianza propuesta. El intervalo ancho recuerda que la muestra pequeña proporciona poca precisión sobre la dispersión. [Hahs-Vaughn §§9.1–9.2]

Para comparar dos varianzas de poblaciones normales independientes, el cociente de varianzas muestrales se compara con una distribución F, con grados de libertad de ambos grupos. El orden del cociente importa para los límites del intervalo, aunque la prueba bilateral contra igualdad se puede expresar de forma coherente usando las dos colas. Esta prueba es sensible a desviaciones de la normalidad; no la presentamos como un detector universal de cambios de dispersión. [Hahs-Vaughn §§9.1–9.2]

> **[PIZARRA]** Si $R=s_1^2/s_2^2$ y $\nu_1=n_1-1$, $\nu_2=n_2-1$, el intervalo del 95 % para $\sigma_1^2/\sigma_2^2$ es $[R/F_{0,975;\nu_1,\nu_2};\ R/F_{0,025;\nu_1,\nu_2}]$. «El cociente observado se divide por el cuantil alto para el límite inferior y por el bajo para el superior». Para probar igualdad usamos $F=R$, con esos dos grados de libertad. En las pruebas bilaterales de varianza y de razón usamos colas iguales: el valor p es dos veces la menor probabilidad de cola, acotado a uno. [Hahs-Vaughn §§9.1–9.2]

En los dos grupos del ejemplo ilustrativo de la escena anterior, con datos simulados, el cociente de varianzas muestrales, grupo primero sobre grupo segundo, es $0,8408$. El intervalo bilateral del noventa y cinco por ciento para el cociente va de $0,1404$ a $5,8669$. El valor p de la prueba bilateral de igualdad es $0,8678$. La conclusión no es «las varianzas son idénticas», sino que estos datos no distinguen la razón de uno con precisión suficiente. El intervalo permite ver cuán amplia es la incertidumbre. **Datos simulados**. [Hahs-Vaughn §§9.1–9.2]

> **[ERROR CRÍTICO]** No apliquen chi-cuadrado o F a datos con dependencia, grupos mezclados o una distribución claramente incompatible con la normalidad, como si el cálculo corrigiera el diseño. Revisen primero la unidad de repetición y los supuestos.

### Escena I3. Potencia y tamaño de muestra dependen del diseño

La potencia es la probabilidad de detectar un efecto concreto: $1-\beta$. Antes de calcularla fijamos el efecto mínimo $\delta$ de interés, la dispersión prevista, el nivel $\alpha$, si la prueba será bilateral y la estructura de las réplicas. Un efecto menor o una dispersión mayor suele exigir más información. La potencia depende de si estimamos una media, diferencias pareadas o dos grupos independientes. Para una media usamos $\sigma$; para parejas, la desviación de las diferencias $\sigma_\Delta$; para dos grupos iguales con varianza común, $\sigma_{común}$. La unidad de muestra debe ser la unidad independiente del diseño, no el número de filas. [Hahs-Vaughn §§6.1.2–6.1.5; 7.1.4–7.1.7; 7.2.2–7.2.4]

> **[PIZARRA]** Efecto estandarizado: $d_C=\delta/\sigma$ para una media; $d_C=\delta/\sigma_\Delta$ para parejas; $d_C=\delta/\sigma_{común}$ para dos grupos. Aproximación normal bilateral: $n\approx[(z_{1-\alpha/2}+z_{1-\beta})/d_C]^2$ para media o parejas, y $n_g\approx2[(z_{1-\alpha/2}+z_{1-\beta})/d_C]^2$ por grupo.

Dividimos el efecto relevante por la desviación pertinente al diseño. Con $\alpha=0,05$, potencia objetivo $0,80$ y $d_C=0,5$, la aproximación normal da unas 31,4 unidades o parejas; con $d_C=0,8$ da 24,5 observaciones por grupo. Son aproximaciones iniciales. Para planificar con muestras pequeñas se usa la distribución t no central y se redondea el tamaño continuo hacia arriba; en una media o parejas los grados de libertad son $n-1$, y en dos grupos iguales, $2n_g-2$. El cálculo de dos grupos supone varianza común y no representa la potencia exacta de Welch. [Hahs-Vaughn §§6.5, 7.8]

> **[EJEMPLO]** En escenarios bilaterales con $\alpha=0,05$ y potencia objetivo $0,80$, para una media o diferencias pareadas con $d_C=0,5$ se requieren aproximadamente $33,37$ unidades o parejas; se planifica con 34. Con 16, la potencia es $0,4649$. Para dos grupos independientes iguales, con varianza común y $d_C=0,8$, hacen falta $25,52$ por grupo, es decir, 26; con 12 por grupo la potencia es $0,4658$. Son escenarios simulados, no recomendaciones para CALAIRE. [Hahs-Vaughn §§6.1.2–6.1.5; 7.1.4–7.1.7; 7.2.2–7.2.3]

En parejas contamos pares independientes, no sus dos miembros; en dos grupos contamos unidades por grupo. Si hay jornadas, ciclos o analistas, definan qué unidad puede variar independientemente. La dispersión prevista debe apoyarse en información previa y el cálculo no autoriza a ignorar otros niveles del diseño. [Hahs-Vaughn §§6.1.2–6.1.5, 7.1.4–7.1.7, 7.2.2–7.2.3]

### Escena I4. Incertidumbre de una desviación estimada

La desviación estándar muestral también tiene incertidumbre. Bajo normalidad e independencia, una aproximación para la incertidumbre estándar de $s$ es $u(s)\approx s/\sqrt{2\nu}$, con $\nu=n-1$. No es el error estándar de la media $s/\sqrt n$ ni sustituye el intervalo de la varianza basado en chi-cuadrado. [GUM §4.3.2, nota, y §E.4.3, ecuación (E.7)]

> **[PIZARRA]** $u(s)\approx s/\sqrt{2\nu}$. Se lee: «la incertidumbre estándar aproximada de la desviación es la desviación estimada dividida por la raíz de dos veces sus grados de libertad».

En la muestra ilustrativa B, $s=0,5263$ nmol/mol y $\nu=7$, así que $u(s)=0,1407$ nmol/mol. La incertidumbre es apreciable frente a la estimación: no reportamos la dispersión de una muestra pequeña como constante exacta ni conservamos decimales injustificados. Esta aproximación vale bajo las condiciones indicadas. [GUM §4.3.2, nota, y §E.4.3, ecuación (E.7)]

### Escena I5. Grubbs y Dixon: pruebas acotadas, nunca una licencia para borrar

Una observación extrema es inusual en relación con un modelo, pero la apariencia extrema no basta para descartarla. Antes de cualquier prueba buscamos causas documentadas: transcripción, estabilización, purga, condición instrumental o cambio de procedimiento. Grubbs y Dixon están diseñadas para situaciones específicas de una muestra aproximadamente normal y para investigar un extremo bajo sus condiciones. No reemplazan el análisis de residuos ni justifican probar repetidamente varios datos hasta obtener una exclusión. [Otto §2.2]

La prueba de Grubbs compara la distancia del valor sospechoso a la media con la desviación estándar de la muestra. La prueba de Dixon ordena los datos y compara un hueco en un extremo con un rango definido. No son intercambiables en cualquier tamaño de muestra, ni responden a la pregunta de si una observación es «incorrecta». El investigador declara qué extremo se prueba, el nivel de significación, el tamaño muestral y la tabla o procedimiento crítico aplicable. Si más de un valor parece extremo, el modelo de prueba simple puede dejar de ser válido. [Otto §2.2]

> **[EJEMPLO]** Para ilustrar la mecánica, construimos el vector fijo **simulado** $[0,02;\ 0,04;\ 0,01;\ 0,03;\ 0,00;\ 0,05;\ 0,02;\ 0,28]$ nmol/mol. Cada valor representa una jornada distinta de un mismo nivel nominal. Bajo la hipótesis de ausencia de atípico suponemos observaciones independientes de una misma población normal. Declaramos antes del contraste que investigamos un único extremo alto; no elegimos después entre ambas colas. En Grubbs usamos $G=(x_{\max}-\bar x)/s$: «la distancia del máximo a la media dividida por la desviación muestral». Obtenemos $2,4374$, mayor que $2,22$ de la tabla 2.11 de Otto para ocho observaciones y $1-\alpha=0,99$, es decir, $\alpha=0,01$. Ese crítico corresponde a la convención unilateral; si buscamos el extremo en cualquiera de las dos colas al mismo riesgo total, el crítico calculado sería aproximadamente $2,2744$. Para Dixon usamos la variante hueco/rango $Q=(x_{(n)}-x_{(n-1)})/(x_{(n)}-x_{(1)})$: «el hueco superior dividido por el rango completo». Da $0,8214$, mayor que $0,59$ de la tabla 2.10 para ese tamaño y $1-\alpha=0,99$. Bajo las condiciones de normalidad y prueba de un extremo declarado, ambos resultados señalan el extremo como inusual. El ejemplo no autoriza su eliminación: se investiga y documenta la causa y se reporta la decisión con el dato conservado o la exclusión justificada. **Datos simulados**. [Otto §2.2]

El valor crítico de Dixon $0,59$ está verificado en Otto, tabla 2.10: $Q(0,99;n=8)$ para $Q_1$ y $Q_n$; aquí se usa $Q_n$, el hueco superior dividido por el rango. El script de práctica también suministra $0,59$ explícitamente. Si la muestra está agrupada, tiene dependencia temporal, contiene más de un extremo sospechoso o la normalidad no es defendible, no apliquen esa conclusión mecánicamente. La prueba no convierte una estructura compleja en una muestra simple. [Otto §2.2]

> **[ERROR CRÍTICO]** Nunca eliminen un resultado solo porque una prueba lo marcó o porque al quitarlo mejora el ajuste. Debe existir una causa técnica documentada y una regla de tratamiento definida; conserven el dato original y expliquen el análisis realizado.

### Práctica I — en clase (15 min). Seleccionar métodos y comenzar

**Enunciado.** En clase trabajen los dos diseños de comparación. Todos los datos son simulados y reproducibles en `calc/M04_practicas_luna.py`, no son resultados de CALAIRE. Primero, ocho pares independientes por jornada en un mismo nivel: A $[0,1; 0,4; -0,2; 0,5; 0,3; -0,1; 0,6; 0,2]$ y B $[-0,1; 0,2; -0,1; 0,1; 0,0; -0,3; 0,2; 0,0]$ nmol/mol. Segundo, dos grupos sin emparejamiento, una jornada por dato: A $[9,6; 10,0; 10,3; 9,8; 10,5; 9,9]$ y B $[10,4; 11,0; 10,7; 11,5; 10,8; 11,3; 10,6]$ nmol/mol. Se supone independencia y normalidad aproximada.

**Tareas.** Declaren la unidad, seleccionen t pareada o Welch y expliquen por qué no se empareja el segundo conjunto por orden de filas. En clase calculen las diferencias pareadas, su media y error estándar, y escriban hipótesis y supuestos para ambos análisis.

**Solución docente — en clase.** La unidad del primer caso es la pareja/jornada. Las diferencias A−B son $[0,2; 0,2; -0,1; 0,4; 0,3; 0,2; 0,4; 0,2]$ nmol/mol, media $0,2250$, desviación $0,1581$ y error estándar $0,0559$ nmol/mol. El segundo caso son grupos independientes, por lo que se prepara Welch, no una t pareada fabricada.

### Práctica I — tarea. Completar análisis y evaluar extremos

**Enunciado.** Completen estadístico, grados de libertad, valor p e intervalo bilateral del 95 % para ambos diseños vistos en clase. Usen la muestra B de la práctica B para inferir sobre una varianza frente a $0,25\ (\mathrm{nmol/mol})^2$ y la razón de varianzas de los grupos independientes. Planifiquen pruebas bilaterales con $\alpha=0,05$ y potencia $0,80$: una media con $\delta=0,30$ y $\sigma=0,60$; parejas con $\delta=0,30$ y $\sigma_\Delta=0,60$; dos grupos iguales con diferencia $0,30$ y desviación común $0,60$ nmol/mol. Estimen $u(s)$ para la muestra B. Finalmente evalúen ocho jornadas $[0,01; 0,05; 0,02; 0,04; 0,03; 0,00; 0,06; 0,18]$ nmol/mol mediante Grubbs para un único extremo alto declarado antes del análisis y Dixon con $Q=(x_{(n)}-x_{(n-1)})/(x_{(n)}-x_{(1)})$. Para Dixon se suministra $Q_{crit}=0,59$ como crítico didáctico de la variante hueco superior/rango completo; no se le atribuye nivel nominal ni garantía de error. No es criterio normativo. No borren observaciones por el resultado de una prueba.

**Solución docente — tarea.** Para la t pareada, con 7 grados de libertad, $t=4,0249$, $p=0,0050$ e IC95 % $[0,0928; 0,3572]$ nmol/mol. Welch estima medias $10,0167$ y $10,9000$; A−B es $-0,8833$, error estándar $0,2005$, $\nu_W=11$, $t=-4,4066$, $p=0,0011$ e IC95 % $[-1,3245; -0,4421]$ nmol/mol.

La muestra B tiene $s^2=0,1057$ $(\mathrm{nmol/mol})^2$, 7 grados de libertad e IC95 % para $\sigma^2$ $[0,0462;0,4379]$. Frente a $H_0:\sigma^2=0,25$, $\chi^2=2,9600$, $p=0,2226$. Para F, $s_A^2/s_B^2=0,7152$, grados $(5,6)$, IC95 % $[0,1195;4,9906]$ y $p=0,7302$. Estos no rechazos no demuestran igualdad.

Para media y parejas, $d_C=0,5$: se requieren $33,37$, redondeado a 34; con 16 la potencia es $0,4649$. Para grupos iguales, $d_C=0,5$: se requieren $63,77$ por grupo, redondeado a 64; con 12 por grupo la potencia es $0,2161$. Se cuentan unidades independientes o parejas, no filas correlacionadas. Con $s=0,3251$ y $\nu=7$, $u(s)\approx0,0869$ nmol/mol. En el vector extremo, $G=2,3157$, superior al crítico unilateral de Grubbs $2,2208$ para $n=8$, $\alpha=0,01$; $Q=0,6667$, mayor que el crítico didáctico suministrado $0,59$. Esta comparación de Dixon no declara nivel nominal. Ambos resultados motivan investigar y documentar la causa, conservando el dato original. Los cálculos se reproducen en `calc/M04_practicas_luna.py`.

**Interpretación y decisión operativa.** Si hay dependencia, agrupamiento, normalidad dudosa, más de un extremo sospechoso o diseño ambiguo, detengan el análisis y escalen. Ninguna prueba por sí sola autoriza a borrar datos.

**Criterio de logro.** Selecciona la prueba según el diseño, informa estimaciones y supuestos, distingue no rechazo de igualdad y trata extremos como señales investigativas, no como permiso de exclusión.

## Cierre del capítulo

Cierro recordando la secuencia de decisiones. En B definimos el parámetro y la unidad independiente, calculamos una media con su intervalo t y contrastamos la hipótesis sin confundir falta de rechazo con igualdad ni significación con importancia metrológica. En I elegimos la prueba que corresponde al diseño: pareada si hay parejas reales, Welch si comparamos grupos independientes sin imponer varianzas iguales; inferimos sobre varianzas solo con las condiciones que sostienen chi-cuadrado y F, planificamos potencia según el efecto y el diseño, y tratamos las pruebas de valores extremos como herramientas limitadas, nunca como permiso para borrar datos. [Hahs-Vaughn §§5.2, 6.1, 7.1–7.2, 9.1–9.3; Otto §2.2]

La conclusión de cualquier análisis debe decir qué parámetro se estimó, con qué intervalo o contraste, bajo qué supuestos, qué unidad de repetición se usó y qué significa el resultado para la pregunta estadística. Si falta una de esas piezas, detengan el cierre y pidan revisión. El siguiente módulo, M05, parte de esta inferencia para planear diseños: decidir qué se va a variar, dónde se necesitan réplicas independientes y qué efectos podrán estimarse. [Hahs-Vaughn §6.1; §7.1]

## Referencias del capítulo

- **Hahs-Vaughn.** Hahs-Vaughn, D. L. y Lomax, R. G. *Statistical Concepts: A First Course*, 4.ª ed., Routledge, 2020. `../Curso_COMPLETO/docs/Statistical Concepts – A First Course.pdf`; extractos `../Curso_COMPLETO/docs/statistical_concepts_c05.pdf` a `../Curso_COMPLETO/docs/statistical_concepts_c09.pdf`. Secciones utilizadas: §5.2; §6.1; §§6.4–6.5; §§7.1–7.2, 7.3.1 y 7.5.3 (Welch); §7.8; §§9.1–9.3.
- **statsmodels.** Equipo de desarrollo de statsmodels, *Statistical Power Analysis*, documentación de las clases `statsmodels.stats.power.TTestPower` y `TTestIndPower`, métodos `power` y `solve_power`. https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations (no disponible en `../Curso_COMPLETO/docs/`). Ejecución documentada en `calc/M04_ejemplos.py` con statsmodels 0.15.0, contrastada con `scipy.stats.nct`; comprobación reproducible en el entorno instalado, no auditoría independiente de la documentación web.
- **GUM.** JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, §4.3.2, nota, y §E.4.3, ecuación (E.7). `../Curso_COMPLETO/docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **Otto, M.** *Chemometrics: Statistics and Computer Application in Analytical Chemistry*, 3.ª ed., Wiley-VCH, 2017. §2.2, pruebas estadísticas y pruebas de valores atípicos. Archivo: `../Curso_COMPLETO/docs/Chemometrics Statistics and Computer Application.pdf`.
