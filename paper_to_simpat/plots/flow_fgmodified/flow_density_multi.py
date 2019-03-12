# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

'''

'''

import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
#import numarray

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
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

### DATA ###
data = np.genfromtxt("flow-density_vd1_pasillo22m.txt",delimiter = ' ') 
density = data[0:len(data)-1,0]
flow = data[0:len(data)-1,1]

data_kpx10 = np.genfromtxt("flow-density_pasillo22m_kpx10.txt",delimiter = ' ') 
density_kpx10 = data_kpx10[:,0]
flow_kpx10 = data_kpx10[:,1]

data_kpx1_kix10 = np.genfromtxt("flow-density_pasillo22m_kpx1_kix10.txt",delimiter = ' ') 
density_kpx1_kix10 = data_kpx1_kix10[:,0]
flow_kpx1_kix10 = data_kpx1_kix10[:,1]

data_kx10 = np.genfromtxt("flow-density_pasillo22m_kx10.txt",delimiter = ' ') 
density_kx10 = data_kx10[:,0]
flow_kx10 = data_kx10[:,1]


plt.plot(density,flow,'b--x',mew=0.7,markersize=4,label='SFM original')
plt.plot(density_kpx10,flow_kpx10,'g:^',mew=0.7,markersize=4,label='$\\kappa_w = 2.4\\times 10^{6}$')
plt.plot(density_kpx1_kix10,flow_kpx1_kix10,'y-.o',mew=0.7,markersize=4,label='$\\kappa_i =2.4  \\times 10^{6}$')
plt.plot(density_kx10,flow_kx10,'-rs',mew=0.7,markersize=4,label='$\\kappa_w=\\kappa_i = 2.4 \\times 10^{6} $')


pylab.grid(False)
#pylab.xlabel('time~$(s)$')
pylab.xlabel('Density~(p~/m$^{2}$)')
pylab.ylabel('Flow~(p~/m/s)')
#pylab.legend()
#pylab.ylim(0.0, 60.0)
#pylab.ylim(0.0, 3.6)
#pylab.yticks(np.arange(3,11,2))
pylab.xlim(0.5, 9.5)
#pylab.xticks(np.arange(0,1100,200))
#pylab.xlim(0, 8)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#plt.legend(loc='upper left',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
plt.legend(frameon=False,loc='best',labelspacing=0.2,borderpad=0.2,handletextpad=0.1,fontsize=6,numpoints=1)
pylab.savefig('flow-density_pasillo22m_fgmodified_multi.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('flow-density_pasillo22m_fgmodified_multi.eps', format='eps', dpi=300, bbox_inches='tight')
