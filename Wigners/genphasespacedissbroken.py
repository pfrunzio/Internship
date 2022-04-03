# Paola Frunzio
# 8/21-22/21
# generalized moving through phase space with dissapation

# libraries
from sympy import *
import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig = plt.figure()


# inputs
num = 6 #resolution
steps = 3 #increment for timestep
levels = 100 #number of contour lines

sigma_x = 1 #x axis diameter
sigma_p = 1 #y axis diameter
x0 = 3 #starting x coordinate
p0 = 0 #starting y coordinate
omega = 1
gamma = 1
D = 1

m = 1 #kg
v_max = 10.0 #m/s
p_max = m*v_max
x_max = 10.0 #m


# set up grid
dx = 2*x_max/pow(2, num)
dp = 2*p_max/pow(2, num)

x = np.arange(-x_max, x_max, dx)
p = np.arange(-p_max, p_max, dp)
x, p = np.meshgrid(x, p)

T = 10
N = 50
Delta_t = T/N


def data_gen():
  for i in itertools.count():
    t = i/steps
    yield x0*np.cos(omega*t) + (p0/(m*omega))*np.sin(omega*t), -1*m*omega*x0*np.sin(omega*t) + p0*np.cos(omega*t), i


# Sympy setup
xs, xts, ps, pts = symbols('xs xts ps pts')

# initial state of Rho
rho_equation = exp(-((pow(xs-xts, 2)/(2*(pow(sigma_x, 2))))+(pow(ps-pts, 2)/(2*(pow(sigma_p, 2))))))
A = np.sum(rho_equation*dx*dp)
rho_equation = rho_equation/A
print(rho_equation)

# Hamiltonian
H = xs**2 + ps**2
# H = xs**4 + 2*xs**2*ps**2 + ps**4


rho_dot_equation = diff(H, xs) * diff(rho_equation, ps) - diff(rho_equation, xs) * diff(H, ps) \
# + 2*gamma*ps*diff(rho_equation*ps, ps) #just friction
# + D*diff(diff(rho_equation, ps), ps) #just diffusion
# + 2*gamma*ps*-1*diff(rho_equation*ps, ps) + D*diff(diff(rho_equation, ps), ps) #both

rho_sol = lambdify([xs,ps], rho_equation.subs([(xts, x0), (pts, p0)]), "numpy")

rho = np.zeros(((len(x), len(p), N)))
rho[:, :, 0] = rho_sol(x,p)


# normalizing
# A = np.sum(rho[:, :, 0]*dx*dp)
# rho[:, :, 0] = rho[:, :, 0]/A

nrm = mpl.colors.Normalize(-rho[:, :, 0].max(), rho[:, :, 0].max())


def frame(data):
  xt, pt, n = data 
  

  # solution
  rho_dot_sol = lambdify([xs,ps,xts,pts], rho_dot_equation, "numpy")

  rho[:, :, n+1] = rho[:, :, n] + rho_dot_sol(x,p,xt,pt)*Delta_t


  # normalizing
  A = np.sum(rho[:, :, n]*dx*dp)
  rho[:, :, n] = rho[:, :, n]/A

  nrm = mpl.colors.Normalize(-rho[:, :, n].max(), rho[:, :, n].max())


  plot = plt.contourf(x, p, rho[:, :, n], levels=levels, cmap="RdBu_r", norm=nrm)
  return plot

# add colorbar
plt.colorbar(plt.contourf(x, p, rho[:, :, 0], levels=levels, cmap="RdBu_r", norm=nrm))

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=N-1, blit=False, repeat=True)

ani
