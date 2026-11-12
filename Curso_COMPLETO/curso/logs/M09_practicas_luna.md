# Bitácora de prácticas M09 — Luna

## Plan

**Alcance:** desarrollar solo las tres prácticas fijadas por `prop_e.md` §5, módulo M9: B calcula diferencia, incertidumbre bajo independencia justificada y $E_n$ en dos puntos, e identifica la falta de justificación en Level 2–SRP 55 sin calcular covarianza; I estima una diferencia con covarianza del SRP 55 compartido y cobertura declarada; A calcula diferencia e incertidumbre frente a referencia común y separa el grado de equivalencia del indicador normalizado. Niveles acumulativos. No añadir taller integrador ni contenido fuera de nivel.

**Escenas/prácticas:** se sustituyen exactamente los tres marcadores del libreto M09 por prácticas narradas completas con datos, tareas, solución docente numérica, interpretación, decisión operativa, criterio de logro y escalamiento donde procede. No se editan otros capítulos, guía, revisión final ni referencias/citas existentes.

**Datos:** todos los de práctica son simulados, fijados determinísticamente en `curso/S3_comparacion_decision/calc/M09_practicas_luna.py`; ninguna cifra se atribuye a CALAIRE. Unidad nmol/mol y coma decimal en el libreto. No se requieren gráficos: son comparaciones numéricas/tabulares, no una visualización.

## Ejecución

- Creado `curso/S3_comparacion_decision/calc/M09_practicas_luna.py`, con cálculos independientes reproducibles de B, I y A.
- Editado únicamente el bloque de cada marcador en `curso/S3_comparacion_decision/M09_libreto.md`.
- Ejecutado `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M09_practicas_luna.py` (rc=0). Resultados: B, $E_n=0,600000$ y $-0,256074$ (ambos dentro del criterio); I, covarianza $0,018000\ (nmol/mol)^2$, varianza de diferencia $0,026500\ (nmol/mol)^2$, $u(\Delta)=0,162788206$ y $U=0,325576412$ nmol/mol; A, $D/u(D)/U(D)$ = $0,300000/0,250000/0,500000$ y $0,800000/0,781024968/1,562049935$ nmol/mol.
- Ejecutado también `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M09_ejemplos.py` (rc=0), que valida GGMR frente a ISO/TS 28037 y conserva reproducción de los ejemplos ya existentes.

## Archivos tocados

1. `curso/S3_comparacion_decision/M09_libreto.md` — sustitución localizada de los tres marcadores; no se cambió texto bibliográfico ni sección de referencias.
2. `curso/S3_comparacion_decision/calc/M09_practicas_luna.py` — nuevo script de cálculo de prácticas.
3. `curso/logs/M09_practicas_luna.md` — esta bitácora.

## Comprobaciones

- `git diff --check -- curso/S3_comparacion_decision/M09_libreto.md curso/S3_comparacion_decision/calc/M09_practicas_luna.py`: sin errores de whitespace.
- Conteo de libreto: 3 etiquetas `### [PRÁCTICA]`; 0 marcadores `[PRÁCTICA — fase de ejercicios]`.
- Se mantuvieron los alcances distintos de B, I y A y las cifras del script se cotejaron con las soluciones del libreto.
- No se crearon gráficos al no ser parte del alcance gráfico de estas prácticas.
- No se hicieron commits.

## Correcciones — ronda Haiku M09 (2026-10-27)

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | Aplicado | A: se añadió sensibilidad a covarianza nula frente a la mitad del máximo admisible en ambos puntos, con interpretación y requisito de evidencia presupuestaria. Libreto, práctica A; script. Cálculos ejecutados y resultados finales registrados abajo. |
| H-02 | Aplicado | A: se identifica `calc/M09_practicas_luna.py` como segunda implementación; el script comprueba las dos hipótesis y la admisibilidad. Libreto, solución A. |
| H-03 | Aplicado | Script I: imprime Δ y ambos cocientes normalizados, valida residuales no negativos, admisibilidad de covarianza y varianza de diferencia. Se precisa el alcance del cotejo; las cifras impresas se cotejaron con la solución y las comprobaciones se ejecutan por `assert`. |
| H-04 | Aplicado | A: se conserva deliberadamente el punto 80 que conecta con la referencia común y se cambia el punto 420 a participante 421,10; referencia 420,20; u=0,70 y 0,40. Ya no repite los dos puntos de B y sustenta la sensibilidad específica de A. |
| H-05 | Aplicado | Se añade esta sección Correcciones con decisión individual y ubicación/resultado para cada H-xx, según guía §8. |
| H-06 | Aplicado | Se dividieron las soluciones B e I en párrafos cortos; A se separa en cálculo base y sensibilidad. |
| H-07 | Aplicado | I declara que sin covarianza la extensión es 0,70 y pasa; con covarianza es 1,0750 y queda fuera del criterio didáctico. Se matiza como resultado próximo al límite y se indica escalar. |

## Ejecución de correcciones y resultados finales

- Ejecutado `curso/.venv/bin/python -I curso/S3_comparacion_decision/calc/M09_practicas_luna.py` (rc=0). Los `assert` de I y A pasaron. Resultados finales:

| Nivel | Punto / hipótesis | Δ o D (nmol/mol) | cov (nmol/mol)² | u (nmol/mol) | U, k=2 (nmol/mol) | cociente |
|---|---|---:|---:|---:|---:|---:|
| B | 80 | 0,300000 | — | uΔ=0,250000 | U1=0,400000; U2=0,300000 | En=0,600000; cumple |
| B | 420 | −0,400000 | — | uΔ=0,781025 | U1=1,200000; U2=1,000000 | En=−0,256074; cumple |
| I | compartida | 0,350000 | 0,018000 | uΔ=0,162788 | UΔ=0,325576 | Δ/U=1,075016; no pasa criterio; sin cov: 0,700000 |
| A | 80, nula | 0,300000 | 0,000000 | uD=0,250000 | 0,500000 | D/U=0,600000 |
| A | 80, mitad admisible | 0,300000 | 0,015000 | uD=0,180278 | 0,360555 | D/U=0,832050 |
| A | 420, nula | 0,900000 | 0,000000 | uD=0,806226 | 1,612452 | D/U=0,558156 |
| A | 420, mitad admisible | 0,900000 | 0,140000 | uD=0,608276 | 1,216553 | D/U=0,739795 |

- El cotejo de esta ronda abarca todas las cifras de las soluciones B, I y A actualizadas. Las operaciones base y sensibilidad se contrastaron manualmente con la fórmula; el script valida las restricciones con `assert`. `M09_ejemplos.py` no se reejecutó en esta ronda porque sus ejemplos de GGMR no se modificaron.
- No se modificaron citas, claves, referencias bibliográficas, contenido fuera de los tres bloques de práctica, otros capítulos, guía ni revisión final. No se crearon gráficos porque estas tareas no exigen visualización. Sin commits.
