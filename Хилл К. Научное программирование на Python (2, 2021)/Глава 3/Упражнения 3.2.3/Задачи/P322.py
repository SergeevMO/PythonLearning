# спираль гауссовых простых чисел
import numpy as np
import matplotlib.pyplot as plt

def issimplenum(n):
    n_max = int(np.sqrt(n)) + 1

    for i in range(2, n_max):
        if n % i == 0:
            return False
    else:
        return True

def isgaus_simple_num(c):
    x = c.real
    y = c.imag

    def isgaus(p):
        p = int(abs(p))
        if issimplenum(p):
            p = p - 3
            m_max = int(p / 4 + 1)
            for k in range(0, m_max):
                if 4 * k == p:
                    return True
            else:
                return False
        else:
            return False

    if x == 0:
        if isgaus(y):
            return True
        return False
    elif y == 0:
        if isgaus(x):
            return True
        return False
    else:
        if issimplenum(x**2 + y**2):
            return True
        return False


c = c0 = 5 + 23j
dc = 1 + 0j
h = 1
h_max = 10000
spiral_list = list()
path_x = list()
path_y = list()

while h <= h_max:
    c = c + dc

    if isgaus_simple_num(c):
        spiral_list.append(c)
        path_x.append(c.real)
        path_y.append(c.imag)
        x, y = -dc.imag, dc.real # (1,0) -> (0,1) -> (-1,0) -> (0,-1) -> (1,0)
        dc = complex(x, y)

    if c == c0:
        path_x.append(spiral_list[0].real)
        path_y.append(spiral_list[0].imag)
        print(f'Число шагов {h}')
        break
    h += 1
#print(spiral_list)

plt.plot(path_x, path_y, lw=0.5)
plt.show()


print('*'*74)
# Второй вариант
def is_prime(a):
    """ Return True if a is a prime number. """
    if a==2:
        return True
    if not a % 2:
        return False
    for d in range(3, int(np.sqrt(a)) + 1, 2):
        if not a % d:
            return False
    return True

def is_gaussian_prime(c):
    """ Return True if c = x + iy is a Gaussian prime (otherwise False). """

    x, y = c
    if x==0 or y==0:
        a = abs(x) or abs(y)
        return is_prime(a) and a % 4 == 3
    a = x**2 + y**2
    return is_prime(a)

def turn_left(c):
    """ Permute (1,0) -> (0,1) -> (-1,0) -> (0,-1) -> (1,0). """
    dx, dy = c
    return -dy, dx

# Starting point and direction
x, y = x0, y0 = 5, 23
dx, dy = 1, 0

# Keep track of the points on our spiral path in these lists
pathx, pathy = [x], [y]
# It isn't known whether every iteration produces a closed loop so
# set a maximum number of steps to take
max_steps = 10000

step = 0
while step < max_steps:
    step += 1
    x, y = x+dx, y+dy
    pathx.append(x)
    pathy.append(y)
    if (x,y) == (x0,y0):
        print('Returned to ({}, {}) in {} steps.'.format(x, y, step))
        break
    if is_gaussian_prime((x,y)):
        dx, dy = turn_left((dx,dy))
else:
    print('max_steps = {} reached.'.format(max_steps))

plt.plot(pathx, pathy, lw=2)
plt.show()