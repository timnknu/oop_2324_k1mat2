import math

def etgen(x, eps):
    a = 1.0
    yield a
    n = 1
    while a > eps:
        a = a * x/n
        n += 1
        yield a
#
x = 10.12
v = etgen(x, 1e-5)
s = sum(v)
print('sum is', s)
print(math.exp(x))