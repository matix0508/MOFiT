import matplotlib.pyplot as plt
from solver import Solver

from utils import get_obsticle, plot_grid


def main():
    s = Solver()
    s.setup()
    for i in range(100):
        s.calculate_next_state()
    plot_grid(s.flux)
    plot_grid(s.vorticity)


if __name__ == "__main__":
    main()