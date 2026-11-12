# Verificación M04 — Etapa 2

**Veredicto: CON OBSERVACIONES.** Los puntos de estructura, prácticas y cifras cumplen; quedan tres referencias residuales (fuera del curso o a archivos inexistentes en esta copia). No hay hallazgos bloqueantes.

## Verificado sin hallazgos

- **Nivel A retirado.** `M04_libreto.md` no contiene «Nivel A», «práctica A», `A1`–`A5`, «avanzado» ni «equivalencia avanzada». `calc/M04_ejemplos.py` y `calc/M04_practicas_luna.py` no tienen bloques exclusivos de A.
- **Agenda de 120 min.** `M04_libreto.md:3-11`: 15 + 45 + 25 + 15 + 20 = 120.
- **Práctica B en clase.** `M04_libreto.md:85` («en clase (25 min)»), con enunciado y solución docente (`:89-93`).
- **Práctica I en clase y tarea, con soluciones.** En clase: `:179-185` (15 min, solución docente `:185`). Tarea: `:187-197` (enunciado `:189`, solución `:191-195`).
- **Revisión de la tarea anterior.** `M04_libreto.md:13-15` revisa la práctica I de M03 (verificado en `M03_libreto.md:229`). M02 no lleva revisión, como se pidió.
- **Tema del PDF (M4: intervalos y pruebas).** Intervalos t: `:53-65`; pruebas, valor p y errores de decisión: `:67-83`; t pareada, Welch, chi-cuadrado, F, potencia, u(s), Grubbs y Dixon en I1–I5.
- **Scripts.** Ejecutados en copia temporal (`/tmp/verif_M04.pjM9c8`) con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`. Ambos terminan con código 0 e imprimen `comprobaciones_M04=OK` y `comprobaciones_practicas_M04=OK`.
- **Cifras del libreto frente a la salida de los scripts.** Coinciden todas las comprobadas (≈60 valores): B (media 0,0375; s 0,5263; se 0,1861; IC [−0,4025; 0,4775]; t 0,2015; p 0,8460); pareada de ejemplo (media 0,1625; IC [0,0632; 0,2618]; t 3,8697; p 0,0061); Welch de ejemplo (diferencia −0,9405; ν 10,9272; t −6,1418; IC [−1,2778; −0,6032]); chi-cuadrado (IC [0,1211; 1,1473]; χ² 7,7550; p 0,7094); F (0,8408; IC [0,1404; 5,8669]; p 0,8678); potencia (33,37 → 34; 0,4649; 25,52 → 26; 0,4658); Grubbs G 2,4374 y crítico calculado 2,2208 / bilateral 2,2744; Dixon Q 0,8214. Práctica B (IC [−0,1218; 0,4218]; t 1,3049; p 0,2332); pareada I (media 0,2250; IC [0,0928; 0,3572]; t 4,0249; p 0,0050); Welch I (A−B −0,8833; se 0,2005; ν 11; t −4,4066; p 0,0011; IC [−1,3245; −0,4421]); chi-cuadrado (s² 0,1057; IC [0,0462; 0,4379]; χ² 2,9600; p 0,2226); F (0,7152; IC [0,1195; 4,9906]; p 0,7302); potencia dos grupos 63,77 → 64 y 0,2161; u(s) 0,0869; G 2,3157; Q 0,6667.
- **Valores críticos de Otto.** Verificados en `Curso_COMPLETO/docs/Chemometrics Statistics and Computer Application.pdf`: Tabla 2.10, n = 8, Q(0,99) = 0,59 (`M04_libreto.md:175`); Tabla 2.11, n = 8, T(0,99) = 2,22 (`:173`).

## Observaciones

1. **`M04_libreto.md:55`: mención residual a M8 (fuera del curso).** El texto dice «se modela por separado en M8». El Etapa 1 (`logs_etapa1/cambios_p2.md:5`) dice que M8 se retiró de M04, así que esta frase reapareció. Debe decir «fuera del alcance de este curso» o eliminarse.

2. **`M04_libreto.md:26` y `:47`: referencias a anexos AX.1 y AX.7 que no existen en `Curso_CORTO`.** El Etapa 1 también las había retirado de M04 (`logs_etapa1/cambios_p2.md:5`). Ni la raíz ni `docs/` de `Curso_CORTO` contienen anexos. Corrección: quitar AX.1/AX.7 de la fila «Anexos» de la ficha y de la frase «la encuentran en el Anexo AX.1», o declarar que las deducciones están fuera del alcance del curso.

3. **`M04_libreto.md:209-212`: rutas `docs/` que no existen en `Curso_CORTO`.** Las referencias apuntan a `docs/Statistical Concepts – A First Course.pdf`, `docs/statistical_concepts_c05.pdf`–`c09.pdf`, `docs/ISO_IEC Guide 98-3_2008…pdf` y `docs/Chemometrics Statistics and Computer Application.pdf`. En `Curso_CORTO/docs/` solo hay dos `.xlsx` (los que usa M06). Los PDF están en `Curso_COMPLETO/docs/`. Corrección: indicar la ruta de `Curso_COMPLETO` o copiar los extractos necesarios.

## Sin cambios en esta verificación

No se editó ningún archivo del curso. Único artefacto nuevo: este informe. La copia temporal de `calc/` se creó en `/tmp` y puede borrarse.
