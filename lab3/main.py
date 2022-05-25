from math import fabs
from matplotlib import pyplot as plt
from handler import Hanlder

def main():
    h = Hanlder()
    h.fixed(False)
    h.loose(False)
    h.damping(False)
    h.forced(False)
    h.resonance(False)
    h.resonance(False, x0=40)
    # h.save_animations()
    # plt.show()

if __name__ == "__main__":
    main()