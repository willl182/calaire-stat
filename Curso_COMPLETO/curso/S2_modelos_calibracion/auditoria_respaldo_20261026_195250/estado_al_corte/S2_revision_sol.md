# S2. Revisión del supervisor

## Nota del supervisor

Responsable: claude-sol (gpt-6.1-sol). Reanudación: 2026-10-26, 05:26 -05:00. Fase: solo contenido. Se conserva el plan anterior; las ediciones interrumpidas se evalúan como candidatas, no como correcciones ya aprobadas.

## Plan de revisión

Fecha: 25 de octubre de 2026. Fase: solo contenido.

1. Leer íntegramente plan maestro, guía, prop_e y revisión final; después, libretos, bitácoras y revisiones Haiku de M05–M08, en ese orden.
2. Contrastar cada escena con los contenidos B/I/A acumulativos de prop_e §5 y las exclusiones de §6. Comprobar tres marcadores de práctica por capítulo, sin enunciados, soluciones ni rúbricas.
3. Revisar definición del resultado, independencia, unidades, signo, componentes de varianza, ajuste inverso, covarianza, cobertura y límites de uso. Separar ejemplos docentes de prácticas pendientes.
4. Leer y ejecutar los cinco scripts con curso/.venv/bin/python; recalcular independientemente ejemplos clave y contrastar resultados con la narración. Actualizar código cuando cambie un cálculo.
5. Extraer con pdftotext las fuentes de docs/ dentro de esta sección y comprobar los numerales citados. prop_e acredita únicamente alcance; las afirmaciones técnicas requieren fuentes externas. Registrar cualquier verificación no resuelta.
6. Comprobar formato oral, notación común, prerrequisitos, transiciones, remisiones AX, datos rotulados, errores críticos y señales de escalamiento. Corregir directamente los libretos y registrar hallazgo, cambio y ubicación.
7. Entregar índice de escenas y pendientes, y estado de contenido distinto de autorización para impartir. No modificar archivos fuera de S2.

## Hallazgos por capítulo

### Hallazgos transversales

- **S-T01 · sección/auditoría · mayor.** Las interrupciones dejaron cambios sin decisión ni trazabilidad de entrega. Se evalúan individualmente los 3 bloques de `auditoria_interrupcion_sol_2/cambios_sol.diff` y los 32 de `auditoria_interrupcion_sol_3/cambios.diff`; las decisiones por capítulo se incorporan abajo. No existe `auditoria_interrupcion_sol/` en S2 ni evidencia C01–C27: el LEEME de sol_2 confirma que S2 no tuvo aquella interrupción anterior. No se importan identificadores de otras secciones. Respaldos preservados.
- **S-T02 · calc/ajustes_sol.py · mayor.** Auxiliar editorial histórico con escrituras directas no idempotentes: reejecutarlo podía restablecer texto obsoleto y duplicar referencias. Se deshabilita su ejecución antes de cualquier escritura y se conserva el cuerpo como evidencia; no es script de cálculo.
- **S-T03 · calc/fuentes_sol/00.txt–21.txt · menor.** Extractos heredados identificados solo por números, sin mapa documental fiable. Se conservan con SHA-256 en `calc/inventario_fuentes_heredadas_sol.json`; no se usan por sí solos para certificar una cita. Verificación nueva mediante extracciones con nombres de fuente identificables.
- **S-T04 · remisiones AX de M05/M06 · mayor.** AX.4 existente desarrolla únicamente un factor aleatorio; AX.11 trata indicadores de M12. No respaldan promesas de deducciones multifactor ni incertidumbre de componentes ANOVA. Corregir remisiones en S2 sin alterar anexos externos.

Revisión por capítulo y decisiones individuales en curso.

## Correcciones aplicadas

- **S-T02:** auxiliar de reescritura deshabilitado mediante `SystemExit` antes de sus escrituras; código histórico preservado en `calc/ajustes_sol.py`. Comprobado con `curso/.venv/bin/python -I`: salida 1 intencional y mensaje de bloqueo; las huellas SHA-256 de los cuatro libretos permanecieron iguales durante la prueba. No es un fallo numérico pendiente.
- **S-T03:** inventario con huellas de los 22 extractos heredados creado en `calc/inventario_fuentes_heredadas_sol.json`; fuentes numeradas conservadas sin atribuciones nuevas.
