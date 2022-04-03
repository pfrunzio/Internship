# Paola Frunzio
# 8/4-5/21, 8/10-16/21
# wigner that moves in phase space with harmonic oscillator hamiltonian

# libraries
import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig = plt.figure()
plt.title('Gaussian Moving Through Phase Space With Harmonic Oscillator Hamiltonian')

# inputs
num = 6 # 8 eventually
steps = 3
levels = 100

# defining values
sigma_x = 1
sigma_p = 1
x0 = 3 #x coordinate
p0 = 0 #y coordinate
omega = 1

# making everything units
m = 1 #kg
v_max = 10.0 #m/s
p_max = m*v_max
x_max = 10.0 #m

# set up steps
dx = 2*x_max/pow(2, num)
dp = 2*p_max/pow(2, num)

# set up plot
x = np.arange(-x_max, x_max, dx)
p = np.arange(-p_max, p_max, dp)
x, p = np.meshgrid(x, p)

T = 10
N = 50
Delta_t = T/N
rho = np.zeros(((len(x), len(p), N)))

def data_gen():
  for i in itertools.count():
    yield i

# normalizing
gaussian = np.exp(-((pow(x-x0, 2)/(2*(pow(sigma_x, 2))))+(pow(p-p0, 2)/(2*(pow(sigma_p, 2))))))
A = np.sum(gaussian*dx*dp)
W = gaussian*A

rho[:, :, 0] = W

nrm = mpl.colors.Normalize(-rho[:, :, 0].max(), rho[:, :, 0].max())

def frame(data):
  n = data  
  
  rho_dot = x * -1*((p-p0)/pow(sigma_p,2))*rho[:, :, n] - p * -1*((x-x0)/pow(sigma_x,2))*rho[:, :, n]

  rho[:,:,n+1] = rho[:,:,n+1]*0
  rho[:, :, n+1] = rho[:, :, n] + rho_dot*Delta_t 

  arho = np.sum(rho[:, :, n+1]*dx*dp)
  rho[:, :, n+1] = rho[:, :, n+1]*arho

  nrm = mpl.colors.Normalize(-rho[:, :, n+1].max(), rho[:, :, n+1].max())
  
  plot = plt.contourf(x, p, rho[:, :, n+1], levels=levels, cmap="RdBu_r", norm=nrm)
  return plot

# add colorbar
plt.colorbar(plt.contourf(x, p, rho[:, :, 0], levels=levels, cmap="RdBu_r", norm=nrm))

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=T*3, blit=False, repeat=True)

ani
