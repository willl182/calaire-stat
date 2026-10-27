# Evidencia de cálculo y revisión de S2

Fase: solo contenido. Los ejemplos resueltos sirven a la explicación narrada; este directorio no constituye un paquete de prácticas, soluciones de ejercicios ni rúbricas.

## Entradas ejecutables

Los cinco scripts docentes son `M05_diseno.py`, `M06_ejemplos.py`, `M06_RR_CALAIRE.py`, `M07_ejemplos.py` y `M08_ejemplos.py`. Se ejecutan desde la raíz del repositorio con `curso/.venv/bin/python`. Los dos primeros capítulos y los dos últimos tienen informes finales separados, integrados después en `../S2_revision_sol.md`. La ejecución técnica y sus reservas se describen allí; una salida sin error no valida por sí sola un modelo.

`m07m08_verificacion_independiente.py` contrasta ejemplos de M07–M08 por otra vía de cálculo. No sustituye el contraste de GGMR con los datos publicados en ISO/TS 28037 ni acredita autorización de uso operativo.

`auditoria_entrega_sol.py` comprueba estructura, doce marcadores de práctica, huellas de extractos heredados y conteos históricos. `trazabilidad_bloques_sol.py` genera `inventario_bloques_sol.json`: 94 bloques con carpeta, capítulo, cabecera y SHA-256. Las decisiones técnicas de conservar, ajustar o revertir pertenecen al informe del supervisor, no al inventario automático. `continuidad_auditorias_sol.py` reconstruye los estados en memoria a partir de cada diff y confirma su igualdad con las instantáneas; `continuidad_auditorias_sol.txt` guarda el resultado. No exige que distintos algoritmos de diff elijan los mismos contextos ni escribe sobre respaldos.

## Auxiliar que no debe ejecutarse para editar

`ajustes_sol.py` es un registro histórico de sustituciones editoriales interrumpidas. Está deshabilitado con `SystemExit` antes de importar o escribir archivos. Su cuerpo conserva propuestas que pueden haber sido ajustadas o descartadas. No es una receta para restablecer la versión final. La prueba `auxiliar_historico_verificacion_sol.txt` documenta salida 1 esperada y ausencia de cambios en las huellas de los libretos.

## Fuentes y salidas heredadas

`fuentes_sol/00.txt` a `21.txt` son extractos antiguos: `inventario_fuentes_heredadas_sol.json` conserva sus 22 huellas. Un nombre numérico no demuestra procedencia. Las extracciones adicionales y los informes documentales deben proporcionar el mapa al PDF y numeral; no se atribuye una cita solo por encontrar palabras en un extracto sin identificar.

Los grupos `M05_M06_*.txt`, `m07m08_*.txt`, `*_sol.out`, `*_revision_sol.out` y los informes previos conservan evidencia de los intentos interrumpidos. Una cifra histórica puede corresponder a texto anterior. Para el estado entregado prevalecen los scripts vigentes, las salidas finales fechadas y las decisiones incorporadas a `S2_revision_sol.md`; no se eliminan ni corrigen retrospectivamente los respaldos para aparentar uniformidad.

Los archivos `m07m08_*antes_P4_sol_*.diff` y `m07m08_git_*.diff` son evidencia comparativa, no programas ni fuentes técnicas externas. Las cuatro auditorías principales están fuera de `calc/`, dentro de la misma sección. Las copias de `versiones/` y `estado_al_corte/` permanecen históricas.

`estado_git_inicio_revision_sol.txt` registra el estado preexistente del repositorio, incluidos cambios ajenos a S2; no atribuye esos cambios a esta revisión. Ningún archivo fuera de S2 se entrega como modificación de este trabajo.

## Límites

Los resultados R&R del libro propio siguen condicionados a la confirmación de signos, fechas, correspondencia de bloques y criterio de selección. Los ejemplos simulados no se atribuyen al laboratorio. La entrega de contenido no autoriza impartición, firma, aprobación de CMC ni uso de herramientas en producción.
