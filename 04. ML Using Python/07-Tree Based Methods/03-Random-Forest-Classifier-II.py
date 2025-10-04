import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Excel Files/data_banknote_authentication.csv")

X = df.drop("Class",axis=1)
y = df["Class"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.15,random_state=101)

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
baseModel = RandomForestClassifier()
paramGrid = {"max_features":[2,3,4],"n_estimators":[64,100,128,200],"bootstrap":[True,False],"oob_score":[True,False]}
gridModel = GridSearchCV(baseModel,paramGrid)
gridModel.fit(X_train,y_train)

print(gridModel.best_params_)

myModel = RandomForestClassifier(max_features=2,n_estimators=200,oob_score=True)
myModel.fit(X_train,y_train)
yPredictions = myModel.predict(X_test)

print(myModel.oob_score_)

from sklearn.metrics import ConfusionMatrixDisplay,classification_report,confusion_matrix

ConfusionMatrixDisplay(confusion_matrix(y_test,yPredictions)).plot(cmap="viridis")
plt.show()

print(classification_report(y_test,yPredictions))

errors = []
misClass = []
from sklearn.metrics import accuracy_score
for n in range(1,200):
    r = RandomForestClassifier(n_estimators=n,max_features=2)
    r.fit(X_train,y_train)
    p = r.predict(X_test)
    err = 1 - accuracy_score(y_test,p)
    errors.append(err)
    n_missed = np.sum(p != y_test)
    misClass.append(n_missed)

plt.plot(range(1,200),errors)
plt.show()

plt.plot(range(1,200),misClass)
plt.show()
