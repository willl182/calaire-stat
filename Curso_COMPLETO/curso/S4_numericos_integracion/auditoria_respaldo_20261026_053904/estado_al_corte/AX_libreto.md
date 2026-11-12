# AX. Anexos de deducciones

## Ficha del capítulo

| Campo | Contenido |
|---|---|
| Competencia estadística | Seguir y justificar las deducciones que sostienen los resultados estadísticos usados en M0–M13, distinguiendo sus supuestos y alcance. |
| Prerrequisitos | Álgebra, esperanza y varianza, derivadas, distribuciones normal, t, chi-cuadrado y F; matrices y cálculo numérico en las secciones avanzadas. |
| Contenido | AX.1–AX.13 según `guia_libreto.md` §7; incluye deducciones y desarrollos enumerados allí, sin crear prácticas ni evaluaciones. Los anexos no se evalúan (prop_e §9). |
| Datos de ejemplos | Simulados con parámetros explícitos para ilustrar las deducciones; no son datos de CALAIRE ni resultados del SRP o del Level 2. |
| Remisiones | M01–M13, identificadas en cada anexo («Se usa desde…») y en la lista de remisiones de la bitácora. |
| Referencias clave | GUM; GUM-S1; ISO/TS 28037; Crowder 2020; Hahs-Vaughn y Lomax; Montgomery. |

| Anexo | Nivel de primer uso | Consumidores |
|---|---|---|
| AX.1 | B | M2-B, M4-B |
| AX.2 | I | M3-I, M8-I; M1-A |
| AX.3 | B | M3-B; presupuestos posteriores |
| AX.4 | B | M6-B/I, M8 |
| AX.5–AX.6 | I | M7-I; M13-A (AX.5) |
| AX.7 | I | M4-I, M8-I |
| AX.8 | A | M7-A, M9-A |
| AX.9 | I | M9-I/A, M10; M13-A |
| AX.10 | I | M10-I/A |
| AX.11 | I | M12-I |
| AX.12 | A | M11-A |
| AX.13 | A | M13-A |

Este capítulo no agrega un nivel de evaluación ni una práctica. Las secciones indican desde qué nivel se usa el resultado; como los niveles son acumulativos, los niveles posteriores también pueden seguir la deducción. Las fórmulas que aparecen en pizarra se leerán en voz alta y se explicarán término por término. Cada ejemplo numérico se reproduce con un script `AX_*.py` en `calc/`.

## AX.1. Divisor `n − 1` y grados de libertad de `s`

**Se usa desde B** (M2-B y M4-B).

### Escena AX.1. La media estimada consume un grado de libertad

Vamos a seguir por qué la dispersión de una muestra se estima con el divisor `n − 1` cuando antes calculamos la media a partir de esos mismos datos. No es una corrección arbitraria: al ajustar la media, los desvíos quedan sujetos a una restricción. Para una muestra aleatoria independiente $X_1,\ldots,X_n$ de una población con media $\mu$ y varianza $\sigma^2$, cada desviación respecto de la media muestral no puede elegirse libremente, porque su suma es cero. La demostración usa el modelo de observaciones independientes con varianza común; no convierte cualquier grupo de lecturas dependientes en una muestra independiente. [Hahs-Vaughn y Lomax; Crowder 2020]

> **[PIZARRA]** $\sum_{i=1}^{n}(X_i-\bar X)=0$ y $\sum_{i=1}^{n}(X_i-\bar X)^2=\sum_{i=1}^{n}(X_i-\mu)^2-n(\bar X-\mu)^2$.

Leamos despacio la segunda identidad. En la suma alrededor de la media verdadera restamos la parte explicada por el hecho de que la media muestral también fluctúa. Tomamos esperanzas: la suma de los primeros cuadrados tiene esperanza $n\sigma^2$. Además, la media muestral tiene varianza $\sigma^2/n$, así que la esperanza de $n(\bar X-\mu)^2$ es $\sigma^2$. Queda $(n-1)\sigma^2$. Al dividir la suma de cuadrados por $n-1$, su esperanza es exactamente $\sigma^2$. Si dividiéramos por n, el promedio esperado sería $(n-1)\sigma^2/n$, que tiende a quedarse corto.

> **[PIZARRA]** $s^2=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar X)^2,\qquad \nu=n-1.$

En palabras: calculamos las distancias a la media de la muestra, elevamos al cuadrado, sumamos y dividimos por uno menos que el número de observaciones. Los grados de libertad cuentan aquí las desviaciones independientes que quedan después de imponer la suma cero. En el ejemplo docente, usemos los valores simulados 2, 4 y 6. La media es 4 y la suma de cuadrados es 8; con divisor 2 obtenemos $s^2=4$, $s=2$ y dos grados de libertad. Con divisor 3 obtendríamos $8/3$, que no es el estimador insesgado de la varianza bajo el modelo.

> **[ERROR CRÍTICO]** No interpreten `n − 1` como regla automática para cualquier conjunto de lecturas. La unidad independiente y el modelo determinan los grados de libertad. Si hay dependencia temporal, bloques, parámetros adicionales estimados o una estructura de varios días, detengan el cálculo y consulten el modelo del capítulo correspondiente.

Este resultado se usa en M2 para describir dispersión muestral y en M4 para comprender los grados de libertad de la t de una media. La deducción se consulta aquí; en el capítulo M02/M04 se aplica sin desarrollarla. [Hahs-Vaughn y Lomax]

## AX.2. Varianza de combinaciones lineales y propagación con covarianza

**Se usa desde I** en la ley general de varianza (M3-I y M8-I); la idea de entradas comunes se anticipa en M1-A. Los niveles posteriores reutilizan el resultado.

### Escena AX.2. Los términos cruzados contienen la dependencia

