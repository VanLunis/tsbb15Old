import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from calcLp2d import lp2Dfilter
from gradCalc import gradCalc
from toGray import rgb2gray
from tEstimate import tEstimateAll
from eEstimate import eEstimateAll


def lkEquation(I, J, maxErr, sigma, ksize):
    if maxErr == 0:
        maxErr = -1

    (df, lp2D)              = lp2Dfilter(ksize,sigma)
    (Ig, Jg, Jgdx, Jgdy)    = gradCalc(I, J, df, lp2D)
    (T11, T12, T22)         = tEstimateAll(Jgdx, Jgdy, lp2D)
    (ex, ey)                = eEstimateAll(Ig, Jg, Jgdx, Jgdy, lp2D)
# Tensor and error for a redion around all points. Needs gaussfilt?

    matrisX = np.multiply(T22,ex) - np.multiply(T12,ey)
    matrisY = np.multiply(T12,ey) - np.multiply(T12,ex)

    detT = T11*T22 - np.power(T12,2)
    detT[detT == 0] = 0.00001 #To avoid div/0
    detTinv = np.divide(np.ones(detT.shape),detT)

    deltaX = np.multiply(detTinv,matrisX)
    deltaY = np.multiply(detTinv,matrisY)

    V = np.empty([I.shape[0], I.shape[1], 2])
    V[:,:,0] = deltaX
    V[:,:,1] = deltaY

    return V
