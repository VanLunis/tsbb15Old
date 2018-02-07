# Lab2 test
import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cvl_labs.lab1 import load_lab_image, get_cameraman
import cvl_labs.lab2
from scipy.ndimage.interpolation import shift as intepShift

from calcLp2d import lp2Dfilter
from gradCalc import gradCalc
from toGray import rgb2gray
from tEstimate import tEstimateAll
from eEstimate import eEstimateAll
from lkSingleScale import lkEquation

#I = mpimg.imread('forwardL/forwardL0.png')
#J = mpimg.imread('forwardL/forwardL1.png')

#I = load_lab_image('chessboard_5.png')
#J = load_lab_image('chessboard_6.png')

cornerIm = load_lab_image('cornertest.png')

I = cornerIm
rows = I.shape[0]
cols = I.shape[1]
J = np.empty([rows,cols])

for y in range(1,rows):
    for x in range(2,cols-1):
        J[y,x] = I[y-1,x-2]
        # d = (2,1)

fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)
for im, name, ax in zip((I, J), ('I', 'J'), axes.flat):
    ax.imshow(im, cmap='gray')
    ax.set_title(name)


ksize = 6
sigma = 3
maxErr = -1

#help(cvl_labs.lab2)
V = lkEquation(I, J, maxErr, sigma, ksize)
cvl_labs.lab2.gopimage(V)





# test lk equation
'''
(df, lp2D)              = lp2Dfilter(ksize,sigma)
(Ig, Jg, Jgdx, Jgdy)    = gradCalc(I, J, df, lp2D)
(T11, T12, T22)         = tEstimateAll(Jgdx, Jgdy, lp2D)
(ex, ey)                = eEstimateAll(Ig, Jg, Jgdx, Jgdy, lp2D)
# Tensor and error for a redion around all points. Needs gaussfilt?

matrisX = np.multiply(T22,ex) - np.multiply(T12,ey)
matrisY = np.multiply(T12,ey) - np.multiply(T12,ex)

detT = T11*T22 - np.power(T12,2)
detTinv = np.divide(np.ones(detT.shape),detT)

deltaX = np.multiply(detTinv,matrisX)
deltaY = np.multiply(detTinv,matrisY)

V = np.empty([I.shape[0], I.shape[1], 2])
V[:,:,0] = deltaX
V[:,:,1] = deltaY
'''

#Test show deltaX, deltaY
'''
plt.figure()
plt.title('dx')
plt.imshow(dx, cmap='gray')
plt.figure()
plt.title('dy')
plt.imshow(dy, cmap='gray')
'''

# Test show lp-filter and lpgrad-filter
'''
plt.figure()
plt.title('Ig')
plt.imshow(Ig, cmap='gray')
plt.figure()
plt.title('Jg')
plt.imshow(Jg, cmap='gray')
plt.figure()
plt.title('Jgdx')
plt.imshow(Jgdx, cmap='gray')
plt.figure()
plt.title('Jgdy')
plt.imshow(Jgdy, cmap='gray')
'''





plt.show()
