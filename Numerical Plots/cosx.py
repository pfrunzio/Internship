# Paola Frunzio
# 7/14/21
# cos(x) and aproximations

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
plt.ylim(top=1.5, bottom=0)

# setting up axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

x = np.linspace(-1.5, 1.5, 100)

# equations
y = np.cos(x)
#taylor polynomials
y0 = 1+x*0
y1 = 1-pow(x, 2)/np.math.factorial(2)
y2 = 1-pow(x, 2)/np.math.factorial(2)+pow(x, 4)/np.math.factorial(4)
y3 = 1-pow(x, 2)/np.math.factorial(2)+pow(x, 4)/np.math.factorial(4)-pow(x, 6)/np.math.factorial(6) 
y4 = 1-pow(x, 2)/np.math.factorial(2)+pow(x, 4)/np.math.factorial(4)-pow(x, 6)/np.math.factorial(6)+pow(x, 8)/np.math.factorial(8)
y5 = 1-pow(x, 2)/np.math.factorial(2)+pow(x, 4)/np.math.factorial(4)-pow(x, 6)/np.math.factorial(6)+pow(x, 8)/np.math.factorial(8)-pow(x, 10)/np.math.factorial(10)

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
