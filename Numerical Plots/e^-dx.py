# Paola Frunzio
# 7/22/21
# numerical plot of e to the negative delta x

# libraries
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(12, 8)
plt.ylim(top=2, bottom=-2)

d = 1/2
x_max = 50

x = np.linspace(-x_max,x_max,x_max*2)

function = np.exp((-d)*x)
ex = np.exp(x)
first_derivative = (-d)*function
second_derivative = (-d)*first_derivative
third_derivative = (-d)*second_derivative

plt.plot(x,ex,color="black",label="e^x")
plt.plot(x,function,color="red",label="f(x)")
plt.plot(x,first_derivative,color="orange",label="f'(x)")
plt.plot(x,second_derivative,color="yellow",label="f''(x)")
plt.plot(x,third_derivative,color="green",label="f'''(x)")

zero = np.zeros(x_max*2)
one = np.ones(x_max*2)

plt.plot(0,1,'ro',color="black")
# plt.plot(0,-1*d,'ro',color="black")

plt.show()
