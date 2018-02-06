import glob

import numpy as np, pandas as pd
from numpy import linalg as LA
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def calParticlePressure(filename):
    # -----read data-----#
    rawdata = pd.read_csv(filename, delim_whitespace=True, comment='#',header = None, skiprows=9)
    wallParticleData =  np.asarray(rawdata.values)
    x1,y1,z1,x2,y2,z2,fx,fy,fz = 0,1,2,3,4,5,6,7,8
    zLow = 0.01
    zHigh = 0.04
    h = zHigh - zLow
    fnComponent = wallParticleData[(wallParticleData[:,z2] >= zLow) & (wallParticleData[:,z2] <= zHigh)]
    fn = LA.norm(fnComponent[:,fx:], axis=1)
    sumfnmag =  np.sum(fn)
    d = 0.0508
    p =  np.pi * d
    A = p * h
    particlePressure = sumfnmag/A
    return particlePressure
    
filename = glob.glob('*.local')   
n = np.arange(len(filename))
pp = np.zeros(len(filename))
for i in n:
    pp[i] = calParticlePressure(filename[i])
    with open('particlePressure.txt','a') as f:
        f.write("%s  %s \n"%(filename[i],str(pp[i])))
with open('particlePressure.txt','a') as f:
	f.write("particlePressure =  %s \n"%(np.average(pp)))
        