import numpy as np
import matplotlib.pyplot as plt

from const import COLS, ROWS


def get_obsticle():
    output = np.zeros((ROWS, COLS))
    output[30:70, 95:105] = 1
    plt.imshow(output)
    plt.show()