# Verificación de la ronda r1

Fecha: 2026-11-11. Directorio: `Curso_CORTO/`. Fuente de hallazgos: `logs_etapa1/verif_sol_etapa1.md`. Registro de cambios: `logs_etapa1/ronda2/cambios_r1.md`. No se editó ningún archivo; los cambios de otros agentes se ignoraron.

## Veredicto

**CON OBSERVACIONES.**

Los hallazgos asignados a r1 (F01, F02, F05) quedaron resueltos y el texto vecino se mantiene coherente. La observación 5.4 quedó resuelta. La observación 5.6 quedó resuelta solo en parte: la delimitación de exclusiones sigue repetida dentro de los mismos párrafos de M02 y M06.

## Comprobación por hallazgo

| Hallazgo | Ubicación | Estado | Comentario |
|---|---|---|---|
| F01 — referencia a M1 | `M03_libreto.md:18` | Resuelto | Ahora remite al punto de partida de M02 y a la ecuación del SRP presentada allí. No queda ninguna mención a M1 en M02–M06 (grep de `M1`, `M7`–`M13`, `AX.x`, `S2`). |
| F02 — promesas de módulos excluidos | `M03_libreto.md:326` | Resuelto | Ya no promete trabajar con covarianza cero; la exclusión de GGMR, PCR, PLS y quimiometría queda declarada una vez. |
| F02 | `M03_libreto.md:354` | Resuelto | La remisión a exclusiones se sustituye por instrucción de escalamiento al especialista. Coherente con `:326`. |
| F02 | `M05_libreto.md:78` | Resuelto | La evolución temporal se atribuye a M02 (que sí trata serie temporal, `M02_libreto.md:86`). Regresión y control se declaran fuera del curso. |
| F02 | `M06_libreto.md:283` | Resuelto | El cierre del curso corto reemplaza la promesa del módulo siguiente; el ajuste referencia–indicación queda fuera. |
| F05 — unidades y condición del SRP | `M02_libreto.md:18` | Resuelto | Declara $c$ en atm, $\alpha$ en atm⁻¹ cm⁻¹, $L$ en cm, $Y=(c/p_0)\cdot10^9$ en nmol/mol y el carácter de modelo simplificado a condiciones estándar. Consistente con `../Curso_COMPLETO/curso/S1_fundamentos/M01_libreto.md:60–64`. |
| Obs. 5.4 — «ya damos por visto» | `M02_libreto.md:22` | Resuelto | Sustituido por una transición que recuerda que las definiciones se acaban de presentar. |
| Obs. 5.6 — exclusiones repetidas | `M02_libreto.md:128` | Parcial | Se delimitó lo de pocos grados de libertad, pero el párrafo sigue repitiendo «fuera del alcance de este curso» dos veces y «no forma parte de este curso corto» una tercera. |
| Obs. 5.6 | `M06_libreto.md:46` | Parcial | El párrafo sigue afirmando dos veces que el presupuesto completo queda fuera (`«no reemplaza un presupuesto completo»` y «construir el presupuesto completo queda fuera del alcance de este curso»). El cambio declarado en `cambios_r1.md` no quedó del todo reflejado. |

## Texto vecino

- `M02_libreto.md:8–10`, `M03_libreto.md:8`: las fichas no se alteraron en sentido contrario; siguen coherentes con el punto de partida.
- `M02_libreto.md:18–22`: la nueva ecuación y la transición encajan con la siguiente escena; no hay duplicación de la apertura.
- `M03_libreto.md:324–328` y `:352–356`: la delimitación de GGMR y el escalamiento se leen de forma consistente.
- `M06_libreto.md:281–283`: el párrafo anterior sigue intacto y el cierre enlaza bien.

No se detectó pérdida de contenido ni duplicación introducida por r1 en los rangos revisados.

## Ejecución de `calc/`

`cambios_r1.md` no registra cambios en `calc/`. Sin embargo, tres scripts tienen mtime posterior al informe de verificación (`calc/M02_examples.py`, `calc/M05_diseno.py`, `calc/M06_practica_I_grafico.py`). Se ejecutaron con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I` dentro de una copia temporal (`/tmp/verif_r1_ygjw/Curso_CORTO`), para no escribir sobre el árbol de trabajo:

| Script | Código de salida | stderr |
|---|---:|---|
| `calc/M02_examples.py` | 0 | vacío |
| `calc/M05_diseno.py` | 0 | vacío |
| `calc/M06_practica_I_grafico.py` | 0 | vacío |

No se comprobó si esos cambios de `calc/` son de r1 o de otro agente; al no figurar en `cambios_r1.md`, se tratan como ajenos a r1.

## Observaciones

1. **Obs. 5.6 incompleta** — `M02_libreto.md:128`: la delimitación de exclusiones sigue redundante dentro del mismo párrafo. Restringir cada «fuera del alcance» a su tema concreto cerraría el punto.
2. **Obs. 5.6 incompleta** — `M06_libreto.md:46`: el párrafo repite la exclusión del presupuesto completo. `cambios_r1.md` afirma que se eliminó la repetición; no es así todavía.
3. **Registro desfasado** — `M02_libreto.md` tiene mtime 21:39:12, posterior a `cambios_r1.md` (21:38:39). Otro agente pudo editarlo después; el estado verificado es el actual, pero `cambios_r1.md` no describe esa edición.
4. **Pendientes ajenos a r1, no evaluados aquí:** F03 (`M02_libreto.md:174`, ajuste de la recta no enseñado), F04, F06 y F07 siguen fuera del alcance de r1.

## Balance

Hallazgos F01, F02 y F05 y observación 5.4 resueltos sin romper el texto vecino. Observación 5.6 resuelta solo parcialmente en `M02_libreto.md:128` y `M06_libreto.md:46`. Ningún cambio de r1 requiere reversión.
