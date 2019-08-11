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
import matplotlib.ticker as ticker
import glob
import natsort

f1 = glob.glob('u*.txt')
f1 = natsort.realsorted(f1)
f2 = glob.glob('head&tail.txt')
f2 = natsort.realsorted(f2)

def readData(filename):
    d = pd.read_csv(filename, delim_whitespace=True,header=None)
    d = np.asarray(d)
    return d

dSlug = readData(f2[0])
lSlug = dSlug[:,1] - dSlug[:,0]
meanSlug = np.mean(lSlug)
stdSlug  = np.std(lSlug)
t        = np.arange(len(lSlug))

u0 = readData(f1[0])
meanu0 = np.mean(u0,axis=0)
stdu0 = np.std(u0,axis=0)
pOnLine =np.linspace(0.0825,-0.0825,num=u0.shape[1])

u1 = readData(f1[1])
meanu1 = np.mean(u1,axis=0)
stdu1 = np.std(u1,axis=0)
pOnLine =np.linspace(0.0825,-0.0825,num=u1.shape[1])

u2 = readData(f1[2])
meanu2 = np.mean(u2,axis=0)
stdu2 = np.std(u2,axis=0)
pOnLine =np.linspace(0.0825,-0.0825,num=u2.shape[1])

u3 = readData(f1[3])
meanu3 = np.mean(u3,axis=0)
stdu3 = np.std(u3,axis=0)
pOnLine =np.linspace(0.0825,-0.0825,num=u3.shape[1])

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

# plot for A #

#ax.errorbar(t,lSlug,yerr=stdSlug,c='k',linestyle='-',label = 'L_s')
ax.errorbar(pOnLine, meanu3,yerr=stdu3,fmt='-o',capsize=2,elinewidth=1,markersize=1,lw=1)


#ax.axhline(0,c='grey',lw=0.5)
#ax.axvline(0,c='grey',lw=0.5)
#---------------------------axis control------------------------#

#ax.set_xlabel("$x/d_b$")
#ax.set_ylabel(r'$u_{fz}\ (cm/s)$')

#ax.set_xlim(-0.6,0.6)
#ax.set_ylim(-6,3)
#majorLocatorY = MultipleLocator(1)
#majorLocatorX = MultipleLocator(0.2)
#minorLocatorY = MultipleLocator(2)
#minorLocatorX = MultipleLocator(0.5)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%2.1f'))

#ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_minor_locator(minorLocatorY)
#ax.yaxis.set_major_locator(majorLocatorY)
#ax.xaxis.set_ticks(np.arange(0, 0.026, 0.005))
#fig.text(0.15,0.82,'(a)',weight="bold",fontsize=15)

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

fig.savefig('liquidSlug.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()