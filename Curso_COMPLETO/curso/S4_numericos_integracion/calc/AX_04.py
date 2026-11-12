from math import sqrt
D, n, s_between, s_r = 4, 3, 0.20, 0.30
v_between, v_repeat = s_between**2/D, s_r**2/(D*n)
v = v_between + v_repeat
print(f'v_entre={v_between:.9g}; v_repetibilidad={v_repeat:.9g}; u2={v:.9g}; u={sqrt(v):.9g}; u_sin_entre={sqrt(v_repeat):.9g}')
