import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("./Excel Files/Ames_Final.csv")

X= df.drop("SalePrice",axis=1)
y=df["SalePrice"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import ElasticNet
baseModel = ElasticNet(max_iter=10 ** 6)

parameterGrid = {"alpha":[0.1,1,5,10,100],
                 "l1_ratio":[0.1,0.7,0.99,1]}

from sklearn.model_selection import GridSearchCV
gridModel = GridSearchCV(estimator=baseModel,
                         param_grid=parameterGrid,
                         scoring="neg_mean_squared_error",
                         cv=5,verbose=1)

gridModel.fit(X_train,y_train)
print(gridModel.best_params_)
yPredicted = gridModel.predict(X_test)

from sklearn.metrics import mean_absolute_error,root_mean_squared_error
MAE = mean_absolute_error(y_test,yPredicted)
RMSE= root_mean_squared_error(y_test,yPredicted)
MSE = np.round(MAE,3)
RMSE = np.round(RMSE,3)
print(MSE)
print(RMSE)