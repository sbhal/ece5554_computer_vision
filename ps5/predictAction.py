# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:09:02 2015

@author: siddh
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import normalize
import numpy as np



def predictAction(testMoments, trainMoments, trainLabels):
    neigh = KNeighborsClassifier(n_neighbors=5)
#neigh.fit([trainMHI[:,:,i].flatten() for i in xrange(20)], trainLabels)
#print(neigh.predict([testMHI.flatten()]))
#    trainMoments_norm = trainMoments/np.linalg.norm(trainMoments) #normalize(trainMoments, axis=1)
#    testMoments_norm = testMoments/np.linalg.norm(trainMoments) #normalize(testMoments, axis=1)
    neigh.fit(trainMoments, trainLabels)
    print(neigh.predict(trainMoments))
#    print(neigh.predict_proba(trainMoments))
    return neigh.predict(testMoments)

#print predictAction(testMoments, trainMoments, trainLabels)