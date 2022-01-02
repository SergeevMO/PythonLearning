import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-20, stop=20, num=10000)
print(len(x))

y1 = np.log(1/np.cos(x)**2)
y2 = np.log(np.sin(x)**(-2))

plt.plot(x, y1)
plt.plot(x, y2)
plt.savefig("L:\Обучение Python\Хилл К. Научное программирование на Python (2, 2021)\Глава 3\Упражнения 3.1.3\grap.png")

plt.show()
print("all")

# Пики не равной высоты из-за того, что значения по оси дискретны
# и по разному отличаются от точных значений, кратных числу пи и 0.