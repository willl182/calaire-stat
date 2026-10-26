#!/usr/bin/env bash
# Utilidades comunes de la orquestación
ROOT=/home/w421/w421/calaire-stat
CURSO=$ROOT/curso
LOGS=$CURSO/logs
FLAGS=(--dangerously-skip-permissions --output-format text)

estado() { printf '%s  %s\n' "$(date '+%F %T')" "$*" >> "$LOGS/estado.log"; }

# run_agent <tipo> <log> <archivo_esperado> <prompt>
# tipo: luna | sol | haiku | opus. Reintenta hasta dos veces (espera red y backoff) si falla o no aparece el archivo esperado.
run_agent() {
  local tipo=$1 log=$2 esperado=$3 prompt=$4 cmd intento
  case $tipo in
    luna)  cmd=(claude-luna) ;;
    sol)   cmd=(claude-sol) ;;
    haiku) cmd=(claude --model claude-haiku-5-5) ;;
    opus)  cmd=(claude --model claude-opus-5-5) ;;
  esac
  for intento in 1 2 3; do
    esperar_red
    estado "INICIO $tipo -> $(basename "$log") (intento $intento)"
    local t0=$(stat -c %Y "$esperado" 2>/dev/null || echo 0)
    ( cd "$ROOT" && "${cmd[@]}" -p "${FLAGS[@]}" "$prompt" ) >> "$log" 2>&1
    local rc=$? t1=$(stat -c %Y "$esperado" 2>/dev/null || echo 0)
    if [[ $rc -eq 0 && -s $esperado && $t1 -gt $t0 ]]; then
      estado "FIN    $tipo -> $(basename "$log") OK"
      return 0
    fi
    estado "FALLO  $tipo -> $(basename "$log") rc=$rc (intento $intento)"
    sleep $((60 * intento))
  done
  return 1
}

# Espera a que haya resolución DNS de los proveedores (máx. 30 min)
esperar_red() {
  local n=0
  until getent hosts chatgpt.com >/dev/null && getent hosts api.anthropic.com >/dev/null; do
    (( n++ == 0 )) && estado "SIN RED: esperando…"
    (( n > 180 )) && return 0
    sleep 10
  done
}

# instantanea <dir_relativo_a_ROOT> <etiqueta> <archivo>... : copia previa a un paso que edita (auditoría)
instantanea() {
  local d=$ROOT/$1 et=$2; shift 2
  local dest=$d/versiones/$(date +%Y%m%d_%H%M%S)_$et
  mkdir -p "$dest" && cp -p "$@" "$dest/" 2>/dev/null
  estado "INSTANTÁNEA $et -> ${dest#$ROOT/}"
}

capitulo() { awk -F'\t' -v id="$1" '$1==id' "$CURSO/scripts/capitulos.tsv"; }
