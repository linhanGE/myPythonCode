import glob
import calmfp
import numpy as np
filename = glob.glob('*.txt')
itfile = iter(filename)
n = np.arange(len(filename))
mfp = np.zeros(len(filename))

for i in n:
    mfp[i] = calmfp.calMeanFreePath(next(itfile))
    with open('mfp','a') as f:
        f.write("%s  %s \n"%(str(i),str(mfp[i])))