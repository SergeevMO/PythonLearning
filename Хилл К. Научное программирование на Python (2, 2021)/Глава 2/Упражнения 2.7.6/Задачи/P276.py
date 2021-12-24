# Интеграл синуса и косинуса в целых степенях
import math

def doble_factorial(n):
    f = 1

    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            f *= i
    else:
        for i in range(2, n + 1, 2):
            f *= i
    return f


def sinm_cosn(m, n):
    if m > 0 and n > 0:
        a1 = doble_factorial(m - 1)
        a2 = doble_factorial(n - 1)
        a3 = doble_factorial(n + m)
        r = a1 * (a2 / a3)
        if m % 2 == 0 and n % 2 == 0:
            return r * math.pi / 2
        return r


for m in range(1, 10):
    for n in range(1, 10):
        print(n, m, sinm_cosn(m, n))


