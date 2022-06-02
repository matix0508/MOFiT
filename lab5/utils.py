import numpy as np

from const import COLS, ROWS


def get_obsticle():
    output = np.zeros((COLS, ROWS))
    output[96:105, 30:70] = 1
    return output