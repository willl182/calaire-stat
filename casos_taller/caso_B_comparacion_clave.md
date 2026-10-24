# Caso B — Comparación clave, ajuste GGMR y grado de equivalencia

## Objetivo

Comparar los resultados publicados de una comparación SRP 36–SRP 7, reproducir su regresión OLS con los valores redondeados visibles y realizar una adaptación didáctica GGMR/GLS con incertidumbres y covarianzas inspiradas en el modelo del SRP27 del protocolo BIPM.QM-K1. El ejercicio distingue claramente los resultados del QAPP de los resultados calculados para el taller.

## Módulos que integra

Regresión OLS, WLS y GGMR; incertidumbre de medida con covarianzas; propagación de incertidumbre; grado de equivalencia; prueba de consistencia χ²; interpretación metrológica de una adaptación.

## Fuentes, datos y limitaciones de entrada

### Datos del QAPP

La Figura 14.2 de *SRP QAPP*, Elemento 14.2, «Example Verification Report», PDF p. 37 (página de documento Element 14, p. 3 de 4), presenta doce pares. La figura rotula las columnas de resultado como SRP 36 y SRP 7, y el comentario de comparación como «SRP 36 vs. SRP 7». Se transcriben tal como aparecen (nmol/mol, equivalentes a ppb para O₃ en esta aplicación):

| Punto | SRP 36 | Std. Dev SRP 36 | SRP 7 | Std. Dev SRP 7 |
|---:|---:|---:|---:|---:|
| 1 | 0,0 | 0,2 | 0,2 | 0,1 |
| 2 | 785,9 | 0,2 | 787,4 | 0,6 |
| 3 | 680,3 | 0,2 | 681,5 | 0,5 |
| 4 | 584,1 | 1,0 | 585,5 | 0,5 |
| 5 | 492,7 | 0,4 | 493,7 | 0,4 |
| 6 | 407,8 | 0,5 | 408,5 | 0,3 |
| 7 | 324,4 | 0,4 | 325,1 | 0,3 |
| 8 | 241,8 | 0,2 | 242,4 | 0,2 |
| 9 | 144,9 | 0,2 | 145,4 | 0,2 |
| 10 | 45,6 | 0,2 | 45,9 | 0,1 |
| 11 | 16,0 | 0,2 | 16,1 | 0,1 |
| 12 | −0,1 | 0,1 | 0,1 | 0,2 |

**Fuente de cada pareja e incertidumbre por punto:** `srp_qapp.pdf`, Elemento 14.2, Figura 14.2, PDF p. 37; columnas “Std. Dev” y nota “Points/Concentration: 12”, también transcritas en `datos_caso_B.csv`. Para la variante (i) se asume que cada Std. Dev es la desviación estándar de las 12 lecturas de ese punto y se usa como incertidumbre estándar de la media, `Std. Dev/√12`. Es un supuesto de trabajo que la figura no explicita como tal.

El recuadro de resultados del QAPP publica pendiente `1,00169 ± 0,00012`, intercepto `0,15209 ± 0,05035 ppb`, `R² = 0,99999985` y desviación residual `0,10872 ppb`. El bloque titulado OLS imprime con más dígitos pendiente `1,00169431`, intercepto `0,152088621`, incertidumbres `0,00012279` y `0,050351308`, `R² = 0,99999985`, covarianza pendiente-intercepto `−5,24592×10⁻⁹`, desviación residual `0,108722272` y `12` puntos. Ese mismo bloque también muestra un RSD residual `0,114028881`; se conserva como aparece en el QAPP y no se confunde con la desviación residual.

**Advertencia de orientación y precisión:** el ajuste publicado corresponde a SRP 36 como x y SRP 7 como y. Para cumplir el planteamiento didáctico (SRP 7 referencia y SRP 36 patrón nacional), el GGMR del caso usa x=SRP 7 e y=SRP 36. Las lecturas tabuladas solo están impresas a 0,1 nmol/mol. El OLS con pares impresos da `s=0,109616506`, distinto de `Res Std Dev=0,108722272`; la cifra del bloque tipo LINEST, `s=0,114028881`, equivale a `√(SSresid/10)` y reproduce la incertidumbre publicada de la pendiente `0,00012279`. `Res Std Dev=0,108722272` equivale a `√(SSresid/11)`. Por tanto, el bloque mezcla convenciones de divisor. No se dispone de las lecturas internas usadas por el QAPP, así que el redondeo es una explicación plausible, no una reproducción exacta.

### Modelo de incertidumbre de la adaptación BIPM

