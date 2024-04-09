def etgen(x, eps):
    a = 1.0
    yield a
    n = 1
    while a > eps:
        a = a * x/n
        n += 1
        yield a
#
x = 0.12
v = etgen(x, 1e-5)
s = 0
for k, el in enumerate(v):
    s += el
    print(k, ':', el)
print('sum is', s)

