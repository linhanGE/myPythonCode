# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 23:03:37 2018

@author: c3216945
"""

Ga = dp**3*rhol*rhod*g/mul**2
    if Ga <1.8:
        Rep = Ga/18
    elif Ga>1.8 and Ga< 2.6e3:
        Rep = (Ga/18)**0.8
    elif Ga >2.6e3 and Ga<3.3e5:
        Rep = 0.45*Ga**0.61
    else:
        Rep = 1.732*Ga**0.5
    
    vt = Rep*mul/dp/rhol