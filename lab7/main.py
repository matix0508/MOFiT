import os
from matplotlib import pyplot as plt
import numpy as np
from utils import plot_moments
from solver import Solver

l_arr = list(range(0, 1000000, 2000))
def ex1():
    solver = Solver()
    if not os.path.exists("data.npy"):
        solver.calculate(int(1e7))
        solver.save_to_file()
    else:
        solver.load_from_file()
    I1 = []
    I2 = []
    I3 = []
    I4 = []
    if not os.path.exists("moment.npy"):
        for l in l_arr:
            I1.append(solver.get_moment(l, 1))
            I2.append(solver.get_moment(l, 2))
            I3.append(solver.get_moment(l, 3))
            I4.append(solver.get_moment(l, 4))
        np.save("moment.npy", [I1, I2, I3, I4])
    else:
        I1, I2, I3, I4 = np.load("moment.npy")
    
    plot_moments(l_arr, I1, I2, I3, I4)

def ex2():
    solver = Solver(True)
    if not os.path.exists("data2d.npy"):
        solver.calculate(int(1e7))
        solver.save_to_file()
    else:
        solver.load_from_file()
    if not os.path.exists("energy.npy"):
        Ep = []
        for l in l_arr:
            Ep.append(solver.get_potential_energy(l))
        np.save("energy", Ep)
    else:
        Ep = np.load("energy.npy")

    
    plt.plot(Ep)
    plt.show()


    # plt.plot(solver.data[:, 0], solver.data[:, 1])
    # plt.show()
def main():
    ex1()
    ex2()
    


if __name__ == "__main__":
    main()