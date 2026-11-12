# AX. Anexos de deducciones — bitácora de desarrollo

## Plan

### Alcance por nivel

Los anexos contienen deducciones y, conforme a prop_e §9, no se evalúan. No se asigna a los anexos una práctica ni un nivel curricular nuevo: se explican pausadamente los resultados que los módulos usan. El nivel indicado al inicio de cada anexo es el primero que utiliza ese resultado; las personas de niveles acumulativos posteriores también pueden consultarlo.

- **Básico (B):** AX.1 (divisor `n − 1` y grados de libertad de `s`, M2-B/M4-B); AX.2 (varianza de combinaciones lineales y propagación con covarianza, M3-I y M8, además de las remisiones A de M1); AX.3 (varianzas rectangular y triangular, M3-B); AX.4 (cuadrados medios esperados y contribución de precisión al promedio, M6-B); AX.9 (diferencia con patrón compartido y referencia común, resultado usado en comparaciones M9); AX.10 (probabilidades de falsa aceptación y falso rechazo, M10); AX.11 (límites de confianza de indicadores de precisión y sesgo, M6/M12); AX.7 se utiliza desde I, no se imputa como contenido B.
- **Intermedio (I):** AX.5 (ecuaciones normales OLS/WLS y covarianza de `a,b`, M7-I); AX.6 (incertidumbre de predicción inversa, M7-I); AX.7 (Welch–Satterthwaite y condiciones, M4-I/M8-I); AX.9 (diferencias con patrón compartido, M9-I/M10); AX.10 (riesgo de decisión, M10-I); AX.11 (límites de confianza, M12-I). AX.2 y AX.4 se reutilizan en M8/M6-I; AX.3 se reutiliza en presupuestos de incertidumbre.
- **Avanzado (A):** AX.8 (formulación matricial GGMR con `V_xy = 0` y chi-cuadrado de consistencia, M7-A/M9-A); AX.9 (grado de equivalencia frente a referencia común, M9-A); AX.10 (riesgo específico/global y decisiones dependientes, M10-A); AX.12 (varianza EWMA y longitud media de corrida EWMA/CUSUM, M11-A); AX.13 (fundamento Monte Carlo GUM-S1 y control del número de ensayos, M13-A). AX.2, AX.5 y AX.9 también sustentan usos avanzados. Se respeta la exclusión de GGMR con `V_xy ≠ 0` y de KCRV combinado (prop_e §6; revision_final_prop_e.md, ajustes aplicados).

### Escenas previstas

Una escena por anexo: AX.1 divisor y pérdida de grados de libertad; AX.2 varianza de combinación lineal y expansión de Taylor; AX.3 integrales para rectangular/triangular y especificaciones `h`/`δ`; AX.4 modelo aleatorio de un factor, cuadrados medios esperados y varianza del promedio; AX.5 OLS y WLS desde mínimos cuadrados hasta covarianza de parámetros; AX.6 gradiente de la predicción inversa y sus fuentes de incertidumbre; AX.7 aproximación de Welch–Satterthwaite, grados de libertad efectivos y condiciones; AX.8 GGMR matricial en el caso validado `V_xy = 0` y estadístico de consistencia; AX.9 cancelación parcial de entradas comunes y diferencia respecto de una referencia común; AX.10 integrales de colas para falsa aceptación/rechazo; AX.11 intervalos chi-cuadrado/t para precisión y sesgo; AX.12 varianza EWMA y ARL de EWMA/CUSUM; AX.13 propagación por Monte Carlo, error de muestreo y control de ensayos.

En cada sección se dará el nivel desde el que se usa el resultado, narración en voz del instructor, acotaciones [PIZARRA], ejemplo ilustrativo numérico reproducible, advertencias críticas cuando proceda, frase de uso/remisión y referencias técnicas. No habrá prácticas ni marcadores de práctica porque prop_e §9 declara que las deducciones no se evalúan y el capítulo AX no tiene prácticas asignadas. El cierre de cada anexo señalará módulos consumidores.

### Datos, origen y cálculos previstos

