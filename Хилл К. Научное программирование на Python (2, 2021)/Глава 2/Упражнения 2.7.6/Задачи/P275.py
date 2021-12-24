import math
g = 9.81

def fly_projectile(v, a):
    L = v ** 2 / g
    r = L * math.sin(2 * math.radians(a))
    h = L * math.sin(math.radians(a)) ** 2 / 2
    return r, h

v, a = 10, 30

R, H = fly_projectile(v, a)
print(f'Дальность полёта - {R:.2f}\nМаксимальная высота полёта - {H:.2f}')