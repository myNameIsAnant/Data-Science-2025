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

from sklearn.linear_model import ElasticNet
baseModel = ElasticNet()
parameterGrid = {"alpha":[0.1,1,5,10,50,100],
                 "l1_ratio":[0.1,0.5,0.7,0.95,0.99,1]}

from sklearn.model_selection import GridSearchCV
gridModel = GridSearchCV(estimator=baseModel,
                         param_grid=parameterGrid,
                         scoring="neg_mean_squared_error",
                         cv=5,verbose=1)

gridModel.fit(X_train,y_train)


gridModelResults = pd.DataFrame(gridModel.cv_results_)
# print(gridModelResults)

yPredicted = gridModel.predict(X_test)

from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_test,yPredicted)
MSE = np.round(MSE,3)
print(MSE)