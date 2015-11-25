# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:39:12 2015

@author: sbhal
"""

import numpy as np
from scipy import ndimage

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
def im2double(im):
    min_val = np.min(im.ravel())
    max_val = np.max(im.ravel())
    out = (im.astype('float') - min_val) / (max_val - min_val)
    return out
xGrad = np.array([-1, 1]).reshape(2,1)
yGrad = np.array([[-1], [1]])


def getElement (r, c, energyImage):
    rows, cols = energyImage.shape
    if (r <0) or (r >= rows) or (c<0) or (c >= cols) :
        return 1e10
    else:
        return energyImage[r][c]

def energy_image (im):
    gray_img = rgb2gray(im)
    double_img = im2double(gray_img)
    xconvolution = ndimage.convolve(double_img, xGrad, mode='constant', cval=0.0)
    yconvolution = ndimage.convolve(double_img, yGrad,  mode='constant', cval=0.0)
    gradient_img = np.sqrt(np.square(xconvolution) + np.square(yconvolution))
    return im2double(gradient_img)
    
def energy_image_2 (im):
    gray_img = rgb2gray(im)
    double_img = im2double(gray_img)
    dx = ndimage.sobel(im, 0)  # horizontal derivative
    dy = ndimage.sobel(im, 1)  # vertical derivative
    mag = numpy.hypot(dx, dy)  # magnitude
    mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
    scipy.misc.imsave('sobel.jpg', mag)
    #gradient_img = ndimage.filters.sobel(double_img, axis=-1, output=None, mode='reflect', cval=0.0) 
    return im2double(gradient_img)
