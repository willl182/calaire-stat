# Verificación etapa 1 — punto 1 (prerrequisitos de M1)

**Veredicto: CON OBSERVACIONES**

La tarea principal está hecha en las fichas (M02:8 y M03:8) y en la escena de apertura de M02. Queda una referencia a M1 en el cuerpo de M03 que el cambio no recogió, y dos incoherencias de redacción en M02 y M03 que conviene corregir.

## Cumplimiento de la tarea

- `M02_libreto.md:8` — la ficha ya no cita M1 y dice que el punto de partida se presenta en el capítulo. **Cumple.**
- `M02_libreto.md:16–19` — sección «Punto de partida» con $x$, $y$, $e=y-x$ y $c=-\ln(T)/(\alpha L)$. Los signos y la fórmula coinciden con `Curso_COMPLETO/curso/S1_fundamentos/M01_libreto.md:26,62`. **Cumple.**
- `M03_libreto.md:8` — prerrequisito reescrito apuntando a M02. **Cumple** en la ficha.
- `M03_libreto.md:18` — el cuerpo del Nivel B aún dice «No sustituye el modelo de medición de M1». **No cumple:** queda una referencia rota a M1 en el texto corrido. El log de cambios no lo menciona.

## Observaciones

1. **M03_libreto.md:18 (rechazo parcial, corregible en una línea).** «el modelo de medición de M1» debe pasar a «el punto de partida de M02» o equivalente.
2. **M02_libreto.md:22 (coherencia con el texto nuevo).** «En el nivel B ya damos por visto qué son la referencia $x$, la indicación $y$ y el error…» presupone que el alumno lo vio antes. Tras el cambio, eso se acaba de presentar en la sección anterior. Sugerencia: «Como acordamos en el punto de partida, …».
3. **M03_libreto.md:8 (sobreafirmación).** Dice que M02 presenta el «modelo de medición». M02 solo presenta $x$, $y$, $e$ y la fórmula del SRP; no introduce $Y=f(X_1,\dots,X_N)$. Reformular como «las entradas del SRP» o añadir una frase de modelo en la escena nueva.
4. **M02_libreto.md:18 (unidades ausentes).** La fórmula $c=-\ln(T)/(\alpha L)$ se da sin unidades. M01 la presenta con $c$ en atm y la conversión a nmol/mol mediante $p_0$. Basta una frase que diga que $c$ sale en atm (con $\alpha$ en atm⁻¹ cm⁻¹ y $L$ en cm) y que la conversión a nmol/mol se hace dividiendo por la presión estándar. No hay que trasladar la conversión completa desde M1, porque M1 ya no existe en el curso corto.

## Otras partes del texto (no evaluadas como punto 1)

- M04, M05 y M06 son idénticos a `Curso_COMPLETO`. Ninguna referencia a M1 queda en ellos. **No rompió nada.**
- En M02 hay una escena «B6» (líneas ~91–98) que no está en el log del punto 1. Pertenece al punto 3 (valores atípicos), según el plan. No la evalúo aquí.
- Otras referencias fuera de alcance (M8, M9-A en M03:282, M10–M12, AX.4 en M06:13) son del punto 2. No las evalúo aquí.
- Números reproducibles: el punto 1 no toca cálculos. `calc/` es idéntico a la fuente en los archivos de M02–M06, así que no fue necesario ejecutar los scripts. Ningún número del texto nuevo depende de cálculo.

## Pendiente para el autor del punto 1

- Corregir `M03_libreto.md:18` (M1 residual).
- Revisar `M02_libreto.md:22` («ya damos por visto»).
- Decidir sobre `M03_libreto.md:8` y la falta de unidades en `M02_libreto.md:18`.
- Añadir al log `cambios_p1.md` la línea de M03:18 si se corrige.
