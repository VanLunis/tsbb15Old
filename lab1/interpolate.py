import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage.interpolation import shift as intepShift

def interpolImage(Im, Jgdx, Jgdy, du, top, bot, left, right):
    newIm = intepShift(Im[top:bot,left:right], du, mode='nearest')
    newDx = intepShift(Jgdx[top:bot,left:right], du, mode='nearest')
    newDy = intepShift(Jgdy[top:bot,left:right], du, mode='nearest')
    return (newIm, newDx, newDy)
