# Центрированная гауссова функция
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-7, 7, 10000)
s1, s2, s3 = 1, 1.5, 2

y1 = (s1*np.sqrt(2*np.pi))**(-1) * np.exp(-x**2 / (2*s1**2))
y2 = (s2*np.sqrt(2*np.pi))**(-1) * np.exp(-x**2 / (2*s2**2))
y3 = (s3*np.sqrt(2*np.pi))**(-1) * np.exp(-x**2 / (2*s3**2))

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()