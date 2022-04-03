# Paola Frunzio
# 7/16-21/21
# numerical plot of negative delta p

# libraries
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(12, 8)

#defining paramaters 
d = 0.1
t0 = .001
delta_t = .001
steps = 1000

t = np.arange(t0,100,delta_t)

pt = np.exp(-d*t)

plt.plot(t,pt,color="black")
plt.show()
