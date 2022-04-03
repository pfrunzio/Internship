# Paola Frunzio
# 8/31/21
# Kerr with moyal bracket

# libraries
import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig = plt.figure()
plt.title('Wigner Moving Through Phase Space With Kerr "cat" Hamiltonian')

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
hbar = 1

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

a = x + 1j*p
astar = x - 1j*p

T = 10
N = 20
Delta_t = .01
rho = np.zeros(((len(x), len(p), N)))

def data_gen():
  for i in itertools.count():
    t = i/steps
    yield x0*np.cos(omega*t) + (p0/(m*omega))*np.sin(omega*t), -1*m*omega*x0*np.sin(omega*t) + p0*np.cos(omega*t), i

# normalizing
gaussian = np.exp(-((pow(x-x0, 2)/(2*(pow(sigma_x, 2))))+(pow(p-p0, 2)/(2*(pow(sigma_p, 2))))))
A = np.sum(gaussian*dx*dp)
W = gaussian/A

rho[:, :, 0] = W

nrm = mpl.colors.Normalize(-rho[:, :, 0].max(), rho[:, :, 0].max())

def frame(data):
  xt, pt, n = data

  a0 = xt + 1j*pt
  astar0 = xt - 1j*pt
  
  # gaussian = np.exp(-((pow(x-xt, 2)/(2*(pow(sigma_x, 2)))) + (pow(p-pt, 2)/(2*(pow(sigma_p, 2))))))
  gaussian = np.exp(-(astar*a - astar0*a - astar*a0 + astar0*a0))
  A = np.sum(gaussian*dx*dp)
  W = gaussian/A  

  rho[:, :, n+1] = rho[:, :, n] + (Delta_t/(1j*hbar)*(
      ((hbar/2)*(-(astar-astar0)*W * 2*astar*a**2-(2*hbar*a) - (a-a0)*W * 2*astar**2*a-(2*hbar*astar) \
                - (2*astar**2*a-(2*hbar*astar) * -(a-a0)*W - 2*astar*a**2-(2*hbar*a) * -(astar-astar0)*W))) # up to here is checked w/ sympy
      + ((hbar/2)**2*(((-(astar-astar0))**2*W * 2*a**2 - (-(a-a0))**2*W * 2*astar**2) - (2*astar**2 * (-(a-a0))**2*W - 2*a**2 * (-(astar-astar0))**2*W)))))

  nrm = mpl.colors.Normalize(-np.real(rho[:, :, n]).max(), np.real(rho[:, :, n]).max())
  
  plot = plt.contourf(x, p, np.real(rho[:, :, n]), levels=levels, cmap="RdBu_r", norm=nrm)
  return plot

# add colorbar
plt.colorbar(plt.contourf(x, p, rho[:, :, 0], levels=levels, cmap="RdBu_r", norm=nrm))

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=N-1, blit=False, repeat=True)

ani
