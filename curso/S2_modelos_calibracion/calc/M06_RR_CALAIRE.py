"""Reproduce resúmenes del estudio R&R con medias diarias del libro CALAIRE.

Origen de entrada: docs/Resultados R&r_2022 2023 (1).xlsx, hojas por nivel.
El cálculo conserva tres bloques de seis días por analista y no empareja días entre analistas.
La asignación de los bloques a campañas requiere confirmación en el libro.
Ejecutar con curso/.venv/bin/python desde la raíz del repositorio.
"""
from pathlib import Path

import numpy as np
import openpyxl
from scipy.stats import f

ROOT = Path(__file__).resolve().parents[3]
BOOK = ROOT / "docs" / "Resultados R&r_2022 2023 (1).xlsx"
LEVELS = [45, 90, 135, 180, 225, 270, 315, 360, 405, 455]


def nested_anova(x):
    """Balanced analyst-by-block decomposition; days nested in cell."""
    # x shape: analyst, block, day
    a, c, d = x.shape
    grand = x.mean()
    mean_a = x.mean(axis=(1, 2))
    mean_c = x.mean(axis=(0, 2))
    mean_ac = x.mean(axis=2)
    ss_a = c * d * np.sum((mean_a - grand) ** 2)
    ss_c = a * d * np.sum((mean_c - grand) ** 2)
    ss_ac = d * np.sum((mean_ac - mean_a[:, None] - mean_c[None, :] + grand) ** 2)
    ss_day = np.sum((x - mean_ac[:, :, None]) ** 2)
    df_a, df_c, df_ac, df_day = a - 1, c - 1, (a - 1) * (c - 1), a * c * (d - 1)
    ms_a, ms_c, ms_ac, ms_day = ss_a/df_a, ss_c/df_c, ss_ac/df_ac, ss_day/df_day
    return {
        "F_analyst": ms_a/ms_ac,
        "F_interaction": ms_ac/ms_day,
        "F_block": ms_c/ms_ac,
        "MS_day": ms_day,
        "MS_interaction": ms_ac,
        "Fcrit_analyst": f.ppf(0.95, df_a, df_ac),
        "Fcrit_interaction": f.ppf(0.95, df_ac, df_day),
        "s_day": np.sqrt(ms_day),
    }


def main():
    wb = openpyxl.load_workbook(BOOK, data_only=True, read_only=True)
    results = []
    for level in LEVELS:
        ws = wb[f"{level}ppb"]
        rows = list(ws.iter_rows(min_row=6, max_row=23, min_col=2, max_col=3, values_only=True))
        data = np.asarray(rows, dtype=float).reshape(3, 6, 2).transpose(2, 0, 1)
        result = nested_anova(data)
        results.append((level, result))
        print(level, " ".join(f"{key}={value:.6f}" for key, value in result.items()))
        if level in (405, 455):
            print(f"{level}_block_means_by_analyst=", np.round(data.mean(axis=2), 6).tolist())
    analyst = [r["F_analyst"] for _, r in results]
    interactions = [(level, r["F_interaction"]) for level, r in results]
    day_sd = [r["s_day"] for _, r in results]
    print("max_F_analyst=", f"{max(analyst):.6f}")
    print("significant_interactions=", [level for level, value in interactions if value > results[0][1]["Fcrit_interaction"]])
    print("interaction_range_selected=", [round(value, 6) for level, value in interactions if level in (135, 360, 405, 455)])
    print("s_day_range=", f"{min(day_sd):.6f}", f"{max(day_sd):.6f}")


if __name__ == "__main__":
    main()
