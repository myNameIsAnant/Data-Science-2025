import matplotlib.pyplot as plt
import numpy as np

"""
plot e= mc^2
"""

m = np.arange(0,11)
c = 3 * 10**8
E = m * c**2


fig = plt.figure(dpi=150)
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(m,E,color="red",lw=2)
ax.set_xlabel("Mass (m)")
ax.set_ylabel("Energy (E)")
ax.set_xlim(0,10)
fig.suptitle("E = mc^2")
# plt.show()

"""
Plot e=mc^2 on a Logarithmic Scale
"""

fig2 = plt.figure(dpi=150)
ax2 = fig2.add_axes([0.1,0.1,0.8,0.8])
ax2.plot(m,E,color="red",lw=2)
ax2.set_yscale("log")
ax2.set_xlabel("Mass (m)")
ax2.set_ylabel("Energy (E)")
ax2.set_xlim(0,10)
# ax1.set_ylim(0,10**18)
ax2.grid(which="both",axis="y")
fig2.suptitle("E = mc^2")
# plt.show()

"""
Plot Yeild Curves Based on Provided Data
"""

### Data Provided Start
labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']
july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]
### Data Provided End

# Ploting in One Chart
fig3 = plt.figure(dpi=150)
ax3 = fig3.add_axes([0.1,0.1,0.8,0.8])
ax3.plot(labels,july16_2007,label="2007")
ax3.plot(labels,july16_2020,label="2020")
ax3.legend(loc=(1.04,0.5))
# plt.show()

# Plotting in 2 Charts
fig4,ax4 = plt.subplots(nrows=2,figsize=(12,8))
ax4[0].plot(labels,july16_2007,label="2007")
ax4[0].set_title("2007")
ax4[1].plot(labels,july16_2020,label="2020")
ax4[1].set_title("2020")
# plt.show()

# Plotting on TWin Axes

fig5,ax5 = plt.subplots(figsize=(12,8))
ax5.plot(labels,july16_2007,label="2007",color="blue")
ax5.set_ylabel("2007",fontsize=16,color="blue")
# ax4[0].set_title("2007")
ax6 = ax5.twinx()
ax6.plot(labels,july16_2020,label="2020",color="red")
ax6.set_ylabel("2020",fontsize=16,color="red")

ax5.spines["left"].set_color("blue")
ax5.spines["right"].set_color("red")

ax5.spines["left"].set_linewidth(5)
ax5.spines["right"].set_linewidth(5)

fig5.suptitle("Yeilds",fontsize=25)
plt.show()
