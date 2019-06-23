# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 13:59:26 2018

@author: sean
"""

import matplotlib.pyplot as plt
import numpy as np
#from scipy.interpolate import griddata
from matplotlib.mlab import griddata
#from matplotlib.collections import PatchCollection
from matplotlib import  cm
from mpl_toolkits.mplot3d import axes3d

data = np.loadtxt('result.txt', delimiter=',')
fig = plt.figure(figsize=(24, 6))

#p=PatchCollection(mypatches,color='none', alpha=1.0,edgecolor="purple",linewidth=2.0)
#levels=np.arange(data[:,2].min(),data[:,2].max(), 0.2)
levels1=np.arange(data[:,2].min(),data[:,2].max(), 5)
norm = cm.colors.Normalize(vmax=data[:,2].max(), vmin=data[:,2].min())

grid_x, grid_y = np.mgrid[data[:,0].min():data[:,0].max():250j, 
                          data[:,1].min():data[:,1].max():250j]   
#grid_z = griddata((data[:,0], data[:,1]), data[:,2], (grid_x, grid_y), method='cubic')
grid_z = griddata(data[:,0], data[:,1], data[:,2], grid_x, grid_y, interp='linear')
C = plt.contourf(grid_x, grid_y, grid_z, len(levels1)+8, 
                cmap=plt.cm.Spectral, norm=norm,)

C1 = plt.contour(grid_x, grid_y, grid_z, levels1, colors='k')

plt.clabel(C1, inline=1, fontsize=10)

for c in C1.collections:
    c.set_linestyle('solid')
    
plt.colorbar(C)

plt.subplots_adjust(left=0.04,right=1.1,wspace=0.25,hspace=0.25,bottom=0.1,top=0.94)

plt.savefig('conrour.eps', format='eps',dpi = 1000)

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#
#ax.plot_surface(grid_x, grid_y, grid_z, rstride=10, cstride=10,alpha=0.3)
#cset = ax.contourf(grid_x, grid_y, grid_z, offset=-20, cmap=cm.coolwarm)
##cset = ax.contour(grid_x, grid_y, grid_z,zdir='z', offset=-20, cmap=cm.coolwarm)
##cset = ax.contour(grid_x, grid_y, grid_z, zdir='x', offset=-10, cmap=cm.coolwarm)
##cset = ax.contour(grid_x, grid_y, grid_z, zdir='y', offset=38.9, cmap=cm.coolwarm)
#plt.show()

#cset1 = plt.contourf(X, Y, data[:,2], cmap=cm.PRGn,norm=norm)