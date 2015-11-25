# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:19:16 2015

@author: sbhal
"""

#from energy_image import getElement
import numpy as np

def getElement (r, c, energyImage):
    rows, cols = energyImage.shape
    if (r <0) or (r >= rows) or (c<0) or (c >= cols) :
        return float("inf")
    else:
        return energyImage[r][c]


def cumulative_minimum_energy_map (energyImage, seamDirection):
    rows, columns = energyImage.shape
    cum_cost = np.empty_like(energyImage)
    if(seamDirection == 'VERTICAL'):
        cum_cost[0, :] = energyImage[0, :]
        for r in range(1, rows):
            for c in range(columns):
                cum_cost[r][c] = energyImage[r][c] + min(getElement(r-1, c-1, energyImage), getElement(r-1, c, energyImage), getElement(r-1, c+1, energyImage))
    elif (seamDirection == 'HORIZONTAL'):
        cum_cost[:, 0] = energyImage[:, 0]
        
        for c in range(1, columns):
            for r in range(rows):
                cum_cost[r][c] = energyImage[r][c] + min(getElement(r, c-1, energyImage), getElement(r-1, c-1, energyImage), getElement(r+1, c-1, energyImage))
    else:
        print "Blunder"
    
    return cum_cost


"""             if(r == 4 and c == 1):
                    print '%.4f %.4f %.4f %.4f' % (getElement(r, c-1, energyImage), getElement(r-1, c-1, energyImage), getElement(r+1, c-1, energyImage), min(getElement(r, c-1, energyImage), getElement(r-1, c-1, energyImage), getElement(r+1, c-1, energyImage)))
                if(r == 4 and c == 2):
                    print '%.4f %.4f %.4f' % (getElement(r, c-1, energyImage), getElement(r-1, c-1, energyImage), getElement(r+1, c-1, energyImage))
                if(r == 5 and c == 3):
                    print '%.4f %.4f %.4f' % (getElement(r, c-1, energyImage), getElement(r-1, c-1, energyImage), getElement(r+1, c-1, energyImage))"""
