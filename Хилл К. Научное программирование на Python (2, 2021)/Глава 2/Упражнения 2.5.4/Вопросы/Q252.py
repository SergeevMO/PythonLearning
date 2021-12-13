import math

# а)
x = 5.2
y = 7.8

if (x >= 0) and (y >= 0) and (x.imag == 0) and (y.imag == 0):
    a = x
    b = y

    while not math.isclose(a, b, rel_tol=1.0e-14, abs_tol=1.0e-15):
        a, b = 0.5*(a + b), math.sqrt(a * b)
print(f'agm({x},{y}) = {a}')


print('\n')

# б) константа Гаусса
x = 1
y = math.sqrt(2)

if (x >= 0) and (y >= 0) and (x.imag == 0) and (y.imag == 0):
    a = x
    b = y

    while not math.isclose(a, b, rel_tol=1.0e-14, abs_tol=1.0e-15):
        a, b = 0.5*(a + b), math.sqrt(a * b)

    G = 1 / a
print(f'G = {G}')


print('\n')

# второй вариант определения константы Гаусса
tol = 1.e-14
an, bn = 1., math.sqrt(2)
while abs(an - bn) > tol:
    an, bn = (an + bn) / 2, math.sqrt(an * bn)
print('G = {:.14f}'.format(1/an))