# M04. Inferencia: estimación y contraste

## Sesión 3 (120 min)

| Bloque | Minutos |
|---|---:|
| Revisión de la tarea de la sesión anterior | 15 |
| Narración B + I | 45 |
| Práctica B — en clase | 25 |
| Práctica I — en clase | 15 |
| Preguntas y cierre | 20 |
| **Total** | **120** |

La narración prevista suma aproximadamente **1668 palabras en B** (12,8 min) y **467 palabras en I** (3,6 min) a 130 palabras/min; el bloque B+I ocupa 45 min e incluye práctica guiada, pausas, pizarra y transiciones.

## Revisión de la tarea de la sesión anterior (15 min)

**Guion de revisión de la práctica I de M03.** Retomen la comparación de dos resultados con covarianza por patrón compartido. Pidan que identifiquen las incertidumbres estándar, la correlación declarada y la incertidumbre de la diferencia con y sin dependencia; expliquen por qué la covarianza cambia la incertidumbre combinada. Cierren preguntando qué fuente común habría que documentar en un caso real.

## Ficha del capítulo

| Elemento | Alcance |
|---|---|
| Competencia estadística | Estimar un efecto con su intervalo y contrastar hipótesis, distinguiendo significación estadística de relevancia metrológica. |
| Prerrequisitos | M2: descripción, dispersión y elección de la respuesta. M3-B: distribución t, cuantiles y grados de libertad. M3-I: covarianza, chi-cuadrado y F. |
| Nivel B | Grados de libertad; intervalo de confianza con t; hipótesis, valor p y errores de decisión; prueba t de un error medio en un nivel, con la unidad de repetición justificada en el enunciado. |
| Nivel I añade | t pareada y Welch; intervalos y pruebas sobre varianzas (chi-cuadrado, F); potencia y tamaño de muestra según el diseño (media, pareadas, dos grupos); incertidumbre de una desviación estimada; pruebas de Grubbs y Dixon solo bajo sus condiciones de aplicación. |
| Datos de ejemplos | **Simulados** y generados por `calc/M04_ejemplos.py`; ilustran cálculos y no describen resultados de CALAIRE. El certificado F-PSMT-01, Level 2 Thermo 49C frente al SRP 55, aporta el contexto del caso, no datos atribuibles a los ejemplos. |
| Anexos | Las deducciones del divisor de la varianza muestral y de Welch–Satterthwaite quedan fuera del alcance de este curso. |
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

Los grados de libertad expresan cuánta información independiente queda para estimar una variabilidad después de ajustar los parámetros correspondientes. Para una muestra simple, al calcular $s$ usamos la media de esa misma muestra, y queda un grado de libertad menos que el número de observaciones. La deducción del divisor queda fuera del alcance de este curso. En la prueba de una media de esta escena, esos grados de libertad determinan qué distribución t usar. [Hahs-Vaughn §5.2; Otto §2.2]

> **[EJEMPLO]** La unidad independiente es una jornada: se toma una pareja referencia–indicación por jornada en ocho jornadas de un único nivel nominal. Para este ejemplo se suponen errores independientes de una misma población normal, sin deriva ni componente común no modelado. No son ocho lecturas consecutivas. El vector de errores del ejemplo ilustrativo B es $[-0,8;\ 0,1;\ 0,4;\ -0,2;\ 0,7;\ 0,0;\ -0,5;\ 0,6]$ nmol/mol. La media es $0,0375$ nmol/mol y la desviación estándar, $0,5263$ nmol/mol. Esa dispersión no debe confundirse con el error estándar, que el mismo cálculo da como $0,1861$ nmol/mol bajo la hipótesis de observaciones independientes. En el libreto estos datos son **simulados**; no son las lecturas de CALAIRE ni una estimación del desempeño real del Level 2. [Hahs-Vaughn §5.2; §6.1]

Al leer el ejemplo, subrayo que los valores negativos no son «lecturas imposibles» que debamos borrar: son errores con signo en un conjunto de ejemplo. El signo conserva la dirección de la diferencia. La media pequeña no significa que cada error sea pequeño, como muestra la desviación muestral. Y el error estándar no es el rango de futuras lecturas; cuantifica la precisión de la media estimada bajo el muestreo declarado. [Hahs-Vaughn §5.2; §6.1]

### Escena B2. La media tiene una distribución muestral

Para construir el intervalo de la media con t, usamos el error estándar estimado y los grados de libertad de la muestra. En el modelo de observaciones independientes de una población normal, si la media planteada es la verdadera media poblacional, la diferencia entre la media observada y esa media, dividida por el error estándar, sigue una distribución t [Hahs-Vaughn §6.1]. La validez del intervalo depende de que el diseño y los supuestos correspondan a los datos. No confundimos la distribución de referencia t con la forma del histograma de lecturas. Este intervalo describe la inferencia de la media bajo el muestreo declarado; no es el presupuesto completo de incertidumbre de calibración. Una incertidumbre común de la referencia no queda estimada por la dispersión de estos errores ni se reduce al repetir jornadas; si existe, requiere un modelo separado, fuera del alcance de este curso.

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

