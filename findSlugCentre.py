# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:35:35 2019

@author: c3216945
"""

import pyvista as pv
import numpy as np
import glob
import natsort 

f = glob.glob('*.vtk')
f = natsort.realsorted(f)

def getSlugUz(filename):
    # read vtk as unstructured data
    data = pv.read(filename)
    aw = data.point_arrays['alpha.water']
    pts = data.points
    
    # get alpha.water on the middle line
    aw = aw[(np.abs(pts[:,0])<=1e-4) & (np.abs(pts[:,1])<=1e-4)]
    pts= pts[(np.abs(pts[:,0])<=1e-4) & (np.abs(pts[:,1])<=1e-4)]
    # keep index
    ind = np.arange(len(aw)).reshape(len(aw),1)
    n1 = np.hstack((aw.reshape(len(aw),1),pts))
    n1 = np.hstack((n1,ind))
    # sort based on z
    n1 = n1[n1[:,3].argsort()]
    # delete first row
    n2 = np.delete(n1,(0),axis=0)
    # copy last row
    x = n2[-1,:]
    # append x as the last row of n2
    n2 = np.vstack((n2,x))
    # find bubble head and tail
    n3 = n1-n2
    headIndex = n1[n3[:,0]<=-0.2]
    tailIndex = n1[n3[:,0]>=0.2]
    m = tailIndex - headIndex[0]
    p1 = headIndex[0,:].reshape(1,5)
    p2 = tailIndex[np.where(m[:,3]>0)]
    return np.asarray([p1[0,3],p2[0,3]])

n = np.arange(len(f))
slug = np.zeros((len(f),2))

for i in n:
    slug[i,:] = getSlugUz(f[i])

with open('slugCentre.txt','a') as storeData:
    np.savetxt(storeData, slug, delimiter=' ',newline='\n')