e = {'a': 1.0, 'b': -2.0}
e['c'] = 0.5
def solve_eq(data):
    D = data['b'] ** 2 - 4 * data['a'] * data['c']
    if D > 0:
        x1 = (-data['b'] - D**0.5) / (2 * data['a'])
        x2 = (-data['b'] + D**0.5) / (2 * data['a'])
        print(x1, x2)
    else:
        print('No solution')

solve_eq(e)
