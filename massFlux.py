# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:35:35 2019

@author: c3216945
"""

import pyvista as pv
import numpy as np
import glob
import natsort
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from numpy import linalg as LA
import pandas as pd
#from scipy.stats import norm
#import matplotlib.mlab as mlab

f = glob.glob('*.vtk')
f = natsort.realsorted(f)

def getMf(f,slugCentre,k):
    # read vtk as unstructured data
    data = pv.read(f)
    pts = data.points
    v   = data.point_arrays['v']
    pxy = pts[:,0:2]
    r = LA.norm(pxy,axis=1)
    D = 0.165
    R = 0.5*D
    dp = 0.00565
    Vp = 1/6*np.pi*dp**3
    rhop = 1.6
    v = v[(r>=(k*R-1.5*dp)) & (r<=(k*R+1.5*dp)) & (pts[:,2]>=slugCentre-0.2*D) & (pts[:,2]<=slugCentre+0.2*D)]
    Np = len(v)
    A = np.pi*((k*R+1.5*dp)**2-(k*R-1.5*dp)**2)
    V = A*0.4*D
    m  = v*rhop*Vp*A*Np/V
    m  = np.sum(m)
    return m

n = np.arange(len(f))
mf1 = np.zeros(len(f))
mf2 = np.zeros(len(f))

ht = pd.read_csv('slugCentre_B1gp.txt', header = None, delim_whitespace =True)
ht = np.asarray(ht)
slugCentre = 0.5*(ht[:,0]+ht[:,1])

for i in n:
    mf1[i] = getMf(f[i],slugCentre[i],0.2)

for i in n:
    mf2[i] = getMf(f[i],slugCentre[i],0.8)   

t = np.arange(len(f))*0.002

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.2, 3.2]
   }
plt.rcParams.update(params)
fig,ax = plt.subplots()

ax.plot(t,mf1,ls='-')
ax.plot(t,mf2,ls='--')

                           
#(mu, sigma) = norm.fit(bin_nu)
#y_fit = mlab.normpdf(bins, mu, sigma)
#ax.plot(bins,y_fit)
#ax.plot(y_pdf, x_pdf )
                           
ax.set_ylim(0,0.02)
ax.set_xlim(0,0.5)
#
##majorLocatorY = MultipleLocator(5)
##majorLocatorX = MultipleLocator(0.2)
#minorLocatorY = MultipleLocator(0.001)
#minorLocatorX = MultipleLocator(5)
##ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%2.1f'))
#
##ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_minor_locator(minorLocatorY)
##ax.yaxis.set_major_locator(majorLocatorY)
#
#ax.set_xlabel("y/w")
#ax.set_ylabel('Probability density')
#
#fig.text(0.15,0.8,'(a)',weight="bold",fontsize=15)
#
##ax.legend(loc=0,frameon=False)
#
#handles, labels = plt.gca().get_legend_handles_labels()
#order = [2,0,1]
#ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],frameon=False)
#
fig.savefig('massfluxA1gp.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()