Para SRP27, el Apéndice 1, §2, ec. [14], del protocolo BIPM (PDF p. 23) da `u(x)=√(0,28²+(2,92×10⁻³ x)²)` nmol/mol. El Apéndice 1, §3, ecs. [18]–[21] (PDF p. 25) atribuye la covarianza común a magnitudes compartidas de presión, temperatura y longitud óptica: `u(xᵢ,xⱼ)=xᵢ xⱼ u_b²`, `u_b=2,92×10⁻³`. La cifra coincide con la combinación cuadrática de contribuciones del presupuesto BIPM (Apéndice 1, §1, tabla, PDF pp. 21–22); se adopta solo como modelo didáctico para esta comparación.

La covarianza de cada eje se construye como

`U = 0,28² I₁₂ + u_b² v vᵀ`,

por tanto `Uᵢᵢ=0,28²+(u_b vᵢ)²` y, si `i≠j`, `Uᵢⱼ=u_b² vᵢvⱼ`. Se aplica el modelo por separado a los vectores SRP 7 y SRP 36. Para las dos variantes GGMR, la matriz de covarianza conjunta se arma con bloques cruzados cero: tratamos los ejes como independientes. **Es una hipótesis fuerte**, no una consecuencia del protocolo BIPM ni una reconstrucción del presupuesto QAPP: ambos SRP midieron en la misma corrida, con el mismo gas y en el mismo laboratorio. Una covarianza cruzada positiva tendería a reducir la incertidumbre de diferencias SRP36−SRP7 y una covarianza negativa a aumentarla; también puede cambiar la pendiente/intercepto ajustados, su covarianza y `χ²`. Sin datos que estimen covarianza cruzada no se asigna un valor inventado.

### Definiciones del protocolo y del método

- BIPM.QM-K1, §7, p. 8: ajuste generalizado de mínimos cuadrados de `x_NS=a x_SRP27+b`, considerando incertidumbres y covarianzas de los puntos.
- Protocolo A, §8, ecs. [2]–[3], PDF p. 9: con mediciones a la concentración nominal, `D=x_NS−x_SRP27` y `u(D)=√(u²(x_NS)+u²(x_SRP27))`.
- Protocolo B, §§10.1–10.2, ecs. [5]–[7], PDF pp. 19–20: forma basada en la predicción, cuya incertidumbre incluye parámetros y su covarianza. La adaptamos para interpolar con la recta en el sentido SRP 7 (referencia) → SRP 36 (nacional).
- ISO/TS 28037:2010(E), cláusula 10, modelo (13), suma minimizada (14), algoritmo 10.2.2 y 10.3, PDF pp. 39–44 / páginas impresas 31–36: GGMR con incertidumbre/covarianza en ambos ejes. El ejemplo de Tablas 25–26 se usa para validar la implementación.

## Enunciado para el estudiante

1. Ajuste OLS a los doce pares en la orientación publicada (x=SRP 36, y=SRP 7). Compare pendiente, intercepto, R² y desviación residual con el QAPP. Repita en la orientación del taller (x=SRP 7, y=SRP 36). Si las cifras no coinciden, analice la precisión de publicación y la orientación de los ejes.
2. Construya dos conjuntos `U_x`,`U_y`: (i) `Std. Dev/√12` por punto más la componente común proporcional y (ii) el término genérico de 0,28 nmol/mol más la componente común. Declare el supuesto de la variante (i) y la independencia entre ejes.
3. Para ambas variantes, ajuste GGMR de `SRP36=a+b·SRP7` e informe lado a lado `a`, `b`, `u(a)`, `u(b)`, `cov(a,b)`, `χ²_obs`, `ν=10`, crítico 95 % y `P(χ²≤χ²_obs)`.
4. Para 80 y 420 nmol/mol calcule el grado de equivalencia interpolado, propague con `cov(a,b)` y compare con la ec. [3] del protocolo si hubiera mediciones directas en esos niveles.
5. Compare OLS y GGMR con los límites del QAPP: pendiente `1,00±0,01`; intercepto `0±1 ppb` (bilaterales). Separe cumplimiento numérico y significado metrológico.

## Solución de referencia

Los cálculos son reproducibles con `python3 calc_casos.py`; el código usa solo NumPy y la biblioteca estándar.

### 1. OLS y comparación con cifras publicadas

Con los pares ya redondeados de la figura, OLS en orientación de la Figura 14.2 (SRP36→SRP7) da:

