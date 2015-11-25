# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:18:40 2015

@author: sbhal
"""

from energy_image import getElement

def find_optimal_horizontal_seam(cumulativeEnergyMap):
    rows, columns = cumulativeEnergyMap.shape
    minEnergy = cumulativeEnergyMap[0][columns-1]
    minrow = 0
    for r in range(rows):
            if (minEnergy > min(minEnergy, getElement(r, columns-1, cumulativeEnergyMap))):
                minrow = r
                minEnergy = cumulativeEnergyMap[r][columns-1]
    colVector = []
    colVector.append(minrow)
    
    for c in reversed(range(columns-1)):
            minval = min(getElement( minrow,c, cumulativeEnergyMap), getElement(minrow-1,c, cumulativeEnergyMap), getElement(minrow+1, c, cumulativeEnergyMap))
            if minval == getElement( minrow, c, cumulativeEnergyMap):
                colVector.append(minrow)
            elif minval == getElement(minrow-1,c, cumulativeEnergyMap):
                colVector.append(minrow-1)
                minrow = minrow-1
            else:
                colVector.append(minrow+1)
                minrow = minrow+1

    return colVector[::-1]
