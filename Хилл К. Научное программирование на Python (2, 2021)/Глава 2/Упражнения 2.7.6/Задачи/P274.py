# Объём и общая площадь поверхности правильной пирамиды
import math
def pyramid_AV(n, s, h):
    """ n - число сторон многоугольника основания пирамиды,
        s - длина стороны многоугольника,
        h - высота пирамиды
        a - апофема многоугольника
        A - площадь (многоугольника) основания пирамиды
        l - высота боковой грани пирамиды """
    a = 0.5 * s / math.tan(math.pi / n)
    A = 0.5 * n * s * a
    l = math.hypot(h, a)
    V = A * h / 3
    S = A + 0.5 * n * s * l
    return V, S

n = 6
s = 2
h = 10

P = pyramid_AV(n, s, h)
print(f'Общий объём - {P[0]}\nОбщая площадь - {P[1]}')
print(pyramid_AV(5, 36.5, 12))