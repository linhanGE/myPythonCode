# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:54:24 2019

@author: c3216945
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import matplotlib.ticker as ticker
import glob
import natsort

f = glob.glob('*.csv')
f = natsort.realsorted(f)

def readData(filename):
    d = pd.read_csv(filename, header=0,usecols=[1,2])
    d = np.asarray(d)
    return d

d1 = readData(f[0])
d2 = readData(f[1])
d3 = readData(f[2])

ymax = 0.0825
R = 0.165*0.5

sortedyz1 = d1[d1[:,1].argsort()]
sortedyz2 = d2[d2[:,1].argsort()]
sortedyz3 = d3[d3[:,1].argsort()]

z1 = sortedyz1[:,1]
z2 = sortedyz2[:,1]
z3 = sortedyz3[:,1]

y1 = sortedyz1[:,0]
y2 = sortedyz2[:,0]
y3 = sortedyz3[:,0]

z1shift = (z1 - z1[0])
z2shift = (z2 - z2[0])
z3shift = (z3 - z3[0])

z1shiftP = (z1-z1[0])/R
z2shiftP = (z2-z2[0])/R
z3shiftP = (z3-z3[0])/R

diffy1 = np.diff(y1)
diffz1 = np.diff(z1shift)
slope1 = diffy1/diffz1

diffy2 = np.diff(y2)
diffz2 = np.diff(z2shift)
slope2 = diffy2/diffz2

diffy3 = np.diff(y3)
diffz3 = np.diff(z3shift)
slope3 = diffy3/diffz3

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4.3, 1.5]
#   'figure.dpi': 300 
   }
plt.rcParams.update(params)
fig,ax = plt.subplots()
fig.subplots_adjust(left=0.12, bottom=.3 , right=0.97, top=0.96)

ax.plot(z1shiftP[1:], np.abs(slope1), lw=1,ls='-',label='$Ca_{TP}=0.0024, Re_{TP}=52$')
ax.plot(z2shiftP[1:], np.abs(slope2),lw=1,ls='--',label='$Ca_{TP}=0.0055, Re_{TP}=121$')
ax.plot(z3shiftP[1:], np.abs(slope3),lw=1,ls='-.',label='$Ca_{TP}=0.0163, Re_{TP}=355$')

#ax.axhline(ymax,c='k',lw=1,ls='--')
#ax.axhline(0,c='k',lw=1,ls='--')

#---------------------------axis control------------------------#

ax.set_ylabel("|dy'/dz'|")
ax.set_xlabel("$z'/L_B$")
#
ax.set_ylim(-0.1,2)
ax.set_xlim(0,1)

majorLocatorX = MultipleLocator(1)
majorLocatorY = MultipleLocator(0.5)
minorLocatorX = MultipleLocator(0.2)
minorLocatorY = MultipleLocator(0.1)
##ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%2.1f'))
#
ax.xaxis.set_major_locator(majorLocatorX)
ax.xaxis.set_minor_locator(minorLocatorX)
ax.yaxis.set_minor_locator(minorLocatorY)
ax.yaxis.set_major_locator(majorLocatorY)
#ax.xaxis.set_ticks(np.arange(0, 0.026, 0.005))
#fig.text(0.15,0.82,'(a)',weight="bold",fontsize=15)

#------------------------legend control------------------------#
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.7))
#ax.legend(loc=0,frameon=False,labelspacing=0.1)
#ax.legend(loc='center left',frameon=False,bbox_to_anchor=(0.2, -0.25))
#ax.legend(loc='center left', bbox_to_anchor=(1.01, 0.7),frameon=False,labelspacing=0.1)
#fig.text(0.2,0.9,'(b)',weight="bold",fontsize=15)

#-----------------------add text------------------------------#

#bbox_args = dict(boxstyle="round", fc="0.8")
#arrow_args = dict(arrowstyle="->")
#ax.annotate('1', xy=(-0.9,0.8 ), xycoords='data', size=11,
#             xytext=(20, 20), textcoords='offset points',
#             ha="left", va="bottom",
##             bbox=bbox_args,
#             arrowprops=arrow_args)
#
#ax.annotate('2', xy=(-0.92,0.5), xycoords='data', size=11,
#             xytext=(30, 10), textcoords='offset points',
#             ha="left", va="bottom",
##             bbox=bbox_args,
#             arrowprops=arrow_args)
##
#ax.annotate('3', xy=(-0.95, 0.3), xycoords='data', size=11,
#             xytext=(30, 5), textcoords='offset points',
#             ha="left", va="bottom",
##             bbox=bbox_args,
#             arrowprops=arrow_args)
#
##
#ax.annotate('$U_{TP}$', xy=(-0.4,1), xycoords='data', size=11,
#             xytext=(-30, 0), textcoords='offset points',
#             ha="center", va="center",
##             bbox=bbox_args,
#             arrowprops=arrow_args)

#----------------------output figure-------------------------#
#plt.margins(0)
#fig.tight_layout(pad=0)
#ax.grid(color="0.95", linestyle='-', linewidth=1)
fig.savefig('slope.tiff', dpi = 300)
plt.show()