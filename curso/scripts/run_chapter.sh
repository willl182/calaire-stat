#!/usr/bin/env bash
# Pasos 1–3 de un capítulo: desarrollo (luna) → revisión de redacción y errores (haiku) → ajustes (luna)
# Uso: run_chapter.sh <ID> [paso_inicial]   (ID de scripts/capitulos.tsv)
set -u
source "$(dirname "$0")/common.sh"

IFS=$'\t' read -r ID SEC S TITULO ALCANCE <<< "$(capitulo "$1")"
[[ -n ${ID:-} ]] || { echo "Capítulo desconocido: $1" >&2; exit 2; }
D=curso/$SEC
LIB=$D/${ID}_libreto.md
BIT=$D/${ID}_bitacora_luna.md
REV=$D/${ID}_revision_haiku.md
mkdir -p "$ROOT/$D/calc"

EXTRA=""
case $ID in
  T_DIFERIDO)  EXTRA="Este capítulo es el taller integrador. Antes de planificar, lee los libretos ya desarrollados de M00–M13 (curso/S*/M*_libreto.md) para usar la misma notación, los mismos datos y remitir a sus escenas y prácticas. Diseña el taller por nivel (B, I y A) con las cuatro familias de casos de prop_e §7 y el producto final (informe con datos tratados, método, resultado, incertidumbre, interpretación estadística y acción). Narra la conducción del taller, las soluciones de referencia y la rúbrica de §8. Indica con honestidad qué paquetes de datos faltan según prop_e §9 y usa conjuntos simulados rotulados donde haga falta." ;;
  AX) EXTRA="Este capítulo reúne los anexos de deducciones AX.1–AX.13 de guia_libreto.md §7. Antes de planificar, busca en los libretos ya desarrollados (grep -n 'AX\\.' curso/S*/M*_libreto.md) desde dónde se remite a cada anexo y con qué notación, para que las deducciones coincidan exactamente con lo que usan los capítulos. Cada anexo se narra como una explicación pausada para quien quiera seguir la deducción, con los pasos completos en [PIZARRA], su referencia verificada y un cierre que recuerde dónde se usa el resultado. Los anexos no se evalúan (prop_e §9) y no llevan prácticas ni marcadores; sustituye las secciones por nivel por una sección por anexo e indica en cada uno el nivel desde el que se usa el resultado." ;;
  M13) EXTRA="Este módulo es solo de nivel A: la ficha lo dice y no hay secciones B ni I." ;;
esac

P1="Eres el agente desarrollador (claude-luna) del capítulo ${ID} «${TITULO}» del curso de estadística aplicada a la fotometría de ozono (operadores del SRP de CALAIRE). Trabajas en el repositorio ${ROOT}.

Lee primero, completos: curso/00_plan_maestro.md y curso/guia_libreto.md (obligatoria: formato libreto narrado, estructura, convenciones, referencias, datos, anexos). Después lee prop_e.md (§1–§4, ${ALCANCE}, §6–§8) y revision_final_prop_e.md. Usa temario_curso.md solo como mapa inicial de referencias del módulo, y los datos de guia_libreto.md §6 que necesite el capítulo.
${EXTRA}

Tarea:
1. ANTES de escribir el libreto, crea ${BIT} con la sección «## Plan»: alcance por nivel tomado literalmente de prop_e, escenas previstas, datos y su rótulo de origen, cálculos previstos, referencias a verificar y anexos a los que remitirás.
2. Escribe ${LIB} completo según la guía: todo narrado (voz del instructor) con acotaciones, niveles B, I y A con todo el contenido que prop_e asigna a cada uno —ni más ni menos—, ejemplos ilustrativos con números, errores críticos como advertencias narradas, señales de escalamiento y referencias del capítulo. FASE ACTUAL: SOLO CONTENIDO. No desarrolles prácticas, ejercicios, soluciones, evidencias evaluables ni rúbricas: en el lugar de cada práctica de prop_e deja solo el marcador «> **[PRÁCTICA — fase de ejercicios]** <título breve>» (guía §1). Escríbelo por partes (una escena o un nivel por vez, añadiendo al archivo) para no truncar. Extensión: la necesaria para impartir todo el contenido; como orientación, 6 000–10 000 palabras.
3. Calcula cada número con curso/.venv/bin/python y guarda los scripts en ${D}/calc/${ID}_*.py. Ningún número sin script que lo reproduzca.
4. Verifica cada numeral citado en docs/ con pdftotext. Si no puedes verificarlo, cita sin numeral y anótalo como pendiente. No inventes referencias.
5. Completa en ${BIT} la sección «## Ejecución»: qué escribiste (escenas y prácticas), scripts y resultados, referencias verificadas (clave, numeral, archivo y página donde lo comprobaste), decisiones tomadas y pendientes.

