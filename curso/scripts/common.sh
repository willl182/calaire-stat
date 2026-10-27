#!/usr/bin/env bash
# Utilidades comunes de la orquestación
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
CURSO=$ROOT/curso
LOGS=$CURSO/logs
# Agentes (decisión del usuario, 2026-10-27): solo claude-sol, claude-luna y Haiku 5.5, todos con esfuerzo bajo.
# Sin respaldo Opus: si sol agota su cuota (429 usage_limit_reached) se espera y se reintenta con sol.
SOL_CMD=(claude-sol --effort low)
FLAGS=(--dangerously-skip-permissions --output-format text)

estado() { printf '%s  %s\n' "$(date '+%F %T')" "$*" >> "$LOGS/estado.log"; }

# run_agent <tipo> <log> <archivo_esperado> <prompt>
# tipo: luna | sol | haiku. Reintenta hasta dos veces (espera red y backoff) si falla o no aparece el archivo esperado.
run_agent() {
  local tipo=$1 log=$2 esperado=$3 prompt=$4 cmd intento=1 esperas=0 quien ultimo
  local respaldo=0
  while (( intento <= 3 )); do
    case $tipo in
      luna)  cmd=(claude-luna --effort low); quien="claude-luna, esfuerzo bajo" ;;
      sol)   cmd=("${SOL_CMD[@]}"); quien="claude-sol (gpt-6.1-sol), esfuerzo bajo" ;;
      haiku) cmd=(claude --model claude-haiku-5-5 --effort low); quien="Haiku 5.5, esfuerzo bajo" ;;
      *)     estado "ABORTA tipo de agente no permitido: $tipo"; return 1 ;;
    esac
    esperar_red
    estado "INICIO $tipo -> $(basename "$log") (intento $intento)${quien:+ [$quien]}"
    local t0=$(stat -c %Y "$esperado" 2>/dev/null || echo 0) n0=$( (wc -l < "$log") 2>/dev/null || echo 0)
    ( cd "$ROOT" && "${cmd[@]}" -p "${FLAGS[@]}" "${prompt//@@SUPERVISOR@@/${quien:-}}" ) >> "$log" 2>&1 < /dev/null
    local rc=$? t1=$(stat -c %Y "$esperado" 2>/dev/null || echo 0)
    if [[ $rc -eq 0 && -s $esperado && $t1 -gt $t0 ]]; then
      estado "FIN    $tipo -> $(basename "$log") OK"
      return 0
    fi
    ultimo=$(tail -n +$((n0 + 1)) "$log" 2>/dev/null)
    if grep -q "hit your session limit" <<< "$ultimo" && (( esperas < 16 )); then
      (( esperas++ ))
      estado "LÍMITE de sesión Claude ($(basename "$log")): espera 30 min (espera $esperas) — $(grep -o 'resets [^ ]*' <<< "$ultimo" | tail -1)"
      sleep 1800; continue
    fi
    if [[ $tipo == sol ]] && grep -q "usage_limit_reached" <<< "$ultimo" && (( esperas < 16 )); then
      (( esperas++ ))
      local aud; aud=$(auditar_respaldo "$esperado")
      estado "LÍMITE cuota sol ($(basename "$log")): espera 30 min (espera $esperas)"
      [[ -n $aud && $prompt != *"AVISO DEL ORQUESTADOR"* ]] && prompt="$prompt

AVISO DEL ORQUESTADOR: un intento previo de este mismo paso se cortó por cuota. Sus ediciones parciales están en ${aud#$ROOT/}/cambios.diff. Trata cada bloque como corrección candidata: conservarla, ajustarla o revertirla, con justificación, y regístrala en tu archivo de revisión."
      sleep 1800; continue
    fi
    estado "FALLO  $tipo -> $(basename "$log") rc=$rc (intento $intento)"
    sleep $((60 * intento)); (( intento++ ))
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

# auditar_respaldo <archivo_esperado>: guarda las ediciones parciales de sol antes del respaldo
auditar_respaldo() {
  local d snap a f b n
  d=$(dirname "$1"); snap=$(ls -d "$d"/versiones/*_antes_P* 2>/dev/null | tail -1)
  [[ -n $snap ]] || return 0
  a=$d/auditoria_respaldo_$(date +%Y%m%d_%H%M%S); mkdir -p "$a/estado_al_corte"
  cp -p "$d"/*_libreto.md "$1" "$a/estado_al_corte/" 2>/dev/null
  for f in "$snap"/*.md; do b=$(basename "$f"); diff -u --label "previo/$b" --label "sol_al_corte/$b" "$f" "$a/estado_al_corte/$b"; done > "$a/cambios.diff"
  n=$(grep -c '^@@' "$a/cambios.diff")
  printf '# Respaldo: claude-sol agotó su cuota a mitad de paso\n\nGenerado por run_agent el %s. Instantánea previa: `%s`. Ediciones de sol al corte: %s bloques (`cambios.diff`). Copia del estado al corte en `estado_al_corte/`. El paso continuó con Opus 5.5 de esfuerzo bajo.\n' "$(date '+%F %T')" "${snap#$ROOT/}" "$n" > "$a/LEEME.md"
  estado "AUDITORÍA respaldo -> ${a#$ROOT/} ($n bloques)"
  echo "$a"
}

capitulo() { awk -F'\t' -v id="$1" '$1==id' "$CURSO/scripts/capitulos.tsv"; }
