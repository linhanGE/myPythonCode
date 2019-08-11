# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:49:21 2019

@author: c3216945
"""

import vtk
from vtk.util.numpy_support import vtk_to_numpy
import glob
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import re
import matplotlib.mlab as mlab
from scipy.stats import norm

#from scipy.stats import binned_statistic

def getPostionDistribution(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    vtk_out = reader.GetOutput()
    points = vtk_out.GetPoints()
    array = points.GetData()
    numpy_nodes = vtk_to_numpy(array)
    y = numpy_nodes[:,1]
#    bin_nu, bin_edges = np.histogram(y, bins = np.linspace(0.0068,0.1932,20))
    return y

filename = glob.glob('run*.vtk')
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
filename = natural_sort(filename)

tstep = 0.001
tstart = 0.02
startindex = int(tstart/tstep)
n = np.arange(startindex,len(filename))
#bin_nu = np.zeros(len(np.linspace(0.0068,0.1932,19)))
k = np.arange(len(n))
bin_nu = getPostionDistribution(filename[1])

for i in k:
#    bin_nu += getPostionDistribution(filename[n[i]])[0]
    if i != 1:
        bin_nu = np.concatenate((bin_nu,getPostionDistribution(filename[n[i]]))) 
#bin_edges = getPostionDistribution(filename[1])[1]

bin_nu = bin_nu[np.where(bin_nu>0.0068)]

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.54, 3.5]
   }
plt.rcParams.update(params)
fig,ax = plt.subplots()

#mean=np.mean(bin_nu)
#var=np.var(bin_nu)
#std=np.sqrt(var)
#y_pdf=stats.norm.pdf(bin_nu,mean,std)
#x_pdf=np.linspace(min(bin_nu), max(bin_nu),10170)
#weights = np.ones_like(bin_nu)/float(len(bin_nu))

n, bins, patches = ax.hist(bin_nu, bins = 30, facecolor='#1b9e77',edgecolor= 'k', orientation='horizontal')
#(mu, sigma) = norm.fit(bin_nu)
#y_fit = mlab.normpdf( bins, mu, sigma)
#ax.plot(y_fit,bins)
#ax.plot(y_pdf, x_pdf )
ax.set_xlabel('Occurence')
ax.set_ylabel('y,cm')
#ax.set_xlim(0,1500)
ax.set_ylim(0.0,0.2)

fig.savefig('10.tiff', dpi = 300, bbox_inches='tight',pad_inches=0)
plt.margins(0)

plt.show()
    
    