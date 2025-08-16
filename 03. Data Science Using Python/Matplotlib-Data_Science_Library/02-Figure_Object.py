import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10,11)
y = x ** 2
a = np.arange(1,11)
b = a ** 3


fig = plt.figure()
# print(fig)
# Big Axes
axes1 = fig.add_axes([0.1,0.1,0.85,0.85])
axes1.plot(x,y)
axes1.set_xlabel("x")
axes1.set_ylabel("f(x) y")

# Small Axes
axes2 = fig.add_axes([0.5,0.5,0.25,0.25])
axes2.plot(x,y)
axes2.set_xlabel("x")
axes2.set_ylabel("f(x) y")
axes2.set_xlim(2,4)
axes2.set_ylim(4,25)
# axes.grid(True)
# print(axes)
# plt.show()


### Figure Parameters
fig1 = plt.figure(figsize=(4,4),dpi = 500)
axes1 = fig1.add_axes([0,0,1,1])
axes1.plot(x,y)
# plt.show()

fig1.savefig("new_figue_matplotlib.jpg",bbox_inches="tight")