Pensemos en un resultado que combina dos magnitudes, por ejemplo una diferencia de resultados fotométricos. La varianza de una suma no se obtiene siempre sumando varianzas: al elevar al cuadrado aparecen productos cruzados. Partimos de variables aleatorias $X_i$ con coeficientes fijos $c_i$, centramos cada entrada respecto de su esperanza y expandimos el cuadrado.

> **[PIZARRA]** $Y=\sum_i c_iX_i,\quad Y-E(Y)=\sum_i c_i(X_i-E(X_i))$.
>
> $u^2(Y)=\sum_i c_i^2u^2(X_i)+2\sum_{i<j}c_ic_j\,\operatorname{cov}(X_i,X_j).$

Voy a leerlo: la varianza de Y es la suma de las varianzas de cada entrada multiplicadas por el cuadrado de su sensibilidad, más dos veces cada covarianza multiplicada por los dos coeficientes. ¿Por qué aparece covarianza? Porque en la expansión del cuadrado figura el producto de las dos desviaciones; su esperanza es, por definición, la covarianza. Esta expresión es exacta para una combinación lineal. En la GUM, la covarianza también se escribe $u(x_i,x_j)$. [GUM 5.2.2]

Para una suma con coeficientes uno, la covarianza positiva aumenta la varianza. Para una diferencia, los coeficientes tienen signos opuestos y la covarianza positiva resta. Imaginemos, como ejemplo **simulado**, dos resultados que comparten una contribución de incertidumbre estándar de 0,30 nmol/mol y tienen cada uno una contribución independiente de 0,20 nmol/mol. Cada varianza total es $0,30^2+0,20^2=0,13$. La covarianza común vale $0,30^2=0,09$. En la diferencia la varianza es $0,13+0,13-2(0,09)=0,08$ y la incertidumbre estándar es aproximadamente 0,283 nmol/mol. Si fingimos independencia, calculamos raíz de 0,26, aproximadamente 0,510 nmol/mol: contabilizamos dos veces una contribución que se cancela.

Pasemos de una combinación lineal a una función general $Y=f(X)$. Cerca de los valores de entrada, aproximamos la función con su expansión de Taylor de primer orden. Los coeficientes de la combinación son las derivadas parciales, o sensibilidades. Así obtenemos la ley de propagación linealizada. [GUM 5.1.2; GUM 5.2.2]

> **[PIZARRA]** $u_c^2(y)\approx \sum_i c_i^2u^2(x_i)+2\sum_{i<j}c_ic_j\,\operatorname{cov}(x_i,x_j),\quad c_i=\left.\frac{\partial f}{\partial x_i}\right|_{\boldsymbol{x}}.$

La aproximación requiere que la función se comporte suficientemente bien en la región de incertidumbre y que los términos de orden superior no sean importantes para el uso previsto. Si la no linealidad importa, M13-A contrasta la linealización con Monte Carlo. Las unidades también sirven de control: cada término debe tener unidades al cuadrado del resultado.

> **[ERROR CRÍTICO]** Una entrada compartida no implica por sí sola que toda la incertidumbre se cancele: solo se cancela la parte común, con el signo y el coeficiente adecuados. No supongan covarianza cero sin sustento ni sumen una covarianza como si fuera una varianza.

M03-I usa la expresión para dependencia; M08 la usa al construir presupuestos; M01-A identifica entradas comunes y M09 la aplica a comparaciones. [GUM 5.1.2; GUM 5.2.2]

## AX.3. Varianzas rectangular y triangular

**Se usa desde B** (M3-B y presupuestos de incertidumbre posteriores).

### Escena AX.3. De los límites a la incertidumbre estándar

Cuando una especificación solo fija límites, convertimos ese intervalo en una distribución supuesta y calculamos su desviación estándar. No estamos afirmando que hayamos observado una muestra: la forma de la distribución representa la información disponible. La GUM describe estas evaluaciones tipo B y las distribuciones rectangulares y triangulares. [GUM 4.3.7, 4.4.5–4.4.6]

Para una rectangular simétrica entre $-h$ y $h$, la densidad es constante, $1/(2h)$. La media es cero por simetría. Integramos el cuadrado desde $-h$ hasta $h$, dividido por el ancho total.

> **[PIZARRA]** $u^2=\frac{1}{2h}\int_{-h}^{h}x^2\,dx=\frac{h^2}{3},\qquad u=\frac{h}{\sqrt 3}.$

En voz alta: la incertidumbre estándar es la semiamplitud dividida por raíz de tres. Si el dato es una resolución total $\delta$ y el error de redondeo está entre $-\delta/2$ y $+\delta/2$, entonces la semiamplitud es $\delta/2$. Sustituyendo, $u=\delta/\sqrt{12}$. No confundamos resolución total con semiamplitud.

En una triangular simétrica con los mismos extremos $-h$ y $h$, la densidad tiene máximo en cero y decrece linealmente hasta los límites. Al integrar $x^2$ contra esa densidad se obtiene $h^2/6$, por tanto $u=h/\sqrt 6$. Su incertidumbre es menor que la rectangular porque asigna más peso a valores cercanos al centro. [GUM 4.3.9; GUM 4.4.6]

> **[PIZARRA]** Rectangular: $u=h/\sqrt3$; triangular: $u=h/\sqrt6$; resolución total $\delta$: $u=\delta/\sqrt{12}$.

Ejemplo docente **simulado**: una tolerancia simétrica de semiamplitud 0,60 nmol/mol da, bajo hipótesis rectangular, $u=0,60/\sqrt3\approx0,346$ nmol/mol. Bajo una hipótesis triangular del mismo ancho, $u=0,60/\sqrt6\approx0,245$ nmol/mol. Si en cambio se trata de una resolución total de 0,12 nmol/mol, la contribución rectangular es $0,12/\sqrt{12}\approx0,0346$ nmol/mol. Las tres cantidades se reproducen en `calc/AX_03.py`.

> **[ERROR CRÍTICO]** No elijan triangular solo porque produce una incertidumbre menor. La forma debe representar la información: igualdad de probabilidad dentro del intervalo sustenta rectangular; información que hace más probables los valores centrales puede sustentar triangular.

