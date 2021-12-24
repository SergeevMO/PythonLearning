# Двойной факториал
n = 11
f = 1

if n % 2 == 1:
    for i in range(1, n + 1, 2):
        f *= i
else:
    for i in range(2, n + 1, 2):
        f *= i

print(f)




print('\n')

# Calcualate n!! = 1.3.5.7...(n-2)n for odd n
n = 11
dfactorial = 1
for i in range(3, n+1, 2):
    dfactorial *= i
print('{:d}!! = {:d}'.format(n, dfactorial))

# Вариант для чётного двойного факториала
# Calcualate n!! = 2.4.6.8...(n-2)n for even n
import math
n = 10
dfactorial = 2**(n // 2) * math.factorial(n // 2)
print('{:d}!! = {:d}'.format(n, dfactorial))