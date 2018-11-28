# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:09:07 2018

@author: c3216945
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

p = pd.read_csv('x.txt', delim_whitespace=True, header=None,skiprows = 1)
p = np.array(p)
t,x,y,z = 0,1,2,3
d = np.sqrt(p[:,x]**2+p[:,y]**2+p[:,z]**2)
db = 0.0317
dp = 30.1e-4
cutoff = 0.5*(db+dp)
cuttoff_array = np.ones(len(p[:,0]))*cutoff
zero = np.zeros(len(p[:,0]))

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.54, 3.5]
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }

plt.rcParams.update(params)  

fig,ax = plt.subplots()

m = d -cuttoff_array
count = np.sum(m<=0)
ax.plot( p[:,t], m, color='k')
ax.plot( p[:,t], zero, color='r')

#ax.plot( p[:,t], cuttoff_array, color='r')
ax.set_ylim(-0.2e-6,0.2e-6)
ax.set_xlim(0.0069,0.0072)

plt.tight_layout()  # ensure labels are not cut off
fig.savefig('single.tiff', dpi = 600)
plt.show()

                        
                        
