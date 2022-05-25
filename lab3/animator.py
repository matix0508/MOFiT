from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


from mstring import String
from const import N

class Animator:
    def __init__(self, s: String, small_limit: bool = False, name: str = ""):
        self.name = name
        self.s = s
        self.fig = plt.figure()
        self.axis = plt.axes()
        self.line, = self.axis.plot([], [], lw=3)
        if not small_limit:
            self.axis.set_xlim(0, 100)
            self.axis.set_ylim(-1, 1)
        else:
            self.axis.set_xlim(0, 100)
            self.axis.set_ylim(-0.005, 0.005)
        self.anim = None

    def init(self):
        self.line.set_data(range(N), self.s.positions[0, :])
        return self.line,

    def animate(self, i):
        self.line.set_data(range(N), self.s.positions[i*3, :])
        return self.line,
    
    def create(self):
        print("Creating animation...")
        self.anim = FuncAnimation(self.fig, self.animate, init_func=self.init, frames=int(len(self.s.t)/3), interval=60, blit=True)
        print("Animation created.")

        