class ElementExtractor:
    def __next__(self):
        print('__next__ called from ElementExtractor')
        return -10

class MyClass:
    def __iter__(self):
        print('__iter__ is called')
        itrobj = ElementExtractor()
        return itrobj # має існувати itrobj.__next__()

if __name__ == "__main__":
    obj = MyClass()

    for el in obj: # b = iter(obj)
        print(el)


# iter() ; __iter__
# next() ; __next__

# iteratable -- ітерований об'єкт
# iterator -- ітератор
