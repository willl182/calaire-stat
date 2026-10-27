# M04 — revisión de prácticas (haiku)

Revisor: Claude Haiku 5.5. Alcance: prácticas `[PRÁCTICA]` de `curso/S1_fundamentos/M04_libreto.md` (B: líneas 72–84; I: 190–208; A: 252–266), `curso/S1_fundamentos/calc/M04_practicas_luna.py` y `curso/logs/M04_practicas_luna.md`. No se editaron libretos ni scripts. No se auditaron referencias.

## Verificaciones ejecutadas

- `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M04_practicas_luna.py` termina con código 0 e imprime `comprobaciones_practicas_M04=OK`.
- Todas las cifras de las soluciones coinciden con la salida del script: B (media 0,0375; s 0,5263; se 0,1861; IC95 [−0,4025; 0,4775]; t 0,2015; p 0,8460); pareada (0,1625; 0,1188; 0,0420; t 3,8697; p 0,0061); Welch (diferencia −0,9405; se 0,1531; gl 10,9272; t −6,1418; p 0,0000750); chi-cuadrado (0,2770; IC [0,1211; 1,1473]; χ² 7,7550; p 0,7094); F (0,8408; IC [0,1404; 5,8669]; p 0,8678); potencia (33,37 → 34; potencia 16 = 0,4649; 25,52 → 26; potencia 12 = 0,4658); u(s) 0,1407 (la solución escribe 0,1407 ✓); G 2,4374 y Q 0,8214; Bonferroni (0,036; 0,093; 0,600); TOST (IC90 [−0,0747; 0,2347]; t 4,2485, p 0,000217; t −2,4597, p 0,01183); χ² Q 2,33, p 0,5068.
- Críticos contra la fuente citada (Otto, `docs/Chemometrics Statistics and Computer Application.pdf`): Tabla 2.11, T(0,99; 8) = 2,22 ✓. Tabla 2.10, Q(0,99; 8) = 0,59 ✓. Grubbs bilateral a 0,01 con n = 8 calculado = 2,2744 ✓ (coincide con la cifra del libreto).
- Diferencias pareadas del apartado 1 reproducidas: [0,2; 0,2; 0,2; −0,1; 0,2; 0,2; 0,1; 0,3] ✓.
- Valor p del contraste frente a cero en A (t = 0,8944, gl 19): 0,382 ✓.
- Decimal: en el texto y en las soluciones se usa coma; el punto aparece solo en código Python y en la sintaxis de `$...$` de LaTeX. ✓
- Alcance frente a prop_e §M4: B (intervalo t, contraste, unidad justificada, magnitud relevante), I (t pareada/Welch, varianzas χ²/F, potencia por diseño, u(s), Grubbs/Dixon con condiciones) y A (multiplicidad, TOST, χ² conjunto) están cubiertos. Ninguna práctica exige gráficos; no hace falta dataviz. No se borra ningún dato. ✓
- Diff de `M04_libreto.md` frente a HEAD: los cambios fuera de los tres bloques son solo sustituciones de citas en los párrafos de Welch (líneas 106–114). No los auditó esta revisión: son ediciones del supervisor de referencias.

## Hallazgos

### H-01 — Severidad alta — las prácticas repiten los ejemplos resueltos

- **Ubicación:** prácticas en `M04_libreto.md` L72–84 (B), L190–208 (I) y L252–266 (A). Ejemplos con los mismos datos y las mismas cifras: L36 (B), L104 (pareada), L112 (Welch), L124 y L130 (χ² y F), L166 (potencia), L184 (extremos), L222 (Bonferroni), L234–236 (TOST), L246 (χ²).
- **Problema:** los vectores de cada práctica son idénticos a los del ejemplo que la precede, y cada solución docente repite los resultados ya dados. Por ejemplo: el apartado 4 de I reproduce 33,37 → 34, 0,4649, 25,52 → 26 y 0,4658 de L166; el apartado 5 reproduce G = 2,4374 y Q = 0,8214 de L184. Un operador puede copiar la solución sin hacer el cálculo. Así no se cumple el requisito de prop_e de «práctica evaluable» (resolver un apartado distinto para cada familia).
- **Escenario:** el alumno lee L104 («Obtenemos ocho diferencias, con media 0,1625…») y luego el apartado 1 de I con los mismos datos, y lo reporta sin cálculo.
- **Corrección propuesta:** dejar los ejemplos como demostración resuelta y generar vectores nuevos (fijos y declarados en el script) para cada práctica: nuevos pares en B, nuevas diferencias y grupos en I, otra muestra para χ²/F, otros parámetros de potencia, otro vector de extremos y otros p-valores y residuos en A. Hay que recalcular las soluciones y añadir esas cifras al script.

### H-02 — Severidad alta — la bitácora y la solución del apartado 4 afirman comprobaciones que el script no hace

