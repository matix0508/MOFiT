import os
from re import I
from matplotlib import pyplot as plt
from solver import Solver


def main():
    solver = Solver()
    if not os.path.exists("data.npy"):
        solver.calculate(int(1e7))
        solver.save_to_file()
    else:
        solver.load_from_file()
    l_arr = list(range(0, 1000000, 2000))
    I1 = []
    I2 = []
    I3 = []
    I4 = []
    for l in l_arr:
        I1.append(solver.get_moment(l, 1))
        I2.append(solver.get_moment(l, 2))
        I3.append(solver.get_moment(l, 3))
        I4.append(solver.get_moment(l, 4))
    plt.scatter(l_arr, I1)
    plt.scatter(l_arr, I2)
    plt.scatter(l_arr, I3)
    plt.scatter(l_arr, I4)
    plt.hlines([0, 0.5, 0.75], 0, 10**6, colors=["cyan", "orange", "purple"])
    plt.show()
    


if __name__ == "__main__":
    main()