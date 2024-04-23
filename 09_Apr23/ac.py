from abc import ABCMeta, abstractmethod
import math

# інтерфейс
class Evaluatable(metaclass=ABCMeta):
    @abstractmethod
    def eval(self, x):
        pass

class SequenceAnalyzer(Evaluatable, metaclass=ABCMeta):
    @abstractmethod
    def terms_gen(self):
        pass
    #
    def __str__(self):
        sr = "First elements are:\n"
        for j, (k, ak) in enumerate(self.terms_gen()):
            if j > 10:
                break
            sr += f"a_{k} = {ak}\n"
        return sr
    #
    def print_minmax(self):
        max_val = None # ініціалізація одним способом
        for j, (k, ak) in enumerate(self.terms_gen()):
            if max_val is None or ak > max_val:
                max_val = ak
            if j==0:
                min_val = ak # ініціалізація іншим способом
            if ak < min_val:
                min_val = ak
            if j > 10:
                break
        print("min =", min_val)
        print("max =", max_val)
    #
    def eval(self, x):
        eps = 1e-5  # те саме, що і 10**(-5)
        sm = 0
        for k, ak in self.terms_gen():
            term = ak * x ** k
            if abs(term) < eps:
                break
            sm += term
        return sm


class SinSeq(SequenceAnalyzer):
    def terms_gen(self):
        a = 1
        n = 1
        yield (n, a)
        while True:
            a = - a / (n+1) / (n+2)
            n += 2
            yield (n, a)
        #
    #
class CosSeq(SequenceAnalyzer):
    def terms_gen(self):
        a = 1
        n = 0
        yield (n, a)
        while True:
            a = - a / (n+1) / (n+2)
            n += 2
            yield (n, a)
        #
    #
#

def print_table(objs, a=0, b=1, npoints=10):
    s = (b-a) / (npoints-1)
    # x[1] == a
    # x[2] == a + s
    # x[3] == a + 2s
    # ...
    # x[npoints] == a + s*(npoints-1)  == b => s = (b-a)/(npoints-1)
    for i in range(1, npoints + 1):
        x = a + (i-1)*s
        print(f"x_{i} = {x} ->", end='')
        for f in objs:
            print(f.eval(x), end=' | ')
        print()
#


class ExactSin(Evaluatable):
    def eval(self, x):
        return math.sin(x)

class ExactCos(Evaluatable):
    def eval(self, x):
        return math.cos(x)

c = CosSeq()
#s = SequenceAnalyzer()
#print(s)
print(c.eval(1.0))
print(math.cos(1.0))
print('---')
print_table([c, ExactCos()], a=-1, b=1)

#
# s = SinSeq()
# print(s.eval(1.0))
# print(math.sin(1.0))