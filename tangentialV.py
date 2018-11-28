# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:19:01 2018

@author: c3216945
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import re


def solveVt(xfile,vfile):
    t,x,y,z = 0,1,2,3
    datax = pd.read_csv(xfile, delim_whitespace = True, skiprows = 1)
    datav = pd.read_csv(vfile, delim_whitespace = True, skiprows = 1)
    
    datax = np.asarray(datax)
    datav = np.asarray(datav)

    time = datav[:,t]

    dx = datax[:,x]
    dy = datax[:,y]
    dz = datax[:,z]

    rsq = dx**2+dy**2+dz**2
    r = np.sqrt(rsq)
    rinv = 1/r

    enx = dx*rinv
    eny = dy*rinv
    enz = dz*rinv

    vx = datav[:,x]
    vy = datav[:,y]
    vz = datav[:,z]

    vn = vx*enx+vy*eny+vz*enz
    vn1 = vn * enx
    vn2 = vn * eny
    vn3 = vn * enz 

    vt1 = vx -vn1
    vt2 = vy - vn2
    vt3 = vz - vn3

    vt = np.sqrt(vt1**2+vt2**2+vt3**2)
    
    return time,vt

def polarAngle(xfile):
    t,x,y,z = 0,1,2,3
    datax = pd.read_csv(xfile, delim_whitespace = True, skiprows = 1)
    datax = np.asarray(datax)
    time = datax[:,t]
    
    pVector = datax[:,x:]
    verticalVector = [0,0,1]
    d = np.linalg.norm(pVector,axis=1)
    cosphi = np.dot(pVector, verticalVector)/d
    sepD = 0.0942/2+0.003/2
    phi = np.rad2deg(np.arccos(cosphi))
    timeS=time[np.where(d>sepD)]
    phiS = phi[np.where(d>sepD)]
    return time, phi, timeS, phiS

def sepDistance(xfile):
    t,x,y,z = 0,1,2,3
    datax = pd.read_csv(xfile, delim_whitespace = True, skiprows = 1)
    datax = np.asarray(datax)
    time = datax[:,t]
    pVector = datax[:,x:]
    d = np.linalg.norm(pVector,axis=1)
    return d

xfile = glob.glob('xFine*.txt')
vfile = glob.glob('vFine*.txt')
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

xfile = natural_sort(xfile)	
vfile = natural_sort(vfile)
	
itfile = iter(xfile)
itfile = iter(vfile)

tstep = 0.1
tstart = 0
startindex = int(tstart/tstep)
n = np.arange(startindex,len(xfile))
h = np.zeros(len(n))
k = np.arange(len(n))

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [4, 3.5]
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
plt.rcParams.update(params)
plt.rcParams["text.usetex"] =True
fig,ax1 = plt.subplots()

time1, phi1,timeS1,phiS1 = polarAngle('xFine2.txt')   
d =  sepDistance('xFine2.txt')
ax1.plot(time1,phi1,'k',label = 'St=0.224')
ax1.scatter(timeS1,phiS1,c = 'k', marker = 'o',s=100)
#ax.plot(time1,phi,label = r'St[i]')
#ax.plot(time1,phi,label = r'St[i]')
#ax.plot(time1,phi,label = r'St[i]')
#ax.plot(time1,phi,label = r'St[i]')
 
ax1.set_xlabel('t,s') 
ax1.set_ylabel(r'$\varphi^\circ$') 
#ax.set_ylim(0,100)
ax1.set_xlim(0,0.04)
ax1.legend(frameon=True)
ax2 = ax1.twinx()
ax2.plot(time1,d,'k')
ax1.legend(loc = 7) 
ax1.text(0.28, 0.15,r'$\varphi$'+'$={:.2f}^\circ$'.format(phiS1),
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax1.transAxes)
plt.margins(0)
fig.tight_layout()
fig.savefig('polarangle.tiff',bbox_inches='tight',dpi = 600)

    






