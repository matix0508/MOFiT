import os
from matplotlib import pyplot as plt
import numpy as np

from mstring import String
from const import N, DT, DX, TIME_LENGTH
from animator import Animator
from utils import zero


class Hanlder:
    def __init__(self):
        self.solvers = {}
        self.animations = {}
        self.trash = []
    
    def fixed(self, animate = True):
        print("Start fixed")
        s = String(100)
        s.calculate("fixed")
        self.solvers["fixed"] = s
        if animate:
            a = Animator(s)
            a.create()
            self.animations["fixed"] = a

    def loose(self, animate = True):
        print("Start loose")
        s = String(100, True)
        s.calculate("loose")
        self.solvers["loose"] = s
        if animate:
            a = Animator(s)
            a.create()
            self.animations["loose"] = a


    def damping(self, animate = True):
        print("Start damping")
        solvs = []
        anims = []
        for b in (0.5, 2, 4):
            s = String(100, False, 0.5)
            s.calculate(f"damping_{b}")
            solvs.append(s)
            if animate:
                a = Animator(s, name=f"{b}")
                a.create()
                anims.append(a)
        self.solvers["damping"] = solvs
        self.animations["damping"] = anims

    def forced(self, animate = True):
        print("Start forced")
        s = String(100, False, 1, 50, np.pi/2, initial=zero)
        s.calculate("forced")
        self.solvers["forced"] = s
        if animate:
            a = Animator(s, True)
            a.create()
            self.animations["forced"] = a

    def resonance(self, animate: bool = True, x0: int = 50):
        print("Start resonance")
        w = np.linspace(0, 10*np.pi, 10)
        E = []
        self.solvers['resonance'] = []
        self.animations['resonance'] = []
        for w_i in w:
            s = String(100, False, 1, x0, w_i, initial=zero)
            print(f"w: {int(w_i/3.14)}")
            s.calculate(f"resonance{int(w_i/3.14)}_{x0}")
            self.solvers['resonance'].append(s)
            E.append(s.average_energy(16, 20))
            if animate:
                a = Animator(s, name=f"{w_i//np.pi}")
                a.create()
                self.animations['resonance'].append(a)
        print(E)
        plt.clf()
        plt.scatter(w, E)
        plt.xlabel("w")
        plt.ylabel("E")
        plt.title(f"Resonance x0 = {x0}")
        plt.savefig(f"output/E(w)_{x0}.png")
        



    def save_animation(self, name: str):

        if name == "resonance":
            print(self.animations[name])
            print(isinstance(self.animations[name], list))
        if isinstance(self.animations[name], list):
            for a in self.animations[name]:
                path = f"output/{name}_{a.name}.gif"
                if os.path.exists(path):
                    q = input(f"File {path} already exists. Do you want to overwrite? (y/n)")
                    if q != "y":
                        return

                print("Saving animation...")
                a.anim.save(path, writer='imagemagick')
                return
        path = f"output/{name}.gif"
        if os.path.exists(path):
            q = input(f"File {path} already exists. Do you want to overwrite? (y/n): ")
            if q != "y":
                return
        self.animations[name].anim.save(path, writer="imagemagick")

    def save_animations(self):
        for name in self.animations:
            self.save_animation(name)
