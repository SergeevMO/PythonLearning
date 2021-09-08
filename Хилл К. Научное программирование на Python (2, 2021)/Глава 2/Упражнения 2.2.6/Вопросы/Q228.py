h = 0.1     # мм
r = 384400  # км
import math
n = (math.log10(r) - math.log10(h) + 6) / math.log10(2)
math.ceil(n)
print(math.ceil(n))

'''
Исходное уравнение:
h*2^n = r
Число 6 учитывает разные единицы измерения.
'''
