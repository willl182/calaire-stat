#!/bin/bash
# Uso: cierre_restantes_opus.sh MXX ruta_libreto ruta_script
set -u
M=$1; LIB=$2; PY=$3; R=/home/w421/w421/calaire-stat; L=curso/logs; LL=$R/curso/logs
H(){ ( cd $R && env -u ANTHROPIC_BASE_URL -u ANTHROPIC_API_KEY -u CLAUDE_CODE_AUTO_MODE_SERVER claude --model claude-haiku-5-5 --effort low -p --dangerously-skip-permissions --output-format text "$1" ); }
BASE="Curso de estadística para operadores del SRP del laboratorio designado (INM), aplicado al ozono. Lee curso/guia_libreto.md. Prácticas aplicadas (B, I, A) con datos, tareas, solución y criterio de logro; demostraciones a anexos. No toques referencias bibliográficas ni citas. No hagas commits git."
if [ "$M" = M06 ]; then
H "$BASE Eres luna (ejecutor). Ronda de correcciones $M. Lee $L/${M}_practicas_revision_haiku.md; aplica o rechaza CADA hallazgo con justificación en $L/${M}_practicas_luna.md (tabla H-xx -> decisión -> ubicación). Corrige solo las prácticas de $LIB y $PY. Ejecuta curso/.venv/bin/python -I $PY y registra resultado." > $LL/cierre_${M}_correccion.log 2>&1
fi
H "$BASE Eres revisor (Haiku). NO edites libretos ni scripts. Revisa las prácticas de $LIB (sección de prácticas) y $PY: exactitud numérica (ejecuta curso/.venv/bin/python -I $PY), coherencia enunciado-solución-script, aplicación a ozono/SRP, que las decisiones registradas en $L/${M}_practicas_luna.md estén realmente en el libreto. Escribe $L/${M}_practicas_revision_cierre_haiku.md con hallazgos H-xx (o 'sin hallazgos')." > $LL/cierre_${M}_revision.log 2>&1
H "$BASE Eres luna (ejecutor). Lee $L/${M}_practicas_revision_cierre_haiku.md; aplica o rechaza cada hallazgo con justificación, añadiendo al final de $L/${M}_practicas_luna.md una sección 'Revisión de cierre' con tabla H-xx -> decisión -> ubicación. Corrige solo prácticas de $LIB y $PY. Ejecuta curso/.venv/bin/python -I $PY y registra rc." > $LL/cierre_${M}_decisiones.log 2>&1
( cd $R/curso && .venv/bin/python -I ${PY#curso/} ) > $LL/cierre_${M}_supervisor.out 2>&1; echo "rc=$?" >> $LL/cierre_${M}_supervisor.out
