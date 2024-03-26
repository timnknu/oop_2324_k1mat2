import copy

class Vector:
    SEP = ','
    def __init__(self, n):
        if isinstance(n, Vector):
            self._data = copy.deepcopy(n._data)
        elif isinstance(n, list):
            self._data = copy.deepcopy(n)
        else:
            assert type(n) is int
            assert n>0
            self._data = [0.0]*n
    def __str__(self):
        comp_list = map(str, self._data)
        s = self.SEP.join(comp_list)
        return '{' + s + '}'
    def __add__(self, other):
        res = copy.deepcopy(self)
        if isinstance(other, Vector):
            assert len(self) == len(other)
            for i in range(len(self)):
                res[i] += other[i]
            # альтернативна реалізація:
            #res = Vector(self)
            #for i in range(len(self._data)):
            #   res._data[i] += other._data[i]
            return res
        else:
            for i in range(len(self)):
                res[i] += other
            return res
    def __getitem__(self, j):
        return self._data[j]
    def __setitem__(self, j, val):
        self._data[j] = val
    def __len__(self):
        return len(self._data)
    def __radd__(self, other):
        #return self.__add__(other)
        return self + other
    def __mul__(self, other):
        res = copy.deepcopy(self)
        assert (type(other) is int or type(other) is float)
        for i in range(len(self)):
            res[i] *= other
        return res
    def __rmul__(self, other):
        return self * other

class Matrix(Vector):
    SEP = '\n'
    def __init__(self, n):
        super().__init__(n)
    def __call__(self, a):
        print(a)
        return -100

row1 = Vector([7,8,9])
row2 = Vector([1,2,3])
row3 = Vector([-2,1,0])
m = Matrix([row1, row2, row3])

result = m('he')
print(result)
