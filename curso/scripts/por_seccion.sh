#!/usr/bin/env bash
# Orquestación por dependencias: cada sección arranca cuando sus capítulos están COMPLETOS.
# AX arranca de inmediato (las remisiones ya existen en los libretos); S4 espera M13 y AX.
set -u
source "$(dirname "$0")/common.sh"
H=$CURSO/scripts

# esperar_caps <ID>... : espera "CAPITULO <ID> COMPLETO" en estado.log; falla si aparece ABORTA de alguno
esperar_caps() {
  local id
  for id in "$@"; do
    until grep -q "CAPITULO $id COMPLETO" "$LOGS/estado.log"; do
      sed -n '/REANUDACIÓN/,$p' "$LOGS/estado.log" | grep -q "ABORTA $id " && return 1
      sleep 30
    done
  done
}

seccion() {  # seccion <S> <ID>...
  local S=$1; shift
  esperar_caps "$@" || { estado "ABORTA $S: capítulo previo abortado"; return 1; }
  estado "=== $S: capítulos listos, inicia revisión de sección ==="
  bash "$H/run_section.sh" "$S"
}

estado "=== ORQUESTACIÓN POR SECCIÓN ==="
seccion S1 M00 M01 M02 M03 M04 &
seccion S2 M05 M06 M07 M08 &
seccion S3 M09 M10 M11 M12 &
( bash "$H/run_chapter.sh" AX; seccion S4 M13 AX ) &
wait
estado "=== FASES 1–3 TERMINADAS (por sección) ==="
