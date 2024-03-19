class Vector:
    def __init__(self, n):
        if isinstance(n, Vector):
            self._data = n._data
        else:
            assert type(n) is int
            assert n>0
            self._data = [0.0]*n

a = Vector(3)

x = [1,2,3]
y = x
y[0] = -100
print(x)