import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("./Excel Files/StudentsPerformance.csv")

### CAT PLOT ###

sns.catplot(data=df,x="gender",y="math score",kind="violin",hue="gender",row="lunch",col="test preparation course")


### Pair Grid ###

g = sns.PairGrid(df,hue="gender")
g = g.map_upper(sns.scatterplot)
g = g.map_lower(sns.kdeplot)
g = g.map_diag(sns.kdeplot)
g = g.add_legend()
plt.show()