# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:38:02 2019

@author: c3216945
"""

import pyvista as pv
import numpy as np
import glob
import natsort 

f = glob.glob('*.vtk')
f = natsort.realsorted(f)

def calCentrifugal(filename,ub,dp,rhop):
    # calculate mass and volume
    Vp =  1/6*np.pi*dp**3
    mp = rhop*Vp
	
    # read data
    data = pv.read(filename)
    v = data.point_arrays['v']
    v = v - np.asarray([ub,0,0])
    f = data.point_arrays['f']
	
    ap = f/mp
    curva = np.sum(np.abs(np.cross(v,ap))**2,axis=-1)**(1./2)/(np.sum(np.abs(v)**2,axis=-1)**(1./2))**3
    f_cen = mp*np.sum(np.abs(v)**2,axis=-1)*curva
    magv = (np.sum(np.abs(v)**2,axis=-1)**(1./2)).reshape(len(v),1)
    v_unit = v/magv
	
	# bubble velocity
    bubbleV = v
    bubbleV[:,0] = ub
    bubbleV[:,1] = 0
    bubbleV[:,2] = 0
    
    # begin to calculate the direction vector of centrifugal force
    v_unitx = v_unit*np.asarray([1,0,0])
    v_unitx = v_unitx[:,0]
    ap_1 = ap[:,0]
    ap_1_unit = ap_1/np.abs(ap_1)
	
    # the direction of centrifugal force should be the opposite of the acceleration of the particle
    fcen_0 = -1*np.abs(v_unitx)*ap_1_unit

    xa = v_unit[:,0]*fcen_0
    b = v_unit[:,1]
    fcen_1 = -1*xa/b
    fcen_zero = np.zeros((len(v),3))
    fcen_zero[:,0] = fcen_0
    fcen_zero[:,1] = fcen_1
    magfcen_zero = np.sum((fcen_zero)**2,axis=-1)**(1./2)
    magfcen_zero = magfcen_zero.reshape(len(magfcen_zero),1)
    f_cenunit = np.divide(fcen_zero,magfcen_zero)
    f_cen = f_cen.reshape((len(f_cen),1))
    f_centrifugal = f_cenunit*f_cen
	
    # append results back to original vtk file
    data['f_centrifugal'] = f_centrifugal
    data['curvature'] = curva
    data['bubbleV'] = bubbleV
    data.save(filename,binary=False)

n = np.arange(len(f))

for i in n:
    calCentrifugal(f[i],31.34,0.0102,5.5)