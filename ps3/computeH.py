# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:08:45 2015

@author: sbhal
"""
import numpy as np

def computeH(t1, t2):
    pts1 = t1
    pts2 = t2
    #t1 = np.array([[1 , 2, 3], [1, 2 , 3]])
    #t2 = np.array([[1 , 2, 3], [1, 2, 3]])
    
    #t1 = np.append(t1, l_row, axis=0)
    #t2 = np.append(t2, l_row, axis=0)
    
    t1 = np.vstack((t1, np.ones(t1.shape[1])))
    t2 = np.vstack((t2, np.ones(t2.shape[1])))
    
    #L = np.zeros((2*n_points, 3*t1.shape[0]))
    L = np.array([]).reshape(0, 3*t1.shape[0])
    
    for ipoint in range(t1.shape[1]):
        piT = t1[:,ipoint].reshape(1,-1)
        xi_prime_multiply_piT = t2[0,ipoint] * piT
        yi_prime_multiply_piT = t2[1,ipoint] * piT
        
        appen = np.array(piT).reshape(1, -1)
        appen = np.append(appen, np.zeros(3).reshape(1, -1))
        appen = np.append(appen, -xi_prime_multiply_piT).reshape(1, -1)
        
        #L = np.append(L, [piT, np.zeros(3) , -xi_prime_multiply_piT])
        L = np.vstack((L, appen))
        #print "Jindabad", [piT, np.zeros(3) , -xi_prime_multiply_piT]
        
        appen = np.array(np.zeros(3)).reshape(1, -1)
        appen = np.append(appen, piT).reshape(1, -1)
        appen = np.append(appen, -yi_prime_multiply_piT).reshape(1, -1)
        
        L = np.vstack((L, appen))
    
    print pts2.flatten()
    sol = np.linalg.lstsq(L, pts2.flatten())[0]
    H = (sol/sol[-1]).reshape(t1.shape[0], t1.shape[0])
    return H
