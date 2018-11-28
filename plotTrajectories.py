import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fine_position = "coarse2.txt"
coarse_position = "coarse3.txt"
#bubble_velocity = "bubbleVelocity.txt"

pFine = pd.read_csv(fine_position, sep='\s+',header=None, comment='%')
pCoarse = pd.read_csv(coarse_position, sep='\s+',header=None, comment='%')
#vbubble = pd.read_csv(bubble_velocity, sep='\s+',header=None, comment='%')

pFine = np.asarray(pFine)
pCoarse = np.asarray(pCoarse)
#vbubble = np.asarray(vbubble)

db = 0.001
t,x,y,z = 0,1,2,3

tend = 0.01
tstep = 1e-6
tn = int(tend/tstep)

#time = vbubble[:,t]
zFinez = pFine[0:tn,z]
zFiney = pFine[0:tn,y]
zCoarsez = pCoarse[0:tn,z]
zCoarsey = pCoarse[0:tn,y]
#meanv = np.mean(vzFinex[:tn])
#bedHeight = np.ones(len(time[0:tn])) * 0.04447
#ub_w = np.ones(len(time[0:tn])) * 0.181120755208

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.8, 3.5]
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }

plt.rcParams.update(params)  

#fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
fig,ax = plt.subplots()
#plt.rc('text', usetex=True)    # use tex

#---plot z position---#
ax.plot(zFiney,zFinez,'r',label = 'particle trajectories (fine)')
ax.plot(zCoarsey,zCoarsez,'b',linestyle ='-.', label = 'particle trajectories (coarse )')
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
ax.set_ylabel('z, cm')
#ax[1].set_ylim([-0.01, 0.3])
#ax[1].plot(time[0:tn],zFinex[0:tn],'r',label = 'bubble z position')
#ax[1].plot(time[0:tn],bedHeight,'--',label = 'bed height')
ax.legend()
ax.set_xlabel('y, cm')
#fig.subplots_adjust(hspace=0.09)
#plt.legend()
#plt.xlabel('time,s')
#plt.xlim(0.05,0.06)
plt.tight_layout()  # ensure labels are not cut off
fig.savefig('trajectories.tiff', dpi = 600)
plt.show()