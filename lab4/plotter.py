from grid import Grid

from matplotlib import pyplot as plt


class Plotter:
    def __init__(self, grid: Grid):
        self.grid = grid

    def plot_a(self, filename):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot(self.grid.a_arr)
        ax.set_title("a")
        ax.set_xlabel("iteration")
        ax.set_ylabel("a")
        fig.savefig(f"output/a{filename}.png")

    def plot_rho(self, filename):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        t = ax.matshow(self.grid.rho_arr)
        fig.colorbar(t)
        ax.set_title('\u03C1')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.savefig(f"output/rho{filename}.png")

    def plot_org(self, filename):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        t = ax.matshow(self.grid.rho_org)
        fig.colorbar(t)
        ax.set_title('\u03C1 org')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.savefig(f"output/rho_org{filename}.png")

    def plot_rho_diff(self, filename):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        t =ax.matshow(self.grid.rho_arr - self.grid.rho_org)
        fig.colorbar(t)
        ax.set_title('\u03C1 diff')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.savefig(f"output/rho_diff{filename}.png")

    def plot_grid(self, filename):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        t = ax.matshow(self.grid.grid)
        fig.colorbar(t)
        ax.set_title('grid')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.savefig(f"output/grid{filename}.png")

    def plot_all(self, filename=""):
        self.plot_a(filename)  
        self.plot_rho(filename)
        self.plot_org(filename)
        self.plot_rho_diff(filename)
        self.plot_grid(filename)
