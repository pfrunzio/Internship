# Paola Frunzio
# 8/3/21
# numerically solved hamiltonian

# libraries
import numpy as np
import matplotlib.pyplot as plt

# inputs
T=10
N=1000
Delta_t = T/N
delta = 0.5

P = np.zeros(N)
P[0]=1

for n in range(N-1):
  P[n+1] = P[n] + (Delta_t/i*h)*()

plt.plot(P)
plt.show()
