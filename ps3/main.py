# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:18:28 2015

@author: sbhal
"""

import numpy as np
from PIL import Image
from computeH import computeH
import matplotlib.pyplot as plt
from warpImage import warpImage

t1 = np.load('cc1.npy').transpose()
t2 = np.load ('cc2.npy').transpose()

H = computeH(t1, t2)

inputIm = np.array(Image.open('crop1.jpg'))
refIm = np.array(Image.open('crop2.jpg'))
    
warpIm, mergeIm = warpImage(inputIm, refIm, H)
plt.figure(1)
plt.imshow(mergeIm)
plt.figure(2)
plt.imshow(warpIm)

#%%
import scipy.io as sio
#t1 = sio.loadmat('points1.mat').transpose()
#t2 = sio.loadmat('points2.mat').transpose()

#t1 = [[90.16377295896746, 206.3963834707542, 156.9975240032448, 119.2219255869141, 239.3289564490938, 214.14522417154, 246.1091920622813, 323.5975990701392, 338.1266753841126, 369.1220381872556, 278.0731599530227, 355.5615669608804],
# [178.0639945273812, 117.0418740086932, 160.6291029506132, 204.2163318925333, 137.3825808482559, 191.6244657537563, 286.5477643383822, 227.4628539948906, 167.4093385638008, 244.8977455716586, 82.17209085515719, 131.5709503226665]]
#t2 = [1,2]

l1 =[[
  229.0000,  255.0000,  291.0000,  348.0000,  350.0000,  220.0000,  372.0000,  303.0000,  301.0000,  276.0000],
  [222.0000,  206.0000,   79.0000,  118.0000,   76.0000,  295.0000,  242.0000,  278.0000,   95.0000,   72.0000]]

l2 =[[ 
  238.0000,  231.0000,  341.0000,  224.0000,  274.0000,  199.0000,  113.0000,  151.0000,  305.0000,  373.0000],
   [80.0000,  106.0000,  303.0000,  283.0000,  387.0000,   33.0000,  131.0000,   76.0000,  286.0000,  310.0000]]
t1 = np.array(l1)
t2 = np.array(l2)
np.save('points1', t1)
np.save('points2', t1)
H = computeH(t1, t2)

inputIm = np.array(Image.open('wdc1.jpg'))
refIm = np.array(Image.open('wdc2.jpg'))
    
warpIm, mergeIm = warpImage(inputIm, refIm, H)
plt.figure(3)
plt.imshow(mergeIm)
plt.figure(4)
plt.imshow(warpIm)
