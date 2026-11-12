# Verificación de M05 — etapa 2

**Veredicto: CON OBSERVACIONES**

El libreto cumple la estructura pedida: sin residuos del nivel A, agenda de 120 min, práctica B en clase, práctica I partida (clase 15 min + tarea) con soluciones, revisión de la tarea anterior y los dos scripts reproducen las cifras narradas. Quedan dos observaciones sustantivas (cobertura del PDF) y un residuo fuera del libreto.

## Comprobaciones

| Punto | Resultado |
|---|---|
| Nivel A retirado en `M05_libreto.md` | Cumple. No hay «Nivel A», «práctica A», «A1/A2» ni referencias a M7–M12 o AX. |
| Agenda de sesión de 120 min | Cumple. `M05_libreto.md:3–11`: 15 + 45 + 25 + 15 + 20 = 120. |
| Revisión de la tarea anterior | Cumple. `M05_libreto.md:14–16` (15 min). M02 no la lleva, como corresponde. |
| Práctica B en clase | Cumple. `M05_libreto.md:110–116` (25 min), con solución docente en `:116`. |
| Práctica I en clase y tarea, con soluciones | Cumple. En clase: `:188–205` (15 min; solución en `:205`). Tarea: `:211–217` (solución en `:217`). |
| Tareas específicas del módulo | Cumplen: jerarquía lectura–ciclo–día, unidades y réplicas, bloqueo, factorial 2³, robustez con escalamiento, reparto del esfuerzo y potencia. |
| Scripts con `-I`, en copia temporal | Ambos terminan con rc=0 (`calc/M05_diseno.py`, `calc/M05_practicas_luna.py`). |
| Cifras del libreto frente a salida de scripts | Coinciden: 0,40 / 0,20 / 0,80 / 0,60; 576 = 480 + 96; efectos F 0,80, C 0,20, T −0,10; interacción F×C 0,30; contraste F alto–T alto 1,22; cuatro contrastes > 0,50 (0,54, 0,98, 1,22, 0,56); potencias 0,284 y 0,495; u = 0,083 / 0,082 / 0,059 (`:180`); 4 y 6 días con sd 0,2021 y 0,2031. |

## Cobertura del tema del PDF (M5: planificación de comparaciones)

Cubierta: planificación de comparaciones, factores y niveles, estructura cruzada/anidada, factorial, potencia aplicada al diseño y EN 14625 como ensayo de un factor a la vez.

Quedan dos huecos frente a `Curso_COMPLETO/temario_curso.md:181–198, 217`. No encontré `Temario estadistica.pdf` en el árbol; uso el temario en Markdown como fuente del PDF:

1. **Diseños anidados escalonados para precisión intermedia** (`temario_curso.md:191`). Estaban en la práctica A retirada; el libreto solo los nombra de paso en `M05_libreto.md:64–66` (anidado) y no los desarrolla.
2. **Juicio sobre si 6 días bastan para la componente entre días del 12 × 8 × 6** (`temario_curso.md:217`). `M05_libreto.md:78–86` describe el diseño pero no contesta si los 6 días bastan; el cálculo de `:180` solo lo ilustra con datos simulados.

## Hallazgos

1. **CON OBSERVACIONES — residuo del nivel A fuera del libreto.** `M05_practicas_luna.md:15–16, 25, 43–44` (y su encabezado en `:1–3`) sigue describiendo la práctica A (H-05, H-06, H-14, «A base», «A con 6 analistas»), con rutas a `../Curso_COMPLETO`. Está en la raíz de `Curso_CORTO` con nombre `M05_*`, aunque no es el libreto ni un script. Conviene retirarlo o reescribirlo como bitácora de B/I. Esta verificación no lo edita.
2. **CON OBSERVACIONES — cobertura PDF M5: escalonado.** Falta tratar el diseño anidado escalonado de ISO 5725-3 (`temario_curso.md:191`), que el libreto ya no contiene (`M05_libreto.md:64–66`). Es una decisión de alcance a confirmar con quien planifica; si se deja fuera, debe anotarse en el plan como excepción.
3. **CON OBSERVACIONES — cobertura PDF M5: suficiencia de días.** `M05_libreto.md:78–86` no responde si 6 días bastan para estimar la componente entre días (`temario_curso.md:217`). Una frase en B3 o en el cierre bastaría.
4. **Observación menor — dependencias fuera de la copia.** `M05_libreto.md:28, 229–243` cita `../Curso_COMPLETO/docs/…` y `../Curso_COMPLETO/curso/S2_modelos_calibracion/M05_bitacora_luna.md`. `Curso_CORTO/docs/` solo tiene dos `.xlsx`. La copia no es autocontenida; si se entrega aparte, esas rutas se rompen.
5. **Observación menor — trazabilidad.** `logs_etapa2/cambios_M05.md` declara «calc/M05_practicas_luna.py: encabezado y cálculos limitados a B/I». Es cierto para el script (no hay cálculos de A), pero el registro de cambios no menciona que `M05_practicas_luna.md` quedó sin actualizar (ver hallazgo 1).

## Sin cambios

No se editó ningún archivo del curso. Solo se escribió este registro.
