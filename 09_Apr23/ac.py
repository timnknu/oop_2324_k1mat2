from abc import ABCMeta, abstractmethod

class SequenceAnalyzer(metaclass=ABCMeta):
    @abstractmethod
    def terms_gen(self):
        pass
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
#


s = SinSeq()
s.print_minmax()