import math

numeric_tuple = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'запятая')
num_tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
z = zip(num_tuple, numeric_tuple)
z_list = list(z)

pi_str = str(math.pi)[:10]

for s in pi_str:
    for n, w in z_list:
        if s == n:
            print(w, end=' ')
print()



# Вариант № 2
num = ('nought', 'one', 'two', 'three', 'four', 'five',
       'six', 'seven', 'eight', 'nine')
print('three point ', end='')
for i in str(math.pi)[2:10]:
    print(num[int(i)], end=' ')
print()