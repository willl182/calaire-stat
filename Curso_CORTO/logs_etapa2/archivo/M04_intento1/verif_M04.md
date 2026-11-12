# Verificación etapa 2 — M04

**Veredicto: RECHAZADO**

El nivel A está retirado sin residuos, la agenda suma 120 min y los dos scripts corren y coinciden con el libreto. Pero la práctica I no está en el libreto: no hay tramo de clase, no hay tarea y no hay enunciado ni solución. Lo declara `cambios_M04.md:9`, y es falso. Además, el recorte de I es mucho mayor que el planeado.

## Hallazgos

1. **Práctica I ausente (bloqueante).** `M04_libreto.md:10` la agenda como «Práctica I — en clase | 15», pero no existe sección de práctica I en el libreto. Faltan el tramo de inicio en clase (selección y cálculo de t pareada/Welch), la tarea (varianzas, potencia, incertidumbre de s y Grubbs/Dixon) y la solución docente. El texto del libreto no contiene «tarea» para la práctica I; solo aparece en la revisión de M03 (`M04_libreto.md:16-18`). `cambios_M04.md:9` afirma que esto está hecho: la afirmación no se sostiene.

2. **Agenda incompleta en la fila de práctica I.** `M04_libreto.md:10` no indica «→ tarea», a diferencia de `00_plan_corto.md:78-84` (práctica I «clase → tarea»).

3. **Recorte de I mucho mayor que el planeado.** `00_plan_corto.md:52-53` y `:90` piden recortar la narración de B+I a unos 45 min, condensando I3 e I4. Al contar palabras, la sección I de `M04_libreto.md:108-141` tiene unas 550 palabras; en el original (`Curso_COMPLETO/curso/S1_fundamentos/M04_libreto.md:92-217`) tiene unas 4 250. La narración total de B+I ronda las 2 900 palabras, unos 22 min a 130 palabras/min, no los 45 reservados. `cambios_M04.md:22-28` justifica la diferencia con «pausas, pizarra y transiciones», lo cual no basta para cubrir 20 min de agenda. Conviene decidir si el contenido perdido (I2, I5 y el resto de I) era necesario o si la agenda debe reducirse.

4. **Valor crítico de Dixon sin fuente válida.** `calc/M04_ejemplos.py` (`qcrit=0.59`, con comentario «tabla de Dixon para n=8 y nivel 0,99») y `calc/M04_practicas_luna.py` (`qcrit=.59`) usan 0,59. Las tablas habituales dan aproximadamente 0,63 para n=8 al 99 %; hay que confirmarlo contra la tabla de Otto que cita el libreto. La conclusión no cambia, porque Q = 0,8214 supera cualquiera de los dos valores. `M04_libreto.md:138` dice «superior al valor tabulado indicado para el ejemplo», pero no indica ningún valor.

5. **Cifras de palabras en el libreto y en el log no coinciden con el texto.** `M04_libreto.md:14` y `cambios_M04.md:22-26` dan 1 668 palabras de B y 467 de I. Contando el bloque B del libreto (`M04_libreto.md:32-101`) salen unas 2 360 palabras con encabezados, tablas y práctica, y la sección I (`:108-141`) unas 550. Son cifras aproximadas, pero el criterio de conteo no está explicado en el libreto.

## Comprobaciones que pasan

- **Nivel A retirado.** No hay menciones residuales en `M04_libreto.md` (búsqueda de «Nivel A», «A1–A3», multiplicidad, Bonferroni, TOST, equivalencia, consistencia). Tampoco en `calc/M04_*.py`. No hay HTML M04.
- **Agenda de sesión.** `M04_libreto.md:5-12` suma 120 min (15 + 45 + 25 + 15 + 20).
- **Revisión de la tarea anterior.** Presente en `M04_libreto.md:16-18`, con el guion de la práctica I de M03.
- **Práctica B en clase.** `M04_libreto.md:88-100`, con enunciado, solución, interpretación y criterio de logro.
- **Tareas del módulo (intervalos y pruebas).** Cubiertas en B1–B3 (`:38-100`) e I1–I5 (`:114-140`). Quedan cubiertos: media con t, contraste con valor p y errores de decisión, pareada, Welch, varianza (chi-cuadrado y F), potencia y tamaño de muestra, incertidumbre de s, y Grubbs/Dixon con límites de uso.
- **Scripts.** Ejecutados desde una copia temporal con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`. `M04_ejemplos.py` termina con código 0 e imprime `comprobaciones_M04=OK`. `M04_practicas_luna.py` termina con código 0 e imprime `comprobaciones_practicas_M04=OK`.
- **Coincidencia script–libreto.** Coinciden:
  - B: media 0,0375, s 0,5263, error estándar 0,1861, IC95 [−0,4025; 0,4775], t 0,2015, p 0,8460 (`M04_libreto.md:52-78`).
  - Pareada: media 0,1625, IC95 [0,0632; 0,2618], t 3,8697, p 0,0061 (`:120`).
  - Welch: −0,9405, IC95 [−1,2778; −0,6032], t −6,1418, p 0,000075 (`:120`).
  - Varianza: IC95 [0,1211; 1,1473] (`:128`).
  - Razón de varianzas: 0,8408, IC95 [0,1404; 5,8669], p 0,8678 (`:128`).
  - u(s) = 0,1407 (`:134`).
  - Potencia: n = 34 para d = 0,5 y n = 26 por grupo para d = 0,8 (`:132`).
  - Grubbs G = 2,4374 (`:138`).
  - Práctica B: media 0,1500, s 0,3251, error estándar 0,1150, IC95 [−0,1218; 0,4218], t 1,3049, p 0,2332 (`:94-96`).
- **Cobertura del PDF (M4: intervalos y pruebas).** Cubierta en B (estimación con intervalo, contraste, errores de decisión) e I (pruebas de dos medias, varianzas, potencia).
- **Referencias fuera del alcance.** Ninguna referencia a M7, M8, M10, M11, M12 ni AX.4 en el libreto.

## Acción requerida para pasar a APROBADO

1. Añadir la práctica I partida (`M04_libreto.md`, tras la escena I5): tramo de clase (15 min), tarea con su enunciado, y solución docente; corregir `:10` con «→ tarea».
2. Corregir `cambios_M04.md:9`, o sea, no declarar hecho lo que no está.
3. Decidir el recorte de I (punto 3) y actualizar `cambios_M04.md:22-28` con cifras que correspondan a la agenda.
4. Confirmar el valor crítico de Dixon y corregir el comentario y el valor en ambos scripts, o explicitar el valor en el libreto (punto 4).
