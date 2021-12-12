# Игра FizzBuzz
num_list = []

for i in range(1, 101):
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