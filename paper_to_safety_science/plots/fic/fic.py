import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pylab
import numpy as np
import math

golden_mean = (math.sqrt(5)-1.0)/2.0       # Aesthetic ratio
fig_width = 3+3/8                          # width  in inches
fig_height = fig_width*golden_mean         # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'axes.linewidth': 0.5, 
          'axes.grid': False,
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

###  DATA  ###


data_koriginal = np.genfromtxt('density_fic_w22m_koriginal.txt', delimiter = ' ')
density_kroiginal = data_koriginal[:,0] 
fic_koriginal = data_koriginal[:,1] 
err_koriginal = data_koriginal[:,2] 


data_kx10 = np.genfromtxt('density_fic_w22m_kx10.txt', delimiter = ' ')
density_kx10 = data_kx10[:,0] 
fic_kx10 = data_kx10[:,1] 
err_kx10 = data_kx10[:,2] 

data_kwx10 = np.genfromtxt('density_fic_w22m_kwx10.txt', delimiter = ' ')
density_kwx10 = data_kwx10[:,0] 
fic_kwx10 = data_kwx10[:,1] 
err_kwx10 = data_kwx10[:,2] 

data_kix10 = np.genfromtxt('density_fic_w22m_kix10.txt', delimiter = ' ')
density_kix10 = data_kwx10[:,0] 
fic_kix10 = data_kix10[:,1] 
err_kix10 = data_kix10[:,2] 


###  PLOT  ###

plt.plot(density_kx10,fic_kx10,'-rs',mew=0.7,markersize=4,label='$\\kappa_w=\\kappa_i = 2.4 \\times 10^{6} $') 
plt.errorbar(density_kx10,fic_kx10,err_kx10,linestyle='none',fmt='none',color='none',ecolor='r') 


plt.plot(density_kroiginal,fic_koriginal,'b--x',mew=0.7,markersize=4,label='SFM original') 
plt.errorbar(density_kroiginal,fic_koriginal,err_koriginal,linestyle='none',fmt='none',color='none',ecolor='b') 

plt.plot(density_kwx10,fic_kwx10,'g:^',mew=0.7,markersize=4,label='$\\kappa_w = 2.4\\times 10^{6}$') 
plt.errorbar(density_kwx10,fic_kwx10,err_kwx10,linestyle='none',fmt='none',color='none',ecolor='g') 

plt.plot(density_kix10,fic_kix10,'y-.o',mew=0.7,markersize=4,label='$\\kappa_i =2.4  \\times 10^{6}$') 
plt.errorbar(density_kix10,fic_kix10,err_kwx10,linestyle='none',fmt='none',color='none',ecolor='y') 



pylab.legend()
pylab.xticks(np.arange(4.0,5.7,0.2))
plt.xlabel('Density~(P~m$^{-2}$) ')
plt.ylabel('frac. clustered indiv.')
plt.ylim(0.0, 1.02)
plt.xlim(4.1,5.5)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='upper left',labelspacing=0.1,borderpad=0.1,handletextpad=0.1,fontsize=6,numpoints=1)
pylab.savefig('fracc_clusteriz_vs_density.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('fracc_clusteriz_vs_density.eps', format='eps', dpi=300, bbox_inches='tight')
