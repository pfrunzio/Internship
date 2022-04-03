# Paola Frunzio
# 7/14/2021, 9/2/21
# 2D gaussian plot animated

# importing libraries
import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig = plt.figure()
plt.title('Animated Gaussian')

# defining values
sigma_x = 1
sigma_p = 1
x0 = 1
p0 = 1
w = 1

# making everything units
m = 1 #kg
v_max = 10.0 #m/s
p_max = m*v_max
x_max = 10.0 #m
N = 8

# steps (actual number is this times 6)
steps = 3

# set up steps
dx = 2*x_max/pow(2, N)
dp = 2*p_max/pow(2, N)

# set up plot
x = np.arange(-x_max, x_max, dx)
p = np.arange(-p_max, p_max, dp)
x, p = np.meshgrid(x, p)

def data_gen():
  for i in itertools.count():
    t = i/steps
    yield x0*np.cos(w*t), -1*p0*w*np.sin(w*t)

# normalizing
gaussian = np.exp(-((pow(x-x0, 2)/(2*(pow(sigma_x, 2))))+(pow(p-p0, 2)/(2*(pow(sigma_p, 2))))))
A = np.sum(gaussian*dx*dp)
gaussian = gaussian/A

nrm = mpl.colors.Normalize(-gaussian.max(), gaussian.max())

def frame(data):
  xt, pt = data
  
  gaussian = np.exp(-((pow(x-xt, 2)/(2*(pow(sigma_x, 2))))+(pow(p-pt, 2)/(2*(pow(sigma_p, 2))))))
  A = np.sum(gaussian*dx*dp)
  gaussian = gaussian/A

  nrm = mpl.colors.Normalize(-gaussian.max(), gaussian.max())

  plot = plt.pcolormesh(x, p, gaussian, cmap="RdBu_r", norm=nrm)
  return plot

# add colorbar
plt.colorbar(plt.pcolormesh(x, p, gaussian, cmap="RdBu_r", norm=nrm))

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=6*steps, blit=False, repeat=True)

ani
