# Определение pH многоосновной слабой кислоты
import math

# Константа кислотности уксусной кислоты
Ka = 1.78e-5
# Мольная концентрация уксусной кислоты в воде (моль/л)
cm = 0.01
# пороговая величина сходимости при расчётах определения концентрации ионов водорода
e = 1.e-10
# концентрация водорода
cH = 0
# разница концентрации водорода на n и n+1 шаге итерации
dH = 100

while not math.isclose(dH, e, abs_tol=e):
    cHn = math.sqrt(Ka * (cm - cH))
    dH = cHn - cH
    cH = cHn

pH = -round(math.log10(cH), 3)

print(pH, '\n', cH, '\n', dH)


print('\n')

# второй вариант
TOL = 1.e-10

# Acid dissociation constant, acid concentration (M)
Ka, c = 1.78e-5, 0.01

Hp = 0.
while True:
    lastHp, Hp = Hp, math.sqrt(Ka * (c - Hp))
    if abs(lastHp - Hp) < TOL:
        break
pH = -math.log10(Hp)

print('[H+] = {:g} M, pH = {:.2f}'.format(Hp, pH))
