import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

advData = pd.read_csv("Advertising.csv")

X = advData.drop("sales",axis=1)
y = advData["sales"]

from sklearn.preprocessing import PolynomialFeatures

featureConverter = PolynomialFeatures(degree=3,include_bias=False)
Xn = featureConverter.fit_transform(X)

from sklearn.linear_model import LinearRegression

model = LinearRegression() # Assigning Linear Regression Algo
model.fit(Xn,y)

from joblib import dump,load

dump(model,"MyFirstPolynomialRegressionModel.joblib")
dump(featureConverter,"MyFirstPolynomialConverter.joblib")

newcamp = [[149,22,12]]
print(model.predict(featureConverter.fit_transform(newcamp)))