
def f():
    #....1
    #....2
    yield -15
    #....3

v = f()
print(v)
for nm in dir(v):
    print(nm)
