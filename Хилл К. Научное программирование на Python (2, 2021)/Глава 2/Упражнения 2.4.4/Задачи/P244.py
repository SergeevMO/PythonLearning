# Треугольник Паскаля
import math

r_max = 12
long = 4

for i in range(0, r_max + 1):
    a = (r_max + 1 - i) * long // 2
    print(f"{' ':>{a}}", end='')
    for j in range(0, i + 1):
        n = math.factorial(i) // (math.factorial(i - j) * math.factorial(j))
        print(f'{n:<{long}}', end='')
    print()




print()

# Вариант № 2
# Output the first nmax rows of Pascal's Triangle

nmax = 8
rows = [[1],[1,1]]
for n in range(2, nmax+1):
    rows.append([1,])
    # Insert the entries for this row by summing neighbours in the previous row
    for k in range(n-1):
        rows[n].append(rows[n-1][k]+rows[n-1][k+1])
    rows[n].append(1)

# Pretty-print the rows as centered strings of numbers
for i,row in enumerate(rows):
    print('{row:^{length:d}}'.format(length=4*(nmax+1),
                                     row=('{:4d}'*(i+1)).format(*row)))

'''
The numbers in each row are calculated by summing the neighbouring numbers from the row above 
(with additional 1s at the start and end of each row). The nice formatting is acheived 
by first creating a string representation of the numbers in a row in 4-character fields, 
and then centring this string in a width equal to the maximum width taken up by the final row.
'''