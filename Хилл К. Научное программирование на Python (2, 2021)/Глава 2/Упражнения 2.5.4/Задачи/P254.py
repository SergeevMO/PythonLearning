# Метод Герона для вычисления квадратного корня
import math

S = 2_117_519.73

xn = 2000
dx = -1

while dx != 0:
    xn1 = 0.5 * (xn + S / xn)
    dx = int((xn1 - xn) * 100)
    print(xn, xn1)
    xn = xn1

print(xn1 - math.sqrt(S))



print('\n')

#
TOL = 0.01
S = 2117519.73
x_old = 2000
while True:
    x_new = (x_old + S / x_old) / 2
    if abs(x_new - x_old) < TOL:
        break
    x_old = x_new

print("sqrt({}) by Hero's method: {:.2f}".format(S, x_new))

import math
print('Compare with the "exact" answer:', math.sqrt(S))