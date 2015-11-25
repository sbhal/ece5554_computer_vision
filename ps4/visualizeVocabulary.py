# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:34:10 2015

@author: sbhal
"""
#from IPython import get_ipython
#get_ipython().magic('reset -sf')

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
#import hickle as hkl


def rgb2gray_matlab(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.587, 0.114])
    
# specific frame dir and siftdir
framesdir = 'frames/'
siftdir = 'sift/'


fnames = glob.glob(siftdir + '*.mat')
fnames = [i[-27:] for i in fnames]

print 'reading %d total files...' %(len(fnames))

N = 100 #to visualize a sparser set of the features


# In[3]:
allDes = np.empty((0, 128))
allPos = np.empty((0, 2))
allScal = np.empty((0, 1))
allOri = np.empty((0, 1))
imgIdx = np.empty((0, 128))
imgAcc = np.empty((480, 704, 0), dtype=np.uint)
pathIdx = np.empty((0, 1))
# Loop through all the data files found
for i in range(len(fnames)):
    print 'reading frame %d of %d' %(i, len(fnames))
    
    # load that file
    fname = siftdir + fnames[i]
    
    mat = scipy.io.loadmat(fname)
    numfeats = mat['descriptors'].shape[0]
    print "numfeats is ", numfeats
    #read the associated image
    imname = framesdir + fnames[i][:-4]

    allDes = np.vstack((allDes, mat['descriptors']))
    allPos = np.vstack((allPos, mat['positions']))
    allScal = np.vstack((allScal, mat['scales']))
    allOri = np.vstack((allOri, mat['orients']))

    desMap = np.tile(i, numfeats)

    imgIdx = np.append(imgIdx, desMap)
    
    imgAcc = np.dstack((imgAcc, np.uint(rgb2gray_matlab(misc.imread(imname)))))

    pathFeats = np.tile(mat['imname'],(numfeats,1))
    
    pathIdx = np.vstack((pathIdx, pathFeats))
    
#k = 1500
k = 150

from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
whiten(allDes)
centroid, kmeans_label = kmeans2(allDes, k)
#kmeans_label, means = kmeans(allDes, k, iter=50)
hkl.dump(centroid, 'centroid.hkl')
hkl.dump(kmeans_label, 'kmeans_label.hkl')
#centroid = hkl.load('centroid.hkl')
#kmeans_label = hkl.load('kmeans_label.hkl')
#%%

#sampleIdx = np.random.randint(0, k, (2))
sampleIdx = np.array([3, 102])

for h in sampleIdx:
    foundFeatureIdxs = np.where(kmeans_label == h)[0]
    #foundFeatureIdxs = np.array(foundFeatureIdxs)
    print "sample idx is ", h, " with size ", foundFeatureIdxs.size
    fig=plt.figure()
    for l in range(6):
        featureIdx = foundFeatureIdxs[l]
        print "for loop starting ", l, " and featureIdx is ", featureIdx
        impath = pathIdx[featureIdx, :]

        im = misc.imread(framesdir+impath[0])
        
        patch_num = featureIdx
        print "patch_num is ", patch_num
        img_patch = getPatchFromSIFTParameters(allPos[patch_num,:], allScal[patch_num], allOri[patch_num], rgb2gray_matlab(im))
    
        
        ax=fig.add_subplot(2,3,l+1)
        #ax.imshow(im)
        print img_patch.size
        ax.set_title("%d" %featureIdx)
        ax.imshow(img_patch,  cmap = cm.Greys_r)
    plt.show()
        


