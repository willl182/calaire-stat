"""Inventario de trazabilidad; no sustituye el cotejo técnico de los archivos."""
from hashlib import sha256
from pathlib import Path

raiz = Path(__file__).resolve().parent
salida = "inventario_auxiliares_sol.tsv"
print("archivo\tbytes\tsha256\ttratamiento")
for archivo in sorted(raiz.rglob("*")):
    if not archivo.is_file() or archivo.name == salida:
        continue
    relativo = archivo.relative_to(raiz)
    carpeta = relativo.parts[0]
    if carpeta in {"referencias_12", "referencias_34"}:
        tratamiento = "histórico preservado; LEEME distingue evidencia vigente"
    elif carpeta == "referencias_00":
        tratamiento = "fuente M00 cotejada de nuevo; ver revisión"
    elif archivo.suffix == ".py":
        tratamiento = "script vigente; ver pruebas y límites en revisión"
    elif archivo.name.endswith("_salida_sol.txt"):
        tratamiento = "salida regenerada en reanudación"
    elif carpeta.startswith(("verificacion_", "verificar_")):
        tratamiento = "evidencia nueva; alcance específico en revisión"
    elif archivo.name == "informe_00.md":
        tratamiento = "informe anterior anotado con recomprobación actual"
    elif archivo.name == "fuentes_00_sha256.txt":
        tratamiento = "manifiesto anterior; nueve identidades recomprobadas"
    elif archivo.name == "entorno_sol.txt":
        tratamiento = "versiones de herramientas recomprobadas"
    else:
        tratamiento = "auxiliar documental; consultar revisión y procedencia"
    contenido = archivo.read_bytes()
    print(f"{relativo}\t{len(contenido)}\t{sha256(contenido).hexdigest()}\t{tratamiento}")
