from constants import *
from sympy.solvers import solve


def straight(enter: str):
    enter = enter.replace(' ', '')
    if '=' in enter:
        enter = enter[:enter.index('=')] + '-(' + enter[enter.index('=')+1:] + ')'
    elif 'y' not in enter:
        enter += '-y'
    else:
        enter += '-x'

    print(enter)
    for char in '0123456789':
        enter = enter.replace(char + 'x', char + '*x')
        enter = enter.replace('x' + char, 'x*' + char)
        enter = enter.replace(char + 'y', char + '*y')
        enter = enter.replace('y' + char, 'y*' + char)
        enter = enter.replace(char + '(', char + '*(')
        enter = enter.replace(')' + char, ')*' + char)
        enter = enter.replace(char + '(', char + '*(')
        enter = enter.replace(')' + char, ')*' + char)
    enter = enter.replace('xy', 'x*y')
    enter = enter.replace('yx', 'y*x')
    enter = enter.replace('xx', 'x*x')
    enter = enter.replace('yy', 'y*y')
    enter = enter.replace(')(', ')*(')

    return enter


def get_roots(enter: str):
    enter = straight(enter)
    Y_roots = []
    X_roots = []
    Y = solve(enter, [y, x])
    X = solve(enter, [x, y])

    print(Y, X)
    if type(Y) == dict:
        Y = [(enter.replace('y', '0'), x)]
        X = []

    if Y and Y[0][1] == x:
        Y_roots = [str(root[0]) for root in Y]
    if X and X[0][1] == y:
        X_roots = [str(root[0]) for root in X]

    print(Y_roots, X_roots)
    return Y_roots, X_roots
