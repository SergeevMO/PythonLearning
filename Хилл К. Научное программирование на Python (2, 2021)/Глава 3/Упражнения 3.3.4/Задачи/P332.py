# Потенциал Леннарда-Джонса
import numpy as np
import matplotlib.pyplot as plt

A = 1.024e-23 # Дж×нм6
B = 1.582e-26 # Дж×нм12

# а)
r = np.linspace(0.1, 1.0, 10001)
#r = rx * 1e-9
Ur = B * r**(-12) - A * r**(-6)
Fr = 12 * B * r**(-13) - 6 * A * r**(-7)

line1 = plt.plot(r, Ur, color='r', label="U(r)")
plt.ylabel("потенциал, Дж")
plt.xlim(0.3, 0.8)
plt.ylim(-2e-21, 2e-21)

plt.twinx()
line2 = plt.plot(r, Fr, color='g', label="F(r)")
plt.ylabel("сила, Н*нм")
plt.xlim(0.3, 0.8)
plt.ylim(-0.15e-19, .25e-19)

lines = line1 + line2

labels = list()

for line in lines:
    labels.append(line.get_label())

plt.legend(lines, labels)

plt.show()


# б) гармонический осциллятор
r0 = (2 * B / A)**(1/6)
e = B * r0**(-12) - A * r0**(-6)
k = 156 * B * r0**(-14) - 42 * A * r0**(-8)
print(r0, e, k)

line1 = plt.plot(r, Ur, color='r', label="U(r)")
plt.ylabel("потенциал ЛД, Дж")


Vr = 0.5 * k * (r - r0)**2 + e
line3 = plt.plot(r, Vr, color='b', label="V(r)")
plt.ylabel("потенциал гармонический")
plt.xlim(0.3, 0.6)
plt.ylim(-1.7e-21, 0.5e-21)

lines = line1 + line3
labels = list()

for line in lines:
    labels.append(line.get_label())

plt.legend(lines, labels)
plt.show()
