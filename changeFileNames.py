# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:38:09 2019

@author: c3216945
"""

import numpy as np
import os
import glob
#import re
import natsort 

f = glob.glob('*.vtk')

f = natsort.realsorted(f)

k = np.arange(len(f))
#
for i in k:
    newName = 'CFD_' + str(i) + '.vtk'
    os.rename(f[i], newName)
