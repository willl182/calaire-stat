# Curso corto — plan (módulos M2 a M6 del temario PDF)

Base: `Temario estadistica.pdf`, módulos M2–M6. Origen: copia íntegra de `Curso_COMPLETO/curso` (M02–M06).

## Contenido copiado

| PDF | Libreto | Palabras | Escenas | Prácticas |
|---|---|---|---|---|
| M2 Descriptiva | M02_libreto.md | 8 036 | 9 | 3 (B, I, A) |
| M3 Probabilidad | M03_libreto.md | 10 016 | 14 | 3 |
| M4 Inferencia | M04_libreto.md | 9 764 | 12 | 3 |
| M5 Diseño de experimentos | M05_libreto.md | 11 753 | 14 | 3 |
| M6 ANOVA y precisión | M06_libreto.md | 10 290 | 14 | 3 |
| **Total** | | **≈49 900** | **63** | **15** |

También se copiaron las prácticas en HTML, `calc/` (12 scripts) y `docs/` (2 libros de Excel que usa M06).
Los 12 scripts corren con `../Curso_COMPLETO/curso/.venv/bin/python -I`. Las rutas se ajustaron a la nueva ubicación.

## Etapa 1 — versión corta "de largo" (cambios mínimos)

1. **Prerrequisitos de M1 que ya no existen.** M02 y M03 citan M1 (modelo de medición, error con signo $e=y-x$, ecuación del SRP).
   Se resuelve con una escena breve al inicio de M02 que enseñe solo lo necesario.
2. **Referencias a módulos fuera del curso** (M7, M8, M10, M11, M12, AX.4): se convierten en «fuera del alcance de este curso» o se eliminan.
3. **Valores atípicos en M2** (es un hueco frente al PDF): subir a M02 el tratamiento que hoy está en M04 (Grubbs y Dixon, escena I5), o al menos un puente hacia él.
4. Se mantiene la numeración M2–M6, que ya coincide con el PDF.
5. Revisión de coherencia y nueva ejecución de los scripts.

## Etapa 2 — curso de 10 horas (plan)

### Peso actual por nivel (palabras de narración; 130 palabras/min)

| Módulo | B | I | A | Prácticas |
|---|---|---|---|---|
| M2 | 4 118 | 1 969 | 1 573 | B, I, A |
| M3 | 3 634 | 2 688 | 2 946 | B, I, A |
| M4 | 2 608 | 4 283 | 2 116 | B, I, A |
| M5 | 3 738 | 3 482 | 3 709 | B, I, A |
| M6 | 1 869 | 3 895 | 3 597 | B, I, A |
| **Total** | **15 967 (≈2,0 h)** | **16 317 (≈2,1 h)** | **13 941 (≈1,8 h)** | 15 |

Curso completo: ≈5,9 h de narración + 15 prácticas (≈25 min c/u ≈ 6,2 h) ≈ **12 h**.

### Propuesta: B + I, sin nivel A

B + I ≈ 4,1 h de narración + 10 prácticas (≈4,2 h) ≈ **8,3 h**; con apertura, cierre y holgura cabe en 10 h sin recortar B ni I a fondo.

| Bloque | Narración | Prácticas | Total |
|---|---|---|---|
| Apertura del curso (objetivos, datos del SRP, entorno de cálculo) | 15 min | — | 0:15 |
| M2 Descriptiva (incluye Punto de partida y B6 atípicos) | 47 min | B + I, 50 min | 1:40 |
| M3 Probabilidad y distribuciones | 49 min | B + I, 50 min | 1:40 |
| M4 Inferencia | 53 min → recortar a ~45 | B + I, 50 min | 1:35 |
| M5 Diseño de experimentos | 56 min → recortar a ~45 | B + I, 50 min | 1:35 |
| M6 ANOVA, precisión y R&R | 44 min | B + I, 50 min | 1:35 |
| Cierre e integración (caso SRP de punta a punta) | — | 30 min | 0:30 |
| Holgura / preguntas | | | 1:20 |
| **Total** | | | **10:00** |

### Riesgos de cobertura frente al PDF al quitar A

1. **M6 «estudios R&R»:** la estructura R&R con datos reales (M06 A, `M06_RR_CALAIRE.py`) y la planificación R&R (M05 A2) están en A. Conservar una versión condensada (≈15 min) dentro de M06 I.
2. **M2 atípicos y M4 Grubbs/Dixon (M04 I5):** se conservan; están en B e I.
3. Las demás exigencias del PDF para M2–M6 están en B o I.

### Recortes dentro de I (para llegar a ~45 min en M4 y M5)

- M04: condensar I3 (potencia) e I4 (incertidumbre de una desviación).
- M05: condensar I3 (un factor a la vez y reparto del esfuerzo); unir la práctica I a la de B si hace falta.

### Decisiones tomadas (2026-11-11)

1. Se elimina el nivel A; el R&R se conserva condensado (~15 min) dentro de M06 I.
2. Prácticas: en clase y como tarea. La práctica B se resuelve en clase; la práctica I se inicia en clase y se termina como tarea.
3. Cinco sesiones de 2 h, una por módulo.

### Estructura final: 5 sesiones × 120 min

| Sesión | Módulo | Narración B + I | Práctica B (clase) | Práctica I (clase → tarea) | Extra | Total |
|---|---|---|---|---|---|---|
| 1 | M2 Descriptiva | 47 min | 25 min | 15 min | apertura del curso 10 min; repaso y preguntas 23 min | 120 |
| 2 | M3 Probabilidad | 49 min | 25 min | 15 min | revisión de la tarea anterior 15 min; preguntas 16 min | 120 |
| 3 | M4 Inferencia | 53 → 45 min | 25 min | 15 min | revisión de la tarea 15 min; preguntas 20 min | 120 |
| 4 | M5 Diseño | 56 → 45 min | 25 min | 15 min | revisión de la tarea 15 min; preguntas 20 min | 120 |
| 5 | M6 ANOVA y R&R | 44 + 15 (R&R) min | 25 min | 10 min | revisión de la tarea 10 min; cierre del curso 15 min | 120 |

### Trabajo de la etapa 2

1. Retirar las secciones «Nivel A» de M02–M06 (y sus prácticas A, HTML y scripts que solo usa A).
2. M06: escena I6 «R&R con datos reales», condensada desde M06 A y M05 A2, con `calc/M06_RR_CALAIRE.py`.
3. Recortar M04 I (condensar I3 potencia e I4 incertidumbre de una desviación) y M05 I (condensar I3) hasta ~45 min de narración.
4. Partir cada práctica I en una parte de clase (15 min) y una parte de tarea, con su enunciado y su solución.
5. Añadir la apertura (sesión 1), la revisión de tareas (sesiones 2–5) y el cierre (sesión 5).
6. Actualizar fichas, cierres y referencias; rehacer el inventario de `calc/`; verificar que el curso cumple con el PDF (M2–M6).
