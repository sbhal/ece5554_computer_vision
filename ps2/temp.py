# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:23:07 2015

@author: sbhal
"""
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

# now, to clear the screen
cls()

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import vq
from scipy.misc import imresize
from PIL import Image

fig, sfig = plt.subplots(1, 2, figsize=(10, 10))

im = np.array(Image.open('fish.jpg'))
cbar = sfig[0].imshow(im)
fig.colorbar(cbar)
sfig[0].set_title("normal")
#im_rgb, meanColors = quantizeRGB(im, 5)
k = 4
#def quantizeRGB(origImg, k):


if 1:
    featuresl = []
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            R = im[x,y,0]
            G = im[x,y,1]
            B = im[x,y,2]
            featuresl.append([R,G,B])
    features = np.array(featuresl,'f')
    centroids,variance = vq.kmeans2(features,k)
    code,distance = vq.vq(features,centroids)
    codeim = code.reshape(im.shape[0],im.shape[1])
    quantized = np.zeros(im.shape)
    for (i,j),value in np.ndenumerate(codeim):
        quantized[i,j,:] = centroids[value]
    cbar = sfig[1].imshow(quantized)
    fig.colorbar(cbar)
    sfig[1].set_title("float")


    #sfig[1].imshow(quantized, vmin=0, vmax=1)
    plt.show()

    #return ret_im, centroids
#im = np.array(Image.open('fish.jpg'))
#im_rgb, meanColors = quantizeRGB(im, 5)