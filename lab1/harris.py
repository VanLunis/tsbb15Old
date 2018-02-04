import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from orientTensor import calcOrientTensor

def calcHarris(Im, gradKsize, gradSigma, window_size, kappa):
    T11, T12, T22 = calcOrientTensor(Im, gradKsize, gradSigma, window_size);
    Ch = np.multiply(T11,T22) - np.multiply(T12,T12) -kappa*(T11+T22)
    return Ch

def cornerThresh(Im, gradKsize, gradSigma, window_size, kappa, thresh):
    Ch = calcHarris(Im, gradKsize, gradSigma, window_size, kappa)
    threshIm = np.multiply((Ch > thresh),Ch)
    return threshIm

def harrisMax(Im, gradKsize, gradSigma, window_size, kappa, thresh):
    threshIm = cornerThresh(Im, gradKsize, gradSigma, window_size, kappa, thresh)
    img_max = scipy.signal.order_filter(threshIm, np.ones((3,3), 9-1)
    
