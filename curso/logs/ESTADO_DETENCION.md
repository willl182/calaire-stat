# Estado al detener la orquestación — 2026-10-25 19:43

Detenido a petición del usuario. Ningún proceso de agente queda en ejecución.

## Capítulos (pasos 1 desarrollo luna → 2 revisión Haiku → 3 ajustes luna)

| Cap. | Paso 1 | Paso 2 | Paso 3 | Estado |
|---|---|---|---|---|
| M00–M06 | ✔ | ✔ | ✔ | completos (2026-10-24) |
| M07, M09–M13 | ✔ | ✔ | ✔ | completos (2026-10-25) |
| M08 | ✔ | ✔ | ✔ (tabla «Correcciones» R01–R16 escrita) | detenido justo al terminar; no quedó registrado «COMPLETO» en estado.log |
| AX | ✔ (13 anexos, «Plan» y «Ejecución») | ✘ | ✘ | falta la revisión Haiku y los ajustes |

## Secciones (paso 4 sol → 5 Opus → 6 correcciones sol)

| Sec. | Paso 4 | Paso 5 | Paso 6 | Estado |
|---|---|---|---|---|
| S1 | interrumpido: había creado S1_revision_sol.md (solo «Plan de revisión»), las salidas `calc/*_salida_sol.txt` y había editado M00–M04 y `calc/M00_ejemplos.py` (27 ediciones, 19:39–19:42) sin registrarlas. **Ediciones reconstruidas y verificadas byte a byte en `S1_fundamentos/auditoria_interrupcion_sol/`** (C01–C27, versiones previas, diff) | ✘ | ✘ | rehacer el paso 4; el prompt obliga a decidir y registrar cada Cxx |
| S2 | ✘ (esperaba a M08) | ✘ | ✘ | no iniciada |
| S3 | interrumpido: solo «Plan de revisión» en S3_revision_sol.md | ✘ | ✘ | rehacer el paso 4 |
| S4 | ✘ (esperaba a AX) | ✘ | ✘ | no iniciada |

## Reanudación
`bash scripts/run_chapter.sh AX 2`, y luego `scripts/run_section.sh S1|S2|S3|S4` (S4 después de AX).

Desde ahora, antes de cada paso que edita libretos (P3, P4, P6), se guarda una instantánea en `<sección>/versiones/<fecha>_<paso>/`.

## Reanudación 2 — 2026-10-25 20:21
- Entorno migrado a `/home/w182`: `ROOT` de `common.sh` ahora se calcula desde la ubicación del script; `.venv` recreado; los 28 scripts de `calc/` corren sin error.
- `claude-sol` y `claude-luna` verificados (responden con `-p`).
- M08 marcado COMPLETO (paso 3 terminado, tabla R01–R16).
- S3: las ediciones de sol no existían (solo «Plan de revisión»); se rehace el paso 4 desde ese plan.
- Lanzado `scripts/reanudar2.sh`: S1, S2, S3 (pasos 4–6) en paralelo; AX pasos 2–3 y luego S4.

## Cuota de sol agotada y sustitución — 2026-10-25 22:00
- 20:30–20:31: los pasos 4 de S1, S2 y S3 fallaron o quedaron bloqueados con `429 usage_limit_reached` (gpt-6.1-sol; también gpt-5.6-sol). Habían editado libretos sin registrar: evidencias en `<sección>/auditoria_interrupcion_sol_2/` (diff contra `versiones/20261025_202101_antes_P4_sol`).
- S4 se pausó antes del paso 4 sin trabajo (cierre suave pedido por el usuario a las 20:26). AX completo.
- **Decisión del usuario (25-10-2026):** los pasos de supervisor (4 y 6) los hace **Opus 5.5 con esfuerzo bajo** (`claude --model claude-opus-5-5 --effort low -p`) en lugar de `claude-sol -p`. El paso 5 sigue siendo Opus 5.5 (esfuerzo por defecto). Configurado en `scripts/common.sh` (`SUPERVISOR_CMD`).
- Reanudado con `scripts/reanudar_pausa.sh`: S1, S2, S3 y S4 desde el paso 4.

