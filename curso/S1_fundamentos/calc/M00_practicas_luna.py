"""Solución docente: reproduce resultados y controles de las tres prácticas M00.
Datos construidos explícitamente para docencia; no son de CALAIRE.
No es una plantilla para entregar al alumnado.
"""
from collections import Counter, defaultdict

# B: la corrección de P99 se sustenta únicamente en el registro original R03.
refs = {"P01": ("L0", 0.0), "P02": ("L1", 50.0),
        "P03": ("L1", 50.0), "P04": ("L2", 100.0)}
indicaciones = [("P01", "R01", -0.2), ("P02", "R02", 50.4),
                ("P99", "R03", 50.8)]
cotejo_autorizado = {
    "R03": {
        "texto": "El registro de adquisición R03 vincula la indicación con la pareja de referencia P03; P04 no fue adquirido",
        "id_original": "P99",
        "id_corregido": "P03",
        "motivo": "el registro de adquisición R03 vincula esta lectura con P03",
    }
}
assert len(refs) == 4 and len(indicaciones) == 3
por_id_original = defaultdict(list)
for clave, adquisicion, y in indicaciones:
    por_id_original[clave].append((adquisicion, y))
assert all(len(v) == 1 for v in por_id_original.values())
completas_antes = {k for k in por_id_original if k in refs}
huerfanas_antes = {k for k in por_id_original if k not in refs}
no_emparejadas_antes = set(refs) - completas_antes
assert (len(completas_antes), len(huerfanas_antes), len(no_emparejadas_antes)) == (2, 1, 2)
por_id = {}
for clave, registros in por_id_original.items():
    adquisicion, y = registros[0]
    if adquisicion in cotejo_autorizado:
        cotejo = cotejo_autorizado[adquisicion]
        assert clave == cotejo["id_original"]
        por_id[cotejo["id_corregido"]] = (clave, adquisicion, y, cotejo["motivo"])
    else:
        por_id[clave] = (clave, adquisicion, y, None)
validos = {clave: registro[2] - refs[clave][1]
           for clave, registro in por_id.items() if clave in refs}
expected_b = {"P01": -0.2, "P02": 0.4, "P03": 0.8}
assert {k: round(v, 1) for k, v in validos.items()} == expected_b
assert por_id["P03"] == ("P99", "R03", 50.8,
                           "el registro de adquisición R03 vincula esta lectura con P03")
assert "P04" not in por_id and len(refs) - len(validos) == 1
assert len(por_id) - len(validos) == 0
print("B antes de R03: parejas completas=2; indicaciones huérfanas=1; referencias no emparejadas=2")
print("B cotejo R03:", cotejo_autorizado["R03"]["texto"])
print("B corrección trazable: id_original=P99; y_original=50.8; id_corregido=P03; motivo=el registro de adquisición R03 vincula esta lectura con P03; fuente=registro de adquisición R03")
print("B después de R03: parejas completas=3; referencia P04 sin indicación adquirida=1; indicaciones huérfanas=0")
print("B: errores", {k: round(v, 1) for k, v in validos.items()})

# I: campaña, analista, día, ciclo, x, y; None conserva el faltante.
data = [
    ("C1", "A1", 1, 1, 50.0, 50.2), ("C1", "A1", 1, 2, 50.0, 50.4),
    ("C1", "A1", 2, 1, 50.0, 50.0), ("C1", "A1", 2, 2, 50.0, 50.2),
    ("C1", "A2", 1, 1, 50.0, 49.8), ("C1", "A2", 1, 2, 50.0, None),
    ("C1", "A2", 2, 1, 50.0, 50.1), ("C1", "A2", 2, 2, 50.0, 50.3),
]
assert len({(campaign, analyst, day, cycle) for campaign, analyst, day, cycle, x, y in data}) == 8
assert sum(y is not None for *_, y in data) == 7
summary = {}
for analyst, day in sorted({(r[1], r[2]) for r in data}):
    ys = [y for campaign, a, d, c, x, y in data if a == analyst and d == day and y is not None]
    es = [y - x for campaign, a, d, c, x, y in data if a == analyst and d == day and y is not None]
    summary[(analyst, day)] = (len(ys), sum(ys) / len(ys), sum(es) / len(es))
expected = {("A1", 1): (2, 50.3, 0.3), ("A1", 2): (2, 50.1, 0.1),
            ("A2", 1): (1, 49.8, -0.2), ("A2", 2): (2, 50.2, 0.2)}
assert {k: (n, round(y, 1), round(e, 1)) for k, (n, y, e) in summary.items()} == expected
print("I: claves únicas campaña-analista-día-ciclo=8 (campaña C1)")
print("I: n, media y, media e por analista-día",
      {k: (n, round(y, 1), round(e, 1)) for k, (n, y, e) in summary.items()})
print("I: completos=7; faltantes=1")

# A: contract check; second output intentionally differs at Q06.
rows = [
    ("Q01", 0.0, -0.1, -0.1), ("Q02", 25.0, 25.2, 0.2),
    ("Q03", 50.0, 50.5, 0.5), ("Q04", 100.0, 100.8, 0.8),
    ("Q05", 150.0, 150.6, 0.6), ("Q06", 200.0, 201.0, 0.9),
]
keys = [key for key, *_ in rows]
assert len(keys) == 6 and len(set(keys)) == 6
assert all(x is not None and y is not None for _, x, y, _ in rows)
assert all(isinstance(x, (int, float)) and isinstance(y, (int, float))
           for _, x, y, _ in rows)
# Input unit metadata must match the expected unit for both columns.
expected_unit = "nmol/mol"

def check_units(units):
    assert units["x"] == expected_unit and units["y"] == expected_unit


input_units = {"x": "nmol/mol", "y": "nmol/mol"}
check_units(input_units)
try:
    check_units({"x": "nmol/mol", "y": "ng/m3"})
except AssertionError:
    negative_unit_test_rejected = True
else:
    raise AssertionError("Negative unit test should reject y=ng/m3")
tol = 0.000001
residuals = [abs((y - x) - e2) for _, x, y, e2 in rows]
assert max(residuals[:5]) < 1e-12 and abs(residuals[5] - 0.1) < 1e-12
max_diff = max(residuals)
assert max_diff > tol
print("A: controles claves_unicas=6; faltantes=0; unidades_compatibles=", True,
      "prueba_negativa_ng/m3_rechazada=", negative_unit_test_rejected)
print("A: errores recalculados", [round(y - x, 1) for _, x, y, _ in rows])
print("A: diferencias", [round(v, 1) for v in residuals],
      "máxima=", round(max_diff, 1), "tolerancia=", tol, "acuerdo=", max_diff <= tol)
