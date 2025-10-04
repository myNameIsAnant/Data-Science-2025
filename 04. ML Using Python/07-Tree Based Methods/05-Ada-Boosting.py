import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Excel Files/mushrooms.csv")
print(df["class"].unique())

sns.countplot(data=df,x="class",hue="class")
plt.show()

featUnique = df.describe().T.reset_index().sort_values(by="unique")
featUnique.columns = ["Features","Count","Unique","Top","Freq"]

plt.figure(figsize=(14,6),dpi=200)
sns.barplot(x="Features",y="Unique",data=featUnique,hue="Features",palette="rainbow")
plt.xticks(rotation=90)
plt.show()

X= pd.get_dummies(df.drop("class",axis=1),drop_first=True)
y = df["class"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.15,random_state=101)

from sklearn.ensemble import AdaBoostClassifier
baseModel = AdaBoostClassifier(n_estimators=1)

baseModel.fit(X_train,y_train)
from sklearn.metrics import confusion_matrix,classification_report,ConfusionMatrixDisplay,accuracy_score
yPredictions = baseModel.predict(X_test)
ConfusionMatrixDisplay(confusion_matrix(y_test,yPredictions),display_labels=y.unique()).plot(cmap="viridis")
plt.show()
print(classification_report(y_test,yPredictions))

errorRate = []
for i in range(1,96):
    myModel = AdaBoostClassifier(n_estimators=i)
    myModel.fit(X_train,y_train)
    yPreds = myModel.predict(X_test)
    myError = 1 - accuracy_score(y_true=y_test,y_pred=yPreds)
    errorRate.append(myError)

plt.figure(figsize=(12,8),dpi=150)
plt.plot(range(1,96),errorRate)
plt.tight_layout()
plt.show()

