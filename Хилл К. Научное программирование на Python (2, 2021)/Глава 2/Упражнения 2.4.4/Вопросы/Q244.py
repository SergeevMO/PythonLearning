# Ряд Мадхавы-Лейбница
import math

n = 20
pi_value_plus = 0
pi_value_minus = 0

for i in range(n):
    if (i+1)%2 != 0:
        pi_value_plus += 1 / ((1+2*i) * 3**i)
        print(i, 'p', pi_value_plus)
    else:
        pi_value_minus += 1 / ((2*i+1) * 3**i)
        print(i, 'n', pi_value_minus)

pi_value_n = math.sqrt(12) * (pi_value_plus - pi_value_minus)

print(pi_value_n)
print(pi_value_n - math.pi)



# второй вариант - учитывает нечётность функции возведения в степень числа 3
pi = 0
for k in range(20):
    pi += pow(-3, -k) / (2*k+1)

pi *= math.sqrt(12)
print('pi = ', pi)
print('error = ', pi - math.pi)