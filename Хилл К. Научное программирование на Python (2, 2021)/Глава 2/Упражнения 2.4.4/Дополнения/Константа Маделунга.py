"""
The Madelung constant is used in determining the electrostatic potential of a single ion in a crystal
by approximating the ions by point charges:

Vi = e / (4π * ϵ0 * r0 ) * ∑j (zj * r0) / rij = (e / 4π * ϵ0 * r0) Mi

where r0 is the nearest neighbour distance,
and the Madelung constant of the ith ion is given by the sum over all the other ions in the crystal:

Mi = ∑j zj * rij / r0.

For the cubic crystal NaCl, the summation may be performed over three orthogonal co-ordinates:

MNa = ∑j,k,l=−∞...∞ [(−1)^(j+k+l) / sqrt(j2+k2+l2)],

where the prime indicates that the term (0,0,0) is excluded.
Benson's formula provides a practical and efficient way of evaluating this sum as:

M(Na+) = −12π * ∑m,n=1,3,...∞ [sech(12π * sqrt(m2+n2))]^2,

where the summation is performed over all positive odd integers m and n.

Write a program to calculate the Madelung constant for Na+ ions in NaCl, -1.74756...
"""

import math
M = 0
for n in range(1, 12, 2):
    for m in range(1, 14, 2):
        s = math.cosh(0.5 * math.pi * math.hypot(n, m)) ** (-2)
        print(f'{n:2}, {m:2}, {s:e}')
        if s >= 1e-16:
            M += s
M *= -12 * math.pi
print(M)


print('*'*74)

# С учётом сходимости
M = 0.
n = 1
while True:
    oldM = M
    for m in range(1, n+1, 2):
            fac = 2
            if n == m:
                fac = 1
            M += fac * math.cosh(0.5*math.pi*math.hypot(n, m))**-2
    if abs(M - oldM) < 1e-16:
        break
    n += 2
print(-12*math.pi*M)