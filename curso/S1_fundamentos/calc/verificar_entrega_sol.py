"""Comprobaciones estructurales de la entrega S1; no sustituyen revisión técnica."""
from pathlib import Path
import re

raiz = Path(__file__).resolve().parents[1]
etiquetas = {
    "PIZARRA", "DIAPOSITIVA", "MATERIAL", "PREGUNTA AL GRUPO", "PAUSA",
    "EJEMPLO", "PRÁCTICA — fase de ejercicios", "ERROR CRÍTICO",
    "ESCALAMIENTO", "TRANSICIÓN", "NOTA AL INSTRUCTOR",
}
marcadores = 0
for numero in range(5):
    archivo = raiz / f"M{numero:02d}_libreto.md"
    texto = archivo.read_text()
    for nivel in "BIA":
        assert re.search(rf"^## Nivel {nivel}\b", texto, re.M), (archivo.name, nivel)
        assert re.search(rf"^### Escena {nivel}\d", texto, re.M), (archivo.name, nivel)
    encontrados = re.findall(r"^> \*\*\[PRÁCTICA — fase de ejercicios\]\*\* (.+)$", texto, re.M)
    assert len(encontrados) == 3, (archivo.name, len(encontrados))
    marcadores += len(encontrados)
    assert "## Cierre del capítulo" in texto
    assert "## Referencias del capítulo" in texto
    for etiqueta in re.findall(r"^> \*\*\[([^\]]+)\]\*\*", texto, re.M):
        assert etiqueta in etiquetas, (archivo.name, etiqueta)
    print(f"{archivo.name}: B/I/A, 3 marcadores, cierre, referencias y etiquetas correctos.")
assert marcadores == 15
revision = (raiz / "S1_revision_sol.md").read_text()
for titulo in ("Plan de revisión", "Hallazgos por capítulo", "Correcciones aplicadas", "Estado de entrega"):
    assert f"## {titulo}" in revision, titulo
assert "### Nota del orquestador: ediciones previas a la interrupción" in revision
hallazgos = revision.split("## Hallazgos por capítulo", 1)[1].split("## Correcciones aplicadas", 1)[0]
correcciones = revision.split("## Correcciones aplicadas", 1)[1].split("## Estado de entrega", 1)[0]
for numero in range(1, 28):
    candidato = f"C{numero:02d}"
    hallazgo = f"S-{numero:03d}"
    for seccion in (hallazgos, correcciones):
        assert any(candidato in fila and hallazgo in fila
                   for fila in seccion.splitlines()), candidato
for numero in range(1, 38):
    candidato = f"D2-{numero:02d}"
    identificador = {1: 30, 2: 28, 3: 29, 4: 31}.get(numero, numero + 27)
    hallazgo = f"S-{identificador:03d}"
    for seccion in (hallazgos, correcciones):
        assert any(candidato in fila and hallazgo in fila
                   for fila in seccion.splitlines()), candidato
asociaciones_r3 = {
    1: 100, 2: 66, 3: 65, 4: 65, 5: 65, 6: 104, 7: 105, 8: 106,
    9: 107, 10: 109, 11: 108, 12: 110, 13: 111, 14: 112, 15: 113, 16: 114,
}
for numero, identificador in asociaciones_r3.items():
    candidato = f"R3-{numero:02d}"
    hallazgo = f"S-{identificador:03d}"
    for seccion in (hallazgos, correcciones):
        assert any(re.search(rf"\b{candidato}\b", fila) and hallazgo in fila
                   for fila in seccion.splitlines()), candidato
assert "## Correcciones tras la revisión Opus" in revision
correcciones_opus = revision.split("## Correcciones tras la revisión Opus", 1)[1]
for numero in range(1, 15):
    candidato = f"O-{numero:02d}"
    assert any(f"| {candidato} |" in fila and
               re.search(r"\| aplicado(?: con cambios)? \||\| rechazado \|", fila)
               for fila in correcciones_opus.splitlines()), candidato
asociaciones_p6 = {
    1: (12,), 2: (1,), 3: (1,), 4: (10,), 5: (11,), 6: (5,),
    7: (5,), 8: (10,), 9: (12,), 10: (10,), 11: (11,), 12: (11,),
    13: (5, 11), 14: (2, 8), 15: (12,), 16: (2,), 17: (3, 9),
    18: (6, 9), 19: (3, 9), 20: (4,), 21: (7,), 22: (4,), 23: (4, 7),
}
respaldo_posterior = raiz / "auditoria_respaldo_20261026_200841" / "cambios.diff"
assert sum(linea.startswith("@@") for linea in respaldo_posterior.read_text().splitlines()) == 23
for numero, ids in asociaciones_p6.items():
    candidato = f"P6-{numero:02d}"
    assert any(f"| {candidato} |" in fila and
               all(f"O-{identificador:02d}" in fila for identificador in ids) and
               re.search(r"\| aplicado(?: con cambios)? \|", fila)
               for fila in correcciones_opus.splitlines()), candidato
assert "## Nota del supervisor" in revision
assert "## Estado de entrega" in revision
assert not re.search(r"^En revisión\.$", revision, re.M)
indice = (raiz / "S1_00_indice.md").read_text()
for numero in range(5):
    assert f"M{numero:02d}_libreto.md" in indice
assert indice.count("[PRÁCTICA — fase de ejercicios]") == 15
print("Entrega: 15 marcadores; C01–C27, D2-01–D2-37 y R3-01–R3-16 con hallazgo y corrección; O-01–O-14 con decisión; nota del orquestador presente; índice completo.")
