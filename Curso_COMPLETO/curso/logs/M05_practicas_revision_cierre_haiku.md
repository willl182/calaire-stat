# M05 — Revisión de cierre de prácticas B, I y A (Haiku)

## Alcance y método

Revisión de solo lectura de `curso/S2_modelos_calibracion/M05_libreto.md` (bloques `[PRÁCTICA]` B, I y A), de `curso/S2_modelos_calibracion/calc/M05_practicas_luna.py` y de la bitácora `curso/logs/M05_practicas_luna.md`. Se ejecutó `curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M05_practicas_luna.py` (rc=0). Se recalcularon a mano los efectos, las interacciones, los contrastes y la tabla factorial con un script temporal fuera del repositorio. No se editaron libretos ni scripts, no se tocaron referencias ni citas y no se hicieron commits.

## Verificado sin hallazgos

- Tabla factorial: los ocho valores coinciden con la fórmula $e=0{,}20+0{,}40F+0{,}10C-0{,}05T+0{,}15FC+0{,}02FT-0{,}01CT+0{,}04FCT$.
- Efectos marginales: F = 0,80; C = 0,20; T = −0,10 nmol/mol.
- Efectos simples de F con C = −1 (0,50) y C = +1 (1,10); diferencia 0,60; interacción F×C con convención I2 = 0,30; contraste F con C y T altos = 1,22 nmol/mol.
- Conteos B: 12×8×6 = 576 = 480 + 96.
- Conteos A base: 192 lecturas; gl 2, 9, 12, 168. Alternativa de seis analistas con una lectura por ciclo: 48 lecturas; gl 5, 18, 24, 0.
- Potencias de la subtarea: sd de media diaria 0,2021 y 0,2031; potencias 0,284 y 0,495 con t no central y gl d−1. La fórmula de no centralidad $\Delta\sqrt d/\sqrt{\tau^2+\sigma^2/n}$ es correcta.
- Enunciados B, I y A tienen las cinco partes del formato (enunciado, tareas, solución, interpretación/decisión, criterio de logro); la práctica A cita AX.4, que existe en `curso/S4_numericos_integracion/AX_libreto.md`.

## Hallazgos

**H-01 — Criterio de escalamiento sin cobertura completa (media).** El enunciado de I fija el criterio «efecto principal o contraste simple de F, C o T» con umbral de 0,50 nmol/mol. La solución solo evalúa F marginal (0,80) y un contraste simple de F (1,22). Recalculados, hay más contrastes simples por encima de 0,50 que no se reportan: C con F = +1 y T = +1, 0,85 − 0,29 = 0,56; F con C = −1 y T = −1, 0,41 − (−0,13)... en la tabla, F = +1 frente a −1 con C = −1, T = −1 es 0,41 − (−0,13) = 0,54; F con C = +1 y T = −1 es 0,85 − (−0,13) = 0,98. La decisión de escalar no cambia, pero la práctica declara que el criterio cubre esos contrastes sin calcularlos ni reportarlos, y el script no los imprime. Ajuste sugerido: o se calculan y se reportan en el script y en la solución, o se limita el criterio a efectos principales y al contraste de ejemplo.

**H-02 — La bitácora `curso/logs/M05_practicas_luna.md` contradice el libreto en H-07 (media).** La bitácora marca H-07 como «Rechazado como práctica redundante» y su Estado dice que la evidencia de potencia queda fuera. El libreto sí incluye la subtarea de repartir esfuerzo y planificar potencia (`Subtarea — repartir esfuerzo y planificar potencia`), con su enunciado, solución y criterio de logro, y la versión de `curso/S2_modelos_calibracion/M05_practicas_luna.md` lo registra como «Revisado y aplicado» con el hallazgo S-M05-01. La bitácora de `curso/logs/` tampoco contiene la entrada S-M05-01 ni los resultados de potencia. Hay dos bitácoras divergentes; la de `curso/logs/` es la que se pidió revisar. Ajuste sugerido: actualizar `curso/logs/M05_practicas_luna.md` con la decisión real de H-07 y S-M05-01, o explicar por qué se mantiene el rechazo.

**H-03 — Frase de potencia exagerada (baja).** El libreto dice que el plan B «casi duplica la potencia». Según el script, pasa de 0,284 a 0,495, es decir, ×1,74. Ajuste sugerido: «aumenta la potencia de 0,28 a 0,50», con cifras de la salida.

**H-04 — La solución de escalonado en el script es texto fijo, no cálculo (baja).** `design_counts()` imprime como literales «4 resultados vs 8», «ahorro=4 (50%)» y la secuencia de etapas. La bitácora dice que el script «registra las etapas descritas» y que «reproduce» el ahorro, pero no lo calcula. Ajuste sugerido: calcularlo a partir de parámetros o describir en la bitácora que es texto de referencia.

**H-05 — Referencia a la revisión interna dentro del texto de la práctica B (baja).** La solución docente de B dice «la revisión detectó en el archivo una estructura distinta que corresponde investigar por separado». Eso es una nota para el instructor que se filtra al enunciado del operador. La decisión H-09 indica que no debe convertirse en actividad de clase. Ajuste sugerido: mover esa frase a un bloque `[NOTA AL INSTRUCTOR]`.

**H-06 — Guía desalineada con la fase de prácticas (baja).** `curso/guia_libreto.md` §1 sigue diciendo «Fase actual: solo contenido» y que las prácticas se desarrollan en una fase posterior. M05 ya tiene prácticas desarrolladas, y el encargo actual las pide. Ajuste sugerido: actualizar la guía o registrar la nueva fase, sin tocarla en esta revisión.

**H-07 — Datos de origen no verificables desde el repositorio (baja, pendiente).** La práctica B cita «certificado F-PSMT-01, hoja Fotometro, celda E17» y la práctica A cita el patrón escalonado de ISO 5725-3 (4 resultados por laboratorio frente a 8, sin fuente local). El repositorio no contiene el certificado, así que el conteo de E17 no se pudo comprobar. El patrón ISO no se verificó en esta revisión. No se tocaron citas, como se pidió.

## Estado

Hallazgos abiertos: H-01 (media), H-02 (media), H-03 a H-07 (baja). La salida del script es correcta en todas las cifras verificadas; los problemas son de cobertura del criterio, de sincronización de bitácoras y de redacción. Ninguno cambia la decisión de escalamiento de la práctica I.
