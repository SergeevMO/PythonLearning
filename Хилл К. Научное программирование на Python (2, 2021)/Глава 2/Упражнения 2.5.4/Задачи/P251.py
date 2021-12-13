# Треугольник Паскаля
import math

r_max = 50
long = 3

for i in range(0, r_max + 1):
    a = (r_max + 1 - i) * long // 2
    print(f"{' ':>{a}}", end='')
    for j in range(0, i + 1):
        n = math.factorial(i) // (math.factorial(i - j) * math.factorial(j))
        if n % 2:
            print(f'{"*":<{long}}', end='')
        else:
            print(f'{" ":<{long}}', end='')
    print()




# второй вариант
# Output a pattern based on the parity of numbers in Pascal's Triangle

nmax = 50
rows = [[1],[1,1]]
for n in range(2, nmax+1):
    rows.append([1,])
    # Insert the entries for this row by summing neighbours in the previous row
    for k in range(n-1):
        rows[n].append(rows[n-1][k]+rows[n-1][k+1])
    rows[n].append(1)

# Pretty-print the rows as asterisks for odd numbers or else spaces
for i,row in enumerate(rows):
    s_row = []
    for x in row:
        if x % 2:
            s_row.append('*')
        else:
            s_row.append(' ')
    print(''.join(s_row))


# The loop printing the asterisks can be expressed more concisely using list comprehension (Section 4.3.2):
for i,row in enumerate(rows):
    print(''.join(['*' if x % 2 else ' ' for x in row]))
