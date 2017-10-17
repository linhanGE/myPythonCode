# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:44:41 2017

@author: c3216945
"""
import numpy as np
import matplotlib.pyplot as plt
sigma = 0.072     # N/m
Rp = 0.0005       # m
Rb = 0.001        # m
delta =  np.linspace(0,3.3e-6,num = 1000)
Ri = delta*np.sqrt((2*Rb-delta)(2*Rp-delta))/(2*(Rp+Rb-delta))
sin_alpha = delta*np.sqrt((2*Rb-delta)(2*Rp-delta))/(2*Rp*(Rb+Rp-delta))
