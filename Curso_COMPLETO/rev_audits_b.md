# Evaluación de las tres auditorías del temario (audit_a, audit_b, audit_c)

**Fecha:** 23-10-2026.
**Objeto:** `audit_a.md`, `audit_b.md` y `audit_c.md`, las tres sobre `temario_curso.md` (22-10-2026) y los casos del taller.

**Criterios de evaluación.** Son los del encargo y los acordados después:
1. El curso completo debe poder darse en B, I y A, organizado en tres perfiles acumulativos: B ejecuta con plantilla, I firma presupuestos y certificados, A es responsable técnico de la comparación con el BIPM, del R&R y de la validación de cálculos.
2. Cada tema se enseña y se practica en clase en ese nivel, o no se da y entra en el nivel siguiente. **No hay "solo lectura", "lectura breve" ni temas "para mostrar".**
3. Las prácticas son de aplicación. Las demostraciones van a anexos. No se filosofa.
4. **Las horas quedan fuera de la auditoría.**
5. La orientación es a conceptos didácticos para los operadores del SRP, no a auditar archivos.
6. Corrección técnica y coherencia interna de cada auditoría.

**Comprobaciones propias.** Para no evaluar solo por lo que cada auditoría dice de sí misma, se contrastaron sus afirmaciones clave contra `temario_curso.md` y contra el XML de los dos libros Excel. Los resultados están en la sección 6.

---

## 1. Dictamen

| | audit_a | audit_b | audit_c |
|---|---|---|---|
| **Fortaleza principal** | Rigor sobre condiciones de aplicación, alcance y estatus de los resultados | Mapa B/I/A por tema, fiel al criterio acordado y directamente utilizable | Hallazgos concretos y numéricos verificados en los libros reales; contenido detallado por módulo y nivel |
| **Debilidad principal** | Rechaza el criterio de niveles y propone horas (48/80/32 = 112 h) | No detectó los errores más graves del caso real (ABS, √576, concentraciones distintas por día) | Propone horas irreales (B en 30 h) y quita módulos enteros de B; varias prácticas contradicen sus propios hallazgos |
| **Respeta el criterio de niveles** | No | Sí, con excepciones menores | Parcialmente |
| **Respeta "sin horas"** | No | Sí | No |
| **Profundidad técnica** | Alta, cualitativa | Media-alta, precisa | Alta, cuantitativa |
| **Coherencia interna** | Alta | Alta, con algunos huecos | Media |
| **Utilidad para reescribir el temario** | Media: dice qué condiciones cumplir, no qué escribir | Alta en estructura, media en contenido | Alta en contenido, baja en estructura |

**Conclusión.** Ninguna basta sola. **audit_b es la mejor base estructural**: es la única que aplica el criterio de niveles acordado. Debe completarse con los hallazgos técnicos de C (verificados) y con los matices de A sobre condiciones de aplicación. La sección 8 propone cómo combinarlas.

---

## 2. audit_a

### 2.1 Qué propone

Tres rutas: básico operativo (48 h), intermedio (80 h) como núcleo y extensión avanzada (32 h). Diecisiete hallazgos H01–H17 clasificados como P1/P2/P3. Además: vacíos que hay que "conectar", tabla de fronteras por tarea, banco de sustituciones de prácticas, rúbricas con porcentajes, orden de implementación y una lista de comprobaciones de cierre.

### 2.2 Ventajas

