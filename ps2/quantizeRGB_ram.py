# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 23:52:10 2015

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

def quantizeRGB(im, k):

    n_clusters = 4
    np.random.seed(0)
    
    #im = array(Image.open('fish.jpg'))
    X = im.reshape((-1, 1))  # We need an (n_sample, n_feature) array
    features = []
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            R = im[x,y,0]
            G = im[x,y,1]
            B = im[x,y,2]
            features.append([R,G,B])
    X = features = np.array(features,'f')
    k_means = cluster.KMeans(n_clusters=n_clusters, n_init=4)
    k_means.fit(X)
    values = k_means.cluster_centers_.squeeze()
    labels = k_means.labels_
    
    # create an array from labels and values
    im_compressed = np.choose(labels, values)
    im_compressed.shape = im.shape
    
    vmin = im.min()
    vmax = im.max()
    
    # original lena
    plt.figure(1, figsize=(10,10))
    #plt.imshow(labels, cmap=plt.cm.gray, vmin=vmin, vmax=256)
    
    # compressed lena
    plt.figure(2, figsize=(10,10))
    plt.imshow(im_compressed, vmin=vmin, vmax=vmax)
    plt.title('RGB Quantized')
    return im_compressed, values

if __name__ == "__main__":
    im = np.array(Image.open('fish.jpg'))
    im_rgb, meanColors = quantizeRGB(im, 10)
