# M13 — revisión de la práctica A (Haiku 5.5)

Fecha: 2026-10-27
Revisado: `curso/S4_numericos_integracion/M13_libreto.md` (bloque `[PRÁCTICA] A`, líneas 216–244, y escena A1, líneas 25–59, por su relación con la práctica); `curso/S4_numericos_integracion/calc/M13_practicas_luna.py`; `curso/logs/M13_practicas_luna.md`.
Verificación: ejecución de `curso/.venv/bin/python curso/S4_numericos_integracion/calc/M13_practicas_luna.py` (rc=0) y de `calc/M13_ejemplos.py` (rc=0). Versiones: statsmodels 0.15.0, scipy 1.18.1, numpy 2.5.4.
No se auditaron referencias bibliográficas (lo hace el otro supervisor). No se modificó ningún archivo distinto de este.

## Hallazgos

### H-01 — Severidad alta — La conclusión «linealización favorable» depende del redondeo de u

- **Ubicación:** `M13_libreto.md` línea 51 (escena A1: «Expresamos la incertidumbre como 1,0 nmol/mol, con dos cifras significativas…») frente a las líneas 43 y 234 (cálculos con u = 1,041437); `M13_practicas_luna.py` líneas 29–34 (usa u sin redondear).
- **Evidencia:** el texto dice que la incertidumbre se toma como 1,0 nmol/mol, pero las diferencias de extremos (0,0117 y 0,0006 nmol/mol) se calculan con 1,041437. Si se usa u = 1,0 como dice el texto, el intervalo lineal queda en [416,8025; 420,7224] nmol/mol y las diferencias son 0,0695 y 0,0806 nmol/mol, ambas mayores que δ = 0,05. Con esa lectura la conclusión «favorable» se invierte. Verificado por ejecución.
- **Corrección propuesta:** elegir una regla y escribirla. Recomiendo conservar u = 1,041437 para la comparación y redactar la frase así: «la incertidumbre se reporta con dos cifras significativas como 1,0 nmol/mol; la comparación de extremos se hace con el valor sin redondear, 1,041437 nmol/mol, porque el redondeo cambia la conclusión». Alternativamente, comparar con 1,0 y declarar que la linealización no supera δ, lo que obliga a escalar o usar Monte Carlo en este caso. Corregir también la solución del apartado 1 (línea 234) para que diga qué valor se usó.

### H-02 — Severidad media — El cálculo independiente pedido en el apartado 2 no se hace ni se reporta

- **Ubicación:** `M13_libreto.md` línea 228 («compare una salida seleccionada con un cálculo independiente») y línea 236 (solución); `M13_practicas_luna.py` líneas 53–60 (únicas comprobaciones: forma, simetría y autovalores).
- **Evidencia:** la matriz 5×5 se calcula con la misma jacobiana analítica que la produce. Las comprobaciones son de forma y de admisibilidad, no de exactitud. El único contraste numérico de la escena A2 (u(c₂₅₀) = 0,0440 con covarianza OLS clásica) no es un cálculo independiente de la matriz de días: ignora los bloques y responde a otra pregunta.
- **Corrección propuesta:** añadir al script un contraste con diferencias finitas centradas de (a, b) → (c₈₀, c₂₅₀, c₄₂₀) sobre las covarianzas del promedio diario, o una propagación Monte Carlo de la matriz de parámetros, y reportar la discrepancia máxima relativa frente a la analítica. Esa cifra debe aparecer en la solución del apartado 2. Si se mantiene la comprobación actual, la solución debe decir explícitamente que no es un cálculo independiente.

### H-03 — Severidad media — El intervalo bootstrap de la solución no lo reproduce el script de la práctica

- **Ubicación:** `M13_libreto.md` línea 238 (solución: pendiente hasta «1,00159362») y línea 124 (escena A3); `M13_practicas_luna.py` línea 66 (`bootstrap_rng = np.random.default_rng(ejemplos.SEED)`).
- **Evidencia:** al ejecutar el script de la práctica, el límite superior de la pendiente es 1,0015936019, es decir, 1,00159360 con ocho decimales. El valor 1,00159362 proviene de `M13_ejemplos.py`, que continúa el mismo generador tras los 400 000 ensayos Monte Carlo. Verifiqué que, si el bootstrap continúa ese flujo, se obtiene 1,00159362. Los otros límites coinciden. La bitácora `curso/logs/M13_practicas_luna.md` (línea 21) registra 1,001593602, lo que confirma la discrepancia.
- **Corrección propuesta:** en el script de la práctica, reemplazar `bootstrap_rng = np.random.default_rng(ejemplos.SEED)` por el mismo generador `rng` ya usado en la simulación, de modo que el resultado coincida con `M13_ejemplos.py`. Alternativamente, cambiar la cifra de la solución a 1,00159360 y actualizarla en la escena A3 para que el lector no vea dos valores distintos.

### H-04 — Severidad media — Faltan señales de escalamiento en los apartados 1 y 2

- **Ubicación:** `M13_libreto.md` líneas 226–242. El enunciado (línea 232) pide «para cada apartado una señal concreta para detenerse y escalar». La solución da señal explícita solo para el bootstrap (línea 238) y para Huber (línea 240).
- **Evidencia:** la solución del apartado 1 (línea 234) concluye que la linealización basta, pero no indica cuándo debe detenerse. La del apartado 2 (línea 236) no incluye señal alguna.
- **Corrección propuesta:** añadir una frase de señal a cada solución. Para el apartado 1: «Señal: si alguna diferencia de extremos supera δ, o si la media o la desviación Monte Carlo se apartan de la lineal más allá de la precisión numérica, o si una entrada no tiene distribución justificada, detener y escalar». Para el apartado 2: «Señal: si la matriz no es semidefinida positiva dentro de tolerancia, si los días no son intercambiables para la pregunta, o si se pide reportar una diferencia entre salidas sin usar la covarianza, detener y escalar».

