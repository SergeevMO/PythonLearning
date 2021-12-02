# 'eggs' or 'ham' - в данном выражении используются непустые строки, которые рассматриваются как True
# Перовое строковое значение является True, поэтому далее проверка ИЛИ не осущетвляется и возвращается eggs
print('eggs' or 'ham')

s = 'eggs'

# s сравнивается с 'eggs'
print(s == ('eggs' or 'ham'))
print(s == 'eggs' or s == 'ham')

# s сравнивается с 'ham'
print(s == ('ham' or 'eggs'))
print(s == 'ham' or s == 'eggs')

