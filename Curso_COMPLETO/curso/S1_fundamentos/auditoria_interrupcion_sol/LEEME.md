# S1 — Cambios de sol interrumpidos (reconstrucción para auditoría)

Elaborado por el orquestador (Claude Opus 5.5) el 2026-10-25, tras detener la orquestación a las 19:43 por petición del usuario.

## Qué pasó

La revisión de sección de S1 (paso 4, sol, `logs/S1_4_revision_sol.log`) arrancó a las 19:30. Escribió el «Plan de revisión» en `S1_revision_sol.md`, ejecutó los scripts de `calc/` (salidas `calc/*_salida_sol.txt`) y, entre 19:39 y 19:42, hizo 27 ediciones en los libretos M00–M04 y en `calc/M00_ejemplos.py`. La detuvimos antes de que registrara sus hallazgos y correcciones. Su único razonamiento escrito antes de editar (19:37:55) fue:

> «La revisión encontró problemas que requieren cambios en el contenido: supuestos de independencia incompletos, un ejemplo de autocorrelación sin cálculo y una referencia incorrecta para la incertidumbre de la desviación estándar. También corregiré la comparación entre no rechazo y equivalencia, y completaré las fórmulas operativas que faltan. Las prácticas seguirán siendo únicamente marcadores.»

## Cómo se reconstruyó

La fuente es el registro de la sesión de sol, `~/.claude/projects/-home-w421-w421-calaire-stat/c024f627-1c29-4798-aae3-38e80c4752a1.jsonl`.

1. Las versiones previas se tomaron de las lecturas íntegras que sol hizo de cada archivo antes de su primera edición.
2. Sobre esas versiones se aplicaron, en orden, las 27 ediciones del registro (sin duplicados, respetando las sustituciones globales).
3. El resultado coincide **byte a byte** con los archivos actuales en los seis casos.

El procedimiento está en `reconstruir.py`.

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `M00_libreto.pre_sol.md` … `M04_libreto.pre_sol.md` | libretos tal como los dejó luna tras la revisión Haiku, antes de sol |
| `M00_ejemplos.pre_sol.py` | script antes de la edición de sol |
| `cambios_sol.diff` | diff unificado previo → actual de los seis archivos |
| `reconstruir.py` | procedimiento de reconstrucción y verificación |

## Cambios (C01–C27)

Las horas son locales (−05). La línea indicada es la de la versión previa a sol. Los textos se muestran abreviados; el texto completo está en `cambios_sol.diff`.

