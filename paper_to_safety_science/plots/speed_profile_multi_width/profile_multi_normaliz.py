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

# density = 6
data_w4 = np.genfromtxt('speed_profile_w4_density6_kappa24.txt', delimiter = '')
data_w15 = np.genfromtxt('speed_profile_w15_density6_kappa24.txt', delimiter = '')
data_w22 = np.genfromtxt('speed_profile_w22_density6_kappa24.txt', delimiter = '')
data_w40 = np.genfromtxt('speed_profile_w40_density6_kappa24.txt', delimiter = '')

# density = 9
data_w4_d9 = np.genfromtxt('speed_profile_w4_density9_kappa24.txt', delimiter = '')
data_w15_d9 = np.genfromtxt('speed_profile_w15_density9_kappa24.txt', delimiter = '')
data_w22_d9 = np.genfromtxt('speed_profile_w22_density9_kappa24.txt', delimiter = '')
data_w40_d9 = np.genfromtxt('speed_profile_w40_density9_kappa24.txt', delimiter = '')

### function normalization of error ###

def error_norm(v,error_v):
	vmax = max(v)
	err_vmax = error_v[np.where(v==vmax)][0]
	error_norm = []
	for i in range(0,len(v)):
		e = (1/vmax)*error_v[i]+(err_vmax*v[i])/(vmax*vmax)
		error_norm+=[e]
	return error_norm



## Density = 6 ##
ancho_w4 = data_w4[:,0] 
v_media_w4 = data_w4[:,1] 
err_media_w4 = data_w4[:,2] 
error_norm_w4 = np.array(error_norm(v_media_w4,err_media_w4))
ancho_w4 = np.true_divide(ancho_w4,4.0)
v_media_w4 = np.true_divide(v_media_w4,max(v_media_w4))


ancho_w15 = data_w15[:,0] 
v_media_w15 = data_w15[:,1] 
err_media_w15 = data_w15[:,2] 
error_norm_w15 = np.array(error_norm(v_media_w15,err_media_w15))
ancho_w15 = np.true_divide(ancho_w15,15.0)
v_media_w15 = np.true_divide(v_media_w15,max(v_media_w15))


ancho_w22 = data_w22[:,0] 
v_media_w22 = data_w22[:,1] 
err_media_w22 = data_w22[:,2] 
error_norm_w22 = np.array(error_norm(v_media_w22,err_media_w22))
ancho_w22 = np.true_divide(ancho_w22,22.0)
v_media_w22 = np.true_divide(v_media_w22,max(v_media_w22))

ancho_w40 = data_w40[:,0] 
v_media_w40 = data_w40[:,1] 
err_media_w40 = data_w40[:,2] 
error_norm_w40 = np.array(error_norm(v_media_w40,err_media_w40))
ancho_w40 = np.true_divide(ancho_w40,40.0)
v_media_w40 = np.true_divide(v_media_w40,max(v_media_w40))

## Density = 9 ##

ancho_w4_d9 = data_w4_d9[:,0] 
v_media_w4_d9 = data_w4_d9[:,1] 
err_media_w4_d9 = data_w4_d9[:,2] 
error_norm_w4_d9 = np.array(error_norm(v_media_w4_d9,err_media_w4_d9))
ancho_w4_d9 = np.true_divide(ancho_w4_d9,4.0)
v_media_w4_d9 = np.true_divide(v_media_w4_d9,max(v_media_w4_d9))

ancho_w15_d9 = data_w15_d9[:,0] 
v_media_w15_d9 = data_w15_d9[:,1] 
err_media_w15_d9 = data_w15_d9[:,2] 
error_norm_w15_d9 = np.array(error_norm(v_media_w15_d9,err_media_w15_d9))
ancho_w15_d9 = np.true_divide(ancho_w15_d9,15.0)
v_media_w15_d9 = np.true_divide(v_media_w15_d9,max(v_media_w15_d9))


ancho_w22_d9 = data_w22_d9[:,0] 
v_media_w22_d9 = data_w22_d9[:,1] 
err_media_w22_d9 = data_w22_d9[:,2] 
error_norm_w22_d9 = np.array(error_norm(v_media_w22_d9,err_media_w22_d9))
ancho_w22_d9 = np.true_divide(ancho_w22_d9,22.0)
v_media_w22_d9 = np.true_divide(v_media_w22_d9,max(v_media_w22_d9))