1. **Matices técnicos que las otras dos no ven:**
   - **H07.** La frase del temario "las lecturas consecutivas subestiman la repetibilidad" es incorrecta. Las lecturas consecutivas sí estiman la repetibilidad, que por definición es la variación en condiciones de corto plazo. Lo que subestiman es la variación entre días, es decir, la precisión intermedia. B y C refuerzan la regla de la pseudorréplica sin corregir esta frase.
   - **H05.** Tiene en cuenta el signo del cambio de σ. Con el monitor en la escala antigua y la auditoría en la nueva, d_i ≈ −1,23 %, no +1,25 %. El temario (M12, línea 446) y C (práctica de M12) mantienen "+1,25 %" y "+1,29 %" sin indicar el signo ni la referencia.
   - **H09.** Lo que calcula el Caso B es un "grado de equivalencia" bajo un modelo didáctico, no un resultado oficial de BIPM.QM-K1. Además, `ggmr_fit` fija U_xy = 0.
   - **H12.** La ISO 5725-4 §5 sí trata el sesgo de un laboratorio. La frase del temario "las Partes 2 y 4 son para estudios interlaboratorio" es demasiado restrictiva. B se apoya en esa frase para quitar Mandel.
   - **H13.** Los supuestos de cov(a,b) OLS, de χ² con n − 2 y de la F de falta de ajuste; el cero inicial y el final no son dos niveles distintos.
   - **H14.** u(x)/x no está definida en x = 0, y la temperatura no debe corregirse dos veces: una en la ecuación y otra en σ(T).
   - **H16.** Resultado de calibración, función de uso y declaración de conformidad son tres productos distintos. La regla de decisión no es obligatoria cuando no se declara conformidad.
2. **§4.2: resultado individual, promedio y resultado futuro.** σ²_día/m + σ²_e/(mn) para el promedio, frente a una lectura futura de otro día. Es la versión rigurosa del vacío "¿s o s/√n?" de B y su mejor formulación en las tres auditorías.
3. **§4.4 y §4.5.** Proponen una convención única y = a + b·x y su inversa, prohibir la extrapolación, evitar el doble conteo y no confundir tipo A/B con aleatorio/sistemático.
4. **Evaluación y cierre.** Es la única que propone rúbricas, una lista de errores críticos que reprueban (confundir U con u, invertir una corrección, mezclar escalas, usar límites ajenos) y criterios objetivos para aceptar la revisión. Es el plan de proceso más completo.
5. **Verificación externa.** Contrasta la σ de 2025 con el informe BIPM 2024/03 y recalcula el ANOVA del R&R.
6. **Advertencia práctica correcta.** En `docs/` no hay datos de la comparación BIPM.QM-K1 propia de CALAIRE; se comprobó. Esto afecta directamente la propuesta de B (sección 3.3).

### 2.3 Desventajas

1. **Rechaza el criterio de niveles.** §1: "No corresponde prometer tres versiones técnicamente equivalentes". El básico "no se presenta como cobertura técnica completa". Es una decisión que ya había tomado el usuario y A la vuelve a discutir.
2. **Propone horas** (48 + 80 + 32 = 112 h), pese a que estaban fuera del encargo. Además, sus rutas no son acumulativas: el intermedio vuelve a empezar desde M0 y "las 48 h básicas no sustituyen las 80 h del núcleo". Es lo contrario de los perfiles acumulativos acordados.
3. **Usa formas de "solo lectura" o "para mostrar":**
   - B6: "lectura breve de un informe BIPM";
   - tabla 5.1: "contexto breve cuando haga falta" y "solo se explica por qué algunos resultados requieren análisis especializado";
   - TB: "puede explicarse por qué estas tareas requieren otro nivel";
   - §8: "podrán incluirse como consulta".

   Son justo las fórmulas que el usuario rechazó.
4. **El básico queda sin estadística aplicada.** Excluye pruebas t/F, ANOVA, la construcción del presupuesto y la regresión. El operador B "aplica una función ya aprobada" e "interpreta un presupuesto aprobado". Eso no cubre el temario con otra profundidad: lo reemplaza por un curso de operación.
5. **Mucho énfasis en gobernanza.** Varias correcciones piden fichas de aplicabilidad, autoridad de adopción, versiones y alcances (H03, H16, H17). Son pertinentes para el sistema de calidad, pero no son conceptos para enseñar en clase. El tono es de auditoría documental, con muchas negaciones ("no equivale", "no acredita", "no demuestra").
6. **Pocos números.** Casi no da ejemplos resueltos ni valores del caso real. Dice qué hay que declarar, pero rara vez cuál es el valor correcto.
7. **Omisiones importantes:**
   - Inspeccionó `Uexp` y `BD_DIAS` sin detectar `STDEV.P(ABS(...))/√576`, el error más grave del caso real.
   - No ve que en los niveles con ozono las 48 lecturas de un nivel mezclan seis concentraciones distintas.
   - No lista E_n, el método de Kragten ni el límite de detección como vacíos.
   - Habla de "pares históricos" para 1,147 frente a 308,32, pero no explica que 1,147 es un truncamiento.

