# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:47:31 2018

@author: c3216945
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('phi-dp.txt', delim_whitespace = True, header=None, skiprows = 0)
data = np.asarray(data)
dp = data[:,0]
phioff = data[:,1]
tr = data[:,2]
#phim = 9+8.1*rhop+(0.9-0.)

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4.6, 3.5],
   'lines.linewidth' : 2
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
plt.rcParams.update(params)
fig,ax1 = plt.subplots()
ln1= ax1.scatter(dp,phioff,marker = 'o',facecolor = 'none', edgecolor = 'k')
ax1.scatter(0.1, 53.19, marker = 's',facecolor = 'none', edgecolor = 'b',label = r'$\varphi_{max}$, corrected $C_d$')
ax1.plot(dp,phioff,'k',label = r'$\varphi_{max}$')
#sc.set_facecolor('none')
ax1.set_xlabel(r'$d_p, mm$')
ax1.set_ylabel(r'${\varphi_{max}}^\circ$')
ax2 = ax1.twinx()
ln2 = ax2.scatter(dp, tr, marker = 'x', c='k')
ax2.scatter(0.1, 0.017453, marker = 'd',facecolor = 'none', edgecolor = 'b',label = '$t_s$, corrected $C_d$')
ax2.plot(dp,tr,'k',linestyle='--', label='$t_s$')
ax2.set_ylim(0.01,0.04)
ax2.set_ylabel('Sliding time ($t_s$), s')
#ax1.margins(0)
#ax2.margins(0)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc=1)
fig.tight_layout()
#plt.legend(frameon=False)
fig.savefig('slidingTime.tiff',bbox_inches='tight',dpi = 600)




