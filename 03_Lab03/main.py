from linear_eq import Equation

class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self._a = a
        super().__init__(b, c)
    #
    def solve(self):
        if self._a == 0:
            return super().solve()
        else:
            D = self._b ** 2 - 4 * self._a * self._c
            if D > 0:
                x1 = (-self._b - D**0.5) / (2 * self._a)
                x2 = (-self._b + D**0.5) / (2 * self._a)
                return (x1, x2)
            elif abs(D) < 1e-10:
                x = (-self._b) / (2 * self._a)
                return (x, )
            else:
                return Equation.NO_SOLS



#e = QuadraticEquation(1, -4, -3)
e = QuadraticEquation(1, -2, 1)
r = e.solve()
print(r, len(r))