## Límite de sesión y reanudación 3 — 2026-10-26 05:26
- 22:04–22:11 del 25-10: todos los agentes Claude (supervisor sustituto y Opus) fallaron con «You've hit your session limit · resets 12:10am»; S1, S2, S3 abortaron en el paso 4 y S4 en el paso 5 (su paso 4 sí terminó a las 22:03 con Opus 5.5 de esfuerzo bajo y quedó registrado).
- S2 dejó ediciones sin registrar del intento de las 22:00: `S2_modelos_calibracion/auditoria_interrupcion_sol_3/` (32 bloques). S1 y S3 no cambiaron.
- `run_agent` (common.sh): el supervisor vuelve a ser `claude-sol -p`; si responde `usage_limit_reached`, el mismo paso sigue con Opus 5.5 de esfuerzo bajo (respaldo, línea RESPALDO en estado.log). Ante «session limit» de Claude espera 30 min sin gastar reintentos (hasta 16 esperas). El supervisor declara su identidad en «## Nota del supervisor».
- Reanudación: S1, S2, S3 desde el paso 4; S4 desde el paso 5.

## Reanudación 4 — 2026-10-26 19:53
- 05:46–07:18 del 26-10: los pasos 5 de S1 y S3 y el respaldo de S2 esperaron el límite de sesión de Claude (reset 10:20). Después la orquestación quedó sin procesos.
- S4 COMPLETA (05:41). S1 y S3 terminaron el paso 4. S2 quedó a medias en el paso 4: claude-sol editó los 4 libretos (05:26–05:48) sin registrar nada. Evidencia en `S2_modelos_calibracion/auditoria_respaldo_20261026_195250/` (40 bloques).
- Auditorías de respaldo de S1 (`auditoria_respaldo_20261026_053907`) y S3 (`auditoria_interrupcion_sol_4`): el paso 4 de esas secciones terminó sin conocerlas. Ahora el paso 5 (Opus) revisa explícitamente todas las carpetas `auditoria_*` y el paso 4 incluye también las `auditoria_respaldo_*`.
- Reanudado: S1 desde el paso 5, S2 desde el paso 4 y S3 desde el paso 5. Supervisor: claude-sol, con respaldo Opus 5.5 low.

## Reinicio de T3 y reanudación 5 — 2026-10-26 20:08
- Hacia las 20:05 del 26-10, un reinicio del servidor T3 mató la orquestación (los procesos con setsid también murieron). S1 y S3 terminaron el paso 5 (Opus) y estaban en el paso 6 (sol); S2 estaba en el paso 4 (sol).
- Ediciones parciales auditadas en `auditoria_respaldo_20261026_200841/` (S1: 23, S2: 19, S3: 24 bloques). El paso 6 ahora incorpora las `auditoria_respaldo_*` posteriores a la revisión Opus.
- Relanzado con `systemd-run --user` (unidades `curso-orq` y `curso-guardian`), fuera del cgroup de T3: S1 desde el paso 6, S2 desde el paso 4 y S3 desde el paso 6.

## Reanudación 6 (2026-10-27)
- Decisión del usuario: no usar más agentes Opus 5.5; solo `claude-sol -p`, `claude-luna -p` y Haiku 5.5, todos con `--effort low`. Sin respaldo Opus: cuota de sol agotada ⇒ espera 30 min y reintento con sol.
- S2 P5 (revisión de sección) ya había terminado con Opus 5.5 a las 01:05:54 (18 hallazgos: 0 críticos, 3 mayores, 15 menores); se conserva. P6 de sol se detuvo al arrancar (01:05:54) sin editar libretos (cmp con la instantánea 20261027_010554_antes_P6_sol: sin cambios).
- Para futuras revisiones de sección (P5) el revisor pasa a Haiku 5.5 low.
- Se relanza `run_section.sh S2 6`.
