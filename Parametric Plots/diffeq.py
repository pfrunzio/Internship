# Paola Frunzio
# 7/17-23/21, fixed 8/2/21
# system of two first order differential equations

# libraries
import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2,1)
fig.set_size_inches(12, 8)

# inputs
T = 10
N = 1000
Delta_t = T/1000
m = 100
omega = 1

x = np.zeros(N)
x[0]=0
p = np.zeros(N)
p[0]=1

for n in range(N-1):
  x[n+1] = x[n] + p[n]*Delta_t/m
  p[n+1] = p[n] - m*pow(omega,2)*x[n]*Delta_t

ax1.set_ylabel("x")
ax1.set_xlabel("t")
ax1.plot(x)

ax2.set_ylabel("p")
ax2.set_xlabel("t")
ax2.plot(p)

# ax1.plot(x, p)

plt.show()
