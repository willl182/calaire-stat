# Caso C — Historial y control estadístico del Level 2

## Objetivo

Describir pendientes e interceptos de verificaciones de un transfer standard; contrastarlos con criterios publicados; construir cartas de individuales y rango móvil con una serie histórica externa como línea base; evaluar deriva temporal y comparar varianzas con las limitaciones de tamaños muestrales pequeños.

## Módulos que integra

Estadística descriptiva, inferencia t y F, ANOVA (discusión de requisitos), regresión para deriva y cartas de control de individuales/rango móvil.

## Datos y fuentes exactas

### C1 — CALAIRE, seis días de calibración

Fuente: plantilla `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`, hoja `Resumen`. La identificación del equipo indica patrón S/N 55 y equipo S/N 59756-324. Encabezados de fila 4: C=`r`, D=`slope(mi)`, E=`intcpt(Ii)`, F=`lin reg`, G=`Archivo`, H=`Fecha Archivo`, I=`Evaluación Fecha`. Las fórmulas de C6:C11 enlazan a `G20` en las hojas diarias, D6:D11 a `I20`, E6:E11 a `I23` y F6:F11 a `G23`; la tabla contiene valores en caché XML. En C1, `r` es la correlación; D es pendiente de regresión libre; E es intercepto; F es pendiente de la regresión forzada al origen, no una segunda pendiente libre.

| Día | Fecha derivada del nombre de archivo* | `r` (C) | Pendiente (D) | Intercepto ppb (E) | Pendiente forzada al origen (F) | Archivo (G) | Código fecha (H) | Evaluación (I) |
|---:|---|---:|---:|---:|---:|---|---:|---|
| 1 | 2023-02-02 | 0,99999907453234782 | 0,99962735577318051 | −0,096778639149249557 | 0,99932457570192323 | Cal23020200_d1.xls | 23020200 | Correcto |
| 2 | 2023-02-03 | 0,99999940366470053 | 0,99992731624096465 | −0,29650620680328643 | 0,99899713056530859 | Cal23020300_d2.xls | 23020300 | Correcto |
| 3 | 2023-02-06 | 0,99999921714888595 | 0,99953601345442988 | −0,18134704226241638 | 0,99896851920236052 | Cal23020600_d3.xls | 23020600 | Correcto |
| 4 | 2023-02-07 | 0,99999953299820898 | 0,99971961159406775 | −0,21239675590692286 | 0,99905484443470083 | Cal23020700_d4.xls | 23020700 | Correcto |
| 5 | 2023-02-08 | 0,99999974915966938 | 1,000150123768615 | −0,17536496805277579 | 0,99960476366845741 | Cal23020800_d5.xls | 23020800 | Correcto |
| 6 | 2023-02-09 | 0,99999946802130024 | 1,0001313205226094 | −0,17185130143326433 | 0,99959457534432028 | Cal23020900_d6.xls | 23020900 | Correcto |

**Cita de los datos de cada fila:** libro citado, hoja `Resumen`, celdas B6:I11. La fecha ISO está interpretada a partir de la cadena `CalYYMMDD00` de la columna G y coincide con el valor en caché de H; se conserva también el código original. Las fechas no son un dato añadido al libro. Los valores completos se guardan en `datos_caso_C1.csv`.

### C2 — datos publicados, NISTIR 6963

La Tabla 4, p. 20, de Paur et al., *Standard Reference Photometer for the Assay of Ozone in Calibration Atmospheres*, NISTIR 6963 (2003), presenta diez comparaciones SRP-0 contra SRP-2. Se transcriben las columnas impresas: pendiente, desviación estándar de la pendiente, intercepto, desviación estándar del intercepto, `Rsq` y `RSD` (RSD residual en ppb).