M03-B convierte especificaciones a incertidumbres estándar; M08 reutiliza las varianzas al combinar entradas. [GUM 4.3.7; GUM 4.3.9; GUM 4.4.5–4.4.6]

## AX.4. Cuadrados medios esperados y precisión del promedio

**Se usa desde B** para interpretar la contribución de precisión en M6-B; I añade la estimación ANOVA.

### Escena AX.4. Separar el día de la lectura

Vamos a deducir el resultado del modelo equilibrado de un factor aleatorio que usa M6. Para cada día $d$ y lectura $j$, escribimos el error como una media general, un efecto aleatorio de día y un error de lectura. Los efectos diarios son independientes con varianza $\tau^2$; las lecturas son independientes con varianza $\sigma^2$, e independientes de los días. Hay el mismo número $n$ de lecturas en cada uno de $d$ días. [GUM H.5; Crowder 2020]

> **[PIZARRA]** $e_{dj}=\mu+D_d+\varepsilon_{dj}$; $E(D_d)=E(\varepsilon_{dj})=0$, $\operatorname{var}(D_d)=\tau^2$, $\operatorname{var}(\varepsilon_{dj})=\sigma^2$.

Para hacer explícito el cálculo, definimos la media de cada día $\bar e_{d\cdot}$ y la media general $\bar e_{\cdot\cdot}$. La suma de cuadrados dentro de días suma $(e_{dj}-\bar e_{d\cdot})^2$. Al centrar dentro del mismo día, el efecto $D_d$ se cancela; en cada uno de los $d$ días quedan $n-1$ contrastes independientes con varianza $\sigma^2$. Su esperanza total es $d(n-1)\sigma^2$, y al dividir por sus grados $d(n-1)$ obtenemos $E(MS_{dentro})=\sigma^2$.

La suma entre días es $n\sum_d(\bar e_{d\cdot}-\bar e_{\cdot\cdot})^2$. Cada media diaria varía con varianza $\tau^2+\sigma^2/n$; al multiplicar por n y tomar la esperanza del cuadrado medio entre días, con $d-1$ contrastes entre medias, obtenemos $E(MS_{entre})=n(\tau^2+\sigma^2/n)=n\tau^2+\sigma^2$. [GUM H.5]

> **[PIZARRA]** $E(MS_{dentro})=\sigma^2$; $E(MS_{entre})=\sigma^2+n\tau^2$.

La diferencia entre los cuadrados medios, dividida por n, estima $\tau^2$. Para interpretar la precisión de la media general, podemos verla directamente: la media general es la media de d efectos diarios y de dn errores de lectura. Los efectos diarios aportan varianza $\tau^2/d$; las lecturas aportan $\sigma^2/(dn)$. Son independientes, así que sumamos.

> **[PIZARRA]** $u^2_{prec}(\bar e)=\frac{\tau^2}{d}+\frac{\sigma^2}{dn}\quad\longrightarrow\quad \widehat u^2_{prec}(\bar e)=\frac{s^2_{entre}}{d}+\frac{s_r^2}{dn}$.

Ejemplo **simulado**: con $d=4$, $n=3$, $s_{entre}=0,20$ y $s_r=0,30$ nmol/mol, la contribución de varianza es $0,20^2/4+0,30^2/12=0,0175$ y su raíz es aproximadamente 0,1323 nmol/mol. Si se omitiera el efecto de día, quedaría $0,09/12=0,0075$, raíz 0,0866: se infravalora la dispersión del promedio en varios días. [GUM H.5]

> **[ERROR CRÍTICO]** Esta fórmula requiere días independientes, equilibrio y el modelo indicado. Si se proporcionan desviaciones de las medias diarias, no se vuelve a añadir la repetibilidad: bajo el mismo modelo se usa la varianza de esas medias dividida por $d$, el número de días. Dependencia, desequilibrio o confusión entre día y ciclo exige revisar el modelo, no forzar la fórmula.

En M6-B el operador recibe las componentes y calcula su contribución de precisión; en M6-I se ajusta el ANOVA y se estiman componentes; M8 suma las demás entradas del presupuesto. [GUM H.5]

## AX.5. Ecuaciones normales OLS/WLS y covarianza de parámetros

**Se usa desde I** (M7-I); A reutiliza la formulación matricial.

### Escena AX.5. De minimizar residuos a la incertidumbre de la recta

Escribimos la recta como $y=a+bx$. En forma matricial, cada fila de la matriz de diseño contiene uno y el valor de referencia. OLS elige los parámetros que minimizan la suma de residuos cuadrados. Derivamos respecto del vector de parámetros, igualamos a cero y obtenemos las ecuaciones normales. Si la matriz de diseño tiene rango completo, la solución es única. [Crowder 2020]

> **[PIZARRA]** $\boldsymbol y=X\boldsymbol\beta+\boldsymbol\varepsilon$, $Q=(\boldsymbol y-X\boldsymbol\beta)^T(\boldsymbol y-X\boldsymbol\beta)$; $X^T X\hat{\boldsymbol\beta}=X^T\boldsymbol y$; $\hat{\boldsymbol\beta}=(X^TX)^{-1}X^T\boldsymbol y$.

Leamos: invertimos la matriz de productos cruzados del diseño y la multiplicamos por los productos entre diseño y observaciones. Si los errores tienen media cero y matriz de covarianza $\sigma^2I$, la covarianza del estimador resulta $\sigma^2(X^TX)^{-1}$. En la práctica se sustituye $\sigma^2$ por una estimación residual.

WLS minimiza una suma de residuos ponderados y reemplaza el producto ordinario por uno con matriz de pesos $W$. Si W es la inversa de la matriz de covarianza conocida salvo un factor de escala, el estimador es GLS para ese modelo. Con pesos diagonales, se trata cada punto como independiente con varianzas distintas; no resuelve por sí solo incertidumbre relevante en x ni dependencia entre puntos. [ISO 28037 5.2.2 y 5.5; Crowder 2020]

