import numpy as np
from matplotlib import pyplot as plt


def merge_different_amp():
    f, phi = 5, 0
    A = [1,2,3,4]
    t = np.linspace(0.0, 2, 1000)

    y = [A[i] * np.sin(2*np.pi*f*t) for i in range(len(A))]
    sum_y = sum(y)

    for i in range(len(y)):
        plt.subplot(4,1,i+1)
        plt.plot(t, y[i])
        plt.ylim(-4,4)
        plt.title("y="+str(A[i])+r"$\sin 10 \pi t$")

    plt.tight_layout()
    plt.show()

    plt.plot(t, sum_y)
    plt.title("sum of y")
    plt.show()

def merge_different_freq():
    A, phi = 1, 0
    f = [2,4,6,8]
    t = np.linspace(0.0, 4, 1000)

    y = [A * np.sin(2*np.pi*f[i]*t) for i in range(len(f))]
    sum_y = sum(y)

    for i in range(len(y)):
        plt.subplot(4,1,i+1)
        plt.plot(t, y[i])
        plt.ylim(-4,4)
        plt.title(r"$y=\sin 2 \pi ft $"+ f", f={f[i]}")

    plt.tight_layout()
    plt.show()

    plt.plot(t, sum_y)
    plt.title("sum of y")
    plt.show()


def merge_different_phase():
    A, f = 1, 5
    # phi = [0, 2*np.pi]
    phi = [0, np.pi / 2]

    # str_phi = [r"$0$", r"$2\pi$"]
    str_phi = [r"$0$", r"$\pi / 2$"]
    t = np.linspace(0.0, 2.0, 1000)

    y = [A * np.sin(2*np.pi*f*t-phi[i]) for i in range(len(phi))]
    sum_y = sum(y)

    for i in range(len(y)):
        plt.subplot(2,1,i+1)
        plt.plot(t, y[i])
        # plt.ylim(-4,4)
        plt.title(r"$y=\sin (10 \pi t - \phi), \phi = $"+ str_phi[i])

    plt.tight_layout()
    plt.show()

    plt.plot(t, sum_y)
    plt.title("sum of y")
    plt.ylim(-2,2)
    plt.show()

# merge_different_amp()
# merge_different_freq()
merge_different_phase()