| Corrida | Fecha impresa | Pendiente | SD pendiente | Intercepto ppb | SD intercepto ppb | `Rsq` | RSD ppb |
|---|---|---:|---:|---:|---:|---:|---:|
| OZN8127 | 01-Aug | 0,99897 | 0,00032 | −0,197 | 0,091 | 0,9999990 | 0,378 |
| OZN8128 | 03-Aug | 1,00007 | 0,00021 | −0,364 | 0,148 | 0,9999996 | 0,249 |
| OZN8129 | 03-Aug | 0,99997 | 0,00023 | −0,275 | 0,115 | 0,9999995 | 0,275 |
| OZN8133 | 20-Aug | 1,00041 | 0,00036 | −0,239 | 0,111 | 0,9999987 | 0,421 |
| OZN8134 | 20-Aug | 0,99996 | 0,00024 | −0,002 | 0,035 | 0,9999994 | 0,279 |
| OZN8135 | 21-Aug | 1,00026 | 0,00023 | 0,077 | 0,046 | 0,9999995 | 0,264 |
| OZN8138 | 26-Aug | 1,00071 | 0,00023 | −0,009 | 0,034 | 0,9999995 | 0,265 |
| OZN8139 | 27-Aug | 1,00073 | 0,00020 | −0,248 | 0,107 | 0,9999996 | 0,235 |
| OZN8140 | 27-Aug | 1,00013 | 0,00022 | −0,048 | 0,038 | 0,9999995 | 0,260 |
| OZN8141 | 29-Aug | 0,99910 | 0,00018 | −0,003 | 0,027 | 0,9999997 | 0,214 |

**Cita de cada fila:** NISTIR 6963, Tabla 4, PDF p. 20; también `datos_caso_C2.csv`. `rsd_ppb` representa la columna `RSD` impresa por NIST (desviación estándar residual de la regresión, en ppb), no el RSD relativo en porcentaje. La fuente muestra día y mes, no se agrega año a las fechas de corrida.

### Criterios y referencias para las cartas

- QAPP, §6.2.3, PDF p. 18 / Element 6, p. 2 of 4, describe la verificación 6×6: seis comparaciones en días distintos, seis concentraciones cada una. Tabla 7-1, PDF p. 23 / Element 7, p. 3 of 4, publica los criterios “RSD of six slopes 3.7%”, “Std. Dev. of 6 intercepts 1.5”, “Slope of 1.00 +/- 3%” e “Intercept of 0 +/- 3 ppb”. No se imprime unidad para el 1.5 de los interceptos; se interpreta como ppb por contexto, manteniendo explícita esta ambigüedad. En Tabla 7-1, el término RSD está ligado a las seis pendientes; para C1 reportamos `100·s/|media|` como convención de cálculo de taller.
- EPA TAD, *Transfer Standards for Calibration of Air Monitoring Analyzers for Ozone*, EPA-454/B-22-003 (2023), Tabla 4-1, PDF p. 33 / impresa p. 19, y §4.4.1, PDF p. 36 / impresa p. 22: reemplaza ese diseño por tres ciclos de verificación, con tres pendientes y tres interceptos; no son los mismos criterios 6×6 del QAPP.
- *Introduction to Statistics in Metrology*, cap. 11, §11.2 (en particular §11.2.2, PDF p. 3 / impresa p. 273), `docs/intro_stats_metro_c11.pdf`, apoya `σ̂=MR̄/1,128` y cartas X-MR. Para límites de 3σ se usan los factores usuales de n=2: `2,66`, `D₃=0`, `D₄=3,267`, dentro del enfoque de cartas X-MR tratado en §11.2 y Otto, cap. 9 (Tabla 9.1, PDF p. 353 / impresa p. 349, presenta límites para carta de rango). No se usan los factores distintos de 95% de Otto, Tabla 9.2.

## Enunciado para el estudiante

