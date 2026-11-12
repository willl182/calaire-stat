#!/usr/bin/env bash
# Pasos 4–6 de una sección: revisión y entrega (sol) → revisión de la sección (opus) → correcciones (sol)
# Uso: run_section.sh <S1|S2|S3|S4> [paso_inicial 4|5|6]
set -u
source "$(dirname "$0")/common.sh"

S=$1
DESDE=${2:-4}
SEC=$(awk -F'\t' -v s="$S" '$3==s{print $2; exit}' "$CURSO/scripts/capitulos.tsv")
[[ -n $SEC ]] || { echo "Sección desconocida: $S" >&2; exit 2; }
CAPS=$(awk -F'\t' -v s="$S" '$3==s{printf "%s%s (%s)", (n++?", ":""), $1, $4}' "$CURSO/scripts/capitulos.tsv")
D=curso/$SEC
RSOL=$D/${S}_revision_sol.md
ROPUS=$D/${S}_revision_opus.md
IDX=$D/${S}_00_indice.md

P4="Eres el supervisor (@@SUPERVISOR@@) de la sección ${S} del curso de estadística aplicada a la fotometría de ozono, directorio ${D}/, capítulos: ${CAPS}. Trabajas en ${ROOT}.

Lee curso/00_plan_maestro.md, curso/guia_libreto.md, prop_e.md completo y revision_final_prop_e.md. Después lee en ${D}/ cada libreto, su bitácora y su revisión Haiku.

Tu tarea es revisar el contenido final de cada capítulo y entregar la sección:
1. Si ${RSOL} no existe, créalo; si existe, consérvalo. Antes de revisar, añade o actualiza «## Nota del supervisor» con quién eres (@@SUPERVISOR@@), fecha y hora, y deja «## Plan de revisión» completo (criterios, orden, cómo verificarás cálculos y referencias).
2. Revisa cada capítulo: fidelidad a prop_e por nivel (nada de más ni de menos; exclusiones de §6); corrección estadística y metrológica (recalcula con curso/.venv/bin/python los ejemplos y soluciones clave y verifica los scripts de ${D}/calc/); referencias (verifica numerales en docs/ con pdftotext; ninguna inventada; Una cita a prop_e solo justifica el alcance; no sustituye la referencia técnica de un concepto, definición o fórmula, que debe ser externa (VIM, GUM, ISO, textos de docs/).); formato libreto narrado según la guía; coherencia entre los capítulos de la sección (notación, prerrequisitos, transiciones, remisiones a anexos AX, sin duplicaciones ni contradicciones); errores críticos y señales de escalamiento. FASE ACTUAL: SOLO CONTENIDO; las prácticas aparecen solo como marcadores «[PRÁCTICA — fase de ejercicios]» (uno por cada práctica de prop_e); no se desarrollan ejercicios, soluciones ni rúbricas.
3. Registra en ${RSOL}, «## Hallazgos por capítulo», cada hallazgo (id S-…, capítulo, ubicación, severidad, problema, corrección).
4. Aplica tú mismo las correcciones en los libretos y registra en ${RSOL}, «## Correcciones aplicadas», cada una (hallazgo → cambio → ubicación). Si tocas cálculos, actualiza los scripts.
5. Crea ${IDX}: índice de la sección entregada (capítulos, escenas por nivel, marcadores de práctica pendientes, anexos a los que remiten, datos usados con su rótulo, estado y pendientes).
6. Cierra ${RSOL} con «## Estado de entrega».

No modifiques archivos fuera de ${D}/. Al terminar responde solo con un resumen de 5 líneas."

P5="Eres el revisor de sección (Haiku 5.5; el archivo conserva el nombre _revision_opus por compatibilidad) de la sección ${S} entregada por el supervisor, directorio ${D}/, capítulos: ${CAPS}. Trabajas en ${ROOT}.

Lee curso/00_plan_maestro.md, curso/guia_libreto.md, prop_e.md, el índice ${IDX}, la revisión del supervisor ${RSOL} y todos los libretos de la sección. Consulta las bitácoras y los scripts de ${D}/calc/ cuando lo necesites.

Evalúa la sección como unidad y cada capítulo: fidelidad a prop_e por nivel y exclusiones; corrección técnica estadística y metrológica (recalcula con curso/.venv/bin/python una muestra significativa de ejemplos y soluciones); referencias (verifica con pdftotext en docs/ al menos 10 numerales repartidos entre capítulos; señala cualquier referencia inventada o mal atribuida; Una cita a prop_e solo justifica el alcance; no sustituye la referencia técnica de un concepto, definición o fórmula, que debe ser externa (VIM, GUM, ISO, textos de docs/).); calidad del libreto como guion oral (claridad, ritmo, acotaciones, que un instructor pueda impartirlo sin rehacerlo); coherencia interna de la sección y con el resto del curso (notación, prerrequisitos, remisiones a AX); que todo el contenido de prop_e esté explicado y que nada quede como lectura, mención u opcional. FASE ACTUAL: SOLO CONTENIDO; las prácticas aparecen solo como marcadores «[PRÁCTICA — fase de ejercicios]» y su falta de desarrollo no es hallazgo, pero sí un marcador ausente.

