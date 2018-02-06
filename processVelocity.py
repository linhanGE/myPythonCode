# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:22:37 2017

@author: c3216945
"""

import glob
import readVelocity as rv
import numpy as np
import matplotlib.pyplot as plt

filename = glob.glob('*.txt')
itfile = iter(filename)
Np = len(filename)
timelen = len(rv.readVelocity('v1.txt')[0])
n = np.arange(Np)
s = (timelen,Np)
vx = np.zeros(s)
vy = np.zeros(s)
vz = np.zeros(s)
t = np.linspace(0,timelen*0.001,num=timelen)
for i in n:
    vx[:,i],vy[:,i],vz[:,i] = rv.readVelocity(next(itfile))
    
vxmean = np.mean(np.mean(np.abs(vx),axis = 0))
vymean = np.mean(np.mean(np.abs(vy),axis = 0))
vzmean = np.mean(np.mean(np.abs(vz),axis = 0))

#---rc setting---#
params = {
   'axes.labelsize': 9,
   'font.family': 'Arial',
   'legend.fontsize': 9,
   'xtick.labelsize': 9,
   'ytick.labelsize': 9,
   'text.usetex': False,
   'figure.figsize': [3.54, 3.54]
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
plt.rcParams.update(params)

fig,ax =plt.subplots()
ax.plot(t,vz[:,0],'k',label = 'simulation')
ax.tick_params(direction='in')

plt.xlabel('time, s')
plt.ylabel('vz, m/s')

fig.savefig('velocity.tiff',bbox_inches='tight',dpi = 1000)