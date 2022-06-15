import numpy as np
from nomad import Nomad


class Solver:
    def __init__(self, is_2d=False):
        self.nomad = Nomad(is_2d)
        self.is_2d = is_2d
        self.data = []


    def calculate(self, n):
        for i in range(n):
            if i % 100 == 0: print(i, end="\r")
            self.data.append(self.nomad.x)
            self.nomad.make_step()
        self.data = np.array(self.data)

    def get_moment(self, l, n):
        return (self.data[:l] ** n).mean()

    def get_potential_energy(self, l):
        return 0.5 * (self.data[:l, 0] ** 2 + self.data[:l, 1] ** 2).mean()
    
    def get_potential_energies(self, l):
        return 0.5 * (self.data[l, 0] ** 2 + self.data[l, 1] ** 2)

    def save_to_file(self):
        np.save("data" if not self.is_2d else "data2d", self.data)

    def load_from_file(self):
        self.data = np.load("data.npy" if not self.is_2d else "data2d.npy")