import copy
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

    # 'getter' для коефіцієнтів
    def get_coef(self, pwr):
        #return self._data.get(pwr, 0.0)
        if pwr in self.__data:
            return self.__data[pwr]
        else:
            return 0.0

    # setter for coefs
    def set_coefs(self, coefs_dict):
        assert isinstance(coefs_dict, dict)
        self.__data = coefs_dict.copy()

    def get_powers(self):
        return self.__data.keys()

    @staticmethod
    def add(p1, p2):
        r = {}
        powers1 = p1.get_powers()
        powers2 = p2.get_powers()
        for pw in set(powers1) | set(powers2):
            cf = p1.get_coef(pw) + p2.get_coef(pw)
            r[pw] = cf
        rslt = Polynom()
        rslt.set_coefs(r)
        return rslt
    #


obj = Polynom()
obj.read_form_file('input01.txt')

second_term = Polynom()
second_term.read_form_file('input02.txt')

r = Polynom.add(obj, second_term)
r.show()