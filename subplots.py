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

#fA1 = 'A1_distribution.txt'
#fB1 = 'B1_distribution.txt'
#fC1 = 'C1_distribution.txt'
#fD1 = 'D1_distribution.txt'
#
#def readData(filename):
#    d = pd.read_csv(filename, header = None, delim_whitespace =True)
#    d = np.asarray(d.values)
#    return d
#
#db = 0.1
#
#A1 = readData(fA1)
#B1 = readData(fB1)
#C1 = readData(fC1)
#D1 = readData(fD1)
#
#A1 = A1[A1[:,2]>=-0.066]
#A1 = A1[A1[:,2]<=-0.065]
#
#B1 = B1[B1[:,2]>=-0.066]
#B1 = B1[B1[:,2]<=-0.065]
#
#C1 = C1[C1[:,2]>=-0.066]
#C1 = C1[C1[:,2]<=-0.065]
#
#D1 = D1[D1[:,2]>=-0.066]
#D1 = D1[D1[:,2]<=-0.065]
#
#
#xA1 = A1[:,0]/db
#yA1 = A1[:,1]/db
#
#xB1 = B1[:,0]/db
#yB1 = B1[:,1]/db
#
#xC1 = C1[:,0]/db
#yC1 = C1[:,1]/db
#
#xD1 = D1[:,0]/db
#yD1 = D1[:,1]/db

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4.6, 4.6]
   }
plt.rcParams.update(params)
fig,ax = plt.subplots(2,2, sharey='row',sharex='col',gridspec_kw={'hspace': 0,'wspace': 0})
#fig.subplots_adjust(hspace=0.2)

ax[0,0].scatter(xA1,yA1,s=10,marker='o',facecolors='none', edgecolors='k')
ax[0,1].scatter(xB1,yB1,s=10,marker='o',facecolors='none', edgecolors='k')
ax[1,0].scatter(xC1,yC1,s=10,marker='o',facecolors='none', edgecolors='k')
ax[1,1].scatter(xD1,yD1,s=10,marker='o',facecolors='none', edgecolors='k')

#---------------------------axis control------------------------#
Reb = ['$Re_b=100$','$Re_b=160$','$Re_b=220$','$Re_b=280$']

for axs, ReTxT in zip(ax.flat,Reb) :
    axs.set_ylim(-0.6,0.6)
    axs.set_xlim(-0.6,0.6)
    majorLocator = MultipleLocator(0.25)    
    axs.xaxis.set_major_locator(majorLocator)
    axs.yaxis.set_major_locator(majorLocator)
    axs.text(0.01,0.92,ReTxT, transform=axs.transAxes)
    axs.set_aspect('equal')

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
fig.text(0.5,0.01, '$x/d_b$', ha='center',fontsize=15)
fig.text(0., 0.5, '$y/d_b$', va='center', rotation='vertical',fontsize=15)
#fig.suptitle('$1.5d_b\leq H \leq 1.6d_b$')
plt.tight_layout()
fig.savefig('distribution.tiff',pad_inches=0,dpi = 300)
plt.show()