import os
from utils import get_obsticle


def main():
    if not os.path.exists("output"):
        os.mkdir("output")
    if not os.path.exists("data"):
        os.mkdir("data")
    get_obsticle()

if __name__ == "__main__":
    main()