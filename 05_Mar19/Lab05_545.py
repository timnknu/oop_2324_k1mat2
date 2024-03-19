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
        res = Vector(len(self._data))
        if isinstance(other, Vector):
            assert len(self._data) == len(other._data)
            for i in range(len(self._data)):
                res._data[i] = self._data[i] + other._data[i]
            # альтернативна реалізація:
            #res = Vector(self)
            #for i in range(len(self._data)):
            #   res._data[i] += other._data[i]
            return res
        else:
            for i in range(len(self._data)):
                res._data[i] = self._data[i] + other
            return res
    def __getitem__(self, j):
        print('getting item', j)
        return -100

a = Vector(3)
print(a[0:100:2])

# a._data[0] = 1.2
# b = a + 9
