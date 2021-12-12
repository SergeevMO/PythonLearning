# Треугольник Паскаля
import math

r_max = 50
long = 3

for i in range(0, r_max + 1):
    a = (r_max + 1 - i) * long // 2
    print(f"{' ':>{a}}", end='')
    for j in range(0, i + 1):
        n = math.factorial(i) // (math.factorial(i - j) * math.factorial(j))
        if n % 2:
            print(f'{"*":<{long}}', end='')
        else:
            print(f'{" ":<{long}}', end='')
    print()