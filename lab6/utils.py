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
    x0 = inv_x_loc(-Ik)
    xk = inv_x_loc(Ik)
    y0 = inv_y_loc(-40)
    yk = inv_y_loc(Jk)
    output[x0:xk+1, y0:yk+1] = 1
    return output

def plot_grid(data, title: str = "", filename: str = "", obsticle: bool = True):
    if not filename:
        filename = title.replace(" ", "_")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    if obsticle:
        im = ax.imshow(get_obsticle().T, origin="lower")
    else:
        im = ax.imshow(data.T, origin="lower")
    ax.contour(data.T, levels=20)
    fig.colorbar(im, ax=ax)
    fig.suptitle(title)
    fig.savefig("output/" + filename + ".png")
    print(f"Saved {filename}.png")

def get_u(psi, x0 = None):
    if not x0:
        output = np.diff(psi, axis=1) / DZ
    else:
        output = np.diff(psi[inv_x_loc(x0), :]) / DZ
    print({
        "shape": output.shape,
        "output": output
    })
    return output

def get_v(psi, x0 = None):
    if not x0:
        return np.diff(psi, axis=0) / DZ
    return np.diff(psi[:, inv_y_loc(x0)]) / DZ

def plot_cross_section(data, x_idx, title: str = "", filename: str = ""):
    if not filename:
        filename = title.replace(" ", "_")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data[x_idx, :])
    fig.suptitle(title)
    fig.savefig("output/" + filename + ".png")
    print(f"Saved {filename}.png")

def plot_cross_u(u, title: str = "", filename: str = ""):
    if not filename:
        filename = title.replace(" ", "_")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(u[inv_x_loc(0)])
    ax.set_xlabel("y")
    ax.set_ylabel("u(y)")
    fig.suptitle(title)
    fig.savefig("output/" + filename + ".png")
    print(f"Saved {filename}.png")

def plot_vel(u, title: str = "", filename: str = ""):
    if not filename:
        filename = title.replace(" ", "_")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(u.T, origin="lower")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fig.colorbar(im, ax=ax)
    fig.suptitle(title)
    fig.savefig("output/" + filename + ".png")
    print(f"Saved {filename}.png")

def is_in_obsticle(i, j):
    return get_obsticle()[i,j] == 1

