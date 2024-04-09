x = 0.12
N = 10

def etgen():
    a = 1.0
    yield a
    for n in range(1, N+1):
        a = a * x/n
        yield a

v = etgen()
for el in v:
    print(el)