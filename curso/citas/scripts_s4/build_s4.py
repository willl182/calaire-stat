import re
import pathlib

ROOT = pathlib.Path('/home/w421/w421/calaire-stat')
CITES = re.compile(r'\[([^\[\]]*(?:GUM|ISO|Efron|Huber|Montgomery|statsmodels|BIPM|CFR|Crowder|Hahs|JCGM|ILAC|Prop_e|VIM)[^\[\]]*)\]', re.I)
FILES = [ROOT / 'curso/S4_numericos_integracion/M13_libreto.md', ROOT / 'curso/S4_numericos_integracion/AX_libreto.md']


def evidence(key, filename, line):
    if 'GUM-S1' in key:
        facts = {
            '5.4': '§5.4 es «Implementations of the propagation of distributions» (índice, p. impresa 10).',
            '5.9': '§5.9 «Monte Carlo approach to the propagation and summarizing stages» (índice, p. 15).',
            '5.10': '§5.10 «Conditions for the valid application…» (índice, p. 16).',
            '5.11': '§5.11 compara GUM y MCM (índice, p. 17).',
            '6.4.8.4': '§6.4.8.4, título/cuerpo en el PDF; trata asignación conjunta multivariada; línea de extracción 1478 remite a covarianza conjunta.',
            '7.2.2': 'texto literal: M debe ser grande respecto de 1/(1−p), p. ej. al menos 10⁴/(1−p), para representación cerca de extremos (línea de extracción 2275).',
            '7.3': '§7.3 «Sampling from probability distributions» (índice, p. 29).',
            '7.5': '§7.5 representación discreta de distribución de salida (índice, p. 30).',
            '7.6': '§7.6 estima salida e incertidumbre estándar (índice, p. 31).',
            '7.7': '§7.7 intervalo de cobertura (índice, p. 31).',
            '7.8': '§7.8 tiempo de cómputo (índice, p. 32).',
            '7.9.2': '§7.9.2 tolerancia numérica (índice, p. 32).',
            '7.9.4': '§7.9.4 procedimiento adaptativo (índice, p. 33); subapartado g) se cita para error de la media.',
            '8.1.3': 'texto literal: comparación de extremos de intervalos GUM/MCM respecto de tolerancia numérica estipulada (línea de extracción 2720).',
        }
        detail = ' '.join(v for k, v in facts.items() if k in key)
        verified = any(token in key for token in ('5.9', '7.2.2', '8.1.3'))
        state = 'verificada' if verified else 'no verificable'
        prefix = 'Cotejo de cuerpo localizado. ' if verified else 'Solo se localizaron encabezados/índice para este numeral; no basta para verificar la afirmación puntual. '
        return state, f'{prefix}Archivo local `docs/ISO_IEC Guide 98-3_2008 Suppl.1_2008 - libgen.li.pdf`; evidencia: {detail} Las líneas son de `pdftotext -layout`, no páginas.'
    if 'GUM-S2' in key:
        return 'verificada', 'Archivo local `docs/ISO_IEC Guide 98-3_2008 Suppl.2_2011 - libgen.li.pdf`: índice sitúa §§5.2–5.3 en pp. impresas 10–11 y §6.2 en p. 15; §6.2.1.3 (línea de extracción 1404) da la matriz de covarianza de salidas para propagación multivariada.'
    if re.search(r'\bGUM\b', key):
        detail = {
            5: '§5.2.2; texto literal de encabezado: “When the input quantities are correlated…” y ecuación combinada (línea de extracción 1692).',
            6: '§5.1.2 (p. impresa 27 según bitácora S4) trata propagación linealizada; §5.2.2 (p. impresa 29 según bitácora) contiene expresión para entradas correlacionadas.',
            8: '§4.3.7 presenta bounds/tipo B; §4.4.5 describe rectangular uniforme; §4.3.9 indica que valores centrales pueden ser más probables; §4.4.6 es trapezoidal e incluye triangular como caso límite β=0 (líneas de extracción 1213, 1217, 1294, 1301).',
            9: '§4.3.9 dice que valores cercanos al centro pueden ser más probables; §4.4.6 describe trapezoidal y caso triangular límite β=0 (líneas de extracción 1294 y 1301).',
            10: '§4.3.7 bounds; §4.3.9 hipótesis triangular; §4.4.5 rectangular; §4.4.6 trapezoidal (líneas de extracción 1213, 1217, 1294, 1301).',
            11: 'Anexo H.5 se titula «Analysis of variance» (índice); su aplicación a los efectos aleatorios requiere revisar el texto del ejemplo local, no solo el título.',
            12: '§5.2.2 aporta fórmula de covarianza; no respalda por sí sola el ejemplo ni su cálculo.',
            13: '§G.4 «Effective degrees of freedom» (índice, p. 73); ecuación G.2b aparece en el texto extraído y da la expresión Welch–Satterthwaite.',
        }
        k = 5 if '5.2.2' in key else 6 if '5.1.2' in key else 8 if '4.3.7' in key and '4.3.9' not in key else 9 if '4.3.9' in key and '4.3.7' not in key else 10 if '4.3.7' in key else 11 if 'H.5' in key else 13 if 'G.4' in key else 12
        return 'verificada', f'Archivo local GUM `docs/ISO_IEC Guide 98-3_2008 Uncertainty of measurement -- Part 3_ Guide to the expression of uncertainty in measurement (GUM_1995) - libgen.li.pdf`. {detail[k]}'
    if 'ISO 28037' in key:
        detail = {
            '5.5': '§5.5, título «Uncertainties and covariance associated with the calibration function parameters» (índice p. 7); texto 5.5.2 formula vector de parámetros y matriz 2×2 (líneas de extracción 803–820).',
            '5.8.1': '§5.8.1 define la recta OLS como parámetros que minimizan la suma de cuadrados (línea de extracción 908; texto posterior del numeral).',
            '6.1.3': '§6.1.3 define pesos wi=1/u(yi) y minimización de suma ponderada (línea de extracción 965).',
            '6.2': '§6.2 se titula estimaciones y covarianza de parámetros; comprobar el desarrollo técnico en cuerpo del numeral (índice línea 90).',
            '10.1': '§10.1 General; capítulo 10 modela incertidumbres/covarianzas de xi y yi (índice línea 112; el cuerpo comienza en p. impresa 31).',
            '10': 'Capítulo 10, modelo de incertidumbres/covarianzas de x e y; §10.1 general y §10.2 estimación de parámetros (índice línea 112).',
            '11.1': '§11.1 «Prediction», p. impresa 37 según índice; la predicción inversa se desarrolla bajo capítulo 11.',
            '5.6.2': '§5.6.2 y notas tratan diagnóstico χ²; el capítulo 5.6 es validación del modelo (líneas 842–865).',
            '5.6.4': '§5.6.4 está citado; no se extrajo en esta ronda su texto íntegro para verificar la parte exacta de la afirmación.',
        }
        selected = [v for k, v in detail.items() if k in key]
        state = 'no verificable' if '5.6.4' in key else ('verificada' if selected else 'no verificable')
        return state, f'Archivo local `docs/ISO 28037.pdf`. ' + ' '.join(selected)
    if 'Crowder' in key:
        if '9.3.1' in key:
            return 'verificada', 'Archivo local `docs/intro_stats_metro_c09.pdf`, §9.3.1 encabezado «Random Effects Models»; el modelo aleatorio respalda el planteamiento general, pero no por sí solo toda la fórmula ANOVA particular.'
        if '10.2.1' in key:
            return 'verificada', 'Archivo local `docs/intro_stats_metro_c10.pdf`, §10.2.1 encabezado «Linear Least Squares»; texto indica que el caso lineal de mínimos cuadrados tiene solución analítica. No verifica toda la derivación matricial ni WLS.'
        if '4.3' in key:
            return 'verificada', 'Archivo local `docs/intro_stats_metro_c04.pdf`, §4.3 corresponde a Exploratory Data Analysis. La referencia no respalda por sí sola el divisor n−1 ni la restricción de grados de libertad; véase nota de alcance en decisiones.'
    if 'Hahs' in key:
        if '§2.3' in key:
            return 'no verificable', 'El índice del PDF local `docs/statistical_concepts_c02.pdf` identifica §2.3 como percentiles, no como demostración de insesgadez del divisor n−1; la ubicación no respalda la afirmación de AX.1. No se cambia la cita en este cotejo porque no se ha comprobado otro numeral del libro que la sustente.'
        return 'no verificable', 'PDF local `docs/Statistical Concepts – A First Course.pdf` y capítulos disponibles, pero no se aisló en el texto consultado el pasaje exacto de §§6.1/9.1 que pruebe los intervalos descritos; no se declara verificación por título de sección.'
    if 'BIPM-K1' in key:
        return 'no verificable', 'Archivo local `docs/BIPM.QM-K1_2.protocol.pdf` existe, pero en esta ronda no se extrajo el pasaje de §8, ec. 2–3. El catálogo o la nota bibliográfica no bastan para verificar su contenido; la generalización con covarianzas se apoya separadamente en GUM 5.2.2.'
    if 'CFR58-A' in key:
        return 'no verificable', 'Archivo local `docs/Appendix A to Part 58_ Title 40 (up to date as of 10-20-2026).pdf` existe; la única extracción localizada remite a §§4.1.2–4.1.3 (línea 430), sin mostrar el pasaje/formulación exacta. No se verifica por disponibilidad o remisión cruzada solamente.'
    if 'Montgomery' in key:
        return 'corregida', 'Fuente primaria consultada: Wiley, sitio compañero oficial, confirma Montgomery, título, 7.ª edición e ISBN 1118146816; resultado de Wiley Online Library indexado identifica la 7.ª ed. como publicación 2013. Búsqueda web también ubica CUSUM/EWMA en cap. 9, §§9.1–9.2, pero no se obtuvo texto primario accesible que permita cotejar las páginas. Se unifica la clave con M11 como «Montgomery 2013»; no se añade numeral/página al libreto.'
    if 'Efron' in key or 'Huber' in key:
        return 'no verificable', 'La obra se declara ausente de `docs/`; no se obtuvo en esta consulta una edición digital abierta con pasaje primario exacto para la afirmación citada. La cita bibliográfica sola no verifica el contenido.'
    if 'statsmodels' in key:
        return 'no verificable', 'La ocurrencia cita la implementación RLM/H1; no se verificó en esta tarea la documentación instalada ni el código fuente de la versión indicada. Es evidencia de software, no cita bibliográfica cotejada.'
    if 'JCGM 106' in key or 'ILAC-G8' in key:
        return 'no verificable', 'JCGM 106 e ILAC-G8 no están en `docs/`; no se obtuvo en esta ronda pasaje público exacto consultable. Por tanto, no se certifica soporte de las definiciones de riesgo.'
    return 'no verificable', 'Cita sin pasaje localizado en esta ronda.'

