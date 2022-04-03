# Paola Frunzio
# 7/14/21
# sin(x) and aproximations

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
plt.ylim(top=.1, bottom=-.1)

# setting up axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

x = np.linspace(-.1, .1, 100)

# equations
y = np.sin(x)
#taylor polynomials
y0 = x
y1 = x-pow(x, 3)/np.math.factorial(3)
y2 = x-pow(x, 3)/np.math.factorial(3)+pow(x, 5)/np.math.factorial(5)
y3 = x-pow(x, 3)/np.math.factorial(3)+pow(x, 5)/np.math.factorial(5)-pow(x, 7)/np.math.factorial(7) 
y4 = x-pow(x, 3)/np.math.factorial(3)+pow(x, 5)/np.math.factorial(5)-pow(x, 7)/np.math.factorial(7)+pow(x, 9)/np.math.factorial(9)
y5 = x-pow(x, 3)/np.math.factorial(3)+pow(x, 5)/np.math.factorial(5)-pow(x, 7)/np.math.factorial(7)+pow(x, 9)/np.math.factorial(9)-pow(x, 11)/np.math.factorial(11)

# plots
plt.plot(x, y, color="black", label="f(x)")

plt.plot(x, y0, color="red", label="p_0(x)")
plt.plot(x, y1, color="orange", label="p_1(x)")
plt.plot(x, y2, color="yellow", label="p_2(x)")
plt.plot(x, y3, color="green", label="p_3(x)")
plt.plot(x, y4, color="blue", label="p_4(x)")
plt.plot(x, y5, color="purple", label="p_5(x)")

plt.legend()
plt.show()
