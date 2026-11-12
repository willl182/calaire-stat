# Verificación etapa 2 — M06

**Veredicto: CON OBSERVACIONES.** No hay incumplimientos de los criterios de etapa 2. Los scripts corren y reproducen las cifras del libreto. Quedan observaciones de redacción, de coherencia de tiempos y de un comentario erróneo en `calc/`.

Alcance: `M06_libreto.md`, `calc/M06_*` y `M06_practica_I_residuos.html`, contra `00_plan_corto.md` (Etapa 2) y `logs_etapa2/cambios_M06.md`. No se editó ningún archivo del curso.

## Criterios

| Criterio | Resultado | Evidencia |
|---|---|---|
| Nivel A retirado sin menciones residuales | Cumple | Búsqueda de «nivel A», «A2», «A.», «AX», «REML», «sesgo» y referencias a M7–M13 en libreto y `calc/M06_*`: sin resultados ajenos a B/I. |
| Agenda de sesión de 120 min | Cumple | `M06_libreto.md:3-13`: 10 + 59 + 25 + 10 + 15 + 1 = 120. Coincide con la fila de sesión 5 del plan. |
| Práctica B en clase | Cumple, con observación | Agenda `M06_libreto.md:9` (25 min en clase). El encabezado `M06_libreto.md:75` («Práctica B») no indica «en clase» como sí lo hace el de la práctica I (`:183`). Ver hallazgo 2. |
| Práctica I partida en clase y tarea, con soluciones | Cumple | En clase: `:183` («en clase, 10 min») y `:200`. Tarea: `:202`. Solución docente con cifras: `:204` y `:206`. |
| Revisión de la tarea anterior (salvo M02) | Cumple | `M06_libreto.md:27-29`, 10 min (`:7`). Coincide con la tarea M05-I (`M05_libreto.md`, potencia 0,284 y 0,495). |
| Tareas específicas del módulo (repetibilidad, precisión intermedia, R&R condensado ~15 min) | Cumple | Repetibilidad y precisión intermedia: B1–B2 (`:35-93`). R&R condensado: escena I6 (`:211-249`). Práctica B: `:77-91`. |
| Scripts M06 corren y coinciden con el libreto | Cumple | Ejecutados con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I` en copia temporal: los cuatro scripts salen con código 0 (ver cifras abajo). |
| Tema del PDF cubierto (M6: repetibilidad, precisión intermedia, R&R) | Cumple | Ver «Cobertura del PDF». |

## Comprobación numérica (script frente a libreto)

- `calc/M06_ejemplos.py`: SS entre 0,56, dentro 0,18, total 0,74; F = 14,0; F crítico 4,256. Coincide con `M06_libreto.md:111-113`.
- `calc/M06_practicas_luna.py` (B): u_prec = 0,127279; U = 0,254558; sin entre días u = 0,034641, U = 0,06928. Coincide con `:83`.
- `calc/M06_practicas_luna.py` (I): medias diarias, SS 0,330651 / 2,588622 / 2,919273; MS 0,066130 / 0,061634; F = 1,072952; F crítico 2,437693; τ² = 0,000562; s_entre = 0,023707; IC σ² [0,041903; 0,099567]; SE(τ²) 0,005492; SE(s_entre) 0,115823; C = 0,450, crítico 0,628724. Coincide con `:204-206`.
- `calc/M06_RR_CALAIRE.py`: máx. F analista 1,238 (umbral 18,51); interacciones significativas en 135, 360, 405, 455 con F 6,61 / 4,31 / 6,47 / 5,07; Bonferroni 6,35 deja 135 y 405; dispersión de días 0,106–0,206; medias de bloque de analista 2 en 405 y 455: 0,729 y 0,828. Coincide con `:223-229`.
- `calc/M06_practica_I_grafico.py`: regenera `M06_practica_I_residuos.html`; el archivo generado es idéntico al existente (`cmp` sin diferencias).

## Cobertura del PDF (M2–M6)

El PDF «Temario estadistica.pdf» no está en el árbol de trabajo. Se verificó contra `Curso_COMPLETO/temario_curso.md`, sección M6 (`:221-267`: objetivo de descomponer la variación, repetibilidad, precisión intermedia, componentes y estudios R&R).

- Repetibilidad y precisión intermedia: B1–B2 y la ISO 5725-3 en I5 (`M06_libreto.md:35-93`, `:173-181`).
- Componentes y ANOVA de efectos aleatorios: I1–I3 (`:97-171`).
- R&R: I6 (`:211-249`), condensado como pide el plan (~15 min narrados).

## Hallazgos

1. **Tiempo de narración sin respaldo en el conteo.** `M06_libreto.md:8` asigna 59 min a «Narración B + I, incluida la escena I6». El conteo de `logs_etapa2/cambios_M06.md` da 43,9 min a 130 palabras/min (B 10,3 + I 21,1 + I6 12,5). Un recuento aproximado del libreto da del orden de 41 min. Hay unos 15 min sin texto que los respalde. La agenda suma 120 min, pero la narración real cabe en unos 45 min. Conviene ajustar la cifra o declarar la holgura. (`M06_libreto.md:8`; `cambios_M06.md`, sección de palabras)
2. **Encabezado de práctica B sin indicar «en clase».** `M06_libreto.md:75` (`### Práctica B`). La agenda (`:9`) y el plan indican que se resuelve en clase en 25 min. Añadir «— en clase (25 min)» para igualar a la práctica I (`:183`).
3. **Error de redacción.** `M06_libreto.md:204`: «Por momentos, σ̂² = …» debe ser «Por tanto» (o «Por momento»). El sentido es de cálculo, no de tiempo.
4. **Comentario erróneo en el script.** `calc/M06_practicas_luna.py:21`: dice «columna AL de BD_DIAS». Las columnas leídas son `cols = [6, 12, 18, 24, 30, 36]` (`:24`), es decir F, L, R, X, AD, AJ, como indica el enunciado (`M06_libreto.md:187`). El cálculo es correcto; solo corregir el comentario.
5. **Nomenclatura de escenas.** `M06_libreto.md:211` usa «### I6.» mientras las demás son «### Escena I1» a «Escena I5» (`:97`, `:117`, `:139`, `:157`, `:173`). Unificar a «### Escena I6.» salvo que se prefiera el formato corto.
6. **Rutas fuera de `Curso_CORTO/`.** `M06_libreto.md:249`, `:268-277` y los encabezados de `calc/` apuntan a `../Curso_COMPLETO/...` para el intérprete, los PDF de referencia y las fuentes (GUM, ISO, MMU, Crowder). No es un error, porque la etapa 1 ya lo decidió. Sin embargo, `Curso_CORTO/docs/` solo contiene los dos libros de Excel. Anotar que el curso corto depende de `Curso_COMPLETO/` para ejecutar.
7. **Cobertura del PDF verificada contra un proxy.** El PDF no está en el árbol, así que la cobertura se comprobó con `Curso_COMPLETO/temario_curso.md`. Si el PDF tiene redacción distinta de M6 (por ejemplo, un % R&R o categorías de distinción), revisarlo contra el original.

## Observaciones sin acción requerida

- El modelo de I6 (`M06_libreto.md:219`) trata los días anidados en analista × bloque y no empareja días entre analistas. Coincide con la nota de `temario_curso.md:253` y con la advertencia de `:245`.
- El texto de I6 es exploratorio y condicional. La advertencia se mantiene en el enunciado (`:213`), el análisis (`:217`) y la comprobación docente (`:249`).

## Resumen

- Criterios de etapa 2 cumplidos: nivel A retirado, agenda de 120 min, práctica B en clase, práctica I partida con soluciones, revisión de la tarea anterior, tareas del módulo y scripts reproducibles.
- Observaciones a atender: 1 (tiempo de narración), 2 (encabezado de práctica B), 3 (redacción), 4 (comentario de script), 5 (nomenclatura de I6), 6 (dependencia de rutas), 7 (PDF no incluido).
- Ningún hallazgo bloquea la etapa 2.
