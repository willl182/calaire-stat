"""Contraste independiente de resultados docentes M00 mediante Decimal."""
from decimal import Decimal as D
from itertools import product

x = list(map(D, ["0", "50", "100", "150"]))
y = list(map(D, ["-0.2", "50.4", "100.8", "150.7"]))
errores = [b - a for a, b in zip(x, y)]
assert errores == list(map(D, ["-0.2", "0.4", "0.8", "0.7"]))
assert sum(errores) / D(4) == D("0.425")
assert D("100.8") - D("50") == D("50.8")
filas = list(product(("C1", "C2"), ("A1", "A2"), (1, 2), (1, 2)))
assert len(filas) == 16
for campania in ("C1", "C2"):
    assert sum(r[0] == campania for r in filas) == 8
for analista in ("A1", "A2"):
    assert sum(r[1] == analista for r in filas) == 8
    for dia in (1, 2):
        assert sum(r[1:3] == (analista, dia) for r in filas) == 4
print("M00: Decimal confirma errores, media 0.425, falso pareo 50.8 y conteos 16/8/4.")
