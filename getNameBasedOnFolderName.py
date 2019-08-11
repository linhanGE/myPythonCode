import numpy as np
import vtk
import glob
import re
from vtk.util.numpy_support import vtk_to_numpy
import os
from numpy import linalg as LA

cwd = os.getcwd()
caseName = os.path.basename(cwd)

def getCol(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    polydata = reader.GetOutput()
    points = polydata.GetPoints()
    array = points.GetData()
    p = vtk_to_numpy(array)
    p = p[p[:,2]!=0]
    sepD = LA.norm(p,axis=1)
    rp = 0.0015
    rb = 0.05
    noc =  len(sepD[sepD<=rp+rb])
    return noc

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

outPutName = caseName + '_collision.txt'

for i in k:
    noc = getCol(f[n[i]])
    with open(outPutName,'a') as storeData:
        storeData.write("%s \n"%(str(noc)))
#        np.savetxt(storeData, noc, delimiter=' ')