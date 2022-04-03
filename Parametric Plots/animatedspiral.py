# Paola Frunzio
# 7/4/2021
# animated spiral plot

# importing libraries
import itertools
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

# number of points on the circle
steps = 400

fig, ax = plt.subplots()
xdata, ydata = [], []
trace, = ax.plot([], [], lw=1)

plt.title('Spiral') 

ax.set_aspect('equal')
ax.grid(True, which='both', linestyle='dashed')

fig.set_size_inches(8, 8)

# setting up axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

axes = plt.gca()
axes.set_xlim([-1,1])
axes.set_ylim([-1,1])

def data_gen():
  for i in itertools.count():
    theta = ((2*np.pi)/steps)*i
    yield (np.exp((theta*-1)/10)*np.cos(theta)), (np.exp((theta*-1)/10)*np.sin(theta))

def frame(data):
  # defining values
  x, y = data
  xdata.append(x)
  ydata.append(y)

  trace.set_data(xdata, ydata)
  return trace

# animate
ani = animation.FuncAnimation(fig, frame, data_gen, save_count=steps)

ani
