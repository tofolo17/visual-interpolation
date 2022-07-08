tfrom abc import ABC, abstractmethod

import numpy as np
import pygame

from pyg.constants import *


class Interpolation(ABC):
    def __init__(self, dots):
        self.dots = dots
        self.coordinates = None

    def render(self, screen):
        self.coordinates = self.dots.coordinates
        self.draw(screen)

    @abstractmethod
    def draw(self, screen):
        pass


class Linear(Interpolation):
    def __init__(self, dots):
        super().__init__(dots)

    def draw(self, screen):
        for i in range(1, len(self.coordinates)):
            pygame.draw.line(screen, WHITE, self.coordinates[i - 1], self.coordinates[i])


class Curve(Interpolation, ABC):
    def __init__(self, dots):
        super().__init__(dots)
        self.x_axis = None
        self.y_axis = None
        self.solution = None

    def draw(self, screen):
        try:

            if len(self.coordinates) >= 2:
                self.x_axis = [point[0] for point in self.coordinates]
                self.y_axis = [point[1] for point in self.coordinates]
                self.solution = self.solve()

                for i in range(len(self.solution)):
                    rays = self.get_rays(i)
                    pygame.draw.lines(screen, PURPLE, False, rays, 1)

        except ZeroDivisionError:
            pass

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def get_rays(self, i):
        pass


class Spline(Curve):
    def __init__(self, dots):
        super().__init__(dots)

    def solve(self):
        return self.__cubic_algorithm()

    def get_rays(self, i):
        f = self.solution[i]

        a = f[0]
        b = f[1]
        c = f[2]
        d = f[3]
        xi = self.x_axis[i]

        x = np.linspace(xi, self.x_axis[i + 1], 100)
        y = a + b * (x - xi) + c * (x - xi) ** 2 + d * (x - xi) ** 3

        position = []
        for j in range(SEGMENTS):
            position.append((x[j], y[j]))

        return position

    def __cubic_algorithm(self):
        """
        References:
        https://faculty.ksu.edu.sa/sites/default/files/numerical_analysis_9th.pdf, página 167/895;
        https://en.wikipedia.org/wiki/Spline_(mathematics).
        """
        # Input
        x = self.x_axis
        y = self.y_axis
        n = len(x)

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
            splines.append([a[i], b[i], c[i], d[i]])

        return splines


class Lagrange:
    pass
