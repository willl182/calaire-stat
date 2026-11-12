#!/usr/bin/env bash
# Guardián del cierre suave. Corre siempre en segundo plano.
# Si existe logs/CIERRE_SOLICITADO, cada cadena (S1, S2, S3, AX→S4) termina el paso en curso
# y, en cuanto intenta arrancar el siguiente agente (línea INICIO), el guardián lo detiene
# antes de que trabaje (segundos tras arrancar) y anota el punto de reanudación en logs/pausa.tsv.
set -u
source "$(dirname "$0")/common.sh"
FLAG=$LOGS/CIERRE_SOLICITADO
PAUSA=$LOGS/pausa.tsv

arbol() {  # arbol <pid>: pid y todos sus descendientes
  local p=$1 h; echo "$p"
  for h in $(ps -o pid= --ppid "$p"); do arbol "$h"; done
}

detener() {  # detener <cadena> <paso>
  local cad=$1 paso=$2 patron raiz pids
  case $cad in
    S1|S2|S3|S4) patron="^bash \S*scripts/run_section\.sh $cad( |$)" ;;
    AX)          patron="^bash \S*scripts/run_chapter\.sh AX( |$)" ;;
  esac
  raiz=$(pgrep -f "$patron" | head -1)
  [[ -n $raiz ]] || return 0
  pids=$(arbol "$raiz")
  kill -TERM $pids 2>/dev/null
  sleep 2; kill -KILL $pids 2>/dev/null
  printf '%s\t%s\n' "$cad" "$paso" >> "$PAUSA"
  estado "PAUSA $cad: detenida antes del paso $paso (sin trabajo hecho en ese paso)"
}

quedan() { pgrep -f "^bash \S*scripts/run_(section|chapter)\.sh " >/dev/null; }

estado "GUARDIÁN de cierre activo (pid $$)"
tail -n0 -F "$LOGS/estado.log" | while IFS= read -r linea; do
  if [[ -f $FLAG && $linea =~ INICIO\ [a-z]+\ -\>\ ([A-Z0-9]+)_([0-9])_ ]]; then
    detener "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}"
  fi
  if [[ -f $FLAG ]] && ! quedan; then
    rm -f "$FLAG"
    estado "CIERRE COMPLETO: ningún agente activo; seguro desconectar. Reanudar: bash curso/scripts/reanudar_pausa.sh"
  fi
done
