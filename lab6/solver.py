import numpy as np

from const import DZ, WIDTH, HEIGHT, Mu
from utils import get_flux, get_vortocity, get_y


class Solver:
    def __init__(self, Q: float = -1):
        self.flux = np.zeros((WIDTH, HEIGHT))
        self.vorticity = np.zeros((WIDTH, HEIGHT))
        self.Q = Q

    def setup(self):
        for i in range(HEIGHT):
            y = get_y(i)
            self.flux[0, i] = get_flux(y, self.Q)
            self.flux[-1, i] = self.flux[0, i]
            self.vorticity[0, i] = get_vortocity(y, self.Q)
            self.vorticity[-1, i] = self.vorticity[0, i]
        y = get_y(0)
        self.flux[:, 0] = get_flux(y, self.Q)
        self.vorticity[:, 0] = get_vortocity(y, self.Q)
        y = get_y(HEIGHT-1)
        self.flux[:, -1] = get_flux(y, self.Q)
        self.vorticity[:, -1] = get_flux(y, self.Q)

    def calculate_next_flux(self):
        for i in range(1, WIDTH-1):
            for j in range(1, HEIGHT - 1):
                self.flux[i, j] = 0.25 * (self.flux[i+1, j] + self.flux[i-1, j] + self.flux[i, j-1] + self.flux[i, j+1] - self.vorticity[i, j] * DZ**2)

    def calculate_next_vorticity(self):
        for i in range(1, WIDTH-1):
            for j in range(1, HEIGHT-1):
                term1 = self.vorticity[i+1, j] + self.vorticity[i-1, j] + self.vorticity[i, j-1] + self.vorticity[i, j+1]
                term1 /= 4
                term2 = (self.flux[i, j+1] - self.flux[i, j-1]) * (self.vorticity[i+1, j] - self.vorticity[i-1, j]) - (self.flux[i+1, j] - self.flux[i-1, j]) * (self.vorticity[i, j+1] - self.vorticity[i, j-1])
                term2 /= 16
                self.vorticity[i, j] = term1 - term2
        


    def calculate_next_state(self):
        self.calculate_next_flux()
        self.calculate_next_vorticity()
