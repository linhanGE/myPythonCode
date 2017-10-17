# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:30:07 2017

@author: c3216945
"""

import numpy as np
import matplotlib.pyplot as plt
import calCd
import CdCal

rho = 1000
u = 0.2
db = 0.001
mu = 0.001
t = np.asarray(CdCal.time)
Cd = 2*np.asarray(CdCal.drag)/(rho*u**2*1/4*np.pi*db**2)
Re = rho*u*db/mu


#---rc setting---#
params = {
   'axes.labelsize': 7,
   'font.family': 'Arial',
   'legend.fontsize': 7,
   'xtick.labelsize': 7,
   'ytick.labelsize': 7,
   'text.usetex': False,
   'figure.figsize': [4.5, 4.5]
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
plt.rcParams.update(params)

from matplotlib.ticker import FormatStrFormatter
fig,ax =plt.subplots()

#ax.style('default')
Arialfont = {'fontname':'Arial'}
ax.plot(t[4:],abs(Cd[4:]),'k',label = 'simulation')

#ax.set_title('Cd vs Time',**Arialfont)
plt.xlabel('time, s')
plt.ylabel('Cd, -')


#---label plots---#
#fig.text(0.01, 0.98, "A", weight="bold", horizontalalignment='left', verticalalignment='center')
#fig.text(0.54, 0.98, "B", weight="bold", horizontalalignment='left', verticalalignment='center')
meanCd = np.mean(Cd)

#---annotate---#
ax.annotate("Re = %s, Cd = %s"%(str(round(Re)),str(round(abs(meanCd),3))),(0.41,0.36),xycoords='figure fraction')

(Re_, Cd_) = calCd.calCd(rho,u,mu,db)
Cd_ = Cd_*np.ones(len(t))
ax.plot(t,Cd_,'k--',label = 'Schiller and Nauman, 1933')

#---legend---#
leg = plt.legend()
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_linewidth(1)

#---tick---#
#ax.get_yaxis().set_tick_params(direction='out')
#ax.get_xaxis().set_tick_params(direction='out')
#ax.get_yaxis().set_tick_params(which='both', direction='out')
#ax.get_xaxis().set_tick_params(which='both', direction='out')
#ax.tick_params(direction='out', pad=5) # To shift the tick labels relative to the ticks use pad
ax.tick_params(direction='in')
plt.yticks(np.arange(0.6, 1.0, 0.1))

#---axis---#
ax.axis([0,5,0.6,1.0])
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

fig.savefig('Cd.tiff',bbox_inches='tight',dpi = 1200)
