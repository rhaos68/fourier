import numpy as np
import matplotlib.pyplot as plt

def draw_exp():
    x = np.arange(-0.2, 3, 0.01)

    y2 = 2 ** x
    y3 = 3 ** x

    plt.plot(x,y2, color='blue')
    plt.text(2.6, 2**2.6+1,r"$y=2^x$")

    plt.plot(x,y3, color='blue')
    plt.text(2.72, 3**2.7+1,r"$y=3^x$")

    ye = np.e ** x
    plt.plot(x,ye, color='green')
    plt.text(2.65, np.e**2.6,r"$y=e^x$", color='green')

    plt.axhline(y=0, color='black', label='x')
    plt.axvline(x=0, color='black', label='y')

    plt.show()

def draw_log():
    x = np.arange(0.1, 30, 0.01)

    ye = np.log(x)
    y2 = np.log2(x)
    y3 = np.log(x) / np.log(3)

    plt.plot(x,y2, color='blue')
    plt.text(15, 4.2,r"$y=\ln 2$")

    plt.plot(x,y3, color='blue')
    plt.text(25, 2.6,r"$y=\ln 3$")

    plt.plot(x,ye, color='green')
    plt.text(20, 3.2,r"$y=\ln x$", color='green')

    plt.axhline(y=0, color='black', label='x')
    plt.axvline(x=0, color='black', label='y')

    plt.show()


# draw_exp()
draw_log()
