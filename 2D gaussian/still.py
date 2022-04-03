# Paola Frunzio
# 7/10-14/2021, 9/2/21
# 2D gaussian plot

# importing libraries
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.title('Gaussian')

# defining values
sigma_x = 1
sigma_p = 1
x0 = 1
p0 = 1

# making everything units
m = 1 #kg
v_max = 10.0 #m/s
p_max = m*v_max
x_max = 10.0 #m
N = 8

# making equation a function
def W(x, p):
  return np.exp(-((pow(x-x0, 2)/(2*(pow(sigma_x, 2))))+(pow(p-p0, 2)/(2*(pow(sigma_p, 2))))))

# normalizing
# A, e = integrate.dblquad(W, -x_max, x_max, -p_max, p_max)
# print(A)

# set up steps
dx = 2*x_max/pow(2, N)
dp = 2*p_max/pow(2, N)

# set up plot
x = np.arange(-x_max, x_max, dx)
p = np.arange(-p_max, p_max, dp)
x, p = np.meshgrid(x, p)

gaussian = W(x, p)
# also normalizing
A = np.sum(gaussian*dx*dp)

gaussian = gaussian/A

nrm = mpl.colors.Normalize(-gaussian.max(), gaussian.max())

plt.pcolormesh(x, p, gaussian, cmap="RdBu_r", norm=nrm)
plt.colorbar()
plt.show()