- Ejemplos numéricos didácticos **simulados** y explícitamente no atribuibles a CALAIRE; no se tomarán resultados de archivos propios como si fueran datos necesarios para demostrar identidades generales.
- Se programarán scripts `curso/.venv/bin/python` bajo `curso/S4_numericos_integracion/calc/AX_*.py`, con constantes declaradas y fórmulas comentadas. Los números de ejemplos se limitarán a resultados deterministas fácilmente reproducibles: momentos de distribuciones, componentes ANOVA, matrices/soluciones de mínimos cuadrados, propagación lineal, cuantiles e integrales, ARL y simulaciones Monte Carlo.
- Se planifica un script reproducible por anexo o por conjunto estrechamente relacionado; la ejecución anotará cada salida que se use y su ubicación en el libreto. Todas las cifras presentadas tendrán correspondencia explícita con código.

### Referencias que se verificarán

Verificar texto y numerales con `pdftotext` en `docs/` antes de citarlos. Fuentes candidatas: Statistical Concepts (varianza muestral y chi-cuadrado/t); Crowder 2020 (varianza, ANOVA, mínimos cuadrados); GUM (propagación, incertidumbre tipo B, grados efectivos); GUM-S1 (Monte Carlo); ISO/TS 28037 (GGMR); Montgomery (EWMA/CUSUM, solo referencia completa sin numeral si no está en docs/); referencias de intervalos de indicadores y de riesgos de decisión solo con ubicaciones comprobadas. No se inventará numeral/página. Si no se comprueba, se citará sin numeral, y quedará como pendiente. Documentos del curso `prop_e.md`/guía solo justifican alcance e identificadores, no son respaldo técnico.

### Remisiones que deben coincidir con los libretos

La búsqueda inicial de `AX.` en `curso/S*/M*_libreto.md` muestra estas remisiones/notaciones existentes: M02 y M04 remiten a AX.1 para `n−1`/grados de libertad; M03 remite a AX.2 (varianza con dependencia/combinación lineal) y AX.3 (rectangular/triangular); M01 remite a AX.2 para entradas comunes y diferencias; M05/M06 remiten a AX.4 para cuadrados medios esperados y precisión del promedio `u²_prec(ē)=s²_entre/d+s²_r/(d·n)`; M04/M08 remiten a AX.7 para Welch–Satterthwaite y condiciones; M07 remite a AX.5 (OLS/WLS y `cov(a,b)`) y AX.6 (predicción inversa); M09 remite a AX.8 para GGMR con `V_xy=0`, consistencia chi-cuadrado, y AX.9 para patrón común; M10 remite a AX.9/AX.10 para dependencia y falsas decisiones; M06/M12 remiten a AX.11; M11 remite a AX.12; M13 remite a AX.2, AX.5, AX.9 y AX.13. Las menciones a identificadores y fórmulas conservarán esta notación. Se remitirá al uso concreto en M01–M13 según corresponda.

## Ejecución

### Contenido escrito

Se creó `AX_libreto.md` con ficha, escena narrada por cada identificador AX.1–AX.13, [PIZARRA], ejemplos ilustrativos, advertencias donde corresponde, alcance por nivel, recordatorio de uso en los módulos y referencias finales. Se incluyen pasos algebraicos para divisor y grados de libertad, propagación, distribuciones, ANOVA, OLS/WLS, predicción inversa, Welch–Satterthwaite, GGMR, diferencias, riesgos, límites de confianza, EWMA/CUSUM y Monte Carlo. Se respetó el límite `V_xy=0` y el alcance de referencia común; se excluyeron las deducciones no asignadas.

No se escribieron prácticas ni marcadores de práctica: AX es un capítulo de deducciones, y prop_e §9 declara que los anexos no se evalúan. No se crearon ejercicios, soluciones, evidencias ni rúbricas. Ejemplos numéricos: todos rotulados **simulados**, con la declaración de que no representan resultados de CALAIRE.

### Scripts y resultados

Se crearon y ejecutaron con `curso/.venv/bin/python` los siguientes scripts; todos terminaron correctamente:

