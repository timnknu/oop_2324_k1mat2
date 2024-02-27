class Polynom:
    def __init__(self):
        self.__data = {}
    def read_form_file(self, file_name):
        self.__data = {}
        with open(file_name) as f:
            for line in f:
                rec = line.strip().split()
                if len(rec)>0:
                    assert len(rec)==2
                    try:
                        pwr = int(rec[0])
                    except:
                        print("Wrong power", rec[0])
                        continue
                    assert pwr >= 0
                    try:
                        coef = float(rec[1])
                    except:
                        print("Wrong coef", rec[1])
                        continue
                    assert pwr not in self.__data
                    self.__data[pwr] = coef
    #
    def show(self):
        print(self.__data)

obj = Polynom()
obj.read_form_file('input01.txt')
obj.show()