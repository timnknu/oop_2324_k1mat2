class MyClass:
    def __init__(self, n):
        self._maxnum = n
        self._index  = 0
    def __iter__(self):
        return self
    def __next__(self):
        self._index += 1
        if self._index > self._maxnum:
            raise StopIteration
        return self._index ** 2

if __name__ == "__main__":
    obj = MyClass(5)

    for el in obj: # b1 = iter(obj)
        for el2 in obj: # b2 = iter(obj)
            print(el, el2)

# iter() ; __iter__
# next() ; __next__

# iteratable -- ітерований об'єкт
# iterator -- ітератор
