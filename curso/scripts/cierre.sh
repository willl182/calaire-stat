#!/usr/bin/env bash
# Cierre suave por etapas.
#   cierre.sh           solicita el cierre: cada cadena acaba su paso actual y no arranca el siguiente
#   cierre.sh estado    muestra qué agentes siguen trabajando
#   cierre.sh cancelar  retira la solicitud (la orquestación sigue normal)
set -u
source "$(dirname "$0")/common.sh"
FLAG=$LOGS/CIERRE_SOLICITADO
mostrar() {
  echo "Agentes en curso (INICIO sin FIN posterior):"
  awk '
    /=== REANUDACIÓN/ {delete act}
    /INICIO/ {split($0,a,"-> "); split(a[2],b," "); act[b[1]]=$0}
    /FIN|FALLO|PAUSA/ {for (k in act) if (index($0,k)) delete act[k]}
    END {for (k in act) print "  " act[k]}' "$LOGS/estado.log"
  [[ -f $FLAG ]] && echo "Cierre SOLICITADO." || echo "Sin solicitud de cierre."
  [[ -f $LOGS/pausa.tsv ]] && { echo "Pausadas (cadena, paso siguiente):"; sed 's/^/  /' "$LOGS/pausa.tsv"; }; true
}
case ${1:-solicitar} in
  solicitar) touch "$FLAG"; estado "CIERRE SOLICITADO: cada cadena termina su paso actual"; mostrar ;;
  estado)    mostrar ;;
  cancelar)  rm -f "$FLAG"; estado "CIERRE CANCELADO"; mostrar ;;
esac
