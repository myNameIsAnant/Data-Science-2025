import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0,11)
b = a * 2

x = np.arange(-10,11)
y = x ** 2

c = np.arange(1,5)
d = c ** 3

p = np.arange(1,5)
q = p ** 4

fig,axes = plt.subplots(ncols=2)
axes[0].plot(a,b)
axes[1].plot(x,y)
# plt.show()


fig1,axes1 = plt.subplots(nrows=2,ncols=2,dpi=250)
axes1[0][0].plot(a,b)
axes1[0][1].plot(x,y)
axes1[1][0].plot(c,d)
axes1[1][1].plot(p,q)
plt.subplots_adjust(wspace=0.5)
fig1.suptitle("My First Subplot",fontsize = 20)
# plt.show()

fig1.savefig("MyFirstSubplots_Matplotlib.jpg",bbox_inches="tight")