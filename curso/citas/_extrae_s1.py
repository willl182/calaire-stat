from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = [ROOT / "curso" / "S1_fundamentos" / f"M{i:02d}_libreto.md" for i in range(5)]
CITATION = re.compile(r"\[([^\[\]]*(?:GUM|VIM|ISO|EN 14625|NIST|NISTIR|CFR50|BIPM|Hahs|Crowder|MMU|ASQ|Otto|Lakens|Milton|statsmodels|SciPy|prop_e|AX\.)[^\[\]]*)\]", re.I)

def main():
    for path in CHAPTERS:
        lines = path.read_text(encoding="utf-8").splitlines()
        for number, line in enumerate(lines, 1):
            for match in CITATION.finditer(line):
                print(f"{path.relative_to(ROOT)}\t{number}\t{match.group(1)}")

if __name__ == "__main__":
    main()