rows = []
for path in FILES:
    text = path.read_text(encoding='utf-8')
    for lineno, line in enumerate(text.splitlines(), 1):
        for match in CITES.finditer(line):
            rows.append((path.name, lineno, match.group(1), line.strip()))

inv = ['# Inventario exhaustivo de citas — lote S4', '', 'Fecha: 2026-10-27. Alcance exclusivo: ocurrencias entre corchetes con referencias bibliográficas en `M13_libreto.md` y `AX_libreto.md`. Se registra una fila por cada ocurrencia, incluidas repeticiones; línea según los archivos después de la edición de AX.12. Las remisiones internas AX y los nombres de herramientas no bibliográficas se excluyen.', '', f'Total: **{len(rows)} ocurrencias** — M13: {sum(x[0] == "M13_libreto.md" for x in rows)}; AX: {sum(x[0] == "AX_libreto.md" for x in rows)}.', '', '| # | Capítulo | Línea | Clave/localizador literal |', '|---:|---|---:|---|']
for i, (filename, line, key, _) in enumerate(rows, 1):
    inv.append(f'| {i} | `{filename}` | {line} | `{key.replace("|", "\\|")}` |')
(ROOT / 'curso/citas/S4_inventario.md').write_text('\n'.join(inv) + '\n', encoding='utf-8')

