#####################################
#-----------import modules----------#
#####################################

import numpy as np
# controal plot behaviour
import matplotlib.pyplot as plt                                     
import matplotlib.mlab as mlab
# control the tick
import matplotlib.ticker as ticker                                  

################################
#----------rc setting----------#
################################

# global setting for journal paper
params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [3.54, 3.5]
   #'mathtext.fontset': 'cm'     # different font for epsilon
#   'axes.linewidth': 1,
#   'patch.linewidth': 1
   }
# update parameters
plt.rcParams.update(params)                                        

##########################
#----------plot----------#
##########################

# 2 represents 2 figures, sharex means share the x axis
fig, axs = plt.subplots(3,sharex=True, sharey=True)                            
# plot line
ax.plot(t2,h2,color='#d95f02',linestyle=':', linewidth=7.0, label = 'xyz')                                
# plot scatter
ax.scatter(x,y,s = 10, c = '#d95f02', marker = 'o',label = 'CFD-DEM')                    
# turn on or off the grid
ax.grid (False)                                                     
# draw horizontal line pass y=0
ax.axhline(y=0.81, color='k',lw = 1,ls = '--' )
# plot with error bar
ax.errorbar(simulation[:,0],meangp,stdgp,linestyle='None',color = '#1b9e77', capsize=2,fmt = 'x',label = 'CFD-DEM') 
                          
###########################
#----------Title----------#
###########################

# set title font
Arialfont = {'fontname':'Arial'}                                    
ax.set_title('Cd vs Time',**Arialfont)                              

###########################################
#----------axis and tick control----------#
###########################################

axs[1].tick_params(bottom='off')

# get the range of x axis, yaxis is ax.get_ylim(), set x axis tick range
start, end = ax.get_xlim()                                           
ax.xaxis.set_ticks(np.arange(start, end, step))   
plt.xticks(np.arange(0.2, 1.4, 0.4))
# set x axis major format                   
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:3.1f}"))
# set both tick label to scientific number  
plt.ticklabel_format(axis='both', style='sci', scilimits=(-2,2))     
# set x tick direction
ax.tick_params(direction='in')                                       
# set tick interval
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
# set max major tick number
ax.xaxis.set_major_locator(ticker.MaxNLocator(5))
# set fixed no. of major ticks   
majors = [3, 4, 5, 6, 7]
ax.xaxis.set_major_locator(ticker.FixedLocator(majors))          
# set x axis lable
ax.set_xlabel('xyz')                                                 
# set x axis range
plt.xlim(0,1)                                                        
ax.set_xlim([0., 1])                                                 
# x,y axis start from same position
plt.margins(0)                                                       
 # move x-axis where y=0
pos1 = ax.spines['bottom'].set_position('zero') or
plt.margins(0)                    
# To shift the tick labels relative to the ticks use pad
ax.tick_params(which='both', direction='out', pad=5)  
# set log scale
ax.set_yscale('log')
# turn off minor ticks
plt.minorticks_off()
plt.xscale('log', subsx=[2, 3, 4, 5, 6, 7, 8, 9])
ax.minorticks_off()

############################
#----------marker----------#
############################

# ================    ===============================
# character           description
# ================    ===============================
   # -                solid line style
   # --               dashed line style
   # -.               dash-dot line style
   # :                dotted line style
   # .                point marker
   # ,                pixel marker
   # o                circle marker
   # v                triangle_down marker
   # ^                triangle_up marker
   # <                triangle_left marker
   # >                triangle_right marker
   # 1                tri_down marker
   # 2                tri_up marker
   # 3                tri_left marker
   # 4                tri_right marker
   # s                square marker
   # p                pentagon marker
   # *                star marker
   # h                hexagon1 marker
   # H                hexagon2 marker
   # +                plus marker
   # x                x marker
   # D                diamond marker
   # d                thin_diamond marker
   # |                vline marker
   # _                hline marker
# ================    ===============================          
# plot empty marker
plt.scatter(data[:,0],data[:,1], s=14, facecolors='none', edgecolors='b', marker = 'o',label = 'simulation')
ax.plot(zenit_small[:,0], zenit_small[:,1], 'o', markersize=8, markeredgewidth=1 ,markeredgecolor='k', markerfacecolor='None',label = 'Zenit et al. 1997')

##########################
#----------text----------#
##########################

# add text to a point
ax[0].text(0.001,2,'xyz')   # data coordinate
axs[0].text(0.8,0.1,r'$U_L=0.0535$',horizontalalignment='center',verticalalignment='center',transform=axs[0].transAxes)     # axis coordinate                                         

fig.text(0.01, 0.98, "A", weight="bold", horizontalalignment='left', verticalalignment='center')

ax.annotate("Re = %s, Cd = %s"%(str(round(Re)),str(round(abs(meanCd),3))),(0.41,0.36),xycoords='figure fraction')

# add text based on coordinates relative to the axis https://matplotlib.org/users/text_props.html
ax.text(0.2, 0.8,r'$\epsilon_{scrit}$'+'={:.2f}'.format(ec),
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)

############################
#----------legend----------#
############################

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
# remove frame
plt.legend(frameon=False)
ax.legend(loc = 3,bbox_to_anchor=(0,0),frameon=False,borderaxespad=None,mode='expand')

##################
#---draw lines---#
##################

ax.axvline(x=maxgp,ymin=0,ymax=0.8,ls = 'dotted', c='b')

#################################################
#----------save figure with resolution----------#
#################################################

fig.savefig('xyz.tiff',bbox_inches='tight',dpi = 600)                              

#################################
#---------special cases---------#
#################################
 
# plot histgram figure
fig,ax = plt.subplots()
mu = np.average(pp)
sigma = np.std(pp)
num_bins = 2000
n,bins,patches = ax.hist(pp,num_bins,normed=True)
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