Revisa también las carpetas de auditoría de la sección (${D}/auditoria_*/): son ediciones que supervisores interrumpidos dejaron sin registrar. Cada edición debe estar decidida y registrada en ${RSOL}; si alguna no lo está, o si su contenido es incorrecto, es un hallazgo.

NO edites los libretos. Nota: el supervisor de esta sección pudo ser claude-sol (o, en pasos anteriores, Opus 5.5 de esfuerzo bajo) (ver su «Nota del supervisor»); revisa su trabajo con el mismo rigor e independencia. Escribe ${ROPUS} con «## Plan de revisión», «## Hallazgos» (tabla: id O-…, capítulo, ubicación con texto citado, severidad crítica/mayor/menor, problema, evidencia, corrección propuesta concreta), «## Verificaciones» (cálculos y referencias comprobadas y resultado), «## Veredicto» (aprobada / aprobada con correcciones / no aprobada, por capítulo y global). Al terminar responde solo con el veredicto y el número de hallazgos por severidad."

P6="Eres el supervisor (@@SUPERVISOR@@) de la sección ${S}, directorio ${D}/. Trabajas en ${ROOT}. Lee curso/guia_libreto.md, tu revisión ${RSOL}, la revisión de Opus ${ROPUS} y los libretos.

Aplica en los libretos las correcciones de ${ROPUS}. Si hay carpetas ${D}/auditoria_respaldo_*/ creadas después de ${ROPUS}, contienen ediciones parciales de un intento tuyo anterior de este mismo paso, que se interrumpió: trata cada bloque como corrección candidata (conservarla, ajustarla o revertirla) y regístrala en la tabla con el id O-… que atiende o como corrección adicional. Las de severidad crítica y mayor son obligatorias salvo que demuestres, con cálculo o referencia verificada, que el hallazgo es incorrecto. Si tocas cálculos, actualiza los scripts de ${D}/calc/.
Añade a ${RSOL} la sección «## Correcciones tras la revisión Opus» con una tabla: id O-…, decisión (aplicado / aplicado con cambios / rechazado), cambio, ubicación, justificación. Actualiza ${IDX} y «## Estado de entrega».

No modifiques archivos fuera de ${D}/. Al terminar responde solo con un resumen de 3 líneas."

AUDS=$(cd "$ROOT" && ls -d $D/auditoria_interrupcion_sol*/LEEME.md $D/auditoria_respaldo_*/LEEME.md 2>/dev/null | tr '\n' ' ')
if [[ -n $AUDS ]]; then
  P4="$P4

REANUDACIÓN: revisiones tuyas anteriores de esta sección se interrumpieron después de editar libretos y antes de registrar hallazgos. Cada carpeta de auditoría (${AUDS}) documenta esas ediciones con las versiones previas y un diff (en auditoria_interrupcion_sol/ están identificadas como C01–C27; en las siguientes, como bloques del diff). Conserva el «Plan de revisión» de ${RSOL} y cualquier «Nota del orquestador». Trata cada edición como una corrección candidata: conservarla, ajustarla o revertirla (desde la versión previa) con justificación técnica. Regístrala en «## Hallazgos por capítulo» y «## Correcciones aplicadas» con su hallazgo S-… y la referencia a la edición (Cxx o archivo y bloque del diff); ninguna puede quedar sin decisión. Revisa también los scripts y archivos auxiliares que esas ejecuciones dejaron en ${D}/calc/. Después continúa la revisión completa."
fi

LOG=$LOGS/${S}
if (( DESDE <= 4 )); then
  instantanea "$D" "antes_P4_sol" "$ROOT"/$D/M*_libreto.md "$ROOT"/$D/AX_libreto.md
  run_agent sol  "${LOG}_4_revision_sol.log"     "$ROOT/$RSOL"  "$P4" || { estado "ABORTA $S en revisión sol"; exit 1; }
fi
if (( DESDE <= 5 )); then
  run_agent haiku "${LOG}_5_revision_opus.log"    "$ROOT/$ROPUS" "$P5" || { estado "ABORTA $S en revisión Opus"; exit 1; }
fi
instantanea "$D" "antes_P6_sol" "$ROOT"/$D/M*_libreto.md "$ROOT"/$D/AX_libreto.md
run_agent sol  "${LOG}_6_correcciones_sol.log" "$ROOT/$RSOL"  "$P6" || { estado "ABORTA $S en correcciones sol"; exit 1; }
estado "SECCION $S COMPLETA"