1. Calcule media, desviación estándar muestral, mínimo y máximo de pendiente e intercepto en C1 y C2. En C2 explique `RSD`/`rsd_ppb`.
2. Evalúe C1 frente al diseño QAPP de verificación 6×6 y sus criterios. Distinga esos requisitos de la verificación EPA TAD de tres ciclos; aplique los límites TAD a C1/C2 solo como contraste orientativo.
3. Construya cartas X-MR de pendiente e intercepto con C2 como línea base. Use límites de individuales `media±2,66·MR̄` (`σ̂=MR̄/1,128`) y rango móvil `LIC=D₃MR̄=0`, `LSC=D₄MR̄=3,267MR̄` para n=2. Ubique los valores de C1 frente a los límites.
4. Ajuste la pendiente de C2 contra el orden 1–10. Pruebe si la pendiente de la regresión es distinta de cero con t al 5 % bilateral.
5. Contraste las varianzas muestrales de las pendientes C1 y C2 con F bilateral al 5 %. Informe grados de libertad y explique los límites del contraste.
6. Discuta si estos datos permiten fijar un intervalo de recalibración para el Level 2 de CALAIRE. Identifique los datos adicionales que recogería.

## Solución de referencia

Ejecute `python3 calc_casos.py` para reproducir todos los valores. En la descriptiva se usa desviación estándar muestral (`ddof=1`); para contrastar con el resumen de NIST también se informa la desviación poblacional (`ddof=0`), que es la que reproduce los números redondeados mencionados en el planteamiento.

### 1. Estadística descriptiva

| Serie | Variable | Media | s muestral | Mínimo | Máximo |
|---|---|---:|---:|---:|---:|
| C1 (n=6) | Pendiente | 0,999848624 | 0,000260899 | 0,999536013 | 1,000150124 |
| C1 (n=6) | Intercepto, ppb | −0,189040819 | 0,065035870 | −0,296506207 | −0,096778639 |
| C2 (n=10) | Pendiente | 1,000031000 | 0,000592386 | 0,998970000 | 1,000730000 |
| C2 (n=10) | Intercepto, ppb | −0,130800000 | 0,150109442 | −0,364000000 | 0,077000000 |
| C2 (n=10) | RSD residual, ppb | 0,284000000 | 0,064613380 | 0,214000000 | 0,421000000 |

El resumen de pendientes e interceptos proporcionado para contraste (media pendiente `1,00003`, s `0,00056`; media intercepto `−0,131 ppb`, s `0,142 ppb`; residual `0,284 ppb`) coincide tras redondeo con la media y desviación **poblacional** de las diez filas de NIST: pendiente `1,00003100`, sigma `0,00056199`; intercepto `−0,130800`, sigma `0,142406`; residual medio `0,284000`. La dispersión muestral se conserva arriba para inferencia.

### 2. Criterios de verificación: QAPP frente a EPA TAD

El diseño CALAIRE descrito para C1 —un Level 2 contra SRP en seis días— corresponde al QAPP **initial 6×6** (§6.2.3; Tabla 7-1), no a las verificaciones de tres ciclos de la TAD. El QAPP requiere seis comparaciones completas (seis concentraciones) en días diferentes. C1 tiene seis pendientes/interceptos diarios: `RSD` de pendientes calculado como `100·s/|media|` = `0,0260939 %`, menor que `3,7 %`; la desviación estándar de los seis interceptos es `0,065035870 ppb`, menor que `1,5` si la unidad tácita se interpreta como ppb; cada pendiente cumple `1,00±3 %` y cada intercepto `0±3 ppb`. C1 satisface numéricamente estos criterios QAPP; la condición de 1,5 conserva la ambigüedad de unidad tal como está impresa.

