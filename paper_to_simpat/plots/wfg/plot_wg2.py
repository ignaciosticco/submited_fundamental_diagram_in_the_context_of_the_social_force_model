# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

'''
Este script hace un grafico de calor del trabajo de la fuerza. 
Hay que pasarle 2 archivos con datos: - uno que tiene ID y Wg  
                                      - Otro que tiene las configuraciones (ID,x,y,etc)
'''

import pylab
import numpy as np
import matplotlib.pyplot as plt
import math

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    			# width  in inches
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
          'savefig.dpi': 600,
         }

pylab.rcParams.update(params)

######## DATA ########

wall_up = 22.0       ## PARAMETER

data1 = np.genfromtxt("wfg_density6_width%i"%wall_up,delimiter = ' ')
indice1 = data1[:,0]
wg = np.abs(data1[:,1])
data2 = np.genfromtxt("config_density6_width%i"%wall_up,delimiter = ' ')
indice2 = data2[:,0]
x = data2[:,1]
y = data2[:,2]
vx = data2[:,3]
vy = data2[:,4]
diameter = data2[:,5]

## Room sizes ##

wall_down = 0.0
begin_corridor = 2.0
end_corridor =  26.0
lenght_x = end_corridor-begin_corridor
lenght_y = wall_up-wall_down

###  ANALYSIS  ###

# Creamos matrices con X Y y el promedio de Wg por persona por 1 metro cuadrado 
grid_x = np.linspace(begin_corridor,end_corridor,end_corridor-begin_corridor)
grid_y = np.linspace(wall_down,wall_up,wall_up-wall_down)

grid_wg = np.zeros((len(grid_y),len(grid_x)))
grid_N = np.zeros((len(grid_y),len(grid_x)))

for i in range(0,len(wg)):
     col=int((x[i]-begin_corridor)/(lenght_x)*(len(grid_x)))
     fil = int((y[i]-wall_down)/(lenght_y)*(len(grid_y)))
     grid_wg[fil][col] += wg[i]
     grid_N[fil][col] += 1

grid_wg = np.divide(grid_wg,grid_N)
print(np.max(grid_wg))


###  PLOT  ###

levels=np.linspace(0,361.3,70,endpoint=True)
levbar=np.linspace(0,361.3,4,endpoint=True)
plt.contourf(grid_x,grid_y,grid_wg, levels, cmap=plt.cm.jet,labelsize=13,zorder=1)
plt.colorbar(ticks=levbar)
#cb = plt.colorbar()
#cb.ax.set_yticklabels(cb.ax.get_yticklabels(), fontsize=12)
plt.grid(False)
plt.xlabel('$x$-location~(m)',fontsize=13)
plt.ylabel('$y$-location~(m)',fontsize=13)
plt.yticks(np.linspace(0,wall_up-2,5), fontsize=13)
plt.xticks(fontsize=13)
pylab.savefig('abswg_width%i.eps'%wall_up,format='eps', bbox_inches='tight')