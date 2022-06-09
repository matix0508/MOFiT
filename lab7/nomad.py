import numpy as np

from utils import get_rho


class Nomad:
    def __init__(self, x0):
        self.x = x0

    def make_step(self):
        dx = (np.random.rand() - 0.5) / 2
        xp = self.x + dx
        y = np.random.rand()
        if get_rho(xp) / get_rho(self.x) > y:
            self.x = xp
        

