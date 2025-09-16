import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

advData = pd.read_csv("Advertising.csv")

X = advData.drop("sales",axis=1)
y = advData["sales"]

from sklearn.preprocessing import PolynomialFeatures

featureConverter = PolynomialFeatures(degree=2,include_bias=False)
Xn = featureConverter.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(Xn,y,test_size=0.3,random_state=101)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,y_train)
testPredictedSales = model.predict(X_test)

testPredictedSales= model.predict(X_test) # Predicting Sales for the Test Data

from sklearn.metrics import mean_absolute_error,mean_squared_error
MAE = mean_absolute_error(y_test,testPredictedSales)
MSE = mean_squared_error(y_test,testPredictedSales)
RMSE = np.sqrt(MSE)
print(advData["sales"].mean())
print(MAE)
print(MSE)
print(RMSE)

"""
How to choose Degree??
> Create the different Order Polynomial
> split polynomial feature into train/test
> fit on train
> Store RMSE for both Train and Test
> Plot Results (Error vs Polynomial Order/ Model Complexity)
"""

trainRMSE = []
testRMSE = []

for deg in range(1,10):
    featConv = PolynomialFeatures(degree=deg,include_bias=False)
    polyFeat= featConv.fit_transform(X)
    X_train,X_test,y_train,y_test = train_test_split(polyFeat,y,test_size=0.3,random_state=101)
    model = LinearRegression()
    model.fit(X_train,y_train)

    trainPred = model.predict(X_train)
    testPred = model.predict(X_test)

    trRMSE = np.sqrt(mean_squared_error(y_train,trainPred))
    tsRMSE = np.sqrt(mean_squared_error(y_test,testPred))

    trainRMSE.append(trRMSE)
    testRMSE.append(tsRMSE)

print(trainRMSE)
print(testRMSE)

plt.plot(range(1,6),trainRMSE[:5],label="Train RMSE")
plt.plot(range(1,6),testRMSE[:5],label="Test RMSE")

plt.legend()
plt.xlabel("Model Complexity")
plt.ylabel("Errors")
plt.show()