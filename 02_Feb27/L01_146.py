class Polynom:
    def __init__(self):
        self.__data = {}
    def process_line(self, line):
        rec = line.split()
        if len(rec) > 0:
            assert len(rec) == 2
            try:
                pwr = int(rec[0])
            except:
                print("Wrong power", rec[0])
                return
            assert pwr >= 0
            try:
                coef = float(rec[1])
            except:
                print("Wrong coef", rec[1])
                return
            assert pwr not in self.__data
            self.__data[pwr] = coef

    def read_form_file(self, file_name):
        self.__data = {}
        with open(file_name) as f:
            for line in f:
                self.process_line( line.strip() )

    #
    def show(self):
        print(self.__data)

obj = Polynom()
obj.read_form_file('input01.txt')
obj.show()