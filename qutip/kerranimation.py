# Paola Frunzio
# 7/23/21, 8/3/21
# kerr movie

# libraries
import itertools
from qutip import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# fig, axes = plt.subplots()

# inputs
hbar = 1
t=2
omega = 1
alpha = 2
N = 20
sec = 2
steps = 30

# hamiltonian
H_Kerr = omega * create(N)**2 * destroy(N)**2 #Kerr "cat"

xvec = np.linspace(-5, 5, 500)

def data_gen():
  for i in itertools.count():
    t = i/steps
    yield (-1j * H_Kerr/hbar * t).expm() * coherent(N, alpha).unit()

def frame(data):
  psi = data

  W = wigner(psi, xvec, xvec)
  nrm = mpl.colors.Normalize(-W.max(), W.max())
  # wmap = wigner_cmap(W)
  
  plt1 = axes[0].contourf(xvec, xvec, W, 100, cmap="RdBu_r", norm=nrm)

  # plt2 = axes[1].contourf(xvec, xvec, W, 100, cmap=wmap)

  return plt1

# add colorbar
W = wigner((-1j * H_Kerr/hbar * t).expm() * coherent(N, alpha).unit(), xvec, xvec)
nrm = mpl.colors.Normalize(-W.max(), W.max())
wmap = wigner_cmap(W)
plt1 = axes[0].contourf(xvec, xvec, W, 100, cmap="RdBu_r", norm=nrm)
# plt2 = axes[1].contourf(xvec, xvec, W, 100, cmap=wmap)

axes[0].set_title("Standard Colormap")
cb1 = fig.colorbar(plt1, ax=axes[0])

# axes[1].set_title("Wigner Colormap")
# cb2 = fig.colorbar(plt2, ax=axes[1])

ani = animation.FuncAnimation(fig, frame, data_gen, save_count=50, blit=False, repeat=True)

ani
