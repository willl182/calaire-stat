"""Inventario reproducible de los 94 bloques históricos de revisión S2."""
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[1]
AUDITS = (
    ('R2', 'auditoria_interrupcion_sol_2/cambios_sol.diff'),
    ('R3', 'auditoria_interrupcion_sol_3/cambios.diff'),
    ('R4', 'auditoria_respaldo_20261026_195250/cambios.diff'),
    ('R5', 'auditoria_respaldo_20261026_200841/cambios.diff'),
)


def collect():
    records = []
    for audit, relative in AUDITS:
        chapter = None
        counter = 0
        block = []
        header = None

        def flush():
            if header is not None:
                payload = '\n'.join(block) + '\n'
                records.append({
                    'id_bloque': f'{audit}-{chapter}-{counter:02d}',
                    'diff': relative,
                    'capitulo': chapter,
                    'cabecera': header,
                    'sha256_bloque': hashlib.sha256(payload.encode()).hexdigest(),
                    'adiciones': sum(line.startswith('+') for line in block[1:]),
                    'supresiones': sum(line.startswith('-') for line in block[1:]),
                })

        for line in (BASE / relative).read_text().splitlines():
            if line.startswith('--- '):
                flush()
                header, block = None, []
                match = re.search(r'(M\d+)_libreto\.md', line)
                chapter = match.group(1) if match else None
                counter = 0
            elif line.startswith('@@ '):
                flush()
                counter += 1
                header, block = line, [line]
            elif header is not None:
                block.append(line)
        flush()
    return records


if __name__ == '__main__':
    records = collect()
    assert len(records) == 94
    assert len({item['id_bloque'] for item in records}) == 94
    destination = BASE / 'calc/inventario_bloques_sol.json'
    destination.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    for chapter in ('M05', 'M06', 'M07', 'M08'):
        selected = [item for item in records if item['capitulo'] == chapter]
        print(f'{chapter}: {len(selected)} bloques')
    print(f'Inventario: {destination.relative_to(BASE)}')
