# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import arange,pi,sin,cos,sqrt,savefig

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8  			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'legend.numpoints': 1,            # the number of points in the legend line
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'legend.fontsize': 8,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)

#################### DATA LAMMPS ##############################

data1= np.genfromtxt('./flux_model_revised_1.dat', delimiter = ' ')	
data4= np.genfromtxt('./flux_model_revised_10.dat', delimiter = ' ')	
data5= np.genfromtxt('./flux_model_revised_100.dat', delimiter = ' ')	
data6= np.genfromtxt('./flux_model_revised_1000.dat', delimiter = ' ')	

#################### PLOT specification ##############################


alpha1=data1[:,0]
flux1 =data1[:,1]

alpha4=data4[:,0]
flux4 =data4[:,1]

alpha5=data5[:,0]
flux5 =data5[:,1]

alpha6=data6[:,0]
flux6 =data6[:,1]

alpha0=np.linspace(0.0,1.0,11)

#################### PLOT specification ##############################

fig=plt.figure(1)                # the first figure

ax1 = fig.add_subplot(111)

#ax1.grid(color='gray', linestyle='--', linewidth=0.3,axis='both')
ax1.grid(False)
#ax2 = ax1.twinx()
#ax2.grid(False)

ax1.plot(alpha1[50:5050]+1,flux1[50:5050],lw=0.7,color='orange',label=r'$\mathcal{K}=1$')
ax1.plot(alpha4[50:5050]+1,flux4[50:5050],lw=0.7,color='firebrick',label=r'$\mathcal{K}=10$')
ax1.plot(alpha5[50:5050]+1,flux5[50:5050],lw=0.7,color='steelblue',label=r'$\mathcal{K}=100$')
ax1.plot(alpha6[50:5050]+1,flux6[50:5050],lw=0.7,color='olive',label=r'$\mathcal{K}=1000$')
ax1.plot(alpha0,alpha0,lw=0.7,linestyle='--',color='gray')
#ax1.plot(alpha,velocity,lw=0.7,color='firebrick',label=r'$N=20$')
#ax1.plot(alpha,velocity,lw=0.7,color='steelblue',label=r'$N=50$')

legend = plt.legend(loc='upper left',prop={'size':5})


ax1.set_ylim(0,5)
#ax1.set_yticks(np.arange(-200,-40,40))
ax1.set_xlim(0, 5)
ax1.set_xticks(np.arange(0,6,1))
#ax1.set_xlabel(r'$1/T$~(MeV$^{-1}$)')
#ax2.set_ylabel(r'$E_\mathrm{sym}$~(MeV)')
ax1.set_xlabel(r'$\rho$')
ax1.set_ylabel(r'$\langle J\rangle$')
#ax2.set_ylabel(r'$\langle v_i\rangle$')
#ax1.set_title(r'Velocity vs. alpha')


pylab.savefig('fig_flux_model.eps', format='eps', dpi=300, bbox_inches='tight')


