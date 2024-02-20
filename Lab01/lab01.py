class QuadraticEquation:
    def show(self):
        print(self.a, self.b)

    def set_coefs(self, coef_a, coef_b, coef_c):
        self.a = coef_a
        self.b = coef_b
        self.c = coef_c

    def solve_eq(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D > 0:
            x1 = (-self.b - D**0.5) / (2 * self.a)
            x2 = (-self.b + D**0.5) / (2 * self.a)
            print(x1, x2)
        else:
            print('No solution')

eq = QuadraticEquation()
eq.a = 1.0
eq.b = -2.0
eq.c = 0.5
eq.solve_eq()

second_eq = QuadraticEquation()
second_eq.set_coefs(1.0, -3.0, 1.5)
second_eq.solve_eq()
