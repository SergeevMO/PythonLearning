# Параллельные реакции первого порядка
import numpy as np
import matplotlib.pyplot as plt

k1 = 300 # c-1
k2 = 100 # c-1
A0 = 2 # моль*дм-3

k = k1 + k2
max_t = 10000 / k # мс

t = np.linspace(start=0, stop=max_t, num=1001)
#print(x)


A = A0 * np.exp(-k*t / 1000)
B = (k1 / k) * A0 * (1 - np.exp(-k*t / 1000))
C = (k2 / k) * A0 * (1 - np.exp(-k*t / 1000))

plt.plot(t, A, label="реагент А")
plt.plot(t, B, label="продукт B")
plt.plot(t, C, label="продукт C")

plt.title("Кинетика первого порядка с параллельными реакциями", fontsize=12)
plt.xlabel("Время, мс", fontsize=15)
plt.ylabel("концентрация, моль/дм3", fontsize=15)
# '$\mathrm{concentration}\;/\mathrm{mol\,dm^{-3}}$'
plt.legend(loc=0, fontsize=11)

plt.xlim([0, 20])
plt.ylim([0, 2.1])
plt.savefig("L:\Обучение Python\Хилл К. Научное программирование на Python (2, 2021)\Глава 3\Упражнения 3.2.3\keenetic")
plt.show()