- **Ubicación:** `M04_libreto.md` L202–204 (solución del apartado 4 de I: «La ejecución contrasta potencia con la distribución t no central de SciPy y los resultados pareados/Welch con funciones independientes de SciPy»); `M04_libreto.md` L262 (solución de A: «se comprueba la forma matricial diagonal»); `curso/logs/M04_practicas_luna.md` L17 («potencia recalculada con t no central y forma matricial diagonal del estadístico conjunto»).
- **Problema:** en `calc/M04_practicas_luna.py` no aparece `scipy.stats.nct` ni `ttest_rel` ni `ttest_ind(equal_var=False)`. La pareada y Welch se calculan con las mismas fórmulas manuales que la solución, así que no hay verificación independiente. Tampoco hay forma matricial: `qstat=np.sum((res/u)**2)` es la suma escalar. La bitácora afirma comprobaciones que no existen.
- **Escenario:** un revisor que lea la bitácora espera ver potencia recalculada con `nct`. Al ejecutar el script no la encuentra y no puede confirmar lo declarado.
- **Corrección propuesta:** o bien añadir al script (a) la potencia por `scipy.stats.nct` comparada con `TTestPower`/`TTestIndPower`, (b) `stats.ttest_rel` y `stats.ttest_ind(..., equal_var=False)` para comparar con las fórmulas manuales, y (c) `Q = r^T V^{-1} r` con V = diag(u²) para comparar con la suma escalar; o bien eliminar esas frases del libreto y de la bitácora.

### H-03 — Severidad media — falta la rúbrica por apartado exigida por prop_e (I)

- **Ubicación:** `M04_libreto.md` L204–208, bloque I, y `curso/logs/M04_practicas_luna.md`.
- **Problema:** prop_e §M4 I pide que la rúbrica «registre método, supuestos, resultado e interpretación por apartado». El bloque I tiene un único «Criterio de logro» global. No hay criterio por apartado (1 a 5) ni se distingue método, supuestos, resultado e interpretación.
- **Corrección propuesta:** añadir un criterio por apartado con esas cuatro columnas, o una tabla de rúbrica bajo la solución del bloque I.

### H-04 — Severidad media — el crítico de Dixon para n = 8 usa la variante de rango completo

- **Ubicación:** `M04_libreto.md` L184 y L192 (extremos, apartado 5); `calc/M04_practicas_luna.py` L47–49.
- **Problema:** el estadístico es Q = (x_n − x_{n−1})/(x_n − x_1). Otto (tabla 2.10) lo tabula con n = 8 y da Q = 0,59 a 0,99; la cifra coincide con la fuente citada, así que el libreto es fiel a Otto. Pero en las tablas de Dixon más usadas (ASTM E178 y similares), la variante de rango completo se aplica solo para n de 3 a 7; para n de 8 a 10 se usa r11 = (x_n − x_{n−1})/(x_n − x_2). Aquí r11 = 0,8519, que sigue superando el crítico, así que la conclusión no cambia. El problema es de método y de fuente, no de cifra: el alumno podría aplicar un crítico de tabla a un estadístico distinto del tabulado en la norma.
- **Corrección propuesta:** declarar explícitamente la variante y la tabla («según Otto, tabla 2.10, rango completo»), o usar r11 con su crítico de la norma y mencionar la diferencia. Esto requiere cotejo con una segunda fuente; no lo verifiqué contra la norma original, solo contra Otto.

### H-05 — Severidad baja — el script evalúa el margen con IC90 y el libreto habla de IC95

- **Ubicación:** `calc/M04_practicas_luna.py` L16–19 (`ci90` y `descarta_magnitud`) frente a `M04_libreto.md` L76 y L202 (la tarea y la solución usan el intervalo del 95 %).
- **Problema:** la comprobación de «descarta ±0,30» del script usa el IC90, pero la solución cita el IC95. Ambos incluyen ±0,30, así que el resultado coincide, pero la cifra verificada no es la que se enuncia.
- **Corrección propuesta:** calcular también el IC95 y reportar `descarta_magnitud` para ambos niveles, o cambiar la tarea a «IC90 con regla de equivalencia» de forma explícita.

### H-06 — Severidad baja — frase obsoleta en el bloque B

- **Ubicación:** `M04_libreto.md` L70: «La práctica correspondiente se desarrollará en la fase de ejercicios».
- **Problema:** la práctica ya está en el libreto (L72). La frase contradice el contenido. El índice `S1_00_indice.md` L83 todavía dice «[PRÁCTICA — fase de ejercicios]», pero está fuera del alcance de este revisor.
- **Corrección propuesta:** sustituir la frase por una remisión a la práctica siguiente.

### H-07 — Severidad baja — redacción confusa sobre la incertidumbre de s

- **Ubicación:** `M04_libreto.md` L172, escena I4.
- **Problema:** «La GUM la da para la desviación del promedio; como esta es s/√n y n es fijo, su incertidumbre relativa es la misma que la de s» mezcla la desviación del promedio con la desviación muestral. La relación u(s) ≈ s/√(2ν) se refiere a s de una serie. La fórmula es correcta, pero el razonamiento no lo muestra.
- **Corrección propuesta:** reescribir la frase para decir que E.4.3 da la incertidumbre relativa de s, y que s/√n no interviene en esa expresión.

### H-08 — Severidad baja — referencia a G*Power sin contenido en el texto

- **Ubicación:** `M04_libreto.md` L150: «el planteamiento de planificación por software también se ilustra con G*Power en el texto».
- **Problema:** en M04 no hay ninguna ilustración con G*Power. La frase promete un contenido ausente.
- **Corrección propuesta:** eliminar la mención o añadir la ilustración.

## Observaciones fuera de alcance

- Las ediciones de citas en Welch (L106–114) están fuera de los bloques de práctica. Son del supervisor de referencias y no las he auditado. Conviene que ese supervisor sepa que tocan párrafos del cuerpo, no solo las referencias.

## Conclusión

Las cifras son correctas y reproducibles; el script corre sin error. Los hallazgos principales son de diseño didáctico (H-01: las prácticas no son nuevas) y de trazabilidad (H-02: la bitácora declara verificaciones que no existen). Antes de cerrar M04, H-01 y H-02 deben resolverse; H-03 a H-08 son correcciones menores.
