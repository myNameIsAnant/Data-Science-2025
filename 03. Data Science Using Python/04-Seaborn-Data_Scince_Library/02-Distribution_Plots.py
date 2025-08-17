import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("./Excel Files/dm_office_sales.csv")
print(df.head())

##### Rug Plot #####
## Check Distribution of Salaries
# plt.figure(figsize=(12,8),dpi=150)
# sns.rugplot(x="salary",data=df,height=0.5)
"""
# height = decide the height of the ticks
"""
# plt.show()

##### Dist Plot #####
# sns.set(style="darkgrid")
# plt.figure(figsize=(12,8),dpi=150)
# sns.displot(data=df,x="salary",bins=40,color="red",edgecolor="blue",lw=2,ls="--",kde=True,rug=True)
"""
# bins = number of parts x axis will be divided into
# kde = True shows the Kernel Density Estimation Plot
# rug = True shows the rug Plot
"""
# plt.show()


##### Hist Plot #####
# sns.histplot(data=df,x="salary")



##### KDE Plot #####
# sns.kdeplot(data=df,x="salary")
# plt.show()


np.random.seed(42)
sample_ages=np.random.randint(0,100,200)
# print(sample_ages)
sample_ages = pd.DataFrame(sample_ages,columns=["age"])
print(sample_ages.head())

# sns.rugplot(data=sample_ages,x="age")
# sns.displot(data=sample_ages,x="age",rug=True,bins=30,kde=True)
sns.kdeplot(data=sample_ages,x="age",clip=[0,100],bw_adjust=0.8,shade=True)
plt.show()