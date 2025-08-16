import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,11)
y = x ** 2

# print(x)
# print(y)

plt.plot(x,y)
plt.title("f(x) y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-10,10)
plt.ylim(0,100)
# plt.show()
plt.savefig("myfirstplot_matplotlib.jpg")