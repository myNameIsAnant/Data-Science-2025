import pandas as pd
import numpy as np

df = pd.read_csv("Advertising.csv")

X= df.drop("sales",axis=1)
y=df["sales"]

from sklearn.preprocessing import PolynomialFeatures
featureConverter = PolynomialFeatures(degree=3,include_bias=False)
Xn = featureConverter.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(Xn,y,test_size=0.3,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

##### Ridge Regression #####
print("--Ridge Model--")
from sklearn.linear_model import Ridge
ridgeModel = Ridge(alpha=10)
ridgeModel.fit(X_train,y_train)
salesPrediction = ridgeModel.predict(X_test)
from sklearn.metrics import mean_absolute_error,mean_squared_error
MAE = mean_absolute_error(y_test,salesPrediction)
RMSE = np.sqrt(mean_squared_error(y_test,salesPrediction))
print(f"MAE:{MAE}")
print(f"RMSE:{RMSE}")

print("--Ridge CV Model--")
from sklearn.linear_model import RidgeCV
ridgeCVModel = RidgeCV(alphas=(0.1,1,10),
                       scoring="neg_root_mean_squared_error")

# from sklearn.metrics import get_scorer_names
# print(get_scorer_names())
ridgeCVModel.fit(X_train,y_train)
salesPrediction = ridgeCVModel.predict(X_test)
MAE = mean_absolute_error(y_test,salesPrediction)
RMSE = np.sqrt(mean_squared_error(y_test,salesPrediction))
print(f"MAE:{MAE}")
print(f"RMSE:{RMSE}")

print("--Lasso CV Model--")
from sklearn.linear_model import LassoCV
lassoCVModel = LassoCV(eps=0.001,alphas=100,cv=5,max_iter=10**6)
lassoCVModel.fit(X_train,y_train)
salesPrediction = lassoCVModel.predict(X_test)
MAE = mean_absolute_error(y_test,salesPrediction)
RMSE = np.sqrt(mean_squared_error(y_test,salesPrediction))
print(f"MAE:{MAE}")
print(f"RMSE:{RMSE}")

print("--Elast Net Model--")
from sklearn.linear_model import ElasticNetCV
elastnetCVModel = ElasticNetCV(l1_ratio=[0.1,0.5,0.7,0.9,0.95,0.99,1],
                               eps=0.001,alphas=100,
                               cv=5,max_iter=10**6)
elastnetCVModel.fit(X_train,y_train)
salesPrediction = elastnetCVModel.predict(X_test)
MAE = mean_absolute_error(y_test,salesPrediction)
RMSE = np.sqrt(mean_squared_error(y_test,salesPrediction))
print(f"MAE:{MAE}")
print(f"RMSE:{RMSE}")
