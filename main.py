from Classes import *


def main():
    x = [1, 2, 3, 4]
    y = [5, 8, 25, 2]

    spline = Spline()
    spline.set_axis(x, y)

    spline.solve()

    print(spline.solution)


main()
