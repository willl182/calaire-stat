"""Cálculos de las prácticas M09; datos simulados definidos en el propio script."""
import math

# B: dos puntos independientes; valores simulados y factor común declarado.
B = [(80.00, 80.30, 0.20, 0.15), (420.00, 419.60, 0.60, 0.50)]
k = 2.0
for x, y, u1, u2 in B:
    delta = y - x
    U1, U2 = k*u1, k*u2
    den = math.hypot(U1, U2)
    print(f"B x={x:.2f} y={y:.2f} delta={delta:.6f} u_delta={math.hypot(u1,u2):.6f} U1={U1:.6f} U2={U2:.6f} En={delta/den:.6f} clasifica={abs(delta/den)<=1}")

# I: misma entrada común R y componentes independientes residuales.
uR, c1, c2 = 0.15, 1.0, 0.8
u1, u2, delta_I = 0.20, 0.15, 0.35
var1, var2 = u1*u1, u2*u2
res1 = var1-(c1*uR)**2
res2 = var2-(c2*uR)**2
cov = c1*c2*uR*uR
var_delta = var1+var2-2*cov
assert res1 >= 0 and res2 >= 0
assert abs(cov) <= u1*u2
assert var_delta >= 0
u_delta = math.sqrt(var_delta)
U_delta = 2*u_delta
print(f"I delta={delta_I:.6f} var_residuales=({res1:.6f},{res2:.6f}) cov={cov:.6f} var_delta={var_delta:.6f} u_delta={u_delta:.9f} U_k2={U_delta:.9f} delta_over_U={delta_I/U_delta:.9f} sin_cov={delta_I/(2*math.hypot(u1,u2)):.9f}")

# A: grado de equivalencia simulado frente a BIPM-SRP27.
# La sensibilidad usa una covarianza positiva hipotética de la mitad del máximo admisible.
A = [(80, 80.30, 80.00, 0.20, 0.15), (420, 421.10, 420.20, 0.70, 0.40)]
for nom, yp, yr, up, ur in A:
    D = yp-yr
    cov_max = up*ur
    for label, cov_A in (("nula", 0.0), ("media_admisible", 0.5*cov_max)):
        var_D = up*up+ur*ur-2*cov_A
        assert abs(cov_A) <= cov_max
        assert var_D >= 0
        ud = math.sqrt(var_D)
        print(f"A nominal={nom} hipotesis={label} D={D:.6f} cov={cov_A:.6f} uD={ud:.9f} U_k2={2*ud:.9f} D_over_U={D/(2*ud):.9f}")
