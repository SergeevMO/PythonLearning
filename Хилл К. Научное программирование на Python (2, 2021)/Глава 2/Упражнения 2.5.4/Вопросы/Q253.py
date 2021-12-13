# Игра FizzBuzz
num_list = []
n_max = 100

for i in range(1, n_max+1):
    s = ''
    if not i % 3:
        s += 'Fizz'
    if not i % 5:
        s += 'Buzz'
    if s == '':
        s = str(i)
    num_list.append((i, s))

for pair in num_list:
    print(pair)