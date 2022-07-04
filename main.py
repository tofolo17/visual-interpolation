from random import randint

import matplotlib.pyplot as plt
import numpy as np

from Classes import *


def main():
    size = randint(3, 20)
    x = sorted([randint(-100, 100) for _ in range(size)])
    y = [randint(-100, 100) for _ in range(size)]

    spline = Spline(x, y)
    solution = spline.solution

    plt.plot(x, y, 'o')
    for i in range(len(solution)):
        f = solution[i]

        a = f[0]
        b = f[1]
        c = f[2]
        d = f[3]
        xi = x[i]

        x_ = np.linspace(xi, x[i + 1], 100)
        y_ = a + b * (x_ - xi) + c * (x_ - xi) ** 2 + d * (x_ - xi) ** 3
        plt.plot(x_, y_)

    plt.show()


main()
