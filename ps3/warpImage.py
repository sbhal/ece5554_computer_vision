# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:13:42 2015

@author: sbhal
"""

import math
import matplotlib.pyplot as plt
import numpy as np


#function [warpIm, mergeIm] =
def warpImage(inputIm, refIm, H):

        
    p,q = np.meshgrid(range(inputIm.shape[0]), range(inputIm.shape[1]), indexing="ij")
    
    #input_coordinates = np.array([p[:], q[:]])
    input_coordinates = np.vstack(([p[:].flatten(), q[:].flatten()]))
    #points = input_coordinates
    #
    #a = np.ones((1, points.shape[1],points.shape[2]))
    #points_homo = np.vstack((points, np.ones((1, points.shape[1],points.shape[2]), dtype=np.int)))
    input_coordinates_homo = np.vstack((input_coordinates, np.ones(input_coordinates.shape[1])))
    uvw = np.dot(H, input_coordinates_homo)
    xs = np.divide(uvw[0,:], uvw[2,:])
    ys = np.divide(uvw[1,:], uvw[2,:])
    output_coords = np.transpose(np.column_stack((xs, ys)))
    
    # dimensions of warped image
    warp_x_min = math.floor( min(output_coords[0,:]))
    warp_x_max = math.ceil(max(output_coords[0,:]))
    warp_y_min = math.floor( min(output_coords[1,:]))
    warp_y_max = math.ceil(max(output_coords[1,:]))
    x_min = min(0,        math.floor( min(output_coords[0,:])))
    x_max = max(refIm.shape[1], math.ceil(max(output_coords[0,:])))
    y_min = min(0,        math.floor( min(output_coords[1,:])))
    y_max = max(refIm.shape[0], math.ceil(max(output_coords[1,:])))
    
    x_width = x_max - (x_min+1)
    y_width = y_max - (y_min+1)
    
    warpMat = np.ones((y_width, x_width, 3));
    mergeMat = np.ones((y_width, x_width, 3));
    
    p,q = np.meshgrid(range(int(x_min),int(x_max)), range(int(y_min), int(y_max)));
    _ = np.vstack(([p[:].flatten(), q[:].flatten()]))
    warpIm_coords = np.vstack((_, np.ones(_.shape[1])))
    
    uvw = np.dot(np.linalg.inv(H), warpIm_coords)
    xs = np.divide(uvw[0,:], uvw[2,:])
    ys = np.divide(uvw[1,:], uvw[2,:])
    origIm_coords = np.transpose(np.column_stack((xs, ys)))
    
    for k in range(1,warpIm_coords.shape[1]):
        x_out = math.floor(warpIm_coords[0,k]);
        y_out = math.floor(warpIm_coords[1,k]);
        x_out_adjusted = max(0, x_out - x_min);
        y_out_adjusted = max(0, y_out - y_min);
        x_in = np.round(origIm_coords[0,k]);
        y_in = np.round(origIm_coords[1,k]);
        if x_in > 0 and x_in < inputIm.shape[1] and y_in > 0 and y_in < inputIm.shape[0] and x_out_adjusted < x_width and y_out_adjusted < y_width:
            for c in range(0,2):
                warpMat[y_out_adjusted, x_out_adjusted, c] = inputIm[y_in, x_in, c];
                mergeMat[y_out_adjusted, x_out_adjusted, c] = inputIm[y_in, x_in, c];
              
    for x in range(0,refIm.shape[1]):
        for y in range(0,refIm.shape[0]):
            for c in range(0,2):
                x_adjusted = x - x_min;
                y_adjusted = y - y_min;
                if y_adjusted > 0 and x_adjusted > 0 and y_adjusted < y_width and x_adjusted < x_width:
                    mergeMat[y_adjusted, x_adjusted, c] = refIm[y, x, c];

    return mergeMat, warpMat
