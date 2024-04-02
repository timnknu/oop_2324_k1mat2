class MyClass:
    def __iter__(self):
        print('__iter__ is called')
        #return ...
        pass

if __name__ == "__main__":
    obj = MyClass()

    for el in obj: # b = iter(obj)
        print(el)


# iter() ; __iter__
# next() ; __next__
# iteratable -- ітерований об'єкт
# iterator -- ітератор
