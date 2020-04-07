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

#def getMf(f,slugCentre,k):
#    # read vtk as unstructured data
#    data = pv.read(f)
#    pts = data.points
#    v   = data.point_arrays['v']*np.asarray([0,0,1])
#    pxy = pts[:,0:2]
#    r = LA.norm(pxy,axis=1)
#    D = 0.165
#    R = 0.5*D
#    dp = 0.00565
#    rhop = 1.6
#    Vp = 1/6*np.pi*dp**3
#    v = v[(r>=(k*R-3*dp)) & (r<=(k*R+3*dp)) & (pts[:,2]>=slugCentre-5*dp) & (pts[:,2]<=slugCentre+5*dp)]
##    v =v[(r<=k*R) & (pts[:,2]>=head) & (pts[:,2]<=tail)]
#    Np = len(v)
#    A = np.pi*((k*R+3*dp)**2-(k*R-3*dp)**2)
##    A = np.pi*(k*R)**2
##    V = A*np.abs(tail-head)
#    V = A*10*dp
#    epsilon = Vp*Np/V
#    m  = rhop*A*v
#    m  = np.sum(m)*epsilon
#    return m

def getMf(f,head,tail,k1,k2):
    # read vtk as unstructured data
    data = pv.read(f)
    pts = data.points
    v   = data.point_arrays['v']*np.asarray([0,0,1])
#    pxy = pts[:,0:2]
    z   = pts[:,2]
#    r = LA.norm(pxy,axis=1)
    D = 0.165
    R = 0.5*D
    dp = 0.00565
#    rhop = 1.6
    Vp = 1/6*np.pi*dp**3
    v = v[(z>=head + k1*(tail-head)) & (z>=head + k2*(tail-head))]
    Np = len(v)
    A = np.pi*R**2
    V = A*(k2-k1)*(tail-head)
    epsilon = Vp*Np/V*1.89
    return epsilon

n = np.arange(len(f))
mf1 = np.zeros(len(f))
mf2 = np.zeros(len(f))
mf3 = np.zeros(len(f))
mf4 = np.zeros(len(f))

ht = pd.read_csv('slugCentre_A1gp.txt', header = None, delim_whitespace =True)
ht = np.asarray(ht)
slugCentre = 0.5*(ht[:,0]+ht[:,1])

for i in n:
    mf1[i] = getMf(f[i],ht[i,0],ht[i,1],0, 0.25)
#    mf1[i] = getMf(f[i],slugCentre[i],0.2)

for i in n:
    mf2[i] = getMf(f[i],ht[i,0],ht[i,1],0.25,0.5)
#    mf2[i] = getMf(f[i],slugCentre[i],0.5)

for i in n:
    mf3[i] = getMf(f[i],ht[i,0],ht[i,1],0.5, 0.75)
#    mf3[i] = getMf(f[i],slugCentre[i],0.8)

for i in n:
    mf4[i] = getMf(f[i],ht[i,0],ht[i,1],0.75, 1.0)
#    mf3[i] = getMf(f[i],slugCentre[i],0.8)

t = np.arange(len(f))*0.002+0.452

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [2.5, 2.5]
   }
plt.rcParams.update(params)
fig,ax = plt.subplots()
figlegend = plt.figure(figsize=(2.5,2.5))

l1 = ax.plot(t,mf1,ls='-',label = '$0 \leq h < 0.25L_S$')
l2 = ax.plot(t,mf2,ls='--',label = '$0.25 \leq h < 0.5L_S$')
l3 = ax.plot(t,mf3,ls='-.',label = '$0.5 \leq h < 0.75L_S$')
l4 = ax.plot(t,mf4,ls='-.',label = '$0.75 \leq h < L_S$')

#plt.yscale('log')
#(mu, sigma) = norm.fit(bin_nu)
#y_fit = mlab.normpdf(bins, mu, sigma)
#ax.plot(bins,y_fit)
#ax.plot(y_pdf, x_pdf )
                           
ax.set_ylim(0,0.06)
ax.set_xlim(0.5,1.1)
#
##majorLocatorY = MultipleLocator(5)
majorLocatorX = MultipleLocator(0.1)
#minorLocatorY = MultipleLocator(0.001)
#minorLocatorX = MultipleLocator(5)
##ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%2.1f'))
#
ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_minor_locator(minorLocatorY)
##ax.yaxis.set_major_locator(majorLocatorY)
#
ax.set_xlabel("t (s)")
#ax.set_ylabel(r'$\.m_{s,axial}\ (mg/s)$')
ax.set_ylabel(r'Solid fraction, $\epsilon_p$')
#
fig.text(0.15,0.8,'(a)',weight="bold",fontsize=15)
#
#ax.legend(loc=0,frameon=False)
#
#handles, labels = plt.gca().get_legend_handles_labels()
#order = [2,0,1]
#ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],frameon=False)
#
plt.figlegend(*ax.get_legend_handles_labels(), loc = 'upper left',frameon=False)
figlegend.savefig('legend.tiff')
fig.savefig('massfluxA1gp_axial.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()
