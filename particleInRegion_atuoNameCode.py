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
from vtk.util.numpy_support import vtk_to_numpy
import os

cwd = os.getcwd()
caseName = os.path.basename(cwd)

def getCor(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
#    usg = dsa.WrapDataObject( reader.GetOutput() )
#    x = usg.Points[:,0]
#    x = x[x!=0]
#    y = usg.Points[:,1]
#    y = y[y!=0] 
#    z = usg.Points[:,2]
#    z = z[z!=0]
#    x = np.asarray(x).reshape(-1,1)
#    y = np.asarray(y).reshape(-1,1)
#    z = np.asarray(z).reshape(-1,1)
#    position = np.concatenate((x,y,z),axis=1)
    polydata = reader.GetOutput()
    points = polydata.GetPoints()
    array = points.GetData()
    numpy_nodes = vtk_to_numpy(array)
    numpy_nodes =numpy_nodes[numpy_nodes[:,0]!=0]
    return numpy_nodes

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

minz = -0.15
maxz = 0
minx = -0.05
maxx = 0.05
miny = -0.05
maxy = 0.05
noOfP = np.zeros(len(n))

outPutName = caseName + '_NoInRegion.txt'

for i in k:
    p = getCor(f[n[i]])
    newP = p[p[:,0]<=maxx]
    newP = newP[newP[:,0]>=minx]
    newP = newP[newP[:,1]<=maxy]
    newP = newP[newP[:,1]>=miny]
    newP = newP[newP[:,2]<=maxz]
    newP = newP[newP[:,2]>=minz]
    noOfP[i] = len(newP)
    with open(outPutName,'a') as storeData:
        storeData.write("%s \n"%(str(noOfP[i])))