| Parámetro | OLS desde pares impresos | QAPP publicado |
|---|---:|---:|
| Intercepto, ppb | 0,180245944 | 0,152088621 (recuadro: 0,15209) |
| Pendiente | 1,001675095 | 1,00169431 (recuadro: 1,00169) |
| `u(a)` | 0,048401674 | 0,050351308 |
| `u(b)` | 0,000118038 | 0,00012279 |
| `cov(a,b)` | −4,32317×10⁻⁶ | −5,24592×10⁻⁹* |
| `R²` | 0,999999861 | 0,99999985 |
| desviación residual, ppb | 0,109616506 | 0,108722272 |

`*` La covarianza publicada `−5,24592×10⁻⁹` no cuadra con `−x̄·u(b)²≈−4,7×10⁻⁶` (correlación implícita `r≈−0,76` con las incertidumbres publicadas). La discrepancia se señala como inconsistencia interna del QAPP, no se corrige inventando una covarianza.

El bloque tipo LINEST tiene `s=0,114028881=√(SSresid/10)`, que sí reproduce `u(b)=0,00012279`; el campo “Res Std Dev” `0,108722272=√(SSresid/11)`. El OLS de los valores impresos da `s=0,109616506`; la comparación apropiada con el s de LINEST es `0,114029`, no `0,108722`.

**Sensibilidad al redondeo:** simulamos 200 000 réplicas independientes con perturbaciones uniformes `U(−0,05; +0,05)` en cada valor impreso de ambas columnas (semilla fija `20261022`; es solo un modelo de redondeo). Las desviaciones simuladas son `SD(a)=0,0180203354` y `SD(b)=0,0000440033`. El intercepto oficial `0,152088621` cae a `−1,563 SD` de la media simulada (percentil 5,957); la pendiente `1,00169431` cae a `+0,431 SD` (percentil 66,539). Esta dispersión muestra que las diferencias OLS son compatibles con el redondeo uniforme supuesto, sin probar que ese fuera el mecanismo real.

Con la orientación didáctica (SRP7→SRP36), los pares impresos dan intercepto `−0,179901408`, pendiente `0,998327568` y desviación residual `0,109433188 ppb`. No se dispone de las lecturas originales, por lo que no se fuerza una coincidencia.

### 2–3. Matrices y dos ajustes GGMR

Para SRP7 (`x`) y SRP36 (`y`), cada covarianza de eje incluye la componente común `u_b²vvᵀ`, con `u_b=2,92×10⁻³`, mientras que el componente aleatorio se pone en la diagonal. En la variante (i), `u_rand=Std. Dev/√12`; suponemos que los Std. Dev impresos describen las 12 lecturas de cada punto y que su media es la magnitud ajustada. En la variante (ii), `u_rand=0,28` para todos los puntos. En ambas `U_xy=0` por hipótesis independiente, pese a la corrida y gas compartidos (véase discusión abajo).

| Resultado `SRP36=a+b·SRP7` | (i) Std. Dev/√12 | (ii) 0,28 nmol/mol |
|---|---:|---:|
| `a`, ppb | −0,184237121 | −0,179922340 |
| `b` | 0,998350748 | 0,998327626 |
| `u(a)`, ppb | 0,031189175 | 0,174759367 |
| `u(b)` | 0,004125035 | 0,004144494 |
| `cov(a,b)` | −3,83046347×10⁻⁶ | −5,77910922×10⁻⁵ |
| `χ²_obs` | 6,318259554 | 0,765027308 |
| `ν` | 10 | 10 |
| `χ²(10; 0,95)` | 18,307038 | 18,307038 |
| `P(χ²≤χ²_obs)` | 0,212146646 | 0,0000496891 (≈5×10⁻⁵) |

En (ii), decir solamente «no se rechaza» omite una señal diagnóstica importante: un χ² observado tan bajo, con probabilidad acumulada ≈`5×10⁻⁵`, indica que la dispersión residual es excepcionalmente pequeña frente a las incertidumbres declaradas; estas sobrestiman la dispersión real bajo el modelo. No prueba invalidez ni autoriza a reducirlas sin más, pero requiere explicar el exceso de incertidumbre. La variante (i) tiene una probabilidad acumulada menos extrema.

### Validación obligatoria de la implementación GGMR

