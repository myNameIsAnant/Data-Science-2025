import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns


## Heat Map
"""
df = pd.read_csv("./Excel Files/country_table.csv")
df = df.set_index("Countries")
print(df)
sns.heatmap(df.drop("Life expectancy",axis=1),lw=0.5,annot=True,cmap="viridis")
plt.savefig("MyHeatMap.jpg",bbox_inches="tight")
# plt.show()
"""

df = pd.read_csv("./Excel Files/country_table.csv")
df = df.set_index("Countries")
print(df)
sns.clustermap(df.drop("Life expectancy",axis=1),lw=0.5,annot=True,cmap="viridis",col_cluster=False)
plt.savefig("MyClusterMap.jpg",bbox_inches="tight")
# plt.show()