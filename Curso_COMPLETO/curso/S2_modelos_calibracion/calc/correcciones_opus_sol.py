"""Registro editorial del cierre Opus; no reejecutar sobre libretos corregidos."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace(text, old, new):
    assert old in text, old
    return text.replace(old, new)


def main():
    path = ROOT / 'M05_libreto.md'
    text = path.read_text()
    text = replace(text, '## Nivel B — Lo que se añade', '## Nivel B — estructurar la pregunta experimental')
    text = replace(text, ', no a un cálculo de potencia de pendiente.', '.')
    text = replace(text, ' La pregunta «¿cuántas corridas hacen falta para detectar un cambio de pendiente de 0,005?» requiere además definir intervalo de concentraciones, variabilidad, diseño y tasas de error; este ejemplo no calcula esa potencia.', '')
    text = replace(text, '[ISO 5725-3; la deducción está en el Anexo AX.4]', '[GUM H.5; AX.4, deducción]')
    text = replace(text, 'Esto ilustra precisión del promedio bajo el modelo, no sustituye un cálculo de potencia para la pendiente 0,005.', 'Esto ilustra la precisión del promedio bajo el modelo.')
    text = replace(text, 'sin cambiar de pregunta a una pendiente', 'para esa misma media')
    text = replace(text, 'ni la potencia de detectar una pendiente de 0,005', 'bajo otros modelos o diseños')
    path.write_text(text)

    path = ROOT / 'M06_libreto.md'
    text = path.read_text()
    text = replace(text, '## Nivel B — interpretar componentes entregadas\n', '## Nivel B — interpretar componentes entregadas\n\nDamos por vistos M3-B, dispersión de lecturas y promedios; M4-B, inferencia de una media y grados de libertad; y M5-B, factores, réplicas, bloques y unidad experimental. Aquí interpretamos componentes ya estimadas, sin ejecutar ANOVA.\n')
    text = replace(text, '[ISO 5725-3 §8].\n\n> **[PIZARRA]** $e_{dj}', '[ISO 5725-3 §6.1].\n\n> **[PIZARRA]** $e_{dj}')
    text = replace(text, '[Crowder 2020 §9.3.1; ISO 5725-3 §8]', '[Crowder 2020 §9.3.1; ISO 5725-3 §6.1]')
    text = replace(text, '[GUM H.5; ISO 5725-3 §8]', '[GUM H.5; ISO 5725-3 §6.1]')
    text = replace(text, '[Hahs-Vaughn, cap. 9; GUM 5.1.2]', '[Hahs-Vaughn §8.2.1; GUM 5.1.2]')
    text = text.replace('[VIM; ISO 5725-1; MMU §4.4]', '[VIM (no disponible en docs/); ISO 5725-3 §§5–6; MMU §4.4]')
    text = replace(text, '[ISO 5725-1; ISO 5725-3 §8; ISO 5725-6]', '[ISO 5725-1 (no disponible en docs/); ISO 5725-3 §8; ISO 5725-6]')
    text = replace(text, 'medias diarias de 0,73 y 0,83', 'medias de bloque (seis días) de 0,73 y 0,83')
    text = replace(text, 'Hasta entonces, presentar solo la estructura observada en las hojas por nivel.', 'Hasta entonces, presentar la estructura observada y los cálculos como descomposición exploratoria condicional, no como inferencia validada de CALAIRE. Todas las salvedades siguientes quedan cubiertas por esta nota: no se documentan muestreo aleatorio, signo ni cruce real de bloques; cruzarlos por posición podría crear interacción artificial.')
    text = replace(text, 'La asociación de los bloques con campañas concretas es una inferencia y no se presenta aquí como dato confirmado. ', '')
    text = replace(text, 'Por eso no afirmamos ni coincidencia ni separación temporal sin confirmar: «día uno» de ambas columnas no constituye una pareja demostrada.', '«Día uno» de ambas columnas no constituye una pareja demostrada.')
    text = replace(text, 'No afirmamos que el libro documente muestreo aleatorio ni correspondencia real entre bloques de ambos analistas. Sin esa correspondencia, cruzar por posición puede crear una interacción artificial y el modelo debe replantearse. ', '')
    text = replace(text, 'En este cálculo condicional no aparece un efecto medio detectable de analista; no es una conclusión validada del estudio histórico. Solo afirmamos que los cocientes calculados no exceden ese umbral bajo el modelo supuesto; todavía no podemos inferir ausencia de diferencia media en el estudio real.', 'Los cocientes calculados no exceden ese umbral bajo el modelo supuesto; consulten la nota inicial antes de interpretarlos como evidencia histórica.')
    text = replace(text, 'Si el emparejamiento de bloques y el signo son válidos, las diferencias entre analistas cambian según el bloque; sin confirmarlos, solo describimos la descomposición numérica. Si la asignación se confirma, se interpretará como interacción con campaña.', 'En el modelo, esto representa diferencias entre analistas que cambian según el bloque; la interpretación como campaña requiere la confirmación indicada al inicio.')
    text = replace(text, 'Capítulo 9 (varianzas) y §8.2.1 (control', 'Capítulo 9 (varianzas) y §8.2.1 (varianza de chi-cuadrado y control')
    path.write_text(text)

    path = ROOT / 'M07_libreto.md'
    text = path.read_text()
    text = replace(text, 'en el conjunto considerado. No informa', 'en el conjunto considerado [Otto §6.1, ec. (6.17)]. No informa')
    text = replace(text, 'aunque el tamaño de los residuos en nmol/mol no cambie.', 'aunque el tamaño de los residuos en nmol/mol no cambie [Hahs-Vaughn §10.1.1.5.2, restricción del intervalo].')
    text = replace(text, 'Por eso R² acompaña al diagnóstico; no lo sustituye [Crowder 2020 §10.4, PDF pp. 9–10].', 'Por eso R² acompaña al diagnóstico de residuos; no lo sustituye [Crowder 2020 §10.4.1].')
    text = replace(text, '[Crowder 2020 §10.1.2, PDF p. 3; ISO 28037 §5.7]', '[Crowder 2020 §10.1.2, PDF p. 3]')
    text = replace(text, 'dividido por la pendiente». La corrección', 'dividido por la pendiente» [ISO 28037 §§5.7, 11.1]. La corrección')
    text = replace(text, '[prop_e §3; ISO 28037 §5.7]', '[prop_e §3, convención del curso; VIM, definición de corrección (no disponible en docs/)]')
    text = replace(text, 'El peso no es una preferencia', '> **[NOTA AL INSTRUCTOR]** ISO 28037 §6.1.3 llama peso a $1/u(y_i)$ y minimiza la suma con ese peso al cuadrado. Aquí llamamos peso a $1/u^2(y_i)$ y lo usamos sin elevarlo otra vez al cuadrado: ambas formulaciones son equivalentes.\n\nEl peso no es una preferencia')
    text = replace(text, 'en este ejemplo aumenta $u(a)$ de $0{,}34152$ a $0{,}36204', 'en GGMR, $u(a)$ pasa de $0{,}342$ sin componente común a $0{,}362')
    # Datos visibles para las tres escenas: mismos valores que el script.
    material = '''> **[MATERIAL]** Comparación OLS/WLS, datos **simulados**, todas las magnitudes salvo pesos en nmol/mol.

| $x$ | $y$ | $u(y)$ |
|---:|---:|---:|
| 0 | 0,4 | 0,25 |
| 100 | 100,5 | 0,30 |
| 200 | 200,8 | 0,40 |
| 300 | 300,2 | 0,60 |
| 400 | 401,4 | 0,90 |
| 500 | 500,5 | 1,20 |

'''
    text = replace(text, 'En este ejemplo simulado, las incertidumbres', material + 'En este ejemplo simulado, las incertidumbres')
    material = '''> **[MATERIAL]** Falta de ajuste: datos **simulados**, nmol/mol. Cada columna de observación contiene una réplica independiente al mismo $x$.

| $x$ | $y_1$ | $y_2$ | $y_3$ |
|---:|---:|---:|---:|
| 0 | 0,1 | 0,2 | 0,3 |
| 100 | 100,2 | 100,1 | 100,3 |
| 200 | 200,0 | 200,1 | 200,2 |
| 300 | 301,0 | 301,1 | 301,2 |

'''
    text = replace(text, 'En un conjunto simulado con cuatro niveles', material + 'En un conjunto simulado con cuatro niveles')
    import numpy as np
    xv = np.linspace(0,550,12)
    yv = .3 + 1.001*xv + np.array([.10,-.20,.15,-.10,.25,-.15,.20,-.25,.10,-.10,.15,-.05])
    rows = '\n'.join(f'| {x:.0f} | {y:.2f} | {u:.2f} |'.replace('.', ',') for x,y,u in zip(xv,yv,np.linspace(.30,.85,12)))
    material = '> **[MATERIAL]** Diagnóstico WLS: datos **simulados**, nmol/mol. Generación: $y_i=0{,}3+1{,}001x_i+\delta_i$, con desviaciones fijadas en el script.\n\n| $x$ | $y$ | $u(y)$ |\n|---:|---:|---:|\n' + rows + '\n\n'
    text = replace(text, 'Empecemos por el caso más simple', material + 'Empecemos por el caso más simple')
    # Redondeo oral; precisión completa permanece en el script.
    replacements = {'`0,99999645`':'casi uno (más de 0,99999)', '`1,0014285714`':'`1,00143`', '`0,24285714 nmol/mol`':'`0,243 nmol/mol`', '0{,}24285714':'0{,}243', '1{,}0014285714':'1{,}00143', '`0,39460649 nmol/mol`':'`0,3946 nmol/mol`', '249{,}90014265':'249{,}900', '-0{,}59985735':'-0{,}600', '0{,}28559521':'0{,}2856', '0{,}0009432899':'0{,}0009433', '-0{,}0002224490':'-0{,}0002224', '`250,60000000 nmol/mol`':'`250,600 nmol/mol`', '`0,44727816 nmol/mol`':'`0,4473 nmol/mol`', '`1,18338678 nmol/mol`':'`1,183 nmol/mol`', '`0,44727816`':'`0,4473`', '0{,}25644562':'0{,}2564', '2{,}05618':'2{,}056', '0{,}52730':'0{,}5273', '`1,0020909091`':'`1,00209`', '0{,}44761905':'0{,}4476', '1{,}0007428571':'1{,}000743', '0{,}41685160':'0{,}4169', '1{,}0009213402':'1{,}000921', '0{,}00003422':'3{,}422\\times10^{-5}', '0{,}3047254':'0{,}3047', '1{,}0013144319':'1{,}001314', '`0,40890065`':'`0,4089`', '0{,}30476190':'0{,}3048', '1{,}00131429':'1{,}001314', '0{,}34240092':'0{,}3424', '1{,}00123076':'1{,}001231', '1{,}77184745':'1{,}772', '1{,}27964725':'1{,}280', '18{,}30703805':'18{,}31', '`0,61604636`':'`0,6160`', '0{,}40890065':'0{,}4089', '`83,36173290`':'`83,36`'}
    for old,new in replacements.items():
        text = text.replace(old,new)
    text += '\n- **VIM** — JCGM 200:2012, *International vocabulary of metrology — Basic and general concepts and associated terms*, 3.ª ed. (no disponible en docs/; definición de corrección, sin numeral).\n'
    path.write_text(text)


if __name__ == '__main__':
    main()