No modifiques archivos fuera de ${D}/. Al terminar responde solo con un resumen de 5 líneas."

P2="Eres el revisor de redacción y errores (Haiku) del capítulo ${ID} «${TITULO}». Trabajas en ${ROOT}. Lee curso/guia_libreto.md, la parte de prop_e.md que corresponde (${ALCANCE}, y §6–§8) y el libreto ${LIB}. Puedes consultar ${BIT} y los scripts de ${D}/calc/.

Revisa:
a) Redacción: ortografía, gramática, puntuación, claridad para ser dicho en voz alta, frases largas, terminología consistente, convenciones de la guía (§4: notación, coma decimal, unidades).
b) Errores: fórmulas, signos, unidades, notación, números de los ejemplos y soluciones (recalcula con curso/.venv/bin/python), contradicciones internas.
c) Formato libreto: que todo esté narrado, acotaciones con las etiquetas permitidas, sin viñetas en el contenido narrado, estructura de la guía §2.
d) Referencias: que cada concepto, fórmula y criterio tenga referencia con el formato de la guía §5; comprueba con pdftotext una muestra de al menos 5 numerales en docs/.
e) Alcance: que cada nivel tenga todo el contenido que prop_e asigna (ni más ni menos) y que se respeten las exclusiones de prop_e §6. En esta fase el libreto es SOLO CONTENIDO: las prácticas aparecen solo como marcadores «[PRÁCTICA — fase de ejercicios]»; no señales su falta de desarrollo, pero sí un marcador ausente o una práctica desarrollada.

NO edites el libreto. Escribe ${REV} con: «## Plan de revisión» (qué revisaste y cómo), «## Hallazgos» (tabla: id R01…, ubicación con escena y texto citado, tipo, severidad crítica/mayor/menor, problema, corrección propuesta concreta), «## Verificaciones hechas» (cálculos y referencias comprobadas, con resultado) y «## Resumen». Al terminar responde solo con el número de hallazgos por severidad."

P3="Eres el agente desarrollador (claude-luna) del capítulo ${ID} «${TITULO}». Trabajas en ${ROOT}. Lee curso/guia_libreto.md, tu bitácora ${BIT}, el libreto ${LIB} y la revisión ${REV}.

Tarea: aplica en ${LIB} cada hallazgo de la revisión que proceda. Si rechazas uno, justifícalo técnicamente con referencia. Si un hallazgo afecta un número, actualiza el script de ${D}/calc/ y recalcula. Corrige también los errores del mismo tipo que encuentres aunque no estén listados.
Después añade a ${BIT} la sección «## Correcciones (revisión Haiku)» con una tabla: id del hallazgo, decisión (aplicado / aplicado con cambios / rechazado), cambio hecho, ubicación, justificación; y una lista de correcciones adicionales por iniciativa propia.

No modifiques archivos fuera de ${D}/. Al terminar responde solo con un resumen de 3 líneas."

LOG=$LOGS/${ID}
DESDE=${2:-1}   # paso desde el que se reanuda (1 desarrollo, 2 Haiku, 3 ajustes)
(( DESDE <= 1 )) && { run_agent luna  "${LOG}_1_desarrollo_luna.log" "$ROOT/$LIB" "$P1" || { estado "ABORTA $ID en desarrollo"; exit 1; }; }
(( DESDE <= 2 )) && { run_agent haiku "${LOG}_2_revision_haiku.log"  "$ROOT/$REV" "$P2" || { estado "ABORTA $ID en revisión Haiku"; exit 1; }; }
(( DESDE <= 3 )) && instantanea "$D" "antes_P3_${ID}" "$ROOT/$LIB"
(( DESDE <= 3 )) && { run_agent luna  "${LOG}_3_ajustes_luna.log"    "$ROOT/$BIT" "$P3" || { estado "ABORTA $ID en ajustes"; exit 1; }; }
estado "CAPITULO $ID COMPLETO"
