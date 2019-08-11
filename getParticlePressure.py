import glob
import numpy as np, pandas as pd
from numpy import linalg as LA
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import re

def calParticlePressure(filename):
    # -----read data-----#
    rawdata = pd.read_csv(filename, delim_whitespace=True, comment='#',header = None, skiprows=9)
    stressData =  np.asarray(rawdata.values)
    z,stress,history = 0,1,2
    zLow = 0.03
    zHigh = 0.06
    h = zHigh - zLow
    D = 0.0508-0.006
    V = 0.25 * np.pi * D * D * h
    pressure1 = stressData[(stressData[:,z] >= zLow)]
    pressure2 = pressure1[pressure1[:,z] <= zHigh]
    pressure = pressure2[:,stress] * pressure2[:,history]
    sumPressure = np.sum(pressure)/V
    return sumPressure
    
filename = glob.glob('*.local')
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
filename = natural_sort(filename)
tstep = 0.01
tstart = 10
startindex = int(tstart/tstep)
n = np.arange(startindex,len(filename))
pp = np.zeros(len(n))
k = np.arange(len(n))
for i in k:
    pp[i] = calParticlePressure(filename[n[i]])
    with open('particlePressure.txt','a') as f:
        f.write("%s  %s \n"%(filename[n[i]],str(pp[i])))
with open('particlePressure.txt','a') as f:
    f.write("particlePressure =  %s \n"%(np.average(pp)))
        