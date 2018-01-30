import numpy as np
import scipy
import math
from scipy.signal import convolve2d as conv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def estimateT(Jgdx, Jgdy, x, y, window_size):
    T = np.zeros((window_size[0],window_size[1],3))
    left = math.floor(x-window_size[1]/2)
    top = math.floor(y-window_size[0]/2)
    right = left + window_size[1]
    bot = top + window_size[0]

    dx = Jgdx[top:bot,left:right]
    dy = Jgdy[top:bot,left:right]

    T[:,:,0] = dx*dx;
    T[:,:,1] = dx*dy;
    T[:,:,2] = dy*dy
    return(T)
