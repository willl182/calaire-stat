#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"
D=curso/S4_numericos_integracion
P="Eres claude-luna, autor del anexo AX. Trabajas en ${ROOT}. Lee ${D}/AX_revision_haiku_O02.md y aplica sus hallazgos al párrafo de AX.12 de ${D}/AX_libreto.md (línea que empieza «En M11-A usamos la varianza del EWMA»): H-01 (verifica primero en ${D}/calc/AX_12.py y en curso/S3_comparacion_decision/M11_libreto.md que k=0,5 y h=5 coinciden; si es así, precisa que el CUSUM de AX.12 usa los mismos k y h pero solo la suma superior) y H-03 (parte la frase para lectura oral). H-02: no cambies la referencia; anótalo como pendiente bibliográfico. No cambies cifras ni scripts ni archivos fuera de ${D}/. Añade a ${D}/AX_bitacora_luna.md «## Ajustes tras revisión Haiku O-02» con decisión por H-01..H-03 (aplicado/rechazado, texto, justificación). Responde solo 'hecho'."
run_agent luna "$LOGS/S4_O02_luna2.log" "$ROOT/$D/AX_bitacora_luna.md" "$P" || { estado "ABORTA O-02 ajuste luna"; exit 1; }
estado "O-02 AX.12 AJUSTES COMPLETO"
