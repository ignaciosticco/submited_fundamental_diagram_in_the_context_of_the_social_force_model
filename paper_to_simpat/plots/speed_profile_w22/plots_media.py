# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

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

data_d2 = np.genfromtxt('speed_profile_w22_density2_kappa24.txt', delimiter = '')
data_d4 = np.genfromtxt('speed_profile_w22_density4_kappa24.txt', delimiter = '')
data_d5 = np.genfromtxt('speed_profile_w22_density5_kappa24.txt', delimiter = '')
data_d6 = np.genfromtxt('speed_profile_w22_density6_kappa24.txt', delimiter = '')
data_d9 = np.genfromtxt('speed_profile_w22_density9_kappa24.txt', delimiter = '')



ancho_d2 = data_d2[:,0] 
v_media_d2 = data_d2[:,1] 
err_media_d2 = data_d2[:,2] 


ancho_d4 = data_d4[:,0] 
v_media_d4 = data_d4[:,1] 
err_media_d4 = data_d4[:,2] 

ancho_d5 = data_d5[:,0] 
v_media_d5 = data_d5[:,1] 
err_media_d5 = data_d5[:,2] 

ancho_d6 = data_d6[:,0] 
v_media_d6 = data_d6[:,1] 
err_media_d6 = data_d6[:,2] 

ancho_d9 = data_d9[:,0] 
v_media_d9 = data_d9[:,1] 
err_media_d9 = data_d9[:,2] 



###  PLOT  ###

plt.plot(ancho_d2,v_media_d2,'b--x',mew=0.7,markersize=4,label='$\\rho$=2~p/m$^2$') 
plt.errorbar(ancho_d2[::4],v_media_d2[::4],err_media_d2[::4],linestyle='none',fmt='none',color='none',ecolor='b') 

plt.plot(ancho_d5,v_media_d5,'g:^',mew=0.7,markerfacecolor='g',markersize=4,markeredgecolor='k',label='$\\rho$=5~p/m$^2$') 
plt.errorbar(ancho_d5[::4],v_media_d5[::4],err_media_d5[::4],linestyle='none',fmt='none',color='none',ecolor='g') 

plt.plot(ancho_d6,v_media_d6,'y-.o',mew=0.7,markerfacecolor='y',markeredgecolor='k',markersize=4,zorder=3,label='$\\rho$=6~p/m$^2$') 
plt.errorbar(ancho_d6[::4],v_media_d6[::4],err_media_d6[::4],linestyle='none',fmt='none',color='none',ecolor='y') 

plt.plot(ancho_d9,v_media_d9,'-rs',mew=0.7,markerfacecolor='r',markeredgecolor='k',markersize=4,label='$\\rho$=9~p/m$^2$') 
plt.errorbar(ancho_d9[::4],v_media_d9[::4],err_media_d9[::4],linestyle='none',fmt='none',color='none',ecolor='r') 


pylab.legend()
#pylab.xticks(np.arange(0,9,2))
pylab.yticks(np.arange(0,1.1,0.25))
pylab.xlabel('$y$-location~(m)')
pylab.ylabel('Velocity (m/s)')
pylab.ylim(0, 1.2)
pylab.xlim(0, 22.2)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=0.2,borderpad=0.2,handletextpad=0.1,fontsize=6,numpoints=1)
pylab.savefig('v(y)_width22_k24.eps', format='eps', dpi=300, bbox_inches='tight')