### 2.4 Coherencia y calidad del plan

Es internamente coherente: sus horas, rutas, rúbricas y lista de cierre encajan entre sí. Su plan de implementación (§9) es el mejor de los tres como proceso. **Pero es coherente con un objetivo distinto del acordado.** Su arquitectura de rutas no se puede usar; sus hallazgos H05, H07, H09, H12, H13, H14 y H16 y las secciones §4.2, §4.4, §4.5 y §7 (evaluación) sí.

---

## 3. audit_b

### 3.1 Qué propone

Tres perfiles acumulativos ligados a la función en el laboratorio, una tabla módulo × nivel con lo que se enseña en cada celda, dieciséis errores E1–E16, vacíos con nivel mínimo, demostraciones que pasan a anexos, taller por nivel y faltantes para que el curso se pueda dictar.

### 3.2 Ventajas

1. **Es la única que aplica el criterio acordado.** Perfiles acumulativos definidos por función (ejecuta / firma / responsable BIPM), la regla "se enseña y se practica o entra en el nivel siguiente" y una celda B/I/A en cada módulo. La tabla de la §3 se puede pasar casi tal cual al temario.
2. **Competencia transversal de B: reconocer cuándo escalar.** Da una lista concreta de señales: pseudorréplica, ν_eff pequeño, resultado cerca del límite, atípicos, deriva, cambio de σ. Responde a la objeción de fondo de A, que en B la plantilla oculta cuándo falla el método, sin renunciar a cubrir el temario. Es la mejor idea pedagógica de las tres auditorías.
3. **Vacíos muy pertinentes para el operador**, cada uno con nivel mínimo:
   - u = U/k;
   - s o s/√n;
   - E_n;
   - Kragten como vía de B para el presupuesto;
   - límite de detección con los ceros;
   - mediana/MAD;
   - deriva como contribución a U;
   - sesgo no corregido;
   - u(s) ≈ 1/√(2(n − 1));
   - IC de una varianza (que M12 usa y M4 no enseña);
   - ISO 13528 para las comparaciones nacionales.

   Ninguna otra auditoría tiene una lista tan orientada al trabajo diario.
4. **Errores bien escogidos y precisos.** E2/E3 (régimen QAPP/TAD y criterio SRP–SRP frente a Level 2), E4 (1,06 % frente a 0,31 %), E6 (Caso B), E8 (≈ 8 para una media, ≈ 16 por grupo), E9 (t pareada dentro de un nivel), E10 (secuencia de las pruebas de atípicos), E11 (k = 2 o t según ν_eff) y E12 (sentido de dσ/dT) son correctos y vienen con su corrección.
5. **Respeta "sin horas"** y declara al principio qué cifras verificó.
6. **Conserva lo que está bien** (§9). Evita reescribir lo que funciona.
7. **Es concisa:** 26 kB frente a 55 kB de A y 68 kB de C.

### 3.3 Desventajas

1. **Se le escaparon los errores más graves del caso real.** Se comprobaron (sección 6):
   - `BD_DIAS!E8` calcula `STDEV.P` de 576 diferencias en **valor absoluto** de los 12 niveles juntos, y `E10` lo divide por √576. Ese 0,0105 nmol/mol entra como `Urepetibilidad` en `Uexp!I8`.
   - El libro R&R trabaja con "VALORES ABSOLUTOS" del error.

   Es el ejemplo real perfecto del vacío "¿s o s/√n?" que la propia B señala como "el error de presupuesto más común", y B no lo conecta con el caso.
