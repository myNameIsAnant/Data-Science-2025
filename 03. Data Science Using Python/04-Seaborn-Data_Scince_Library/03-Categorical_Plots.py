import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("./Excel Files/dm_office_sales.csv")
print(df.head())

# print(np.round(df.groupby(["level of education","division"])["salary"].agg(["mean","std"]).fillna(0),2))


##### Categorical Plot For Single Column #####

### Count Plot
"""
plt.figure(figsize=(10,4),dpi=150)
sns.countplot(x="level of education",data=df,hue="division")
plt.show()
"""

### Bar Plot Plot
"""
plt.figure(figsize=(10,4),dpi=150)
sns.barplot(x="level of education",y="salary",data=df,estimator=np.mean,ci="sd",hue="division")
plt.legend(bbox_to_anchor=(1.05,1))
plt.show()
"""



##### Categorical Plot For Multiple Columns #####
df = pd.read_csv("./Excel Files/StudentsPerformance.csv")
print(df.head())

# df["Min Math Score"]= df.groupby(["parental level of education","race/ethnicity"])["math score"].transform("min")
# print(df)


### Box Plot ###
# plt.figure(dpi=150)
# sns.boxplot(data=df,y="math score",x="test preparation course",hue="test preparation course")
# plt.show()


"""
plt.figure(figsize=(12,8),dpi=150)
sns.boxplot(data=df,y="reading score",x="parental level of education",hue="test preparation course")
plt.legend(bbox_to_anchor=(1.05,0.5))
# plt.show()
plt.savefig("MyBoxPlot.jpg",bbox_inches="tight")
"""

### Violin Plot ###
"""
fig = plt.figure(figsize=(12,8),dpi=150)
fig.canvas.manager.set_window_title("Violin Plots")
sns.violinplot(data=df,x="math score",y="parental level of education",hue="test preparation course",split=True,inner="quartile")
plt.legend(bbox_to_anchor=(1.05,0.5))
plt.savefig("MyVoilinPlot.jpg",bbox_inches="tight")
# plt.show()
"""

fig = plt.figure(figsize=(12,8),dpi=150)
sns.swarmplot(data=df,x="math score",y="gender",hue="test preparation course",dodge=True,size=2)
"""
# hue = to decide color
# dodge = to separate the points for hue
# size to define the size of the dots
"""
plt.show()

