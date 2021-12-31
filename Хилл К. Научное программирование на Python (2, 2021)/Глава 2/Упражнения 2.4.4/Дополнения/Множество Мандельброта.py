"""
The Mandlelbrot set is the set of all points in the complex plane for which, starting with z0=0,
the iteration zn+1 = zn^2 + c remains bounded. It is the case that if |zn| ever becomes larger than 2,
then the sequence diverges (i.e. is not bounded).

The Mandelbrot set may be visualised as an image in which the (x,y) coordinates of each pixel are
the real and imaginary parts of c=x+iy, and the pixel is coloured black or white
according to whether c is in the set or not.

Write a program to display the Mandelbrot set in the region of the complex plane bounded by −3 ≤ x ≤ 1,−2 ≤ y ≤ 2,
by displaying a space if a point is in the set or an asterisk if it isn't.

Hints:
Map the region of interest to an array 40 rows of 80-character strings, and inspect each point in this array:
#
cx, cy = -1., 0.
xsize, ysize = 80, 40
for j in range(ysize):
    for i in range(xsize):
        x = cx + 4. * (i - xsize / 2.) / xsize
        y = cy + 4. * (j - ysize / 2.) / ysize
        ...
#
Either use Python's builtin support for complex numbers, e.g.:
#
z = 3. + 8.5j
#
or handle the real and imaginary parts as separate floats.

When iterating, in addition to checking if |zn|≥2, keep track of the number of iterations performed and
bail (assume c is in the set) if this number exceeds some maximum (say, 1000).

(Extra credit). Extend your answer to the previous exercise by generating a 500 x 500 pixel greyscale image of
the Mandelbrot set. The shade of grey a pixel is coloured should reflect the number of iterations required to
determine that the corresponding point is not in the set. Use PIL, the Python Imaging Library as follows:
#
from PIL import Image

im = Image.new('RGB', (xsize, ysize))
...
im.putpixel((i, j), (ired, igreen, iblue))
...
im.save('mandelbrot.png', 'PNG')
#
where a pixel is placed at (i,j) and coloured with red, green and blue components ired, igreen, iblue
(each an integer from 0 to 255, such that (0,0,255) is pure blue, (255, 255, 255) is white, (0, 0, 0) is black, etc).
"""
"""
z = complex(0.,0.)
c = complex(1.,0.)
for x in range(-3, 1.1, 0.1):
    for y in range(-2, 2.1, 0.1):
        z = z**2 + complex(x, y)"""
max_it = 1000
cx, cy = -1., 0.
xsize, ysize = 80, 40

for j in range(ysize):
    row = []
    for i in range(xsize):
        x, y = (cx + 4. * (i - xsize / 2) / xsize,
                cy + 4. * (j - ysize / 2) / ysize)

        a, b = (0., 0.)
        it = 0
        while (a**2 + b**2<= 4.0 and it < max_it):
            a, b = a**2 - b**2 + x, 2*a*b + y
            it += 1
        if it == max_it:
            char = ' '
        else:
            char = '*'
        row.append(char)
    print(''.join(row))


print('\n\n\n')

from PIL import Image

max_it = 1024
cx, cy = -1., 0.
xsize, ysize = 10000, 10000

im = Image.new('RGB', (xsize, ysize))
for i in range(xsize):
    for j in range(ysize):
        c = complex(cx + 4. * (i - xsize / 2.) / xsize,
                    cy + 4. * (j - ysize / 2.) / ysize)

        z = 0. + 0.j
        it = 0
        while (abs(z) <= 2.0 and it < max_it):
            z = z ** 2 + c
            it += 1

        if it == max_it:
            col = 0
        else:
            col = it * 1 % 1023
        im.putpixel((i, j), (col, col, col))

im.save('mandelbrot5000.png', 'PNG')