import copy

class Vector:
    def __init__(self, n):
        if isinstance(n, Vector):
            self._data = copy.deepcopy(n._data)
        if isinstance(n, list):
            self._data = copy.deepcopy(n)
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
            assert len(self) == len(other)
            for i in range(len(self)):
                res[i] = self[i] + other[i]
            # альтернативна реалізація:
            #res = Vector(self)
            #for i in range(len(self._data)):
            #   res._data[i] += other._data[i]
            return res
        else:
            for i in range(len(self)):
                res[i] = self[i] + other
            return res
    def __getitem__(self, j):
        return self._data[j]
    def __setitem__(self, j, val):
        self._data[j] = val
    def __len__(self):
        return len(self._data)
    def __radd__(self, other):
        print('radd', other)
        return -100

#a = Vector(3)
#a[:] = [1,2,3]
a = Vector([7,8,9])
b = 1+ a
print(b)

# a._data[0] = 1.2
# b = a + 9

