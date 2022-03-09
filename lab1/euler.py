import matplotlib.pyplot as plt
from body import Body
from utils import plot_group
from constants import M, x_0, v_0


def euler(alpha: float, dt: float, range: float, first: bool = True, subdir: str = "other", axph=plt):
    """
    Calculates values with euler method and creates plots
    """
    body = Body(M, x_0, v_0, alpha=alpha, dt=dt)
    body.calculate_euler(range=range)
    plot_group(body, dt, alpha, range, subdir, first, axph)
