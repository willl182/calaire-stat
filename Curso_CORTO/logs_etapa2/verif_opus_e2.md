# Verificación de cierre de la etapa 2 (Opus) — Curso_CORTO

**Veredicto: ETAPA 2 NO CERRADA.**

H1–H3 y la observación de `verif_sol_e2.md` quedaron resueltos en lo sustancial. Pero la corrección de H1 dejó **texto vecino que contradice la nueva agenda** (H-O1) y una tabla del plan sin marcar como superada (H-O2). Son ajustes menores, pero rompen la coherencia de la temporización, que era justamente lo que había que cerrar.

## Comprobación de los pendientes anteriores

| Pendiente | Estado | Evidencia |
|---|---|---|
| H1: temporización por sesión | **Resuelto en agenda y plan** | Las agendas separan la narración medida del bloque «Ejemplos en pizarra, lectura de gráficos y discusión guiada»: `M02_libreto.md:8–9`, `M03_libreto.md:8–9`, `M04_libreto.md:8–9`, `M05_libreto.md:8–9`, `M06_libreto.md:8–9`. Cada agenda suma 120 (M02 10+33+14+25+15+23; M03 15+32+17+25+15+16; M04 15+25+20+25+15+20; M05 15+34+11+25+15+20; M06 10+40+19+25+10+15+1). Coinciden fila a fila con `00_plan_corto.md:99–105`. |
| H2: minuto faltante de la sesión 5 | **Resuelto** | `00_plan_corto.md:84` incluye «preguntas 1 min»: 44+15+25+10+10+15+1 = 120. |
| H3: «sesgos opuestos» en M02 | **Resuelto** | `M02_libreto.md:31` describe dispersión, grupos y tendencia; ninguna aparición de «sesgos opuestos» en libretos ni en `calc/`. |
| Observación: devolución de la tarea final | **Resuelto** | `M06_libreto.md:203` y `00_plan_corto.md:107`: entrega escrita después de la sesión 5, retroalimentación fuera de las 10 h. |

### Conteo de narración (`orquesta_curso_corto/contar_narracion.py M0*_libreto.md`)

| Libreto | Palabras | Min (130 p/min) | Plan `:101–105` | Agenda |
|---|---:|---:|---|---|
| M02 | 4 225 | 32,5 | 33 (4 225) | 33 |
| M03 | 4 175 | 32,1 | 32 (4 175) | 32 |
| M04 | 3 229 | 24,8 | 25 (3 229) | 25 |
| M05 | 4 461 | 34,3 | 34 (4 461) | 34 |
| M06 | 5 160 | 39,7 | 40 (5 160) | 40 |

Los conteos de palabras coinciden exactamente con el plan y los minutos redondeados con las agendas. Total: 5 × 120 = 600 min.

## Hallazgos nuevos

### H-O1 — Nota residual de M03 contradice la agenda corregida (bloqueante para H1)

`M03_libreto.md:14`: «La narración prevista suma aproximadamente **3065 palabras en B** (24 min…) y **2781 palabras en I** (21 min). El total de 49 minutos sigue el plan de sesión…». Justo debajo de una agenda que asigna 32 min de narración (`:8`) y 17 de discusión guiada (`:9`). Son 5 846 palabras frente a las 4 175 medidas, y «49 minutos» corresponde a la asignación anterior. **Para cerrar:** retirar la nota o alinearla con 4 175 palabras ≈ 32 min + 17 min de discusión guiada.

### H-O2 — Tabla «Estructura final» del plan conserva la narración antigua sin marcarla

`00_plan_corto.md:80–84` sigue indicando «Narración B + I» 47 / 49 / 53→45 / 56→45 / 44+15 min. La tabla «Temporización verificada» (`:99–105`) reparte esos mismos minutos entre narración medida y discusión guiada, pero nada indica que la primera tabla haya quedado superada. Las sumas son compatibles (p. ej., 47 = 33 + 14), aunque el rótulo «Narración» de `:78` ya no corresponde a lo que se narra. **Para cerrar:** renombrar la columna (p. ej., «Narración + discusión guiada») o remitir a `:95`.

### H-O3 — Agendas de M03 y M04 sin fila de total (menor, no bloqueante)

`M03_libreto.md:5–12` y `M04_libreto.md:5–12` no tienen la fila **Total** que sí aparece en M02, M05 y M06. Suman 120. Solo es una cuestión de homogeneidad.

## Restos del nivel A

No hay secciones, prácticas ni escenas A activas en libretos ni en `calc/`. Busqué «Nivel A», «Práctica A», «Escena A», rótulos A1…, AX., M07–M13 y «sesgos opuestos». Las referencias a A del plan son historia del recorte (`00_plan_corto.md:72`, `:88`). La escena I6 R&R es la excepción que el plan ordenó conservar en I.

## Cobertura frente al PDF (M2–M6)

El PDF (una página, «Temario resumido») pide M2 Descriptiva, M3 Probabilidad y distribuciones, M4 Inferencia, M5 Diseño de experimentos y M6 ANOVA y precisión. Las correcciones posteriores solo tocaron agendas, ficha de M02 y la nota de la tarea final. Los contenidos siguen presentes: IQR y atípicos en M02, distribuciones incluida la triangular en M03, valor p e intervalos en M04, aleatorización y planificación en M05, precisión intermedia y R&R (I6) en M06. **Cobertura: se mantiene.**

## Ejecución de calc/ (copia temporal)

Usé una copia en `mktemp -d` con `/home/w421/w421/calaire-stat/Curso_COMPLETO/curso/.venv/bin/python -I`.

| Script | Código | stderr |
|---|---:|---|
| M02_examples.py, M02_practicas_luna.py | 0, 0 | vacío |
| M03_ejemplos.py, M03_practicas_luna.py | 0, 0 | vacío |
| M04_ejemplos.py, M04_practicas_luna.py | 0, 0 | vacío |
| M05_diseno.py, M05_practicas_luna.py | 0, 0 | vacío |
| M06_ejemplos.py, M06_practicas_luna.py, M06_RR_CALAIRE.py, M06_practica_I_grafico.py | 0, 0, 0, 0 | vacío |

**12/12 correctos.** Los HTML de la copia (`M02_practica_B_grafico.html`, `M02_practica_I_grafico.html`, `M06_practica_I_residuos.html`, `calc/M03_practica_I_probabilidad.html`) son idénticos byte a byte a los originales.

## Condiciones de cierre

1. Corregir o retirar `M03_libreto.md:14` (H-O1).
2. Ajustar el rótulo de la columna «Narración» de `00_plan_corto.md:78–84`, o remitir a la tabla verificada (H-O2).
3. Opcional: añadir la fila Total en las agendas de M03 y M04 (H-O3).

Con 1 y 2, la etapa 2 puede declararse cerrada sin más verificación de contenido ni de scripts.
