def str_vector(v):
    assert type(v) is list or type(v) is tuple,\
                'argument to str_vector must be a list or tuple'
    assert len(v) in (2,3),\
                'vector must be 2D or 3D in str_vector'
    unit_vectors = ['i','j','k']
    s = []
    for i, component in enumerate(v):
        try:
            s.append('{}{}'.format(float(component), unit_vectors[i]))
        except (TypeError, ValueError):
            raise ValueError(
                'Элемент в векторе {}: {} не действительное число'.format(v, component))

    return '+'.join(s).replace('+-', '-')

print(str_vector([-2, 3.5]))

print(str_vector((4, 0.5, -2)))

#print(str_vector((4, complex(0.5, 3), -2)))

print(str_vector([-2, '3.5']))

print(str_vector([-2, 'y']))

print('*'*79)

# второй вариант
def str_vector(v):
    if type(v) is not list and type(v) is not tuple:
        raise TypeError('argument to str_vector() must be a list or tuple')
    if len(v) not in (2,3):
        raise ValueError('vector must be 2D or 3D in str_vector()')
    unit_vectors = ['i','j','k']
    s = []
    for i, component in enumerate(v):
        try:
            s.append('{:s}{:1s}'.format(str(float(component)), unit_vectors[i]))
        except (TypeError, ValueError):
            raise ValueError('Invalid element in vector {}: {} is'
                ' not a real number'.format(v, component))
    return ' + '.join(s).replace('+ -', '- ')

print(str_vector([-2, 3.5]))

print(str_vector((4, 0.5, -2)))

print(str_vector((4, complex(0.5, 3), -2)))