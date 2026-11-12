# M04 — ronda de correcciones de prácticas (luna)

Fecha: 2026-10-27.

## Alcance y límites

Se revisaron los ocho hallazgos H-01…H-08 de `M04_practicas_revision_haiku.md`. Se editaron únicamente los tres bloques de práctica y el script de cálculo, con dos correcciones colaterales mínimas pedidas por hallazgos: la frase obsoleta inmediatamente anterior a práctica B (H-06), la explicación de `u(s)` en I4 (H-07) y la mención de G*Power en la explicación de planificación (H-08). No se tocaron referencias, claves, citas, secciones bibliográficas, otros capítulos, guía ni `revision_final.md`. Las sustituciones concurrentes de referencias en Welch/A1 se conservaron tal como estaban.

Los datos son vectores y resúmenes sintéticos fijos para formación; no describen CALAIRE. Unidad: nmol/mol; coma decimal en prosa. No hay gráficos requeridos por este módulo.

## Tabla de decisiones y resultados

| Hallazgo | Decisión | Ubicación | Resultado |
|---|---|---|---|
| H-01 | Aplicado | `M04_libreto.md`: práctica B, apartados 1–2 y 5 de I, residuos de A; `calc/M04_practicas_luna.py` | Los vectores de B e I y el vector de extremos/residuos A ahora difieren de los ejemplos ilustrativos. Los resultados de práctica se recalcularon y reemplazaron. Se mantienen deliberadamente los parámetros de potencia de los ejemplos donde son los únicos datos numéricos que definen el plan; la evaluación de ejecución numérica es distinta y el enunciado declara explícitamente cada alternativa. |
| H-02 | Aplicado | `M04_libreto.md`: solución I y A; `calc/M04_practicas_luna.py` | Se añadieron comparaciones independientes `scipy.stats.ttest_rel`, `ttest_ind(equal_var=False)`, potencia directa mediante `scipy.stats.nct` (verificación de `statsmodels`) y forma matricial `r @ solve(V,r)` frente a suma escalar. Se cambiaron las frases para describir esas operaciones realmente existentes. |
| H-03 | Aplicado | `M04_libreto.md`: rúbrica al final de práctica I | Tabla por cada apartado con cuatro dimensiones explícitas: método, supuestos, resultado e interpretación. Criterio indica repetir el apartado cuando falla un supuesto o la unidad experimental. |
| H-04 | Aplicado con alcance limitado | `M04_libreto.md`: enunciado y solución del apartado 5 de I | Se declara el valor crítico Q=0,59 como crítico didáctico suministrado para la variante de rango completo, sin atribución normativa. Se expresa que no es criterio normativo y que la conclusión queda limitada a la convención declarada. No se amplió ni alteró bibliografía porque se prohibió modificar referencias y Haiku no verificó ASTM E178. |
| H-05 | Aplicado | `calc/M04_practicas_luna.py`; práctica B | La decisión respecto de ±0,30 se calcula ahora usando el IC95 que solicita el enunciado y reporta la solución (IC95 [−0,1218; 0,4218]); no se usa IC90 bajo esa etiqueta. |
| H-06 | Aplicado | `M04_libreto.md`: cierre de escena B3, inmediatamente anterior al bloque B | Se sustituyó «se desarrollará en la fase de ejercicios» por remisión a la práctica siguiente y al vector distinto. |
| H-07 | Aplicado | `M04_libreto.md`: escena I4 | Se aclaró que E.4.3 se refiere a la desviación muestral `s`; `s/√n` es el error estándar de la media y no interviene en la aproximación de `u(s)`. |
| H-08 | Aplicado | `M04_libreto.md`: escena I3 | Se retiró la promesa de ilustración con G*Power; la frase ahora describe `statsmodels` y el redondeo del tamaño. No se alteró la referencia citada. |
| S-M04-01 | Aplicado: se cambió solo la diferencia del apartado 4 de I de 0,45 a 0,30 nmol/mol | Enunciado de práctica I | Mantiene $d_C=0,5$ y los resultados ya reproducidos: 63,77 observaciones por grupo, redondeo 64 y potencia 0,2161 con 12 por grupo. |
| S-M04-02 | Aplicado | Solución docente, apartado 5 de I | Se distingue explícitamente el Q matricial de consistencia chi-cuadrado en A del Q de Dixon del apartado de extremos. |
| S-M04-03 | Aplicado | Enunciado y solución docente, apartado 5 de I; script | Grubbs usa el crítico unilateral calculado con SciPy para n=8, alfa=0,01 (2,2208). Dixon conserva Qcrit=0,59 como crítico didáctico suministrado para la variante superior/rango completo, sin asignarle nivel nominal ni garantía de alfa. |

