# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:36:14 2015

@author: sbhal
"""

import numpy as np
import math
from scipy import misc
from skimage import feature, filters
from scipy import ndimage
from PIL import Image
from scipy import misc
import matplotlib.pyplot as plt
import cv2


def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

fig, ax = plt.subplots(1, 2, figsize=(10, 10))

def detectCircles(img, r, useGradient):
    grayimg = rgb2gray(img)
    edges = cv2.Canny(img,100,200)
    ax[0].imshow(edges, cmap=plt.cm.gray)
    ax[0].set_title('after canny image operation')
    if useGradient == 0:
        accumulator1 = np.zeros(edges.shape)
        for (i,j),value in np.ndenumerate(edges):
            if value:
                for t_idx in np.arange(0,2*math.pi,math.pi/100):
                    a = int(i - (r * math.cos(t_idx)));
                    b = int(j + (r * math.sin(t_idx)));
                    if a>0 and b>0 and a < accumulator1.shape[0] and b < accumulator1.shape[1]:
                        accumulator1[a, b] += 1
        
        print accumulator1
        ax[1].imshow(accumulator1, cmap=plt.cm.gray)
        ax[1].set_title('Accumulator array without using gradient')
    else:
        dx = ndimage.sobel(grayimg, axis=0, mode='constant')
        dy = ndimage.sobel(grayimg, axis=1, mode='constant')
        accumulator = np.zeros(edges.shape)
        for (i,j),value in np.ndenumerate(edges):
            if value:
                gradient = math.atan(-dx[i,j]/(dy[i,j]+0.00001))
                for theta in np.arange(gradient-math.pi/4,gradient+math.pi/4,math.pi/100):
                    a = int(i - (r * math.cos(theta)));
                    b = int(j + (r * math.sin(theta)));
                    if a < accumulator.shape[0] and b < accumulator.shape[1]:
                        accumulator[a, b] += 1
        ax[1].imshow(accumulator, cmap=plt.cm.gray)
        ax[1].set_title('Accumulator array with gradient')
        print accumulator
    return 
if __name__ == "__main__":
    img = np.array(Image.open('jupiter.jpg'))
    detectCircles(img, 100, 0)