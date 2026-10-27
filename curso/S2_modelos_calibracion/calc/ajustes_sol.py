"""Registro histórico de ajustes interrumpidos; NO ejecutar sobre los libretos.

Las decisiones vigentes se registran en S2_revision_sol.md. Este archivo conserva
el texto histórico para auditoría, no forma parte de los cálculos reproducibles.
"""
raise SystemExit("Auxiliar histórico deshabilitado: consultar S2_revision_sol.md; no se modificó ningún libreto.")
from pathlib import Path
import re

BASE = Path(__file__).resolve().parents[1]

def paragraph(text, start, replacement):
    begin = text.index(start)
    end = text.find('\n\n', begin)
    if end < 0:
        end = len(text)
    return text[:begin] + replacement + text[end:]

p = BASE / 'M07_libreto.md'
s = p.read_text()
s = paragraph(s, 'Revisemos ahora si las discrepancias', 'El diagnóstico ponderado y chi-cuadrado con incertidumbres declaradas se desarrolla en A2. Aquí aprendemos a elegir los pesos y a revisar residuos sin importar automáticamente criterios de otro procedimiento. El WLS de I conserva el eje de referencia fijo [Crowder 2020 §10.2.3].')
s = s.replace('También interpretaremos la inferencia de una correlación, sin confundirla con una validación de calibración. ', '')
s = s.replace('y las pruebas de pendiente y falta de ajuste', 'y la falta de ajuste')
s = s.replace('pendiente y falta de ajuste con réplicas verdaderas', 'falta de ajuste con réplicas verdaderas')
s = s.replace('### Escena I4. Pendiente, error puro y falta de ajuste', '### Escena I4. Error puro y falta de ajuste')
s = s.replace('[Otto; Brereton; prop_e §5, M7-I]', '[Otto §6.1, tabla 6.1, PDF p. 222]')
s = s.replace('[prop_e §5, M7-I; archivo propio F-PSMT-01, sin numeral externo]', '[Otto §6.1, tabla 6.1; F-PSMT-01, fuente propia del diseño]')
s = s.replace('La solución matricial se expresa como `β̂ = (XᵀX)⁻¹Xᵀy`, donde cada fila de `X` contiene un uno y el correspondiente valor `xᵢ`, y `β̂` contiene el intercepto y la pendiente. ', '')
s = s.replace('; $\\hat\\beta=(X^T X)^{-1}X^T y$', '')
s = s.replace('`eᵣ = y − ŷ`', '`r = y − ŷ`').replace('$s_res^2', '$s_{\\mathrm{res}}^2')
s = s.replace('Lomax, R. G.; Hahs-Vaughn, D. L.', 'Hahs-Vaughn, D. L.; Lomax, R. G.')
s = s.replace('(sin numeral; ubicación específica pendiente de verificación)', '(§6.1, tabla 6.1, PDF p. 222) ', 1)
s = s.replace('(sin numeral; ubicación específica pendiente de verificación)', '(bibliografía de diseño; no se usa como fuente de falta de ajuste)')
s = s.replace('| Anexos | AX.5:', '| Anexos | AX.7: cobertura aproximada por bloques independientes; AX.8: formulación matricial GGMR. AX.5:')
s = s.replace('GGMR según la terminología de este curso, estima', 'GGMR según la terminología de este curso, estima')
s = s.replace('Para cada `u(xᵢ) = 0,25 nmol/mol` añadimos', 'A una componente independiente de cada referencia de `0,25 nmol/mol` añadimos')
s = s.replace('Para este capítulo la herramienta autorizada trabaja con `V_xy = 0`', 'El cálculo docente de este capítulo trabaja con `V_xy = 0`; no equivale a una herramienta operativa autorizada')
s = s.replace('para el alcance validado del ejemplo', 'para el alcance restringido del ejemplo')
s = s.replace('alcance validado de la herramienta que usamos', 'alcance restringido de la herramienta docente que usamos')
s = s.replace('aproximadamente `3,48 × 10⁻²⁹`', 'del orden de $10^{-29}$ (el último dígito depende de la plataforma)')
s = s.replace('no contiene variación coherente', 'no contienen variación coherente')
s = s.replace('y no contienen', 'y no contienen')
# prop_e se mantiene solo en referencias internas de alcance; nunca como fuente técnica.
s = re.sub(r'\[prop_e[^\]]*; (Crowder 2020[^\]]*|ISO 28037[^\]]*)\]', r'[\1]', s)
s = re.sub(r'; prop_e §[^\]]*(?=\])', '', s)
s = s.replace('[prop_e §5, M7]', '[Crowder 2020 §10.4]')
s = s.replace('[prop_e §3; ISO 28037 §5.7]', '[ISO 28037 §§5.7, 11.1]')
s = s.replace('[prop_e §5, M7–M8]', '[GUM 4.1–5.2]')
s = s.replace('**AX.5 y AX.6**', '**AX.5, AX.6, AX.7 y AX.8**')
s += '\n- **GUM** — JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, G.4. Archivo GUM en `docs/`, identificado en M08.\n- **F-PSMT-01** — CALAIRE, certificado G1 S/N 59756-324, archivo propio `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm`.\n'
p.write_text(s)

