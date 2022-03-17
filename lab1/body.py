from utils import derivative
from typing import Tuple
import numpy as np
from utils import Ek, V


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
        self.debugging = False

    def debug(self, text):
        if self.debugging:
            print(text)

    def get_next_x_euler(self) -> float:
        """
        Calculates next position with euler method
        """
        output = self.x + self.v * self.dt
        return output

    def get_next_v_euler(self) -> float:
        """
        Calculates next velocity with euler method
        """
        output = self.v - 1 / self.mass * \
            derivative(V, self.x) * self.dt - self.alpha * self.v * self.dt
        return output

    def update(self, t: float):
        self.past_positions.append(self.x)
        self.past_velocities.append(self.v)
        self.past_times.append(t)
    
    def create_numpy_arr(self):
        self.past_positions = np.array(self.past_positions)
        self.past_velocities = np.array(self.past_velocities)
        self.past_times = np.array(self.past_times)
        self.Eks = Ek(self.mass, self.past_velocities)
        self.Vs = V(self.past_positions)

    def get_next_euler(self) -> Tuple[float, float]:
        """
        Return tuple of next position and velocity
        """
        return self.get_next_x_euler(), self.get_next_v_euler()


    def calculate_euler(self, range: float):
        """
        Computes array of positions, velovities and energies with euler method
        """
        t = 0
        self.debug("[INFO]::Calculating Euler...")
        while t <= range:
            self.x, self.v = self.get_next_euler()
            t += self.dt
            self.update(t)
            

        self.debug("[SUCCESS]::Calculations completed!")
        self.create_numpy_arr()

    def F1(self, xnext: float, vnext: float) -> float:
        self.debug(f"[INFO]::Calculating F1")
        return xnext - self.x - self.dt / 2 * (vnext + self.v)

    def F2(self, xnext: float, vnext: float) -> float:
        self.debug(f"[INFO]::Calculating F2")
        return vnext - self.v - self.dt / 2 * (-1 / self.mass * (derivative(V, xnext) - derivative(V, self.x)) - self.alpha * (vnext - self.v))

    def get_B(self, xnext, vnext):
        self.debug("[INFO]::Calculcating B vector")
        B = -np.array([self.F1(xnext, vnext), self.F2(xnext, vnext)])
        self.debug(f"[SUCCESS]::B: \n{B}")
        return B

    def get_A(self, xnext: float) -> np.ndarray:
        self.debug("[INFO]::Creating Matrix A")
        A = np.array([
            [1, -self.dt / 2],
            [self.dt / (2 * self.mass) * derivative(V, xnext, 2),
             1 + self.dt / 2 * self.alpha],
        ])
        self.debug(f"[SUCCESS]::A: \n{A}")
        
        return A


    def get_next_trapezoid(self) -> np.ndarray:
        eps = 1e-3
        X = np.array([10., 10.]) # x_mu, v_mu

        b = self.get_B(X[0], X[1])

        while abs(b[0]) > eps and abs(b[1]) > eps:
            solve_x = np.linalg.solve(self.get_A(X[0]
            ), b)
            X += solve_x
            b = self.get_B(X[0], X[1])
        return X[0], X[1]

    def calculate_trapezoid(self, range: float):
        t = 0
        self.debug("[INFO]::Calculating Trapezoid...")
        while t < range:
            self.x, self.v = self.get_next_trapezoid()
            self.update(t)
            t += self.dt
            # print(f"[PROGRESS]: {t/range * 100}%")
        
        self.create_numpy_arr()

