# Bitácora de desarrollo — prácticas M10

Fecha: 2026-10-27. Alcance autorizado: reemplazar únicamente los tres marcadores de práctica B, I y A en `curso/S3_comparacion_decision/M10_libreto.md`; no taller integrador.

## Plan

- **B:** completar certificado docente; resultado, incertidumbre expandida, k, intervalo, función/regla suministrada y acción dentro/cerca/fuera del límite. Modelo y regla ya explicados en M10-B; practicar aplicación, no selección.
- **I:** elegir y justificar entre dos reglas; cuantificar falsas aceptaciones/rechazos condicionales y relacionar incertidumbre con tolerancia. Mantenerse en normal, guardas y riesgo del alcance I.
- **A:** riesgo específico/global con modelo explícito, requisito bilateral y decisión con dependencia. Contrastar numericamente con/sin covarianza y reportar unidades; remitir deducciones a AX.2, AX.9 y AX.10.
- Datos simulados mediante parámetros fijados en el script propio, sin atribución a CALAIRE. No se requieren gráficos para resolver estos cálculos de reglas y riesgos; por tanto no se generan visualizaciones.

## Ejecución

- Leídos `curso/guia_libreto.md`, `prop_e.md` y `curso/revision_final.md`. La petición actual autoriza desarrollar las prácticas pese al marcador de fase anterior. Respetado el alcance por nivel de prop_e §5, M10.
- Leída la habilidad dataviz en la ruta indicada por el usuario. No se necesita gráfico en estas prácticas; conforme a H-08, no se ejecutó ni se declara validación de paleta.
- Archivos: script `curso/S3_comparacion_decision/calc/M10_practicas_luna.py` y esta bitácora. Se editaron localizadamente solo los bloques prácticos M10 en el libreto y el script propio.
- Ejecución final: `curso/.venv/bin/python curso/S3_comparacion_decision/calc/M10_practicas_luna.py`, código 0. B: $u=0,6$; intervalos [98,8;101,2] aceptar, [101,0;103,4] retener/escalar y [104,8;107,2] rechazar; zona de aceptación central [99,2;101,8], rechazo $y<96,8$ o $y>104,2$ nmol/mol.
- I: $g=0$, rechazo conforme en $\\theta=9$: 0,10564977 y falsa aceptación en $\\theta=10,5$: 0,26598553; $g=1$: 0,50000000 y 0,03039636. $U=1,6$ nmol/mol, TUR definido=6,25. En el resultado observado $y=9$, ambas reglas inclusivas aceptan.
- A: global, $g=0$: falsa aceptación 0,02646254 y falso rechazo 0,02659615; $g=1$: 0,00337106 y 0,08670579. Covarianza=0,48 (nmol/mol)²; incertidumbre del promedio=0,56568542 bajo independencia y 0,74833148 con covarianza. En $\\theta=10,5$, falsa aceptación para el promedio con guarda=0,00400497 y 0,02251044, respectivamente. Caso específico separado, $y=0,u=6$: cada cola=0,02623387; riesgo de falsa aceptación dado que se acepta=0,05246774; conformidad=0,94753226; suma=1,00000000.
- Aserciones ejecutadas: umbrales B; resultados I; varianzas del promedio; falsa aceptación dependiente/independiente; simetría de colas y suma posterior. La salida anterior queda transcrita en esta bitácora; se vuelve a ejecutar al cerrar.
- `git diff --check -- curso/S3_comparacion_decision/M10_libreto.md curso/S3_comparacion_decision/calc/M10_practicas_luna.py curso/logs/M10_practicas_luna.md` terminó sin errores.

## Correcciones tras revisión Haiku

| Hallazgo | Decisión | Ubicación y resultado |
|---|---|---|
| H-01 | Aplicado | M10 A, enunciado: la regla se aplica expresamente a $\\bar Y=(Y_1+Y_2)/2$. Los riesgos globales continúan siendo los definidos para una medición individual y ya no se comparan con la falsa aceptación del promedio en $\\theta=10,5$; se aclara que el punto de dependencia usa el promedio. Cálculo final: 0,00400497 (independencia) y 0,02251044 (con covarianza). |
| H-02 | Aplicado | `calc/M10_practicas_luna.py`, `a_risks()`: agregado cálculo posterior truncado para $y=0,u=6$, ambas colas y aserciones de normalización/reproducción. Salida final: cola inferior=cola superior=0,02623387; total no conforme=0,05246774; conforme=0,94753226; suma=1,00000000. |
| H-03 | Aplicado | M10 A, enunciado y solución: el caso $y=0$ se separa como medición única con decisión sin guarda; se identifica que se acepta y que el riesgo específico de falsa aceptación dado el resultado es 0,05246774. |
| H-04 | Aplicado | M10 I, enunciado y solución: los extremos de ambas zonas son inclusivos; $y=9$ queda aceptado bajo $g=0$ y $g=1$. Las probabilidades condicionadas a $\\theta$ se conservan como riesgos distintos de la decisión puntual. |
| H-05 | Aplicado | `calc/M10_practicas_luna.py`: se ejecutan aserciones para simetría de las colas, suma conforme+no conforme, los dos riesgos de A con y sin covarianza y los resultados I clave. Bitácora corregida a estas comprobaciones efectivas; no se atribuyen al script verificaciones no implementadas. |
| H-06 | Aplicado | M10 I, decisión operativa: recomendación condicional cuantificada; con prioridad de falsa aceptación, $g=1$ la reduce 0,2660→0,0304, y sube el rechazo conforme en $\\theta=9$ de 0,1056→0,5000. |
| H-07 | Aplicado | M10 B, enunciado: se describe la simulación como valores fijados explícitamente en el script, no como salida de un generador. `b_interval_decisions()` imprime parámetros y resultados declarados. |
| H-08 | Aplicado | Se elimina la aseveración de validación de paleta: M10 no requiere gráfico; no se ejecutó ni se reporta validación cromática. |
| H-09 | Aplicado | `i_risks()` elimina la línea de rechazo duplicada y calcula probabilidades usando variables theta explícitas; M10 A calcula efectivamente la suma de probabilidades y verifica 1. |

## Referencias y pendientes

- No se modificaron citas existentes, claves, bibliografía ni secciones de referencias. Las prácticas usan citas ya presentes en el capítulo y remiten deducciones a anexos.
- El archivo `curso/revision_final.md` no se editó. No se hicieron commits.
- La regla B, la especificación I y todos los valores de riesgo son didácticos; no son criterios, datos ni resultados de CALAIRE. En A, todos los modelos y valores son simulados y se expresan en nmol/mol cuando corresponde.
- No se sustituyeron ni alteraron otros capítulos. Solo se corrigieron bloques de práctica M10 y su script de cálculo.
