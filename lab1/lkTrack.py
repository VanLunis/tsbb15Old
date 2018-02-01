import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from gradCalc import gradCalc
from toGray import rgb2gray
from estimateT import estimateT
from estimateE import estimateE
from interpolate import interpolImage

def trackLK(I, J, x, y, height, width, maxSteps, maxErr):
    if maxErr == 0:
        maxErr = -1
    steps = 1;
    currErr = 10000000

    left = math.floor(x-width/2)
    top = math.floor(y-height/2)
    right = left + width
    bot = top + height

    Ig, Jg, Jgdx, Jgdy = gradCalc(I, J, 6, 3)

    #Windowed versions of all images
    JgdxWin = Jgdx[top:bot,left:right]
    JgdyWin = Jgdy[top:bot,left:right]
    IgWin = Ig[top:bot,left:right]
    JgWin = Jg[top:bot,left:right]

    JgOld = Jg
    JgdxOld = Jgdx
    JgdyOld = Jgdy

    print('Jgsape: ' + str(Jg.shape))
    print('Jgdxshape: ' + str(Jgdx.shape))
    print('Jgdyshape: ' + str(Jgdy.shape))

    # First itteration outsdie of loop, in order to window
    T = estimateT(Jgdx, Jgdy, x, y, [height,width])
    e = estimateE(Ig, Jg, Jgdx, Jgdy, x, y, [height,width])
    dEst = np.linalg.solve(T,e)
    Jg, Jgdx, Jgdy = interpolImage(Jg, Jgdx, Jgdy, dEst, top, bot, left, right)

    x = math.floor(width/2)
    y = math.floor(height/2)
    left = math.floor(x-width/2)
    top = math.floor(y-height/2)
    right = left + width
    bot = top + height




    while ((steps < maxSteps) and (currErr > maxErr)):
        T = estimateT(Jgdx, Jgdy, x, y, [height,width])
        e = estimateE(Ig, Jg, Jgdx, Jgdy, x, y, [height,width])
        dEst = np.linalg.solve(T,e)
        '''
        print('**********Before*************')
        print('Jgsape: ' + str(Jg.shape))
        print('Jgdxshape: ' + str(Jgdx.shape))
        print('Jgdyshape: ' + str(Jgdy.shape))
        '''
        Jg, Jgdx, Jgdy = interpolImage(Jg, Jgdx, Jgdy, dEst, top, bot, left, right)
        '''
        print('**********After*************')
        print('Jgsape: ' + str(Jg.shape))
        print('Jgdxshape: ' + str(Jgdx.shape))
        print('Jgdyshape: ' + str(Jgdy.shape))
        '''
        error = e.sum
        steps = steps + 1

        print('********Results**********')
        print('Step: ' + str(steps))
        print('dEst: ' + str(dEst))
        print('*******************')



    return dEst
