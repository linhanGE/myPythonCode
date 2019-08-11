# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:08:36 2019

@author: c3216945
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'residuals.dat'
data = pd.read_csv(file, delim_whitespace = True, header=None, skiprows = 2)
data = np.asarray(data)
t = data[:,0]
p = data[:,1]
ux = data[:,2]
uy = data[:,3]
uz = data[:,4]
params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
#   'figure.figsize': [3.54, 3.5]
   #'mathtext.fontset': 'cm'     # different font for epsilon
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
fig,ax = plt.subplots(figsize=(10,8))

ax.plot(t,p,c='#e41a1c',label = 'p')
ax.plot(t,ux,c='#377eb8',label = 'ux')
ax.plot(t,uy,c='#4daf4a',label = 'uy')
ax.plot(t,uz,c='#984ea3',label = 'uz')
ax.set_xlabel('time,s')      
ax.set_ylabel('variable')    
ax.set_yscale('log')
ax.legend(loc=0)