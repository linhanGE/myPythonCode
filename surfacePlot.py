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
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

f = 'surfaceData.csv'

def readData(filename):
    d = pd.read_csv(filename, usecols=[1,2,6],header=0)
    d = np.asarray(d)
    return d

d = readData(f)
y = d[:,0]
z = d[:,1]
y, z = np.meshgrid(y,z)
uz = d[:,2]

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4, 4]
   }
plt.rcParams.update(params)

fig = plt.figure()
ax = fig.gca(projection='3d')

# surfaceplot #

#ax.plot_surface(y, z, uz, cmap=cm.coolwarm, edgecolor='none')

ax.plot_trisurf(y, z, uz,linewidth=0.5, edgecolors='r')

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

#ax.axhline(0,c='k',lw=0.5,ls='-',alpha=0.5)
#ax.axvline(0,c='k',lw=0.5,ls='-',alpha=0.5)
#---------------------------axis control------------------------#
#
ax.set_xlabel("y")
ax.set_ylabel('z')
ax.set_zlabel('uz')

#ax.xaxis.set_label_coords(1.1, 0.5)
#ax.yaxis.set_label_coords(0.3, 0.89)

#ax.set_xlim(-0.5,0.5)
#ax.set_ylim(-0.3,0.3)
#majorLocatorY = MultipleLocator(1)
#majorLocatorX = MultipleLocator(0.25)
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
#ax.legend(loc='center left', bbox_to_anchor=(1.01, 0.7),frameon=False,labelspacing=0.1)
#ax.legend(loc=0,frameon=False,labelspacing=0.1)
#fig.text(0.81,0.82,'(a)',weight="bold",fontsize=15)

#-----------------------add text------------------------------#
# ax.text(0.8, 0.9,r'$\epsilon_{p}=0.05$',
#     horizontalalignment='center',
#     verticalalignment='center',
#     transform = ax.transAxes)

#----------------------output figure-------------------------#
#plt.margins(0)
fig.tight_layout(pad=0)
#ax.grid(color="0.95", linestyle='-', linewidth=1)

fig.savefig('surfaceUzA1g.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()