cot = ['# Cotejo bibliográfico por ocurrencia — lote S4', '', 'Fecha de cotejo: 2026-10-27. Se comprobó cada localizador en el PDF de `docs/` mediante extracción de texto y/o en las fuentes abiertas indicadas. La clasificación califica el respaldo de la afirmación concreta, no la mera existencia de una obra. «Corregida» indica ajuste de clave/localizador o limitación de atribución; no significa que todas las afirmaciones del capítulo estén verificadas. Las páginas se consignan solo cuando constan en el PDF/catálogo consultado; las líneas señaladas son números de extracción de `pdftotext`, no páginas.', '', '| # | Capítulo/línea | Clave/localizador | Estado | Motivo y evidencia exacta cotejada |', '|---:|---|---|---|---|']
for i, (filename, line, key, _) in enumerate(rows, 1):
    state, ev = evidence(key, filename, line)
    cot.append(f'| {i} | `{filename}:{line}` | `{key.replace("|", "\\|")}` | **{state}** | {ev} |')
cot += ['', '## Fuentes abiertas consultadas para Montgomery', '', '- Wiley, sitio compañero de la 7.ª edición, ISBN 1118146816: https://bcs.wiley.com/he-bcs/Books?action=index&bcsId=7328&itemId=1118146816. Confirma autor y 7.ª edición; la página recibida no declara el año.', '- Wiley Online Library, registro de capítulo citado en búsqueda: https://onlinelibrary.wiley.com/doi/10.1002/9781119528425.ch7. El resultado indexado confirma la 7.ª edición como 2013, pero no fue posible recuperar su contenido para cotejar paginación.', '- O’Reilly, capítulo 9 (resultado de búsqueda; acceso 403 en la consulta): https://www.oreilly.com/library/view/statistical-quality-control/9781118146811/Chapter09.html. La búsqueda lo identifica como CUSUM/EWMA; no se le atribuyen páginas exactas.', '', 'Por límite de acceso a texto primario de Montgomery, se normaliza la clave bibliográfica a `Montgomery 2013` para concordar con M11, pero no se añade localizador a AX.12. Las entradas `no verificable` quedan explícitas; ni un índice ni un título se consideran evidencia suficiente por sí solos.']
(ROOT / 'curso/citas/S4_cotejo.md').write_text('\n'.join(cot) + '\n', encoding='utf-8')
