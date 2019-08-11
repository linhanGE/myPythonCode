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
    headIndex = n1[n3[:,0]<=-0.4]
    tailIndex = n1[n3[:,0]>=0.4]
    m = tailIndex - headIndex[0]
    p1 = headIndex[0,:].reshape(1,5)
    p2 = tailIndex[np.where(m[:,3]>0)]
    
    sampleZ = 7
    sampledP = np.linspace(p1[0,3],p2[0,3],num=sampleZ,endpoint=False)
    sampledP = sampledP[1:]

    k = np.arange(sampleZ-1)
    posOnLine = np.zeros((sampleZ-1,sampleSize+1))
    uOnline = np.zeros((sampleZ-1,sampleSize+1))
    
    for z,i in zip(sampledP,k):
        # find the nearest point in grid
        # targetP = pts[np.abs(pts[:,2]-z).argmin()]
        targetP1 = [0,0.0825,z]
        targetP2 = [0,-0.0825,z]
        line = pv.Line(targetP1,targetP2,resolution=sampleSize)
        
        sampled = line.sample(data)
        sampleUz = sampled['U'][:,2]
        posOnLine = sampled['Distance']
        uOnline[i,:] = sampleUz
    return p1,p2,sampledP,posOnLine,uOnline

n = np.arange(len(f))

sampleSize = 30

u0 = np.zeros((len(n),sampleSize+1))
u1 = np.zeros((len(n),sampleSize+1))
u2 = np.zeros((len(n),sampleSize+1))
u3 = np.zeros((len(n),sampleSize+1))
u4 = np.zeros((len(n),sampleSize+1))
u5 = np.zeros((len(n),sampleSize+1))

for i in n:
    head,tail, posz,posy,u = getSlugUz(f[i],sampleSize)
   
    u0[i] = u[0,:]
    u1[i] = u[1,:]
    u2[i] = u[2,:]
    u3[i] = u[3,:]
    u4[i] = u[4,:]
    u5[i] = u[5,:]
    
    with open('head&tail.txt','a') as storeData:
        storeData.write("%s %s \n"%(str(head[0,3]), str(tail[0,3])))
    
with open('u0.txt','w') as storeData:
    np.savetxt(storeData, u0, delimiter=' ',newline='\n')

with open('u1.txt','w') as storeData:
    np.savetxt(storeData, u1,delimiter=' ',newline='\n')
    
with open('u2.txt','w') as storeData:
    np.savetxt(storeData, u2,delimiter=' ',newline='\n')

with open('u3.txt','w') as storeData:
    np.savetxt(storeData, u3, delimiter=' ',newline='\n')

with open('u4.txt','w') as storeData:
    np.savetxt(storeData, u4, delimiter=' ',newline='\n')

with open('u5.txt','w') as storeData:
    np.savetxt(storeData, u5, delimiter=' ',newline='\n')