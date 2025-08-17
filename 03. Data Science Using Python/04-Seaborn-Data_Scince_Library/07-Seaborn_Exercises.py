import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("./Excel Files/application_record.csv")
# print(df)

"""
Recreate the Scatter Plot shown below
"""

# employed = df[df["DAYS_EMPLOYED"]<0]
# employed["DAYS_EMPLOYED"] = employed["DAYS_EMPLOYED"] * -1
# employed["DAYS_BIRTH"] = employed["DAYS_BIRTH"] * -1

# plt.figure(figsize=(12,6),dpi=150)
# sns.scatterplot(data=employed,y="DAYS_EMPLOYED",x="DAYS_BIRTH",alpha=0.01,lw=0)
# plt.show()
# print(employed)



"""
Recreate the Histogram shown below
"""

# df["DAYS_BIRTH"] = df["DAYS_BIRTH"]*-1
# df["Age_Years"] =  np.round(df["DAYS_BIRTH"]/365,2)
# # print(df["Age_Years"])
# sns.histplot(data=df,x="Age_Years",bins=45,color="red",edgecolor="black",alpha=0.4,lw=2)
# plt.show()

"""
Recreate the Categorical Plot shown below:
"""
# plotdata = df.nsmallest(n=(len(df)//2),columns="AMT_INCOME_TOTAL")
# print(plotdata)

# plt.figure(figsize=(12,5),dpi=150)
# sns.boxplot(data=plotdata,y="AMT_INCOME_TOTAL",x="NAME_FAMILY_STATUS",hue="FLAG_OWN_REALTY")

# plt.legend(loc=(1.05,0.5))
# plt.show()


"""
Recreate the Heat Map shown below
"""
plt.figure(figsize=(12,8),dpi=150)
heatdata= df.drop("FLAG_MOBIL",axis=1).corr(numeric_only=True)
sns.heatmap(heatdata,cmap="viridis",annot=True)
plt.show()