import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Excel Files/rock_density_xray.csv")
df.columns = ["Signal","Density"]

sns.scatterplot(x="Signal",y="Density",data=df)
plt.show()

X = df["Signal"].values.reshape(-1,1)
y= df["Density"]

# LINEAR REGRESSION
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=101)

from sklearn.linear_model import LinearRegression
linModel = LinearRegression()
linModel.fit(X_train,y_train)

linPredictions = linModel.predict(X_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error

MAE = mean_absolute_error(y_test,linPredictions)
MSE = mean_squared_error(y_test,linPredictions)
RMSE = root_mean_squared_error(y_test,linPredictions)
print(MAE)
print(RMSE)

sigRange = np.arange(1,100)
sigPredictions = linModel.predict(sigRange.reshape(-1,1))
plt.figure(figsize=(12,8),dpi=150)
sns.scatterplot(x="Signal",y="Density",data=df)
plt.plot(sigPredictions,color="orange")
plt.show()

def runModel (model,X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test):
    model.fit(X_train,y_train)
    modelPredictions = model.predict(X_test)
    RMSE = root_mean_squared_error(y_test,modelPredictions)
    MAE = mean_absolute_error(y_test,modelPredictions)
    print(f"MAE:{MAE}")
    print(f"RMSE:{RMSE}")
    sigRange= np.arange(101)
    fitLine = model.predict(sigRange.reshape(-1,1))
    
    plt.figure(figsize=(12,8),dpi=150)
    sns.scatterplot(x="Signal",y="Density",data=df)
    plt.plot(fitLine,color="orange")
    plt.show()


model = LinearRegression()
runModel(model)

# POLYNOMIAL REGRESSION

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
pipe = make_pipeline(PolynomialFeatures(degree=6),LinearRegression())
runModel(pipe)

# KNN Regression
from sklearn.neighbors import KNeighborsRegressor
kValues = [1,5,10]

for n in kValues:
    knnModel = KNeighborsRegressor(n_neighbors=n)
    runModel(knnModel)

# Decision Tree Regression

from sklearn.tree import DecisionTreeRegressor
decisionModel = DecisionTreeRegressor()
runModel(decisionModel)

# Support Vector Regression

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR

svrModel = SVR()
paramGrid = {"C":[0.01,0.1,1,5,10,100,1000],
             "gamma":["auto","scale"]}
gridModel = GridSearchCV(svrModel,paramGrid)
runModel(gridModel)

# Random Forest Regression

from sklearn.ensemble import RandomForestRegressor

randonForestModel = RandomForestRegressor(n_estimators=10)
runModel(randonForestModel)

# Gradient Boosting Method
from sklearn.ensemble import GradientBoostingRegressor,AdaBoostRegressor

gbModel = GradientBoostingRegressor()
runModel(gbModel)

gbModel = AdaBoostRegressor()
runModel(gbModel)
