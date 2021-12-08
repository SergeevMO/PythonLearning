P = [4, 5, 0, 2]
dPdx = []

for i, c in enumerate(P[1:]):
    dPdx.append((i + 1) * c)

print(dPdx)


# второй вариант
P = [4, 5, 0, 2]
dPdx = []
for i, c in enumerate(P[1:], start=1):
    dPdx.append(i*c)
print(dPdx)