2. **La corrección de E1 queda incompleta.** B propone usar "las 6 medias diarias" de un nivel. Pero en los niveles con ozono la concentración generada cambia de día a día: en el nivel 4, de 127,22 a 131,23 nmol/mol, verificado. Las medias diarias de las lecturas brutas siguen midiendo el generador. La variable correcta es la diferencia con signo d = y − x (C, E-04). B lo intuye en E9 para la t pareada, pero no lo convierte en regla general.
3. **Refuerza una frase errónea del temario** sobre pseudorréplica y repetibilidad, en vez de corregirla (A, H07). Toma además como cierta la frase "Partes 2 y 4 son interlaboratorio" para quitar Mandel (A, H12).
4. **No ve el signo del cambio de escala en M12** (A, H05) ni el truncamiento 1,147 → 1,25 % (C, E-02). Solo corrige el sentido de dσ/dT.
5. **Infringe su propia regla en algunos puntos:**
   - E7: "en B e I solo se menciona que existen";
   - §5.2: "una línea en B e I" para %R&R y "una línea" para PCR/PLS;
   - M13: "optativo" en I;
   - M2 en A: "repaso".

   Son menores, pero contradicen la regla que la misma auditoría enuncia en §1 y §2.
6. **Depende de datos que no están en `docs/`.** M9 en B y el Caso B en los tres niveles se apoyan en "los datos de la comparación propia de CALAIRE". No están en `docs/` (A lo advierte y se comprobó). Si no se consiguen, B se queda sin M9 en ese nivel.
7. **Carga del nivel B sin contrastar.** B incluye ANOVA de un factor, Kragten, E_n, banda de guarda, X-MR, d_i y la competencia de escalar. Las horas están fuera del encargo, pero no se comprueba si con plantilla es factible. A y C, con todos sus defectos, al menos lo pensaron.
8. **Evaluación apenas esbozada** (§8.1), sin rúbrica ni errores críticos. A es mucho más completa.

### 3.4 Coherencia y calidad del plan

Es la auditoría más coherente con el encargo, y su mapa (§2–§3) es consistente: lo que no está en B aparece en I, y lo que no está en I aparece en A. Su plan de acción es menos detallado que el de A en proceso y que el de C en contenido. Sus faltas no son de estructura sino de **profundidad en el caso real**: no abrió la plantilla hasta las fórmulas que importan.

---

## 4. audit_c

### 4.1 Qué propone

Tres niveles escalonados (30 / 50 / 66 h acumuladas), nueve errores del temario, un error del Caso B, una sección de errores en los libros Excel, vacíos, demostraciones que pasan a anexos (A1–A5), contenido detallado por módulo y por nivel con prácticas B/I/A, y una hoja de ruta para `temario_build.py`.

### 4.2 Ventajas

1. **Los hallazgos más importantes y verificables de las tres auditorías** (todos comprobados, sección 6):
   - **E-04.** En el nivel 4, las medias diarias del SRP son 127,85; 127,22; 129,62; 128,63; 131,23 y 131,22 nmol/mol. Las 48 lecturas brutas de un nivel mezclan seis concentraciones: s ≈ 1,60 frente a 0,40 nmol/mol de las diferencias. Esto invalida las prácticas de M2, M3, M4 y M6 tal como están redactadas.
   - **§2.3 B.1.** `STDEV.P(ABS(...))` sobre 576 diferencias de 12 niveles, dividida por √576, entra como `Urepetibilidad`.
   - **§2.3 A.** El R&R trabaja en valor absoluto ("VALORES ABSOLUTOS", `BASE DE DATOS!B70`), con `#REF!` en la fila 137 y con `AVERAGE(D118:D123)` en la fila 138 (comprobado).
   - **§2.3 B.3.** `Upatron = √(0,28² + (0,00292·x)²)` usa el presupuesto interno del SRP27 y omite la incertidumbre de la propia comparación del SRP 55.
2. **Otros errores del temario bien resueltos con números:**
   - E-02: 308,32 atm⁻¹ cm⁻¹ equivale a 1,1476×10⁻¹⁷; el 1,25 % sale de truncar a 1,147. Comprobado: 308,32/2,6868×10¹⁹ = 1,1475×10⁻¹⁷.
   - E-01: con la σ nueva, 0,00425·x. Comprobado.
   - E-03: falta el factor 10⁹ y la definición de f_ij.
   - E-06: a frente a δ.
   - E-08: el detalle de los criterios del SOP, del QAPP 6×6, de la TAD 2013 y de la TAD 2023 es más completo que en B.
