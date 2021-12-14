# Последовательность чисел-градин. Гипотеза Коллатца.
# а)
n = 27

print(n)
while n != 1:
    if n % 2:
        n = 3 * n + 1
    else:
        n = int(n / 2)
    print(n)



print('*'*70)
# б1)
n = 27
i = 1

while n != 1:
    if n % 2:
        n = 3 * n + 1
    else:
        n = int(n / 2)
    i += 1
print(i)



print('*'*70)
# б2)
for j in range(1, 101):
    n, i = j, 1
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n = int(n / 2)
        i += 1
    print(f'для {j} = {i}')

