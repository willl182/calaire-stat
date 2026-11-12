#!/usr/bin/env python3
"""Ejecuta rondas luna/Haiku; el supervisor verifica y cierra los hitos aparte."""
from pathlib import Path
import subprocess
import sys

ROOT = Path('/home/w421/w421/calaire-stat')
LOG = ROOT / 'curso/logs'
BASE = '''Trabaja en /home/w421/w421/calaire-stat. Lee curso/guia_libreto.md, prop_e.md y curso/revision_final.md. La petición actual autoriza desarrollar las prácticas pese a la restricción de fase anterior de la guía. Curso narrado para operadores SRP del laboratorio designado INM, caso ozono/SRP, competencias estadísticas B/I/A acumulativas. Prácticas aplicadas, NO demostraciones; deducciones se remiten a anexos. NO commits. NO cambies referencias bibliográficas, claves, citas existentes ni secciones de referencias: supervisor paralelo las trabaja. No cambies otros capítulos, guía ni revision_final.md. Edita únicamente los bloques de práctica y crea tus propios archivos de bitácora/cálculo. Datos explícitamente simulados con regla reproducible o propios con ruta verificable; nunca atribuyas simulaciones a CALAIRE. Unidades nmol/mol, coma decimal. Usa curso/.venv/bin/python para cálculos, scripts en calc/ de la sección. Si el alcance exige gráficos, prepara datos y tareas de trazado y también salida gráfica reproducible: lee antes la habilidad dataviz en /tmp/claude-1000/bundled-skills/2.1.310/2f61c5aeeb1c7fa7387d9a5b54dd86ec/dataviz/SKILL.md, aplica sus referencias y valida paleta; usa marcas/estilos distintos, leyenda, unidades y tabla accesible. No omitas un gráfico obligatorio por simplificar. Escribe solución docente verificable, decisión operativa y señales de escalamiento, sin convertir defectos de archivos en ejercicios. Ajusta estrictamente el alcance de cada nivel a prop_e. Evita sobrescribir cambios concurrentes: ediciones exactas localizadas, no reemplazar el archivo entero.'''

def run(cmd, prompt, logfile):
    with logfile.open('w') as out:
        p = subprocess.run(cmd + [prompt], cwd=ROOT, stdout=out, stderr=subprocess.STDOUT)
    if p.returncode:
        raise RuntimeError(f'{logfile}: rc={p.returncode}')

luna = ['claude-luna','--effort','low','-p','--dangerously-skip-permissions','--output-format','text']
haiku = ['env','-u','ANTHROPIC_BASE_URL','-u','ANTHROPIC_API_KEY','-u','CLAUDE_CODE_AUTO_MODE_SERVER','claude','--model','claude-haiku-5-5','--effort','low','-p','--dangerously-skip-permissions','--output-format','text']
for n in ([int(sys.argv[1])] if len(sys.argv) > 1 else range(1, 14)):
    name = f'M{n:02d}'
    chapter = next((ROOT/'curso').glob(f'S*/{name}_libreto.md'))
    rel = chapter.relative_to(ROOT)
    review = f'curso/logs/{name}_practicas_revision_haiku.md'
    record = f'curso/logs/{name}_practicas_luna.md'
    count = 'una práctica nivel A' if n == 13 else 'tres prácticas, una por nivel B, I y A'
    if len(sys.argv) < 3:
        run(luna, BASE + f'\nHito capítulo {name}: desarrolla {count} sustituyendo los marcadores de {rel}. Usa etiqueta [PRÁCTICA] para los bloques desarrollados. Cada práctica: título correspondiente a prop_e, enunciado narrado, datos suficientes, tareas aplicadas, solución docente con números y comprobaciones, interpretación y criterio de logro breve. No desarrolles taller integrador adicional. Guarda plan, ejecución, archivos tocados y comprobaciones en {record}. Ejecuta tus cálculos. Deja todas las prácticas completas, no como propuestas.', LOG/f'{name}_practicas_ejecucion.log')
    if len(sys.argv) < 3 or sys.argv[2] == 'revision':
        run(haiku, BASE + f'\nEres revisor, NO edites libretos ni scripts. Revisa las prácticas nuevas de {rel}, sus scripts y {record}. Lee archivo real, verifica números mediante ejecución cuando corresponda, coherencia estadística, alcance B/I/A, origen datos, soluciones y aplicación ozono/SRP. Escribe revisión en {review} con hallazgos H-01 etc., severidad, ubicación y corrección propuesta; si no hay hallazgos dilo explícitamente. No audites referencias (otro supervisor).', LOG/f'{name}_practicas_revision.log')
    run(luna, BASE + f'\nRonda de correcciones {name}. Lee {review}; aplica o rechaza CADA hallazgo con justificación explícita en {record}. Corrige únicamente prácticas nuevas de {rel} y sus scripts. Ejecuta cálculos y registra resultados finales. No basta prometer cambios. Si no hay hallazgos registra decisión sin cambios. Incluye tabla H-xx -> decisión -> ubicación y resultado.', LOG/f'{name}_practicas_correccion.log')
    (LOG/f'{name}_practicas_listo.txt').write_text(f'{rel}\n{review}\n{record}\n')
