import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("Excel Files/penguins_size.csv")
df = df.dropna()

print(df[df["species"] == "Gentoo"].groupby("sex").describe().T)

df.at[336,"sex"] = "FEMALE"

# print(df["sex"].unique())

sns.pairplot(df,hue="species")
plt.show()

sns.catplot(x="species",y="culmen_length_mm",data=df,kind="box",hue="species",col="sex")
plt.show()

X = pd.get_dummies(df.drop("species",axis=1),drop_first=True)
y= df["species"]

from sklearn.model_selection import train_test_split
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.tree import DecisionTreeClassifier
baseModel = DecisionTreeClassifier()
baseModel.fit(X_train,y_train)

yPredictions = baseModel.predict(X_test)
from sklearn.metrics import classification_report,ConfusionMatrixDisplay,confusion_matrix
print(classification_report(y_test,yPredictions))
ConfusionMatrixDisplay(confusion_matrix(y_test,yPredictions),display_labels=y.unique()).plot(cmap="viridis")
plt.show()

fi = pd.DataFrame({"Features":X.columns,"Importance":baseModel.feature_importances_}).sort_values("Importance")
print(fi)

from sklearn.tree import plot_tree
plt.figure(figsize=(12,8),dpi=150)
plot_tree(baseModel,feature_names=X.columns,filled=True)
plt.tight_layout()
plt.show()

def report_model(model):
    modelPredictions = model.predict(X_test)
    print(classification_report(y_test,modelPredictions))
    # ConfusionMatrixDisplay(confusion_matrix(y_test,yPredictions),display_labels=y.unique()).plot(cmap="viridis")
    print("\n")
    plt.figure(figsize=(12,8),dpi=150)
    plot_tree(model,feature_names=X.columns,filled=True)
    plt.tight_layout()
    plt.show()

report_model(baseModel)

prunedModel = DecisionTreeClassifier(max_depth=2)
prunedModel.fit(X_train,y_train)
report_model(prunedModel)

maxLeafModel = DecisionTreeClassifier(max_leaf_nodes=3)
maxLeafModel.fit(X_train,y_train)
report_model(maxLeafModel)


entropyModel = DecisionTreeClassifier(criterion="entropy")
entropyModel.fit(X_train,y_train)
report_model(entropyModel)

