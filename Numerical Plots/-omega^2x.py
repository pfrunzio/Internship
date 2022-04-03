# 7/22/21
# second derivative is -omega^2*x

# libraries
import numpy as np
import matplotlib.pyplot as plt

T = 50
N = 50000
Delta_t = T/N

x = np.zeros(N)
x[0]=1
x_dot_at_zero = 0
x[1] = x[0] + x_dot_at_zero*Delta_t
w = 0.5
for n in range(N-2):
  x[n+2] = 2*x[n+1] - x[n] - (pow(w,2)*x[n]*pow(Delta_t,2))
plt.plot(x)

plt.show()
