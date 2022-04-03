# Paola Frunzio
# 7/9/2021
# circle plot but you choose the center 

# importing libraries
import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots()

plt.title('Circle') 

# set center of circle
x0 = 3
y0 = 2

ax.set_aspect('equal')
ax.grid(True, which='both', linestyle='dashed')

fig.set_size_inches(8, 8)

# defining values
theta = np.arange(0, 2*np.pi, .01)
x = np.cos(theta)+x0
y = np.sin(theta)+y0

ax.plot(x, y)
plt.show()
