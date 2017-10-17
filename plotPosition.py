import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
bubble_position = "position_bubble.txt"
particle_position = "position_particle.txt"
bubble_velocity = "velocity_bubble.txt"
particle_velocity = "velocity_particle.txt"

pbubble = pd.read_csv(bubble_position, sep='\s+',header=None, comment='%')
pparticle = pd.read_csv(particle_position, sep='\s+',header=None, comment='%')
vbubble = pd.read_csv(bubble_velocity, sep='\s+',header=None, comment='%')
vparticle = pd.read_csv(particle_velocity, sep='\s+',header=None, comment='%')

pbubble = np.asarray(pbubble)
pparticle = np.asarray(pparticle)
vbubble = np.asarray(vbubble)
vparticle = np.asarray(vparticle)

dp = 0.0001
db = 0.001
t,x,y,z = 0,1,2,3
time = pbubble[:,t]
r = (np.sqrt((pbubble[:,x]-pparticle[:,x])**2+(pbubble[:,y] \
            -pparticle[:,y])**2+(pbubble[:,z]-pparticle[:,z])**2)-0.5*dp-0.5*db)*1e4
rmin = (0.5*dp+0.5*db)*np.ones(len(time))

zbubble = pbubble[:,z]
zparticle = pparticle[:,z]
vzbubble = vbubble[:,z]
vzparticle = vparticle[:,z]

fig,ax = plt.subplots(2, sharex=True)
plt.rc('text', usetex=True)    # use tex

#---plot z position---#
ax[0].plot(time,pbubble[:,3],'r',label = 'bubble')
ax[0].plot(time,pparticle[:,3],'b',label = 'particle')

#---plot separation distance---#
#ax[0].plot(time,r,'r',label = 'separation')
#ax[0].plot(time,rmin,'b-', label = 'contact distance')
#ax[0].set_ylabel(r'separation distance, 10^4 m')
#ax[0].text(0.001,2,'kn=0.1 , k=6.26e-2, cutoff=5e-10')

#ax[0].set_ylim([0.05, 0.15])
ax[0].tick_params(direction='in')
#ax[0].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))

ax[1].plot(time,vzbubble,'r',label = 'bubble')
ax[1].plot(time,vzparticle,'b', label = 'particle')
ax[1].set_ylabel('vz, m/s')
#ax[1].set_ylim([-0.01, 0.3])
ax[1].tick_params(direction='in')
fig.subplots_adjust(hspace=0.09)

plt.legend()
plt.xlabel('time,s')
#plt.xlim(0.05,0.06)

plt.tight_layout()  # ensure labels are not cut off
fig.savefig('results_2.tiff', dpi = 600)
plt.show()
