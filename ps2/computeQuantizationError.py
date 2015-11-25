# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 23:53:24 2015

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

def computeQuantizationError(origImg,quantizedImg):
    return np.sum((origImg[:,:,0:3]-quantizedImg[:,:,0:3])**2)

