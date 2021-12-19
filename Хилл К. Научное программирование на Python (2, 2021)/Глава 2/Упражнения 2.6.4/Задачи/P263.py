# Индекс подобия Земле (Earth Similarity Index – ESI)
import math

file = "D:\\103 Книги\IT\\Машинное обучение, ИИ, глубокое обучение\\Хилл Кристиан. Научное программирование на Python (2, 2015, 1, 2021)\\ex2-6-g-esi-data.txt"
ESI_list = []

params_list = [False, True, True, False, True, False, True, False]
weight = [1, 0.57, 1.07, 1, 0.7, 1, 5.58, 1]

f = open(file, 'r')

title = []
for el in f.readline().strip().split(' '):
    if el.isalnum() or '_' in el:
        title.append(el)
#print(title)

quantity_params = len(title) - 1

title2 = ['']
for e in f.readline().strip().split(' '):
    le = len(e) - 1
    if e[1:le].isalpha():
        title2.append(e)
#print(title2)

f.readline()

cosmic_body_list = []
for line in f:
    body = []
    body.append(line[:15].strip())
    line_params = line[15:].strip().split()
    for lf in line_params:
        body.append(float(lf))
    cosmic_body_list.append(body)
#print(cosmic_body_list)

n = params_list.count(True)
for body in cosmic_body_list:
    ESI = 1
    for i, p in enumerate(params_list):
        if p:
            ESI *= (1 - abs((body[i + 1] - cosmic_body_list[0][i + 1]) / (body[i + 1] + cosmic_body_list[0][i + 1]))) ** (weight[i])
    ESI = ESI ** (1 /n)
    ESI_list.append((ESI, body[0]))

ESI_list.sort(reverse=True)

print(f"\n{'Cosmic body name':<17}{'  ESI':^7}")
for cb in ESI_list:
    print(f'{cb[1]:<17}{cb[0]:7.3f}')

f.close()



print('*'*74)
# второй вариант
f = open(file, 'r')
# skip the three header lines
f.readline()
f.readline()
f.readline()

# The column indexes of fields *after the first, name field* within the
# provided data table for the properties needed to calculate the ESI
cols = (1, 2, 4, 6)
n = len(cols)
# The terrestrial values of those parameters and their weights
x_earth, w = (1, 1, 1, 288.), (0.57, 1.07, 0.70, 5.58)

print('-'*29)
print('Planet/Satellite Name   ESI  ')
print('-'*29)
for line in f.readlines():
    name = line[:15].lstrip()
    fields = line[15:].split()
    ESI = 1
    for i, col in enumerate(cols):
        xi = float(fields[col])
        ESI *= (1 - abs((xi - x_earth[i])/(xi + x_earth[i])))**w[i]
    ESI = ESI**(1/n)
    print('{:<21s}   {:5.3f}'.format(name, ESI))
print('-'*29)