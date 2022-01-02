# Уравнение Михаэлиса-Ментен
import numpy as np
import matplotlib.pyplot as plt

Km1 = 0.004 # M
Km2 = 0.04 # M
Km3 = 0.4 # M
Vmax = 0.1 # M/c

s = np.linspace(start=0, stop=5, num=10000)
v1 = Vmax * s / (Km1 + s)
v2 = Vmax * s / (Km2 + s)
v3 = Vmax * s / (Km3 + s)

plt.plot(s, v1)
plt.plot(s, v2)
plt.plot(s, v3)
plt.savefig("L:\Обучение Python\Хилл К. Научное программирование на Python (2, 2021)\Глава 3\Упражнения 3.1.3\Mihael-Menten.png")
plt.show()