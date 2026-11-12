# M03 — revisión de prácticas B, I y A (haiku)

Fecha: 2026-10-27. Revisor: Haiku 5.5. Alcance: `curso/S1_fundamentos/M03_libreto.md` (bloques de práctica), `curso/S1_fundamentos/calc/M03_practicas_luna.py` y `curso/logs/M03_practicas_luna.md`. No se editaron libretos, scripts ni bitácoras de otros autores. No se auditaron referencias.

## Verificación ejecutada

- `curso/.venv/bin/python curso/S1_fundamentos/calc/M03_practicas_luna.py`: rc=0, imprime `comprobaciones_M03_practicas=OK`. Las aserciones pasan, pero cubren solo una parte de las cifras del libreto (ver H-01 y H-06).
- Cálculo independiente (`/tmp/chk_m03.py`, ejecutado con `-I`) de cifras del texto:
  - Chi-cuadrado IC 95 %: [0,00312; 0,04812] — coincide.
  - F IC 95 %: [0,5597; 28,586] — coincide.
  - Puntos de Blom para n = 6: ±1,2816; ±0,6433; ±0,2019 — el texto no los lista (ver H-04).
  - Autovalores de la matriz de correlaciones 3×3: 0,4069; 0,75; 1,8431 — coincide con 0,407; 0,750; 1,843.
  - Correlación de retardo uno del ejemplo A2 (12 contra 12 valores): 0,5 — coincide, pero no se reproduce en el script de práctica (ver H-06).
  - Razón de canales sin covarianza: u = 0,53125 — **no** coincide con 0,50583 (ver H-02).
- Coinciden: u rectangular 0,1732; u resolución 0,02887; u(U/k) 0,300; u media iid 0,200; u media con común 0,3606; media global 420,375; diferencia de mitades 0,400; medias de bloque 420,075 / 420,275 / 420,475 / 420,675; covarianza 0,36; u(Δ) 1,000 y 0,5292; χ² = 4,000; F = 4,000; u(R) con covarianza 0,40625; u(x₂−x₁) 3,000 y 4,123; autovalores de V_canales 0,02595 y 0,10405; autovalores de V_puntos 0 y 17; autovalores de la matriz inválida −0,2 y 2,2; correcciones a t₀ = 0 dan 420,000 en los cuatro bloques.
- Convención: sin números con punto decimal en prosa de las prácticas. Unidades nmol/mol correctas. "SRP 55" es nombre consistente con el resto del curso.

## Hallazgos

### H-01 — Mayor — reproducibilidad del gráfico de probabilidad
- **Ubicación:** `calc/M03_practicas_luna.py:45-47`; enunciado de I en `M03_libreto.md:214`.
- **Problema:** el enunciado pide puntos de probabilidad para **seis** errores (`[-0,10; 0; 0,10; -0,10; 0; 0,10]`) con posiciones de Blom. El script usa un vector distinto de **siete** valores (`[-0,12; -0,07; -0,03; 0,00; 0,02; 0,05; 0,09]`), que no aparece en el libreto. Además, los cuantiles teóricos se obtienen de una muestra simulada de 300 000 normales con semilla fija (`np.quantile(...)`), no de `norm.ppf` en las posiciones de Blom; por eso dan −1,3674 y 1,3629 en lugar de los de Blom para n = 7 (±1,3645 en los extremos; la práctica usa n = 6, con extremos ±1,2816). El script no reproduce la solución del libreto.
- **Corrección propuesta:** sustituir las líneas 46-47 por `p = (np.arange(1,7)-0.375)/(6+0.25)`, `teo = norm.ppf(p)` (importar `norm` de `scipy.stats`) y `obs = np.sort([-0.10,-0.10,0,0,0.10,0.10])`. Añadir `assert` que compruebe los seis pares. En el libreto, listar en la solución docente los seis pares (cuantil, error) con dos decimales.

