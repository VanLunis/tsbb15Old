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
    steps = 0;
    currErr = 10000000
    dEst = 0;

    left = math.floor(x-width/2)
    top = math.floor(y-height/2)
    right = left + width
    bot = top + height

    Ig, Jg, Jgdx, Jgdy = gradCalc(I, J, 6, 1)

    #Windowed versions of all images
    JgdxWin = Jgdx[top:bot,left:right]
    JgdyWin = Jgdy[top:bot,left:right]
    IgWindowed = Ig[top:bot,left:right]
    JgWin = Jg[top:bot,left:right]

    #print('Shape of IgWin: ' + str(IgWin.shape))

    JgOld = Jg
    JgdxOld = Jgdx
    JgdyOld = Jgdy

    '''
    # First itteration outsdie of loop, in order to window
    T = estimateT(Jgdx, Jgdy, x, y, [height,width])
    e = estimateE(Ig, Jg, Jgdx, Jgdy, x, y, [height,width])
    dEst = np.linalg.solve(T,e)
    Jg, Jgdx, Jgdy = interpolImage(JgOld, JgdxOld, JgdyOld, dEst, int(round(top+dEst[1])), int(round(bot+dEst[1])), int(round(left+dEst[0])), int(round(right+dEst[0])))

    x = math.floor(width/2)
    y = math.floor(height/2)
    left = math.floor(x-width/2)
    top = math.floor(y-height/2)
    right = left + width
    bot = top + height

    print('********Results**********')
    print('Step: ' + str(steps))
    print('dEst: ' + str(dEst))
    print('*********End of step**********')
    '''


    while ((steps < maxSteps) and (currErr > maxErr)):
        T = estimateT(Jgdx, Jgdy, x, y, [height,width])
        e = estimateE(IgWindowed, Jg, Jgdx, Jgdy, math.floor(width/2), math.floor(height/2), [height,width])
        dEst = dEst + np.linalg.solve(T,e)

        x = int(round(x+dEst[0]))
        y = int(round(y+dEst[1]))
        left = math.floor(x-width/2)
        top = math.floor(y-height/2)
        right = left + width
        bot = top + height

        print('x: ' + str(x))
        print('y: ' + str(y))
        print('top: ' + str(top))
        print('bot: ' + str(bot))
        print('left: ' + str(left))
        print('right: ' + str(right))

        Jg, Jgdx, Jgdy = interpolImage(JgOld, JgdxOld, JgdyOld, dEst, top, bot, left, right)

        error = e.sum
        steps = steps + 1

        print('********Results**********')
        print('Step: ' + str(steps))
        print('dEst: ' + str(dEst))
        print('********End of step***********')



    return dEst
