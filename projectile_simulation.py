#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import sin,cos,pi

u0 = 40 # projectile velocity
g = 9.81 # gravity

theta1 = 45 # projectile angle
theta2 = 30

ux1 = u0*cos(theta1*pi/180)
uy1 = u0*sin(theta1*pi/180)

ux2 = u0*cos(theta2*pi/180)
uy2 = u0*sin(theta2*pi/180)

t_total_1 = 2*uy1/g
t_total_2= 2*uy2/g

t1 = np.linspace(0,t_total_1,100)
t2 = np.linspace(0,t_total_2,100)

sx1 = ux1*t1
sy1 = (uy1*t1)-(0.5*g*t1**2)

sx2 = ux2*t2
sy2 = (uy2*t2)-(0.5*g*t2**2)

plt.figure(figsize=(10,5))
plt.plot(sx1,sy1,label=r'$\theta={}$'.format(theta1))
plt.plot(sx2,sy2,label=r'$\theta={}$'.format(theta2))
plt.ylim(0,50)
plt.legend()
plt.show()


# In[ ]:




