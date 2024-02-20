class QuadraticEquation:
    def __init__(self, coef_a, coef_b, coef_c):
        self.a = coef_a
        self.b = coef_b
        self.c = coef_c
    def solve_eq(self):
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

eq = QuadraticEquation(1.0, -2.0, 0.5)
s = eq.solve_eq()
print(s)

second_eq = QuadraticEquation(1.0, -3.0, 1.5)
s = second_eq.solve_eq()
print(s)
