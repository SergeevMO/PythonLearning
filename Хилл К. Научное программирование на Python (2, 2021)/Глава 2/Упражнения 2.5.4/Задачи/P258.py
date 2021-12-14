# Решето Эратосфена - алгоритм для поиска простых чисел
num = 10000

n_list = list(range(2, num))
p_list = []

for i, n in enumerate(n_list):
    k = 1
    for p in range(2, int((n + 1) / 2 + 1)):
        if not n % p:
            k += 1
            if k > 1:
                break
    else:
        p_list.append(n)

print(p_list)
print(len(p_list))



print('*'*74)
# Второй вариант (правильный алгоритм Эратосфена)
n = 10000

# isprime - это массив булевых значений, которые равны True, если их индексы являются простыми числами
isprime = [True]*n
isprime[0] = isprime[1] = False     # 0 and 1 are not considered prime

print('[', end='')
# Start with the first prime, 2
#isprime[2] = True
for i, prime in enumerate(isprime):
    if prime:
        # We've found a prime: print it and mark its multiples as composite
        print(i, end=', ')
        for m in range(i, n, i):
            isprime[m] = False
print()