p = BASE / 'M05_libreto.md'
s = p.read_text()
s = paragraph(s, 'Los documentos de referencia muestran', 'Los documentos de referencia muestran que no hay una única secuencia que sirva para todas las preguntas. El SRP QAPP describe ciclos de comparación para el objetivo que define [SRP QAPP §6.2.1]. El SRP SOP establece sus propias condiciones y el mínimo de ciclos de su verificación [SRP SOP §§9.7.19–9.7.20]. No elegimos una cifra de un documento para presentarla como regla universal. El protocolo y la organización de BIPM.QM-K1 quedan fuera de este capítulo y del curso.')
s = paragraph(s, 'En la revisión de los diseños reales', 'Los ciclos de SRP QAPP y SRP SOP responden a sus propios procesos de verificación [SRP QAPP §6.2.1; SRP SOP §§9.7.19–9.7.20]. No son recetas universales ni sustituyen la pregunta estadística del diseño local. Esta precaución ya se explicó en B4; aquí la aplicamos al decidir qué componentes se podrán estimar.')
s = s.replace('BIPM.QM-K1, SRP QAPP', 'SRP QAPP').replace('documentos SRP y protocolo BIPM.QM-K1', 'documentos SRP')
s = re.sub(r'^- BIPM\. .*\n', '', s, flags=re.M)
s = s.replace('Cambio de pendiente', 'Cambio de pendiente')
s = s.replace('Si cada analista calibra el Level 2 en campañas diferentes y no hay campañas compartidas, campaña y analista quedan confundidos: cada campaña pertenece a un solo analista y no hay comparación común que los separe.', 'Si hay una sola campaña propia por analista, sus efectos están confundidos. Si hay varias campañas independientes por analista, campaña está anidada en analista: bajo un modelo aleatorio adecuado sí pueden separarse componentes de campaña y analista; lo que no puede estimarse es una interacción cruzada analista × campaña [ISO 5725-3 §§9.3–9.5].')
s = s.replace('Si el diseño solo contiene analistas diferentes en campañas distintas, no debemos prometer separar analista de campaña.', 'Si hay una sola campaña por analista, no podemos separar analista de campaña; con varias campañas por analista cabe un modelo anidado, no uno cruzado.')
s = s.replace('La **robustez** pregunta', 'La **robustez** pregunta')
needle = 'La palabra **escalonado** no equivale'
insert = 'Hagamos visible un patrón publicado, sin aplicarlo como estudio interlaboratorio. Dentro de un laboratorio, un diseño totalmente anidado con dos operadores, dos días propios por operador y dos resultados por día exige ocho resultados. En el escalonado de ISO 5725-3, el operador uno obtiene dos resultados bajo repetibilidad el día uno y un resultado el día dos; el operador dos obtiene un resultado el día tres. Son cuatro resultados por laboratorio: primero cambia solo día y después día y operador. La replicación del patrón aporta información a distintas escalas, pero no permite inventar un factorial completo ni una interacción cruzada. La norma cuenta laboratorio, operador, día y residual en su jerarquía. La economía implica mayor incertidumbre y un análisis más complejo [ISO 5725-3 §9.5, figura 1 y §9.8].\n\n'
s = s.replace(needle, insert + needle)
p.write_text(s)

