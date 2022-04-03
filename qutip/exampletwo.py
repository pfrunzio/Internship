import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np

# inputs
hbar = 1
t=21.99
omega = 1
alpha = 2
N = 20

# hamiltonians
H_harm = omega * create(N) * destroy(N) #harmonic
H_Kerr = omega * create(N)**2 * destroy(N)**2 #Kerr "cat"
#H_harm_driven = 

psi = (-1j * H_Kerr /hbar * t).expm() * coherent(N, alpha).unit()#(basis(10, 0) + basis(10, 3) + basis(10, 9)).unit()

xvec = np.linspace(-5, 5, 500)

W = wigner(psi, xvec, xvec)

wmap = wigner_cmap(W)  # Generate Wigner colormap

nrm = mpl.colors.Normalize(-W.max(), W.max())

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

plt1 = axes[0].contourf(xvec, xvec, W, 100, cmap=cm.RdBu, norm=nrm)

axes[0].set_title("Standard Colormap");

cb1 = fig.colorbar(plt1, ax=axes[0])

plt2 = axes[1].contourf(xvec, xvec, W, 100, cmap=wmap)  # Apply Wigner colormap

axes[1].set_title("Wigner Colormap");

cb2 = fig.colorbar(plt2, ax=axes[1])

fig.tight_layout()

plt.show()
