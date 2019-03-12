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

data_koriginal = np.genfromtxt('fis_225p_d0.92.txt', delimiter = ' ')
vd_kroiginal = data_koriginal[:,0] 
iter_koriginal = data_koriginal[:,1] 
te_koriginal = data_koriginal[:,2] 
indv_inside_koriginal = data_koriginal[:,3] 

data_kx10 = np.genfromtxt('fis_225p_d0.92_kx10.txt', delimiter = ' ')
vd_kx10 = data_kx10[:,0] 
iter_kx10 = data_kx10[:,1] 
te_kx10 = data_kx10[:,2] 
indv_inside_kx10 = data_kx10[:,3] 


###  ANALYSIS  ###

vd_total = 15 		# cantidad total de velocidades de deseo (vd)
iter_total = 30 	# cantidad total de iteraciones por vd
list_vd = np.linspace(0.5,7.5,15)

def promedia_te(te,iter_total,vd_total):
	te_mean=[]
	te_std=[]
	i=0
	while i<vd_total:
		te_mean+=[np.mean(te[i*iter_total:i*iter_total+iter_total])]
		te_std += [np.std(te[i*iter_total:i*iter_total+iter_total])]
		i+=1
	return te_mean,te_std

te_mean_kx10=promedia_te(te_kx10,iter_total,vd_total)[0]
e_te_mean_kx10=promedia_te(te_kx10,iter_total,vd_total)[1]


###  PLOT  ###

fig, ax1 = plt.subplots()

plt.plot(list_vd,te_mean_kx10,'-bo',mew=0.7,markersize=4,label='$\\kappa=2.4\\times10^{6}$') 
plt.errorbar(list_vd,te_mean_kx10,e_te_mean_kx10,linestyle='none',fmt='none',color='none',ecolor='b') 

pylab.grid(False)
pylab.xlabel('$v_d$~(m/s)')
pylab.ylabel('$t_e$~(s)')


############ Insert plot ############

te_mean=promedia_te(te_koriginal,iter_total,vd_total)[0]
e_te_mean=promedia_te(te_koriginal,iter_total,vd_total)[1]

#left, bottom, width, height = [0.17, 0.59, 0.28, 0.28]
left, bottom, width, height = [0.6, 0.2, 0.28, 0.28]
ax2 = fig.add_axes([left, bottom, width, height])

ax2.plot(list_vd,te_mean,'-g*',mew=0.7,markersize=4,label='$\\kappa=2.4\\times10^{5}$') 
ax2.errorbar(list_vd,te_mean,e_te_mean,linestyle='none',fmt='none',color='none',ecolor='g') 

fig.patch.set_facecolor('black')

pylab.xlabel('$v_d$~(m/s)',size='5.5',labelpad=1)
pylab.ylabel('$t_e$~(s)',size='5.5',labelpad=-3,zorder=1)
#pylab.xlim(1.5, 4)
#pylab.ylim(19, 25)
ax2.set_yticklabels([])
plt.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False) 
plt.tick_params(axis='y',which='both',bottom=False,top=False,labelbottom=False) 

#lgd=plt.legend(numpoints=1,handlelength=0.8) 
ax2.legend(frameon=False,loc='upper center',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=5,numpoints=1) 


ax2.xaxis.set_ticks_position('none') 
ax2.yaxis.set_ticks_position('none') 
ax2.grid(False)

plt.text(-1, 130, "135", size=4.5)
plt.text(0.2, 40, "0.5", size=4.5)
plt.text(-0.8, 55, "50", size=4.5)
plt.text(7, 40, "7.5", size=4.5)

pylab.savefig('fis_kx10.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('fis_kx10.eps', format='eps', dpi=300, bbox_inches='tight')