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

a = Vector(3)
print(a)