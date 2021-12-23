# а) добавить return
def line():
    return '-----'

my_sum = '\n'.join([' 56', ' +44', line(), ' 100', line()])
print('a\n', my_sum)


# б) правильно
def line():
    return '-----'

my_sum = '\n'.join([' 56', ' +44', line(), ' 100', line()])
print('б\n', my_sum)


# в) поставить вызовы функции
def line():
    return '-----'

my_sum = '\n'.join([' 56', ' +44', line(), ' 100', line()])
print('в\n', my_sum)


# г) Вызвать функцию после её определения и убрать из неё печать информации о функции
print('г')
def line():
    print('-----')
    print(' 56')
    print(' +44')
    #print(line)
    print(' 100')
    #print(line)
line()

# д) Заменить печать вызова функции на вызов функции
print('д')
def line():
    print('-----')

print(' 56')
print(' +44')
print(line())
print(' 100')
print(line())


# е) правильно
print('е')
def line():
    print('-----')

print(' 56')
print(' +44')
line()
print(' 100')
line()