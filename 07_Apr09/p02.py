def etgen(x):
    a = 1.0
    yield a
    n = 1
    while True:
        a = a * x/n
        n += 1
        yield a
#
x = 0.12
N = 10
v = etgen(x)
for el in v:
    print(el)