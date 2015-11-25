# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:17:00 2015

@author: sbhal
"""

from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave

def reduceHeight (im, energyImage):
    cum_energy = cumulative_minimum_energy_map(energyImage, "HORIZONTAL")
    hSeam = find_optimal_horizontal_seam(cum_energy)
    new_im = np.empty_like(im)
    crop_im = new_im[:(im.shape[0]-1), :]
#    print "crop_im size is"
#    print crop_im.shape
    new_energy_map = np.empty_like(energyImage)
#    print "new_energy_map size is"
#    print new_energy_map.shape
    crop_energy_map = new_energy_map[:(energyImage.shape[0]-1), :]        
#    print "crop_energy_map size is" 
#    print crop_energy_map.shape
      
    for col in range(im.shape[1]):
        for row in range(im.shape[0]):
                if( row < hSeam[col]):
                    #print "Col is %d and hSeam[col] is %d" % (col, hSeam[col])
                    crop_im[row][col] = im[row][col]
                    crop_energy_map[row][col] = energyImage[row][col]
                elif(row == hSeam[col]):
                    pass                    
                else:
                    crop_im[row-1][col] = im[row][col]
                    crop_energy_map[row-1][col] = energyImage[row][col]
#    imsave("crop_output.jpg", crop_im)
    return crop_im, crop_energy_map
