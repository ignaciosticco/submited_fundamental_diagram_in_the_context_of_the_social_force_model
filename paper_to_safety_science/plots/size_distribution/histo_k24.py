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
fig_width = 3+3/8 			              # width  in inches
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
data = np.genfromtxt("raw_histo_clsuters_density4.5_pasillo22m.txt",delimiter = ' ') 


#hist, bin_edges = np.histogram(data,bins=100)
###  PLOT  ###
binwidth = 1

weights = np.ones_like(data)/float(len(data))
plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth),weights=weights)


pylab.grid(False)
pylab.xlabel('Cluster size~(p)',fontsize=15)
pylab.ylabel('Frecuency',fontsize=15)
pylab.title('$\\rho=4.5$ \quad   $\\kappa=2.4\\times10^5$',fontsize=15)
pylab.xticks(np.linspace(0,80,5))
#pylab.xticks(np.linspace(0,3000,4))
pylab.xlim(0, 80)
plt.yscale('log')
pylab.ylim(10**(-4), 10**(0))
plt.tick_params(labelsize=15)
pylab.savefig('size_distribution_w22_density4_5.eps', format='eps', dpi=300, bbox_inches='tight')
