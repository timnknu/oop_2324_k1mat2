import traceback

class ProtectedDictIntError(KeyError):
    ERR_NONINT_KEY = 1
    ERR_EXISTING_KEY = 2

    def __init__(self, err_type, a):
        super().__init__(a)
        self._useful_info = a
        self._err_typ = err_type
    def __str__(self):
        if self._err_typ == self.ERR_EXISTING_KEY:
            s = f"ключ {self._useful_info} уже існує"
        elif self._err_typ == self.ERR_NONINT_KEY:
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
            if key not in self._data:
                self._data[key] = value
            else:
                raise ProtectedDictIntError(ProtectedDictIntError.ERR_EXISTING_KEY, key)
        else:
            obj = ProtectedDictIntError(ProtectedDictIntError.ERR_NONINT_KEY, key)
            raise obj

d = ProtectedDictInt()

#d[2.0] = -100500

try:
    d[1] = 12.0
    d[2.0] = -100500 #/0
    d[1] = -8
    print('---')
except ProtectedDictIntError as e:
    print('виникла помилка', e)
    #s = traceback.format_exc()
    #print('---')
    #print(e._useful_info)
    #print(e.__traceback__.tb_lineno)
    #print('---')
    #print('старе повідомлення про помилку -', s)
except ZeroDivisionError:
    print('Ділити на нуль не можна!')

print(d)