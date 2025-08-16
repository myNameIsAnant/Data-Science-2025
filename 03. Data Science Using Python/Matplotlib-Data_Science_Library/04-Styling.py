import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,11)

fig = plt.figure()
fig1 = plt.figure(dpi=250)
ax = fig.add_axes([0.1,0.1,0.85,0.85])
ax1 = fig1.add_axes([0.1,0.1,0.85,0.85])

### Legends
ax.plot(x,x**2,label="x^2")
ax.plot(x,x*2,label="2x")
ax.plot(x,color="brown")
ax.legend()
# plt.show()

### Colors and Styling
ax1.plot(x,x**2,label="x^2",color="#FFD900EA")
ax1.plot(x,2*x,label="2x",color="#D35CE2EA",lw =2)
ax1.plot(x,5*x,label="5x",color="#86E9DCEA",lw=3,ls="--")
ax1.plot(x,color="brown")
lines = ax1.plot(x,x+9,color="red",lw=3)
lines[0].set_dashes([1,1,3,1])
ax1.plot(x,x**3,label="x^3",color="green",lw=2,marker="^",ms=4,markerfacecolor="blue",markeredgecolor="red",markeredgewidth=0.5)
ax1.legend()
plt.show()

