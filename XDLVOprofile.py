import numpy as np
import matplotlib.pyplot as plt

epsilon0 = 8.854e-12 # CV-1m-1
epsilon =  78.4  # constant
psip = -50e-3      # V
psib =-35e-3       # V
kappa = 1/9.6e-9    # reciprocal of kappa
K = 2.7e-3         # N/m, strength of the hydrophobic force
l = 6e-9           # lambda 
A132 = -1.5e-20    #
Rb = 1e-3#0.0005        # m 
Rp = 3.3e-5 #0.00025
R_ = Rp*Rb/(Rp+Rb) 
cutoff = 0.7e-9   # m
#H1 = np.linspace(0,cutoff, num =250)
#H2 = np.linspace(cutoff,50e-9,num = 750)
#H = np.concatenate([H1,H2])
#Hvdw1 = np.linspace(cutoff,cutoff,num = 250)
#Hvdw2 = np.linspace(cutoff,50e-9,num=750)
#Hvdw = np.concatenate([Hvdw1,Hvdw2])
H = np.linspace(cutoff,50e-9,num = 1000)
Vvdw = -A132*R_/(6*H)
Vedl = np.pi*epsilon0*epsilon*R_*(2*psip*psib*np.log((1+np.exp(-kappa*H))/(1-np.exp(-kappa*H)))+(psib**2+psip**2)*np.log(1-np.exp(-2*kappa*H)))
#Vedl = 0.25*epsilon0*epsilon*R_*(2*psip*psib*np.log((1+np.exp(-kappa*H))/(1-np.exp(-kappa*H)))+(psib**2+psip**2)*np.log(1-np.exp(-2*kappa*H)))
Vh = -R_*K*l*np.exp(-H/l)
VT = Vvdw + Vedl + Vh

maxVT = str(max(VT))
#minVT = min(VT)
maxH = str(H[np.argmax(VT)])
fig, ax = plt.subplots()

# ax.annotate('minimum',xy=(min(VT)))
line1, = ax.plot(H,VT)
ax.text(0.08,0.3,'maxH = '+maxH+'  '+'maxVT = '+maxVT,transform=ax.transAxes)
#line2, = ax.plot(H,Vvdw)
#line3, = ax.plot(H,Vedl)
#line4, = ax.plot(H,Vh)
plt.show()