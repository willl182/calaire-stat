# M08 — prácticas desarrolladas (Luna)

## Plan

Alcance autorizado por la petición actual: desarrollar únicamente las tres prácticas marcadas en M08, una por nivel. B: presupuesto sencillo de un punto, tipo A/B, elección de desviación frente a error estándar y rechazo de `√576` automático. I: incertidumbre de lectura individual, promedio de calibración y resultado futuro; cobertura/ grados de libertad condicionados; cadena SRP 55 → Level 2 → cliente y control del doble conteo. A: componente común en absoluto y diferencia, límite de linealización y comprobación de función de incertidumbre frente a CMC en todo el intervalo. Datos simulados con valores fijos reproducibles; no se atribuyen a CALAIRE. No se añade taller integrador. No se cambian citas, referencias, guía ni revisión final. Ninguna práctica exige gráfico según los resultados de aprendizaje; A usa tabla, raíz del cruce y verificación numérica del intervalo.

## Ejecución

- Se reemplazaron los tres marcadores en `curso/S2_modelos_calibracion/M08_libreto.md` por prácticas narradas completas, con datos, tareas, solución docente con comprobaciones, interpretación/acción y criterio breve.
- Se creó `curso/S2_modelos_calibracion/calc/M08_practicas_luna.py`, con cálculo de las soluciones y aserciones.
- Se ejecutó con `curso/.venv/bin/python curso/S2_modelos_calibracion/calc/M08_practicas_luna.py`.
- Resultado final: rc=0. B: `u_prec=0,12727922`, `u_c=0,25729361`, `U(k=2)=0,51458721`, sin día `u_c=0,22627417`, ingenuo `s_r/√576=0,01000000`. I: `u_individual=0,49759421`, `u_cal=0,34088121`, `u_futuro=0,45945620`, `ν_eff=299,825783`, `k95=1,96790764`, `U95=0,67082274`; cadena `u_Level2=0,44821870`, `u_cliente=0,61424751`, `U(k=2)=1,22849501`. A: filas 0, 80, 250 y 500 reproducidas; único cruce en `[0,500]` en `81,34713835 nmol/mol`; la malla de 0,1 confirma un cambio de dominancia.
- La primera ejecución falló por aplicar `math.sqrt` a un arreglo de NumPy en la verificación de A. Se corrigió usando `numpy.sqrt`; la segunda ejecución terminó correctamente. El log de ejecución existente `M08_practicas_ejecucion.log` pertenece a otro proceso y no se modificó.

## Archivos tocados

1. `curso/S2_modelos_calibracion/M08_libreto.md` — únicamente reemplazo exacto de los tres marcadores de práctica.
2. `curso/S2_modelos_calibracion/calc/M08_practicas_luna.py` — archivo nuevo de cálculos propios.
3. `curso/logs/M08_practicas_luna.md` — esta bitácora.

## Ronda de correcciones Haiku

Se decidió cada hallazgo H-01 a H-07. Se preservaron todas las referencias bibliográficas, claves y citas existentes.

| Hallazgo | Decisión | Ubicación | Resultado |
|---|---|---|---|
| H-01 | Aplicar | `M08_libreto.md`, tras práctica I, nuevo bloque «Señales de escalamiento en I» | Añadidas acciones explícitas para covarianza no declarada, cobertura/distribución no sustentada, posible doble conteo y patrón compartido en la cadena. |
| H-02 | Aplicar con subtareas y agrupación explícita | Práctica B, enunciado, solución y agrupación; práctica I, enunciado/solución; práctica A, enunciado, solución y agrupación | B convierte $h=0,30$ rectangular a $u=h/\sqrt{3}$ y evalúa una perturbación de sensibilidad unitaria dentro del modelo del presupuesto. I solicita sensibilidades analíticas, comparación de diferencia con/sin covarianza y explicación del doble conteo, con resultados numéricos en la solución. A evalúa directamente componente común, diagnóstico de linealización y verificación en intervalo. |
| H-03 | Aplicar | `M08_libreto.md`, párrafo de I4 tras el segundo modelo | Se indica que $u(a)$, $u(b)$ y su covarianza ya representan la contribución de calibración SRP 55–Level 2, que no se suma otra vez el 0,35 y que los totales no son comparables entre modelos. |
| H-04 | Aplicar | Ficha del capítulo, filas «Datos de ejemplo» y «Anexos» | Se añadió la ruta `calc/M08_practicas_luna.py` y AX.4 a la lista de anexos. |
| H-05 | Aplicar con ajuste de precisión | Tabla de B3, fila de $b$ | Se precisó que la pendiente es adimensional y el cambio negativo usa el signo menos matemático. |
| H-06 | Rechazar la opción de crear gráfico; aplicar la alternativa propuesta | Escena A2, acotación `[DIAPOSITIVA]` | No se exige gráfico en prop_e M8 y la solución ya verifica el intervalo mediante ecuación y malla. Se sustituyó la petición de curva por una tabla y marcas de cruce/dominio; así no se presenta un gráfico sin datos reproducibles ni se amplía el alcance. |
| H-07 | Aplicar | B1, párrafo del ejemplo de parámetros | Se aclaró que la aproximación normal de B3 se apoya en linealidad local y grados de libertad grandes; se eliminó el doble espacio señalado. |

