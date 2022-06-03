import os

import numpy as np
from solver import Solver
from utils import get_obsticle, plot_grid


def main():
    if not os.path.exists("output"):
        os.mkdir("output")
    if not os.path.exists("data"):
        os.mkdir("data")
    solver = Solver(get_obsticle(), 0.5)
    
    if os.path.exists('data/potential.npy'):
        solver.grid = np.load('data/potential.npy')
    else:
        solver.setup_potential()
        solver.calculate("potential")
    solver.save_to_file("potential")
    plot_grid(solver.grid, get_obsticle(), "potential")

    solver = Solver(get_obsticle(), 1)
    if os.path.exists('data/flux.npy'):
        solver.grid = np.load('data/flux.npy')
    else:
        solver.setup_flux()
        solver.calculate("flux")
    solver.save_to_file("flux")
    plot_grid(solver.grid, get_obsticle(), "flux")

if __name__ == "__main__":
    main()