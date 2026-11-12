"""Cuenta palabras de narración B+I: prosa fuera de tablas, citas (>), encabezados, fórmulas y código;
excluye apertura, revisión de tarea, prácticas, cierre y referencias."""
import re, sys
EXCL = re.compile(r"^#+ .*(Apertura|Revisión de la tarea|Práctica|PRÁCTICA|Cierre|Referencias|Ficha|Sesión)", re.I)
for f in sys.argv[1:]:
    skip, w = True, 0
    for line in open(f):
        if line.startswith("#"):
            if re.match(r"^## ", line): skip = bool(EXCL.match(line)) or not re.search(r"Nivel|Punto de partida", line)
            elif re.match(r"^###", line) and EXCL.match(line): skip_sub = True; skip_local = True
            if re.match(r"^###", line): skip_local = bool(EXCL.match(line))
            continue
        if skip or locals().get("skip_local") or line.lstrip().startswith(("|", ">")): continue
        t = re.sub(r"\$[^$]*\$|`[^`]*`|\[[^\]]*\]", " ", line)
        w += len(re.findall(r"\b\w+(?:[-’']\w+)*\b", t))
    print(f"{f}\t{w}\t{w/130:.1f}")
