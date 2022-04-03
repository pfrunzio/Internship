# Paola Frunzio
# 7/2/2021
# circle plot

# importing libraries
import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots()

plt.title('Circle') 

# setting up axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.set_aspect('equal')
ax.grid(True, which='both', linestyle='dashed')

fig.set_size_inches(8, 8)

# defining values
theta = np.arange(0, 2*np.pi, .01)
x = np.cos(theta)
y = np.sin(theta)

ax.plot(x, y)
plt.show()
