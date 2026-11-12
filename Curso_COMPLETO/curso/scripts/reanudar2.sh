#!/usr/bin/env bash
# Reanudación del 2026-10-25 tras la detención de las 19:43 (ver logs/ESTADO_DETENCION.md).
# M00–M13 completos. Pendiente: AX pasos 2–3; secciones S1–S4 pasos 4–6 (S4 tras AX).
set -u
source "$(dirname "$0")/common.sh"
H=$CURSO/scripts

estado "=== REANUDACIÓN 2: secciones S1–S3 y AX (pasos 2–3), luego S4 ==="
bash "$H/run_section.sh" S1 &
bash "$H/run_section.sh" S2 &
bash "$H/run_section.sh" S3 &
( bash "$H/run_chapter.sh" AX 2 && bash "$H/run_section.sh" S4 ) &
wait
estado "=== FASES 1–3 TERMINADAS (reanudación 2) ==="
