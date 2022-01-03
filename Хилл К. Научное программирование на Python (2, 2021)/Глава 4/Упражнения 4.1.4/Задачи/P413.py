def powr(x, y):
    if x == y == 0:
        raise ValueError('Неопределённость 0^0')
    return x**y

print(powr(2, 3))

print(powr(0, 5))

print(powr(5, 0))

print(powr(0, 0))


# второй вариант
def powr(x, y):
    assert x != 0 or y != 0,\
        'Неопределённость 0^0'
    return x**y

print(powr(2, 3))

print(powr(0, 5))

print(powr(5, 0))

print(powr(0, 0))
