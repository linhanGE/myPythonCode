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

f1 = glob.glob('uy*.txt')
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
zP = np.linspace(0,meanSlug,num=6,endpoint=False)
zP = np.delete(zP,[0])


u0 = readData(f1[0])
meanu0 = np.mean(u0,axis=0)
stdu0 = np.std(u0,axis=0)

u1 = readData(f1[1])
meanu1 = np.mean(u1,axis=0)
stdu1 = np.std(u1,axis=0)

u2 = readData(f1[2])
meanu2 = np.mean(u2,axis=0)
stdu2 = np.std(u2,axis=0)

u3 = readData(f1[3])
meanu3 = np.mean(u3,axis=0)
stdu3 = np.std(u3,axis=0)

u4 = readData(f1[4])
meanu4 = np.mean(u4,axis=0)
stdu4 = np.std(u4,axis=0)

pOnLine =np.linspace(-1,1,num=u0.shape[1])

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

ax.plot(pOnLine, meanu4,lw=1,ls='-',label=r'$\frac{5}{6}L_S$')
ax.plot(pOnLine, meanu3,lw=1,ls='--',label=r'$\frac{2}{3}L_S$')
ax.plot(pOnLine, meanu2,lw=1,ls=':',label=r'$\frac{1}{2}L_S$')
ax.plot(pOnLine, meanu1,lw=1,ls='-.',label=r'$\frac{1}{3}L_S$')
ax.plot(pOnLine, meanu0,lw=1,dashes=[5,2,20,2],label=r'$\frac{1}{6}L_S$')

## set the x-spine (see below for more info on `set_position`)
#ax.spines['left'].set_position('zero')
#
## turn off the right spine/ticks
#ax.spines['right'].set_color('none')
#ax.yaxis.tick_left()
#
## set the y-spine
#ax.spines['bottom'].set_position('zero')
#
## turn off the top spine/ticks
#ax.spines['top'].set_color('none')
#ax.xaxis.tick_bottom()

ax.axhline(0,c='k',lw=0.5,ls='-',alpha=0.5)
ax.axvline(0,c='k',lw=0.5,ls='-',alpha=0.5)
#---------------------------axis control------------------------#

ax.set_xlabel("$y/w$")
ax.set_ylabel(r'$u_{f,z}\ (cm/s)$')

#ax.xaxis.set_label_coords(1.1, 0.5)
#ax.yaxis.set_label_coords(0.3, 0.89)

ax.set_xlim(-1,1)
ax.set_ylim(-1.5,1.5)
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
ax.legend(loc='center left', bbox_to_anchor=(1.01, 0.75),frameon=False,labelspacing=0.1)
#ax.legend(loc=0,frameon=False,labelspacing=0.1)
fig.text(0.15,0.82,'(b)',weight="bold",fontsize=15)

#-----------------------add text------------------------------#
# ax.text(0.8, 0.9,r'$\epsilon_{p}=0.05$',
#     horizontalalignment='center',
#     verticalalignment='center',
#     transform = ax.transAxes)

#----------------------output figure-------------------------#
#plt.margins(0)
#fig.tight_layout(pad=0)
#ax.grid(color="0.95", linestyle='-', linewidth=1)

fig.savefig('uyB1g.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()