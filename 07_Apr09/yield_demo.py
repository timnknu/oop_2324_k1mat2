def f():
    for k in range(10):
        yield k**2
    # tmpl = 3.14
    # print('A', tmpl)
    # yield -15
    # print('B', tmpl)
    # yield -54
    # print('С', tmpl)
    # yield 100500
    # print('D', tmpl)

v = f()

print(v)
for elem in v:
    print(elem)

# b = iter(v)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
