import numpy as np
import matplotlib.pyplot as plt

from const import ROWS, COLS


class Solver:
    def __init__(self, obsticle, u0: float):
        self.potential = np.zeros((COLS, ROWS))
        self.obsticle = obsticle

    def setup(self):
        self.potential[0, 50:] = 1
        self.potential[-1, 50:] = 1
        self.potential[:, -1] = 1
        plt.imshow(self.potential.T, origin='lower')
        plt.show()

