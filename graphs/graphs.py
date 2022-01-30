from constants import *
from random import randint


def get_graph(roots, ax):
    color = (randint(1, 10) / 10, randint(1, 10) / 10, randint(1, 10) / 10)
    x = np.arange(-100, 100, 0.0001)
    for root in roots[0]:
        y = eval(root)
        try:
            if 'I' not in root:
                y[:-1][abs(np.diff(y)) > 10 ** 4] = np.nan
                ax.plot(x, y, color=color)
        except TypeError:
            ax.axhline(y, color=color)
    y = np.arange(-100, 100, 0.0001)
    for root in roots[1]:
        x = eval(root)
        try:
            if 'I' not in root:
                x[:-1][abs(np.diff(x)) > 10 ** 4] = np.nan
                ax.plot(x, y, color=color)
        except TypeError:
            ax.axvline(x, color=color)
