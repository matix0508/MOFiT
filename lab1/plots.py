from typing import Union, List

from matplotlib.axes import Axes
from body import Body
import numpy as np
import matplotlib.pyplot as plt
from utils import create_dir



def plot(x: Union[np.ndarray, List[np.ndarray]], y: Union[np.ndarray, List[np.ndarray]], title: str = "", xlabel: str = "", ylabel: str = "", subdir: str = "other", legend: List[str] = None, ax=plt):
    """
    Creates a plot or a group of plots
    """
    plt.cla()
    if isinstance(x, list) and isinstance(y, list) and isinstance(legend, list):
        for xi, yi, l in zip(x, y, legend):
            ax.plot(xi, yi, label=l)
    elif isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        ax.plot(x, y)
    else:
        print(type(x), type(y), type(legend))
        raise Exception("Wrong type")

    if ax == plt:

        if title:
            plt.title(title)
        if ylabel:
            plt.ylabel(ylabel)

        if xlabel:
            plt.xlabel(xlabel)

        plt.tight_layout()
        path = f"images/{subdir}"
        create_dir(path)
        plt.savefig(f"{path}/{title}.png")
    else:
        if legend:
            ax.legend()
        if title:
            ax.set_title(title)
        if ylabel:
            ax.set_ylabel(ylabel)


def plot_group(body: Body, dt: float, alpha: float, max_time: float,  subdir: str, first: bool, axph: Axes):
    """
    plots a group of graphs
    """
    if first:
        fig, [ax1, ax2, ax3] = plt.subplots(3, 1, sharex=True)
        print("[INFO]::Plotting x(t)...")
        plot(
            body.past_times,
            body.past_positions,
            title=rf"$x(t)$, $\Delta t={dt}$, $\alpha={alpha}$ $(0,{max_time}s)$",
            subdir=subdir,
            ax=ax1

        )
        print("[INFO]::Plotting v(t)...")
        plot(
            body.past_times,
            body.past_velocities,
            title=rf"$v(t)$, $\Delta t={dt}$, $\alpha={alpha}$ $(0,{max_time}s)$",
            subdir=subdir,
            ax=ax2
        )
        print("[INFO]::Plotting E(t)...")
        plot(
            [body.past_times] * 3,
            [body.Eks, body.Vs, body.Vs + body.Eks],
            title=rf"$E(t)$, $\Delta t={dt}$, $\alpha={alpha}$ $(0,{max_time}s)$",
            subdir=subdir,
            legend=[r"$Ek(t)$", r"$V(t)$", r"$Ec(t)$"],
            ax=ax3
        )
        create_dir("output")
        fig.tight_layout()
        path = f"output/alpha {alpha} st {dt} range {max_time}.png"
        fig.savefig(path)
        print(f"[SUCCESS]::Saved Figure in {path}")

    else:
        print("[INFO]::Plotting v(x)...")
        plot(
            body.past_positions,
            body.past_velocities,
            title=rf"$v(x)$ $\Delta t={dt}$, $\alpha={alpha}$ ${max_time}s$",
            subdir=subdir,
            ax=axph
        )