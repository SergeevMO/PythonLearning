#C:\Anaconda3\envs\python39interpret\python.exe "C:\Program Files\JetBrains\PyCharm 2021.2\plugins\python\helpers\pydev\pydevconsole.py" --mode=client --port=61523
#import sys
#print('Python %s on %s' % (sys.version, sys.platform))
#sys.path.extend(['L:\\Обучение Python\\Хилл К. Научное программирование на Python (2, 2021)', 'L:/Обучение Python/Хилл К. Научное программирование на Python (2, 2021)'])


import numpy as np
import matplotlib.pyplot as plt

# а) Архимедова спираль
theta = np.linspace(0, 8.*np.pi, 10001)
a, b = 0, 2

r = a + b * theta

plt.polar(theta, r)
plt.show()

# б) Логарифмическая спираль
theta = np.linspace(0, 8.*np.pi, 10001)
a = 0.8

r = a ** theta

plt.polar(theta, r)
plt.show()