La relevancia metrológica es una pregunta distinta de la significación. Antes de calcular, el responsable puede fijar una magnitud de error que sería importante para el uso, con unidades, signo si procede y justificación técnica. Si el intervalo es ancho y cubre efectos relevantes tanto positivos como negativos, un valor p grande solo nos dice que no distinguimos el efecto de cero con precisión suficiente; no demuestra que el equipo sea adecuado. Si el intervalo es estrecho, puede excluir cero y aun así quedar enteramente dentro de una banda de efecto pequeño que no cambia la decisión de uso. El contraste estadístico no decide por sí mismo la aptitud del instrumento. En nuestro ejemplo, si fijamos de antemano una magnitud relevante de $0,30$ nmol/mol en cualquiera de los dos sentidos, el intervalo del 95 % incluye tanto $-0,30$ como $+0,30$: no descarta efectos de esa magnitud aunque no rechacemos cero. Es un criterio didáctico, no una tolerancia del laboratorio. [Hahs-Vaughn §6.1]

> **[ERROR CRÍTICO]** No conviertan «no rechazar cero» en «aceptar que el sesgo es cero» o «demostrar que el error es despreciable». Y no confundan significación estadística con relevancia metrológica: son afirmaciones distintas y requieren criterios distintos.

En el caso del Level 2 frente al SRP 55, estimamos el intervalo del error medio en un nivel y lo contrastamos con cero y con una magnitud relevante. Declaramos la unidad de repetición y la comparación; el ejemplo simulado no sustituye el análisis del certificado. [Hahs-Vaughn §6.1]

> **[PRÁCTICA B — en clase (25 min)]** Intervalo y contraste del error medio del Level 2 en un nivel
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

Elegimos métodos según el diseño, inferimos sobre varianzas, planeamos potencia y evaluamos valores extremos solo bajo sus condiciones. [Hahs-Vaughn §§6.1, 7.1–7.2, 9.1–9.3; Otto §2.2]

### Escena I1. Pareadas o independientes: la estructura manda

Si cada resultado de un equipo tiene una pareja natural del otro tomada bajo la misma condición, y la pareja es la unidad independiente, analizamos las diferencias. La prueba t pareada es una prueba de una media aplicada a ellas. No fabriquen parejas por el orden de las filas. Para grupos sin emparejamiento y sin base para suponer varianzas iguales, Welch compara las medias usando la variabilidad de cada grupo y grados de libertad aproximados. [Hahs-Vaughn §§7.1–7.2, 7.3.1 y 7.5.3]

> **[PIZARRA]** $\Delta_i=A_i-B_i$; $t=\bar\Delta/(s_\Delta/\sqrt n)$. Para Welch, $SE=\sqrt{s_1^2/n_1+s_2^2/n_2}$; se conservan grados de libertad fraccionarios.

En el ejemplo pareado simulado, ocho jornadas independientes dan media de diferencias $0,1625$ nmol/mol, IC95 % $[0,0632; 0,2618]$, $t=3,8697$ y $p=0,0061$. Para los grupos independientes simulados, Welch estima A−B $=-0,9405$ nmol/mol, IC95 % $[-1,2778; -0,6032]$, $t=-6,1418$ y $p=0,000075$. Inferimos sobre medias, no sobre cada lectura. Si hay agrupamiento por día o nivel, escalen a un modelo apropiado. [Hahs-Vaughn §§7.1–7.2, 7.3.1 y 7.5.3]

### Escena I2. Inferir sobre la variabilidad

Bajo normalidad e independencia, chi-cuadrado permite intervalos y pruebas de una varianza; F permite comparar dos varianzas de poblaciones normales independientes. Son métodos sensibles a desviaciones de normalidad. Un no rechazo no demuestra igualdad. [Hahs-Vaughn §§9.1–9.2]

> **[PIZARRA]** $\chi^2=(n-1)s^2/\sigma_0^2$; para dos muestras, $F=s_1^2/s_2^2$.

En el ejemplo simulado B, $s^2=0,2770$ $(\mathrm{nmol/mol})^2$ y el IC95 % para la varianza poblacional es $[0,1211; 1,1473]$. En los grupos simulados, la razón de varianzas es $0,8408$, IC95 % $[0,1404; 5,8669]$ y $p=0,8678$: los datos no distinguen la razón de uno con precisión suficiente. [Hahs-Vaughn §§9.1–9.2]

### Escenas I3 e I4. Potencia y precisión de la dispersión

