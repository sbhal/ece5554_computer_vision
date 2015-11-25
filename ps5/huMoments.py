# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:10:33 2015

@author: siddh
"""
import cv2

def huMoments (H):
#    for i in range(allMHIs.shape[2]):
    moments = cv2.moments(H)
    output = cv2.HuMoments(moments)
    return output[:,0]
