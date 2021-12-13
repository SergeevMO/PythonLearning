a = [2, 4, 10, 6, 8, 4]
an = []

a_min = min(a)
a_max = max(a)

a_d = a_max - a_min

for i in a:
    an.append((i - a_min) / a_d)

print(an)


print('\n')

# второй вариант
a = [2,4,10,6,8,4]
amin, amax = min(a), max(a)
for i, val in enumerate(a):
    a[i] = (val-amin) / (amax-amin)
print(a)