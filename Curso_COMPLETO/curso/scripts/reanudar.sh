#!/usr/bin/env bash
# Reanudación tras el corte de red del 2026-10-24 16:44 (ver logs/estado.log).
# Fase 1 pendiente: M07 y M11 desde ajustes (3); M08, M09, M10, M12, M13 desde Haiku (2).
set -u
source "$(dirname "$0")/common.sh"
H=$CURSO/scripts

estado "=== REANUDACIÓN: fase 1 pendiente ==="
printf '%s\n' "M07 3" "M11 3" "M08 2" "M09 2" "M10 2" "M12 2" "M13 2" \
  | xargs -P 7 -L1 bash "$H/run_chapter.sh"

estado "=== FASE 2: secciones S1–S3 y anexos AX ==="
bash "$H/run_section.sh" S1 & bash "$H/run_section.sh" S2 & bash "$H/run_section.sh" S3 &
bash "$H/run_chapter.sh" AX &
wait

estado "=== FASE 3: sección S4 ==="
bash "$H/run_section.sh" S4

estado "=== FASES 1–3 TERMINADAS (reanudación) ==="
