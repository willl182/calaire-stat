"""Extrae corchetes para cotejar la cobertura de los inventarios bibliográficos.

Es un control literal, no decide si una referencia está verificada.
"""
import argparse
import csv
import hashlib
import re
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("curso", type=Path)
parser.add_argument("salida", type=Path)
args = parser.parse_args()
acotaciones = {
    "PIZARRA", "DIAPOSITIVA", "MATERIAL", "PREGUNTA AL GRUPO", "PAUSA",
    "EJEMPLO", "ERROR CRÍTICO", "ESCALAMIENTO", "TRANSICIÓN",
    "NOTA AL INSTRUCTOR", "PRÁCTICA — fase de ejercicios",
}
with args.salida.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t")
    writer.writerow(["archivo", "sha256", "linea", "corchete_literal"])
    for path in sorted(args.curso.glob("*/*_libreto.md")):
        if not (path.name.startswith("M") or path.name == "AX_libreto.md"):
            continue
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        for number, line in enumerate(raw.decode("utf-8").splitlines(), 1):
            for match in re.finditer(r"\[([^\]\n]+)\]", line):
                value = match.group(1)
                if value not in acotaciones:
                    writer.writerow([str(path), digest, number, value])
