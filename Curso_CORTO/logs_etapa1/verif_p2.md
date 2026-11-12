# Verificación punto 2 — etapa 1

**Veredicto: APROBADO CON OBSERVACIONES** (sin defectos bloqueantes; hallazgos menores de redacción y de registro).

Alcance: punto 2 del plan (`00_plan_corto.md`): retirar referencias a módulos fuera del curso (M7, M8, M10, M11, M12, AX.x) o convertirlas en «fuera del alcance de este curso». Revisé M02–M06 en `Curso_CORTO/`, comparando con el original en `Curso_COMPLETO/curso/`. Ignoré los cambios de los puntos 1 y 3 (p. ej. Escena B6 en M02, prerrequisitos de M02/M03, bloque de atípicos de M04).

## Cumplimiento de la tarea

- **Cumplida.** `grep` sobre M02–M06 no encuentra `AX`, `M7`–`M13` (como referencia a módulo) ni `S1`–`S4`. La única coincidencia restante es `GUM-S2` (M03, bibliografía), que es correcto conservar.
- Las referencias eliminadas se reemplazaron por «fuera del alcance de este curso» o se quitaron del texto, y las remisiones internas válidas (M2, M3, M4, M5, M6) se conservaron.
- Ejemplos de sustitución correcta: `M02_libreto.md:86` (control de M11), `M02_libreto.md:128` (residuos en M7), `M02_libreto.md:160` (ajuste en M07), `M02_libreto.md:206` (M12-B), `M03_libreto.md:282` (M9-A), `M04_libreto.md:42` (modelo de M8), `M05_libreto.md:112` (M1, M7, M8, M10, M12), `M06_libreto.md:46` (presupuesto de M8).
- Entradas de tabla `Anexos`: M02:13, M03:13, M04:13, M05:13 y M06:13 ya no citan AX.
- Bibliografía: se eliminaron las entradas `AX.x` en M02:228, M03:375–376, M04:292–293 y M06:298. No queda ninguna entrada huérfana.

## Coherencia con el texto vecino

- Las frases nuevas encajan con el contenido de cada escena. Ejemplo: M05:112 deriva los temas no resueltos a «evaluación técnica específica, fuera del alcance», y sigue apuntando a M2 para el dato atípico, coherente con el punto 3.
- M03:166, M03:184 y M03:280 usan la misma fórmula («la derivación queda fuera del alcance…»). Es coherente y no contradice M03:326 (GGMR fuera de curso).

## Números

- Comparé tokens numéricos de cada bloque modificado contra el original. Las únicas diferencias son identificadores de sección (AX.x, M7, M8, M10, M12, M07). **No cambió ningún valor de cálculo.**
- No hubo cambios en `calc/`, así que no re-ejecuté scripts. Motivo: el punto 2 no toca `calc/`.

## Observaciones (no bloqueantes)

1. **Registro desactualizado.** `logs_etapa1/cambios_p2.md` cita líneas que ya no corresponden al cambio:
   - `M02_libreto.md:82` y `:117` (la línea 117 es hoy un `>` vacío). El cambio real de M11 está en la línea 86, y el de M12/M7 en 128 y 160.
   - Motivo probable: otros puntos insertaron líneas antes. Conviene actualizar el registro con las líneas actuales.
2. **Redundancia en M02:128.** Dos veces «fuera del alcance de este curso» en el mismo párrafo.
3. **Redundancia en M06:46.** «…no reemplaza un presupuesto completo, fuera del alcance de este curso» y, al final del mismo párrafo, «el presupuesto completo queda fuera del alcance de este curso».
4. **Frase ambigua en M06:140.** «La deducción de un factor aleatorio queda fuera del alcance de este curso; no cubre estas tablas» no queda claro qué quiere decir con «no cubre». Propuesta: «…queda fuera del alcance de este curso; las tablas citadas son la referencia para consultarla».
5. **Repetición de la misma exclusión en M04.** La deducción del divisor n−1 aparece en M04:13, M04:34 y M04:292. Basta con una mención en la tabla y otra en el cierre.

## Qué no revisé

- No ejecuté las prácticas HTML ni los scripts de `calc/` (sin cambios).
- No verifiqué si las citas bibliográficas externas (Crowder, ISO, GUM, Hahs-Vaughn) se conservaron tal como estaban; el punto 2 no las toca, y sí están en M05:251 y M06:140.
