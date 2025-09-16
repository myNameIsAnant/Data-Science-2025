import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt


df = pd.read_csv("./Excel Files/Ames_Missing_Data_Cleaned.csv")

df["MS SubClass"] = df["MS SubClass"].apply(str)

myStringDF = df.select_dtypes(include="object")
myNumericDF = df.select_dtypes(exclude="object")

stringParameterDummies = pd.get_dummies(myStringDF,drop_first=True)
finalDF = pd.concat([myNumericDF,stringParameterDummies],axis=1)

finalDF.to_csv("./Excel Files/Ames_Final.csv")