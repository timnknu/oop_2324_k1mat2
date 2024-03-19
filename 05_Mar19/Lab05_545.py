import copy

class Vector:
    def __init__(self, n):
        if isinstance(n, Vector):
            self._data = copy.deepcopy(n._data)
        else:
            assert type(n) is int
            assert n>0
            self._data = [0.0]*n
    def __str__(self):
        #s = '{'
        s = str(self._data)
        return s
    def __add__(self, other):
        if isinstance(other, Vector):
            assert len(self._data) == len(other._data)
            res = Vector(len(self._data))
            for i in range(len(self._data)):
                res._data[i] = self._data[i] + other._data[i]
            return res

a = Vector(3)
b = a + 1
print(b)