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
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
import re
import glob

f = glob.glob('e*.txt')

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

f = natural_sort(f)

def readData(filename):
    d = pd.read_csv(filename, header = None, delim_whitespace =True)
    d = np.asarray(d.values)
    return d

k = np.arange(len(f))

e1 = readData(f[0])
np1 = e1

e2 = readData(f[1])
np2 = e2

e3 = readData(f[2])
np3 = e3

e4 = readData(f[3])
np4 = e4

e5 = readData(f[4])
np5 = e5

db = 0.1

t1 = (np.arange(len(np1))+1)*10000*2e-7
t2 = (np.arange(len(np2))+1)*10000*2e-7
t3 = (np.arange(len(np3))+1)*10000*2e-7
t4 = (np.arange(len(np4))+1)*10000*2e-7
t5 = (np.arange(len(np5))+1)*10000*2e-7

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4.248, 3.6]
   }
plt.rcParams.update(params)
fig,ax = plt.subplots()
# make a little extra space between the subplots
#fig.subplots_adjust(hspace=0.2)

# plot for A #
ax.plot(t1,np1,c='k',lineStyle='-',label = '$\epsilon_p=0.01$')
ax.plot(t2,np2,c='k',lineStyle='--',label = '$\epsilon_p=0.06$')
ax.plot(t3,np3,c='k',lineStyle='-.',label = '$\epsilon_p=0.12$')
ax.plot(t4,np4,c='k',lineStyle=':',label = '$\epsilon_p=0.18$')
ax.plot(t5,np5,c='k',lineStyle=(0,(5,5)),label = '$\epsilon_p=0.24$')

ip = InsetPosition(ax, [0.2,0.2,0.5,0.45])
ax2 = plt.axes([0,0,1,1])
ax2.set_axes_locator(ip)
ax2.plot(t1[t1>=0.6],np1[t1>=0.6],c='k',lineStyle='-')
ax2.plot(t2[t2>=0.6],np2[t2>=0.6],c='k',lineStyle='--')
ax2.plot(t3[t3>=0.6],np3[t3>=0.6],c='k',lineStyle='-.')
ax2.plot(t4[t4>=0.6],np4[t4>=0.6],c='k',lineStyle=':')
ax2.plot(t5[t5>=0.6],np5[t5>=0.6],c='k',lineStyle=(0,(5,5)))

# inset plot #
mark_inset(ax, ax2, loc1=1, loc2=3, fc="none", ec='r',lw='0.5')
#ax2.plot
#---------------------------axis control------------------------#

ax.set_xlabel("$t\ (s)$")
ax.set_ylabel("Particle number")
        
#ax[0,0].set_xlim(0,0.6)
ax2.set_xlim(0.6,1.0)

ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_yaxis().set_visible(False)

#ax.set_ylim(0.,0.8)
#majorLocator = MultipleLocator(1)
#majorFormatter = FormatStrFormatter('%d')
#minorLocator = MultipleLocator(0.5)

#ax.xaxis.set_major_locator(majorLocator)
#ax.xaxis.set_minor_locator(minorLocator)
#ax.xaxis.set_ticks(np.arange(0, 0.026, 0.005)) 

#------------------------legend control------------------------#
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.7))
ax.legend(loc=0,frameon=False,labelspacing=0.01)

#-----------------------add text------------------------------#
# ax.text(0.8, 0.9,r'$\epsilon_{p}=0.05$',
#     horizontalalignment='center',
#     verticalalignment='center',
#     transform = ax.transAxes)

#----------------------output figure-------------------------#
#plt.margins(0)
fig.tight_layout(pad=0)
#ax.grid(color="0.95", linestyle='-', linewidth=1)


fig.savefig('SolidFraction-NoInRegion.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()