# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:53:12 2020

@author: legen
"""

from clear_console import cls 
import numpy as np
import matplotlib.pyplot as plt

cls()

points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z,cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

# Array-Oriented Programming with Arrays

pointss = np.arange(-1,1,0.5)
print(pointss)
xxs, yys = np.meshgrid(pointss,pointss)
zz = np.sqrt(xxs**2 + yys**2)
print(zz)
print(zz.shape)

plt.imshow(zz,cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot for a grid of values")




 