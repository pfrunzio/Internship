# Paola Frunzio
# 8/10-12/21, 8/17/21, 8/23/21
# gaussian that moves in phase space with harmonic hamiltonian with dissipation terms

# libraries
import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig = plt.figure()
plt.title('Gaussian Moving Through Phase Space with Harmonic Oscillator Hamiltonian and Dissapation Terms')

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
gamma = 1
D = 1

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
    t = i/steps
    yield x0*np.cos(omega*t) + (p0/(m*omega))*np.sin(omega*t), -1*m*omega*x0*np.sin(omega*t) + p0*np.cos(omega*t), i

# normalizing
W = np.exp(-((pow(x-x0, 2)/(2*(pow(sigma_x, 2))))+(pow(p-p0, 2)/(2*(pow(sigma_p, 2))))))
# A = np.sum(gaussian*dx*dp)
# W = gaussian/A

rho[:, :, 0] = W

nrm = mpl.colors.Normalize(-rho[:, :, 0].max(), rho[:, :, 0].max())

def frame(data):
  xt, pt, n = data
  
  W = np.exp(-((pow(x-xt, 2)/(2*(pow(sigma_x, 2)))) + (pow(p-pt, 2)/(2*(pow(sigma_p, 2))))))
  # A = np.sum(gaussian*dx*dp)
  # W = gaussian/A
  
  rho_dot = x * -1*((p-pt)/pow(sigma_p,2))*W - p * -1*((x-xt)/pow(sigma_x,2))*W 
  # + 2*gamma*p*-1*((p-pt)/pow(sigma_p,2))*W+W #just friction
  # + D*pow(-1*((p-pt)/pow(sigma_p,2)),2)*W #just diffusion
  # + 2*gamma*p*-1*((p-pt)/pow(sigma_p,2))*W+W + D*pow(-1*((p-pt)/pow(sigma_p,2)),2)*W #both

  rho[:, :, n+1] = rho[:, :, n] + rho_dot*Delta_t

  nrm = mpl.colors.Normalize(-rho[:, :, n].max(), rho[:, :, n].max())
  
  plot = plt.contourf(x, p, rho[:, :, n], levels=levels, cmap="RdBu_r", norm=nrm)
  return plot

# add colorbar
plt.colorbar(plt.contourf(x, p, rho[:, :, 0], levels=levels, cmap="RdBu_r", norm=nrm))

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=N-1, blit=False, repeat=True)

ani
