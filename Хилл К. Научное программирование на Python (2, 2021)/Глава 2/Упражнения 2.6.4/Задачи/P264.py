file = "D:\\103 Книги\\IT\\Машинное обучение, ИИ, глубокое обучение\\Хилл Кристиан. Научное программирование на Python (2, 2015, 1, 2021)\\P264.txt"

# а)
grid = []
f = open(file, mode='r')

for line in f:
    grid.append([*line.strip().split()])
f.close()

print(grid)

columns_max = len(grid[0])
row_max = len(grid)
grid_columns = []

for j in range(0, columns_max):
    col = []
    for i in range(0, row_max):
        col.append(grid[i][j])
    grid_columns.append(col)
print(grid_columns)

# б)
grid_diag_L = []

for j in range(0, columns_max):
    col = []
    k = j * 1
    for i in range(0, row_max):
        if k >= 0:
            col.append(grid[i][k])
            k -= 1
        else:
            break
    grid_diag_L.append(col)

    if j == columns_max - 1:
        for i in range(1, row_max):
            col = []
            k = columns_max - 1
            for q in range(k, 0, -1):
                if q >= i:
                    print(i, k, q)
                    col.append(grid[i][q])
                    i += 1
            grid_diag_L.append(col)
print(grid_diag_L)

grid_diag_R = []

for j in range(columns_max - 1, -1, -1):
    col = []
    k = j * 1
    for i in range(0, row_max):
        #if i >= columns_max - 1 - k:
        if k < columns_max:
            col.append(grid[i][k])
            k += 1
        else:
            break
    grid_diag_R.append(col)

    if j == 0:
        for i in range(1, row_max):
            col = []
            r = i * 1 + 1
            for q in range(0, r):
                if i < row_max:
                    print(i, r, q)
                    col.append(grid[i][q])
                    i += 1
            grid_diag_R.append(col)
print(grid_diag_R)




print('*'*74)
# второй вариант (более короткий)
'''
The grid of strings can be read in simply by splitting each of its lines on the whitespace delimiter and
appending the resulting list to the grid list. Iteration over its columns is easy enough;
to get the diagonals imagine the grid shifted so that each row is displaced by one entry to the left relative
to the preceding row. For the example grid in the question, this process would give:

A B C D * *
* E F G H *
* * I J K L

where * represents a "non-entry". Now the required NE-SW diagonals can be seen as the columns of this modified grid.
Consider indexing this modified grid by column, p and row, q.
The index p increases over the columns from 0 to m+n−2 inclusive.
For each p, the corresponding row index, q, takes values in the range q1≤q<q2 where q1=0 for p<n (i.e. A, B, C, D) or
q1=p−n+1 for p≥n (here, H and then L) and q2=p+1 for p<m−1 (A, E and then I) or q2=m for p≥m (columns to I, J, K, L).

We don't need to store the modified array: the indices p,q are related to the original array's row and column indices,
y and x through y=q,x=p−q. To obtain the other diagonal entries (those in the direction NW-SE),
simply imagine writing each row backwards.
'''
grid = []
f = open(file, 'r')
for line in f.readlines():
    grid.append(line.split())
f.close()

# number of rows, number of columns: ie grid is m x n
m, n = len(grid), len(grid[0])

# The grid is read in as a list of rows:
print('rows:', grid, sep='\n')

# Loop over the grid to retrieve its columns
cols = []
for x in range(n):
    cols.append([]) # вставляет пустые списки для последующего их заполнения
    for y in range(m):
        cols[-1].append(grid[y][x]) # каждый раз вставляет в последний список новые элементы
        print(cols)
print('cols:', cols, sep='\n')

# Retreive the NE-SW (diag1) and NW-SE (diag2) diagonals
diag1 = []
diag2 = []
for p in range(m+n-1):
    diag1.append([])
    diag2.append([])
    q1 = 0
    if p >= n: # n - число столбцов
        q1 = p - n + 1
    q2 = m # m - число строк
    if p < m-1:
        q2 = p+1
    for q in range(q1, q2):
        x, y = p - q, q
        diag1[-1].append(grid[y][x])
        # To get the other diagonal, read each row "backwards"
        x = n - x - 1
        diag2[-1].append(grid[y][x])
print('diag1:', diag1, sep='\n')
print('diag2:', diag2, sep='\n')