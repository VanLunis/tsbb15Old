import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.signal import convolve2d as conv2

def eEstimateAll(Ig, Jg, Jgdx, Jgdy, lp2D):
    diff = Ig-Jg
    dx = np.array(Jgdx)
    dy = np.array(Jgdy)

    ex = diff*dx
    ey = diff*dy

    ex = conv2(ex, lp2D, mode='same')
    ey = conv2(ey, lp2D, mode='same')

    return (ex, ey)
