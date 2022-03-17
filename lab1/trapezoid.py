from matplotlib.axes import Axes
from body import Body
from constants import M, x_0, v_0
from plots import plot_group
import numpy as np
import matplotlib.pyplot as plt


def get_x(x1: float, x2: float, v1: float, v2: float) -> np.ndarray:
    return np.array([x2 - x1, v2 - v1])


def trapezoid(alpha: float, dt: float, range: float, first: bool = True, subdir: str = "other", axph=plt):

    body = Body(M, x_0, v_0, alpha, dt)
    body.calculate_trapezoid(range=range)
    plot_group(body, dt, alpha, range, subdir, first, axph)

