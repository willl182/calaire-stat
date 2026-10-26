# S1. Revisión de contenido y entrega — Sol

Fecha: 25 de octubre de 2026. Alcance de edición: exclusivamente `curso/S1_fundamentos/`. Fase: solo contenido; no acredita preparación de prácticas ni autorización para impartir.

## Plan de revisión

Plan registrado antes de revisar los capítulos. Se han leído íntegramente `curso/00_plan_maestro.md`, `curso/guia_libreto.md`, `prop_e.md` y `revision_final_prop_e.md`.

1. Leer, en orden M00 → M04, cada libreto, bitácora y revisión Haiku, sin dar por verificados sus dictámenes. Construir una correspondencia entre todos los contenidos B/I/A de prop_e §5 y las escenas; comprobar niveles acumulativos y exclusiones de §6.
2. Revisar corrección estadística y metrológica, notación, supuestos, unidad de repetición, escala, signo, cobertura, errores críticos y escalamiento. Distinguir ejemplos docentes resueltos de prácticas: conservar exactamente un marcador por práctica curricular y no desarrollar ejercicios, soluciones ni rúbricas.
3. Leer y ejecutar los cinco scripts con `curso/.venv/bin/python`, sin generar archivos fuera de S1. Recalcular los valores clave con una segunda implementación o identidades independientes; comprobar correspondencia entre resultados y narración. Incorporar comprobaciones reproducibles en `calc/` cuando sea necesario.
4. Verificar las referencias técnicas y sus numerales mediante `pdftotext` sobre los PDF de `docs/`; guardar la evidencia de verificación dentro de S1. No usar prop_e como respaldo técnico. Para fuentes ausentes, identificar expresamente esa condición y no inventar numerales.
5. Revisar el formato hablado, acotaciones, lectura de fórmulas, ejemplos por tema cuantitativo, rótulos de origen, transiciones, prerrequisitos y referencias AX; eliminar duplicaciones innecesarias sin suprimir la recapitulación acumulativa.
6. Registrar hallazgos con id S-…, capítulo, ubicación, severidad, problema y corrección. Aplicar las correcciones personalmente; conservar las bitácoras y revisiones previas como antecedentes, sin reescribirlas como si fueran esta revisión.
7. Crear el índice de entrega con escenas por nivel, los quince marcadores pendientes, datos y rótulos, anexos, estado y pendientes. Cerrar con pruebas ejecutadas, límites de la verificación y estado de entrega; no declarar listo para impartir el curso.

Severidad: crítica (resultado o decisión inválidos), alta (error técnico, referencia equivocada o contenido curricular ausente), media (ambigüedad de supuestos, reproducibilidad o forma), baja (claridad editorial). No se modificarán archivos externos a S1.

## Hallazgos por capítulo

En revisión. Esta revisión fue interrumpida el 2026-10-25 a las 19:43 antes de registrar hallazgos. Ver la nota siguiente.

## Correcciones aplicadas

En revisión.

### Nota del orquestador: ediciones previas a la interrupción

Antes de la interrupción, sol aplicó 27 ediciones sin registrarlas: 25 en los libretos M00–M04 y una en `calc/M00_ejemplos.py`. Están reconstruidas y verificadas byte a byte en `auditoria_interrupcion_sol/LEEME.md` (tabla C01–C27, versiones previas `*.pre_sol.*` y `cambios_sol.diff`). Al reanudar, cada Cxx debe quedar aquí asociada a un hallazgo S-…, con su decisión (conservada, ajustada o revertida) y su justificación.
