# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:18:57 2015

@author: sbhal
"""

from energy_image import getElement

def find_optimal_vertical_seam(cumulativeEnergyMap):
    rows, columns = cumulativeEnergyMap.shape
    minEnergy = cumulativeEnergyMap[rows-1][0]
    mincol = 0
    for c in range(columns):
            if minEnergy > min(minEnergy, getElement(rows-1, c, cumulativeEnergyMap)):
                mincol = c
                minEnergy = cumulativeEnergyMap[rows-1][c]

    colVector = []
    colVector.append(mincol)
    
    for r in reversed(range(rows-1)):
            minval = min(getElement(r, mincol, cumulativeEnergyMap), getElement(r, mincol-1, cumulativeEnergyMap), getElement(r, mincol+1, cumulativeEnergyMap))
            if minval == getElement(r, mincol, cumulativeEnergyMap):
                colVector.append(mincol)
            elif minval == getElement(r, mincol-1, cumulativeEnergyMap):
                colVector.append(mincol-1)
                mincol = mincol-1
            else:
                colVector.append(mincol+1)
                mincol = mincol=1
    return colVector[::-1]