3. **Los hallazgos se convierten en prácticas.** Comparar s de lecturas brutas con s de diferencias, corregir `Uexp`, auditar el ABS. Los errores del laboratorio pasan a ser material del curso, que es justo la forma de usar los archivos que pide el enfoque conceptual.
4. **Contenido por módulo y por nivel listo para redactar** (§5.3), con práctica B/I/A en cada módulo. Es la base de texto más avanzada de las tres para regenerar `temario_curso.md`.
5. **Vacíos bien elegidos:** paso de (x, y) a d con signo, predicción inversa completa, función continua U(x) para la CMC, E_n, n_eff con r₁.
6. **Anexos A1–A5 bien delimitados** y una hoja de ruta concreta sobre los archivos.

### 4.3 Desventajas

1. **Propone horas** (30/50/66) pese a que estaban fuera del encargo, y son irreales. Un B de 30 h con M1–M4, M7, M8, M10, M11, M12 y dos casos del taller da 2 h para M3, 2 h para M4 y 4 h para el presupuesto. Va contra la prioridad de calidad sobre horas. Además, el total avanzado (66 h) coincide con el temario actual, pero con más contenido.
2. **Quita módulos enteros de B (M5, M6, M9).** El criterio acordado es por tema, no por módulo. En B el operador puede distinguir réplica de pseudorréplica (M5) y hacer un ANOVA de un factor con plantilla (M6), como propone B.
3. **Formas "para mostrar":**
   - M9 en B: "en M1 y M10 se explica en 15 minutos qué es la comparación";
   - M6 en B: "el operador recibe la componente entre días como un término tipo A dado", es decir, usa una cifra que no aprendió a obtener;
   - M13 "opcional" en I.
4. **Prácticas que contradicen sus propios hallazgos:**
   - M4 en B: IC y t pareada "sobre las 8 réplicas de un nivel en un día". Son lecturas consecutivas, justo lo que la misma C (§3.2.1, M5) llama no independientes. La conclusión no se puede generalizar más allá de ese día.
   - M11 en I: "superponer los 6 días de F-PSMT-01" sobre la carta construida con las 10 comparaciones del NIST. Es lo que A (H10) muestra que no vigila el Level 2 de CALAIRE.
   - M12: repite "+1,29 %" sin indicar signo ni referencia (A, H05).
   - M4 en A: Cochran "para demostrar la heterocedasticidad" de los 12 niveles. La heterocedasticidad entre 0 y 455 nmol/mol se espera por diseño: la prueba no aporta y la palabra "demostrar" va contra el enfoque del curso.
   - La autocorrelación queda solo en A, aunque es la base del problema de pseudorréplica que C quiere enseñar desde B.
5. **Afirmación incorrecta sobre la CMC.** Según C (§2.3 B.4), la plantilla no aplica `max(U, CMC)`. Se comprobó lo contrario: `Uexp!P8 = IF(O8<=N8,"OK","ERROR")` y `Q8 = IF(P8="OK",N8,O8)`. Es decir, Q8 toma en cada punto el mayor entre la U calculada (N8) y la curva cúbica (O8). El desplazamiento de `EcuOffset`/`U22` es un paso **adicional**, no un sustituto. A lo describe bien.
6. **Orientación a auditar archivos.** El usuario dijo que le interesan los conceptos, no los errores de los archivos. La §2.3 y varias prácticas ("auditar BD_DIAS", "corregir Uexp") ponen la plantilla del laboratorio en el centro del curso. Tiene valor didáctico, pero también un riesgo: el curso se convierte en una revisión del sistema de calidad. Además, los errores de una plantilla en uso no deberían esperar a la clase (sección 7).
7. **Supuestos sin respaldo.** Da por hecha la "CMC acreditada ONAC" y la mantiene Mandel h/k en M6 I sin aclarar su utilidad en un solo laboratorio.
8. **Forma.** Mayúsculas en todos los títulos, negrita en exceso, enlaces `file://` absolutos y párrafos muy largos. Es la menos legible de las tres.

### 4.4 Coherencia y calidad del plan

Es fuerte en el diagnóstico y en el contenido, más débil en la arquitectura. Las horas, la exclusión de módulos en B y varias prácticas chocan con sus propios hallazgos o con el criterio acordado. Es la auditoría con **más hallazgos nuevos verificados**, pero la que más hay que corregir antes de usarla.

---

## 5. Comparación por tema