Para planificar fijamos efecto mínimo, nivel de significación, potencia y dispersión según el diseño. La réplica es la unidad independiente: en parejas se cuentan parejas, en dos grupos unidades por grupo. Con aproximación t no central, el ejemplo didáctico con $d_C=0,5$ requiere 34 unidades para media o parejas; con $d_C=0,8$, requiere 26 por grupo. Son resultados condicionales, no recomendaciones de campaña. [Hahs-Vaughn §§6.1.2–6.1.5, 7.1.4–7.1.7 y 7.2.2–7.2.4]

La desviación muestral también tiene incertidumbre. Una aproximación bajo normalidad es $u(s)\approx s/\sqrt{2\nu}$; no es el error estándar de la media ni sustituye el intervalo chi-cuadrado. Para el ejemplo B, $u(s)=0,1407$ nmol/mol. [GUM §4.3.2, nota, y §E.4.3, ecuación (E.7)]

### Escena I5. Grubbs y Dixon: pruebas acotadas

Grubbs y Dixon ayudan a investigar un extremo bajo condiciones específicas de una muestra independiente aproximadamente normal; no deciden por sí solas la exclusión. Declaren previamente el extremo y nivel, busquen una causa técnica y conserven el dato original. En el vector simulado de ocho jornadas, Grubbs da $G=2,4374$, superior al crítico unilateral $2,22$ para $\alpha=0,01$; Dixon da $Q=0,8214$, superior al valor tabulado indicado para el ejemplo. El resultado inicia una investigación, no autoriza borrar. Si hay dependencia, varios extremos o normalidad no defendible, no apliquen mecánicamente estas pruebas. [Otto §2.2]

> **[ERROR CRÍTICO]** Nunca eliminen un resultado solo porque una prueba lo marcó o porque al quitarlo mejora el ajuste. Documenten causa técnica y regla de tratamiento. [Otto §2.2]

## Cierre del capítulo

Cierro recordando la secuencia de decisiones. En B definimos el parámetro y la unidad independiente, calculamos una media con su intervalo t y contrastamos la hipótesis sin confundir falta de rechazo con igualdad ni significación con importancia metrológica. En I elegimos la prueba que corresponde al diseño: pareada si hay parejas reales, Welch si comparamos grupos independientes sin imponer varianzas iguales; inferimos sobre varianzas solo con las condiciones que sostienen chi-cuadrado y F, planificamos potencia según el efecto y el diseño, y tratamos las pruebas de valores extremos como herramientas limitadas, nunca como permiso para borrar datos. [Hahs-Vaughn §§5.2, 6.1, 7.1–7.2, 9.1–9.3; Otto §2.2]

La conclusión de cualquier análisis debe decir qué parámetro se estimó, con qué intervalo o contraste, bajo qué supuestos, qué unidad de repetición se usó y qué significa el resultado para la pregunta estadística. Si falta una de esas piezas, detengan el cierre y pidan revisión. El siguiente módulo, M05, parte de esta inferencia para planear diseños: decidir qué se va a variar, dónde se necesitan réplicas independientes y qué efectos podrán estimarse. [Hahs-Vaughn §6.1; §7.1]

## Referencias del capítulo

- **Hahs-Vaughn.** Hahs-Vaughn, D. L. y Lomax, R. G. *Statistical Concepts: A First Course*, 4.ª ed., Routledge, 2020. `../Curso_COMPLETO/docs/Statistical Concepts – A First Course.pdf`; extractos `../Curso_COMPLETO/docs/statistical_concepts_c05.pdf` a `../Curso_COMPLETO/docs/statistical_concepts_c09.pdf`. Secciones utilizadas: §5.2; §6.1; §§6.4–6.5; §§7.1–7.2, 7.3.1 y 7.5.3 (Welch); §§9.1–9.3.
- **statsmodels.** Equipo de desarrollo de statsmodels, *Statistical Power Analysis*, documentación de las clases `statsmodels.stats.power.TTestPower` y `TTestIndPower`, métodos `power` y `solve_power`. https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations (no disponible en `docs/`). Ejecución documentada en `calc/M04_ejemplos.py` con statsmodels 0.15.0, contrastada con `scipy.stats.nct`; comprobación reproducible en el entorno instalado, no auditoría independiente de la documentación web.
- **GUM.** JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, §4.3.2, nota, y §E.4.3, ecuación (E.7). `../Curso_COMPLETO/docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **Otto, M.** *Chemometrics: Statistics and Computer Application in Analytical Chemistry*, 3.ª ed., Wiley-VCH, 2017. §2.2, pruebas estadísticas y pruebas de valores atípicos. Archivo: `../Curso_COMPLETO/docs/Chemometrics Statistics and Computer Application.pdf`.
- Las deducciones del divisor $n-1$ y de Welch–Satterthwaite quedan fuera del alcance de este curso.
