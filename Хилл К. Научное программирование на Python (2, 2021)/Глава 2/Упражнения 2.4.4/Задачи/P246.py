# Двойной факториал
n = 10
f = 1

if n % 2 == 1:
    for i in range(1, n + 1, 2):
        f *= i
else:
    for i in range(2, n + 1, 2):
        f *= i

print(f)




print('\n')

# Вариант для чётного двойного факториала
import math
n = 10
dfactorial = 2**(n // 2) * math.factorial(n // 2)
print('{:d}!! = {:d}'.format(n, dfactorial))