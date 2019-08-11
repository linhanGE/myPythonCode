# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:48:28 2019

@author: c3216945
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

import re

import glob

f = glob.glob('B*.txt')

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

f = natural_sort(f)

n = np.arange(0,len(f))
k = np.arange(len(n))

def readData(filename):
    d = pd.read_csv(filename, header = None, delim_whitespace =True)
    d = np.asarray(d.values)
    return d

db = 0.1

B1 = readData(f[0])[99:,:]
B8 = readData(f[1])[99:,:]
B9 = readData(f[2])[99:,:]
B10 = readData(f[3])[99:,:]

B1 = B1[(B1[:,2]>=-0.15) & (B1[:,2]<=-0.05) & (B1[:,0]>=-0.003) & (B1[:,0]<=0.003)]/db
B8 = B8[(B8[:,2]>=-0.15) & (B8[:,2]<=-0.05) & (B8[:,0]>=-0.003) & (B8[:,0]<=0.003)]/db
B9 = B9[(B9[:,2]>=-0.15) & (B9[:,2]<=-0.05) & (B9[:,0]>=-0.003) & (B9[:,0]<=0.003)]/db
B10 = B10[(B10[:,2]>=-0.15) & (B10[:,2]<=-0.05) & (B10[:,0]>=-0.003) & (B10[:,0]<=0.003)]/db

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4.6, 4.6]
   }

plt.rcParams.update(params)
#fig,ax = plt.subplots(2,2, sharey='row',sharex='col',gridspec_kw={'hspace': 0.08,'wspace': 0})
fig,ax = plt.subplots(2,2, sharey='row',sharex='col')

ax[0,1].scatter(B8[:,1],B8[:,2],s=8,marker='o',facecolors='none', edgecolors='k')
ax[0,0].scatter(B1[:,1],B1[:,2],s=8,marker='o',facecolors='none', edgecolors='k')
ax[1,0].scatter(B9[:,1],B9[:,2],s=8,marker='o',facecolors='none', edgecolors='k')
ax[1,1].scatter(B10[:,1],B10[:,2],s=8,marker='o',facecolors='none', edgecolors='k')

#---------------------------axis control------------------------#
stp = ['$St_p=0.001$','$St_p=0.007$','$St_p=0.027$','$St_p=0.058$']

for axs, stpTxT in zip(ax.flat,stp) :
    axs.set_ylim(-1.6,-0.3)
    axs.set_xlim(-0.6,0.6)
#    majorLocator = MultipleLocator(0.3)    
#    axs.xaxis.set_major_locator(majorLocator)
#    axs.yaxis.set_major_locator(majorLocator)
    axs.text(0.01,0.92,stpTxT, transform=axs.transAxes)
    axs.set_aspect('auto')

#majorFormatter = FormatStrFormatter('%d')
#minorLocator = MultipleLocator(0.5)
#ax[0,0].text('$Re_b=100$')
#ax[0,1].text('$Re_b=160$')
#ax[1,0].text('$Re_b=220$')
#ax[1,1].text('$Re_b=280$')

#ax.xaxis.set_minor_locator(minorLocator)
#ax.set_ylim(0.5,2.1)
#ax.xaxis.set_ticks(np.arange(0, 0.026, 0.005)) 

#------------------------legend control------------------------#
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.7))
#ax.legend(loc=0,frameon=False)

#-----------------------add text------------------------------#
# ax.text(0.8, 0.9,r'$\epsilon_{p}=0.05$',
#     horizontalalignment='center',
#     verticalalignment='center',
#     transform = ax.transAxes)

#----------------------output figure-------------------------#
#plt.margins(0)
#fig.tight_layout(pad=0)
#ax.grid(color="0.95", linestyle='-', linewidth=1)
fig.text(0.5,0.0, '$y/d_b$', ha='center',fontsize=15)
fig.text(0., 0.5, '$z/d_b$', va='center', rotation='vertical',fontsize=15)
#fig.suptitle('$1.5d_b\leq H \leq 1.6d_b$')
plt.tight_layout()
fig.savefig('distributionB.tiff',dpi = 300)
plt.show()