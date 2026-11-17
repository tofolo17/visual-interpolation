import numpy as np
from matplotlib import pyplot as plt


class Spline:
    def __init__(self, x: list, y: list, t: str = 'cubic'):
        self.x = x
        self.y = y
        self.t = t

        self.solution = self.solve()

    def solve(self):
        if len(self.x) != len(self.y):
            raise Exception('The axes are not the same size.')
        if self.t == 'cubic':
            if len(self.x) < 3:
                raise Exception(
                    'You need three (or more) points to smooth the dataset with cubic interpolation.'
                )
            return self.__cubic_algorithm()
        return

    def plot(self):
        if self.t == 'cubic':
            self.__cubic_plot()

    def __cubic_algorithm(self):
        """
        References:
        https://faculty.ksu.edu.sa/sites/default/files/numerical_analysis_9th.pdf, página 167/895;
        https://en.wikipedia.org/wiki/Spline_(mathematics).
        """
        # Input
        x = self.x
        y = self.y
        n = len(self.x)

        # 1.
        a = [0] * n
        for i in range(n):
            a[i] = y[i]

        # 2.
        b = [0] * (n - 1)
        d = [0] * (n - 1)

        # 3.
        h = [0] * (n - 1)
        for i in range(n - 1):
            h[i] = x[i + 1] - x[i]

        # 4.
        alpha = [0] * (n - 1)
        for i in range(1, n - 1):
            alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (
                a[i] - a[i - 1]
            )

        # 5.
        c = [0] * n
        u = [0] * n
        z = [0] * n
        l_ = [0] * n

        # 6.
        l_[0] = 1

        # 7.
        for i in range(1, n - 1):
            l_[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1]
            u[i] = h[i] / l_[i]
            z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l_[i]

        # 8.
        l_[-1] = 1
        z[-1] = 0

        # 9.
        for j in range(n - 2, -1, -1):
            c[j] = z[j] - u[j] * c[j + 1]
            b[j] = (a[j + 1] - a[j]) / h[j] - (
                h[j] * (c[j + 1] + 2 * c[j])
            ) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

        # Output
        splines = []
        for i in range(n - 1):
            splines.append([a[i], b[i], c[i], d[i]])

        return splines

    def __cubic_plot(self):
        plt.plot(self.x, self.y, 'o')
        for i in range(len(self.solution)):
            f = self.solution[i]

            a = f[0]
            b = f[1]
            c = f[2]
            d = f[3]
            xi = self.x[i]

            x_ = np.linspace(xi, self.x[i + 1], 100)
            y_ = a + b * (x_ - xi) + c * (x_ - xi) ** 2 + d * (x_ - xi) ** 3
            plt.plot(x_, y_)

        plt.show()