> **[PIZARRA]** $\hat{\boldsymbol\beta}_{W}=(X^TWX)^{-1}X^TW\boldsymbol y$; $\operatorname{cov}(\hat{\boldsymbol\beta}_{W})=\hat\sigma^2(X^TWX)^{-1}$ bajo el modelo de pesos relativos correctos.

Para mostrar de dónde sale la covarianza entre intercepto y pendiente, consideremos dos puntos de referencia igualmente ponderados, 0 y 1, con la misma varianza residual. Hay dos observaciones y dos parámetros: la recta pasa por ambos y el ajuste residual no deja grados para estimar la varianza por sí mismo; por eso el ejemplo de cálculo de covarianza requiere tomar $\sigma^2$ como conocida o estimada independientemente. Para este diseño $X^TX=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, cuya inversa es $\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$. Así la covarianza de a y b es $-\sigma^2$, y la varianza de b es $2\sigma^2$. El signo negativo importa al predecir.

> **[ERROR CRÍTICO]** No se fija automáticamente $\nu=n-2$ para cualquier ajuste, ni se interpreta $R^2$ como prueba de adecuación. El diseño, réplicas, pesos y modelo determinan la inferencia. Si la incertidumbre del eje de referencia es relevante, el ajuste con x fijo se escala a A.

M07-I remite aquí para las ecuaciones normales y la covarianza de parámetros; M13-A también usa esta base al producir parámetros y salidas múltiples. [ISO 28037 5.5]

## AX.6. Incertidumbre de la predicción inversa

**Se usa desde I** (M7-I).

### Escena AX.6. Propagar a través de la inversión

La recta de calibración describe indicación en función de referencia: $y=a+bx$. Para una indicación nueva, resolvemos para la referencia, $\hat x=(y-a)/b$. La incertidumbre no es solo la incertidumbre de y: también dependen a y b, y a y b suelen estar correlacionados. Linealizamos esta función alrededor de las estimaciones y aplicamos la ley de propagación. [GUM 5.1.2; ISO 28037]

> **[PIZARRA]** $g(y,a,b)=\frac{y-a}{b}$; $\frac{\partial g}{\partial y}=\frac1b$, $\frac{\partial g}{\partial a}=-\frac1b$, $\frac{\partial g}{\partial b}=-\frac{y-a}{b^2}=-\frac{\hat x}{b}$.

Al sustituir las derivadas, sumamos la varianza de cada entrada multiplicada por el cuadrado de su derivada y los términos de covarianza. Si y es independiente del ajuste, no hay covarianzas entre y y los parámetros, pero sí permanece $\operatorname{cov}(a,b)$.

> **[PIZARRA]** $u^2(\hat x)\approx\frac{u^2(y)+u^2(a)+\hat x^2u^2(b)+2\hat x\,\operatorname{cov}(a,b)}{b^2}$.

El signo del término cruzado se verifica: las sensibilidades de a y b son ambas negativas, de modo que su producto es positivo y el término es $+2\hat x\operatorname{cov}(a,b)$ en el numerador. En ejemplos donde la covarianza es negativa, esa contribución reduce la varianza. Si la nueva indicación $y_0$ comparte datos con el ajuste o existe incertidumbre en $x$, hay más términos o un modelo diferente.

Ejemplo **simulado**: tomemos $a=1$, $b=2$, $y=11$, de modo que $\hat x=5$. Sean $u(y)=0,20$, $u(a)=0,10$, $u(b)=0,02$ y $\operatorname{cov}(a,b)=-0,001$. El numerador es $0,04+0,01+25(0,0004)+10(-0,001)=0,05$; dividido por 4 da 0,0125 y la incertidumbre estándar linealizada es 0,1118 en las unidades de x.

> **[ERROR CRÍTICO]** Esta aproximación puede fallar si la pendiente está cerca de cero, las incertidumbres son grandes o la transformación inversa es muy no lineal en la región de interés. No extrapolen más allá del intervalo validado.
>
> **[ESCALAMIENTO]** Si la pendiente es inestable, la incertidumbre del eje de referencia es relevante, o la incertidumbre de la predicción depende fuertemente de la posición dentro del intervalo, detengan el cálculo de plantilla y consulten el análisis avanzado o a la persona responsable.

M07-I usa este resultado para la incertidumbre de un valor de uso; el presupuesto completo todavía debe incluir las demás fuentes. [GUM 5.1.2]

## AX.7. Welch–Satterthwaite y grados de libertad efectivos

**Se usa desde I** (M4-I/M8-I).

### Escena AX.7. Aproximar cuánta información sostiene la incertidumbre

Supongamos que el presupuesto combinado contiene componentes independientes $u_i^2$ y que cada componente procede de una estimación con grados de libertad $\nu_i$. El cuadrado de la incertidumbre combinada es la suma de esos cuadrados. Pero no todas las componentes tienen la misma precisión. Welch–Satterthwaite aproxima la distribución de esa suma de variables escaladas por una chi-cuadrado equivalente, igualando su media y su varianza. La razón resultante define los grados de libertad efectivos. [GUM G.4, ecuación G.2b]

> **[PIZARRA]** $u_c^2=\sum_i u_i^2,\qquad \nu_{eff}\approx\frac{u_c^4}{\sum_i u_i^4/\nu_i}.$

La fórmula dice: elevamos al cuadrado la varianza combinada; abajo sumamos la cuarta potencia de cada contribución dividida por sus grados de libertad. Si una contribución domina y tiene pocos grados, el total también tendrá pocos grados. Si una contribución tipo B se considera evaluada con grados infinitos, su término en el denominador se toma como cero; no significa que la incertidumbre desaparezca.

