# Секвойя красная (Sequoia sempervirens)
file = "D:\\103 Книги\\IT\\Машинное обучение, ИИ, глубокое обучение\Хилл Кристиан. Научное программирование на Python (2, 2015, 1, 2021)\\redwood-data.txt"
name_tree = []
location = []
diameter_m = []
height_m = []

f = open(file, 'r')
f.readline()
f.readline()
for line in f:
    fields = line.strip().split('\t')
    name_tree.append(fields[0].strip())
    location.append(fields[1].strip())
    diameter_m.append(float(fields[2].strip()))
    height_m.append(float(fields[3].strip()))

max_h = max(height_m)
indx_max_h = height_m.index(max_h)
print(f'Максимальная высота {max_h} м у дерева {name_tree[indx_max_h]} в {location[indx_max_h]}')

max_d = max(diameter_m)
indx_max_d = diameter_m.index(max_d)
print(f'Максимальный диаметр {max_d} м у дерева {name_tree[indx_max_d]} в {location[indx_max_d]}')




print('*'*74)
# Второй вариант
data_file = file

# Indexes of the fields in each record:
NAME, LOCATION, DIAMETER, HEIGHT = 0, 1, 2, 3

f = open(data_file)
# Skip the header lines
f.readline()
f.readline()

tree_data = []
max_height, max_diameter = 0, 0
for i, line in enumerate(f.readlines()):
    records = line.split('\t')
    diameter = records[DIAMETER] = float(records[DIAMETER])
    height = records[HEIGHT] = float(records[HEIGHT])
    if diameter > max_diameter:
        max_diameter, max_diameter_index = diameter, i
    if height > max_height:
        max_height, max_height_index = height, i
    tree_data.append(records)

highest_tree = tree_data[max_height_index]
print('The highest tree: {}, {} m in {}'.format(highest_tree[NAME],
                            highest_tree[HEIGHT], highest_tree[LOCATION]))

widest_tree = tree_data[max_diameter_index]
print('The widest tree: {}, with diameter {} m in {}'.format(widest_tree[NAME],
                            widest_tree[DIAMETER], widest_tree[LOCATION]))