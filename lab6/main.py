import matplotlib.pyplot as plt
from solver import Solver

from utils import get_obsticle, get_u, get_v, inv_x_loc, plot_cross_section, plot_cross_u, plot_grid, plot_vel
import os


def ex1():
    print("Start ex1")
    s = Solver()
    tmax = 2000
    if os.path.exists("data/ex1flux.npy"):
        s.load_from_file("ex1")
        print("Loaded from file")
    else:
        s.calculate(tmax, "ex1")

    plot_grid(s.flux, "Flux", "flux_ex1", False)
    plot_cross_section(s.flux, inv_x_loc(0), "Flux", "flux_ex1_cross_0")
    plot_cross_section(s.flux, inv_x_loc(70), "Flux", "flux_ex1_cross_70")
    plot_grid(s.vorticity, "Vorticity", "vorticity_ex1", False)
    plot_cross_section(s.vorticity, inv_x_loc(0), "Vorticity", "vorticity_ex1_cross_0")
    plot_cross_section(s.vorticity, inv_x_loc(70), "Vorticity", "vorticity_ex1_cross_70")

    plot_cross_u(get_u(s.flux, 0), "u", "u_ex1")



def ex2(Q: float = -1):
    s = Solver(Q=Q, obsticle=True)
    tmax = 2000
    if os.path.exists(f"data/ex2_{Q}flux.npy"):
        s.load_from_file(f"ex2_{Q}")
    else:
        s.calculate(tmax, f"ex2_{Q}")
    plot_grid(s.flux, "Flux", f"flux_ex2_{Q}")
    plot_grid(s.vorticity, "Vorticity", f"vorticity_ex2_{Q}")
    plot_vel(get_u(s.flux), "u", f"u_ex2_{Q}")
    plot_vel(get_v(s.flux), "v", f"v_ex2_{Q}")



def main():
    if not os.path.exists("output"):
        os.mkdir("output")
        print("Created output folder")
    ex1()
    print("Start ex2")
    for q in [-1, -10, -100, -200, -400]:
        print(f"Q = {q}")
        ex2(q)


if __name__ == "__main__":
    main()
