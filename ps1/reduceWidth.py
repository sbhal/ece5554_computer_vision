# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:17:53 2015

@author: sbhal
"""

import numpy as np
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam


def reduceWidth (im, energyImage):
    cum_energy = cumulative_minimum_energy_map(energyImage, "VERTICAL")
    vSeam = find_optimal_vertical_seam(cum_energy)
    
    #new_im = np.zeros(im.shape[0], im.shape[1]-1)
    #new_energy_map = np.empty_like(energyImage)    
    new_im = np.empty_like(im)
    crop_im = new_im[:, :(im.shape[1]-1)]
#    print "crop_im size is"
#    print crop_im.shape
    new_energy_map = np.empty_like(energyImage)
#    print "new_energy_map size is"
#    print new_energy_map.shape
    crop_energy_map = new_energy_map[:, :(new_energy_map.shape[1]-1)]        
#    print "crop_energy_map size is" 
#    print crop_energy_map.shape
    
    for row in range(im.shape[0]):
        for col in range(im.shape[1]):
                if( col < vSeam[row]):
                    #print "Col is %d and vSeam[row] is %d" % (col, vSeam[row])
                    crop_im[row][col] = im[row][col]
                    crop_energy_map[row][col] = energyImage[row][col]
                elif(col == vSeam[row]):
                    pass
                else:
                    crop_im[row][col-1] = im[row][col]
                    crop_energy_map[row][col-1] = energyImage[row][col]
    return crop_im, crop_energy_map
