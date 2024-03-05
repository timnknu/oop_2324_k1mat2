from linear_eq import Equation
from quadr_eq import QuadraticEquation

class BiQuadraticEquation(QuadraticEquation):
    def solve(self):
        r = super().solve()
        if r == Equation.NO_SOLS:
            return Equation.NO_SOLS
        if r == Equation.INF_SOLS:
            return Equation.INF_SOLS
        #
        for t in r:
            print(t)


e = BiQuadraticEquation(1, 2, -3) # (x**2 - 1)*(x**2 + 3) = 0
r = e.solve()
#print(r, len(r))

