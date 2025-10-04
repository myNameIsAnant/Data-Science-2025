import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("Excel Files/wine_fraud.csv")

print(df["quality"].unique())

sns.countplot(x="quality",data=df,hue="quality",legend=False)
plt.show()

sns.countplot(x="quality",data=df,hue="type")
plt.show()

redWine = len(df[(df["type"]=="red")& (df["quality"]=="Fraud")]["type"]) / len(df[df["type"]=="red"]["type"])
print(f"Percentage of Fraud In Red Wines: {redWine * 100}")
whiteWine = len(df[(df["type"]=="white")& (df["quality"]=="Fraud")]["type"]) / len(df[df["type"]=="white"]["type"])
print(f"Percentage of Fraud In White Wines: {whiteWine * 100}")

df["Fraud"] = df["quality"].map({"Fraud":1,"Legit":0})

df.corr(numeric_only=True)["Fraud"][:-1].sort_values().plot(kind="bar")
plt.show()

sns.clustermap(df.corr(numeric_only=True),cmap="viridis")
plt.show()

df = df.drop("Fraud",axis=1)
df["type"] = pd.get_dummies(df["type"],drop_first=True)

X = df.drop("quality",axis=1)
y = df["quality"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test  =train_test_split(X,y,test_size=0.1,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.svm import SVC
baseModel = SVC(class_weight="balanced")

from sklearn.model_selection import GridSearchCV
paramGrid={"C":[0.001,0.01,0.1,0.5,1]}
gridModel = GridSearchCV(baseModel,paramGrid)
gridModel.fit(X_train,y_train)
print(gridModel.best_params_)

from sklearn.metrics import confusion_matrix,classification_report
yPredictions = gridModel.predict(X_test)
print(confusion_matrix(y_test,yPredictions))
print(classification_report(y_test,yPredictions))