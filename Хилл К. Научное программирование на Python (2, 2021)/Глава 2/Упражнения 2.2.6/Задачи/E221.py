print('Способ № 1')
# Не-И И ИЛИ
a = True
b = True
x = not(a and b) and (a or b)
print(x)

a = False
b = True
x = not(a and b) and (a or b)
print(x)

a = True
b = False
x = not(a and b) and (a or b)
print(x)

a = False
b = False
x = not(a and b) and (a or b)
print(x)



print('Способ № 2')
# И ИЛИ НЕ-ИЛИ
a = True
b = True
x = (a and b) or not(a or b)
print(x)

a = False
b = True
x = (a and b) or not(a or b)
print(x)

a = True
b = False
x = (a and b) or not(a or b)
print(x)

a = False
b = False
x = (a and b) or not(a or b)
print(x)



print('Способ № 3')
# (НЕ И) ИЛИ (НЕ И)
a = True
b = True
x = (not a and b) or (not b and a)
print(x)

a = False
b = True
x = (not a and b) or (not b and a)
print(x)

a = True
b = False
x = (not a and b) or (not b and a)
print(x)

a = False
b = False
x = (not a and b) or (not b and a)
print(x)



print('Способ № 4')
# НЕ РАВНО
a = True
b = True
x = a != b
print(x)

a = False
b = True
x = a != b
print(x)

a = True
b = False
x = a != b
print(x)

a = False
b = False
x = a != b
print(x)