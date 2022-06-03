from matplotlib import pyplot as plt
import numpy as np

from const import COLS, ROWS


def get_obsticle():
    output = np.zeros((COLS, ROWS))
    output[96:105, 30:70] = 1
    return output

def plot_grid(obj, obj2=None, filename="grid"):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(obj.T, origin='lower')
    ax.contour(obj.T, levels=35)
    if obj2 is not None:
        ax.imshow(obj2.T, origin='lower')
    ax.set_title(filename)
    fig.savefig(f"output/{filename}.png")

def get_phi(x: int, u0: float) -> float:
    return (x+1) * u0

def get_psi(y: int, u0: float) -> float:
    return (y+1) * u0