ancho_w40_d9 = data_w40_d9[:,0] 
v_media_w40_d9 = data_w40_d9[:,1] 
err_media_w40_d9 = data_w40_d9[:,2] 
error_norm_w40_d9 = np.array(error_norm(v_media_w40_d9,err_media_w40_d9))
ancho_w40_d9 = np.true_divide(ancho_w40_d9,40.0)
v_media_w40_d9 = np.true_divide(v_media_w40_d9,max(v_media_w40_d9))


###  PLOT  ###

## Density = 6 ##

plt.plot(ancho_w4[1::2],v_media_w4[1::2],'bx',markersize=4,zorder=1,label='width=4m') 
plt.errorbar(ancho_w4[1::4],v_media_w4[1::4],error_norm_w4[1::4],linestyle='-',fmt='.',color='none',ecolor='b',zorder=2) 

plt.plot(ancho_w15[1::4],v_media_w15[1::4],'g^',markerfacecolor='none',markeredgecolor='g',markersize=4,zorder=1) 
plt.errorbar(ancho_w15[1::8],v_media_w15[1::8],error_norm_w15[1::8],linestyle='-',fmt='.',color='none',ecolor='g',zorder=3) 

plt.plot(ancho_w22[1::4],v_media_w22[1::4],'yo',markerfacecolor='none',markeredgecolor='y',markersize=4,zorder=1) 
plt.errorbar(ancho_w22[1::8],v_media_w22[1::8],error_norm_w22[1::8],linestyle='-',fmt='.',color='none',ecolor='y',zorder=3) 

plt.plot(ancho_w40[1::4],v_media_w40[1::4],'rs',markerfacecolor='none',markeredgecolor='r',markersize=3,zorder=1) 
#plt.errorbar(ancho_w40[1::16],v_media_w40[1::16],error_norm_w40[1::16],linestyle='-',fmt='.',color='none',ecolor='r',zorder=3) 

## Density = 9 ##

plt.scatter(ancho_w4_d9[::2],v_media_w4_d9[::2],marker='x',color='b',linewidths=1,zorder=1) 
plt.errorbar(ancho_w4_d9[::4],v_media_w4_d9[::4],error_norm_w4_d9[::4],linestyle='-',fmt='.',color='none',ecolor='b',zorder=2) 

plt.plot(ancho_w15_d9[::4],v_media_w15_d9[::4],'g^',markerfacecolor='g',markeredgecolor='k',markersize=4,zorder=1,label='width=15m') 
plt.errorbar(ancho_w15_d9[::8],v_media_w15_d9[::8],error_norm_w15_d9[::8],linestyle='-',fmt='.',color='none',ecolor='g',zorder=2) 

plt.plot(ancho_w22_d9[::4],v_media_w22_d9[::4],'yo',markerfacecolor='y',markeredgecolor='k',markersize=4,zorder=1,label='width=22m') 
plt.errorbar(ancho_w22_d9[::8],v_media_w22_d9[::8],error_norm_w22_d9[::8],linestyle='-',fmt='.',color='none',ecolor='y',zorder=2) 

plt.plot(ancho_w40_d9[::4],v_media_w40_d9[::4],'rs',markerfacecolor='r',markeredgecolor='k',markersize=3,zorder=1,label='width=40m') 
plt.errorbar(ancho_w40_d9[::12],v_media_w40_d9[::12],error_norm_w40_d9[::12],linestyle='-',fmt='.',color='none',ecolor='r',zorder=2) 


pylab.legend()
#pylab.xticks(np.arange(0,9,2))
pylab.yticks(np.arange(0,1.1,0.25))
pylab.xlabel('$y$-location~/~width ')
pylab.ylabel('$v~/~v_{max}$ ')
pylab.ylim(0.25, 1.1)
pylab.xlim(0, 1.02)
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=0.1,borderpad=0.1,handletextpad=0.1,fontsize=6,numpoints=1)
pylab.savefig('v(y)_multi_width_normalizado.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('v(y)_multi_width_normaliz.eps', format='eps', dpi=300, bbox_inches='tight')
