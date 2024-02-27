class Polynom:
    def __init__(self):
        self.__data = {}
    def _process_line(self, line):
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
                self._process_line( line.strip() )
    #
    def read_from_keyboard(self):
        self.__data = {}
        print("Input powers & coefs, or empty line to stop")
        while True:
            s = input()
            if s == "":
                break
            self._process_line( s )

    #
    def show(self):
        print(self.__data)

    def evaluate_at_x(self, x):
        result = 0
        for pwr, cf in self.__data.items():
            result += x**pwr * cf
        return result



obj = Polynom()
obj.read_form_file('input01.txt')
#obj.read_from_keyboard()
r = obj.evaluate_at_x(0.5)
print(r)
#obj.show()