import pandas as pd
import numpy as np

moviescores = pd.read_csv("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\movie_scores.csv")
print(moviescores)

def dataSetup():
    names = ["Chetan","Nivedha","Anchal","Ashish","Shariq","Rini"]
    subjects = ["Maths","Accounts","Business Studies","English","Computer Science"]
    scoredata = [[86, 75, 91, 88, 86],[89, 84, 91, np.nan, 87],[np.nan, np.nan, np.nan, np.nan, np.nan],[85, np.nan, 86, 78, 75],[85, 86, 86, 86, 80],[79, 75, 77, 75, 72]]
    df = pd.DataFrame(data=scoredata,index=names,columns=subjects)
    return df



## Checking for NA Values
df = dataSetup()
print(df)
print(df.isnull())
print(df[df["Accounts"].notnull()])
print(df[df["Accounts"].isnull()])
print(df[(df["Accounts"].isnull()) & (df["Maths"].notnull())])


## Dropping Data
df = dataSetup()
df_cleaned1 = df.dropna()
print(df_cleaned1)

df_cleaned2= df.dropna(thresh=1)
print(df_cleaned2)

df_cleaned3= df.dropna(axis=1)
print(df_cleaned3)

df_cleaned4= df.dropna(subset=["Accounts","English"])
print(df_cleaned4)

## Replacing the Values
df = dataSetup()
print(df)
df["Maths"]=df["Maths"].fillna(np.round(df["Maths"].mean(),0))
print(df)