La EPA TAD 2023 **no conserva el 6×6 como su criterio vigente**: Tabla 4-1 y §4.4.1 especifican tres ciclos estables, cada pendiente dentro de `1,00±0,03`, intercepto `0±3 ppb`, `SD(pendientes)<0,0075` y `SD(interceptos)<1,00 ppb`. Esos límites corresponden a tres regresiones de una verificación según el TAD; por tanto C1 (seis días) y C2 (diez corridas externas) no son verificaciones TAD de exactamente tres ciclos. El TAD define `SD=√((1/3)·Σ(mᵢ−m̄)²)` y la misma forma para interceptos (ecs. 8–9, Apéndice, p. A-5): es la desviación con divisor N, y el 3 aparece porque una verificación tiene N = 3 regresiones. Aplicada con N = 6 y N = 10 a los grupos completos, como comparación orientativa, da: `SD_TAD` de pendientes C1=`0,000238167`, C2=`0,000561987`; de interceptos C1=`0,059369355 ppb`, C2=`0,142406320 ppb`. Los valores de C2 coinciden con las desviaciones que publica el NIST (0,00056 y 0,142), que usa la misma forma con divisor N. Todas quedan numéricamente bajo los límites, y los rangos individuales también caen dentro de los límites, pero esto no constituye una evaluación formal TAD. Para comparación, la desviación muestral usual (divisor N − 1) es: pendientes C1=`0,000260899`, C2=`0,000592386`; interceptos C1=`0,065035870`, C2=`0,150109442 ppb`. Punto de discusión para la clase: con N pequeño, elegir N o N − 1 cambia la cifra; hay que declarar siempre cuál se usó.

C1 se contrasta directamente con el diseño 6×6 del QAPP; C2 solo sirve de contraste estadístico histórico, pues reúne SRP-0/SRP-2 de EE. UU., no un Level 2 CALAIRE.

### 3. Cartas X-MR (valores calculados)

Fórmulas: `MRᵢ=|xᵢ−xᵢ₋₁|`; `MR̄=media(MRᵢ)`; `σ̂=MR̄/1,128`; límites individuales `X̄±2,66·MR̄` (equivalente a 3σ); rango móvil `LIC=D₃MR̄=0`, `LSC=D₄MR̄=3,267MR̄` para n=2. Los límites de referencia son didácticos: se estiman con solo diez C2 puntos externos, por lo que no constituyen límites operativos de CALAIRE.

| Variable | Centro `X̄` C2 | `MR̄` C2 | `σ̂` | Límites X (LIC, LSC) | Límites MR (LIC, LSC) |
|---|---:|---:|---:|---:|---:|
| Pendiente | 1,000031 | 0,000498889 | 0,000442277 | (0,998703956; 1,001358044) | (0; 0,001629870) |
| Intercepto, ppb | −0,130800 | 0,130888889 | 0,116036249 | (−0,478964444; 0,217364444) | (0; 0,427614000) |

Los diez puntos C2 y los seis valores individuales C1 quedan dentro de los límites X. Los cinco MR de C1, en orden de fecha, son para pendiente `0,000299960; 0,000391303; 0,000183598; 0,000430512; 0,000018803`, y para intercepto `0,199727570; 0,115159160; 0,031049710; 0,037031790; 0,003513670`. **Los cinco rangos móviles de ambas variables están entre 0 y el LSC**; en particular, el quinto MR no señala nada porque el límite inferior es cero y no hay MR negativo. No hay señal en la carta MR de C1 bajo los límites 3σ especificados.

La superposición es matemática, no una carta de control legítima para CALAIRE: C2 proviene de dos SRP de EE. UU. y de una campaña/escala distinta; C1 es Thermo 49C S/N 59756-324 frente al SRP55 en febrero de 2023. Además, la carta se basa en resúmenes de regresión por corrida y no en observaciones homogéneas de un único proceso estable. Se requieren límites propios para uso operativo.

### 4. ¿Hay deriva en C2?

Regresión OLS de pendiente sobre el orden de corrida `1…10`:

- intercepto de la tendencia: `0,999811333`;
- cambio estimado por corrida: `3,99394×10⁻⁵` unidades de pendiente/corrida;
- error estándar del cambio: `6,77192×10⁻⁵`;
- `t=0,589779`, `gl=8`;
- crítico bilateral 95 %: `t(8;0,975)=2,306004`.

