import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("./Excel Files/StudentsPerformance.csv")
print(df.head())

### Joint Plots ###
# plt.figure(figsize=(12,8),dpi=150)

"""
sns.jointplot(data=df,x="reading score",y="writing score",hue="gender")

sns.jointplot(data=df,x="reading score",y="writing score",kind="kde",fill=True)
plt.show()
"""

### Pair Plots ###
sns.pairplot(data=df,hue="gender",corner=True)
plt.show()