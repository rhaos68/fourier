import numpy as np
from matplotlib import pyplot as plt


f1, f2, f3 = 60, 120, 180
t = np.linspace(0.0, 0.1, 1000)
y1 = 1.1 * np.sin(2* np.pi * f1 * t)
y2 = 0.8 * np.sin(2* np.pi * f2 * t)
y3 = 0.5 * np.sin(2* np.pi * f3 * t)
y = y1 + y2 + y3

plt.subplot(4,1,1)
plt.plot(t,y)
plt.title(r"$y = y1 + y2 + y3$")

plt.subplot(4,1,2)
plt.plot(t,y1)
plt.title(r"$y1 = 1.1 \cdot \sin (2 \pi \cdot 60t) $")

plt.subplot(4,1,3)
plt.plot(t,y2)
plt.title(r"$y1 = 0.8 \cdot \sin (2 \pi \cdot 120t) $")

plt.subplot(4,1,4)
plt.plot(t,y3)
plt.title(r"$y1 = 1.5 \cdot \sin (2 \pi \cdot 180t) $")

plt.tight_layout()
plt.show()