Ejemplo **simulado**: dos contribuciones independientes, 0,30 con 5 grados y 0,40 con 20. El total al cuadrado es 0,25; el denominador es $0,30^4/5+0,40^4/20=0,0029$; por tanto $\nu_{eff}=0,25^2/0,0029\approx21,55$. Para cobertura bilateral central del 95 %, se usa el cuantil t con esos grados efectivos, no se reemplaza sin justificación por 2. [GUM G.4]

> **[ERROR CRÍTICO]** La aproximación presentada es para componentes independientes conforme al modelo. No se aplica mecánicamente a componentes correlacionadas ni arregla un presupuesto con doble conteo.
>
> **[ESCALAMIENTO]** Si hay covarianzas entre componentes, cobertura no simétrica o pocos grados efectivos cuya distribución no quede descrita por la aproximación, detengan la conversión automática a un factor t y soliciten revisión avanzada del modelo.

M04-I usa aproximaciones de grados de libertad para pruebas de Welch; M08-I la usa en presupuestos elementales y declara sus límites. [GUM G.4]

## AX.8. GGMR matricial con `V_xy = 0` y chi-cuadrado de consistencia

**Se usa desde A** (M7-A/M9-A), dentro del alcance validado con covarianza cruzada entre ejes nula.

### Escena AX.8. Ajustar parámetros y abscisas verdaderas

En OLS las abscisas se tratan como fijas. En la regresión generalizada de Gauss–Markov, los valores observados de x e y tienen incertidumbres y covarianzas. Introducimos para cada punto una abscisa ajustada $\xi_i$, además de los parámetros a y b. Minimizar una distancia cuadrática ponderada por la covarianza cuantifica cuánto hay que corregir las mediciones para que satisfagan $y_i=a+b\xi_i$. ISO/TS 28037 desarrolla el caso general; aquí restringimos a `V_xy=0`, tal como el alcance validado del curso. [ISO 28037, cláusula 10.1]

> **[PIZARRA]** $\boldsymbol r(\boldsymbol\theta)=\begin{pmatrix}\boldsymbol x-\boldsymbol\xi\\\boldsymbol y-a\boldsymbol 1-b\boldsymbol\xi\end{pmatrix},\quad V=\begin{pmatrix}V_x&0\\0&V_y\end{pmatrix},\quad Q=\boldsymbol r^TV^{-1}\boldsymbol r.$

La minimización no lineal se resuelve iterativamente, por ejemplo con Gauss–Newton. En cada iteración se linealizan los residuos respecto de parámetros y abscisas ajustadas, se resuelve el sistema ponderado y se actualiza la estimación. La matriz de covarianza conjunta describe también dependencias entre puntos dentro de cada eje. Matrices diagonales representan independencia; una causa común puede producir elementos fuera de la diagonal. El cero en los bloques cruzados no autoriza a eliminar covarianzas entre puntos de x o entre puntos de y. [ISO 28037, cláusula 10]

Después del ajuste, la suma cuadrática ponderada se compara con una distribución chi-cuadrado con grados de libertad coherentes con el diseño y el número de restricciones. En el modelo lineal regular, contamos observaciones independientes y restamos restricciones ajustadas. Con $n$ puntos hay $2n$ observaciones (abscisas y ordenadas) y $n+2$ parámetros (las $n$ abscisas ajustadas, $a$ y $b$). Quedan $2n-(n+2)=n-2$ grados de libertad. Con seis puntos, quedan cuatro. Si la matriz de covarianza tiene estructura o hay restricciones adicionales, el conteo se debe justificar en la formulación y no asumir por analogía. El cociente de la distancia entre sus grados de libertad, $Q/\nu$, es un resumen reducido, no una nueva estimación de incertidumbre por sí sola. Un valor excesivamente alto puede indicar inconsistencias o incertidumbres subestimadas; uno anormalmente bajo puede indicar incertidumbres sobrestimadas, correlaciones mal modeladas o grados de libertad incorrectos. El diagnóstico no es una prueba automática de que el modelo sea verdadero. [ISO 28037, cláusula 5.6]

Ejemplo didáctico **simulado**: para un ajuste con seis puntos, quedan cuatro grados de libertad; si la distancia observada es 3,2, el cociente reducido $Q/\nu$ es $3,2/4=0,8$. Se interpreta junto con la distribución y los residuos, no como umbral universal. Este cociente es ilustrativo.

> **[ERROR CRÍTICO]** No use esta forma como GGMR general cuando $V_{xy}\ne0$. No sustituye la validación del software ni permite atribuir una comparación simulada a CALAIRE.
>
> **[ESCALAMIENTO]** Si la matriz no es simétrica, no es admisible, resulta singular, o las incertidumbres cruzadas entre ejes no son nulas, no continúen con esta formulación reducida: remitan el caso a una implementación avanzada validada.

M7-A y M9-A usan la formulación para ajustar con incertidumbre en ambos ejes y revisar consistencia. [ISO 28037, cláusula 10]

## AX.9. Diferencia con patrón compartido y grado de equivalencia

**Se usa desde I** para diferencias dependientes (M9-I/M10); A añade la comparación con referencia común.

### Escena AX.9. Lo común puede cancelarse

Partamos de dos resultados, $R_1$ y $R_2$, que dependen de una contribución común $C$ y de contribuciones independientes $A$ y $B$: $R_1=C+A$ y $R_2=C+B$. Al restar, $C$ desaparece algebraicamente. En el lenguaje de varianzas, cada resultado contiene $u^2(C)$ y su covarianza mutua también contiene $u^2(C)$. [GUM 5.2.2]

> **[PIZARRA]** $\Delta=R_1-R_2$; $u^2(\Delta)=u_1^2+u_2^2-2\operatorname{cov}(R_1,R_2)$.

Esta es AX.2 aplicada a coeficientes uno y menos uno. Si el patrón común introduce la misma contribución con igual sensibilidad, se cancela en la diferencia. Si las sensibilidades difieren, solo se cancela parcialmente; si la entrada afecta con signos opuestos, puede aumentar la diferencia. La estructura causal y el modelo de medición deciden el signo y el tamaño de la covarianza.

