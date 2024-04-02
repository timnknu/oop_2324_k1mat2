class ElementExtractor: # iterator -- ітератор
    def __init__(self, maxn):
        self._index = 0
        self._max_n = maxn

    def __next__(self):
        #print('__next__ called from ElementExtractor')
        self._index += 1
        if self._index > self._max_n:
            raise StopIteration
        return self._index ** 2

class MyClass: # iteratable -- ітерований об'єкт
    def __init__(self, n):
        self._maxnum = n
    def __iter__(self):
        #print('__iter__ is called')
        itrobj = ElementExtractor(self._maxnum)
        return itrobj # має існувати itrobj.__next__()

if __name__ == "__main__":
    obj = MyClass(3)

    for el in obj: # b1 = iter(obj)
        for el2 in obj: # b2 = iter(obj)
            print(el, el2)

# iter() ; __iter__
# next() ; __next__

# iteratable -- ітерований об'єкт
# iterator -- ітератор
