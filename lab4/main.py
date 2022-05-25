from matplotlib import pyplot as plt
import numpy as np
from grid import Grid
from plotter import Plotter
from const import N

import os


def main():
    if not os.path.exists("output"):
        os.mkdir("output")
    grid = Grid(N)
    if os.path.exists('output/grid.npy'):
        grid.load_from_file('output/grid')
    else:
        grid.calculate()
    grid.save_to_file("output/grid")
    plotter = Plotter(grid)
    plotter.plot_all()

    iters = []
    w_arr = np.linspace(1, 2, 50)
    if os.path.exists('output/iters.npy'):
        iters = np.load('output/iters.npy')
    else:
        for w in w_arr:
            grid2 = Grid(N, 1000, w, True)
            i = grid2.calculate()
            iters.append(i)
        iters = iters[:1]
    w_arr = w_arr[:-1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(w_arr, iters)
    fig.savefig("output/iters.png")
    np.save('output/iters', np.array(iters))
    grid_final = Grid(N, 1000, w_arr[iters.argmin()])
    if os.path.exists('output/grid_final.npy'):
        grid_final.load_from_file('output/grid_final')
    else:
        grid_final.calculate()
    grid_final.save_to_file('output/grid_final')
    plotter = Plotter(grid_final)
    plotter.plot_all("final")
    print(f"Final w is: {w_arr[iters.argmin()]}")

if __name__ == "__main__":
    main()