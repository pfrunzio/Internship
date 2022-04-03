# Paola Frunzio
# 7/2/2021
# graph of mass spring system over time with friction

# importing libraries
import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots()

plt.title('Mass Spring System Over Time with Friction') 

# setting up axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.set_aspect('equal')
ax.grid(True, which='both', linestyle='dashed')

fig.set_size_inches(20, 8)

# defining values
t = np.arange(0, 2*np.pi, .01)
x = np.exp(t*-1)*np.cos(10*t)
p = np.exp(t*-1)*np.sin(10*t)
decay = np.exp(t*-1)

ax.plot(t, x, label = 'displacement from equilibrium')
ax.plot(t, p, label = 'momentum')
ax.plot(t, decay, label = 'decay')
plt.legend()
plt.show()
