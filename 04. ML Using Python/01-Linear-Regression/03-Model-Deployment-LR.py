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

predSales = model.predict(X)

from joblib import dump,load

dump(model,"myFirstLinearRegressionModel.joblib")

newcamp = [[149,22,12]]
print(model.predict(newcamp))