| Tema | A | B | C | Mejor tratamiento |
|---|---|---|---|---|
| Arquitectura de niveles | Rutas separadas, no acumulativas | Perfiles acumulativos por tema | Niveles acumulativos por módulo | **B** |
| Horas | 112 h | No las trata (correcto) | 30/50/66 h | **B** |
| Pseudorréplica / unidad de réplica | Corrige la frase del temario (H07) | Regla "día, n = 6" (E1) | d con signo; 8 lecturas en B (contradictorio) | **B + A H07 + C E-04** |
| Variable de análisis entre días | — | Implícita en E9 | d = y − x con signo (E-04) | **C** |
| ABS y √576 en el certificado | No lo detecta | No lo detecta | Lo detecta (verificado) | **C** |
| R&R en valor absoluto | No | No | Sí (verificado) | **C** |
| σ: 1,06 % frente a 0,31 % | H04, con advertencia de no mezclar presupuestos | E4 | E-01 con 0,00425·x | **C con la advertencia de A** |
| σ: 1,25 % frente a 1,29 % | "Pares históricos" | — | Truncamiento (E-02) | **C** |
| Signo del cambio de escala en la red | H05 | — | Lo repite sin signo | **A** |
| QAPP / TAD / SOP | Ficha de aplicabilidad (H03) | E2, E3 y decidir una vez en M10 | Tabla completa de criterios (E-08) | **B (decisión) + C (tabla)** |
| t pareada | H06 | E9: dentro de un nivel, 6 días | E-07: dentro de un nivel, 8 lecturas | **B** |
| Tamaño de muestra | Pide especificarlo | ≈ 8 / ≈ 16 | ≈ 8 + 2 / 16 | **B o C** |
| Atípicos en M2 | H15 | E10 | §3.1 | Empate B/C |
| `max(U, CMC)` | Correcto (Q8) | — | Incorrecto | **A** |
| Corrección y función de uso | §4.4, H16 | E13 (convención) | E-09 | **A** |
| Promedio frente a resultado futuro | §4.2 | "s o s/√n" | — | **A + B** |
| E_n, Kragten, LOD, u(s), IC de varianza | — | Sí | Solo E_n | **B** |
| Regresión: supuestos | H13 | E1 (error puro con medias diarias) | Predicción inversa completa | **A + C** |
| Estatus del Caso B | H08, H09 | E6 | §2.2 | **A** |
| Datos propios BIPM | Advierte que no existen | Depende de ellos | Usa el caso actual | **A** |
| Demostraciones → anexos | §6, §8 | §6 (diez casos) | §4, §6 (A1–A5) | Empate B/C |
| Evaluación | Rúbricas y errores críticos | Esbozo | — | **A** |
| Contenido redactable por módulo | — | Tabla resumida | §5.3 detallado | **C** |
| Orientación a conceptos | Media (gobernanza) | Alta | Media (archivos) | **B** |

---

## 6. Comprobaciones hechas en esta evaluación

| Afirmación | Auditoría | Resultado |
|---|---|---|
| `BD_DIAS!F15` = `ABS(C15−E15)` (y así hasta la fila 110, en seis bloques de columnas) | C | **Cierto** |
| `BD_DIAS!E8` = `STDEV.P(...)` sobre 576 valores = 0,2525 | C | **Cierto** |
| `BD_DIAS!E10` = `E8/SQRT(E4)`, con E4 = 576, da 0,0105; `Uexp!I8 = BD_DIAS!$E$10` | C | **Cierto** |
| `Uexp!J8` = `SQRT(J6² + (0,00292·D8)²)` = 0,28 | C | **Cierto** |
| `Uexp!G8` = `E8 − $D$20` | C | Cierta la fórmula; no se verificó a qué magnitud corresponde cada columna |
| La plantilla no aplica `max(U, CMC)` | C | **Falso.** `P8 = IF(O8<=N8,"OK","ERROR")`, `Q8 = IF(P8="OK",N8,O8)`: es un máximo punto por punto. `U22 = Q6+T10+S6` añade el desplazamiento |
| Medias diarias del SRP en el nivel 4: 127,85 … 131,22 | C | **Cierto** (127,85; 127,22; 129,62; 128,63; 131,23; 131,22) |
| R&R `BASE DE DATOS!B70` = "VALORES ABSOLUTOS"; `D137` = `#REF!`; `D138 = AVERAGE(D118:D123)` | C | **Cierto** |
| 308,32 atm⁻¹ cm⁻¹ ↔ 1,1475×10⁻¹⁷ cm² | C | **Cierto** (con la constante de Loschmidt 2,6868×10¹⁹ cm⁻³) |
| √(0,00292² + 0,00309²) = 0,00425 | C | **Cierto** |
| El temario dice "subestiman la repetibilidad" (línea 242) | A | **Cierto**: la frase está en M6 |
| El temario dice "Partes 2 y 4 son para estudios interlaboratorio" (línea 257) | A | **Cierto** |
| M12 del temario: "sesgo de +1,25 %" (línea 446) | A | **Cierto**: la frase no dice qué σ usa cada equipo |
| No hay datos de la comparación BIPM.QM-K1 propia en `docs/` | A | **Cierto** |
| La tabla de módulos asigna B solo a M1–M2 y B–I a M3 | C | **Cierto** (líneas 27–43) |

