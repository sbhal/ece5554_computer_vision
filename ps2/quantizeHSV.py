# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 23:51:02 2015

@author: siddh
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#import sklearn
from sklearn import cluster
from PIL import Image
import matplotlib 
from scipy.cluster import vq

def quantizeHSV(origImg, k):
    hsv_img = matplotlib.colors.rgb_to_hsv(origImg)
    k_means_hue = cluster.KMeans(k)
    k_means_hue.fit(hsv_img[:,:,0].reshape((-1,1)))
    meanHues = k_means_hue.cluster_centers_.squeeze()
    labels = (k_means_hue.labels_).reshape((hsv_img.shape[0],hsv_img.shape[1]))
    h_out = (np.array([meanHues[labels[I]] for I in np.ndindex(labels.shape)])).reshape((hsv_img.shape[0],hsv_img.shape[1]))
    hsv = np.dstack((h_out,hsv_img[:,:,1],hsv_img[:,:,2]))
    outputImg = matplotlib.colors.hsv_to_rgb(hsv) 
    plt.figure(figsize=(10,10))
    plt.imshow(outputImg.astype('uint8'))
    plt.title('HSV Quantized Image k= %d' % k)
    return outputImg,meanHues
if __name__ == "__main__":
    im = np.array(Image.open('fish.jpg'))
    im_hsv, meanHues = quantizeHSV(im, 3)
