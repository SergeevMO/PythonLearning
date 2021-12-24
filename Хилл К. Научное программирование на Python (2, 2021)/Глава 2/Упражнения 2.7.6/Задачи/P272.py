import math

for n in range (1, 1000):
    f = math.factorial(n)
    f_str = str(f)
    digits = list(f_str)
    sum_digits = 0

    for i in digits:
        sum_digits += int(i)

    if f % sum_digits != 0:
        print(n)
        break




# второй вариант
# Find the smallest positive integer, n, for which n! is *not* divisible
# by the sum of its digits.

def sum_digits(n):
    """ Return the sum of the decimal digits of n. """
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

n = nfac = 1
while True:
    nfac *= n
    digit_sum = sum_digits(nfac)
    if nfac % digit_sum:
        # Success! report and exit the loop
        print('{}! is not divisible by the sum of its digits'.format(n))
        break
    n += 1
