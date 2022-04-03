# Paola Frunzio
# 7/5-6/2021
# animated gaussian plot

# importing libraries
import itertools
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

# defining values
sigma_x = 1
sigma_y = 1
# y is p
c = 1
x0 = 1
y0 = 1
w = 1

#size of plot
if (3*sigma_x+x0) > (3*sigma_y+y0):
  size = 3*sigma_x+x0
else:
  size = 3*sigma_y+y0
# steps (actual number is this times 6)
steps = 10

x = np.linspace(-size, size, 1000)
y = np.linspace(-size, size, 1000)
x, y = np.meshgrid(x, y)

fig = plt.figure()
ax = Axes3D(fig)

def data_gen():
  for i in itertools.count():
    t = i/steps
    yield x0*np.cos(w*t), -1*y0*w*np.sin(w*t)

def frame(data):
  ax.clear()
  plt.title('Gaussian') 
  ax.set_xlabel('X(t)')
  ax.set_xlim3d(-size,size)
  ax.set_ylabel('Y(t)')
  ax.set_ylim3d(-size,size)
  ax.set_zlabel('Z(t)')
  ax.set_zlim3d(0,c) 

  xt, yt = data

  gaussian = c*np.exp(-((pow(x-xt, 2)/(2*(pow(sigma_x, 2))))+(pow(y-yt, 2)/(2*(pow(sigma_y, 2))))))

  plot = ax.plot_surface(x, y, gaussian, cmap='viridis')
  return plot

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=6*steps, blit=False, repeat=True)

ani
