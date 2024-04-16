import traceback

class ProtectedDictIntGeneralError(KeyError):
    def __init__(self, a):
        super().__init__(a)
        self._useful_info = a
    def __str__(self):
        s = f"ключ {self._useful_info} є помилковим"
        return s

class NonIntegerKeyError(ProtectedDictIntGeneralError):
    def __str__(self):
        s = f"ключ {self._useful_info} із NonIntegerKeyError"
        return s

class KeyAlreadyExistsError(ProtectedDictIntGeneralError):
    def __str__(self):
        s = f"ключ {self._useful_info} із KeyAlreadyExistsError"
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
                raise KeyAlreadyExistsError(key)
        else:
            raise NonIntegerKeyError(key)

d = ProtectedDictInt()

try:
    d[1] = 12.0
    #d[2.0] = -100500 #/0
    d[1] = -8
    print('---')
except NonIntegerKeyError as e:
    print('помилка:', e)
except KeyAlreadyExistsError as e:
    print('негаразд:', e)




print(d)