| Id | Hora | Archivo | Línea — sección | Tipo | Antes | Después |
|---|---|---|---|---|---|---|
| C01 | 19:39:33 | `M00_libreto.md` | 30 — Nivel B — Conservar cada lectura y su pareja | sustitución | el error con signo se define como indicación menos referencia: $e = y − x$. [prop_e §3] | el error con signo se calcula como indicación menos valor de referencia: $e = y − x$. La GUM permite usar en la práctica un valor convencional de referencia cuando el valor verdadero es desconocido. [GUM B.2.19; prop_e §3, convenc… |
| C02 | 19:39:41 | `M00_libreto.md` | 36 — Nivel B — Conservar cada lectura y su pareja | sustitución | nmol/mol, que en esta aplicación equivale a ppb. [prop_e §3] | nmol/mol; aquí ppb significa una fracción molar de una parte en mil millones. EN 14625 usa esa equivalencia en la nota de su tabla 2. [EN 14625 §8.2, tabla 2, nota] |
| C03 | 19:39:51 | `M00_libreto.md` | 88 — Escena B2. Dato original, valor calculado y corrección trazable | sustitución | > **[PRÁCTICA — fase de ejercicios]** Organizar un conjunto corto del Level 2 y calcular `e` | > **[PRÁCTICA — fase de ejercicios]** Organizar un conjunto corto del Level 2, calcular $e=y-x$, detectar una pareja desplazada y un faltante, y documentar la corrección sin borrar el original. |
| C04 | 19:39:58 | `M00_libreto.md` | 142 — Escena I2. De ancho a largo, sin inventar observaciones | sustitución | Después: `campaña \| analista \| día \| ciclo \| lectura`. | Después: `campaña \| analista \| día \| ciclo \| y (nmol/mol)`. El índice `lectura` se conserva como identificador cuando el diseño contiene varias lecturas por ciclo. |
| C05 | 19:40:05 | `M00_libreto.md` | 144 — Escena I2. De ancho a largo, sin inventar observaciones | sustitución | `ciclo` identifica a qué ciclo pertenece la fila y `lectura` contiene el valor que ocupaba la celda. | `ciclo` identifica a qué ciclo pertenece la fila y `y` contiene la indicación que ocupaba la celda. No reutilizamos `lectura`, que antes definimos como índice, para nombrar una concentración. |
| C06 | 19:40:17 | `M00_libreto.md` | 229 — Referencias del capítulo | sustitución | - **Cálculos ilustrativos.** Conjunto simulado y script de reproducción: | - **GUM.** JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, B.2.19. Archivo: `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of un… |
| C07 | 19:40:25 | `M00_ejemplos.py` | 113 — script | sustitución | tolerancia = 1e-12 | tolerancia = 1e-12 assert len(e_tool_calc) == len(e_tool_python) == 3 assert diferencia_maxima <= tolerancia, "Python y Calc exceden la tolerancia declarada" |
| C08 | 19:40:38 | `M01_libreto.md` | 8 — Ficha del capítulo | sustitución | Ninguno formal para B. I acumula B; A acumula B e I. | M00: parejas, unidades y conservación de originales. I acumula B; A acumula B e I. |
| C09 | 19:40:38 | `M02_libreto.md` | 70 — Escena B4. Elegir entre indicación, error y CV | sustitución | [ASQ, sin numeral] | [ASQ, apéndice C, entrada «coefficient of variation», p. 572] |
| C10 | 19:40:38 | `M03_libreto.md` | 12 — Ficha del capítulo | sustitución | Resolución de 0,1 nmol/mol: valor citado en la propuesta B (M3-B), usado en una ilustración **adaptada**; confirmar con el manual del 49C o el certificado antes de impartir. | Resolución de 0,1 nmol/mol: entrada hipotética **simulada**, no una especificación del 49C ni del SRP. |
| C11 | 19:40:38 | `M04_libreto.md` | 20 — Nivel B — estimar y contrastar una media | sustitución global | [Statistical Concepts | [Hahs-Vaughn |
| C12 | 19:41:28 | `M01_libreto.md` | 66 — Escena B2. El modelo de medición es una función | sustitución | simulamos una transmitancia de 0,9864 y una longitud óptica de 90,0 cm, | simulamos una transmitancia de 0,9864 y una longitud óptica de 90,0 cm, elegidas como pareja de entradas de un trayecto hipotético, no como la transmitancia combinada ni la longitud total del SRP real, |
| C13 | 19:41:28 | `M02_libreto.md` | 62 — Escena B4. Elegir entre indicación, error y CV | sustitución | Las referencias son 80, 80, 200, 200, 420 y 420 nmol/mol; las indicaciones correspondientes son 80,2; 80,1; 199,9; 200,1; 420,3 y 420,1 nmol/mol. | Se mantiene un único nivel nominal de 200 nmol/mol, con dos parejas por día. Las referencias son 199,8; 199,8; 200,0; 200,0; 200,2 y 200,2 nmol/mol; las indicaciones correspondientes son 200,0; 199,9; 199,9; 200,1; 200,5 y 200,3 n… |
| C14 | 19:41:28 | `M03_libreto.md` | 26 — Escena B1. De una repetición a un modelo de probabilidad | sustitución | «La probabilidad de un evento está entre cero y uno. Cero representa un evento imposible dentro del modelo y uno, uno seguro. Si los resultados posibles de un ensayo se describen mediante probabilidades, la suma de las probabilida… | «La probabilidad de un evento está entre cero y uno. Un evento imposible tiene probabilidad cero, pero la recíproca no vale en general: un punto exacto de una variable continua puede tener probabilidad cero sin ser un valor imposi… |
| C15 | 19:41:28 | `M04_libreto.md` | 36 — Escena B1. De la muestra al estimador | sustitución | > **[EJEMPLO]** El vector de errores del ejemplo ilustrativo B es | > **[EJEMPLO]** La unidad independiente es una jornada: se toma una pareja referencia–indicación por jornada en ocho jornadas de un único nivel nominal. Para este ejemplo se suponen errores independientes de una misma población no… |
| C16 | 19:41:52 | `M02_libreto.md` | 64 — Escena B4. Elegir entre indicación, error y CV | sustitución | Si describimos las indicaciones brutas, su desviación estándar muestral es 154,27 nmol/mol. La referencia cambia ampliamente de un par a otro, de modo que esa cifra refleja principalmente que estamos juntando niveles distintos. | Si describimos las indicaciones brutas, su desviación estándar muestral es 0,240 nmol/mol. La referencia cambia ligeramente entre días aun dentro del mismo nivel nominal, y ese movimiento también aparece en las indicaciones. |
| C17 | 19:41:52 | `M03_libreto.md` | 30 — Escena B1. De una repetición a un modelo de probabilidad | sustitución | > **[EJEMPLO]** Modelo simulado: en cada uno de cinco ciclos independientes, la probabilidad de una lectura fuera de banda es 0,1. Sea X el número de ciclos fuera de banda; sus valores posibles son 0, 1, 2, 3, 4 y 5. «Si en cada c… | > **[EJEMPLO]** Modelo hipotético simulado de un ciclo: $X=0$ si la lectura queda dentro de banda y $X=1$ si queda fuera. Se suministran $P(X=0)=0,9$ y $P(X=1)=0,1$. «La variable asigna un número a cada uno de los dos resultados d… |
| C18 | 19:41:52 | `M04_libreto.md` | 90 — Escena I1. Pareadas o independientes: la estructura manda | sustitución | > **[PIZARRA]** Definimos $d_i=A_i-B_i$. Después calculamos $t=\bar d/(s_d/\sqrt n)$, con $n-1$ grados de libertad para la prueba de una media de diferencias. | > **[PIZARRA]** Definimos $\Delta_i=A_i-B_i$; reservamos $d$ para el número de días. Después calculamos $t=\bar\Delta/(s_\Delta/\sqrt n)$, con $n-1$ grados de libertad para la prueba de una media de diferencias. |
| C19 | 19:41:52 | `M01_libreto.md` | 114 — Nivel I — interpretar cambios de escala | sustitución global | [prop_e §3; prop_e §5, M1-I] | [GUM B.2.19–B.2.20; prop_e §5, M1-I, alcance curricular] |
| C20 | 19:42:17 | `M02_libreto.md` | 66 — Escena B4. Elegir entre indicación, error y CV | sustitución | La diferencia entre las dispersiones de $y$ y de $e$ muestra por qué no se deben combinar niveles y días sin conservar la estructura. La referencia explica casi toda la variación amplia de las indicaciones de este ejemplo; no es c… | La diferencia entre las dispersiones de $y$ y de $e$ muestra por qué debemos conservar la referencia de cada pareja incluso en un solo nivel nominal. No atribuimos toda la dispersión de $y$ al fotómetro ni toda su diferencia respe… |
| C21 | 19:42:17 | `M03_libreto.md` | 67 — Escena B2. Distribuciones que aparecen en la fotometría | sustitución | Ejemplo adaptado de resolución total de 0,1 nmol/mol citada en la propuesta B (M3-B); confirmar con el manual del 49C o el certificado antes de impartir. | Segundo ejemplo simulado: se supone una resolución total de 0,1 nmol/mol, sin atribuirla a un instrumento real. |
| C22 | 19:42:17 | `M04_libreto.md` | 96 — Escena I1. Pareadas o independientes: la estructura manda | sustitución | > **[PIZARRA]** $SE(\bar X_1-\bar X_2)=\sqrt{s_1^2/n_1+s_2^2/n_2}$. Los grados de libertad de Welch se calculan con la aproximación de Welch–Satterthwaite; su expresión y sus condiciones quedan en AX.7. En voz alta: «la raíz de la… | > **[PIZARRA]** $SE(\bar X_1-\bar X_2)=\sqrt{s_1^2/n_1+s_2^2/n_2}$; $\displaystyle\nu_W=\frac{(s_1^2/n_1+s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1)+(s_2^2/n_2)^2/(n_2-1)}$. El error estándar es la raíz de la suma de las varianzas estimad… |
| C23 | 19:42:17 | `M01_libreto.md` | 104 — Escena B3. Sensibilidad numérica con una plantilla | sustitución | > **[PRÁCTICA — fase de ejercicios]** Sensibilidad del modelo SRP al cambiar la sección eficaz | > **[PRÁCTICA — fase de ejercicios]** Recalcular tres concentraciones con dos valores de sección eficaz declarados e indicar el signo y la magnitud relativa del cambio. |
| C24 | 19:42:48 | `M01_libreto.md` | 164 — Escena A1. Una entrada compartida puede desaparecer de la diferencia | borrado | Para ver la distinción sin entrar todavía en una fórmula de incertidumbre, volvamos a los resultados $Y_1=2,3 \mathrm{nmol/mol}$ y $Y_2=1,9 \mathrm{nmol/mol}$. En cada resultado absoluto aparece el término común +2,0 nmol/mol. En … | *(eliminado)* |
| C25 | 19:42:48 | `M02_libreto.md` | 68 — Escena B4. Elegir entre indicación, error y CV | sustitución | $s(y)=154,27$ | $s(y)=0,240$ |
| C26 | 19:42:48 | `M03_libreto.md` | 69 — Escena B2. Distribuciones que aparecen en la fotometría | sustitución | La procedencia del valor de resolución se marca como adaptada a la propuesta B (M3-B); no estamos afirmando que esa sea una lectura ni una especificación confirmada del instrumento particular de CALAIRE. Antes de impartir, confirm… | Ambas entradas son hipotéticas y simuladas: no son lecturas ni especificaciones confirmadas de CALAIRE. Una aplicación real necesitaría la resolución documentada del equipo. |
| C27 | 19:42:49 | `M04_libreto.md` | 202 — Referencias del capítulo | sustitución global | §7.5.3 | §7.5.2 |
## Estado y tratamiento

Estos cambios **no están revisados**: sol no los registró ni los justificó. Al reanudar S1, el supervisor (sol) debe:

1. tratar cada C01–C27 como una corrección candidata;
2. conservarla, ajustarla o revertirla (a partir de las versiones `*.pre_sol.*`) con justificación técnica;
3. registrarla en `S1_revision_sol.md` con su hallazgo S-… y la referencia al Cxx.
