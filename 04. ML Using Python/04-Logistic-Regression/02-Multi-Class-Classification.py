import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("Excel Files/iris.csv")
# print(df.head())

# sns.countplot(x="species",data=df,hue="species")
# sns.scatterplot(x="petal_length",y="petal_width",data=df,hue="species")
# sns.pairplot(data=df,hue="species")
# sns.heatmap(df.corr(numeric_only=True),annot=True)
# plt.show()

X = df.drop("species",axis=1)
y = df["species"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.multiclass import OneVsRestClassifier

# baseModel = LogisticRegression(solver="saga",max_iter=5000)
baseModel = OneVsRestClassifier(LogisticRegression(solver="saga",max_iter=5000))

penalty = ["l1","l2","elasticnet"]
l1_ratio = np.linspace(0,1,20)
C = np.logspace(0,10,20)

param_grid = {"estimator__penalty":penalty,
              "estimator__l1_ratio":l1_ratio,
              "estimator__C":C}

gridModel = GridSearchCV(baseModel,param_grid=param_grid)
gridModel.fit(X_train,y_train)

print(gridModel.best_params_)
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

