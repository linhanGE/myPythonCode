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
import matplotlib.ticker as ticker
import glob
import natsort

def readAsort(filename):
    f = glob.glob(filename)
    f = natsort.realsorted(f)
    return f

f1 = glob.glob('A*.txt')
f1 = natsort.realsorted(f1)

f2 = glob.glob('B*.txt')
f2 = natsort.realsorted(f2)

f3 = glob.glob('C*.txt')
f3 = natsort.realsorted(f3)

def readData(filename):
    d = pd.read_csv(filename, delim_whitespace=True,header=None)
    d = np.asarray(d)
    return d

utp = np.asarray([4.6,10.7,31.4])
tstart = -200

def meanV(tstart,u,utp):
    meanU = np.mean(u[tstart:,:],axis=0)/utp
    return meanU

pOnLine =np.linspace(-1,1,num=readData(f1[0]).shape[1])

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [8, 3.2]
   }
plt.rcParams.update(params)
fig,ax = plt.subplots(1,3, sharey='row')

k= np.asarray([0,1,2])
line = ['-','--',':']


for i,j in zip(f1,k):
    u = readData(i)
    meanU = meanV(tstart,u,utp[0])
    ax[0].plot(pOnLine, meanU,ls=line[j])

for i,j in zip(f2,k):
    u = readData(i)
    meanU = meanV(tstart,u,utp[1])
    ax[1].plot(pOnLine, meanU,ls=line[j])

for i,j in zip(f3,k):
    u = readData(i)
    meanU = meanV(tstart,u,utp[2])
    ax[2].plot(pOnLine, meanU,ls=line[j])
    
#---------------------------axis control------------------------#

majorLocatorX = MultipleLocator(0.5)
minorLocatorX = MultipleLocator(0.1)
majorLocatorY = MultipleLocator(0.5)
minorLocatorY = MultipleLocator(0.1)

for axs in ax.flat:
    axs.set_ylim(0,2.5)
    axs.set_xlim(-1,1)
    axs.axhline(2,c='k',lw=0.5,ls='-',alpha=0.5)
    axs.axvline(0,c='k',lw=0.5,ls='-',alpha=0.5)
    
    axs.xaxis.set_major_locator(majorLocatorX)
    axs.xaxis.set_minor_locator(minorLocatorX)
    axs.yaxis.set_major_locator(majorLocatorY)
    axs.yaxis.set_minor_locator(minorLocatorY)

ax[1].set_xlabel("$y'/R$")
ax[0].set_ylabel('$u_{f,z}/u_{TP}$')

handles, labels= ax[1].get_legend_handles_labels()
labelList = [r"$z'=0.1L_S$",r"$z'=0.5L_S$",r"$z'=0.9L_S$"]

ax[1].legend(handles, labels=labelList,loc='center', bbox_to_anchor=(0.5, 1.1),frameon=False,labelspacing=0.01,ncol=3)

fig.savefig('axialVelocity.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()