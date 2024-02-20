class QuadraticEquation:
    def __init__(self, coef_a, coef_b = None, coef_c = None):
        if isinstance(coef_a, QuadraticEquation):
            self.a = coef_a.a
            self.b = coef_a.b
            self.c = coef_a.c
        else:
            self.a = coef_a
            self.b = coef_b
            self.c = coef_c

    def show(self):
        print(f'({self.a}) * x**2 + ({self.b}) * x + ({self.c}) = 0')

    def solve_eq(self):
        assert self.a != 0 # перевірка, чи дійсно рівняння квадратне
        D = self.b ** 2 - 4 * self.a * self.c
        if D > 0:
            x1 = (-self.b - D**0.5) / (2 * self.a)
            x2 = (-self.b + D**0.5) / (2 * self.a)
            return [x1, x2]
        elif abs(D) < 1e-10:
            x = (-self.b) / (2 * self.a)
            return [x]
        else:
            return []

eq = QuadraticEquation(1.0, -2.0, 1.0) # 1 sol
second_eq = QuadraticEquation(1.0, -3.0, 1.5) # 2 sol
third_eq = QuadraticEquation(1.0, -3.0, 10.5)  # 0 sol
cloned_equation = QuadraticEquation(eq)


for obj in [eq, second_eq, third_eq, cloned_equation]:
    s = obj.solve_eq()
    if len(s) == 1:
        obj.show()
        print(s)

