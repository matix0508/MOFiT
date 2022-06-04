import numpy as np

from const import DZ, WIDTH, HEIGHT, Ik, Jk, Mu
from utils import get_flux, get_vortocity, get_x, get_y, inv_x_loc, inv_y_loc, is_in_obsticle
import os


class Solver:
    def __init__(self, Q: float = -1, obsticle: bool = False):
        self.flux = np.zeros((WIDTH, HEIGHT))
        self.vorticity = np.zeros((WIDTH, HEIGHT))
        self.Q = Q
        self.obsticle = obsticle

    def setup(self):
        print("Setting up...")
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
        self.vorticity[:, -1] = get_vortocity(y, self.Q)
        if self.obsticle:
            for i in range(WIDTH):
                for j in range(HEIGHT):
                    if is_in_obsticle(i, j):

                        self.flux[i, j] = get_flux(get_y(0), self.Q)
            # self.flux[inv_x_loc(-Ik):inv_x_loc(Ik), :inv_y_loc(Jk)] = 0
            # self.vorticity[inv_x_loc(-Ik):inv_x_loc(Ik), inv_y_loc(Jk)] = 0
            # self.flux[inv_x_loc(-Ik), :inv_y_loc(Jk)] = get_flux(0, self.Q)
            # self.flux[inv_x_loc(-Ik):inv_x_loc(Ik), inv_y_loc(Jk)] = get_flux(0, self.Q)
            # self.flux[inv_x_loc(Ik), :inv_y_loc(Jk)] = get_flux(0, self.Q)
        print("Done")

    def bondary_conditions(self):
        self.vorticity[:, -1] = 2 * (self.flux[:, -2] - self.flux[:, -1]) / DZ**2
        self.vorticity[:, 0] = 2 * (self.flux[:, 1] - self.flux[:, 0]) / DZ**2
        self.vorticity[inv_x_loc(-Ik), :inv_y_loc(Jk)+1] = 2*(self.flux[inv_x_loc(-Ik-1), :inv_y_loc(Jk)+1] - self.flux[inv_x_loc(-Ik), :inv_y_loc(Jk)+1]) / DZ**2
        self.vorticity[inv_x_loc(Ik), :inv_y_loc(Jk)+1] = 2*(self.flux[inv_x_loc(Ik+1), :inv_y_loc(Jk)+1] - self.flux[inv_x_loc(Ik), :inv_y_loc(Jk)+1]) / DZ**2

    def calculate(self, tmax: int, filename: str = "data"):
        self.setup()
        print("Calculating...")
        for i in range(tmax):
            if self.obsticle:
                self.bondary_conditions()
            self.calculate_next_state()
        print("Done")
        self.save_to_file(filename)



    def calculate_next_flux(self):
        for i in range(1, WIDTH-1):
            for j in range(1, HEIGHT - 1):
                if is_in_obsticle(i, j) and self.obsticle:
                    continue
                self.flux[i, j] = 0.25 * (self.flux[i+1, j] + self.flux[i-1, j] +
                                          self.flux[i, j-1] + self.flux[i, j+1] - self.vorticity[i, j] * DZ**2)

    def calculate_next_vorticity(self):
        for i in range(1, WIDTH-1):
            for j in range(1, HEIGHT-1):
                term1 = self.vorticity[i+1, j] + self.vorticity[i-1,
                                                                j] + self.vorticity[i, j-1] + self.vorticity[i, j+1]
                term1 /= 4
                term2 = (self.flux[i, j+1] - self.flux[i, j-1]) * (self.vorticity[i+1, j] - self.vorticity[i-1, j]) - (
                    self.flux[i+1, j] - self.flux[i-1, j]) * (self.vorticity[i, j+1] - self.vorticity[i, j-1])
                term2 /= 16
                self.vorticity[i, j] = term1 - term2

    def save_to_file(self, filename):
        if not os.path.exists("data"):
            os.mkdir("data")
            print("Creating data folder")
        np.save("data/"+filename + "flux", self.flux)
        np.save("data/" + filename + "vorticity", self.vorticity)
        print("Saved flux and vorticity to data/"+filename)

    def load_from_file(self, filename):
        self.flux = np.load("data/"+filename + "flux.npy")
        self.vorticity = np.load("data/"+filename + "vorticity.npy")
        print("Loaded flux and vorticity from data/"+filename)

    def calculate_next_state(self):
        self.calculate_next_flux()
        self.calculate_next_vorticity()
