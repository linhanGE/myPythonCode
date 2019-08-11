# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:31:49 2019

@author: c3216945
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:38:09 2019

@author: c3216945
"""

import numpy as np
import vtk
from vtk.numpy_interface import dataset_adapter as dsa
import glob
import re
import os

cwd = os.getcwd()
caseName = os.path.basename(cwd)

def getZ(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    usg = dsa.WrapDataObject( reader.GetOutput() )
    z = usg.Points[:,2]
    z = z[z!=0]
    return z

def getY(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    usg = dsa.WrapDataObject( reader.GetOutput() )
    y = usg.Points[:,1]
    y = y[y!=0]
    return y

def getX(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    usg = dsa.WrapDataObject( reader.GetOutput() )
    x = usg.Points[:,0]
    x = x[x!=0]
    return x

cwd = cwd +'/DEM/post/'
os.chdir(cwd)

f = glob.glob('run*.vtk')

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

f = natural_sort(f)

n = np.arange(0,len(f))
k = np.arange(len(n))

minz = np.zeros(len(n))
maxz = np.zeros(len(n))
minx = np.zeros(len(n))
maxx = np.zeros(len(n))
miny = np.zeros(len(n))
maxy = np.zeros(len(n))

outPutName = caseName + '_region.txt'

for i in k:
    minz[i]  = np.min(getZ(f[n[i]]))
    maxz[i]  = np.min(getZ(f[n[i]]))
    minx[i]  = np.min(getX(f[n[i]]))
    maxx[i]  = np.max(getX(f[n[i]]))
    miny[i]  = np.min(getY(f[n[i]]))
    maxy[i]  = np.max(getY(f[n[i]]))    
    
    with open(outPutName,'a') as storeData:
        storeData.write("%s %s %s %s %s %s \n"%(str(minx[i]),str(maxx[i]),str(miny[i]),str(maxy[i]),str(minz[i]),str(maxz[i])))