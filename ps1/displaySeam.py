# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:18:10 2015

@author: sbhal
"""
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt

def displaySeam (im, seam, type):
    plt.figure(1)
    if (type == 'HORIZONTAL'):
        plt.plot(range(len(seam)), seam)
        plt.title('Horizontal Seam')
#        for cols in range(im.shape[1]):
#                im[seam[cols]][cols] = [255, 255, 255];
    elif (type == 'VERTICAL'):
            plt.plot(seam, range(len(seam)))
            plt.title('Vertical Seam')
#        for row in range(im.shape[0]):
#                im[row][seam[row]] = [255, 255, 255];
    else:
        print "Error in displaySeam"
    
    
 
    plt.hold(True)
        
    plt.imshow(im)
#    plt.hold(True)
    #plt.plot(seam, range(len(seam)))
    plt.show()
    imsave("output_with_seam.jpg", im)
