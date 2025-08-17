import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import seaborn as sns

df = pd.read_csv("./Excel Files/dm_office_sales.csv")
print(df.head())

plt.figure(figsize=(12,4),dpi=150)
# sns.scatterplot(x="salary",y="sales",data=df,hue="level of education",palette="Dark2")
# sns.scatterplot(x="salary",y="sales",data=df,size="work experience")
# sns.scatterplot(x="salary",y="sales",data=df,s=150,alpha=0.2)
sns.scatterplot(x="salary",y="sales",data=df,style="level of education",hue="level of education")

"""
# hue- Defines how we want to change our Colors of the Plots
# palette- Choose from pre defined set of Palletes to change the set of colors
# size - Increase the Size of Dots on the basis of a coulumn
# s- to increase the size generally
# alpha- to increase the transparency (b/w 0 and 1 0- Fully Transperant and 1- Fully Opaque)
# style- to change the plot marker on the basis of column 
# combine it with hue of same column to have different color of Markers as well

"""

# plt.show()
plt.savefig("My_First_ScatterPlot-Seaborn.png")