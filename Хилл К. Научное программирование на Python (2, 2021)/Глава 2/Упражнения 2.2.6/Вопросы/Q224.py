# Вариант № 1
print((complex(0., 1.) ** complex(0., 1.)).real)



# Вариант № 2
print((1j**1j).real)



# Вариант № 3
'''
По формуле Эйлера
exp(ix) = cos(x) +i*sin(x)
при х = пи / 2
exp(i*пи/2) = 0 +i*1 = i
Тогда
i**i = exp((пи/2)*i*i + 2пи*k) = exp(-пи/2 + 2пи*k)
где k - целое положительное число.
При k = 0
i**i = exp(-пи/2)
'''
import math
print(math.exp(-math.pi / 2))