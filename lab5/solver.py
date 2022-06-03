import numpy as np
import matplotlib.pyplot as plt

from const import ROWS, COLS
from utils import get_phi, get_psi, plot_grid


class Solver:
    def __init__(self, obsticle, u0: float):
        self.grid = np.zeros((COLS, ROWS))
        self.obsticle = np.zeros((COLS, ROWS))
        self.u0 = u0

    def setup_potential(self):
        self.grid[0, 50:] = get_phi(0, self.u0)
        self.grid[-1, 50:] = get_phi(COLS-1, self.u0)
        for i in range(COLS):
            self.grid[i, -1] = get_phi(i, self.u0)
        for i in range(1, COLS-1):
            for j in range(50, ROWS-1):
                self.grid[i, j] = get_phi(i, self.u0)

    def potential_conditions(self):
        self.grid[:95, 50] = self.grid[:95, 51]
        self.grid[106:, 50] = self.grid[106:, 51]
        self.grid[95, 50:70] = self.grid[94, 50:70]
        self.grid[105, 50:70] = self.grid[106, 50:70]
        self.grid[95:105, 70] = self.grid[95:105, 71]
        self.grid[95, 70] = 0.5*(self.grid[94, 70] + self.grid[95, 71])
        self.grid[105, 70] = 0.5*(self.grid[105, 71] + self.grid[106, 70])


    def setup_flux(self):
        for j in range(50, ROWS):
            self.grid[0, j] = get_psi(j, self.u0)
            self.grid[-1, j] = get_psi(j, self.u0)
        self.grid[:, -1] = get_psi(ROWS-1, self.u0)
        self.grid[:95, 50] = self.grid[0, 50]
        self.grid[95:106, 70] = self.grid[0, 50]
        self.grid[106:, 50] = self.grid[0, 50]
        self.grid[95, 50:70] = self.grid[0, 50]
        self.grid[105, 50:70] = self.grid[0, 50]
        for i in range(1, COLS-1):
            for j in range(50, ROWS-1):
                if 95 <= i <= 105 and 30 <= j <= 70:
                    continue
                self.grid[i, j] = get_psi(j, self.u0)



    def get_next_point(self, i, j):
        if self.obsticle[i, j] == 0:
            self.grid[i, j] = 0.25 * (self.grid[i+1, j] + self.grid[i-1, j] + self.grid[i, j+1] + self.grid[i, j-1] )

    def calculate(self, name: str):
        for num in range(1000):
            print(num)
            if name == "potential":
                self.potential_conditions()
            for i in range(1, COLS-1):
                for j in range(51, ROWS-1):
                    if 95 <= i <= 105 and 30 <= j <= 70:
                        continue
                    self.get_next_point(i, j)


    def save_to_file(self, name: str):
        np.save(f"data/{name}", self.grid)