p = BASE / 'M08_libreto.md'
s = p.read_text()
s = s.replace('Ocho lecturas de un mismo día dan una media', 'En este modelo simulado, la media de ocho lecturas de un mismo día es')
s = s.replace('y una desviación de repetibilidad $s_r=0{,}24\\ \\mathrm{nmol/mol}$.', 'y se entrega una estimación de repetibilidad $s_r=0{,}24\\ \\mathrm{nmol/mol}$ del proceso antes de cuantizar. Se obtuvo por una evaluación independiente de mayor resolución: no es la desviación de estas mismas lecturas redondeadas.')
s = s.replace('Si la cuantización de cada lectura se trata como rectangular,', 'Suponemos aquí errores de cuantización rectangulares, independientes entre lecturas e independientes de esa repetibilidad. Si se justifican esas condiciones,')
s = s.replace('Para el promedio de ocho contribuciones independientes,', 'Para el promedio de ocho errores de cuantización independientes,')
s = s.replace('La combinación de ambas partes de la entrada $y$', 'Si la repetibilidad se hubiera estimado con los datos ya redondeados, no se sumaría automáticamente otra vez la cuantización. Con las dos fuentes separadas de este modelo, la combinación de ambas partes de la entrada $y$')
s = s.replace('En nuestro ejemplo inicial solo como ilustración, con $k=2$,', 'En el ejemplo se suministra además una aproximación normal para la salida: las contribuciones dominantes de intercepto y pendiente tienen grados de libertad grandes, son independientes y la linealización es adecuada. La pequeña contribución tipo A tiene siete grados de libertad; I2 comprobará el factor aproximado. Bajo esta ficha, $k=2$ representa aproximadamente el 95 %, no exactamente. Con ese factor,')
s = s.replace('[guia_libreto §6; prop_e §5, M8-B]', '[GUM 4.2; GUM H.5; F-PSMT-01, fuente propia del diseño]')
s = s.replace('doce puntos, ocho lecturas por punto y seis días', 'doce puntos (diez de concentración y dos de cero), ocho lecturas por punto y día, y seis días')
s = s.replace('[BIPM KCDB]', '[CIPM MRA-G-13]')
s = s.replace('[BIPM, KCDB, Calibration and Measurement Capabilities (CMC), sin numeral; no disponible en docs/]', '[CIPM MRA-G-13, documento sin numeral; no disponible en docs/]')
s = s.replace('- **BIPM KCDB.** BIPM, *Key Comparison Database (KCDB): Calibration and Measurement Capabilities (CMCs)*, recurso en línea (no disponible en `docs/`; sin numeral).', '- **CIPM MRA-G-13.** BIPM, *Calibration and measurement capabilities in the context of the CIPM MRA*, versión 1.1, 2021 (no disponible en `docs/`; sin numeral; definición institucional, no contenido sobre KCDB).')
s = s.replace('Si reportamos un valor corregido', 'Si reportamos un valor corregido')
s = s.replace('[prop_e §5, M8; calc/M08_ejemplos.py]', '[GUM 6.2–6.3; calc/M08_ejemplos.py, construcción matemática simulada]')
s = s.replace('[prop_e §5, M8; GUM 6.2–6.3]', '[GUM 6.2–6.3; CIPM MRA-G-13]')
s = s.replace('En esta escena no vamos a decidir conformidad con una regla externa;', 'El máximo puntual es una construcción docente del ejemplo, no una regla de decisión derivada de la GUM ni una aprobación de CMC;')
s = s.replace('[prop_e §5, M8; Crowder 2020 §7.5–7.7]', '[Crowder 2020 §7.5–7.7; CIPM MRA-G-13]')
s = s.replace('u_c^2(y)=', 'u_c^2(Y)=')
s = s.replace('cᵢ=∂f/∂xᵢ', 'c_i=\\partial f/\\partial x_i')
s = s.replace('Las dos primeras son aproximadamente adimensionales', 'Las dos primeras son exactamente adimensionales')
s = s.replace('[prop_e §5, M8; GUM G.3–G.4]', '[GUM G.3–G.4]')
needle='No confundamos una comparación puntual'
insert='Para verificar todo el intervalo simulado de cero a quinientos, buscamos los cruces de ambas funciones, no solo cuatro puntos. Al igualar sus cuadrados resulta $0{,}000128x^2-0{,}0064x-0{,}3264=0$. Se lee: cero coma cero cero cero uno dos ocho por equis al cuadrado, menos cero coma cero cero seis cuatro por equis, menos cero coma tres dos seis cuatro, igual a cero. La única raíz dentro del intervalo es $x\\approx81{,}36\\ \\mathrm{nmol/mol}$. Como las dos funciones originales son positivas, el signo de ese polinomio determina cuál es mayor: CMC domina desde cero hasta ese cruce; $U$ domina después, hasta quinientos. Esto verifica la envolvente en todo el intervalo para estas funciones particulares; no impone una forma funcional a presupuestos reales [calc/M08_ejemplos.py, álgebra del ejemplo simulado].\n\n'
s=s.replace(needle,insert+needle)
s += '\n- **F-PSMT-01.** CALAIRE, certificado G1 S/N 59756-324, archivo propio `docs/F-PSMT-01 Certificado de Calibracion_G1-sn59756-324_TBH.xlsm` (solo estructura).\n'
p.write_text(s)