Como `|t|<2,306004`, no se detecta una tendencia lineal estadísticamente significativa al 5 %. El orden es solo un sustituto temporal: fechas repetidas y ausencia de año/intervalos homogéneos hacen impropio interpretar esa pendiente como deriva por día o por mes.

### 5. Prueba F para varianzas de pendientes

`s²_C1=6,80682171×10⁻⁸`, `s²_C2=3,50921111×10⁻⁷`; el cociente mayor/menor es `F=5,155433`, con `gl₁=9` (C2, varianza mayor) y `gl₂=5` (C1). Para prueba bilateral al 5 %, el crítico superior es `F(0,975;9,5)=6,681054`. Dado que `5,155433<6,681054`, no se rechaza igualdad de varianzas al 5 %. Los cuantiles se calculan por integración numérica en el script; no mantengo la cita a “Brereton, Apéndice A.3”, que no pude verificar contra una copia local inequívoca de esa obra y edición.

La prueba tiene poca potencia con n=6 y n=10 y depende de normalidad e independencia. Más importante, C1 y C2 no representan poblaciones comparables (diferentes instrumentos, cadena de trazabilidad y época), por lo que el resultado F es un ejercicio de inferencia, no una conclusión sobre estabilidad relativa del Level 2.

### ANOVA y periodicidad

No se calcula un ANOVA de componentes entre días/runs: solo hay un resumen de pendiente e intercepto por día o corrida, sin réplicas homogéneas suficientes dentro de cada grupo para estimar por separado variación intra- e inter-corrida. Para ANOVA se necesitan resultados repetidos comparables (p. ej., múltiples calibraciones independientes por fecha/ciclo), con protocolo y condiciones registrados.

Estos datos **no sostienen un intervalo de recalibración de CALAIRE**. C1 cubre seis días consecutivos y C2 no es el Level 2 de CALAIRE. Un intervalo normativo de referencia no debe confundirse con un intervalo inferido: la Tabla 4-1 EPA indica verificación anual para Level 2 contra Level 1, pero la periodicidad aplicable al laboratorio designado debe confirmarse con el QAPP/SOP y requisitos del INM. Para estimar intervalo propio: acumular verificaciones periódicas repetidas de Thermo 49C vs SRP55 durante varios ciclos/años; conservar lecturas primarias y réplicas, pendientes/interceptos/errores y covarianzas; documentar ajustes, mantenimiento, operador, condiciones y fechas; incluir verificaciones intermedias independientes y criterios de acción; fijar límites de control con un periodo base homogéneo y suficiente.

## Puntos de discusión

- Una carta controla un proceso de medición estable; no convierte datos históricos de otro instrumento en límites válidos para CALAIRE.
- La correlación `r` próxima a uno y el R² elevado describen ajuste lineal, no descartan deriva o sesgo metrológico.
- La prueba F y el test t tienen poca potencia con tamaños muestrales pequeños; “no significativo” no demuestra equivalencia de varianzas ni ausencia de deriva.
- El uso de la desviación poblacional reproduce el resumen NIST redondeado; para inferencia se usa la desviación muestral.
- Las comparaciones deben conservar orientación de los ejes, incertidumbres, correcciones y registros del patrón de referencia.

## Limitaciones

C2 son datos publicados de EE. UU. (SRP-0/SRP-2) y no describen el Thermo 49C de CALAIRE. C1 es un extracto de una sola plantilla/calibración de seis días; no es un historial de largo plazo. Las cartas superpuestas y las pruebas C1-C2 son didácticas, con procesos diferentes. No se inventa una fecha anual para C2 ni se prescribe un intervalo del Level 2 sin serie propia. Para decisiones del laboratorio se deben sustituir los datos externos por verificaciones CALAIRE trazables al SRP55 y cumplir los procedimientos vigentes del INM.