Ejemplo **simulado**: incertidumbre común 0,30 y dos contribuciones independientes de 0,20. Cada resultado tiene $u^2=0,13$, y la covarianza es 0,09. Así $u^2(\Delta)=0,13+0,13-0,18=0,08$, o $u(\Delta)=0,283$ nmol/mol. Si se trata de una diferencia de dos participantes frente a una referencia común $R$, escribimos $D_i=R_i-R$. Para dos diferencias, $\operatorname{cov}(D_i,D_j)$ incluye la varianza de R. La misma referencia compartida induce dependencia entre grados de equivalencia; no se cuentan los participantes como independientes.

> **[PIZARRA]** $D_i=x_i-x_{ref};\quad \operatorname{cov}(D_i,D_j)=\operatorname{cov}(x_i,x_j)-\operatorname{cov}(x_i,x_{ref})-\operatorname{cov}(x_{ref},x_j)+u^2(x_{ref}).$

El grado de equivalencia frente a una referencia común describe la diferencia y su incertidumbre: se informa $D_i$ con $u(D_i)$ o con incertidumbre expandida declarada. Un indicador normalizado puede complementar, pero no sustituye la diferencia ni convierte el resultado en verificación independiente. El alcance aquí es una referencia común definida, no un KCRV combinado al que contribuya quien se evalúa. [GUM 5.2.2]

> **[ERROR CRÍTICO]** No calculen la incertidumbre de una diferencia como cuadratura simple cuando comparten patrón sin justificar la independencia. Y no describan una compatibilidad estadística bajo el modelo de dependencia como prueba independiente del instrumento.

M9-I/M10 emplean la diferencia con covarianza; M9-A informa el grado de equivalencia frente a referencia común. [GUM 5.2.2]

## AX.10. Falsa aceptación y falso rechazo

**Se usa desde I** para riesgos de decisión (M10-I); A añade modelos de riesgo específicos, globales y dependientes.

### Escena AX.10. Integrar la distribución a ambos lados de la regla

Una regla de decisión separa resultados aceptables de no aceptables. El riesgo de falsa aceptación es la probabilidad de que el resultado cumpla la regla de aceptación cuando el valor verdadero está fuera de especificación. El falso rechazo es la probabilidad de no aceptar cuando el valor verdadero sí está dentro. Son probabilidades condicionadas a un valor o distribución de valores verdaderos y a un modelo de medida. No hay un número universal de riesgo sin esas condiciones. [JCGM 106:2012, no disponible en docs/; ILAC-G8:09/2019, no disponible en docs/]

Consideremos una medición $Y\sim N(\theta,u^2)$ y un límite superior $L$. La regla simple acepta si $Y\le L$. Si el valor verdadero es $\theta>L$, la falsa aceptación es la probabilidad de que Y caiga bajo L. Si $\theta\le L$, el falso rechazo es la probabilidad de que Y exceda L. Al estandarizar obtenemos las colas de la normal.

> **[PIZARRA]** $P_{FA}(\theta)=P(Y\le L\mid\theta>L)=\Phi\!\left(\frac{L-\theta}{u}\right)$; $P_{FR}(\theta)=P(Y>L\mid\theta\le L)=1-\Phi\!\left(\frac{L-\theta}{u}\right)$.

Con límite bilateral $[L_i,L_s]$ y aceptación si la medición cae dentro, escribimos la probabilidad de aceptación como $\Phi((L_s-\theta)/u)-\Phi((L_i-\theta)/u)$. Para un valor verdadero fuera, esa probabilidad es la falsa aceptación; para un valor dentro, el falso rechazo es uno menos esa probabilidad, o la suma de las dos colas. Una banda de guarda sustituye el intervalo de aceptación por uno más estrecho, de modo que cambia ambos riesgos. Para riesgos globales, promediamos las probabilidades condicionadas respecto de una distribución explícita de valores verdaderos. Esta es una integración de densidad sobre la región que lleva a la decisión equivocada; la función de distribución aparece al integrar la densidad normal hasta un umbral. [JCGM 106:2012, no disponible en docs/]

Ejemplo **simulado** de límite superior: $L=10$, $u=1$. Si $\theta=12$ está fuera, $P_{FA}=\Phi(-2)\approx0,0228$. Si $\theta=8$ está dentro, $P_{FR}=1-\Phi(2)\approx0,0228$. Para $\theta=10$, justo en el límite, la probabilidad de aceptar es 0,5 y la de rechazar también. Ninguna regla sin guarda da un riesgo pequeño en ese punto; por eso, cerca del límite debemos declarar la regla y el riesgo tolerado.

> **[ERROR CRÍTICO]** No llamen “riesgo del equipo” a una probabilidad condicionada sin especificar modelo, regla y valor verdadero. La decisión estadística no reemplaza el requisito contractual ni una regla acordada.

M10-I compara reglas y riesgos; M10-A extiende el análisis a dependencia y riesgo global con distribuciones explícitas. [JCGM 106:2012; ILAC-G8:09/2019; ambas no disponibles en docs/]

## AX.11. Límites de confianza para precisión y sesgo

**Se usa desde I** (M12-I).

### Escena AX.11. La dispersión también tiene incertidumbre

Si las observaciones independientes provienen de una población normal, la suma de cuadrados alrededor de la media, dividida por la varianza verdadera, sigue una chi-cuadrado con $n-1$ grados de libertad. Al invertir los cuantiles obtenemos límites de confianza para la desviación estándar. [Hahs-Vaughn y Lomax]

> **[PIZARRA]** $\frac{(n-1)s^2}{\sigma^2}\sim\chi^2_{n-1};\quad \sigma_{inf}=s\sqrt{\frac{n-1}{\chi^2_{1-\alpha/2,n-1}}},\quad \sigma_{sup}=s\sqrt{\frac{n-1}{\chi^2_{\alpha/2,n-1}}}.$

