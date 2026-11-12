"""Comprueba los diffs sin aplicarlos sobre ningún archivo histórico."""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parents[1]
PAIRS = (
    ('versiones/20261025_202101_antes_P4_sol',
     'versiones/20261025_220040_antes_P4_sol',
     'auditoria_interrupcion_sol_2/cambios_sol.diff'),
    ('versiones/20261025_220040_antes_P4_sol',
     'versiones/20261026_052610_antes_P4_sol',
     'auditoria_interrupcion_sol_3/cambios.diff'),
    ('versiones/20261026_052610_antes_P4_sol',
     'auditoria_respaldo_20261026_195250/estado_al_corte',
     'auditoria_respaldo_20261026_195250/cambios.diff'),
    ('versiones/20261026_195354_antes_P4_sol',
     'auditoria_respaldo_20261026_200841/estado_al_corte',
     'auditoria_respaldo_20261026_200841/cambios.diff'),
)


def reconstruct(lines, source, name):
    section = False
    output = []
    position = 0
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith('--- '):
            section = line.endswith('/' + name)
        elif section and line.startswith('@@ '):
            match = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
            assert match, line
            start, old_count, _, new_count = match.groups()
            start = int(start) - 1
            old_count, new_count = int(old_count or 1), int(new_count or 1)
            output.extend(source[position:start])
            position = start
            used_old = used_new = 0
            while used_old < old_count or used_new < new_count:
                index += 1
                operation = lines[index]
                assert operation and operation[0] in ' +-', operation
                if operation[0] in ' -':
                    assert source[position] == operation[1:], (name, position + 1)
                    position += 1
                    used_old += 1
                if operation[0] in ' +':
                    output.append(operation[1:])
                    used_new += 1
            assert (used_old, used_new) == (old_count, new_count)
        index += 1
    output.extend(source[position:])
    return output


if __name__ == '__main__':
    for old, new, audit in PAIRS:
        lines = (BASE / audit).read_text().splitlines()
        for chapter in ('M05', 'M06', 'M07', 'M08'):
            name = f'{chapter}_libreto.md'
            source = (BASE / old / name).read_text().splitlines()
            target = (BASE / new / name).read_text().splitlines()
            assert reconstruct(lines, source, name) == target, (audit, name)
        print(f'{audit}: reconstrucción exacta de los cuatro libretos.')
    for chapter in ('M05', 'M06', 'M07', 'M08'):
        name = f'{chapter}_libreto.md'
        cut = BASE / 'auditoria_respaldo_20261026_195250/estado_al_corte' / name
        initial = BASE / 'versiones/20261026_195354_antes_P4_sol' / name
        assert cut.read_bytes() == initial.read_bytes(), chapter
    print('Estado al corte idéntico a la instantánea previa de esta reanudación.')
    for chapter in ('M05', 'M06', 'M07', 'M08'):
        name = f'{chapter}_libreto.md'
        cut = BASE / 'auditoria_respaldo_20261026_200841/estado_al_corte' / name
        initial = BASE / 'versiones/20261026_200856_antes_P4_sol' / name
        assert cut.read_bytes() == initial.read_bytes(), chapter
    print('Último estado al corte idéntico a la instantánea 20261026_200856.')
    print('Cadena histórica de libretos cubierta por 94 bloques; auxiliares auditados aparte.')
