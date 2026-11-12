# Ejemplo AX.1: muestra simulada 2, 4, 6.
x = [2.0, 4.0, 6.0]
n = len(x)
mean = sum(x) / n
ss = sum((v - mean) ** 2 for v in x)
print(f'media={mean:g}; suma_cuadrados={ss:g}; s2={ss/(n-1):g}; s={((ss/(n-1))**0.5):g}; nu={n-1}')
print(f'varianza_divisor_n={ss/n:.9g}')
