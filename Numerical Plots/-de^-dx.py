# 7/22/21
# derivative equals -de^-dx (derivative of e^-dx)

# libraries
import numpy as np
import matplotlib.pyplot as plt

# inputs
T=10
N=1000
Delta_t = T/N
delta = 0.5

sol = np.zeros(N)
sol[0]=1

for n in range(N-1):
  sol[n+1] = sol[n] * (1-delta * Delta_t)
plt.plot(sol)

plt.show()
