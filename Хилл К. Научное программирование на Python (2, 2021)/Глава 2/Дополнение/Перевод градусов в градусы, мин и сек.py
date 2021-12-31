"""
Write a program to convert an longitude or latitude expressed as a signed quantity in degrees
(possibly with a fractional component expressed in decimal notation) to one expressed in
degrees, minutes and seconds (the first two as integers and the last as a floating point number).
Input latitudes may be −90−+90 and longitudes −180−+180.

In addition to the numerical values of degrees, minutes and seconds, also output a string in
the form deg° min′ sec″ X where X is N, S, E, or W as appropriate. For example,

In [x]: deg_to_dms(38.889469)
Out[x]: (38, 53, 22.088400000007823)

In [x]: deg_to_dms(38.889469, pretty_print='latitude')
Out[x]: '38° 53′ 22.0884″ N'

In [x]: deg_to_dms(-77.035258)
Out[x]: (-77, 2, 6.928799999994226)

In [x]: deg_to_dms(-77.035258, pretty_print='longitude')
Out[x]: '77° 2′ 6.9288″ W'

"""

def deg_to_dms(deg, pretty_print=None):
    v = str()
    degrees = int(deg)
    deg = (deg - degrees) * 60

    if (pretty_print is None) or (pretty_print == 'longitude'):
        if degrees >= -180 and degrees <= 180:
            minutes = int(deg)
            deg -= minutes
            seconds = deg * 60
            if pretty_print == 'longitude':
                if degrees >= 0:
                    v = 'В'
                else:
                    v = 'З'
                return f'{abs(degrees)}° {abs(minutes)}′ {abs(seconds):.4f}" {v}'
            else:
                return degrees, abs(minutes), abs(seconds)
        else:
            return "Неверное значение градусов."
    elif pretty_print == 'latitude':
        if degrees >= -90 and degrees <= 90:
            minutes = int(deg)
            deg -= minutes
            seconds = deg * 60
            if degrees >= 0:
                v = 'С'
            else:
                v = 'Ю'
            return f'{abs(degrees)}° {abs(minutes)}′ {abs(seconds):.4f}" {v}'
        else:
            return "Неверное значение градусов."
    else:
        return "Неверное значение направления."

print(deg_to_dms(38.889469))
print(deg_to_dms(38.889469, pretty_print='latitude'))
print(deg_to_dms(-77.035258))
print(deg_to_dms(-77.035258, pretty_print='longitude'))



print('*'*74)

# Второй вариант
def deg_to_dms2(deg, pretty_print=None, ndp=4):
    """Convert from decimal degrees to degrees, minutes, seconds."""

    m, s = divmod(abs(deg)*3600, 60)
    d, m = divmod(m, 60)
    if deg < 0:
        d = -d
    d, m = int(d), int(m)

    if pretty_print:
        if pretty_print=='latitude':
            hemi = 'N' if d>=0 else 'S'
        elif pretty_print=='longitude':
            hemi = 'E' if d>=0 else 'W'
        else:
            hemi = '?'
        return '{d:d}° {m:d}′ {s:.{ndp:d}f}″ {hemi:1s}'.format(
                    d=abs(d), m=m, s=s, hemi=hemi, ndp=ndp)
    return d, m, s

print(deg_to_dms2(38.889469))
print(deg_to_dms2(38.889469, pretty_print='latitude'))
print(deg_to_dms2(-77.035258))
print(deg_to_dms2(-77.035258, pretty_print='longitude'))