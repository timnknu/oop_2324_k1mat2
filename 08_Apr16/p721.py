import traceback

class ProtectedDictIntError(KeyError):
    def __init__(self, a):
        super().__init__(a)
        self._useful_info = a
    def __str__(self):
        s = f"ключ {self._useful_info} не був цілим значенням"
        return s

class ProtectedDictInt:
    def __init__(self):
        self._data = {}
    def __str__(self):
        return str(self._data)
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        if isinstance(key, int):
        # if type(key) is int: # альтернативна перевірка
            # в key -- ціле число => це допутисмий ключ
            self._data[key] = value
        else:
            obj = ProtectedDictIntError(key)
            raise obj

d = ProtectedDictInt()

#d[2.0] = -100500

try:
    d[1] = 12.0
    d[2.0] = -100500 #/0
    print('---')
except ProtectedDictIntError as e:
    print('виникла помилка', e)
    s = traceback.format_exc()
    print('---')
    print(e._useful_info)
    print(e.__traceback__.tb_lineno)
    print('---')
    print('старе повідомлення про помилку -', s)
    pass
except ZeroDivisionError:
    print('Ділити на нуль не можна!')

print(d)