# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:55:20 2018

@author: c3216945
"""
import numpy as np
import glob
import pandas as pd
#from vtk.util import numpy_support as VN
import vtk
import re

from vtk.util.numpy_support import vtk_to_numpy
import matplotlib.pyplot as plt

def calBedHeight(pos):
    z = 2
    pz =  pos[:,z]
    pz[::-1].sort()
    # topparticle =  np.zeros(5018)
    # nrp = 0
    # for i in np.arange(len(px)-1):
        # if nrp <=220 and np.abs(px[i]-px[i+1]) > 0.006 and np.abs(py[i]-py[i+1]) > 0.006:
            # topparticle [i] = 1
            # nrp +=1
    # toplayer = pz[np.nonzero(topparticle)[0]]
    hmean = np.abs(np.average(pz[0:594-1]))+0.0005
    return hmean

def geth(filename):
    #as_numpy = numpy_support.vtk_to_numpy(vtk_points.GetData())
    reader = vtk.vtkPolyDataReader()
    #reader = vtk.vtkGenericDataObjectReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    vtk_out = reader.GetOutput()
#    scalar_names = [reader.GetScalarsNameInFile(i) for i in range(0, reader.GetNumberOfScalarsInFile())]
    #p = np.asarray(vtk_out.GetCellData().GetArray('pressure'))
    points = vtk_out.GetPoints()
    array = points.GetData()
    pos = vtk_to_numpy(array)
    h = calBedHeight(pos)
#    pointData = vtk_out.GetPointData()
#    scalarData = pointData.GetArray('pressure')
#    p = vtk_to_numpy(scalarData)
    return h

filename = glob.glob('*.vtk')

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
filename = natural_sort(filename)

tstep = 0.02
tstart = 0
startindex = int(tstart/tstep)
n = np.arange(startindex,len(filename))
interval = 1
n = n[0::interval]
k = np.arange(len(n))
h = np.zeros(len(k))
u = np.zeros(len(k))

for i in k:
    h[i] = geth(filename[n[i]])
    u[i] = 0.002+(0.04-0.002)/250*i
    with open('epsilon.txt','a') as f:
        f.write("%s %s\n"%(str(u[i]),str(h[i])))

rawdata = pd.read_csv('epsilon.txt', delim_whitespace=True, header = None,skiprows = 0)
rawdata =  np.asarray(rawdata.values)

pnum = 10000
vt = 0.117
rhol = 1000
dp = 0.001
mu = 0.001
Ret = rhol*vt*dp/mu
D = 0.01385*2
A = 0.25*np.pi*D**2
Vp = 1/6*np.pi*dp**3
alpha_ = 1-pnum*Vp/(A*h)

if Ret <0.2:
    nindex = 4.65+19.5*dp/D
if Ret <1:
    nindex = (4.35+17.5*dp/D)*Ret**(-0.3)
if Ret <200 :
    nindex = (4.45+18*dp/D)*Ret**(-0.1)
if Ret <500:
    nindex = 4.45*Ret**(-0.1)
if Ret >=500:
    nindex = 2.39

alpha = (u/vt)**(1/nindex)

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4, 3.8],
   'lines.linewidth' : 2
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
plt.rcParams.update(params)
fig,ax = plt.subplots()

ax.plot(rawdata[:,0],rawdata[:,1], linestyle='-', c='#1b9e77',label = 'CFD-DEM')
ax.plot(u,alpha,c='#d95f02',linestyle='--',label = "Richardson-zaki equation,Eq.(20)")
ax.set_xlim([0.015,0.04])
ax.set_ylim([0.4,0.8])
ax.set_xlabel('$U_l$, m/s')
ax.set_ylabel(r'$\epsilon_l$')
plt.margins(0)
ax.legend(loc=0)
fig.tight_layout()
fig.savefig('bedExpansion.tiff',bbox_inches='tight',dpi = 600)

