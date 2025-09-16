import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Manual Data

price_df = pd.DataFrame({"Area sqm":[200,190,230,180,210],
                   "Bedrooms":[3,2,3,1,2],
                   "Bathrooms":[2,1,3,1,2],
                   "Price":[500000,450000,650000,400000,550000]})

x1,x2,x3 = price_df["Area sqm"],price_df["Bedrooms"],price_df["Bathrooms"]
y = price_df["Price"]

coeff1 = np.polyfit(x1,y,deg=1) # Calculates b0 and b1 for equation y= b1x + b0
coeff2 = np.polyfit(x2,y,deg=1) # Calculates b0 and b1 for equation y= b1x + b0
coeff3 = np.polyfit(x3,y,deg=1) # Calculates b0 and b1 for equation y= b1x + b0

prod_df = pd.DataFrame({"Production Hours (x)":[34,35,39,42,43,47],
                   "Production Volume (y)":[102,109,137,148,150,158]})

X = prod_df["Production Hours (x)"]
y= prod_df["Production Volume (y)"]

coeff = np.polyfit(X,y,deg=1) # Calculates b0 and b1 for equation y= b1x + b0

planHrs = np.linspace(34,48,15)
predVolume = coeff[0]*planHrs + coeff[1]

"""
sns.scatterplot(x="Production Hours (x)",y="Production Volume (y)",data=prod_df,color="orange")
plt.plot(planHrs,predVolume,color="blue")
plt.show()
"""

"""
prod_df["Predicted Volume"] = (coeff[0] * prod_df["Production Hours (x)"]) + coeff[1]
yp = prod_df["Predicted Volume"]
fig = plt.figure(figsize=(6,15),dpi = 150)
axes1 = fig.add_axes([0.1,0.1,0.85,0.85])
axes1.scatter(X,y,color="orange")
axes1.plot(X,yp,color="blue")
plt.show()
"""

"""
Using Data
"""


advData = pd.read_csv("Advertising.csv")
advData["Total Spends"] = advData["TV"] + advData["radio"] + advData["newspaper"]
# print(advData.head())

X = advData["Total Spends"]
y = advData["sales"]
coeffData = np.polyfit(X,y,deg=1)
potentialSpends = np.linspace(0,500,100)
predSales = coeffData[0]*potentialSpends + coeffData[1]


"""
sns.scatterplot(x="Total Spends",y="sales",data=advData,color="orange")
plt.plot(potentialSpends,predSales,color="blue")
plt.show()
"""

coeffDataP = np.polyfit(X,y,deg=3)
predSalesP = coeffDataP[0]*potentialSpends**3+coeffDataP[1]*potentialSpends**2+coeffDataP[2]*potentialSpends+coeffDataP[3]


sns.scatterplot(x="Total Spends",y="sales",data=advData,color="orange")
plt.plot(potentialSpends,predSalesP,color="blue")
plt.show()