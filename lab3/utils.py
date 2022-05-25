import numpy as np

def func(x: float) -> float:
    return np.exp(-100 * (x-0.5)**2)

def zero(x: float) -> float:
    return 0

def get_derr_u(u: np.array, dx):
    return np.gradient(u, dx) 