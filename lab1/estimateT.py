import numpy as np
import scipy
import math
from scipy.signal import convolve2d as conv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def estimateT(Jgdx, Jgdy, x, y, window_size):
    T = np.zeros((window_size[0],window_size[1],3))
    left = math.floor(x-window_size[1]/2)
    top = math.floor(y-window_size[0]/2)
    right = left + window_size[1]
    bot = top + window_size[0]

    dx = Jgdx[top:bot,left:right]
    dy = Jgdy[top:bot,left:right]

    T[:,:,0] = dx*dx;
    T[:,:,1] = dx*dy;
    T[:,:,2] = dy*dy

    # Displays for test purpouse

    plt.figure()
    plt.title('T11')
    plt.imshow(T[:,:,0], cmap='gray')

    plt.figure()
    plt.title('T12')
    plt.imshow(T[:,:,1], cmap='gray')

    plt.figure()
    plt.title('T22')
    plt.imshow(T[:,:,2], cmap='gray')

    #End display

    T = T.sum(axis=1)
    T = T.sum(axis=0)
    T11 = T[0]
    T12 = T[1]
    T22 = T[2]
    '''
    print('T: ')
    print(T11)
    print(T12)
    print(T22)
    '''

    Tmat = np.matrix([[T11, T12], [T12, T22]])
    '''
    print('Tmat: ')
    print(Tmat)
    '''
    return(Tmat)
