# Тетрация
def tetracie(x, n):
    if n == 0:
        return 1
    return x ** tetracie(x, n - 1)

x, n = 5, 3
print(tetracie(x, n))

x, n = 2, 5
print(tetracie(x, n))





print('*'*74)

# итерационный вариант
import math

def tet(x, n):
    """ Tetration, ^nx, by loop over decreasing exponent counter. """
    if n == 0:
        return 1
    p = x
    while n > 1:
        p = x**p
        n -= 1
    return p

x, n = 5, 3
t = tet(x,n)
print('tet({:d}, {:d}) = {:d}'.format(x, n, t))
ndigits = int(math.log10(t)) + 1
print('(a number with {:d} digits)'.format(ndigits))