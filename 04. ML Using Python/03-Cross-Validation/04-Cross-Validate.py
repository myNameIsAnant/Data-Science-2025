import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Advertising.csv")

X = df.drop("sales",axis=1)
y= df["sales"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import Ridge
baseModel = Ridge(alpha=1)

from sklearn.model_selection import cross_validate
scores = cross_validate(baseModel,X_train,y_train,
                        cv=10,
                        scoring=["neg_mean_squared_error","neg_mean_absolute_error"])

baseModel.fit(X_train,y_train)
yPredicted = baseModel.predict(X_test)

from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_test,yPredicted)
MSE = np.round(MSE,3)
print(MSE)