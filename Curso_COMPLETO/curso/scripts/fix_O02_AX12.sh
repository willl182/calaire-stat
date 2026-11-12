#!/usr/bin/env bash
# Pendiente cruzado S3 O-02: atribución de ARL a M11 en AX.12. luna corrige, Haiku revisa.
source "$(dirname "$0")/common.sh"
D=curso/S4_numericos_integracion
instantanea curso/S4_numericos_integracion antes_O02 "$ROOT/$D/AX_libreto.md" "$ROOT/$D/AX_bitacora_luna.md"
P1="Eres claude-luna, autor del anexo AX. Trabajas en ${ROOT}. Lee curso/guia_libreto.md, ${D}/AX_libreto.md (sección AX.12, en especial el párrafo que empieza «M11-A usa la varianza y ARL») y curso/S3_comparacion_decision/M11_libreto.md (bloques A1–A2, líneas con 'ARL' y 'demora') y la nota de coordinación O-02 al final de curso/S3_comparacion_decision/S3_revision_sol.md.
Problema: AX.12 atribuye a M11-A el uso de ARL, pero M11-A usa EWMA L=2,7 y CUSUM bilateral, probabilidades de alarma en un horizonte y demoras condicionadas (que M11 declara que NO son ARL); el ejemplo de AX.12 usa EWMA L=3 y CUSUM unilateral.
Tarea: reescribe SOLO ese párrafo de AX.12 en estilo libreto narrado para que describa con exactitud qué hace M11-A, diga que el ejemplo de AX.12 usa otros parámetros a modo de contraste, y que el ARL es la herramienta complementaria de AX.12, no la que usa M11-A. Mantén la referencia existente. No cambies cifras ni scripts. No toques archivos fuera de ${D}/.
Registra en ${D}/AX_bitacora_luna.md una sección «## Corrección O-02 (S3, 2026-10-27)» con planificación, texto anterior, texto nuevo y justificación. Responde solo 'hecho'."
run_agent luna "$LOGS/S4_O02_luna.log" "$ROOT/$D/AX_bitacora_luna.md" "$P1" || { estado "ABORTA O-02 luna"; exit 1; }
P2="Eres el revisor de redacción y errores (Haiku 5.5). Trabajas en ${ROOT}. Revisa la corrección O-02 registrada al final de ${D}/AX_bitacora_luna.md y el párrafo resultante en ${D}/AX_libreto.md (AX.12), contrastándolo con curso/S3_comparacion_decision/M11_libreto.md (A1–A2). Verifica: exactitud de lo atribuido a M11-A (EWMA L=2,7, CUSUM bilateral, probabilidad en horizonte, demora condicional, no ARL), redacción oral, referencia conservada. NO edites el libreto. Escribe ${D}/AX_revision_haiku_O02.md con «## Plan», «## Hallazgos» (tabla id H-…, ubicación, problema, corrección propuesta) y «## Veredicto». Responde solo con el veredicto."
run_agent haiku "$LOGS/S4_O02_haiku.log" "$ROOT/$D/AX_revision_haiku_O02.md" "$P2" || { estado "ABORTA O-02 haiku"; exit 1; }
estado "O-02 AX.12 COMPLETO (luna + haiku)"
