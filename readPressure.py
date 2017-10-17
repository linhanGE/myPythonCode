# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:27:21 2017

@author: c3216945
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
def readData(filename):
    rawdata = pd.read_csv(filename, delim_whitespace=True, comment='#',header=None,skiprows = 10)
    pdata = rawdata.values
    return pdata

p = readData('0.189')

rho = 1000
rhop = 2230
Np = 139 
deltap = (p[:,2]-p[:,1])*rho
timestep = 0.01
t = p[0,0]+np.arange(len(p[:,0]-1))*timestep
dp = 0.008
Vp = 1/6*np.pi*dp**3
g = 9.81
dc = 0.05
Ac = 1/4*np.pi*dc**2
t_deltap = (rhop-rho)*Vp*Np*g/Ac

#---rc setting---#
params = {
   'axes.labelsize': 10,
   'font.family': 'Arial',
   'legend.fontsize': 10,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
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
ax.plot(t,deltap,'k',label = 'simulation')

#ax.set_title('Cd vs Time',**Arialfont)
plt.xlabel('time, s')
plt.ylabel('Pressure, Pa')


#---label plots---#
#fig.text(0.01, 0.98, "A", weight="bold", horizontalalignment='left', verticalalignment='center')
#fig.text(0.54, 0.98, "B", weight="bold", horizontalalignment='left', verticalalignment='center')

#---annotate---#
#ax.annotate("Re = %s, Cd = %s"%(str(round(Re)),str(round(abs(meanCd),3))),(0.41,0.36),xycoords='figure fraction')
t_deltap = t_deltap*np.ones(len(t))
ax.plot(t,t_deltap,'k--',label = 'Theoretical')

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
#plt.yticks(np.arange(0.6, 1.0, 0.1))

#---axis---#
#ax.axis([0,5,0.6,1.0])
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

fig.savefig('pressuredrop.tiff',bbox_inches='tight',dpi = 1200)