import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-0.2, 3, 0.01)

y2 = 2 ** x
y2_prime = 2 ** x * np.log(2)

y3 = 3 ** x
y3_prime = 3 ** x * np.log(3)


plt.plot(x,y2, color='blue')
plt.text(2.6, 2**2.6+1,r"$y=2^x$")

plt.plot(x,y2_prime, color='red')
plt.text(2.5, 2**2.5*np.log(2)-1,r"$y=2^x \ln 2$")

plt.plot(x,y3, color='blue')
plt.text(2.72, 3**2.7+1,r"$y=3^x$")

plt.plot(x,y3_prime, color='red')
plt.text(2.1, 3**2.5*np.log(3),r"$y=3^x \ln 3$")

ye = np.e ** x
plt.plot(x,ye, color='green')
plt.text(2.65, np.e**2.6,r"$y=e^x$", color='green')

plt.axhline(y=0, color='black', label='x')
plt.axvline(x=0, color='black', label='y')



plt.show()
