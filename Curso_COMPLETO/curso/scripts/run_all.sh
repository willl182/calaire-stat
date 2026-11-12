#!/usr/bin/env bash
# Orquestación completa (fases 1–3 del plan maestro). La fase 4 la hace el orquestador.
set -u
source "$(dirname "$0")/common.sh"
H=$CURSO/scripts

estado "=== FASE 1: capítulos M00–M13 ==="
printf '%s\n' M00 M01 M02 M03 M04 M05 M06 M07 M08 M09 M10 M11 M12 M13 \
  | xargs -P 7 -I{} bash "$H/run_chapter.sh" {}

estado "=== FASE 2: secciones S1–S3 y anexos AX ==="
bash "$H/run_section.sh" S1 & bash "$H/run_section.sh" S2 & bash "$H/run_section.sh" S3 &
bash "$H/run_chapter.sh" AX &
wait

estado "=== FASE 3: sección S4 ==="
bash "$H/run_section.sh" S4

estado "=== FASES 1–3 TERMINADAS ==="
grep -E 'ABORTA|COMPLETO|COMPLETA' "$LOGS/estado.log" | tail -30
