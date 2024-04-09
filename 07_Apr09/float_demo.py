print(1.1 - 0.1 - 1.0)
print(1.1 - 1.0 - 0.1)

p = 15

for k in range(20):
    eps = 10.**(-k)
    val = ((1+eps)**p - 1) / eps
    print(k, eps, ':', val)