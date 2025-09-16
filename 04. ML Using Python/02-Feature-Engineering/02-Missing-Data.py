import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt


df = pd.read_csv("./Excel Files/Ames_FE_OutlierRemoved.csv")
df.drop("PID",axis=1)

def percentMissingData(df):
    percentNullData = df.isnull().sum() * 100 /len(df)
    percentNullData = percentNullData[percentNullData>0].sort_values()
    return percentNullData

percentNullData = percentMissingData(df)

# plt.figure(figsize=(8,4),dpi=150)
# sns.barplot(x=percentNullData.index,y=percentNullData,hue=percentNullData.index,legend=False)
# plt.xticks(rotation=90)
# plt.ylim(0,1)
# plt.show()

df = df.dropna(axis=0,subset=["Electrical","Garage Cars"])

#Bsmt Numeric Values
basementNumeric = ["BsmtFin SF 1","BsmtFin SF 2","Bsmt Unf SF","Total Bsmt SF","Bsmt Half Bath","Bsmt Full Bath"]
df[basementNumeric] = df[basementNumeric].fillna(0)

#Bsmt String Values
basementString = ["Bsmt Qual","Bsmt Cond","Bsmt Exposure","BsmtFin Type 1","BsmtFin Type 2"]
df[basementString] = df[basementString].fillna("None")

# percentNullData = percentMissingData(df)

# plt.figure(figsize=(8,4),dpi=150)
# sns.barplot(x=percentNullData.index,y=percentNullData,hue=percentNullData.index,legend=False)
# plt.xticks(rotation=90)
# plt.ylim(0,1)
# plt.tight_layout()
# plt.show()

df["Mas Vnr Type"] = df["Mas Vnr Type"].fillna("None")
df["Mas Vnr Area"] = df["Mas Vnr Area"].fillna(0)

# percentNullData = percentMissingData(df)

# percentNullData = percentMissingData(df)
# plt.figure(figsize=(8,4),dpi=150)
# sns.barplot(x=percentNullData.index,y=percentNullData,hue=percentNullData.index,legend=False)
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

# Garage Numeric Columns
df["Garage Yr Blt"] = df["Garage Yr Blt"].fillna(0)

# Garage String Columns
garageString = ["Garage Type","Garage Finish","Garage Qual","Garage Cond"]
df[garageString]= df[garageString].fillna("None")


# percentNullData = percentMissingData(df)
# plt.figure(figsize=(8,4),dpi=150)
# sns.barplot(x=percentNullData.index,y=percentNullData,hue=percentNullData.index,legend=False)
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

df = df.drop(["Pool QC","Misc Feature","Alley","Fence"],axis=1)

df["Fireplace Qu"] = df["Fireplace Qu"].fillna("None") 

# percentNullData = percentMissingData(df)
# plt.figure(figsize=(8,4),dpi=150)
# sns.barplot(x=percentNullData.index,y=percentNullData,hue=percentNullData.index,legend=False)
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

df["Lot Frontage"] = df.groupby("Neighborhood")["Lot Frontage"].transform(lambda value: value.fillna(value.mean()))

df["Lot Frontage"] = df["Lot Frontage"].fillna(0)

df.to_csv("./Excel Files/Ames_Missing_Data_Cleaned.csv")