Los cuantiles se nombran aquí con probabilidad acumulada a la izquierda. Como el cuantil inferior está en el denominador del límite superior, el orden se invierte. La construcción del intervalo requiere normalidad e independencia de la unidad de análisis. Si hay dependencia temporal o mezcla de periodos, la fórmula no queda validada por el simple hecho de tener muchos datos.

Para el sesgo medio, el error estándar de la media es $s/\sqrt n$. Al estandarizar con t porque la desviación se estima con los mismos datos, obtenemos un intervalo bilateral. [Hahs-Vaughn y Lomax, inferencia t]

> **[PIZARRA]** $\mu\in\left[\bar d-t_{1-\alpha/2,n-1}\frac{s}{\sqrt n},\;\bar d+t_{1-\alpha/2,n-1}\frac{s}{\sqrt n}\right].$

Ejemplo **simulado**: con n=10 diferencias independientes, $\bar d=0,20$, $s=0,30$ nmol/mol, un intervalo para la media usa el cuantil $t_{0,975;9}$ y semiancho $t_{0,975;9}(0,30/\sqrt{10})$. Para la precisión, los límites dependen de los cuantiles chi-cuadrado con nueve grados.

> **[ERROR CRÍTICO]** No se intercambian límites de precisión y sesgo: uno usa chi-cuadrado para la varianza normal, el otro t para una media. El intervalo de una desviación no es una incertidumbre de calibración ni sustituye el presupuesto de incertidumbre.

M12-I usa estos límites para indicadores de precisión y sesgo. [Hahs-Vaughn y Lomax]

## AX.12. Varianza de EWMA y longitud media de corrida

**Se usa desde A** (M11-A).

### Escena AX.12. Memoria exponencial y tiempo hasta la señal

Un EWMA actualiza su estadístico mezclando la observación presente con el valor previo. Para lecturas independientes de varianza $\sigma^2$ y el estadístico centrado en la media bajo control, desplegamos la recurrencia. Cada observación histórica recibe un peso geométrico; al calcular la varianza, las observaciones independientes no tienen términos cruzados. La suma geométrica lleva a la varianza del EWMA en el instante t. [Montgomery, *Introduction to Statistical Quality Control*, no disponible en docs/]

> **[PIZARRA]** $Z_t=\lambda X_t+(1-\lambda)Z_{t-1}$; $\operatorname{var}(Z_t)=\sigma^2\frac{\lambda}{2-\lambda}\left[1-(1-\lambda)^{2t}\right]$; en régimen, $\sigma_Z^2=\sigma^2\frac{\lambda}{2-\lambda}$.

Para ver la suma, repetimos la sustitución: $Z_t=(1-\lambda)^tZ_0+\lambda\sum_{j=1}^{t}(1-\lambda)^{t-j}X_j$. Si iniciamos en el objetivo conocido, el primer término no aporta varianza. Elevamos al cuadrado cada peso y multiplicamos por $\sigma^2$; queda $\lambda^2\sigma^2\sum_{k=0}^{t-1}(1-\lambda)^{2k}$. La suma geométrica es $[1-(1-\lambda)^{2t}]/[1-(1-\lambda)^2]$, y el denominador se simplifica a $\lambda(2-\lambda)$. Así obtenemos la expresión de la pizarra. La memoria larga se produce cuando $\lambda$ es pequeño: el peso de hoy es menor y las observaciones previas tardan más en desaparecer. Los límites que usan la varianza transitoria cambian con t; en régimen se aproximan a límites constantes. Si las observaciones están autocorrelacionadas, la suma necesita covarianzas adicionales y esta expresión independiente no basta.

La longitud media de corrida, ARL, es el número esperado de observaciones hasta una señal. Se deriva de la probabilidad de supervivencia: si cada instante tuviera probabilidad constante e independiente p de señal, la longitud sería geométrica y su esperanza $1/p$. En cartas con estadísticos dependientes, incluido EWMA, la probabilidad de señal depende del estado previo. Discretizamos el estado en celdas: $P_{ij}$ es la probabilidad de pasar del estado i a la celda j sin señal. Si $m_i$ es el ARL desde el estado i, condicionamos al primer paso: $m_i=1+\sum_jP_{ij}m_j$.

En forma matricial, $(I-P)\boldsymbol m=\boldsymbol 1$, de donde $\boldsymbol m=(I-P)^{-1}\boldsymbol 1$. La discretización aproxima la transición continua; hay que refinar la malla para comprobar estabilidad.

Para CUSUM se construye la matriz con la transición del acumulador $S_t=\max(0,S_{t-1}+X_t-k)$ y el umbral $h_C$: las transiciones que lo superan son absorbentes y se excluyen de P. [Montgomery, *Introduction to Statistical Quality Control*, no disponible en docs/]

Ejemplo **simulado**: para $\lambda=0,20$ y $\sigma=1$, el factor de régimen es $0,20/1,80=0,1111$ y la desviación del estadístico es 0,3333. Suponiendo observaciones independientes $N(0,1)$, con límites EWMA de tres desviaciones estándar, umbral aproximado 1, y una cadena discretizada en 240 estados, el script estima un ARL bajo control de 559,679. Para CUSUM unilateral con holgura $k=0,5$, umbral 5 y 240 estados, bajo la misma distribución, estima 921,016. Son aproximaciones numéricas para esos parámetros y discretización, no recomendaciones universales; refinar la malla y variar los parámetros permite estudiar estabilidad y sensibilidad. Como referencia matemática, si hubiera señal independiente con probabilidad 0,01 por lectura, la longitud geométrica esperada sería 100; eso no describe el ARL dependiente de EWMA/CUSUM.

> **[ERROR CRÍTICO]** No confundan límites de control con tolerancias y no presenten el ARL bajo control como el tiempo garantizado hasta una alarma. Falsas alarmas, sensibilidad y cambios deben compararse bajo el modelo temporal especificado.

