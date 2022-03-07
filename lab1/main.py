from body import Body
from typing import List
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from constants import M, x_0, v_0
from euler import euler

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})


def exercise(method, alpha, dt, subdir, ph: Axes = None):
    method(alpha=alpha, dt=dt, range=30, subdir=subdir)
    method(alpha=alpha, dt=dt, range=100,
           first=False, subdir=subdir, axph=ph[0])
    method(alpha=alpha, dt=dt, range=1000,
           first=False, subdir=subdir, axph=ph[1])


def exercise1(method=euler):
    fig_ph, axs = plt.subplots(2, 2)
    for i, dt in enumerate([0.01, 0.001]):
        exercise(method, alpha=0, dt=dt, subdir=f"ex1/{i}", ph=axs[i])
    fig_ph.tight_layout(pad=0.3)
    fig_ph.savefig("output/phases1.png")


def exercise2(method=euler):
    fig_ph, axs = plt.subplots(3, 2)
    for i, alpha in enumerate([0.5, 5, 201]):
        exercise(method, alpha, dt=0.01, subdir=f"ex2/{i}", ph=axs[i])
    fig_ph.tight_layout()
    fig_ph.savefig("output/phases2.png")


def main():
    exercise1()
    exercise2()


if __name__ == "__main__":
    main()
