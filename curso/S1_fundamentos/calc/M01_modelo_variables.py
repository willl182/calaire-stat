#!/usr/bin/env python3
"""Reproduce the illustrative arithmetic used in M01."""

from math import log

# Illustrative indicated and reference values, in nmol/mol.
x_ref = 420.0
y_ind = 421.3
error = y_ind - x_ref
additive_correction = x_ref - y_ind

# Illustrative SRP model: alpha is in atm^-1 cm^-1 and L in cm;
# normalize c in atm by the declared standard pressure before conversion.
transmittance = 0.9864
alpha_old = 308.32
alpha_new = 304.39
path_cm = 90.0
standard_pressure_atm = 1.0
scale = 1e9
concentration_old = (
    -log(transmittance) / (alpha_old * path_cm) / standard_pressure_atm * scale
)
concentration_new = (
    -log(transmittance) / (alpha_new * path_cm) / standard_pressure_atm * scale
)
concentration_change = concentration_new - concentration_old
relative_change = concentration_change / concentration_old
alpha_ratio = alpha_old / alpha_new

# Two additional declared scale pairs from prop_e M1-I.
section_pair_ratio = 1.147 / 1.1329
absorption_pair_ratio = 308.32 / 304.39

# Numerical sensitivity for the illustrative model, holding the other inputs fixed.
transmittance_step = 0.0001
sensitivity_transmittance = (
    -log(transmittance + transmittance_step)
    / (alpha_new * path_cm)
    / standard_pressure_atm
    * scale
    - concentration_new
) / transmittance_step
alpha_step = 0.01
sensitivity_alpha = (
    -log(transmittance)
    / ((alpha_new + alpha_step) * path_cm)
    / standard_pressure_atm
    * scale
    - concentration_new
) / alpha_step

# Illustrative multiplicative scale model, in nmol/mol.
scale_factor = 1.0129
scale_levels = (100.0, 500.0)
scaled_results = tuple(scale_factor * value for value in scale_levels)
scale_errors = tuple(result - value for result, value in zip(scaled_results, scale_levels))
relative_errors = tuple(error / value for error, value in zip(scale_errors, scale_levels))

# Illustrative shared additive contribution and instrument-specific terms, in nmol/mol.
shared = 2.0
specific_1 = 0.3
specific_2 = -0.1
result_1 = shared + specific_1
result_2 = shared + specific_2
difference = result_1 - result_2

print(f"x_ref={x_ref:.6f} nmol/mol; y_ind={y_ind:.6f} nmol/mol")
print(f"error={error:.6f} nmol/mol; additive_correction={additive_correction:.6f} nmol/mol")
print(f"SRP old alpha={concentration_old:.9f} nmol/mol")
print(f"SRP new alpha={concentration_new:.9f} nmol/mol")
print(f"concentration_change={concentration_change:.9f} nmol/mol")
print(f"relative_change={100 * relative_change:.9f} %; scale_ratio={alpha_ratio:.9f}")
print(f"1.147/1.1329={section_pair_ratio:.9f}; increment={(section_pair_ratio - 1) * 100:.9f} %")
print(f"308.32/304.39={absorption_pair_ratio:.9f}; increment={(absorption_pair_ratio - 1) * 100:.9f} %")
print(f"sensitivity_T={sensitivity_transmittance:.9f} nmol/mol per unit T")
print(f"sensitivity_alpha={sensitivity_alpha:.9f} nmol/mol per (atm^-1 cm^-1)")
for level, result, err, relative in zip(scale_levels, scaled_results, scale_errors, relative_errors):
    print(f"scale x={level:.6f}: y={result:.6f}; e={err:.6f} nmol/mol; e/x={100 * relative:.6f} %")
print(f"shared example: Y1={result_1:.6f}; Y2={result_2:.6f}; delta={difference:.6f} nmol/mol")
