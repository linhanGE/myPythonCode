# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt

#====================================%
# simulation data 1
#====================================%
rhof = 10			# density in kg/m3

def readPressure(filename):
    # -----read data-----#
    rawdata = pd.read_csv(filename, delim_whitespace=True, header = None,skiprows = 100)
    pData =  np.asarray(rawdata.values)
#    t, p1, p2 = 0,1,2
#    pinlet = stressData[:,p1]
#    poutlet = stressData[:,p2]
#    pdrop = pinlet-poutlet
    return pData

path = 'Umin.dat'
pdrop = readPressure(path)
pdrop_sim = pdrop[:,1] * rhof
average_pdrop_sim = np.mean(pdrop_sim[1000:])
t_sim = pdrop[:,0]

#====================================%
# analytical calculation
#====================================%

#===================
# Ergun Equation
#===================

dp = 0.001	                                           # particle diameter
phip = 1			                                       # sphericity
epsilon = 0.4                                          # voidfraction

#==================================
# min fluidization velocity in m/s
#==================================
rhoP = 2000                     # particle density in kg/m3
g = 9.81                        # gravity m/s2
L = 0.017			                                   # length of bed
nu = 1.5e-4			                               # kinemat Visk in m2/s
mu = nu*rhof			                               # dynam visc in Pa s

Umf = dp**2*(rhoP-rhof)*g/(150*mu)*(epsilon**3*phip**2)/(1-epsilon)
ReMF = Umf*dp*rhof/mu
# Wen and Yu
C1 = 33.7
C2 = 0.0408
Remf = np.sqrt(33.7**2+0.0408*dp**3*rhof*(rhoP-rhof)*g/mu**2)-C1
Umf = Remf*mu/dp/rhof
#if ReMF>=1000:
#    Umf = np.sqrt(dp*(rhoP-rhof)*g/(1.75*rhof)*epsilon**3*phip)
#    ReMF = Umf*dp*rhof/mu

dpUmf= L * (
                150*((1-epsilon)**2/epsilon**3)*((mu*Umf)/(phip*dp)**2) 
              +1.75*((1-epsilon)/epsilon**3)*((rhof*Umf**2)/(phip*dp))
        )


Ustart = 0.002
Uend = 0.02
timeStepSize = 0.00001                                  # time interval of pressure data
Tstart = 0
Tend = t_sim[len(t_sim)-1]
deltaU=(Uend-Ustart)/((Tend-Tstart)/timeStepSize)
Uergun = np.linspace(Ustart+deltaU,Umf+deltaU,Umf/deltaU)         # velocity over time
U = np.linspace(Ustart+deltaU,Uend+deltaU,num = len(t_sim))
Ua = Uergun / epsilon		                                   # physical velocity


dpErgun= L * (
                150*((1-epsilon)**2/epsilon**3)*((mu*Uergun)/(phip*dp)**2) 
              +1.75*((1-epsilon)/epsilon**3)*((rhof*Uergun**2)/(phip*dp))
        )


#pHydr=0
#dpUmf2=(L*(1-epsilon)*(rhoP-rhof)*g+pHydr)
#====================================%
# plot data
#====================================%

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.54, 3.5]
   }

plt.rcParams.update(params)  


fig, ax = plt.subplots()
ax.plot(U,pdrop_sim,color='k',label = 'CFD-DEM')
#title("Ergun pressure drop vs. simulation")
#a=strcat("analytical (Ergun), Umf=",num2str(Umf),", dpUmf=",num2str(dpUmf));
#legend(a,"simulation")
ax.set_xlabel("$U_L$, m/s")
ax.set_ylabel("$\Delta$P, Pa")

#axis([0,Uend,0,dpErgun(length(dpErgun))])

#plot(U,dpErgun,U,pdrop_sim,[Umf,Uend],dpUmf*ones(1,2))
ax.plot(Uergun,dpErgun,color='k',lineStyle = '--', label ='Ergun equation')
ax.plot([Umf,Uend],dpUmf*np.ones(2),color='k', lineStyle= '-.',label = 'apparent weight')
#title("Ergun pressure drop vs. simulation")
#a=strcat("analytical (Ergun), Umf=",num2str(Umf),", dpUmf=",num2str(dpUmf));
#legend(a,"simulation","analyt. deltaP at Umf","location","northwest")
#axis([0,Uend,0,dpErgun(length(dpErgun))])
ax.set_ylim(0,300)
ax.set_xlim(0.0019,0.02)
ax.legend()
fig.savefig('Umf.tiff',bbox_inches='tight',dpi=600)
