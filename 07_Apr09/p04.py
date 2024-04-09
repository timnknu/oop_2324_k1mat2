# D_n = b * D_(n-1) - c*a*D_(n-2)
# D_1 = b
# D_2 = b**2 - a*c

def Dgen(a, b, c):
    Dnm2 = b
    yield Dnm2 # D_1
    Dnm1 = b**2 - a*c
    yield Dnm1 # D_2

    while True:
        Dn = b * Dnm1 - a*c*Dnm2
        yield Dn
        Dnm2, Dnm1 = Dnm1, Dn


v = Dgen(2, 5, 3)
for k, elem in zip(range(10), v):
    print(k, ':', elem)
