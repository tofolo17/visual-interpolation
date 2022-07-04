import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 1000)

y = np.piecewise(x, [x < 0, ((x >= 0) & (x <= 2)), x > 2], [lambda x: -x, lambda x: x, lambda x: x ** 2])

plt.plot(x, y, 'o')
plt.show()

# Usar 'piecewise' ou vários plots:
