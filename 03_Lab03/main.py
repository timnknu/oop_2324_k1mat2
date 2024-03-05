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
        roots = []
        for t in r:
            if t>0:
                roots.append( t**0.5 )
                roots.append(- t ** 0.5)
            if t==0:
                roots.append(0)
            #
        return tuple(roots)
#

#e = BiQuadraticEquation(1, 2, -3) # (x**2 - 1)*(x**2 + 3) = 0
e = BiQuadraticEquation(1, 3, 0) # x**2*(x**2 + 3) = 0
#e = BiQuadraticEquation(1, -4, 3) # (x**2 - 1)*(x**2 - 3) = 0
#e = BiQuadraticEquation(1, -3, 0) # x**2*(x**2 - 3) = 0

#e = BiQuadraticEquation(1, 4, 3) # (x**2 + 1)*(x**2 + 3) = 0
#e = BiQuadraticEquation(0, 0, 0)
#e = BiQuadraticEquation(0, 1, -1) # x**2 - 1 = 0
r = e.solve()
print(r, len(r))

