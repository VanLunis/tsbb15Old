import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from estimateT import estimateT

def calcOrientTensor(im, gradKsize, gradSigma, window_size):
    Ig, Jg, Jgdx, Jgdy = gradCalc(Im, Im, gradKsize, gradSigma)
    structTens = estimateT(Jgdx, Jgdy,)
