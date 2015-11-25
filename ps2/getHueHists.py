# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 23:49:51 2015

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


def getHueHists(origImg, k):
    hsv_img = matplotlib.colors.rgb_to_hsv(origImg)

    hist1 = np.histogram(hsv_img[:,:,0],k)

    k_means_hue = cluster.KMeans(k, n_init=4)
    k_means_hue.fit(hsv_img[:,:,0].reshape((-1,1)))

    meanHues = k_means_hue.cluster_centers_.squeeze()
    labels = (k_means_hue.labels_).reshape((hsv_img.shape[0],hsv_img.shape[1]))
    index_of_closestClust = np.zeros((hsv_img.shape[0],hsv_img.shape[1]))
    for i in range(hsv_img.shape[0]):
        for j in range(hsv_img.shape[1]):
            index_of_closestClust[i,j] = int(k_means_hue.predict(hsv_img[i,j,0]))
            #print "index ",index_of_closestClust[i,j]
    hist2 = np.histogram(index_of_closestClust.reshape(-1),k)
    plt.figure()
    plt.hist(hsv_img[:,:,0].reshape(-1), bins=k, color='red')
    plt.title('histogram uniform')
    plt.figure()

    plt.hist(index_of_closestClust.reshape(-1), bins=k, color='blue')
    plt.title('histogram  Clustered')
    #plt.show()
    #print "the size of bincount is: ", hist2.shape 
    return hist1, hist2

if __name__ == "__main__":
    im = np.array(Image.open('fish.jpg'))
    getHueHists(im, 5)
