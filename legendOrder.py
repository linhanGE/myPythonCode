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

delta_B = np.asarray([0.00203,0.00367,0.00798])
delta_H = np.asarray([0.00194,0.00338,0.00690])
delta_simulation = np.asarray([0.0021,0.0038,0.0071])

delta_error = 0.05*delta_simulation

ub = np.asarray([4.83,11.69,37.53])

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

ax.errorbar(ub, delta_simulation,yerr=delta_error,fmt='-o',capsize=2,elinewidth=1,markersize=5,lw=1,label='VOF-DEM')
ax.plot(ub,delta_B,ls='--',label='Bretherton(1961)')
ax.plot(ub,delta_H,ls='-.',label='Han etal.(2011)')

ax.set_ylim(0.0015,0.0085)
ax.set_xlim(0,40)

ax.set_xlabel(r"$U_B\ (m/s)$")
ax.set_ylabel(r'$\delta\ cm$')

fig.text(0.8,0.2,'(a)',weight="bold",fontsize=15)

#ax.legend(loc=0,frameon=False)

handles, labels = plt.gca().get_legend_handles_labels()
order = [2,0,1]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],frameon=False)