---

## 7. Un punto fuera del curso

Los hallazgos de C sobre `BD_DIAS` (ABS, STDEV.P y √576) afectan a la `Urepetibilidad` de un certificado de calibración real del Level 2. El efecto es una subestimación de la repetibilidad. Su efecto final sobre la U reportada puede quedar tapado por la regla del máximo con la CMC: en `Uexp!P8` la U calculada no alcanza a la curva. Aun así, es un asunto del sistema de calidad del laboratorio, independiente del curso. Conviene llevarlo a quien sea responsable de la plantilla F-PSMT-01 y no esperar a usarlo como ejercicio.

---

## 8. Recomendación: cómo combinarlas

**Base: audit_b**, con su arquitectura de perfiles (§2), su mapa por nivel (§3), sus vacíos (§5.1) y su competencia de escalar.

**Incorporar de audit_c:**
1. E-04 como regla del curso. En los niveles con ozono, la variable entre días es d = y − x con signo, y la unidad de réplica es el día. Esto completa E1 de B.
2. E-01 (0,00425·x), E-02 (truncamiento), E-03 (10⁹ y f_ij), E-06 (a frente a δ) y la tabla de criterios de E-08.
3. Como prácticas, no como auditoría:
   - en B, s de lecturas brutas frente a s de diferencias;
   - en B o I, "¿s o s/√n?" con el caso real de √576;
   - en I, ANOVA de d por nivel;
   - en I, ABS en el R&R: por qué el valor absoluto oculta sesgos de signo contrario.
4. Predicción inversa completa y función continua U(x) para la CMC (A).
5. El contenido de §5.3 como borrador de redacción, pero ajustado al mapa de B. M5, M6 y M9 recuperan su celda B.

**Incorporar de audit_a:**
1. H07: corregir la frase "subestiman la repetibilidad".
2. H05: signo y referencia del cambio de escala en M1 y M12.
3. H09: rotular el resultado del Caso B como didáctico.
4. H12: matizar la ISO 5725-4 y revisar si se quita Mandel.
5. H13 y H14: supuestos de regresión, x = 0 y unidades.
6. H16 y §4.4: los tres productos (resultado, función de uso, conformidad) y la convención y = a + b·x.
7. §4.2: incertidumbre del promedio frente a la del resultado futuro, como versión I/A del vacío "¿s o s/√n?" de B.
8. §7, evaluación: rúbricas y la lista de errores críticos, adaptadas a los perfiles B/I/A.

**Descartar:**
- las horas de A y de C;
- las rutas no acumulativas de A;
- la exclusión de módulos enteros en C;
- toda forma de "lectura", "15 minutos", "una línea", "solo se menciona" u "opcional" en las tres, incluidas las de B.

**Pendiente de decisión del usuario:**
1. Si se consiguen los datos de la comparación BIPM.QM-K1 propia. Sin ellos, M9 en B y el Caso B deben trabajar con el caso actual, rotulado como didáctico.
2. Qué régimen de criterios sigue CALAIRE para el Level 2: QAPP 6×6, TAD 2023 o procedimiento del INM. Las tres auditorías coinciden en que hay que fijarlo una sola vez.