| Script | Resultado numérico reproducido |
|---|---|
| `calc/AX_01.py` | media 4; suma de cuadrados 8; varianza muestral 4; s 2; ν=2; varianza con divisor n = 2,66666667 |
| `calc/AX_02.py` | varianzas individuales 0,13; covarianza 0,09; varianza de diferencia 0,08; u=0,282842712 frente a 0,509901951 suponiendo independencia |
| `calc/AX_03.py` | rectangular 0,346410162; triangular 0,244948974; resolución 0,0346410162 |
| `calc/AX_04.py` | varianza entre días 0,01; repetibilidad 0,0075; total 0,0175; u=0,132287566; sin efecto entre días u=0,0866025404 |
| `calc/AX_05.py` | matriz inversa de diseño `[[1,-1],[-1,2]]` |
| `calc/AX_06.py` | x̂=5; numerador 0,05; varianza 0,0125; u=0,111803399 |
| `calc/AX_07.py` | u² combinado 0,25; denominador 0,0029; ν_eff=21,5517241 |
| `calc/AX_08.py` | distancia 3,2; cuatro grados; chi-cuadrado reducido 0,8 |
| `calc/AX_09.py` | varianza individual 0,13; covarianza 0,09; varianza de diferencia 0,08; u=0,282842712 |
| `calc/AX_10.py` | con límite 10 y u=1: colas 0,0227501319 para θ=12/8; colas iguales a 0,5 en θ=10 |
| `calc/AX_11.py` | ν=9; chi-cuadrado 2,7003895 y 19,0227678; IC de σ (0,206350562; 0,547683055); t crítico 2,26215716; IC de media (-0,014607072; 0,414607072) |
| `calc/AX_12.py` | factor EWMA 0,111111111; desviación 0,333333333; EWMA discretizado (240 estados) ARL₀≈559,679; CUSUM unilateral discretizado (240 estados, k=0,5, h=5) ARL₀≈921,016; ARL geométrico de referencia p=0,01: 100 |
| `calc/AX_13.py` | M=10 000: error estándar teórico 0,02; M=40 000: 0,01; errores empíricos 0,0202339 y 0,00995442 |

Durante la verificación se corrigió el ejemplo de Welch–Satterthwaite: para 0,30 con 5 grados y 0,40 con 20, el denominador es 0,0029 y ν_eff=21,55, de acuerdo con `AX_07.py` (no 0,00485/12,89). Los ejemplos de AX.12 y AX.13 emplean semillas fijas para reproducibilidad.

### Referencias verificadas con `pdftotext`

| Clave y ubicación citada | Archivo | Página PDF comprobada | Comprobación |
|---|---|---:|---|
| GUM 4.3.7 y 4.4.5 | `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf` | 21 | Extracción de los apartados sobre rectangular y evaluación tipo B |
| GUM 4.4.6 | mismo PDF GUM | 22 | Extracción del apartado triangular |
| GUM 5.1.2 | mismo PDF GUM | 27 | Encabezado y explicación de incertidumbre combinada linealizada |
| GUM 5.2.2 | mismo PDF GUM | 29 | Encabezado y ecuación para entradas correlacionadas |
| GUM G.4, ecuación G.2b | mismo PDF GUM | 81 | Extracción de Welch–Satterthwaite y grados efectivos |
| GUM H.5 | mismo PDF GUM | 106–107 | Encabezado de análisis de varianza y discusión de variación entre días/dentro del día |
| ISO 28037 5.2.2 | `docs/ISO 28037.pdf` | 14 | Definiciones de incertidumbres y covarianzas |
| ISO 28037 5.5 | `docs/ISO 28037.pdf` | 15 | Incertidumbres y covarianza de parámetros de calibración |
| ISO 28037 5.6 | `docs/ISO 28037.pdf` | 16 | Validación del modelo mediante la suma cuadrática de residuos ponderados y chi-cuadrado |
| ISO 28037 10.1 | `docs/ISO 28037.pdf` | 39 | Modelo con incertidumbres y covarianzas de x e y |
| GUM-S1 5.9 | `docs/ISO_IEC Guide 98-3_2008 Suppl.1_2008 - libgen.li.pdf` | 23 | Muestreo repetido y evaluación del modelo |
| GUM-S1 5.10 | mismo PDF GUM-S1 | 24–25 | Condiciones de aplicación del método |
| GUM-S1 7.2 | mismo PDF GUM-S1 | 37 | Selección y control del número de ensayos |
| Statistical Concepts, grados de libertad `n−1` | `docs/Statistical Concepts – A First Course.pdf` | 207 | Texto que concluye los grados de libertad de la t para una media como n−1 |

