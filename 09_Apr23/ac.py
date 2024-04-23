from abc import ABCMeta, abstractmethod

class SequenceAnalyzer(metaclass=ABCMeta):
    @abstractmethod
    def terms_gen(self):
        pass
    #
    def print_minmax(self):
        for el in self.terms_gen():
            k, ak = el
            print(k, ak)
            if k> 10:
                break

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