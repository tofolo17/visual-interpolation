from Errors import *


class Interpolation:
    def __init__(self):
        self.x_axis = list()
        self.y_axis = list()

    def set_axis(self, x: list, y: list):
        self.x_axis = x
        self.y_axis = y


class Spline(Interpolation):
    def __init__(self):
        super().__init__()
        self.__solution = None

    @property
    def solution(self):
        if self.__solution is None:
            self.solve()
        return self.__solution

    def solve(self, t: str = 'cubic'):
        if len(self.x_axis) != len(self.y_axis):
            raise DifferentLength
        if t == 'cubic':
            if len(self.x_axis) < 3:
                raise SmallLength

        self.__solution = self._solver_algorithm()

    def _solver_algorithm(self):
        """
        References:
        https://faculty.ksu.edu.sa/sites/default/files/numerical_analysis_9th.pdf, página 167/895;
        https://en.wikipedia.org/wiki/Spline_(mathematics).
        """
        # Input
        x = self.x_axis
        y = self.y_axis
        n = len(self.x_axis)

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
            alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

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
            b[j] = (a[j + 1] - a[j]) / h[j] - (h[j] * (c[j + 1] + 2 * c[j])) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

        # Output
        splines = []
        for i in range(n - 1):
            splines.append([a[i], b[i], c[i], d[i], x[i]])

        return splines