### Decisiones y pendientes

- Las ubicaciones de Crowder y Statistical Concepts para ANOVA, covarianza lineal, WLS y límites chi-cuadrado/t no se fijaron como numerales; las referencias aparecen sin numeral o como ubicación por tema. **Pendiente** precisar apartados/páginas de apoyo si se requiere una bibliografía granular.
- La ubicación específica en ISO 28037 para la deducción de incertidumbre de predicción inversa no quedó verificada como cláusula/página; se cita sin numeral y queda pendiente. La ley de propagación que se aplica sí está citada a GUM 5.1.2, verificada.
- JCGM 106, ILAC-G8 y Montgomery no están disponibles en `docs/`; se citaron sin numerales como referencias externas, tal como permite guía_libreto.md §5. No se afirmó una página ni numeral no verificado.
- El texto de ISO/TS 28037 10.1 y los cálculos se circunscriben al caso didáctico `V_xy=0`; no se presenta como solución de GGMR general ni validación de software.
- Se verificó coherencia de remisiones con la búsqueda inicial: AX.1 M02/M04; AX.2 M01/M03/M08/M09/M11/M13; AX.3 M03/M08; AX.4 M05/M06; AX.5–AX.6 M07/M13; AX.7 M04/M08; AX.8 M09; AX.9 M09/M10/M13; AX.10 M10; AX.11 M06/M12; AX.12 M11; AX.13 M13. La formulación mantiene notaciones existentes (`s_r`, `s_entre`, `u²_prec(ē)`, `cov(a,b)`, `V_xy=0`, `E_n`, `D`, `ν_eff`, EWMA/CUSUM).
- No se modificó ningún archivo fuera de `curso/S4_numericos_integracion/`.

## Correcciones (revisión Haiku)

