# Подсолнечник
import numpy as np
import matplotlib.pyplot as plt

n = 1000
phi = (1 + np.sqrt(5)) / 2 # Золотое сечение
k = 2*np.pi / phi

s = np.linspace(0, n-1, n)
r = np.sqrt(s)
theta = k * s

plt.polar(theta, r, marker='o', linestyle='', markersize=5, markeredgecolor='k', color="tab:orange")
plt.show()