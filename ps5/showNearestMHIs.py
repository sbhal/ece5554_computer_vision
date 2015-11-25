# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:16:02 2015

@author: siddh
"""
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import cv2
import os
from computeMHI import computeMHI
from huMoments import huMoments
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#change k to change input image
k = 16

basedir = './'
actions = ['botharms', 'crouch', 'leftarmup', 'punch', 'rightkick']
allMHIs_counter = 0
allMHIs = np.empty((480,640,20), dtype=np.float32)
allMoments = np.empty((20,7), dtype=np.float64)
for actionnum in range(len(actions)):
    subdirname = basedir + actions[actionnum] + '/'
    subdir = os.listdir(subdirname)
    for seqnum in range(len(subdir)):
        allMHIs[:,:,allMHIs_counter] = computeMHI(subdirname + subdir[seqnum])
        allMoments[allMHIs_counter,:] = huMoments(allMHIs[:,:,allMHIs_counter])
        allMHIs_counter += 1

allMoments = allMoments/np.linalg.norm(allMoments)
testMoments = allMoments[k,:]
allLabels = [i for i in xrange(1,6) for j in xrange(4)]
allLabels = np.array(allLabels)


neigh = KNeighborsClassifier(n_neighbors=5)
#neigh.fit([trainMHI[:,:,i].flatten() for i in xrange(20)], trainLabels)
#print(neigh.predict([testMHI.flatten()]))
neigh.fit(allMoments, allLabels)
dist, ind = neigh.kneighbors(testMoments, n_neighbors=4)

fig=plt.figure()
ax=fig.add_subplot(3,2,1)
ax.set_title("Input")
ax.imshow(allMHIs[:,:,k], cmap = cm.Greys_r)
for i in xrange(ind.size):
    bx=fig.add_subplot(3,2,i+3)
    bx.set_title("Nearest - %d" %i)
    bx.imshow(allMHIs[:,:,ind[0][i]], cmap = cm.Greys_r)
#    cv2.imshow("pic %d"%i, allMHIs[:,:,i])
plt.show()
if 0xFF & cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()