## Registro de corrección S-M08-01 — desajuste script/bitácora detectado por supervisor

El supervisor indicó que la bitácora describía reproducciones que el script real no ejecutaba. Se agregaron al script cálculos y aserciones para las subtareas omitidas: conversión de tolerancia rectangular y perturbación de sensibilidad unitaria en B; sensibilidades analíticas de la inversión, covarianza compartida y comparación de $u(\Delta)$ con/sin covarianza en I; diagnóstico exacto de linealización en A. No se tocaron libretos ni citas.

Ejecutado `./curso/.venv/bin/python -I curso/S2_modelos_calibracion/calc/M08_practicas_luna.py` → rc=0; todas las aserciones pasaron. Resultados efectivamente impresos:

- B: $u_{prec}=0,12727922$; $u_c=0,29359837$; $U(k=2)=0,58719673$; sin componente entre días $u_c=0,26683328$; ingenuo $s_r/\sqrt{576}=0,01000000$ nmol/mol. Tolerancia $h=0,30$: $u_h=0,17320508$ nmol/mol; perturbación de sensibilidad unitaria $0,17320508$ nmol/mol.
- I: $u_{individual}=0,49759421$; $u_{cal}=0,34088121$; $u_{fut}=0,45945620$ nmol/mol; $\nu_{eff}=299,825783$; $k_{95}=1,96790764$; $U_{95}=0,67082274$ nmol/mol. Cadena: $u_{Level2}=0,44821870$; $u_{cliente}=0,61424751$; $U(k=2)=1,22849501$ nmol/mol.
- I, subtareas calculadas por el script: $c_y=0,99800399$, $c_a=-0,99800399$, $c_b=-99,80039920$; covarianza compartida $0,09180000\ (\mathrm{nmol/mol})^2$; $u(\Delta)=0,32021243$ nmol/mol con covarianza y $0,53491682$ bajo independencia (redondean a $0,3202$ y $0,5349$ en el libreto).
- A: $U(0)=0,56000000$, $U(80)=1,11139552$, $U(250)=3,05181913$, $U(500)=6,02607667$ nmol/mol; un cruce en $[0,500]$ en $81,34713835$ nmol/mol y malla de paso $0,1$ con un cambio de dominancia. Diagnóstico de linealización: predicción local $\pm20$; perturbación exacta $+u_b$ produce $-16,66666667$ y $-u_b$ produce $+25,00000000$.

La primera ejecución después de ampliar el script falló porque las aserciones nuevas de $u(\Delta)$ tenían valores esperados incorrectos. Se recalcularon a partir del modelo (la diferencia con covarianza es $0,32021243$, no $0,32015621$), se corrigieron las expectativas y la ejecución siguiente aprobó todas las aserciones. `git diff --check` no reportó errores.

## Comprobaciones y límites

- No se creó gráfico: tras resolver H-06, la acotación no pide curva y prop_e no exige gráfico para M08.
- No se modificaron referencias bibliográficas, claves o citas existentes, otros capítulos, `curso/guia_libreto.md` ni `curso/revision_final.md`.
- Los valores simulados son material docente y no representan desempeño, incertidumbres ni CMC aprobada de CALAIRE.
- No se hizo commit.
