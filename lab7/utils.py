from matplotlib import pyplot as plt
import numpy as np


def get_rho(x):
    return np.pi ** (-0.5) * np.exp(-x**2)

def get_rho2D(r):
    return 1/np.pi * np.exp(-(r ** 2).sum())

def plot_moments(l_arr, I1, I2, I3, I4):
    plt.scatter(l_arr, I1, label="first moment")
    plt.scatter(l_arr, I2, label="second moment")
    plt.scatter(l_arr, I3, label="third moment")
    plt.scatter(l_arr, I4, label="fourth moment")
    plt.hlines([0, 0.5, 0.75], 0, 10**6, colors=["cyan", "orange", "purple"])
    plt.xlabel("iteration steps")
    plt.ylabel("Moments")
    plt.legend()
    plt.savefig("moments.png")
    plt.show()