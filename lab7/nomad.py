import numpy as np

from utils import get_rho, get_rho2D


class Nomad:
    def __init__(self, is_2d = False):
        self.is_2d = is_2d
        self.x = 0 if not is_2d else np.array([0, 0])

    def make_step(self):
        if self.is_2d:
            self.make_step2D()
            return
        dx = (np.random.rand() - 0.5) / 2
        xp = self.x + dx
        y = np.random.rand()
        if get_rho(xp) / get_rho(self.x) > y:
            self.x = xp

    def make_step2D(self):
        dr = (np.random.rand(2) - 0.5) / 2
        rp = self.x + dr
        y = np.random.rand()
        if get_rho2D(rp) / get_rho2D(self.x) > y:
            self.x = rp
        
        

