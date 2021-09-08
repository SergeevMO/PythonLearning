import math
a = 5
s = math.copysign(1, a)
sig = str(s)
if sig[0] == '-':
    print(sig[0])
else:
    print('+')

b = -5
s = math.copysign(1, b)
sig = str(s)
if sig[0] == '-':
    print(sig[0])
else:
    print('+')