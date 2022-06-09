import numpy as np
from nomad import Nomad


class Solver:
    def __init__(self):
        self.nomad = Nomad(0)
        self.data = []


    def calculate(self, n):
        for i in range(n):
            self.data.append(self.nomad.x)
            self.nomad.make_step()
        self.data = np.array(self.data)

    def get_moment(self, l, n):
        return (self.data[:l] ** n).mean()

    def save_to_file(self):
        np.save("data", self.data)

    def load_from_file(self):
        self.data = np.load("data.npy")