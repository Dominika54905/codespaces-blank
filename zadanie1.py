import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    y_interp = np.zeros(len(x_interp))
    for i in range(len(x_interp)):
        L = np.ones(n)
        for j in range(n):
            for k in range(n):
                if k != j:
                    L[j] *= (x_interp[i] - x[k]) / (x[j] - x[k])
        y_interp[i] = np.sum(y * L)
    return y_interp


x = np.linspace(-1, 1, 10)
y = np.sin(np.pi * x)
x_interp = np.linspace(-1, 1, 100)


y_interp = lagrange_interpolation(x, y, x_interp)


plt.plot(x_interp, y_interp, label='Interpolacja Lagrange\'a')
plt.scatter(x, y, c='r', label='Punkty interpolacji')
plt.legend()
plt.show()