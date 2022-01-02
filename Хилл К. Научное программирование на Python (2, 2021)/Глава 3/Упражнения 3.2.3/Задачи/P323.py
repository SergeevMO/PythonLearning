#C:\Anaconda3\envs\python39interpret\python.exe "C:\Program Files\JetBrains\PyCharm 2021.2\plugins\python\helpers\pydev\pydevconsole.py" --mode=client --port=61523
#import sys
#print('Python %s on %s' % (sys.version, sys.platform))
#sys.path.extend(['L:\\Обучение Python\\Хилл К. Научное программирование на Python (2, 2021)', 'L:/Обучение Python/Хилл К. Научное программирование на Python (2, 2021)'])


import numpy as np
import matplotlib.pyplot as plt

ages = np.array([1, 4, 14, 24, 34, 44, 54, 64, 74, 84, 94])
f_risk = -np.log10(np.array([227, 5376, 10417, 4132, 2488, 1106, 421, 178, 65, 21, 7]))
m_risk = -np.log10(np.array([177, 4386, 8333, 1908, 1215, 663, 279, 112, 42, 15, 6]))

line1 = plt.plot(ages, f_risk, color='r', marker='D', lw=1, label="М")
line2 = plt.plot(ages, m_risk, color='b', marker='^', lw=1, label="Ж")
lines = line1 + line2
print(lines)
labels = []
for line in lines:
    print(line)
    labels.append(line.get_label())
print(labels)
plt.legend(loc=0)
plt.title("Вероятность смерти 1:N")
plt.xlabel("возраст, год")
plt.ylabel("риск смерти")
plt.show()

