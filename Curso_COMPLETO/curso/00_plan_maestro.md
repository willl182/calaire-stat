# Plan maestro: desarrollo del curso en formato libreto

**Fecha:** 24 de octubre de 2026.
**Base curricular:** [prop_e.md](../prop_e.md), versión final aprobada, con los ajustes de [revision_final_prop_e.md](../revision_final_prop_e.md).
**Guía de estilo y de referencias:** [guia_libreto.md](guia_libreto.md).
**Orquestador:** Claude Opus 5.5 (sesión principal). Diseña las secciones, lanza los agentes y hace la revisión final ([revision_final.md](revision_final.md)).

## 1. Qué se entrega

Un libreto por capítulo: el texto que el instructor dice en clase, con acotaciones de escena (pizarra, diapositiva, pausa, práctica). Todo se narra; no es un libro de texto. Cada concepto, definición, fórmula o criterio lleva su referencia verificable. El contenido de cada capítulo cubre los niveles B, I y A tal como los define prop_e.

**Alcance de esta fase (decisión del usuario, 24-10-2026): solo contenido.** Las prácticas, ejercicios, soluciones, evidencias, rúbricas y el taller integrador se desarrollan en una fase posterior; los libretos dejan un marcador en el lugar de cada práctica (guía §1).

## 2. Secciones y capítulos

| Sección | Directorio | Capítulos | Supervisor de sección |
|---|---|---|---|
| **S1. Fundamentos** | `S1_fundamentos/` | M00 Estructura de datos · M01 Modelo de medición · M02 Descriptiva · M03 Probabilidad y dependencia · M04 Inferencia | `claude-sol -p` |
| **S2. Modelos de la calibración** | `S2_modelos_calibracion/` | M05 Diseño · M06 ANOVA y componentes · M07 Regresión y calibración inversa · M08 Propagación | `claude-sol -p` |
| **S3. Comparación, decisión y seguimiento** | `S3_comparacion_decision/` | M09 Comparación · M10 Decisión y riesgo · M11 Control y series · M12 Indicadores | `claude-sol -p` |
| **S4. Métodos numéricos y anexos** | `S4_numericos_integracion/` | M13 Métodos numéricos (solo A) · AX Anexos de deducciones | `claude-sol -p` |

Los anexos (AX) reúnen las deducciones que los capítulos no desarrollan. Los capítulos remiten a ellos con los identificadores fijados en la guía (§7), de modo que puedan escribirse en paralelo.

## 3. Flujo de trabajo y responsables

| Paso | Agente | Modelo | Entrada | Salida (auditable) |
|---|---|---|---|---|
| 1. Desarrollo del capítulo | `claude-luna -p` | gpt-6-luna | prop_e, guía, bibliografía, casos | `MXX_libreto.md` + `MXX_bitacora_luna.md` (plan y ejecución) |
| 2. Revisión de redacción y errores | `claude --model claude-haiku-5-5 -p` | Haiku 5.5 | libreto | `MXX_revision_haiku.md` (no edita el libreto) |
| 3. Ajustes | `claude-luna -p` | gpt-6-luna | revisión Haiku | libreto corregido + sección «Correcciones» en la bitácora |
| 4. Revisión del contenido final de cada capítulo y entrega de la sección | `claude-sol -p` | gpt-6.1-sol | todos los libretos de la sección | `SX_revision_sol.md` (plan, hallazgos, correcciones aplicadas) + `SX_00_indice.md` |
| 5. Revisión de la sección entregada | `claude --model claude-opus-5-5 -p` | Opus 5.5 | sección entregada | `SX_revision_opus.md` (no edita) |
| 6. Correcciones | `claude-sol -p` | gpt-6.1-sol | revisión Opus | libretos corregidos + sección «Correcciones tras la revisión Opus» en `SX_revision_sol.md` |
| 7. Revisión final | Orquestador | Opus 5.5 | curso completo | `revision_final.md` |

Orden de ejecución:

1. **Fase 1:** pasos 1–3 de M00–M13, en paralelo (máximo 7 capítulos a la vez).
2. **Fase 2:** pasos 4–6 de S1, S2 y S3, en paralelo; a la vez, pasos 1–3 de AX (lee los capítulos de la fase 1).
3. **Fase 3:** pasos 4–6 de S4.
4. **Fase 4:** revisión final del orquestador.

Los scripts están en `scripts/` y la salida de consola de cada agente en `logs/`.

## 4. Reglas que todos los agentes cumplen

1. Es un curso **de estadística** aplicado a la fotometría de ozono y al SRP; el dominio aporta datos y casos (prop_e §1).
2. Los niveles son acumulativos y cada tema incluido en un nivel se enseña, se practica y se evalúa en clase. Nunca «lectura», «para mostrar» ni «opcional».
3. Las deducciones van a AX. Las prácticas (de aplicación) se desarrollan en la fase de ejercicios.
4. Las exclusiones de prop_e §6 se respetan (ISO 13528, z, ζ, Mandel, PCR/PLS, Allan, GGMR con `V_xy ≠ 0`, KCRV combinado, protocolo de BIPM.QM-K1 y KCDB).
5. Ningún resultado simulado o adaptado se atribuye al laboratorio.
6. Los números de los ejemplos se calculan con código (Python) que queda en `SX/calc/`, y la bitácora registra cómo se verificaron.
7. No se inventan referencias ni numerales: se verifican en `docs/` (con `pdftotext`) o se marcan como pendientes.
8. Cada agente deja su archivo `.md` de trabajo: qué planificó, qué hizo y qué corrigió.
9. Ningún agente modifica archivos fuera de `curso/`.
