# Verificación independiente del supervisor — 2026-10-27

## Bloqueo de revisión Haiku

Los comandos exigidos para Haiku 5.5 terminaron con rc=1 y `API Error: 400 unknown provider for model claude-haiku-5-5`. Evidencia: `AB_revision_haiku.log` y `M00_practicas_revision.log`. No hubo una revisión Haiku ni hallazgos H-xx; no se inventan ni se sustituyen por otro modelo. El pipeline se detuvo antes de M01. No se cambia proveedor/autenticación ni se envía contenido a otro servicio.

## S-01 — mayor — grafía QAPP

La afirmación de luna de haber confirmado visualmente que NO es ± es falsa. El supervisor renderizó docs/srp_qapp.pdf, página PDF 23 (Element 7, página impresa 3/4), y amplió a 400 dpi la celda de verificación Level 1. La página muestra un signo más CON una raya debajo, tanto en `1.00 ± 0.01` como en `intercept <± 1 ppb`. La extracción pierde la raya: no es una transcripción visual fiel `<+`. Reproducción de la ampliación: `pdftoppm -f 23 -l 23 -r 400 -x 1550 -y 960 -W 900 -H 230 -png -singlefile docs/srp_qapp.pdf /tmp/calaire_qapp_supervisor_signo`. El revisor puede abrir /tmp/calaire_qapp_supervisor_signo.png. Corregir informe A y párrafo M10 para distinguir extracción `<+` de grafía visible `<±`. No convertir automáticamente `<±` en |intercepto|<1 ni inventar desigualdad autorizada. Mantener escalamiento operativo ante ambigüedad semántica. No cambiar bibliografía/citas.

## S-02 — mayor — M00-B emparejamiento contradictorio

M00:92 dice que hay cuatro indicaciones P01/P02/P04/P03; la tabla solo tiene tres valores y un faltante. La solución dice que P04 no tiene indicación concordante, pero la tabla contiene una indicación con ID P04=50,8. Emparejar por clave daría precisamente P04 con referencia 100,0; no se puede declarar huérfana sin evidencia adicional. El enunciado debe aportar metadatos suficientes que demuestren cuál clave está mal, o plantear una indicación verdaderamente no asignable (p.ej. P99) con registro autorizado explícito para resolverla. Respetar prop_e M00-B: detectar una pareja desplazada y un faltante, documentar corrección sin borrar original. Fijar tablas, reglas de generación, conteos, solución y script para que coincidan, sin adivinar por magnitud ni orden. El resultado debe preservar un faltante genuino y tener emparejamiento inequívoco o incertidumbre explícitamente justificada.

## S-03 — menor — reproducibilidad del diagnóstico histórico

B tiene lista de fuentes y datos faltantes correcta y script exploratorio existente ejecutable. Conviene guardar un script diagnóstico propio, solo lectura, para reproducir inventario de hojas, ubicación de VALORES ABSOLUTOS, dimensión de bloques, rango y ausencia de signo; no promover el ANOVA de magnitudes a validación de errores firmados. El supervisor ejecutó M06_RR_CALAIRE.py con rc=0 y confirmó Fmáx 1,238163 y Bonferroni [135,405]. La validación histórica permanece bloqueada por datos de signo/diseño faltantes.

## Decisión de alcance

Aplicar S-01/S-02 mediante luna y registrar S-03. Detener nuevos capítulos hasta restablecer la revisión Haiku obligatoria. M00 puede conservarse como borrador corregido NO aprobado. M01–M13 no se declaran desarrollados. Documentar este bloqueo, no simular cierre ni revisión.
