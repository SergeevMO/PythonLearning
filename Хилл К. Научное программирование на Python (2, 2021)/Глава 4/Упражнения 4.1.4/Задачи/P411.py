# Африканская ласточка
file = "L:\\Обучение Python\\Хилл К. Научное программирование на Python (2, 2021)\\Глава 4\\Упражнения 4.1.4\\Задачи\\swallow-speeds.txt"

# а) учёт точек
f = open(file=file, mode='r')
v_list = list()

for line in f:
    try:
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        num = float(line)
    except ValueError:
        d = []
        for symb in line:
            if symb.isdecimal() or symb == '.':
                d.append(symb)
        num = ''.join(d)
        v_list.append(float(num))
        print(f'Строка обработана. Число {num}')
        continue
    v_list.append(num)

f.close()

avg = sum(v_list) / len(v_list)
print(avg)


# а) не учёт точек
f = open(file=file, mode='r')
v_list = list()

for line in f:
    try:
        v_list.append(float(line))
    except ValueError:
        print(f'Строка {line} не обработана')

f.close()

avg = sum(v_list) / len(v_list)
print(round(avg, 3))
