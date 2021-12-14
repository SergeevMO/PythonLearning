# Мультипликативная функция Эйлера
n = 100

for i in range(1, n):
    nip = 0
    for j in range(1, i + 1):
        a, b = i, j
        while b:
            a, b = b, a % b
        if a == 1:
            nip += 1
            #print(i, j)
    print(f'Функция Эйлера \u03C6({i}) = {nip}')
