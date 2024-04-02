class ElementExtractor:
    def __init__(self):
        self._index = 0
    def __next__(self):
        print('__next__ called from ElementExtractor')
        self._index += 1
        if self._index > 10:
            raise StopIteration
        return self._index ** 2

class MyClass:
    def __iter__(self):
        print('__iter__ is called')
        itrobj = ElementExtractor()
        return itrobj # має існувати itrobj.__next__()

if __name__ == "__main__":
    obj = MyClass()

    for el in obj: # b1 = iter(obj)
        print(el)

    for el2 in obj: # b2 = iter(obj)
        print(el2)

# iter() ; __iter__
# next() ; __next__

# iteratable -- ітерований об'єкт
# iterator -- ітератор