## Resultados finales reproducidos

Comando ejecutado: `curso/.venv/bin/python -I curso/S1_fundamentos/calc/M04_practicas_luna.py`.

- B, ocho jornadas: media 0,1500; s 0,3251; SE 0,1150 nmol/mol; IC95 [−0,1218; 0,4218]; t=1,3049; p=0,2332. IC95 incluye +0,30 pero no −0,30: no descarta efectos de magnitud 0,30 en ambos sentidos.
- I pareada: media de A−B 0,2250; s=0,1581; SE=0,0559; gl=7; IC95 [0,0928; 0,3572]; t=4,0249; p=0,0050.
- I Welch: medias 10,0167 y 10,9000; diferencia A−B −0,8833; SE=0,2005; gl=11,0000; IC95 [−1,3245; −0,4421]; t=−4,4066; p=0,0011.
- Varianza B: s²=0,1057 (nmol/mol)²; IC95 [0,0462; 0,4379]; chi²=2,9600; p=0,2226. F: razón=0,7152; gl=(5,6); IC95 [0,1195; 4,9906]; p=0,7302.
- Planificación: media y parejas n*=33,3671, redondeo 34; potencia con n=16: 0,4649. Dos grupos, efecto 0,5: n*=63,7656 por grupo, redondeo 64; potencia con 12 por grupo: 0,2161; potencia directa por t no central al tamaño continuo objetivo: 0,8000000.
- Incertidumbre de s: 0,0869 nmol/mol. Extremos: G=2,3157 frente al crítico unilateral calculado con SciPy 2,2208 para n=8 y alfa=0,01; Q de Dixon=0,6667 frente a 0,59 suministrado didácticamente para la variante superior/rango completo, sin garantía de nivel nominal. Decisión: investigar; no borrar automáticamente.
- A: Bonferroni ajustados [0,036; 0,093; 0,600]. TOST conserva los datos sintéticos del caso de práctica: IC90 [−0,0747; 0,2347], p inferior 0,000217 y superior 0,011832; el contraste frente a cero da t=0,8944, p≈0,382. Chi-cuadrado con residuos nuevos: Q escalar=3,3600 y Q matricial=3,3600; gl=3, crítico=7,8147, p=0,3394.
- Salida final del script tras S-M04-01..04: `comprobaciones_practicas_M04=OK`; crítico unilateral de Grubbs reproducido por SciPy: 2,220833451510429. Código de salida real: 0.
- S-M04-04 | Aplicado | `calc/M04_practicas_luna.py:21`: se reemplazó `descarta_magnitud is False` por `assert not descarta_magnitud`, porque el resultado puede ser `numpy.bool_` y no es idéntico al singleton `False`. Se conserva la lógica AND del cálculo.

## Validaciones y notas

El script compara los cálculos manuales pareado/Welch con funciones de SciPy; compara `statsmodels` con potencia basada en la t no central; y verifica numéricamente la forma cuadrática matricial diagonal frente a suma escalar. Las comprobaciones pasan. Los apartados de consistencia y equivalencia conservan los escenarios docentes dados; se alteró el vector de residuos de consistencia para atender H-01, manteniendo su interpretación.

**Pendiente fuera de alcance:** el índice de sección, mencionado en la revisión Haiku, no se editó. No se hicieron commits.