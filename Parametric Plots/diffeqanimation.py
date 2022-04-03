# Paola Frunzio
# 8/2/21
# system of two first order differential equations animated

# libraries
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig = plt.figure()
fig.set_size_inches(8, 8)

# inputs
T = 10
m = 100
omega = 1

# steps (actual number is this times 6)
steps = 3

x = np.zeros(N)
x[0]=0
p = np.zeros(N)
p[0]=1

def data_gen():
  for i in itertools.count():
    N = i+1
    Delta_t = T/N
    yield N, Delta_t

def frame(data):
  N, Delta_t = data
  n = N-1

  x[n+1] = x[n] + p[n]*Delta_t/m
  p[n+1] = p[n] - m*pow(omega,2)*x[n]*Delta_t

  plot = plt.pcolormesh(x[n+1], p[n+1], cmap="seismic", vmax=1.0, vmin=-1.0)
  return plot
plt.colorbar(plt.pcolormesh(x, p, cmap="seismic", vmax=1.0, vmin=-1.0))

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=6*steps, blit=False, repeat=True)

ani
