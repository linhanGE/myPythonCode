# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:28:03 2019

@author: c3216945
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'forceCoeffs.dat'
data = pd.read_csv(file, delim_whitespace = True, header=None, skiprows = 9)
data = np.asarray(data)
t = data[:,0]
cd = data[:,2]

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

ax.plot(t,cd,c='#e41a1c',label = '$C_d$')
ax.set_xlabel('time,s')      
ax.set_ylabel('cd')    
#ax.set_yscale('log')
ax.legend(loc=0)