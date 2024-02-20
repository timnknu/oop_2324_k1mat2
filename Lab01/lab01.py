

class QuadraticEquation:
    def show(self):
        print(self.a, self.b)

    def solve_eq(data):
        D = data.b ** 2 - 4 * data.a * data.c
        if D > 0:
            x1 = (-data.b - D**0.5) / (2 * data.a)
            x2 = (-data.b + D**0.5) / (2 * data.a)
            print(x1, x2)
        else:
            print('No solution')

eq = QuadraticEquation()
eq.a = 1.0
eq.b =-2.0
eq.c = 0.5
eq.solve_eq()
