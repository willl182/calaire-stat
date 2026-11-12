# Revisión de las prácticas M09 (Haiku 5.5)

**Alcance:** bloques `### [PRÁCTICA]` de `curso/S3_comparacion_decision/M09_libreto.md` (B: líneas 76–102; I: 167–178; A: 265–276), `curso/S3_comparacion_decision/calc/M09_practicas_luna.py` y `curso/logs/M09_practicas_luna.md`. Contraste con `prop_e.md` §2 y §5 (M9), y con `curso/guia_libreto.md` §1, §3, §4 y §8. No se revisaron referencias ni citas (otro supervisor). No se editó ningún libreto ni script.

**Verificación ejecutada:** `curso/.venv/bin/python -I curso/S3_comparacion_decision/calc/M09_practicas_luna.py` (rc=0) y `M09_ejemplos.py` (rc=0). Recalculados a mano con `curso/.venv/bin/python -I`.

## Cifras verificadas (sin discrepancias)

| Bloque | Cifra en libreto | Recalculado |
|---|---|---|
| B, 80 | Δ=0,30; u(Δ)=0,25; U₁=0,40; U₂=0,30; E_n=0,60 | igual |
| B, 420 | Δ=−0,40; u(Δ)=0,7810; U₁=1,20; U₂=1,00; denominador 1,5620; E_n=−0,2561 | igual (E_n=−0,256074) |
| I | cov=0,0180; residuales 0,0175 y 0,0081; u²(Δ)=0,0265; u(Δ)=0,16279; U=0,32558 | igual (0,162788; 0,325576) |
| I | Δ/U(Δ)=1,0750; sin covarianza 0,70 | igual (1,075016; 0,35/0,5=0,70) |
| I | admisibilidad \|0,018\| ≤ u₁u₂ = 0,030 | igual |
| A, 80 | D=0,30; u(D)=0,25; U(D)=0,50; D/U=0,60 | igual |
| A, 420 | D=0,80; u(D)=0,781025 (cuadrado 0,61); U(D)=1,562050 | igual |

Formato: no hay puntos decimales en los bloques de práctica; los rótulos de origen (simulados, regla reproducible, no CALAIRE) están presentes en los tres. Los marcadores `[PRÁCTICA — fase de ejercicios]` quedaron sustituidos (3 de 3, 0 restantes). Alcance B/I/A correcto: B no usa covarianza, I usa covarianza de patrón compartido, A usa referencia común y separa D/u(D) del indicador normalizado.

## Hallazgos

### H-01 — mayor — Falta el análisis de sensibilidad a la covarianza exigido en A

- **Ubicación:** `M09_libreto.md`, bloque «Grado de equivalencia frente a una referencia común» (líneas 265–276), enunciado y solución.
- **Problema:** `prop_e.md` §5 (M9, A, práctica evaluable) pide «analizar la sensibilidad a las hipótesis de covarianza». El bloque solo declara covarianza residual nula y dice en prosa que «si hubiera una contribución compartida, se necesitaría su covarianza». No hay ningún cálculo de sensibilidad.
- **Corrección propuesta:** añadir una tarea y su solución. Con $\operatorname{cov}(P,R)$ como parámetro, $u^2(D)=u_P^2+u_R^2-2\operatorname{cov}$. Valores verificados:
  - 80 nmol/mol, $u_Pu_R=0,030$: cov=0 → u(D)=0,2500, U=0,5000; cov=0,015 (ρ=0,5) → u(D)=0,1803, U=0,3606; cov=0,030 (ρ=1) → u(D)=0,0500, U=0,1000.
  - 420 nmol/mol, $u_Pu_R=0,30$: cov=0 → u(D)=0,7810, U=1,5620; cov=0,15 (ρ=0,5) → u(D)=0,5568, U=1,1135; cov=0,30 (ρ=1) → u(D)=0,1000, U=0,2000.
  - Pedir al alumno que diga qué hipótesis cambia la conclusión de la comparación y qué información de presupuesto la respalda. Añadir los mismos valores a `M09_practicas_luna.py` para que sean reproducibles.

### H-02 — menor — «Herramienta contrastada» no identificada

- **Ubicación:** `M09_libreto.md`, solución de la práctica A («La herramienta se contrasta aritméticamente por segunda vía…»).
- **Problema:** `prop_e.md` §5 pide resolver «con herramienta contrastada». La solución no nombra ninguna herramienta; la «segunda vía» es el mismo cálculo a mano con cuadrados. El script `M09_practicas_luna.py` produce las cifras, pero el libreto no lo menciona en la solución (solo en el enunciado como fuente de datos).
- **Corrección propuesta:** citar en la solución el script `calc/M09_practicas_luna.py` como herramienta de contraste y decir qué se comprueba con él. No cambiar el texto de la segunda vía si se mantiene.

