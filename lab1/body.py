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
        print("[INFO]::Calculating Euler...")
        while t <= range:
            self.x, self.v = self.get_next_euler()
            t += self.dt
            self.past_positions.append(self.x)
            self.past_velocities.append(self.v)
            self.past_times.append(t)
        print("[SUCCESS]::Calculations completed!")
        self.past_positions = np.array(self.past_positions)
        self.past_velocities = np.array(self.past_velocities)
        self.past_times = np.array(self.past_times)
        self.Eks = Ek(self.mass, self.past_velocities)
        self.Vs = V(self.past_positions)