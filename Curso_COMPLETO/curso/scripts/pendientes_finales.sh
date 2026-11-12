#!/usr/bin/env bash
# Dos supervisores claude-sol (esfuerzo bajo): citas (pendiente 1) y demás pendientes (2–4) de revision_final.md.
# Cada supervisor delega en claude-luna (ejecuta) y Haiku 5.5 (revisa a luna), todos con esfuerzo bajo.
source "$(dirname "$0")/common.sh"
# Reemplazo (usuario, 2026-10-27): supervisor Opus 5.5 low en lugar de sol; ejecutor Haiku 5.5 low en lugar de luna.
SOL_CMD=(env -u ANTHROPIC_BASE_URL -u ANTHROPIC_API_KEY claude --model claude-opus-5-5 --effort low)
H1=curso/logs/hitos_citas.md; H2=curso/logs/hitos_pendientes.md
REGLAS="Reglas de delegación (obligatorias):
- Ejecutor (reemplaza a claude-luna): ( cd ${ROOT} && env -u ANTHROPIC_BASE_URL -u ANTHROPIC_API_KEY -u CLAUDE_CODE_AUTO_MODE_SERVER claude --model claude-haiku-5-5 --effort low -p --dangerously-skip-permissions --output-format text \"<prompt>\" ) — trabaja y edita archivos.
- Revisor de luna: ( cd ${ROOT} && env -u ANTHROPIC_BASE_URL -u ANTHROPIC_API_KEY -u CLAUDE_CODE_AUTO_MODE_SERVER claude --model claude-haiku-5-5 --effort low -p --dangerously-skip-permissions --output-format text \"<prompt>\" ) — NO edita libretos; escribe un archivo de revisión con hallazgos H-xx; luego luna aplica o rechaza con justificación.
- Tú supervisas: defines hitos, das prompts precisos con rutas, verificas el resultado (lee los archivos, no confíes solo en la respuesta) y decides. No edites libretos tú mismo salvo correcciones triviales del orquestador.
- Lee curso/guia_libreto.md y curso/revision_final.md. El curso es para operadores del SRP del laboratorio designado (INM), aplicado al ozono; prácticas aplicadas, demostraciones a anexos.
- No hagas commits git.
- Usa corridas separadas de Haiku para ejecutar y para revisar. Donde los registros digan luna, el nuevo ejecutor continúa su trabajo.
- REANUDACIÓN: una corrida previa se cortó porque Haiku se invocaba con la URL del proxy (error 400 unknown provider). El comando de Haiku ya está corregido (env -u ...). Lee REPORTE y los logs previos, no rehagas lo hecho: primero pasa a Haiku lo que quedó sin revisar, luego continúa. Añade los nuevos hitos al final de REPORTE (no borres lo anterior).
- REPORTE POR HITO: cada vez que cierres un hito, añade a REPORTE una sección «## Hito N — <nombre> — $(date +%F) HH:MM» con: qué se hizo, archivos tocados, hallazgos Haiku y decisión, estado (cerrado/bloqueado y por qué). Al terminar, una sección «## Cierre» con el resumen. Responde solo 'hecho'."

P1="Eres el supervisor (Opus 5.5, reemplaza a claude-sol por cuota agotada) del cotejo de referencias del curso en ${ROOT}/curso. Pendiente 1 de curso/revision_final.md: 57 citas marcadas «no disponible en docs/». Hitos sugeridos: (1) inventario de todas las citas y claves bibliográficas por capítulo (curso/**/M*_libreto.md, AX_libreto.md) en curso/citas/inventario.md; (2) luna coteja cada cita (edición, numeral, página) contra docs/ y fuentes de acceso abierto verificables, marcando verificada / corregida / no verificable con motivo — nunca inventes páginas; (3) unificación de claves entre capítulos (incluido H-02 de O-02: «Montgomery» vs «Montgomery 2013»); (4) Haiku revisa cada lote de luna, luna ajusta. Trabaja por lotes (una sección S1–S4 por hito). REPORTE=${H1}.
${REGLAS//REPORTE/${H1}}"

P2="Eres el supervisor (Opus 5.5, reemplaza a claude-sol por cuota agotada) de los demás pendientes del curso en ${ROOT}/curso (pendientes 2–4 de curso/revision_final.md; el 1, citas, lo lleva otro supervisor en paralelo: no toques referencias bibliográficas; el 5, git, no se hace). Hitos: (A) pendiente 3: grafía «<+ 1 ppb» del QAPP en S3 — verifica contra docs/ y corrige; (B) pendiente 2: validación histórica del R&R de S2 con datos reales de CALAIRE — busca datos en el repositorio (docs/, casos_taller/); si existen, luna hace el análisis con script reproducible en calc/; si no, deja el pendiente bloqueado con la lista exacta de datos requeridos; (C) pendiente 4: desarrollar los marcadores de práctica (3 por capítulo M00–M12, 1 en M13) como ejercicios aplicados al caso ozono/SRP, un capítulo por hito, con Haiku revisando cada capítulo. REPORTE=${H2}.
${REGLAS//REPORTE/${H2}}"

estado "INICIO pendientes_finales (2 supervisores sol)"
run_agent sol "$LOGS/sup_citas_sol.log" "$ROOT/$H1" "$P1" & a=$!
run_agent sol "$LOGS/sup_pendientes_sol.log" "$ROOT/$H2" "$P2" & b=$!
wait $a; ra=$?; wait $b; rb=$?
estado "FIN pendientes_finales citas rc=$ra pendientes rc=$rb"
