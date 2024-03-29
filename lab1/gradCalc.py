import numpy as np
import scipy
from scipy.signal import convolve2d as conv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def gradCalc(I, J, ksize, sigma):
    if sigma <= 0:
        sigma = 0.1

    lp = np.atleast_2d(np.exp(-0.5 * np.square(np.arange(-ksize,ksize,1)/sigma)))
    lp=lp/np.sum(lp)
    lp2D = conv2(lp, np.transpose(lp))
    df = np.atleast_2d(-1.0/np.square(sigma) * np.arange(-ksize,ksize,1) * lp)

    Ig = conv2(I, lp2D)

    Jg = conv2(J, lp2D)
    Jgdx = conv2(J, df, mode='same')
    Jgdy = conv2(J, np.transpose(df), mode='same')

    return (Ig, Jg, Jgdx, Jgdy)
