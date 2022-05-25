import numpy as np

from const import N, X0, D

def rho(i, j):
    x = i - N
    y = j - N
    return np.exp(-((x-X0)**2 + y**2)/D**2) - np.exp(-((x+X0)**2 + y**2)/D**2)