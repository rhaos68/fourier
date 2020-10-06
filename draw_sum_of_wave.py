import numpy as np
from matplotlib import pyplot as plt

def draw_sum_of_wave(a0, coeffi, w):
    t = np.linspace(0.0, 1.0, 1000) # 1ms 단위. ~1초
    n = range(1,len(coeffi)+1) # 1,2,3,...len(coeffi)

    y_a0 = a0 * np.ones(len(t))

    cos_val = [ab[0] * np.cos(i*w*t) for ab,i in zip(coeffi,n)] #an*cos(nwt)
    sin_val = [ab[1] * np.sin(i*w*t) for ab,i in zip(coeffi,n)] #bn*sin(nwt)
    yn = [(a0 + c + s) for c,s in zip(cos_val,sin_val)]

    y_sum = yn[0]
    for y in yn[1:]:  y_sum += y

    plt.subplot(5,1,1)
    plt.plot(t, y_sum)
    plt.title(r"$y(t)=a_0 + \sum _{n=0}^{\infty}{a_n \cos n\omega t + b_n \sin n\omega t}$")

    plt.subplot(5,1, 2)
    plt.plot(t, y_a0)
    plt.title("$y(t)=a_0$")

    plt.subplot(5, 2, 5)
    plt.plot(t, cos_val[0])
    plt.plot(t,np.zeros(len(t)))
    plt.title(r"$y(t)=a_1 \cos \omega t$")

    plt.subplot(5, 2, 6)
    plt.plot(t, sin_val[0])
    plt.plot(t, np.zeros(len(t)))
    plt.title(r"$y(t)=b_1 \sin \omega t$")

    plt.subplot(5, 2, 7)
    plt.plot(t, cos_val[1])
    plt.plot(t, np.zeros(len(t)))
    plt.title(r"$y(t)=a_2 \cos \omega t$")

    plt.subplot(5, 2, 8)
    plt.plot(t, sin_val[1])
    plt.plot(t, np.zeros(len(t)))
    plt.title(r"$y(t)=b_2 \sin \omega t$")

    plt.subplot(5, 2, 9)
    plt.plot(t, cos_val[2])
    plt.plot(t, np.zeros(len(t)))
    plt.title(r"$y(t)=a_3 \cos \omega t$")

    plt.subplot(5, 2, 10)
    plt.plot(t, sin_val[2])
    plt.plot(t, np.zeros(len(t)))
    plt.title(r"$y(t)=b_3 \sin \omega t$")

    plt.tight_layout()
    plt.show()

a0 = 0.4
coeffi = (
    (0.3,0.5), (0.2,0.5), (0.2,0.3), (0.7,0.6),(1.2,0.3), (0.3,0.6),(0.2,0.3), (2.3,0.6),(1.5,1.5),(0.2,0.5),(2.3,0.6),(1.5,1.5),(0.2,0.5)
)
w = 2*np.pi*4

draw_sum_of_wave(a0, coeffi, w )