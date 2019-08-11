import numpy as np
up = np.linspace(0.00001,1,10000)
mu = 0.001
rhol = 998.2
rhop = 2500
dp = 0.002
g = 9.81
Vp = 1/6*np.pi*dp**3
mp= rhop * Vp
Rep = rhol * up * dp/mu
cd = 24/Rep*(1+0.15*Rep**0.687)
force = rhol*g*Vp + 1/8*cd*rhol*np.pi*dp**2*up**2 - mp*g
vt = up[np.argmin(np.abs(force))]