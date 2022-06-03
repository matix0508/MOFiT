import matplotlib.pyplot as plt
from solver import Solver

from utils import get_obsticle, plot_grid
import os


def ex1():
    s = Solver()
    tmax = 1000
    if os.path.exists("data/ex1flux.npy"):
        s.load_from_file("ex1")
    else:
        s.calculate(tmax, "ex1")
    plot_grid(s.flux, "Flux")
    plot_grid(s.vorticity, "Vorticity")

def ex2():
    s = Solver(obsticle=True)
    tmax = 1000
    if os.path.exists("data/ex2flux.npy"):
        s.load_from_file("ex2")
    else:
        s.calculate(tmax, "ex2")
    plot_grid(s.flux, "Flux")
        



def main():
    # ex1()
    ex2()



if __name__ == "__main__":
    main()