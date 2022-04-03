# Paola Frunzio
# 7/5/2021
# gaussian plot

# importing libraries
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

plt.title('Gaussian') 

# defining values
sigma_x = 1
sigma_y = 1
# y is p
c = 1
x0 = 1
y0 = 1

# changes axis boundaries
x = np.linspace(-3*sigma_x+x0, 3*sigma_x+x0, 1000)
y = np.linspace(-3*sigma_y+y0, 3*sigma_y+y0, 1000)
x, y = np.meshgrid(x, y)

gaussian = c*np.exp(-((pow(x-x0, 2)/(2*(pow(sigma_x, 2))))+(pow(y-y0, 2)/(2*(pow(sigma_y, 2))))))

plt.imshow(gaussian)

# 3D surveillance map
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, gaussian, cmap='bwr')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 3D view
# plt.show()

# top down
ax.view_init(azim=0, elev=90)
plt.show()
