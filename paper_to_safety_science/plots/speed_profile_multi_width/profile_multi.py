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


data_w4 = np.genfromtxt('speed_profile_w4_density6_kappa24.txt', delimiter = '')
data_w15 = np.genfromtxt('speed_profile_w15_density6_kappa24.txt', delimiter = '')
data_w22 = np.genfromtxt('speed_profile_w22_density6_kappa24.txt', delimiter = '')
data_w40 = np.genfromtxt('speed_profile_w40_density6_kappa24.txt', delimiter = '')

ancho_w4 = data_w4[:,0] 
v_media_w4 = data_w4[:,1] 
err_media_w4 = data_w4[:,2] 
ancho_w4 = np.true_divide(ancho_w4,4.0)

ancho_w15 = data_w15[:,0] 
v_media_w15 = data_w15[:,1] 
err_media_w15 = data_w15[:,2] 
ancho_w15 = np.true_divide(ancho_w15,15.0)

ancho_w22 = data_w22[:,0] 
v_media_w22 = data_w22[:,1] 
err_media_w22 = data_w22[:,2] 
ancho_w22 = np.true_divide(ancho_w22,22.0)

ancho_w40 = data_w40[:,0] 
v_media_w40 = data_w40[:,1] 
err_media_w40 = data_w40[:,2] 
ancho_w40 = np.true_divide(ancho_w40,40.0)


###  PLOT  ###

fig, ax1 = plt.subplots()
ax1.plot(ancho_w4,v_media_w4,'b--x',mew=0.7,markersize=4,label='width=4m') 
ax1.errorbar(ancho_w4[::4],v_media_w4[::4],err_media_w4[::4],linestyle='none',fmt='none',color='none',ecolor='b') 

ax1.plot(ancho_w15[::2],v_media_w15[::2],'g:^',mew=0.7,markerfacecolor='g',markersize=4,markeredgecolor='k',label='width=15m') 
ax1.errorbar(ancho_w15[::4],v_media_w15[::4],err_media_w15[::4],linestyle='none',fmt='none',color='none',ecolor='g') 

ax1.plot(ancho_w22[::2],v_media_w22[::2],'y-.o',mew=0.7,markerfacecolor='y',markeredgecolor='k',markersize=4,zorder=3,label='width=22m') 
ax1.errorbar(ancho_w22[::4],v_media_w22[::4],err_media_w22[::4],linestyle='none',fmt='none',color='none',ecolor='y') 

ax1.plot(ancho_w40[::2],v_media_w40[::2],'-rs',mew=0.7,markerfacecolor='r',markeredgecolor='k',markersize=4,label='width=40m') 
ax1.errorbar(ancho_w40[::4],v_media_w40[::4],err_media_w40[::4],linestyle='none',fmt='none',color='none',ecolor='r') 


pylab.legend()

plt.xlabel('$y$-location~/~width ')
plt.ylabel('Velocity (m/s)')
plt.ylim(0.1, 1.3)
ax1.legend(frameon=False,loc='upper left',labelspacing=0.1,borderpad=0.1,handletextpad=0.1,fontsize=6,numpoints=1)

pylab.savefig('v(y)_multi_width.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('v(y)_multi_width.eps', format='eps', dpi=300, bbox_inches='tight')
