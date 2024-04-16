class ProtectedDictInt:
    def __init__(self):
        self._data = {}
    def __str__(self):
        return str(self._data)
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        if isinstance(key, int):
            # в key -- ціле число => це допутисмий ключ
            self._data[key] = value
        else:
            print('помилка')

d = ProtectedDictInt()

d[1] = 12.0
d[2.0] = -100500
print('---')
print(d)