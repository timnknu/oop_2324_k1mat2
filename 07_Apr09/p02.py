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
k = 0
b = zip([1,2], ['A', 'X', '?'])
for elem in b:
    print(elem)
# for el in v:
#     k += 1
#     if k > 10:
#         break
#     print(el)
#
