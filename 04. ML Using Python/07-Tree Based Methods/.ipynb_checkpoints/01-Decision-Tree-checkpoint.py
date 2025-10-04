import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt

df = pd.read_csv("./Excel Files/hearing_test.csv")
# print(df.describe())

# sns.countplot(data=df,x="test_result",hue="test_result",legend=False)
# plt.show()

# plt.figure(dpi=150)
# sns.boxplot(data=df,x="test_result",y="age",hue="test_result",legend=False)
# plt.show()

# sns.scatterplot(x="age",y="physical_score",data=df,hue="test_result")
# plt.show()

# sns.scatterplot(x="test_result",y="physical_score",data=df,hue="test_result")
# plt.show()

# sns.heatmap(df.corr(),annot=True)
# plt.show()

# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure(dpi=150)
# ax = fig.add_subplot(111,projection="3d")
# ax.scatter(data=df,xs="age",ys="physical_score",zs="test_result",c="test_result")
# plt.show()

X = df.drop("test_result",axis=1)
y = df["test_result"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
baseModel = LogisticRegression()
baseModel.fit(X_train,y_train)


print(baseModel.coef_)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay

yPredicted = baseModel.predict(X_test)

accuracy = accuracy_score(y_test,yPredicted)
print(accuracy)

# cm = confusion_matrix(y_test,yPredicted)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm)
# disp.plot()
# plt.show()

print(classification_report(y_test,yPredicted))

from sklearn.metrics import precision_score,recall_score,f1_score

p = precision_score(y_test,yPredicted)
r = recall_score(y_test,yPredicted)
f = f1_score(y_test,yPredicted)

print(p)
print(r)
print(f)

from sklearn.metrics import PrecisionRecallDisplay,RocCurveDisplay,precision_recall_curve,roc_curve,roc_auc_score
yScores = baseModel.predict_proba(X_test)[:,1]
p ,r ,_ =precision_recall_curve(y_test,yScores)
f,t,_ = roc_curve(y_test,yScores)
a = roc_auc_score(y_test,yScores)
k = RocCurveDisplay(fpr=f,tpr=t)
d = PrecisionRecallDisplay(precision=p,recall=r)
d.plot(label=round(a,2))
plt.show()