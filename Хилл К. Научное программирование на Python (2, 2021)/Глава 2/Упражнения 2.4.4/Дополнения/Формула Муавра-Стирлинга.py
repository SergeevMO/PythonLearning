# Stirling's Approximation for lnn! is:
# lnn! ≈ n * ln(n) − n
# Write a program to output ln(n!), its Stirling's approximation and the relative error in the approximation,
# (exact-approx)/exact, for n<100. Then modify the program to output only the first value of n for which the relative error is less than 1%.
# Hint: the math module provides ("exposes") a factorial() method.

import math
err = False

for n in range(2, 100):
    lnn_approx = n * math.log(n) - n
    lnn_exact = math.log(math.factorial(n))
    ref_error = 100 * (lnn_approx - lnn_exact) / lnn_exact
    if abs(ref_error) < 1:
        err = True
    print(f'{n:>4}\t{lnn_exact:12.5f}\t{ref_error:10.5f}\t{err}')
