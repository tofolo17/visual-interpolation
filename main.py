def main():
    x = [5, 8, 23]
    y = [1, 2, 3]

    spline = Spline()
    spline.set_axis(x, y)

    spline.solve()


# Testing some error classes
class DifferentLength(Exception):
    def __init__(self, message="The axes are not the same size."):
        super().__init__(message)


class SmallLength(Exception):
    def __init__(
            self,
            message="You need three (or more) points to smooth the dataset with cubic spline interpolation."
    ):
        super().__init__(message)


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

    def solve(self, t: str = 'cubic'):
        if len(self.x_axis) != len(self.y_axis):
            raise DifferentLength
        if t == 'cubic':
            if len(self.x_axis) < 3:
                raise SmallLength

        n = len(self.x_axis)
        self._solver_algorithm()

    def _solver_algorithm(self):
        """
        References:
        https://faculty.ksu.edu.sa/sites/default/files/numerical_analysis_9th.pdf, página 167/895;
        https://en.wikipedia.org/wiki/Spline_(mathematics).
        """
        # arrays de tamanho n + 1
        x = self.x_axis
        y = self.y_axis
        n = len(self.x_axis)
        print(f'x: {x}\t| size: {n}')
        print(f'y: {y}\t| size: {n}')

        # 1. array a de tamanho n + 1
        a = [0] * n
        for i in range(n):
            a[i] = y[i]
        print(f'a: {a}\t| size: {len(a)}')

        # 2. arrays b e d de tamanho n
        b = [0] * (n - 1)
        d = [0] * (n - 1)
        print(f'b: {b}\t| size: {len(b)}')
        print(f'd: {d}\t| size: {len(d)}')

        # 3. array h de tamanho n
        h = [0] * (n - 1)
        for i in range(n - 1):
            h[i] = x[i + 1] - x[i]
        print(f'h: {h}\t| size: {len(h)}')

        # 4. array alpha de tamanho n
        alpha = [0] * (n - 1)
        for i in range(1, n - 1):
            alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])
        print(f'alpha: {alpha}\t| size: {len(alpha)}')

        # 5. 


main()
