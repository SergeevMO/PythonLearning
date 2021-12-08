rank = 1
exam_list = [87, 75, 75, 50, 32, 32]
rank_list = []

value = exam_list[0]

for i, v in enumerate(exam_list, 1):
    if value != v:
        rank = i
        value = v
    rank_list.append(rank)

print(rank_list)


# второй вариант
exam_list = [87, 75, 75, 50, 32, 32]
rank_list = []
for v in exam_list:
    rank_list.append(exam_list.index(v) + 1)
print(rank_list)