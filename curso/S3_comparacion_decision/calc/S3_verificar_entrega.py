"""Comprueba estructura de la entrega sin modificar archivos."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    "PIZARRA", "DIAPOSITIVA", "MATERIAL", "PREGUNTA AL GRUPO", "PAUSA",
    "EJEMPLO", "PRÁCTICA — fase de ejercicios", "ERROR CRÍTICO",
    "ESCALAMIENTO", "TRANSICIÓN", "NOTA AL INSTRUCTOR",
}


def main():
    total = 0
    for number in range(9, 13):
        path = ROOT / f"M{number:02d}_libreto.md"
        text = path.read_text()
        markers = re.findall(r"^> \*\*\[PRÁCTICA — fase de ejercicios\]\*\* .+$", text, re.M)
        assert len(markers) == 3, (path.name, "marcadores", len(markers))
        for level in "BIA":
            section = re.search(rf"^## Nivel {level}[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
            assert section, (path.name, level)
            assert section.group(1).count("[PRÁCTICA — fase de ejercicios]") == 1
        labels = re.findall(r"^> \*\*\[([^\]]+)\]\*\*", text, re.M)
        assert set(labels) <= ALLOWED, (path.name, set(labels) - ALLOWED)
        for heading in ("## Ficha del capítulo", "## Cierre del capítulo", "## Referencias del capítulo"):
            assert heading in text, (path.name, heading)
        assert not any(ord(c) < 32 and c not in "\n\t\r" for c in text), path.name
        total += len(markers)
        scenes = re.findall(r"^### Escena .+$", text, re.M)
        print(f"{path.name}: {len(scenes)} escenas; 3 marcadores; niveles y etiquetas conformes")
    print(f"Total: {total} prácticas pendientes, sin desarrollar en este control estructural.")
    print("Este control no sustituye la revisión semántica de contenido y referencias.")


if __name__ == "__main__":
    main()
