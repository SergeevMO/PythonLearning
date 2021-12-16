# Метод Монте-Карло для определения числа пи
import math
import random

# Первый вариант
n = 10000000
i = 0
s = 0

while i != n:
    x = random.random()
    y = random.random()

    if y <= math.sqrt(1 - x ** 2):
        s += 1

    i += 1

s /= n
pi = 4 * s
print(pi, '\n', pi - math.pi)



print('*'*74)
# Второй вариант
n = 10000000
i = 0
s = 0

while i != n:
    x = random.random()

    s += math.sqrt(1 - x ** 2)

    i += 1

s /= n
pi = 4 * s
print(pi, '\n', pi - math.pi)