a = [1, 2, 3]
b = [5, 8, 10]
c = [4, 6, 7]
a, b, c = [1, -2, 1], [2, -0.5, -1], [0.5, 1, -1.5]

def scalar_mult(x, y):
    sm = 0
    for i, e in enumerate(x):
        sm += e * y[i]
    return sm

def vector_mult(x, y):
    return [x[1]*y[2] - x[2]*y[1], x[2]*y[0] - x[0]*y[2], x[0]*y[1] - x[1]*y[0]]


print('скалярное произведение векторов: ', scalar_mult(a, b))
print('векторное произведение векторов: ', vector_mult(a, b))




def mix_scalar_mult(x, y, z):
    v = vector_mult(y, z)
    return scalar_mult(x, v)

def mix_vector_mult(x, y, z):
    v = vector_mult(y, z)
    return vector_mult(x, v)

print('смешанное скалярное произведение векторов: ', mix_scalar_mult(a, b, c))
print('смешанное векторное произведение векторов: ', mix_vector_mult(a, b, c))


# второй вариант
def dot(a, b):
""" Return the dot product of vectors a, b. """
return sum(ai * bi for ai, bi in zip(a, b))

def cross(a, b):
""" Return the vector (cross) product of vectors a, b. """
return [a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]]

def scalar3(a, b, c):
""" Return the scalar triple product of vectors a, b, c. """
return dot(a, cross(b, c))

def vector3(a, b, c):
""" Return the vector triple product of vectors a, b, c. """
return cross(a, cross(b, c))

a, b, c = [1, -2, 1], [2, -0.5, -1], [0.5, 1, -1.5]

print('a . b =', dot(a, b))
print('a x b =', cross(a, b))
print('a . (b x c) =', scalar3(a, b, c))
print('a x (b x c) =', vector3(a, b, c))