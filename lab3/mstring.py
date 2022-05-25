import os
import numpy as np
import matplotlib.pyplot as plt

from const import N, DT, DX, TIME_LENGTH
from utils import get_derr_u, func


class String:
    def __init__(self, tmax: int, loose_end: bool = False, beta: float = 0, x0: int = 50, w: float = 0, initial=func):
        self.positions = np.zeros((TIME_LENGTH, N))
        self.velocities = np.zeros((TIME_LENGTH, N))
        self.t = np.linspace(0, tmax, TIME_LENGTH)
        self.loose = loose_end
        self.beta = beta
        self.x0 = x0
        self.w = w
        self.initial = initial

    def get_af(self, t: int, i: int):
        if i == self.x0:
            return np.cos(self.w*self.t[t])
        else:
            return 0

    def get_a(self, t: int, i: int, beta: float = 0):
        right = self.positions[t, i+1]
        left = self.positions[t, i-1]
        middle = self.positions[t, i]
        return (right + left - 2 * middle) / (DX**2) - 2 * beta * self.velocities[t, i]

    def get_next_v(self, t: int, i: int):
        return (self.velocities[t, i] + DT / 2 * (self.get_a(t+1, i)+self.get_a(t, i, self.beta) + self.get_af(t, i) + self.get_af(t+1, i))) / (1+self.beta*DT)

    def get_next_position(self, t: int, i: int):
        return self.positions[t, i] + DT * self.velocities[t, i]+DT**2/2*(self.get_a(t, i))

    def setup(self):
        print("Setting up...")

        for point in range(1, N-1):
            self.positions[0, point] = self.initial(point*DX)

        self.positions[0, 0] = 0
        self.positions[0, N-1] = 0

    def loose_end(self, t):
        self.positions[t, 0] = self.positions[t, 1]
        self.positions[t, N-1] = self.positions[t, N-2]

    def calculate(self, name: str = "", use_file: bool = True):
        # check if file exists
        if os.path.exists(f"output/{name}") and name:
            if use_file:
                print(f"Using file: {name}")
                self.read_file(f"output/{name}")
                return
            q = input("Data already exists. Do you want to use it? (y/n)")
            if q == "y":
                self.read_file(f"output/{name}")
                return

        self.setup()
        print("Calculating...")
        for t in range(len(self.t)-1):
            for point in range(1, N-1):
                self.positions[t+1, point] = self.get_next_position(t, point)
            if self.loose:
                self.positions[t+1, 0] = self.positions[t+1, 1]
                self.positions[t+1, N-1] = self.positions[t+1, N-2]
            for point in range(1, N-1):
                self.velocities[t+1, point] = self.get_next_v(t, point)
        print("Calculated.")
        if name:
            self.save_to_file(f"output/{name}")

    def energy(self, t):
        return 0.5 * np.sum(self.velocities[t, :]**2 + get_derr_u(self.positions[t, :], DX)**2) * DX

    def average_energy(self, t1, t2):
        return np.sum([self.energy(t) for t in range(t1, t2+1)]) / (t2-t1)

    def save_to_file(self, filename: str = ""):
        if not os.path.exists("./output"):
            os.makedirs("./output")
        if not filename:
            print("No filename given.")
            filename = f"output/string_{self.x0}_{self.w}.txt"
            print(f"Using default filename: {filename}")
        with open(filename, "w") as f:
            for t in range(len(self.t)):
                for point in range(N):
                    f.write(str(self.positions[t, point]) + " ")
                f.write("\n")

    def read_file(self, filename: str):
        print(f"Reading file: {filename}")
        with open(filename, "r") as f:
            for t in range(len(self.t)):
                line = f.readline()
                line = line.split(" ")
                while '' in line:
                    line.remove('')
                while '\n' in line:
                    line.remove('\n')
                for i, point in enumerate(line):
                    try:
                        self.positions[t, i] = float(point)
                    except ValueError:
                        print(f"Error at {t} {i}")
                        print(type(point))
                        print(f"point: xx{point}xx")
                        print(not point)
                        print(point == '')

    def plot(self):
        print("Plotting...")
        plt.plot(self.positions[5, :])
