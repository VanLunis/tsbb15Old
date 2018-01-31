import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def estimateE(Ig, Jg, Jgdx, Jgdy, x, y, window_size):
    IgWin = np.zeros((window_size[0],window_size[1],3))
    JgWin = np.zeros((window_size[0],window_size[1],3))
    left = math.floor(x-window_size[1]/2)
    top = math.floor(y-window_size[0]/2)
    right = left + window_size[1]
    bot = top + window_size[0]

    IgWin = Ig[top:bot,left:right]
    JgWin = Jg[top:bot,left:right]

    JgdxWin = Jgdx[top:bot,left:right]
    JgdyWin = Jgdy[top:bot,left:right]

    diff = IgWin-JgWin
    error = np.transpose([np.multiply(diff,JgdxWin), np.multiply(diff,JgdxWin)])
    error = error.sum(axis=1)
    error = error.sum(axis=0)
    return error