| ID | Decisión | Cambio hecho | Ubicación | Justificación |
|---|---|---|---|---|
| R01 | aplicado | Reemplazado “raíz” por cociente reducido $Q/\nu$; ejemplo expresa $3,2/4=0,8$. | `AX_libreto.md`, AX.8 | Coincide con la salida del script `AX_08.py`; no requiere recálculo. |
| R02 | aplicado | Sustituido D por $d$, definido como número de días. | `AX_libreto.md`, AX.4 | Mantiene notación guía §4; D_d representa efecto diario, no conteo de días. |
| R03 | aplicado | Quitada referencia a M6 de uso de límites de confianza. | `AX_libreto.md`, AX.11 | prop_e asigna esos indicadores a M12-I, no a M6. |
| R04 | aplicado con cambios | Eliminadas notas de verificación/páginas y numerales pendientes de narración; claves quedan sin numeral cuando no se verificó. | `AX_libreto.md`, citas AX.1, AX.4–AX.6, AX.11–AX.12 y referencias | Guía §5 manda pendientes a bitácora. Se conservaron numerales comprobados; se corrigió la nota de Montgomery para indicar que referencia externa carece de edición consignada, no como dato hablado. |
| R05 | aplicado | Quitados nombres de scripts del texto hablado. | `AX_libreto.md`, AX.3, AX.6, AX.8, AX.10–AX.11 | Trazabilidad queda en bitácora; libreto narra contenido de clase. |
| R06 | aplicado | Normalizada notación λ; aclarado umbral $h_C$ y holgura $k$. | `AX_libreto.md`, AX.12 | Evita colisión con semiamplitud h de AX.3 y con “referencia” metrológica. |
| R07 | aplicado | Aclarado que en θ=L, aceptar y rechazar tienen probabilidad 0,5. | `AX_libreto.md`, AX.10 | θ=L pertenece al lado conforme; formulación evita atribuir ambos riesgos condicionados a estado fuera/dentro. |
| R08 | aplicado | Añadido conteo $2n-(n+2)=n-2$ y caso de seis puntos. | `AX_libreto.md`, AX.8 | Explicita grados de libertad del modelo de abscisas ajustadas; evita regla automática confundible con OLS. |
| R09 | aplicado | “Primeros momentos” cambiado por “media y varianza”. | `AX_libreto.md`, AX.7 | Especifica los momentos igualados en la aproximación. |
| R10 | aplicado | “El nuevo y” cambiado por “la nueva indicación $y_0$”. | `AX_libreto.md`, AX.6 | Distingue variable medida de conjunción. |
| R11 | aplicado | Usada `cov` en ambas pizarras y añadido que GUM escribe la covarianza como $u(x_i,x_j)$. | `AX_libreto.md`, AX.2 | Notación uniforme con puente explícito a notación GUM. |
| R12 | aplicado | Unificada definición en $D_i=R_i-R$. | `AX_libreto.md`, AX.9 | Conserva símbolos empleados en el ejemplo y la referencia compartida. |
| R13 | aplicado | “Intervalación” sustituido por “construcción del intervalo”. | `AX_libreto.md`, AX.11 | Léxico correcto y natural en narración. |
| R14 | aplicado con cambios | Claves narrativas normalizadas a “Crowder 2020” y “Hahs-Vaughn y Lomax”; referencias finales precisadas con datos bibliográficos disponibles. | `AX_libreto.md`, citas y referencias | Autor/editorial de Crowder no se pudieron verificar con seguridad en los documentos disponibles; no se inventaron. Pendiente queda registrado abajo. |
| R15 | aplicado | Retirada referencia curricular prop_e del corchete técnico. | `AX_libreto.md`, AX.9 | prop_e justifica alcance, no respaldo técnico según guía §5. |
| R16 | aplicado con cambios | Divididas explicaciones extensas de grados de libertad GGMR, recurrencia EWMA y matriz ARL en unidades orales más breves. | `AX_libreto.md`, AX.8 y AX.12 | Reduce carga sintáctica sin alterar deducciones ni resultados. |
| R17 | aplicado | Añadida tabla anexo/nivel de primer uso/consumidores en ficha. | `AX_libreto.md`, ficha | Declara adaptación estructural adecuada a anexos, sin inventar niveles curriculares. |
| R18 | aplicado | Ficha remite a cada marca “Se usa desde…” y a lista de remisiones de bitácora. | `AX_libreto.md`, ficha | Describe estructura real, no una matriz inexistente ni cierres que no siempre listan consumidores. |
| R19 | rechazado | Se mantuvo referencia conjunta a guía §7 y prop_e §9, sin afirmar que §9 enumera todos los AX. | `AX_libreto.md`, ficha | No hay contradicción: guía §7 fija el catálogo AX.1–AX.13; prop_e §9 establece que anexos no se evalúan. La ficha ya aclara que contenido sigue guía §7 y que §9 solo respalda carácter no evaluable. |

### Correcciones adicionales por iniciativa propia

- Corregida la fila de tabla de remisiones en la ficha y agregada tabla compacta de consumidores por anexo; detectado al integrar R17–R18.
- Corregida notación de AX.9 en la pizarra, alineándola con $D_i=R_i-R$.
- Retiradas menciones residuales a páginas PDF dentro de citas narradas, conservando solo ubicaciones técnicas verificadas en referencias y bitácora.
- Reescritas y segmentadas frases largas de AX.8 y AX.12 para lectura oral.
- Revisada AX.8: el cociente reducido se presenta como diagnóstico, no como estimación nueva de incertidumbre. Script no cambió porque el cálculo ya era $Q/\nu=0,8$.

### Pendientes bibliográficos

- Verificar metadatos completos (autor, año, editorial) de Crowder 2020 y ubicación precisa para AX.1/AX.4/AX.5.
- Verificar edición de Montgomery y ubicación de predicción inversa en ISO 28037, si se requiere granularidad adicional.
