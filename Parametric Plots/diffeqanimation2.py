# Paola Frunzio
# 8/2/21
# system of two first order differential equations animated
# parametric plot style version

# libraries
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig, ax = plt.subplots()
xdata, ydata = [], []
trace, = ax.plot([], [], lw=1)

ax.set_aspect('equal')
ax.grid(True, which='both', linestyle='dashed')

fig.set_size_inches(8, 8)

# setting up axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# inputs
T = 10
num = 1000
m = 100
omega = 1

axes = plt.gca()
axes.set_xlim([-num,num])
axes.set_ylim([-num,num])

# steps (actual number is this times 6)
steps = 3

x = np.zeros(num)
x[0]=0
p = np.zeros(num)
p[0]=1

def data_gen():
  for n in itertools.count():
    N = n+1
    Delta_t = T/N

    x[n+1] = x[n] + p[n]*Delta_t/m
    p[n+1] = p[n] - m*pow(omega,2)*x[n]*Delta_t
    yield x[n], p[n]

def frame(data):
  # defining values
  x, p = data
  xdata.append(x)
  ydata.append(p)

  trace.set_data(xdata, ydata)
  return trace

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=num-1, blit=False, repeat=True)

ani
