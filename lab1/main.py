
from re import sub
from typing import Tuple, Union, List
import matplotlib.pyplot as plt
import numpy as np
import os
M = 1  # kg
x_0 = 2.83228  # m
v_0 = 0

dx = 1e-3


def create_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def plot(x: Union[np.ndarray, List[np.ndarray]], y: Union[np.ndarray, List[np.ndarray]], title: str = "", xlabel: str = "", ylabel: str = "", subdir: str = "other", legend: list[str] = None):
    if isinstance(x, list) and isinstance(y, list) and isinstance(legend, list):
        for xi, yi, l in zip(x, y, legend):
            # print((xi, yi, l))
            plt.plot(xi, yi, label=l)
    elif isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        plt.plot(x, y)
    else:
        raise Exception("Wrong type")
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    plt.tight_layout()
    path = f"images/{subdir}"
    create_dir(path)
    plt.savefig(f"{path}/{title}.png")
    plt.show()



def derivative(func, x0: float) -> float:
    dy = func(x0+dx) - func(x0)
    return dy/dx


def V(x: Union[np.ndarray, float]) -> Union[np.ndarray, float]:
    return -np.exp(-x**2)-1.2*np.exp(-(x-2)**2)  # J


def Ek(m: np.ndarray, v: np.ndarray) -> np.ndarray:
    return 0.5 * m * v ** 2


class Body:
    def __init__(self, mass: float, x0: float, v0: float, alpha: float, dt: float = 1e-3) -> None:
        self.mass = mass
        self.x = x0
        self.v = v0
        self.dt = dt
        self.alpha = alpha
        self.past_positions = [x0]
        self.past_velocities = [v0]
        self.past_times = [0]
        self.x0 = x0
        self.v0 = v0

    def get_next_x_euler(self) -> float:
        output = self.x + self.v * self.dt
        return output

    def get_next_v_euler(self) -> float:
        output = self.v - 1 / self.mass * \
            derivative(V, self.x) * self.dt - self.alpha * self.v * self.dt
        return output

    def get_next_euler(self) -> Tuple[float, float]:
        return self.get_next_x_euler(), self.get_next_v_euler()


    def reset_data(self):
        self.x = self.x0
        self.v = self.v0
        self.past_positions = [self.x]
        self.past_velocities = [self.v]
        self.past_times = [0]

    def calculate_euler(self, range: float):
        t = 0
        while t <= range:
            self.x, self.v = self.get_next_euler()
            t += self.dt
            self.past_positions.append(self.x)
            self.past_velocities.append(self.v)
            self.past_times.append(t)
        self.past_positions = np.array(self.past_positions)
        self.past_velocities = np.array(self.past_velocities)
        self.past_times = np.array(self.past_times)
        self.Eks = Ek(self.mass, self.past_velocities)
        self.Vs = V(self.past_positions)




def euler(alpha: float, dt: float, range: float, first: bool = True, subdir: str = "other"):
    body = Body(M, x_0, v_0, alpha=alpha, dt=dt)
    body.calculate_euler(range=range)
    if first:
        plot(
            body.past_times,
            body.past_positions,
            title=f"x(t), dt={dt}, alpha={alpha}, range={range}",
            subdir=subdir

        )
        plot(
            body.past_times,
            body.past_velocities,
            title=f"v(t), dt={dt}, alpha={alpha}, range={range}",
            subdir=subdir


        )
        plot(
            [body.past_times] * 3,
            [body.Eks, body.Vs, body.Vs + body.Eks],
            title=f"E(t), dt={dt}, alpha={alpha}, range={range}",
            subdir=subdir,
            legend=["Ek(t)", "V(t)", "Ec(t)"]

        )

    else:
        plot(
            body.past_positions,
            body.past_velocities,
            title=f"v(x), dt={dt}, alpha={alpha}, range={range}",
            subdir=subdir
        )

def trapezoid(alpha: float, dt: float, range: int, first: bool = True, subdir: str = "other"):
    body = Body(M, x_0, v_0, alpha, dt)



def exercise(method, alpha, dt, subdir):
    method(alpha=alpha, dt=dt, range=30, subdir=subdir)
    method(alpha=alpha, dt=dt, range=100, first=False, subdir=subdir)
    method(alpha=alpha, dt=dt, range=1000, first=False, subdir=subdir)


def exercise1(method=euler):
    for i, dt in enumerate([0.01, 0.001]):
        exercise(method, alpha=0, dt=dt, subdir=f"ex1/{i}")


def exercise2(method=euler):
    for i, alpha in enumerate([0.5, 5, 201]):
        exercise(method, alpha, dt=0.01, subdir=f"ex2/{i}")


def main():
    exercise1()
    exercise2()


if __name__ == "__main__":
    main()
