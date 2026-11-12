u1, nu1, u2, nu2 = .30, 5., .40, 20.
u2c = u1**2 + u2**2
den = u1**4/nu1 + u2**4/nu2
print(f'u2c={u2c:.9g}; denominator={den:.9g}; nu_eff={u2c**2/den:.9g}')
