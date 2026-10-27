# Revisión final del orquestador

Fecha: 2026-10-27. Revisor: orquestador (Claude Code). Alcance: fase de contenido de las secciones S1–S4. Las prácticas quedan como marcadores «[PRÁCTICA — fase de ejercicios]».

## Plan de revisión

1. Comprobar que el pipeline de cada sección terminó: capítulos (luna, Haiku, luna) y sección (supervisor, revisor de sección, supervisor).
2. Comprobar que cada carpeta `auditoria_*` está registrada en la revisión del supervisor o del revisor de sección.
3. Comprobar que cada hallazgo O-… del revisor de sección tiene una decisión registrada.
4. Ejecutar todos los scripts de `calc/` con `curso/.venv/bin/python`.
5. Resolver el pendiente que cruza secciones, S3 O-02 (atribución de ARL a M11 en AX.12).
6. Listar los pendientes que no bloquean la entrega.

## Ejecución

### 1. Estado del pipeline (`logs/estado.log`)

| Sección | Capítulos | Supervisor (P4/P6) | Revisor de sección (P5) | Estado |
|---|---|---|---|---|
| S1 Fundamentos | M00–M04 | claude-sol; Opus 5.5 low como respaldo por cuota | Opus 5.5 | COMPLETA |
| S2 Modelos y calibración | M05–M08 | P4: Opus 5.5 low (respaldo); P6: claude-sol low | Opus 5.5 (terminó a las 01:05:54) | COMPLETA (01:14:52) |
| S3 Comparación y decisión | M09–M12 | claude-sol; Opus 5.5 low como respaldo | Opus 5.5 | COMPLETA |
| S4 Numéricos e integración | M13, AX | claude-sol; Opus 5.5 low como respaldo | Opus 5.5 | COMPLETA |

Desde la reanudación 6 (2026-10-27), por decisión del usuario, solo se usan `claude-sol`, `claude-luna` y Haiku 5.5, todos con `--effort low`, y no hay respaldo Opus (`scripts/common.sh`). La revisión P5 de S2 ya estaba terminada y se conservó.

### 2. Carpetas de auditoría

Cada carpeta está citada al menos una vez en `Sx_revision_sol.md` o `Sx_revision_opus.md`:

- S1: `auditoria_interrupcion_sol`, `_sol_2`, `auditoria_respaldo_20261026_053907`, `_200841`, `_201402`.
- S2: `auditoria_interrupcion_sol_2`, `_sol_3`, `auditoria_respaldo_20261026_195250`, `_200841`, `_201411`.
- S3: `auditoria_interrupcion_sol_2`, `_sol_4`, `auditoria_respaldo_20261026_200841`, `_201526`.
- S4: `auditoria_respaldo_20261026_053904`.

Los revisores de sección declaran todas las ediciones interrumpidas decididas y registradas.

### 3. Hallazgos del revisor de sección y decisiones

| Sección | Hallazgos O-… | Aplicado | Aplicado con cambios | Rechazado |
|---|---|---|---|---|
| S1 | 14 | 9 | 5 | 0 |
| S2 | 18 (0 críticos, 3 mayores, 15 menores) | 12 | 6 | 0 |
| S3 | 17 (0 críticos, 1 mayor, 16 menores) | 11 | 6 | 0 |
| S4 | 17 | 17 | 0 | 0 |

En S2, los ids del supervisor tienen la forma `S-M05…`/`S-T01…` (no `S-01`). Esto es coherente con su tabla y no es un hallazgo.

### 4. Scripts de cálculo

- S1 (10 scripts), S3 (8) y S4 (14): todos terminan con rc=0.
- S2, scripts docentes: `M05_diseno`, `M06_ejemplos`, `M06_RR_CALAIRE`, `M07_ejemplos` y `M08_ejemplos` terminan con rc=0. Los auxiliares `auditoria_entrega_sol`, `continuidad_auditorias_sol`, `m07m08_verificacion_independiente` y `trazabilidad_bloques_sol` también.
- S2, scripts de parche de una sola pasada de sol (`ajustes_sol.py`, `correcciones_opus_sol.py`, `correcciones_M08_opus_sol.py`): se cortan a propósito porque ya fueron aplicados. Al ejecutarlos no se modificó ningún libreto (comprobado por la hora de modificación). No son material docente.
- **Corrección del orquestador:** `S2_modelos_calibracion/calc/verificacion_M05_M06_final_sol.py` fallaba (`TypeError: 'int' object is not callable`). El bucle factorial de las líneas 43–45 usaba `C` como variable y tapaba el `C()` de patsy en las fórmulas posteriores. Renombré la variable a `Cx`, sin cambios en la lógica. Resultado: 29 comprobaciones, 0 FAIL.

### 5. Pendiente que cruza secciones: S3 O-02

- Problema: AX.12 (`S4_numericos_integracion/AX_libreto.md:315`) decía que «M11-A usa la varianza y ARL». En realidad M11-A compara EWMA L=2,7 y CUSUM bilateral mediante probabilidades de alarma en un horizonte y demoras condicionadas, que no son ARL.
- Ronda 1: claude-luna (low) reescribió el párrafo; Haiku 5.5 (low) lo revisó en `AX_revision_haiku_O02.md` y emitió H-01..H-03.
- Ronda 2: claude-luna (low) aplicó H-01 (el CUSUM de AX.12 usa los mismos k=0,5 y h=5 que M11, solo la suma superior) y H-03 (frases cortas para lectura oral). H-02 (unificar la clave «Montgomery» con «Montgomery 2013» de M11) queda como pendiente bibliográfico. Todo está registrado en `AX_bitacora_luna.md`.
- Verificación del orquestador: k=.5 y límite 5. en `calc/AX_12.py:18`; el script termina con rc=0. Las cifras de ARL no cambiaron. O-02 queda cerrado.

## Pendientes que no bloquean la entrega

1. Hay 57 citas marcadas «no disponible en docs/» (obras externas como Montgomery). Hay que cotejar edición, numeral y página con la obra física o digital antes de impartir el curso, y unificar las claves bibliográficas entre capítulos (por ejemplo, H-02 de O-02).
2. S2: validación histórica del R&R con datos reales de CALAIRE (señalada por el supervisor).
3. S3: grafía «<+ 1 ppb» del QAPP.
4. Fase de ejercicios: desarrollar los marcadores de práctica (3 por capítulo en M00–M12, 1 en M13).
5. Los cambios del curso no se han confirmado en git (`git status` muestra los libretos modificados respecto de `437e8bf`).

## Veredicto

**Fase de contenido aprobada.** Las cuatro secciones están completas, todos los hallazgos del revisor de sección están decididos (66 en total, ninguno rechazado), todas las auditorías están registradas, todos los scripts docentes se reproducen y el pendiente S3 O-02 está cerrado. Como señalan los supervisores (prop_e §10), el curso no está listo para impartir hasta cerrar los pendientes 1 y 4.