Antes de usar el cálculo para el caso se reprodujo el ejemplo GGMR resuelto de ISO/TS 28037:2010(E), cláusula 10, Tabla 25 (PDF p. 43 / impresa p. 35) y Tabla 26 (PDF p. 44 / impresa p. 36). El ejemplo tiene siete parejas, matrices `U_x`, `U_y` y covarianzas cruzadas nulas. La implementación reproduce, a las cifras impresas, `a=0,3424`, `b=1,0012`, `u(a)=2,0569`, `u(b)=0,0090`, `cov(a,b)=−0,0129` y `χ²_obs=1,772` (ISO). La norma informa `ν=5` y `χ²_crit=11,070`; `1,772<11,070`. **La coincidencia valida la implementación para usarla en este caso.** El script incluye los datos de validación y comprueba esos resultados.

### 4. Grados de equivalencia

El protocolo A, §8, ec. [2], define para mediciones directas `D=x_NS−x_SRP27`; la ec. [3] combina `u(x_NS)` y `u(x_SRP27)` en cuadratura. **La figura QAPP no contiene puntos medidos a 80 ni 420 nmol/mol**, así que aquí no se usa esa fórmula directa para la estimación principal: se interpola con la recta `SRP36=a+b·SRP7` a la concentración nominal exacta `x₀`. Por tanto, `D(x₀)=a+(b−1)·x₀` y `u²(D)=u²(a)+x₀²u²(b)+2x₀·cov(a,b)`. No se añade nuevamente `u_ref`: hacerlo contaría dos veces la referencia ya representada en el ajuste y su matriz `U_x`.

| Variante GGMR | x₀ | D(x₀), ppb | u(D), ppb |
|---|---:|---:|---:|
| (i) Std. Dev/√12 | 80 | −0,316177277 | 0,330547626 |
| (i) Std. Dev/√12 | 420 | −0,876922936 | 1,731866684 |
| (ii) 0,28 nmol/mol | 80 | −0,313712265 | 0,362251261 |
| (ii) 0,28 nmol/mol | 420 | −0,882319448 | 1,735508342 |

Como contraste hipotético, si hubiera mediciones directas y **ambos** SRP tuvieran la misma incertidumbre del modelo SRP27 `u(x)=√(0,28²+(0,00292x)²)`, la ec. [3] daría `u(D)=√2·u(x)`: `0,515691691 ppb` a 80 y `1,779020495 ppb` a 420. Es solo una ilustración condicional, no incertidumbres observadas para SRP 36/SRP 7 ni resultado del QAPP.

### 5. Criterios y discusión OLS/GLS

Con la orientación nacional sobre referencia, OLS da `b=0,998327568`, `a=−0,179901408 ppb`; ambas variantes GGMR tienen `b=0,998340767` / `0,998327626` y `a=−0,179540362` / `−0,179922340 ppb`. Todos quedan dentro del criterio bilateral del QAPP, pendiente `1,00±0,01` e intercepto `0±1 ppb`. El texto extraído como “1.00 + 0.01” y “<+ 1 ppb” pierde el signo ±; se conserva el criterio bilateral descrito en la fuente, no un límite unilateral. El cumplimiento numérico no certifica ni reemplaza el resultado oficial.

## Puntos de discusión

- ¿Qué significa que el SRP7 sea eje de referencia para el taller, si la orientación impresa por el QAPP estima la relación inversa?
- ¿Qué parte de la discrepancia OLS puede atribuirse al redondeo de las parejas y qué dato faltaría para una reproducción exacta?
- ¿Qué cambia en `U` al incluir un sesgo multiplicativo común frente a asumir puntos independientes?
- Asumir independencia entre ejes es una hipótesis fuerte: mismo gas, misma corrida, mismo laboratorio. Una covarianza cruzada altera principalmente las incertidumbres de la diferencia y puede modificar ajuste y χ²; faltan datos para cuantificarla.
- En la variante (ii), `χ²=0,765` y `P(χ²≤χ²_obs)≈5×10⁻⁵` apunta a que las incertidumbres asumidas sobrestiman la dispersión observada; no basta decir “no se rechaza”. Un χ² bajo tampoco prueba equivalencia ni justifica reducir incertidumbres sin evidencia.

## Limitaciones

Los datos experimentales de comparación proceden de un QAPP de EE. UU.; SRP36/SRP7 no son los patrones de CALAIRE. La comparación real no fue evaluada con el modelo SRP27 BIPM aquí aplicado. El modelo de covarianza de ambos ejes, la independencia entre ejes y las incertidumbres SRP27 a 80/420 nmol/mol son adaptación didáctica. Para uso metrológico se deben reemplazar por lecturas sin redondear, certificados, incertidumbres y covarianzas trazables de los SRP 55 y Thermo 49C de CALAIRE, y por el procedimiento vigente del INM.
