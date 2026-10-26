"""Reproduce ejemplos didácticos simulados del capítulo M05."""
from itertools import product


def main():
    # Ilustración inicial de una respuesta y un contraste simulados.
    repeated_readings = (0.30, 0.35, 0.40, 0.40, 0.45, 0.50, 0.40, 0.40)
    low_condition = (0.10, 0.20, 0.30)
    high_condition = (0.70, 0.80, 0.90)
    print("Media de ocho lecturas dentro de una condición:",
          f"{sum(repeated_readings)/len(repeated_readings):.2f} nmol/mol")
    low_mean = sum(low_condition) / len(low_condition)
    high_mean = sum(high_condition) / len(high_condition)
    print("Medias simuladas por condición:", f"baja={low_mean:.2f}, alta={high_mean:.2f} nmol/mol")
    print("Diferencia simulada entre condiciones:",
          f"{high_mean - low_mean:.2f} nmol/mol")

    # Conteo estructural del certificado F-PSMT-01.
    levels, readings_per_point, days_certificate = 12, 8, 6
    print("Conteo 12 × 8 × 6 del diseño F-PSMT-01:",
          levels*readings_per_point*days_certificate)
    target_slope_change = 0.005
    print("Cambio de pendiente objetivo planteado en prop_e:", target_slope_change)

    # Diseño factorial 2^3; respuesta simulada en nmol/mol.
    # Factores codificados: flujo F, acondicionamiento C, temperatura T.
    rows = []
    for f, c, t in product((-1, 1), repeat=3):
        y = 0.20 + 0.40*f + 0.10*c - 0.05*t + 0.15*f*c + 0.02*f*t - 0.01*c*t + 0.04*f*c*t
        rows.append((f, c, t, y))
    effects = {
        "flujo": sum(f*y for f, c, t, y in rows) / 4,
        "acondicionamiento": sum(c*y for f, c, t, y in rows) / 4,
        "temperatura": sum(t*y for f, c, t, y in rows) / 4,
        "flujo×acondicionamiento": sum(f*c*y for f, c, t, y in rows) / 4,
        "flujo×temperatura": sum(f*t*y for f, c, t, y in rows) / 4,
        "acondicionamiento×temperatura": sum(c*t*y for f, c, t, y in rows) / 4,
        "flujo×acondicionamiento×temperatura": sum(f*c*t*y for f, c, t, y in rows) / 4,
    }
    print("2^3 combinaciones:", len(rows))
    print("Corridas con dos repeticiones independientes por combinación:", 2 * len(rows))
    print("Efectos (diferencia de medias nivel + menos nivel -), nmol/mol:")
    for name, coefficient in effects.items():
        print(f"  {name}: {coefficient:.3f}")

    # Precisión simulada del promedio bajo el modelo de AX.4.
    s_between, s_r = 0.20, 0.10
    print("\nIncertidumbre estándar simulada del promedio de errores (nmol/mol):")
    for days_precision, readings_precision in ((6, 8), (6, 16), (12, 8)):
        u_mean = (s_between**2 / days_precision
                  + s_r**2 / (days_precision * readings_precision)) ** 0.5
        print(f"  d={days_precision}, n={readings_precision}: {u_mean:.3f}")

    # Ejemplo simulado de reparto: 3 o 6 analistas, 4 días por analista,
    # 2 ciclos independientes por día y 8 lecturas subordinadas por ciclo.
    days, cycles, readings = 4, 2, 8
    print("\nDiseño R&R simulado:")
    for analysts in (3, 6):
        print(f"{analysts} analistas: {analysts*days} días, "
              f"{analysts*days*cycles} ciclos, "
              f"{analysts*days*cycles*readings} lecturas;")
        print(f"  niveles independientes del factor analista: {analysts}")
        print(f"  lecturas subordinadas por día: {cycles*readings}")


if __name__ == "__main__":
    main()