### H-02 — Mayor — cifra incorrecta en la solución de A
- **Ubicación:** `M03_libreto.md:340` (solución docente de la práctica A).
- **Problema:** el texto escribe «Si se omite la covarianza, resulta u(R)=√0,255859 = 0,50583». Con sensibilidades 1,25 y −1,5625 y varianzas 0,04 y 0,09, la suma sin término cruzado es 0,0625 + 0,219727 = 0,282227; por tanto u(R) = **0,53125**. La cifra 0,255859 no corresponde a ningún cálculo del ejemplo. La conclusión cualitativa (la covarianza cambia el resultado: 0,406 frente a 0,531) se mantiene, pero el número es erróneo y el script no lo comprueba: la única aserción sobre la razón es la versión con covarianza.
- **Corrección propuesta:** en `M03_libreto.md:340` cambiar «√0,255859 = 0,50583» por «√0,282227 = 0,53125». En el script añadir `u_ratio_sin_cov = sqrt((0.2/0.8)**2 + (0.3/0.8**2)**2)` con `assert np.isclose(u_ratio_sin_cov, 0.53125)` e imprimirlo.

### H-03 — Mayor — la práctica I excede el alcance de M3 y contradice el propio libreto
- **Ubicación:** enunciado y solución de I en `M03_libreto.md:214-220`; la advertencia está en `M03_libreto.md:188`.
- **Problema:** el libreto dice en la línea 188 «No vamos a ejecutar aquí pruebas de hipótesis sobre varianzas; eso corresponde a M4-I». Sin embargo, la práctica pide calcular el estadístico χ² «para contrastar la varianza de referencia 0,010» y un intervalo del 95 % de la varianza, además del intervalo central de F. Según `prop_e.md` (M3-I), la práctica evaluable de M3 es «calcular la incertidumbre de una diferencia con y sin covarianza»; los intervalos y pruebas sobre varianzas (χ², F) están en M4-I. Esto convierte la práctica en una mezcla de M3 y M4 y hace que la solución docente incluya inferencia no evaluable en M3.
- **Corrección propuesta:** eliminar del enunciado y la solución de I el contraste y el intervalo χ² y el intervalo de F, dejando solo la descripción de su distribución (ya en la escena I2) o trasladándolos a M4-I. Si se quiere conservar el cálculo de la varianza muestral de los seis errores como dato de partida, mantenerlo sin contraste ni intervalo. En el script, retirar `chi_stat`, `chi_interval`, `f_stat` y `f_interval` (líneas 36-44) con sus aserciones e impresiones, o moverlos a un script de M4.

### H-04 — Mayor — solución de I no verificable: faltan los puntos de probabilidad
- **Ubicación:** `M03_libreto.md:222` (solución docente de I) y criterio de logro en `M03_libreto.md:226`.
- **Problema:** el criterio exige «genera los puntos de probabilidad», pero la solución solo describe el procedimiento («se ordenan… se asocian a cuantiles… calculados en las posiciones de Blom»). No da los seis pares, así que un operador no puede comprobar su resultado. Lo mismo ocurre con la escala de cuantiles.
- **Corrección propuesta:** añadir en la solución los seis pares, con dos decimales: (−1,28; −0,10), (−0,64; −0,10), (−0,20; 0), (0,20; 0), (0,64; 0,10), (1,28; 0,10). Se verifican con `norm.ppf` de las posiciones (i−0,375)/6,25. Ver la corrección de H-01.

### H-05 — Mayor — no se entrega la salida gráfica que la práctica pide
- **Ubicación:** `M03_libreto.md:214` y `:222` (la práctica pide construir puntos «de un gráfico de probabilidad» y describe «se representa cuantil teórico en el eje horizontal…»); `curso/logs/M03_practicas_luna.md:13` (la bitácora dice «no se crea salida gráfica separada»).
- **Problema:** `prop_e.md` incluye «gráficos de probabilidad» en el contenido de I, y la práctica describe la construcción de un gráfico con ejes definidos. La bitácora decide no producir figura, y el libreto no tiene una salida reproducible. Según la instrucción del encargo, si el alcance exige gráficos hay que preparar datos, tarea de trazado y salida gráfica reproducible; no se debe omitir por simplificación.
- **Corrección propuesta:** o bien (a) añadir al script una salida gráfica reproducible del gráfico de probabilidad (PNG o HTML) con los seis pares de H-04, ejes «cuantil normal teórico» y «error observado (nmol/mol)», marcas distintas y leyenda, y citarla en el libreto; o bien (b) si el responsable decide que el gráfico no es obligatorio, reescribir la frase de la solución para que diga «puntos para trazar» y registrar esa decisión en la bitácora. En cualquier caso, aplicar la habilidad `dataviz` para paleta y accesibilidad antes de generar la figura.

