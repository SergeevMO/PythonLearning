import math
a = 6_378_137.0         # м
c = 6_356_752.314_245   # м
e = math.sqrt(1 - (c ** 2) / (a ** 2))
r = 6371
s_obl = 2 * math.pi * (a ** 2) * (1 + ((1 - e ** 2) / e) * math.atanh(e))
s = 4 * math.pi * (r * 1000) ** 2
print(s_obl)
print(s)
print((s_obl - s) * 100 / s_obl)
