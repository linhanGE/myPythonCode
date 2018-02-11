#-----------import modules----------#

import numpy as np
# controal plot behaviour
import matplotlib.pyplot as plt                                     
import matplotlib.mlab as mlab
# control the tick
import matplotlib.ticker as ticker                                  

#----------rc setting----------#

# global setting for journal paper
params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.54, 3.5]
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
# update parameters
plt.rcParams.update(params)                                        

#----------plot----------#

# 2 represents 2 figures, sharex means share the x axis
fig,ax = plt.subplots(2, sharex=True)                               
# plot line
ax[0].plot(x,y,'r-',label = 'xyz')                                  
# plot scatter
ax.scatter(x,y,s = 10, c = '#d95f02', marker = 'o',label = 'CFD-DEM')                    
# turn on or off the grid
ax.grid (False)                                                     
# draw horizontal line pass y=0
ax.axhline(y=0, color='k',linewidth = 1)                            

#----------Title----------#

# set title font
Arialfont = {'fontname':'Arial'}                                    
ax.set_title('Cd vs Time',**Arialfont)                              

#----------axis and tick control----------#

# get the range of x axis, yaxis is ax.get_ylim(), set x axis tick range
start, end = ax.get_xlim()                                           
ax.xaxis.set_ticks(np.arange(start, end, step))   
# set x axis major format                   
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:3.1f}"))
# set both tick label to scientific number  
plt.ticklabel_format(axis='both', style='sci', scilimits=(-2,2))     
# set x tick direction
ax.tick_params(direction='in')                                       
# set tick interval
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))             
# set x axis lable
ax.set_xlabel('xyz')                                                 
# set x axis range
plt.xlim(0,1)                                                        
ax.set_xlim([0., 1])                                                 
# x,y axis start from same position
plt.margins(0)                                                       
 # move x-axis where y=0
pos1 = ax.spines['bottom'].set_position('zero')                     
# To shift the tick labels relative to the ticks use pad
ax.tick_params(which='both', direction='out', pad=5)                 

#----------text----------#

# add text to a point
ax[0].text(0.001,2,'xyz')                                            

fig.text(0.01, 0.98, "A", weight="bold", horizontalalignment='left', verticalalignment='center')

ax.annotate("Re = %s, Cd = %s"%(str(round(Re)),str(round(abs(meanCd),3))),(0.41,0.36),xycoords='figure fraction')

#----------legend----------#

# show legend, this one should not coexit with next one
plt.legend(loc = 1)              
# control the legend location                                           
ax.legend(loc = 1)     
					# Location String 	Location Code
					# ‘best’ 	                0
					# ‘upper right’ 	        1
					# ‘upper left’ 	        	2
					# ‘lower left’ 	       	 	3
					# ‘lower right’ 	        4
					# ‘right’ 	            	5
					# ‘center left’ 	        6
					# ‘center right’ 	        7
					# ‘lower center’ 	        8
					# ‘upper center’ 	        9
					# ‘center’ 	            	10


# ensure labels are not cut                                              
plt.tight_layout()                                                   
# get the object of legend
leg = plt.legend()
# set legend frame color
leg.get_frame().set_edgecolor('k')
# set legend frame linewidth
leg.get_frame().set_linewidth(1)


#----------save figure with resolution----------#
fig.savefig('xyz.tiff',bbox_inches='tight',dpi = 600)                              

#---------special cases---------#
 
# plot histgram figure
fig,ax = plt.subplots()
mu = np.average(pp)
sigma = np.std(pp)
num_bins = 2000
n,bins,patches = ax.hist(pp,num_bins,normed=True)
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
