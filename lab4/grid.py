import numpy as np
from const import DX

from utils import rho


class Grid:
    def __init__(self, n, iterations=1000, w=1, search_w: bool = False, eps: float = 0.1):
        self.grid = np.zeros((2*n+1, 2*n+1))
        self.n = n
        self.a_arr = []
        self.rho_arr = np.zeros((2*n+1, 2*n+1))
        self.rho_org = np.zeros((2*n+1, 2*n+1))
        self.iterations = iterations
        self.w = w
        self.search_w = search_w
        self.eps = eps
        self.stopped_iteration = None

    def __repr__(self):
        return str(self.grid)

    def get_a(self):
        output = 0
        for i in range(1, self.grid.shape[0]-1):
            for j in range(1, self.grid.shape[1]-1):
                part1 = (self.grid[i+1, j] - self.grid[i-1, j]) / (2*DX)
                part1 = 0.5*part1**2
                part2 = (self.grid[i, j+1] - self.grid[i, j-1]) / (2*DX)
                part2 = 0.5*part2**2
                part3 = -self.rho_org[i, j] * self.grid[i, j]
                output += part1 + part2 + part3
        return output * DX**2

    def get_rhop(self, i, j):
        return - (self.grid[i+1, j] + self.grid[i-1, j] + self.grid[i, j-1] + self.grid[i, j+1] - 4*self.grid[i, j]) / DX**2

    def fill_rho(self):
        for i in range(1, self.grid.shape[0]-1):
            for j in range(1, self.grid.shape[1]-1):
                self.rho_org[i, j] = rho(i, j)

    def fill(self):
        for i in range(1, self.grid.shape[0]-1):
            for j in range(1, self.grid.shape[1] -1):
                self.grid[i, j] = (1-self.w) * self.grid[i, j] + self.w * 0.25 * (self.grid[i+1, j] + self.grid[i-1, j] + self.grid[i, j+1] + self.grid[i, j-1] + self.rho_org[i, j]*DX**2)
    def calculate(self):
        print("Start calculating")
        self.fill_rho()
        print("Filled rho")
        print("starting iterations")
        for i in range(self.iterations):
            self.fill()
            self.a_arr.append(self.get_a())
            if self.search_w:
                if abs(self.a_arr[i] - self.a_arr[i-1]) < self.eps and i > 1:
                    self.stopped_iteration = i
                    return i
        print("finished iterations")
        for i in range(1, self.grid.shape[0]-1):
            for j in range(1, self.grid.shape[1]-1):
                self.rho_arr[i, j] = self.get_rhop(i, j)
        print("finished calculating")


    def save_to_file(self, filename):
        print("Saving to file")
        np.save(filename + ".npy", self.grid)
        np.save(filename + "_a.npy", self.a_arr)
        np.save(filename + "_rho.npy", self.rho_arr)
        np.save(filename + "_rho_org.npy", self.rho_org)
        print("Saved to file")

    def load_from_file(self, filename):
        print("Loading from file")
        self.grid = np.load(filename + ".npy")
        self.a_arr = np.load(filename + "_a.npy")
        self.rho_arr = np.load(filename + "_rho.npy")
        self.rho_org = np.load(filename + "_rho_org.npy")
        print("Loaded from file")
