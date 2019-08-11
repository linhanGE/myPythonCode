# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:55:21 2017

@author: c3216945
"""
import numpy as np
import pandas as pd
import glob
import re

def calBedHeight(filename):
    rawdata = pd.read_csv(filename, delim_whitespace = True, comment='#',header=None,skiprows = 9)
    hdata = rawdata.values
    x = 2
    y = 3
    z = 4
    px =  hdata[:,x]
    py =  hdata[:,y]
    pz =  hdata[:,z]
    pz[::-1].sort()
    # topparticle =  np.zeros(5018)
    # nrp = 0
    # for i in np.arange(len(px)-1):
        # if nrp <=220 and np.abs(px[i]-px[i+1]) > 0.006 and np.abs(py[i]-py[i+1]) > 0.006:
            # topparticle [i] = 1
            # nrp +=1
    # toplayer = pz[np.nonzero(topparticle)[0]]
    hmean = np.abs(np.average(pz[0:100-1]))+0.0015
    return hmean

filename = glob.glob('*.run')
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
filename = natural_sort(filename)	
itfile = iter(filename)
tstep = 0.1
tstart = 0
startindex = int(tstart/tstep)
n = np.arange(startindex,len(filename))
h = np.zeros(len(n))
k = np.arange(len(n))
for i in k:
    h[i] = calBedHeight(filename[n[i]])
    with open('hmean.txt','a') as f:
        f.write("%s  %s \n"%(str(i),str(h[i])))

with open('hmean.txt','a') as f:
        f.write("mean =  %s \n"%(np.average(h)))