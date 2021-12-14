# Формула Полиньяка для определения числа конечных нулей
n = 126
fn = 0

for i in range(1, n+1):
    fn += int(n / 5 ** i)

print(fn)



print('\n')
# Второй вариант
# Caculate the number of trailing zeros in n! using de Polignac's formula:
# nzeros = sum_i floor(n/5^i)
import math

n = 126

nzeros = 0
term = n
while True:
    term //= 5
    if term == 0:
        break
    nzeros += term

print('{:d}! ends in {:d} zeros.'.format(n, nzeros))
print('{:d}! = {:d}'.format(n, math.factorial(n)))