"""Contraste independiente de la identidad descriptiva O-02 con Decimal."""
from decimal import Decimal, getcontext

getcontext().prec = 40
x = list(map(Decimal, ['199.8', '199.8', '200', '200', '200.2', '200.2']))
y = list(map(Decimal, ['200', '199.9', '199.9', '200.1', '200.5', '200.3']))
e = [yi - xi for xi, yi in zip(x, y)]


def covariance(a, b):
    mean_a, mean_b = sum(a) / len(a), sum(b) / len(b)
    return sum((ai - mean_a) * (bi - mean_b)
               for ai, bi in zip(a, b)) / (len(a) - 1)


terms = [covariance(x, x), covariance(e, e), 2 * covariance(x, e)]
variance_y = covariance(y, y)
assert abs(sum(terms) - variance_y) < Decimal('1e-35')
assert terms[0] == Decimal('0.032')
assert terms[2] == Decimal('0.008')
print('O-02: varianzas referencia/error/término cruzado =', terms)
print('O-02: varianza indicación =', variance_y)
print('O-02: porcentajes descriptivos =', [100 * value / variance_y for value in terms])
print('O-02: desviación referencia =', terms[0].sqrt())
print('Contraste Decimal independiente: OK')
