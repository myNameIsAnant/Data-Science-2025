import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Advertising.csv")

X = df.drop("sales",axis=1)
y= df["sales"]

from sklearn.model_selection import train_test_split
X_train,X_other,y_train,y_other = train_test_split(X,y,test_size=0.3,random_state=101)
X_eval,X_test,y_eval,y_test = train_test_split(X_other,y_other,test_size=0.5,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_eval = scaler.transform(X_eval)
X_test = scaler.transform(X_test)

from sklearn.linear_model import Ridge
baseModel = Ridge(alpha=100)
baseModel.fit(X_train,y_train)
yPredicted = baseModel.predict(X_eval)

from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_eval,yPredicted)
MSE = np.round(MSE,3)
print(MSE)


adaptModel = Ridge(alpha=1)
adaptModel.fit(X_train,y_train)
yPredicted = adaptModel.predict(X_test)
MSE = mean_squared_error(y_test,yPredicted)
MSE = np.round(MSE,3)
print(MSE)
