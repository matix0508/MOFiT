from matplotlib import pyplot as plt
import numpy as np
from const import DZ, HEIGHT, WIDTH, Ik, Jk, Mu


def get_x_loc(i: int) -> int:
    return i -100


def inv_x_loc(i: int) -> int:
    return i + 100


def get_y_loc(i: int) -> int:
    return i - 40


def inv_y_loc(i: int) -> int:
    return i + 40


def get_x(i: int) -> int:
    return DZ * get_x_loc(i)


def get_y(i: int) -> int:
    return DZ * get_y_loc(i)

def get_flux(y, Q):
    return Q / (2 * Mu) * ((y**3) / 3 - 0.4**2 * y)

def get_vortocity(y, Q):
    return Q / (2 * Mu) * (2 * y)

def get_obsticle() -> np.ndarray:
    output = np.zeros((WIDTH, HEIGHT))
    x0 = inv_x_loc(-Ik-1)
    xk = inv_x_loc(Ik+1)
    y0 = inv_y_loc(-40)
    yk = inv_y_loc(Jk+1)
    output[x0:xk, y0:yk] = 1
    return output

def plot_grid(data, title: str = ""):
    grid = data.T - get_obsticle().T * data.T
    plt.imshow(grid, origin="lower")
    plt.contour(grid, levels=10)
    plt.colorbar()
    plt.title(title)
    plt.show()

def is_in_obsticle(i, j):
    return get_obsticle()[i,j] == 1
