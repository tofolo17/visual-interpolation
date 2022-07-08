from Modules.interpolation import *


def main():
    x = [1000, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 2000]
    y = [0, 0.01, 0.03, 0.08, 0.2, 0.4, 0.67, 0.85, 0.93, 0.97, 1.0]

    spline = Spline(x, y)

    spline.plot()


main()
