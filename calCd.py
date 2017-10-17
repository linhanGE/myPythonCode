# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:26:48 2017

@author: c3216945
"""

def calCd(rho,u,mu,d):
    """ This function calculate Re and Cd. The Cd value is based on
    Schiller and Nauman. 
    Return as
    (Re,Cd)."""   
    Re = rho*u*d/mu
    Cd = 24/Re*(1+0.15*Re**(0.687))
    return Re,Cd
