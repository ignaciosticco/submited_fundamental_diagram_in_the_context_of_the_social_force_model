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
print(list_vd)

def promedia_te(te,iter_total,vd_total):
	te_mean=[]
	te_std=[]
	i=0
	while i<vd_total:
		te_mean+=[np.mean(te[i*iter_total:i*iter_total+iter_total])]
		te_std += [np.std(te[i*iter_total:i*iter_total+iter_total])]
		i+=1
	return te_mean,te_std

te_mean=promedia_te(te_koriginal,iter_total,vd_total)[0]
e_te_mean=promedia_te(te_koriginal,iter_total,vd_total)[1]
te_mean_kx10=promedia_te(te_kx10,iter_total,vd_total)[0]
e_te_mean_kx10=promedia_te(te_kx10,iter_total,vd_total)[1]

###  PLOT  ###

### original kappa ###
#plt.plot(list_vd,te_mean,'--bo',mew=0.7,mec='b',markersize=4,label='$\\kappa=2.4\\times10^{5}$') 
#plt.errorbar(list_vd,te_mean,e_te_mean,linestyle='none',fmt='none',color='none',ecolor='b') 

### modified kappa ###
#plt.plot(list_vd,te_mean_kx10,'-.rs',mfc='none',mew=0.7,mec='r',markersize=4,label='$\\kappa=2.4\\times10^{6}$') 
#plt.errorbar(list_vd,te_mean_kx10,e_te_mean_kx10,linestyle='none',fmt='none',color='none',ecolor='r') 

### ratio ###

ratio =np.divide(te_mean_kx10,te_mean)
e_ratio =[]
i=0
while i<vd_total:
	e_ratio+=[e_te_mean[i]/te_mean_kx10[i] + te_mean_kx10[i]**(-2)*te_mean[i]*e_te_mean_kx10[i]]
	i+=1

#plt.plot(list_vd,ratio,'go',mew=0.3,mec='k',markersize=3) 
#plt.errorbar(list_vd,ratio,e_ratio,linestyle='none',fmt='o',color='none',ecolor='g') 
plt.errorbar(list_vd,ratio,e_ratio,linestyle='none',color='g',elinewidth='1',markeredgewidth='2') 

'''
## Fiteo lineal ##
coef_fit = np.polyfit(list_vd[7::],ratio[7::],1)
a = coef_fit[0]
b = coef_fit[1]
print(a)
t = np.linspace(5,7.5,100)
#plt.plot(t,t*a+b,'-r')
#plt.axhline(y=9, color='r', linestyle='-')
'''

pylab.grid(False)
#pylab.xlabel('time~$(s)$')
pylab.xlabel('$v_d$~(m/s)')
#pylab.title('Rate evacuation time')
#pylab.ylabel('$t_e$~(s)')
pylab.ylabel('$t_e(\\kappa_{10})/t_e$')
#pylab.legend()
#pylab.ylim(0.0, 3.6)
#pylab.yticks(np.arange(3,11,2))
pylab.ylim(0, 10)
pylab.xlim(0, 8)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
pylab.savefig('fis_cociente.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('fis_cociente.eps', format='eps', dpi=300, bbox_inches='tight')
