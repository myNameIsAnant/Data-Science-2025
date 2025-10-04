import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Excel Files/penguins_size.csv")
df = df.dropna()

df.at[336,"sex"] = "FEMALE"
df["sex"].unique()

X = pd.get_dummies(df.drop("species",axis=1),drop_first=True)
y = df["species"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.ensemble import RandomForestClassifier
baseModel = RandomForestClassifier(n_estimators=10,
                                   max_features="sqrt",
                                   random_state=101)

baseModel.fit(X_train,y_train)
yPredictions = baseModel.predict(X_test)
from sklearn.metrics import confusion_matrix,classification_report,ConfusionMatrixDisplay
ConfusionMatrixDisplay(confusion_matrix(y_test,yPredictions),display_labels=y.unique()).plot()
plt.show()
print(classification_report(y_test,yPredictions))