### H-03 — menor — El script no reproduce todas las cifras del libreto y la bitácora sobreafirma el cotejo

- **Ubicación:** `calc/M09_practicas_luna.py`, sección I (cálculo de residuales, cov y u(Δ)); `curso/logs/M09_practicas_luna.md`, sección «Comprobaciones» («las cifras del script se cotejaron con las soluciones»).
- **Problema:** el script no imprime Δ=0,35 ni Δ/U(Δ)=1,0750 del bloque I, que son las cifras que el alumno debe obtener y que el libreto usa para la clasificación. Tampoco comprueba con `assert` la admisibilidad de la covarianza ni la no negatividad de los residuales, que el libreto afirma («ambas no negativas», «admisible»). La bitácora dice que todas las cifras se cotejaron; esto es cierto solo para u(Δ), U y las de B y A.
- **Corrección propuesta:** en la sección I del script, imprimir `delta = 0.35` y `delta/U_k2` (debe salir 1,075016); añadir `assert var1-(c1*uR)**2 >= 0`, `assert var2-(c2*uR)**2 >= 0` y `assert abs(cov) <= u1*u2`. En la bitácora, precisar qué cifras se verificaron con el script y cuáles a mano.

### H-04 — menor — El bloque A reutiliza los datos y el cálculo de B

- **Ubicación:** `M09_libreto.md`, enunciado de la práctica A (líneas 265–276).
- **Problema:** las parejas (80; 80,30 frente a 80,00; u 0,20 y 0,15) y (420; 420,80 frente a 420,00; u 0,60 y 0,50) son las de B cambiando solo el valor de y en 420. La práctica A repite la misma operación de cuadratura; el elemento nuevo (referencia común, separar D de E_n) queda solo en la narración. Con H-01 resuelto la práctica ganaría contenido propio, pero conviene además que los datos de A no sean los de B, o que el libreto diga que se reutilizan a propósito.
- **Corrección propuesta:** cambiar la pareja de 420 de A (o las incertidumbres) por valores propios de esa comparación, fijados en el script, o añadir una frase que diga que es la misma serie vista desde el grado de equivalencia.

### H-05 — menor — La bitácora no sigue la estructura de la guía

- **Ubicación:** `curso/logs/M09_practicas_luna.md`.
- **Problema:** `guia_libreto.md` §8 exige para la bitácora las secciones Plan, Ejecución y **Correcciones** (tabla hallazgo → acción → ubicación). La bitácora tiene Plan, Ejecución, Archivos tocados, Comprobaciones y Pendientes, sin Correcciones. Además, el estado «Ninguno» en Pendientes no recoge H-01 a H-04 de esta revisión.
- **Corrección propuesta:** añadir la sección Correcciones (puede quedar vacía en esta primera entrega, con la fecha) y, cuando se atiendan H-01 a H-04, registrar cada uno con su acción.

### H-06 — bajo — La narración de las soluciones es densa para lectura oral

- **Ubicación:** `M09_libreto.md`, párrafos «Solución docente» de B (línea ~84), I (~170) y A (~268).
- **Problema:** `guia_libreto.md` §1 pide frases cortas y ritmo oral. Los párrafos de solución mezclan 8 a 12 cifras, fórmulas y unidades en una sola frase larga; el de I tiene más de 150 palabras.
- **Corrección propuesta:** dividir cada párrafo de solución en pasos cortos («Primero, la covarianza… Segundo, las varianzas residuales…»), o pasar las cifras a una tabla de solución, como ya se hace en otros capítulos.

### H-07 — bajo — En I, el punto docente del cambio de decisión no se enuncia

- **Ubicación:** `M09_libreto.md`, solución de la práctica I (línea ~170).
- **Problema:** la misma diferencia de 0,35 nmol/mol da 0,70 sin covarianza y 1,0750 con ella: la covarianza positiva cambia el lado del criterio. El bloque solo dice «ignorar covarianza daría 0,25 nmol/mol». El alumno debería ver explícitamente que la conclusión depende del modelo. Además, la frase «señala incompatibilidad estadística» es fuerte para un valor de 1,075 que la propia práctica llama próximo al límite; conviene matizarla.
- **Corrección propuesta:** añadir una frase: «Sin covarianza, la extensión sería 0,70 y pasaría el criterio; con la covarianza, 1,075 lo incumple. La misma diferencia cambia de lado solo por el modelo.» Cambiar «señala incompatibilidad» por «queda fuera del criterio didáctico y, por cercanía al límite, se escala».

## Conclusión

Las cifras de B, I y A son correctas y reproducibles con `calc/M09_practicas_luna.py`, y el alcance por nivel es el de `prop_e.md`. Hay un hallazgo mayor (H-01: falta la sensibilidad a la covarianza en A) y seis menores o bajos. H-01 y H-03 deberían corregirse antes de dar el bloque por cerrado; los demás son de redacción o de trazabilidad.
