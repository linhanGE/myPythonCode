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

def getSlugUz(filename,sampleSize):
    # read vtk as unstructured data
    data = pv.read(filename)
    aw = data.point_arrays['alpha.water']
    pts = data.points
    
    D = 0.2
    ## get alpha.water on the middle line
    aw = aw[(np.abs(pts[:,1]-0.1)<=1e-4) & (pts[:,2] == 0)]
    pts= pts[(np.abs(pts[:,1]-0.1)<=1e-4) & (pts[:,2] == 0)]
    n1 = np.hstack((aw.reshape(len(aw),1),pts))
    # sort based on x
    n1_sorted = n1[np.argsort(n1[:,1])]
    n1_diff = np.diff(n1_sorted[:,0])
    
    n1_sorted = np.delete(n1_sorted,-1,0)
    
    firstHead_index = np.argmax(n1_diff >= 0.2)
    firstTail_index = np.argmax(n1_diff <= -0.2)
    secondHead_index = np.argmax(n1_diff[firstHead_index+5:] >= 0.2) + firstHead_index+5
    secondTail_index = np.argmax(n1_diff[firstTail_index+5:] <= -0.2) + firstTail_index+5
    
    p1 = n1_sorted[firstHead_index,1]
    p2 = n1_sorted[firstTail_index,1]
    p3 = n1_sorted[secondHead_index,1]
    p4 = n1_sorted[secondTail_index,1]
    
    if p2 < p1 :
        ls1 = p4 - p1
        ls2 = 4-p3 + p2
        x_mid1 = 0.5*(p1 + p4)
        if p3 + p2 >4 :
            x_mid2 = 0.5*(p2 + p3) - 2
        else :
            x_mid2 = 2 + 0.5*(p2 + p3)
    else :
        ls1 = p2 - p1
        ls2 = p4 - p3
        x_mid1 = 0.5 * (p1 + p2)
        x_mid2 = 0.5 * (p3 + p4)
        
    sampleZ = 5
    sampleSize = 30
    
    sampledP = np.asarray([x_mid1, x_mid2])
    
    k = np.arange(sampleZ-1)
    posOnLine = np.zeros((sampleZ-1,sampleSize+1))
    uOnline = np.zeros((sampleZ-1,sampleSize+1))
    
    for x,i in zip(sampledP,k):
        # find the nearest point in grid
        # targetP = pts[np.abs(pts[:,2]-z).argmin()]
        targetP1 = [0,0.5*D,x]
        targetP2 = [0,-0.5*D,x]
        line = pv.Line(targetP2,targetP1,resolution=sampleSize)
        
        sampled = line.sample(data)
        sampleUz = sampled['U'][:,0]
        posOnLine = sampled['Distance']
        uOnline[i,:] = sampleUz
    return ls1,ls2,sampledP,posOnLine,uOnline

n = np.arange(len(f))

sampleSize = 30

u0 = np.zeros((len(n),sampleSize+1))
u1 = np.zeros((len(n),sampleSize+1))
u2 = np.zeros((len(n),sampleSize+1))

for i in n:
    ls1,ls2, posz,posy,u = getSlugUz(f[i],sampleSize)
   
    u0[i] = u[0,:]
    u1[i] = u[1,:]
    u2[i] = u[2,:]
    
    with open('L_slug.txt','a') as storeData:
        storeData.write("%s %s \n"%(str(ls1), str(ls2)))
    
with open('uz0.txt','w') as storeData:
    np.savetxt(storeData, u0, delimiter=' ',newline='\n')

with open('uz1.txt','w') as storeData:
    np.savetxt(storeData, u1,delimiter=' ',newline='\n')
    
with open('uz2.txt','w') as storeData:
    np.savetxt(storeData, u2,delimiter=' ',newline='\n')