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
import matplotlib

fig, sfig = plt.subplots(1, 2, figsize=(10, 10))

im = np.array(Image.open('fish.jpg'))
cbar = sfig[0].imshow(im)
fig.colorbar(cbar)
sfig[0].set_title("normal")
#im_rgb, meanColors = quantizeRGB(im, 5)
k = 2
#def quantizeRGB(origImg, k):


#def quantizeHSV(origImg, k):
if 1:
    im_hsv = im
    print "im_hsv shape is ", im_hsv.shape
    features = []
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            R = im[x,y,0]
            G = im[x,y,1]
            B = im[x,y,2]
            features.append([R,G,B])
    features_temp = np.reshape(im_hsv,(im_hsv.shape[0]*im_hsv.shape[1],3))
    features = features_temp[:,0]
    # cluster
    codebook,variance = vq.kmeans2(features,k)
    print "codebook shape ", codebook.shape
    code,distance = vq.vq(features,codebook)
    # create image with cluster labels
    
    res = codebook[code]
    res = np.reshape(res,(im_hsv.shape[0],im_hsv.shape[1]))
    print "res shape", res.shape


    im[:,:,0] = res
    plt.imshow(im)
    im_rgb = matplotlib.colors.hsv_to_rgb(im_hsv)
    fig = plt.figure(figsize=(15,15))
    fig.add_subplot(1,2,1, title="")
    plt.imshow(im_hsv)
    fig.add_subplot(1,2,2, title="")
    #codeim = imresize(codeim,im.shape[:2],interp='nearest')
    plt.imshow(im_rgb)
    plt.show()
    #return codeim, codebook
