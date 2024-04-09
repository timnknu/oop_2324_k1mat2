x = 0.12
a = 1.0
N = 10
for n in range(1, N+1):
    tmp = a * x/n
    a = tmp
    print(n, a)