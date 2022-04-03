# Paola Frunzio
# 7/14/21
# e^x and aproximations

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
# plt.ylim(top=8000)
plt.ylim(top=20) #zoom in

x = np.linspace(0, 2.5, 100)

# equations
y = np.exp(x)
#taylor polynomials
y0 = 1+x*0
y1 = 1+x
y2 = 1+x+pow(x, 2)/np.math.factorial(2)
y3 = 1+x+pow(x, 2)/np.math.factorial(2)+pow(x, 3)/np.math.factorial(3)
y4 = 1+x+pow(x, 2)/np.math.factorial(2)+pow(x, 3)/np.math.factorial(3)+pow(x, 4)/np.math.factorial(4)
y5 = 1+x+pow(x, 2)/np.math.factorial(2)+pow(x, 3)/np.math.factorial(3)+pow(x, 4)/np.math.factorial(4)+pow(x, 5)/np.math.factorial(5)

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
