import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CNfile = "CourantMax_0"

CN = pd.read_csv(CNfile, sep='\s+',header=None)

courantNum = np.asarray(CN)

dp = 0.001
t,value = 0,1

tend = 0.01
tstep = 1e-6
tn = int(tend/tstep)

time = courantNum[:,t]
cn = courantNum[:,value]

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.54, 3.5]
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }

#fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
fig,ax = plt.subplots()
#---plot z position---#
ax.plot(time,cn,'r')

ax.legend()
ax.tick_params(direction='in')
#ax[0].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_xlabel('t, s')
ax.set_ylim([0, 0.05])
#ax[1].plot(time[0:tn],zFinex[0:tn],'r',label = 'bubble z position')
#ax[1].plot(time[0:tn],bedHeight,'--',label = 'bed height')
#ax.legend()
ax.set_ylabel('courant number')
#fig.subplots_adjust(hspace=0.09)
#plt.legend()
#plt.xlabel('time,s')
#plt.xlim(0.05,0.06)
plt.tight_layout()  # ensure labels are not cut off
fig.savefig('courant number.tiff', dpi = 600)
plt.show()