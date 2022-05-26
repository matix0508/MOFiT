import os
from solver import Solver
from utils import get_obsticle


def main():
    if not os.path.exists("output"):
        os.mkdir("output")
    if not os.path.exists("data"):
        os.mkdir("data")
    solver = Solver(get_obsticle(), 0.5)
    solver.setup()

if __name__ == "__main__":
    main()