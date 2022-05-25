import numpy as np

from const import COLS, ROWS


class Container:
    def __init__(self, obsticle: np.ndarray):
        self.grid = np.zeros((ROWS, COLS))
        self.obsticle = obsticle
