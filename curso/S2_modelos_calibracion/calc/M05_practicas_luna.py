"""Cálculos reproducibles para las prácticas B, I y A de M05.

Los valores simulados son didácticos y no describen resultados de CALAIRE.
"""
from itertools import product
import random
from math import sqrt

from scipy.stats import nct, t


def plan_power():
    delta, tau, sigma, alpha = 0.20, 0.20, 0.10, 0.05
    print("Planificación simulada de potencia (delta,tau,sigma nmol/mol):",
          delta, tau, sigma)
    for days, readings in ((4, 12), (6, 8)):
        sd_day = sqrt(tau**2 + sigma**2 / readings)
        noncentrality = delta * sqrt(days) / sd_day
        critical = t.ppf(1 - alpha / 2, days - 1)
        power = (nct.cdf(-critical, days - 1, noncentrality)
                 + nct.sf(critical, days - 1, noncentrality))
        print(f"{days} días × {readings} lecturas: total={days*readings}, "
              f"sd_media_día={sd_day:.4f}, potencia={power:.3f}")


def factorial():
    rows = []
    for f, c, t in product((-1, 1), repeat=3):
        e = (0.20 + 0.40*f + 0.10*c - 0.05*t + 0.15*f*c
             + 0.02*f*t - 0.01*c*t + 0.04*f*c*t)
        rows.append((f, c, t, e))
    print("Tabla factorial simulada (F,C,T,e nmol/mol):")
    for f, c, t, e in rows:
        print(f, c, t, f"{e:.2f}".replace("-", "−").replace(".", ","))
    for name, idx in (("F", 0), ("C", 1), ("T", 2)):
        high = sum(r[3] for r in rows if r[idx] == 1) / 4
        low = sum(r[3] for r in rows if r[idx] == -1) / 4
        print(f"Efecto marginal {name}, alto-bajo: {high-low:.2f}".replace("-", "−").replace(".", ","), "nmol/mol")
    conditional_f = {}
    for c in (-1, 1):
        dif = (sum(r[3] for r in rows if r[0] == 1 and r[1] == c) / 2
               - sum(r[3] for r in rows if r[0] == -1 and r[1] == c) / 2)
        conditional_f[c] = dif
        print(f"Efecto F con C={c:+d}: {dif:.2f}".replace(".", ",").replace("-", "−"), "nmol/mol")
    interaction_fc = (conditional_f[1] - conditional_f[-1]) / 2
    difference_fc = conditional_f[1] - conditional_f[-1]
    simple_f = next(r[3] for r in rows if r[:3] == (1, 1, 1)) - next(
        r[3] for r in rows if r[:3] == (-1, 1, 1))
    for label, value in (("Interacción F×C (convención I2)", interaction_fc),
                         ("Diferencia de efectos simples F×C", difference_fc),
                         ("Contraste simple F con C alto y T alto", simple_f)):
        print(f"{label}: {value:.2f}".replace(".", ","), "nmol/mol")
    names = {0: "F", 1: "C", 2: "T"}
    print("Todos los contrastes simples (alto−bajo, condicionados a los otros dos factores):")
    for idx in (0, 1, 2):
        others = [i for i in range(3) if i != idx]
        for fixed in product((-1, 1), repeat=2):
            low = next(r[3] for r in rows if r[idx] == -1 and (r[others[0]], r[others[1]]) == fixed)
            high = next(r[3] for r in rows if r[idx] == 1 and (r[others[0]], r[others[1]]) == fixed)
            value = high - low
            flag = " (supera 0,50)" if abs(value) > 0.50 + 1e-9 else ""
            print(f"  {names[idx]} | {names[others[0]]}={fixed[0]:+d}, {names[others[1]]}={fixed[1]:+d}: "
                  f"{f'{value:.2f}'.replace('.', ',').replace('-', '−')} nmol/mol{flag}")
    treatments = [(f, c, t, rep) for f, c, t in product((-1, 1), repeat=3)
                  for rep in (1, 2)]
    random.Random(20261027).shuffle(treatments)
    print("Orden aleatorio reproducible (semilla 20261027):")
    for i, treatment in enumerate(treatments, start=1):
        print(i, treatment)


def design_counts():
    print("Diseño B: registros totales=12*8*6=", 12 * 8 * 6)
    print("Diseño B: concentración=10*8*6=", 10 * 8 * 6)
    print("Diseño B: cero=2*8*6=", 2 * 8 * 6)
    analysts, days, cycles, readings = 3, 4, 2, 8
    print("Diseño A base:", analysts, "analistas;", analysts*days, "días;",
          analysts*days*cycles, "ciclos;",
          analysts*days*cycles*readings, "lecturas")
    print("gl por estrato:", analysts-1, analysts*(days-1),
          analysts*days*(cycles-1), analysts*days*cycles*(readings-1))
    print("Diseño A seis analistas:", 6, 6*days, 6*days*cycles,
          6*days*cycles*readings, "gl analista:", 6-1)
    one_reading = 1
    alt_days = 6 * days
    alt_cycles = alt_days * cycles
    alt_readings = alt_cycles * one_reading
    alt_df = (6 - 1, 6 * (days - 1), alt_days * (cycles - 1),
              alt_cycles * (one_reading - 1))
    print("Diseño A seis analistas, una lectura/ciclo:", 6, alt_days,
          alt_cycles, alt_readings, "gl por estrato:", *alt_df)
    print("Estrato lectura dentro de ciclo: 0 gl; ciclo y lectura no se separan")
    operators, days_per_operator, results_per_day = 2, 2, 2
    nested = operators * days_per_operator * results_per_day
    stages = (("repetibilidad", 2), ("otro día, mismo analista", 1),
              ("otro día y otro analista", 1))
    stepwise = sum(n for _, n in stages)
    print(f"Diseño escalonado ISO 5725-3: {stepwise} resultados vs {nested} "
          f"totalmente anidados; ahorro={nested - stepwise} "
          f"({(nested - stepwise) / nested:.0%})")
    print("Secuencia escalonada (publicada):",
          "; ".join(f"{n} {label}" for label, n in stages))


if __name__ == "__main__":
    plan_power()
    design_counts()
    factorial()
