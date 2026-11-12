"""Reproduce los ejemplos numéricos didácticos de M03 (datos simulados)."""
from math import sqrt
import numpy as np
from scipy.stats import t, norm

# Especificaciones interpretadas como intervalos y distribuciones declaradas.
h = 0.3
rect_h = h / sqrt(3)
delta = 0.1
rect_resolution = delta / sqrt(12)
triangular_h = h / sqrt(6)
u_from_U = 0.60 / 2.0

# Lecturas: desviación estándar y error estándar del promedio independiente.
s_reading = 0.8
n = 16
sem_independent = s_reading / sqrt(n)

# Modelo con efecto común y ruido de lectura independiente.
u_common = 0.3
u_random = 0.8
u_mean_with_common = sqrt(u_common**2 + u_random**2 / n)

# Deriva B3: serie determinista; los residuos NO son una muestra iid.
# Tiempo en minutos, una lectura por minuto. Pendiente conocida por construcción.
drift_time = np.arange(16, dtype=float)
drift_beta = 0.05
drift_residual = np.tile([-0.8, 0.8, 0.8, -0.8], 4)
drift_y = 420.0 + drift_beta * drift_time + drift_residual
drift_halves = drift_y.reshape(2, 8).mean(axis=1)
drift_blocks = drift_y.reshape(4, 4).mean(axis=1)
drift_corrected_zero = drift_y - drift_beta * drift_time
drift_corrected_center = drift_y - drift_beta * (drift_time - 7.5)
drift_naive_sem = np.std(drift_y, ddof=1) / sqrt(16)
drift_residual_sem = np.std(drift_corrected_zero, ddof=1) / sqrt(16)
assert np.allclose(drift_halves, [420.175, 420.575])
assert np.allclose(drift_blocks, [420.075, 420.275, 420.475, 420.675])
assert np.isclose(drift_blocks.mean(), drift_y.mean())
assert np.isclose(drift_halves[1] - drift_halves[0], 0.4)
assert np.allclose(drift_corrected_zero.reshape(4, 4).mean(axis=1), 420.0)
assert np.isclose(drift_corrected_center.mean(), 420.375)

# Dos resultados con ruido parcialmente compartido; covariance = rho*u1*u2.
u1, u2, rho = 0.8, 0.6, 0.75
cov = rho * u1 * u2
u_sum_independent = sqrt(u1**2 + u2**2)
u_sum_correlated = sqrt(u1**2 + u2**2 + 2 * cov)
u_diff_correlated = sqrt(u1**2 + u2**2 - 2 * cov)

# Un ciclo hipotético: X=0 dentro de banda, X=1 fuera de banda (B1).
p_out_of_band = 0.1
probability_zero_out = 1 - p_out_of_band
probability_one_out = p_out_of_band
assert np.isclose(probability_zero_out + probability_one_out, 1.0)
z_score = (421.6 - 420.0) / 0.8
degrees_freedom = 5 - 1
student_975_df4 = t.ppf(0.975, degrees_freedom)
normal_975 = norm.ppf(0.975)
chi_square_two_df2 = 1**2 + (-1)**2
f_ratio_example = (6 / 3) / (4 / 2)

assert np.isclose(u_mean_with_common**2, u_common**2 + sem_independent**2)

for label, value in [
    ("rectangular_semiamplitud_h", rect_h),
    ("rectangular_resolucion_delta", rect_resolution),
    ("triangular_semiamplitud_h", triangular_h),
    ("u_desde_U_sobre_k", u_from_U),
    ("s_lectura", s_reading),
    ("error_estandar_n_independiente", sem_independent),
    ("u_promedio_con_componente_comun", u_mean_with_common),
    ("covarianza_dos_variables", cov),
    ("u_suma_suponiendo_independencia", u_sum_independent),
    ("u_suma_con_correlacion", u_sum_correlated),
    ("u_diferencia_con_correlacion", u_diff_correlated),
    ("probabilidad_cero_fuera_de_banda", probability_zero_out),
    ("probabilidad_una_fuera_de_banda", probability_one_out),
    ("puntaje_estandar_z", z_score),
    ("grados_libertad_muestra", degrees_freedom),
    ("cuantil_t_975_df4", student_975_df4),
    ("cuantil_normal_975", normal_975),
    ("chi_cuadrado_suma_1y_menos1_df2", chi_square_two_df2),
    ("cociente_F_ejemplo", f_ratio_example),
]:
    print(f"{label}={value:.10g}")
print(f"deriva_tiempos_min={drift_time.tolist()}")
print(f"deriva_residuos_declarados={drift_residual.tolist()}")
print(f"deriva_lecturas={drift_y.tolist()}")
print(f"deriva_medias_mitades={drift_halves.tolist()}")
print(f"deriva_medias_bloques={drift_blocks.tolist()}")
print(f"deriva_media_global={drift_y.mean():.10g}")
print(f"deriva_s_sobre_raiz_n_no_validado={drift_naive_sem:.10g}")
print(f"deriva_medias_bloques_corregidos_t0={drift_corrected_zero.reshape(4, 4).mean(axis=1).tolist()}")
print(f"deriva_media_corregida_t0={drift_corrected_zero.mean():.10g}")
print(f"deriva_media_corregida_t7_5={drift_corrected_center.mean():.10g}")
print(f"deriva_residuos_s_sobre_raiz_n_no_validado={drift_residual_sem:.10g}")
print("comprobaciones_M03=OK")
