import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

advData = pd.read_csv("Advertising.csv")

X = advData.drop("sales",axis=1)
y = advData["sales"]

from sklearn.model_selection import train_test_split

"""
Breaking Data into Train Test Split to check model Accuracy
"""
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.linear_model import LinearRegression

model = LinearRegression() # Assigning Linear Regression Algo

model.fit(X_train,y_train) # Training Model on Test Data

testPredictedSales= model.predict(X_test) # Predicting Sales for the Test Data

from sklearn.metrics import mean_absolute_error,mean_squared_error

MAE = mean_absolute_error(y_test,testPredictedSales)
MSE = mean_squared_error(y_test,testPredictedSales)
RMSE = np.sqrt(MSE)

print(advData["sales"].mean())
print(MAE)
print(MSE)
print(RMSE)

residuals = y_test - testPredictedSales
predS = model.predict(X)

"""
fig, ax = plt.subplots(nrows=3,ncols=1,figsize=(6,16),dpi=150)
ax[0].plot(advData["TV"],advData["sales"],"o")
ax[0].plot(advData["TV"],predS,"o",color="orange")
ax[0].set_ylabel("Sales")
ax[0].set_xlabel("TV")
ax[1].plot(advData["radio"],advData["sales"],"o")
ax[1].plot(advData["radio"],predS,"o",color="orange")
ax[1].set_ylabel("Sales")
ax[1].set_xlabel("radio")
ax[2].plot(advData["newspaper"],advData["sales"],"o")
ax[2].plot(advData["newspaper"],predS,"o",color="orange")
ax[2].set_ylabel("Sales")
ax[2].set_xlabel("TV")
plt.tight_layout()
plt.show() # This Scatter plot compares the predicted sales and the actual points
"""

"""
sns.pairplot(advData)
plt.show() # It plots the data into the chart
"""

"""
sns.scatterplot(x=y_test,y=residuals,color="orange")
plt.axhline(y=0,color="blue",ls="--")
plt.show() # This is residual plot to make sure it is not a line or a curve
"""

"""
import scipy as sp
fig, ax = plt.subplots(figsize=(6,8),dpi=150)
_ = sp.stats.probplot(residuals,plot=ax)
plt.show() 
"""
