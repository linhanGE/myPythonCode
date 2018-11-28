# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:32:03 2018

@author: c3216945
"""

import readDataFromFile as rd
import numpy as np

force = rd.readDataFromFile('forces.txt',0)

zforce_= np.mean(force[:,2])

d = 0.001
uL = 0.2
rhoL= 998.2
A = 0.25*np.pi*d**2

Cd = 2*zforce_/(rhoL*uL**2*A)