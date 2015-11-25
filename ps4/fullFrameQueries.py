# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:34:10 2015

@author: sbhal
"""

import numpy as np
import scipy.io
import glob
from scipy import misc
import matplotlib.pyplot as plt
from displaySIFTPatches import displaySIFTPatches
from selectRegion import roipoly
from getPatchFromSIFTParameters import getPatchFromSIFTParameters
from skimage.color import rgb2gray
import matplotlib.cm as cm
import pylab as pl
import hickle as hkl

# specific frame dir and siftdir
framesdir = 'frames/'
siftdir = 'sift/'

queryID = 7
hist = np.empty((centroid.shape[1], 0))
for i in range(len(fnames)):
    a_where = np.where(imgIdx == i)
    a_where2 = kmeans_label[a_where]
    a_hist = np.histogram(a_where2, centroid.shape[1])
    hist = np.hstack((hist, a_hist[0].reshape(128,1)))

# In[3]
simIdx = np.empty((0,2))
for l in range(len(fnames)):
    
    dj = hist[:,l]
    
    q = hist[:, queryID]
    print "q is ", q
    sim = np.sum(np.multiply(dj, q))
    print sim
    
    normal = np.linalg.norm(np.multiply(dj, np.linalg.norm(q)),2)
    print normal
    
    sim = sim/normal
    
    simIdx = np.vstack((simIdx, [sim, l]))
    
#%%
    
simIdx = np.sort(simIdx, axis=-0)[::-1]
fig=plt.figure()
pl.imshow(imgAcc[:, :, queryID],   cmap = cm.Greys_r)
fig=plt.figure()
#ax.imshow(im)
for i in range(3):
    ax=fig.add_subplot(1,3,i+1)
    ax.set_title("%d" %simIdx[i][1])
    ax.imshow(imgAcc[:, :, simIdx[i, 1]],  cmap = cm.Greys_r)
plt.show()