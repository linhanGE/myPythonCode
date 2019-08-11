import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fine_v = "vFine.txt"
coarse_v = "vFine.txt"
#bubble_velocity = "bubbleVelocity.txt"

vFine = pd.read_csv(fine_v, sep='\s+',header=None, comment='%')
vCoarse = pd.read_csv(coarse_v, sep='\s+',header=None, comment='%')
#vbubble = pd.read_csv(bubble_velocity, sep='\s+',header=None, comment='%')

vFine = np.asarray(vFine)
vCoarse = np.asarray(vCoarse)
#vbubble = np.asarray(vbubble)

db = 0.001
t,x,y,z = 0,1,2,3

tend = 0.01
tstep = 1e-6
tn = int(tend/tstep)

time = vFine[0:tn,t]
vzFinez = vFine[0:tn,z]
#zFiney = vFine[0:tn,y]
vzCoarsez = vCoarse[0:tn,z]
#zCoarsey = vCoarse[0:tn,y]
#meanv = np.mean(vzFinex[:tn])
#bedHeight = np.ones(len(time[0:tn])) * 0.04447
#ub_w = np.ones(len(time[0:tn])) * 0.181120755208

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
#plt.rc('text', usetex=True)    # use tex

#---plot z position---#
ax.plot(time,vzFinez,'r',label = 'fine mesh')
ax.plot(time,vzCoarsez,'b',linestyle ='-.', label = 'coarse mesh')
#ax[0].plot(time[0:tn],ub_w,'--',label = 'bubble velocity in water (Tomiyama etal. 1998)')
#---plot separation distance---#
#ax[0].plot(time,r,'r',label = 'separation')
#ax[0].plot(time,rmin,'b-', label = 'contact distance')
#ax[0].set_ylabel(r'separation distance, 10^4 m')
#ax[0].text(0.001,2,'kn=0.1 , k=6.26e-2, cutoff=5e-10')
#ax[0].set_ylim([0.05, 0.15])
ax.legend()
ax.tick_params(direction='in')
#ax[0].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_xlabel('t, s')
#ax[1].set_ylim([-0.01, 0.3])
#ax[1].plot(time[0:tn],zFinex[0:tn],'r',label = 'bubble z position')
#ax[1].plot(time[0:tn],bedHeight,'--',label = 'bed height')
ax.legend()
ax.set_ylabel('Upz, cm/s')
#fig.subplots_adjust(hspace=0.09)
#plt.legend()
#plt.xlabel('time,s')
#plt.xlim(0.05,0.06)
plt.tight_layout()  # ensure labels are not cut off
fig.savefig('velocities.tiff', dpi = 600)
plt.show()