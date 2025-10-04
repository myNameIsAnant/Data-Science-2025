import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Excel Files/mushrooms.csv")

X= pd.get_dummies(df.drop("class",axis=1),drop_first=True)
y = df["class"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.15,random_state=101)

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

paramGrid = {"n_estimators":[50,100],
             "learning_rate":[0.1,0.05,0.2],
             "max_depth":[3,4,5]}

gbModel = GradientBoostingClassifier()
gridModel = GridSearchCV(gbModel,paramGrid)
gridModel.fit(X_train,y_train)

from sklearn.metrics import confusion_matrix,classification_report,ConfusionMatrixDisplay,accuracy_score
yPredictions = gridModel.predict(X_test)
ConfusionMatrixDisplay(confusion_matrix(y_test,yPredictions),display_labels=y.unique()).plot(cmap="viridis")
plt.show()
print(classification_report(y_test,yPredictions))

featImp = pd.DataFrame({"Features":X.columns,"Importance":gridModel.best_estimator_.feature_importances_})
featImp = featImp.sort_values(by="Importance")
featImp = featImp[featImp["Importance"]>0.0005]

plt.figure(figsize=(14,6),dpi=200)
sns.barplot(x="Features",y="Importance",data=featImp,hue="Features",palette="rainbow")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


