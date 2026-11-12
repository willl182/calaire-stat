#!/usr/bin/env bash
cd /home/w421/w421/calaire-stat/Curso_CORTO; L=logs_etapa2; E=$L/estado.txt; : > $E
ver(){ grep -m1 -oE "RECHAZADO|CON OBSERVACIONES|APROBADO" "$1" 2>/dev/null || echo "sin veredicto"; }
for m in M02 M03 M04 M05 M06; do
 ( echo "$(date +%T) $m luna INICIO" >> $E
   claude-luna -p --effort low --dangerously-skip-permissions "$(cat /home/w421/w421/calaire-stat/orquesta_curso_corto/e_$m.txt)" > $L/luna_$m.log 2>&1
   echo "$(date +%T) $m luna FIN (exit $?) registro: $([ -f $L/cambios_$m.md ] && echo sí || echo FALTA)" >> $E
   claude -p --model claude-haiku-5-5 --effort low --dangerously-skip-permissions "$(cat /home/w421/w421/calaire-stat/orquesta_curso_corto/v_$m.txt)" > $L/haiku_$m.log 2>&1
   echo "$(date +%T) $m haiku FIN veredicto: $(ver $L/verif_$m.md)" >> $E ) &
done
wait
echo "$(date +%T) sol INICIO" >> $E
claude-sol -p --effort low --dangerously-skip-permissions "Directorio /home/w421/w421/calaire-stat/Curso_CORTO. Verificación global de la etapa 2 (curso de 10 h en 5 sesiones de 120 min, solo niveles B e I) según 00_plan_corto.md. Lee logs_etapa2/cambios_M0*.md y verif_M0*.md. Comprueba: cobertura del PDF /home/w421/.t3/userdata/attachments/a4307bec-cdcb-489e-82fa-5e2e16ccbd98-3ba09308-7d01-4dd1-9c26-73aa937425e7-pdf.pdf (M2–M6); que no queden restos del nivel A; que la duración de cada sesión cuadre con 120 min (narración a 130 palabras/min más los tiempos de práctica); que las revisiones de tarea correspondan a la práctica I real del módulo anterior; la coherencia entre sesiones (apertura en M02, R&R en M06 I6, cierre del curso); y que los scripts de calc/ corran (/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I, en copia temporal). NO edites. Escribe una tabla por sesión y el veredicto ETAPA 2 CERRADA / NO CERRADA, con hallazgos (archivo:línea), en logs_etapa2/verif_sol_e2.md." > $L/sol.log 2>&1
echo "$(date +%T) sol FIN veredicto: $(grep -m1 -oE 'ETAPA 2 (NO )?CERRADA' $L/verif_sol_e2.md 2>/dev/null || echo 'sin veredicto')" >> $E
echo "$(date +%T) TODO TERMINADO" >> $E
