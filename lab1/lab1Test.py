import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cvl_labs.lab1 import load_lab_image, get_cameraman

from gradCalc import gradCalc
from toGray import rgb2gray
from estimateT import estimateT
from estimateE import estimateE


'''
image = rgb2gray(mpimg.imread('baboon.png'))
jmage = rgb2gray(mpimg.imread('cameraman.png'))

Ig, Jg, Jgdx, Jgdy = gradCalc(image, jmage, 6, 3)

plt.figure()
plt.imshow(Ig, cmap='gray')

plt.figure()
plt.imshow(Jg, cmap='gray')

plt.figure()
plt.imshow(Jgdx, cmap='gray')

plt.figure()
plt.imshow(Jgdy, cmap='gray')

plt.show()

'''
'''
testIm = rgb2gray(mpimg.imread('cameraman.png'))
print(testIm.shape)
Ig, Jg, Jgdx, Jgdy = gradCalc(0, testIm, 6, 3)
T = estimateT(Jgdx, Jgdy, 128, 128, [256,256])

plt.figure()
plt.imshow(T[:,:,0], cmap='gray')
plt.show()

plt.figure()
plt.imshow(T[:,:,1], cmap='gray')
plt.show()

plt.figure()
plt.imshow(T[:,:,2], cmap='gray')
plt.show()
'''


I, J, dTrue = get_cameraman()
Ig, Jg, Jgdx, Jgdy = gradCalc(I, J, 6, 3)

error = estimateE(Ig, Jg, Jgdx, Jgdy, 120, 85, [70,40])
print(error)
