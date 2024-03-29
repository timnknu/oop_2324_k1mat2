class Equation:
    INF_SOLS = (0, 0, 0, 0, 0)
    NO_SOLS = tuple()

    def __init__(self, b, c):
        self._b = b
        self._c = c
    def solve(self):
        # b*x + c = 0 => x = -c/b
        if self._b == 0:
            if self._c == 0:
                return Equation.INF_SOLS
            else:
                return Equation.NO_SOLS
        else:
            x = -self._c / self._b
            return (x,)
    #

#print(__name__)
if __name__ == "__main__":
    e = Equation(-2, -1)
    #e = Equation(-2, 0)
    #e = Equation(0, -1)
    #e = Equation(0, 0)
    r = e.solve()
    print(r, len(r))
