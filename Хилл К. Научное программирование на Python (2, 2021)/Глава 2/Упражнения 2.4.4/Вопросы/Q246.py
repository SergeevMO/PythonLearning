a = ('a0', 'a1', 'a2', 'a3', 'a4')
b = ('b0', 'b1', 'b2', 'b3', 'b4')

z = zip(a, b)


'''
# Функция zip образует список кортежей из элементов переменных с одинаковым индексом:

for pair in z:
    print(pair)

# Распаковка такого списка (*z) в функции zip означает передачу в неё следующих аргументов:
('a0', 'b0')
('a1', 'b1')
('a2', 'b2')
('a3', 'b3')
('a4', 'b4')
которые она упаковывает по номеру индекса, тем самым получая снова первоначальные переменные.
'''

A, B = zip(*z)
print(A, '\n', B, sep='')
