#!/usr/bin/env bash
# Reanuda las cadenas detenidas por el cierre suave (logs/pausa.tsv).
set -u
source "$(dirname "$0")/common.sh"
H=$CURSO/scripts
P=$LOGS/pausa.tsv
[[ -s $P ]] || { echo "No hay cadenas pausadas."; exit 0; }
mv "$P" "$LOGS/pausa_$(date +%Y%m%d_%H%M%S).tsv"
estado "=== REANUDACIÓN desde pausa ==="
while IFS=$'\t' read -r cad paso; do
  case $cad in
    AX) ( bash "$H/run_chapter.sh" AX "$paso" && bash "$H/run_section.sh" S4 ) & ;;
    *)  bash "$H/run_section.sh" "$cad" "$paso" & ;;
  esac
done < "$LOGS/$(ls -t "$LOGS" | grep '^pausa_' | head -1)"
wait
estado "=== FASES 1–3 TERMINADAS (reanudación desde pausa) ==="