M11-A usa la varianza y ARL para comparar sensibilidad a falsas alarmas y justificar intervalos de revisión. [Montgomery, *Introduction to Statistical Quality Control*, no disponible en docs/]

## AX.13. Fundamento de Monte Carlo y control del número de ensayos

**Se usa desde A** (M13-A).

### Escena AX.13. Propagar distribuciones cuando la linealización no alcanza

La idea de Monte Carlo es directa: representamos las entradas del modelo mediante sus distribuciones conjuntas, generamos realizaciones de esas entradas conservando sus dependencias, evaluamos el modelo para cada realización y resumimos la distribución de salida. La distribución conjunta importa: para una causa común no se sortean sus efectos como si fueran independientes. GUM-S1 describe este procedimiento como una implementación de la propagación de distribuciones y establece condiciones para resumir sus resultados. [GUM-S1 5.9–5.10]

> **[PIZARRA]** Para $r=1,\ldots,M$: generar $\boldsymbol X^{(r)}\sim p_X$; calcular $Y^{(r)}=f(\boldsymbol X^{(r)})$; estimar $y$ y $u(y)$ con la media y desviación estándar de las salidas.

La media de M resultados aleatorios tiene error estándar aproximadamente $s_Y/\sqrt M$. La razón se ve al sumar M realizaciones independientes: cada una tiene varianza $\sigma_Y^2$, la varianza de su suma es $M\sigma_Y^2$, y al dividir la suma por M la varianza de la media queda $\sigma_Y^2/M$. Como $\sigma_Y$ no se conoce, la estimamos con la desviación muestral de las salidas. Por eso aumentar M mejora la estabilidad a ritmo de raíz cuadrada: para reducir a la mitad el error de Monte Carlo, se necesitan aproximadamente cuatro veces más ensayos. Esta relación trata el error numérico de muestreo; no reduce la incertidumbre física de la medición ni corrige un modelo equivocado. El número de ensayos se elige atendiendo a la estabilidad de los resúmenes de interés y a la precisión requerida. Puede usarse un criterio adaptativo, pero debe declararse. [GUM-S1 7.2]

Ejemplo **simulado**: si las salidas tienen desviación 2,0 unidades y se usan $M=10\,000$ ensayos, el error estándar de la media simulada es aproximadamente 0,02 unidades. Para obtener aproximadamente 0,01, se requieren unos 40 000 ensayos. Una incertidumbre estándar estimada, un cuantil de cobertura y un extremo de cola pueden estabilizarse a velocidades diferentes; verificar solo la media no garantiza que los cuantiles estén precisos.

> **[PIZARRA]** $u_{MC}(\bar Y)\approx s_Y/\sqrt M;\qquad M_{2}=4M_{1}\;\Rightarrow\;u_{MC,2}\approx u_{MC,1}/2.$

En el ejemplo de predicción inversa, Monte Carlo conserva la distribución de a, b y la indicación, y evalúa $\hat x=(y-a)/b$ en cada ensayo. Si el denominador puede acercarse a cero, la salida puede ser muy asimétrica o incluso no tener momentos útiles; no se oculta esa forma con una media y desviación sin revisar la distribución. Las semillas fijadas en los scripts permiten reproducir los ejemplos docentes.

> **[ERROR CRÍTICO]** Más ensayos no convierten una distribución de entrada no sustentada en válida. Declare modelo, dependencias, semilla para reproducibilidad y control de convergencia del estadístico reportado.

M13-A contrasta propagación lineal y Monte Carlo, y este anexo justifica la propagación y el control de ensayos. [GUM-S1 5.9–5.10; 7.2]

## Cierre del capítulo

Hemos seguido trece deducciones que explican por qué los métodos de los módulos funcionan y dónde dejan de funcionar. En B se consultan principalmente el divisor muestral, las distribuciones tipo B y el promedio de precisión; en I aparecen propagación, ANOVA, regresión inversa, grados efectivos, diferencias dependientes, riesgos e intervalos de indicadores; en A se añaden formulación matricial, referencia común, control secuencial y Monte Carlo. No se evalúan estas demostraciones, conforme a prop_e §9. El resultado útil es poder regresar al capítulo de aplicación y reconocer qué supuestos acompañan cada fórmula.

## Referencias del capítulo

- **GUM.** JCGM 100:2008 (ISO/IEC Guide 98-3:2008), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*. Archivo: `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`.
- **GUM-S1.** JCGM 101:2008, *Evaluation of measurement data — Supplement 1: Propagation of distributions using a Monte Carlo method*. Archivo: `docs/ISO_IEC Guide 98-3_2008 Suppl.1_2008 - libgen.li.pdf`.
- **ISO 28037.** ISO/TS 28037:2010, *Determination and use of straight-line calibration functions*. Archivo: `docs/ISO 28037.pdf`.
- **Statistical Concepts.** Hahs-Vaughn, D. L. y Lomax, R. G., *Statistical Concepts — A First Course*. Archivo: `docs/Statistical Concepts – A First Course.pdf` y capítulos separados en `docs/statistical_concepts_c*.pdf`.
- **Crowder.** *Introduction to Statistics in Metrology*. Archivo: `docs/Introduction to Statistics in Metrology.pdf` y capítulos `docs/intro_stats_metro_c*.pdf`.
- **Montgomery.** Montgomery, D. C., *Introduction to Statistical Quality Control*. No disponible en `docs/`; fuente externa para EWMA/CUSUM. Numeral y edición pendientes de verificación.
- **JCGM 106.** JCGM 106:2012, *The role of measurement uncertainty in conformity assessment*. No disponible en `docs/`.
- **ILAC-G8.** ILAC-G8:09/2019, *Guidelines on Decision Rules and Statements of Conformity*. No disponible en `docs/`.
- **Prop_e.** *Propuesta E: curso de estadística aplicada a la fotometría de ozono*, 24 de octubre de 2026, §§6 y 9. Referencia de alcance curricular, no técnica.
