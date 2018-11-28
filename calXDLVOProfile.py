# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:52:31 2018

@author: c3216945
"""
import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(1e-9,50e-9,100)        #- separation distance
A132 = -6.07e-21                        #- Hamaker constant
epsilon = 78.4                         #- dielectric constant of medium
epsilon0 = 8.854e-12
K132 = 5.7e-20 
gammalv = 0.072                         #- surface tension of water
# epsilon0 =                            #- dielectric constant of vacuum
kappainv = 40e-9                        #- reciprocal of the Debye length
psip = -63.9e-3                         #- surface potention of bubble,mv 
psib = -32.78e-3                        #- surface potention of particle,mv
# gamma =                               #- surface tension
theta = 43.8                            #- water contact angle
# D = 10                                #- decay length of the hydrophobic force
dp = 42.8e-6*2
db = 0.51e-3*2
Rp = 0.5*dp
Rb = 0.5*db
hm = Rp*Rb/(Rp+Rb)                      #- harmonici mean

#- Electrostatic energy
Ve = (0.25*epsilon*epsilon0*hm*(psip*psip+psib*psib)*
      (
       2*psip*psib/(psip*psip+psib*psib)*
       np.log(
               (1+np.exp(-h/kappainv))/(1-np.exp(-h/kappainv))
             )+
       np.log(1-np.exp(-2*h/kappainv))
       )
      )

#- hydrophobic energy
Vh = -1/6*hm*K132/h

#- Van der waals
l = 3.3e15
b = 3e-17
c = 3e8

Vd = -1/6*A132*hm/h*(1-(1+2*b*l)/(1+b*c/h))

Vsum = Ve+Vh+Vd
fsum = Vsum/h
Wa = -gammalv*np.pi*Rp**2*(1-np.cos(theta/180*np.pi)**2)
#fa = 3/2*hm*np.pi*Wa
#Vsum = np.hstack([Wa, Vsum])
#np.concatenate([[0],h])
#h = np.hstack([0,h])
fig, ax = plt.subplots()
line1,= ax.plot(h,Vsum)
line2,= ax.plot(h,Ve,'r--',label = 'Ve' )
#line3,= ax.plot(h,Vd,'b--',label = 'Vd')
#line4,= ax.plot(h,Vh,'g--',label = 'Vh')
ax.set_ylim([-20e-17,20e-17])
plt.ticklabel_format(axis='both', style='sci', scilimits=(-2,2))
plt.legend()
#pos1 = ax.spines['bottom'].set_position('zero')       # x-axis where y=0
ax.axhline(y=0, color='k',linewidth = 1)               # show x axis

fig.savefig('test.tiff', dpi = 600)