### H-05 — Severidad baja — Falta el criterio por apartado exigido en prop_e

- **Ubicación:** `M13_libreto.md` línea 244 (un único «Criterio de logro» para los cuatro apartados).
- **Evidencia:** `prop_e.md`, sección M13, establece que «cada apartado tiene resultado, supuestos y criterio en la rúbrica». El bloque da un solo criterio agregado.
- **Corrección propuesta:** desglosar el criterio en cuatro líneas, una por apartado, cada una con resultado, supuesto y criterio de verificación.

### H-06 — Severidad baja — Los 36 datos del apartado 2 no se pueden consultar sin leer el código

- **Ubicación:** `M13_libreto.md` línea 222 («Usen los valores de las 36 observaciones del script»); `M13_practicas_luna.py` líneas 37–49 (la matriz se define pero no se imprime ni se exporta).
- **Evidencia:** el script imprime coeficientes, inversas, covarianzas y resultados del bootstrap, pero no las 36 observaciones. El enunciado remite a «los valores del script» sin que el estudiante pueda obtenerlos sin copiar código. El apartado 4 sí da sus datos en el texto (línea 224).
- **Corrección propuesta:** imprimir la matriz 6×6 de `y` (o escribirla en un CSV dentro de `calc/`), e indicar en el enunciado la salida donde aparecen.

### H-07 — Severidad baja — Duplicación de datos entre el script de la práctica y `M13_ejemplos.py`

- **Ubicación:** `M13_practicas_luna.py` líneas 37–46 (`levels`, `offsets`, `point_noise`) y 77–78 (`x_robust`, `y_clean`); duplican los literales de `M13_ejemplos.py` líneas 76–87 y 127–129.
- **Evidencia:** hoy coinciden (verificado: el resultado de la práctica reproduce el de los ejemplos en todas las cifras citadas, salvo H-03). Pero dos copias pueden divergir sin aviso.
- **Corrección propuesta:** mover esos literales a constantes de nivel de módulo en `M13_ejemplos.py` e importarlos desde la práctica. Es un cambio de mantenimiento; no afecta a los números actuales.

## Lo verificado sin hallazgos

- **Números de la práctica (ejecución):** estimación 418,762475; u lineal 1,041437; media MC 418,763825; desviación MC 1,040327; IC MC [416,733012; 420,803052]; diferencias de extremos 0,011715 y 0,000601 (ambas ≤ 0,05 con u sin redondear); covarianza 5×5 simétrica con autovalores no negativos; a = 0,65184834, b = 1,00151145; u(a), u(b), u(c₈₀), u(c₂₅₀), u(c₄₂₀) = 0,107231; 0,0000461; 0,107113; 0,107624; 0,108696; cov(a,b) = −2,5383·10⁻⁸; cov(c₈₀, c₂₅₀) = 0,01149744; correlaciones 0,9974, 0,9974 y 0,9896 entre correcciones.
- **Escena A2:** el promedio de las rectas diarias coincide con el OLS agrupado (verificado: ambos dan a = 0,65184834 y b = 1,00151145). La correlación OLS clásica (−0,8559) y u(c₂₅₀) clásica (0,0440) coinciden con el texto.
- **Bootstrap:** 462 multiconjuntos verificado; semiancho percentil / 1,96 = 0,0976 para la corrección y 4,13·10⁻⁵ para la pendiente, coherentes con el texto. Límites de la corrección a 250 nmol/mol reproducidos (−1,21228848; −0,82985981).
- **Huber/OLS (apartado 4):** OLS limpio (0,49971429; 1,00201429), OLS alterado (−1,10028571; 1,01534762), Huber (0,38975488; 1,00293061), escala MAD 0,20499252, umbral 0,27571494, peso 0,03568701, predicciones 201,969238 y 200,975878, residuos 4,621667 y 7,725918. Errores H1 0,1668 y 0,000738; u(b) de OLS 0,00764. Tabla de sensibilidad (c = 0,20; 0,35; 1,00; 2,00; 5,00) reproducida con `M13_ejemplos.py`. Se conserva el peso del punto alterado; no se elimina ningún dato.
- **Alcance:** la práctica es solo de nivel A, como exige `prop_e.md` para M13. Cubre los cuatro contenidos declarados (Monte Carlo, salidas múltiples, bootstrap por bloques y Huber frente a OLS).
- **Origen de los datos:** los cuatro conjuntos se declaran simulados, con semilla y regla reproducible. Ningún valor se atribuye a CALAIRE. La alteración del apartado 4 se declara deliberada y no se presenta como dato de laboratorio.
- **Unidades y formato:** nmol/mol en todos los resultados; coma decimal en el bloque de práctica (búsqueda de puntos decimales sin resultados).
- **Aplicación ozono/SRP:** el caso se presenta como calibración de ozono en nmol/mol, sin afirmar datos de la campaña ni del SRP 55.

## Observaciones fuera del bloque de práctica

- La escena A4 (línea 184) y la escena A3 (línea 126) indican diapositivas con gráficas que no existen en `calc/`. Son texto previo al bloque de práctica y `prop_e.md` no exige gráficos en M13; el resumen de la bitácora dice que no se requiere visualización. Conviene que el autor decida si se produce la gráfica o se cambia la indicación a una tabla. No lo cuento como hallazgo de la práctica.
