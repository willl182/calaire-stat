# M13 — bitácora de prácticas (Luna)

## Plan

- Alcance: solo nivel A de M13, según `prop_e.md` §5, módulo M13. La práctica integradora cubre Monte Carlo frente a propagación lineal, salidas múltiples con covarianza, bootstrap por bloques y Huber frente a OLS. No se añade taller integrador.
- Edición: desarrollar únicamente el bloque de práctica A en `curso/S4_numericos_integracion/M13_libreto.md` y mantener el trabajo localizado en scripts de cálculo M13. No editar referencias, claves, citas existentes, escenas ajenas a la práctica, otros capítulos, guía ni revisión final.
- Datos: simulaciones reproducibles con semilla/reglas declaradas; ningún dato se atribuye a CALAIRE.
- Gráficos: esta práctica evalúa cálculos, intervalos y matrices; no requiere gráficos. No se añadió visualización.

## Ronda de correcciones Haiku

| Hallazgo | Decisión | Ubicación | Resultado |
|---|---|---|---|
| H-01 | Aplicar | `M13_libreto.md`, escena A1 y solución docente, líneas 51 y 234 | Se aclara que el valor para comparar extremos es $u=1,041437$ sin redondear; $1,0$ se usa solo como presentación. Con valor redondeado la conclusión cambia, así que no se redondea antes de decidir. Recalculado: diferencias de extremos 0,011715 y 0,000601 nmol/mol, ambas ≤0,05. |
| H-02 | Aplicar | `calc/M13_practicas_luna.py`, `M13_libreto.md` apartado 2 y solución | Se añadió comprobación independiente mediante diferencias finitas centradas de la transformación de covarianza, además de imprimir en ejecución la tabla de 36 observaciones. Discrepancia relativa máxima: $1,8324387\times10^{-9}$ (reportada como $1,8\times10^{-9}$). La solución limita explícitamente el significado de esta comprobación: valida la transformación, no valida independientemente el ajuste ni los datos. |
| H-03 | Aplicar | `calc/M13_practicas_luna.py`, `M13_libreto.md` solución A3 | El bootstrap de práctica ahora continúa el mismo generador `rng` después de Monte Carlo. El límite superior reproducido es 1,0015936167, que redondea a 1,00159362; la solución mantiene ocho decimales y la ejecución del ejemplo/práctica da los mismos cuantiles. |
| H-04 | Aplicar | `M13_libreto.md`, criterios de logro por apartado | Se agregó señal explícita de escalamiento a cada uno de los cuatro criterios, incluyendo incertidumbre numérica/distribuciones, admisibilidad y dependencia, pocos bloques e influencia/cambio real. |
| H-05 | Aplicar | `M13_libreto.md`, criterios de logro | Se reemplazó el criterio global por cuatro criterios separados, cada uno con resultado observable, supuestos y verificación. |
| H-06 | Aplicar | `calc/M13_practicas_luna.py` y `M13_libreto.md` enunciado A2 | El script imprime la matriz 6×6 bajo el rótulo “A2: observaciones y”; el enunciado indica filas por día, columnas por nivel y dónde obtenerla. |
| H-07 | Aplicar | `calc/M13_ejemplos.py` y `calc/M13_practicas_luna.py` | Se centralizaron niveles, desplazamientos, ruido, abscisas y respuestas simuladas en constantes del módulo de ejemplos; se añadieron funciones de generación diaria. La práctica importa esas constantes/regla y ya no duplica los literales. |

## Ejecución final

- Se desarrolló el bloque `[PRÁCTICA] A` con cuatro apartados aplicados, soluciones docentes, decisiones operativas, señales para escalar y criterios observables separados. Se conservan unidades nmol/mol y coma decimal en el libreto.
- `curso/.venv/bin/python curso/S4_numericos_integracion/calc/M13_practicas_luna.py`: terminó con rc=0 tras la ronda. A1: estimación 418,762475; $u_{lin}=1,041437$; media MC 418,763825; $s_{MC}=1,040327$; IC central [416,733012; 420,803052]; diferencias de extremos [0,011715; 0,000601] nmol/mol. A2: $a=0,65184834$ nmol/mol, $b=1,00151145$, $u(a)=0,107231$, $u(b)=0,000046137$; incertidumbres de corrección 0,107113, 0,107624 y 0,108696 nmol/mol. Diferencia relativa máxima jacobiana centrada/analítica: $1,8324387\times10^{-9}$. Se imprimieron las 36 indicaciones simuladas en matriz 6×6. A3: IC bootstrap de pendiente [1,0014318720; 1,0015936167] y corrección a 250 [−1,2122884799; −0,8298598133] nmol/mol. A4: Huber $a=0,38975488$, $b=1,00293061$, escala 0,204992519 nmol/mol, umbral 0,275714938 nmol/mol y peso 0,035687014; predicción a 200: OLS 201,969238 y Huber 200,975878 nmol/mol.
- `curso/.venv/bin/python curso/S4_numericos_integracion/calc/M13_ejemplos.py`: terminó con rc=0. Tras centralizar literales, el bootstrap del ejemplo y de la práctica concuerda: límite superior de pendiente 1,0015936167 y demás cuantiles coincidentes.
- En la primera ejecución de comprobación, tras cambiar el origen de los datos compartidos, apareció un `NameError` por referencia antigua a `offsets`; se corrigió a `ejemplos.DAY_OFFSETS` y se repitieron ambos scripts hasta rc=0.
- No se modificaron las referencias bibliográficas ni sus claves, citas existentes fuera de cambios estrictamente en el bloque de práctica, otros capítulos, guía o revisión final. No se hizo commit.
