
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



def derivative(func, x0: float, n: int = 1) -> float:
    """
    Computes derivative of a function f where x=x0
    """
    if n == 1:
        # computes first derivative
        dy = func(x0+dx) - func(x0)
        return dy/dx
    if n > 1:
        # reduces higher derivatives to lower ones
        dy = derivative(func, x0 + dx, n-1) - derivative(func, x0, n-1)
        return dy / dx




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
