import matplotlib.pyplot as plt
import os
from typing import Union, List
import numpy as np
from constants import dx


def create_dir(path: str):
    """
    Creates directory if it doesn't exist already
    """
    if not os.path.exists(path):
        print(f"[INFO]::Creating a directory: {path}")
        os.makedirs(path)
        print(f"[SUCCESS]::directory creation completed!")


def plot(x: Union[np.ndarray, List[np.ndarray]], y: Union[np.ndarray, List[np.ndarray]], title: str = "", xlabel: str = "", ylabel: str = "", subdir: str = "other", legend: List[str] = None, ax=plt):
    """
    Creates a plot or a group of plots
    """
    plt.cla()
    if isinstance(x, list) and isinstance(y, list) and isinstance(legend, list):
        for xi, yi, l in zip(x, y, legend):
            # print((xi, yi, l))
            ax.plot(xi, yi, label=l)
    elif isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        # print(ax)
        ax.plot(x, y)
    else:
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
        # plt.show()
    else:
        if legend:
            ax.legend()
        if title:
            ax.set_title(title)
        if ylabel:
            ax.set_ylabel(ylabel)


def derivative(func, x0: float) -> float:
    """
    Computes derivative of a function f where x=x0
    """
    dy = func(x0+dx) - func(x0)
    return dy/dx


def V(x: Union[np.ndarray, float]) -> Union[np.ndarray, float]:
    """
    Custom Potential Energy dependent of position
    """
    return -np.exp(-x**2)-1.2*np.exp(-(x-2)**2)  # J


def Ek(m: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Calculates Kinematic Energy 
    """
    return 0.5 * m * v ** 2
