"""Comprobaciones estructurales de S2; no modifica libretos ni respaldos."""
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[1]


def main():
    for chapter in ('M05', 'M06', 'M07', 'M08'):
        text = (BASE / f'{chapter}_libreto.md').read_text()
        markers = text.count('**[PRÁCTICA — fase de ejercicios]**')
        assert markers == 3, (chapter, markers)
        assert '## Referencias del capítulo' in text
        assert '## Cierre del capítulo' in text
        allowed = {'PIZARRA', 'DIAPOSITIVA', 'MATERIAL', 'PREGUNTA AL GRUPO',
                   'PAUSA', 'EJEMPLO', 'PRÁCTICA — fase de ejercicios',
                   'ERROR CRÍTICO', 'ESCALAMIENTO', 'TRANSICIÓN', 'NOTA AL INSTRUCTOR'}
        tags = re.findall(r'\*\*\[([^\]]+)\]\*\*', text)
        assert set(tags) <= allowed, (chapter, set(tags) - allowed)
        for level in ('B', 'I', 'A'):
            assert f'## Nivel {level}' in text, (chapter, level)
            section = re.search(rf'^## Nivel {level}[^\n]*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
            assert section is not None
            assert section.group(1).count('**[PRÁCTICA — fase de ejercicios]**') == 1, (chapter, level)
        for reference in re.findall(r'`(docs/[^`]+)`', text):
            if reference.endswith(('.pdf', '.xlsx', '.xlsm')):
                assert (BASE.parents[1] / reference).is_file(), (chapter, reference)
        scenes = re.findall(r'^### Escena ([BIA]\d+)\. (.+)$', text, re.M)
        assert len(scenes) == len(set(number for number, _ in scenes))
        print(f'{chapter}: tres marcadores, niveles y cierre presentes; {len(scenes)} escenas.')
        for number, title in scenes:
            print(f'  {number}. {title}')

    inventory = json.loads((BASE / 'calc/inventario_fuentes_heredadas_sol.json').read_text())
    for entry in inventory:
        actual = hashlib.sha256((BASE / entry['archivo']).read_bytes()).hexdigest()
        assert actual == entry['sha256'], entry['archivo']
    print(f'Extractos heredados: {len(inventory)} huellas verificadas.')

    total = 0
    for audit in ('auditoria_interrupcion_sol_2/cambios_sol.diff',
                  'auditoria_interrupcion_sol_3/cambios.diff',
                  'auditoria_respaldo_20261026_195250/cambios.diff',
                  'auditoria_respaldo_20261026_200841/cambios.diff'):
        text = (BASE / audit).read_text()
        count = len(re.findall(r'^@@ ', text, re.M))
        total += count
        print(f'{audit}: {count} bloques candidatos.')
    assert total == 94, total
    print('Total: 94 bloques; cotejar decisiones en S2_revision_sol.md.')

    disabled = BASE / 'calc/ajustes_sol.py'
    text = disabled.read_text()
    assert text.index('raise SystemExit(') < text.index('from pathlib import Path')
    print('ajustes_sol.py: bloqueo anterior a importaciones y escrituras.')


if __name__ == '__main__':
    main()