### H-06 — Menor — el script no reproduce el ejemplo de autocorrelación y calcula un valor sin uso
- **Ubicación:** `calc/M03_practicas_luna.py:48-50` (`serie` de 8 valores, `I_corr_serie_lag1=0,9897`); la cifra 0,5 de A2 está en `M03_libreto.md:292-294` y solo se reproduce en `calc/M03_ejemplos.py:78-96`.
- **Problema:** el valor impreso como `I_corr_serie_lag1` (0,9897) no aparece en el libreto; el valor del libreto (0,5 sobre 12 pares) no se calcula en el script de prácticas. La bitácora afirma «Reproduce todos los cálculos de las prácticas», lo cual es incorrecto.
- **Corrección propuesta:** eliminar las líneas 48-50 y su impresión, o sustituirlas por la secuencia de 13 valores del libreto y su correlación de 0,5, con aserción. Corregir la afirmación de la bitácora a «reproduce las cifras de los bloques de práctica; el ejemplo de A2 se reproduce en M03_ejemplos.py».

### H-07 — Menor — la práctica B no evalúa las distribuciones que prop_e lista para B
- **Ubicación:** `M03_libreto.md:124-140`; alcance en `prop_e.md` (M3-B: «normal, rectangular y triangular»; «distribución t, cuantiles y grados de libertad»).
- **Problema:** la práctica B cubre la rectangular y la de resolución, pero no pide ni la normal ni la triangular, ni la t con grados de libertad. El criterio de logro tampoco los menciona.
- **Corrección propuesta:** añadir en el enunciado de B una entrada de tipo triangular (o declarar explícitamente que se omite por alcance), y una tarea: calcular la semiamplitud en 0,95 con t(15) para la media de 16 lecturas, o al menos reconocer cuándo se usa t frente a z. Ajustar el criterio de logro.

### H-08 — Menor — A no evalúa la autocorrelación que prop_e incluye en A
- **Ubicación:** `M03_libreto.md:330-350`; alcance en `prop_e.md` (M3-A: «autocorrelación»; práctica evaluable: «matriz pequeña… y comparar estrategias de promediado»).
- **Problema:** la autocorrelación se explica en A2 (con un ejemplo), pero la práctica no pide estimarla ni interpretarla. La práctica tampoco exige la autocorrelación como señal de escalamiento.
- **Corrección propuesta:** en la práctica A añadir una tarea corta: calcular ρ₁ de la serie de 16 lecturas con la definición del libreto (declarar el estimador) y decidir si el promedio simple es aplicable; o declarar en el enunciado que la autocorrelación no se evalúa en esta práctica.

### H-09 — Menor — supuesto de normalidad no soportado por una regla
- **Ubicación:** `M03_libreto.md:212`.
- **Problema:** el enunciado afirma que los seis errores «proceden… de una población normal», pero son seis valores escritos a mano en {−0,10; 0; 0,10} sin regla de generación. Un valor simulado debe tener regla reproducible. La afirmación de origen normal no puede verificarse.
- **Corrección propuesta:** sustituir «procedentes —por supuesto del ejercicio— de una población normal» por «valores fijados para el ejercicio; se trabajan bajo el supuesto normal declarado», o generarlos con semilla y regla explícitas en el script.

## Sin hallazgos

- Estructura de la práctica (enunciado narrado, datos y origen, tareas, solución, interpretación, señal de escalamiento y criterio de logro) completa en B, I y A.
- Los datos de B (especificaciones hipotéticas, serie determinista) están declarados como simulados y no atribuidos a CALAIRE.
- Las fórmulas de conversión (h/√3, δ/√12, U/k), la covarianza con signo y la regla de matriz admisible son correctas.
- Las matrices de A (simétricas, autovalores 0,026 y 0,104; 0 y 17; inválida con −0,2) son correctas.
- La razón de canales con covarianza (0,40625) y la diferencia de puntos (3,000 frente a 4,123) son correctas.
- Corrección por pendiente conocida: los cuatro bloques dan 420,000; la afirmación de que la corrección no se aplica a datos reales sin modelo validado es adecuada.

## Resumen

Mayor: 5 (H-01 a H-05). Menor: 4 (H-06 a H-09). Crítica: 0.

Los cambios de H-02 y H-04 son numéricos y se pueden aplicar con exactitud. H-03 requiere una decisión de alcance del responsable del curso: retirar la inferencia de varianzas de M3 o aceptarla con un cambio explícito en prop_e. H-05 también requiere decisión: producir la figura o declarar que el gráfico no es evaluable.
