import pandas as pd,numpy as np, seaborn as sns,matplotlib.pyplot as plt


def createAges(mu=50,sigma=13,numSamples=100,seed=42):
    np.random.seed(seed)
    sampleAges = np.random.normal(loc=mu,scale=sigma,size=numSamples)
    sampleAges = np.round(sampleAges,decimals=0)

    return sampleAges

sample = createAges()

# print(sample)

# sns.displot(sample,bins=20)
# sns.boxplot(sample)
# plt.show()

sampleSeries = pd.Series(sample)

q1,q3 = np.percentile(sampleSeries,[25,75])
iqr = q3 - q1
lowerLimit = q1 - (1.5*iqr)
upperLimit = q3 + (1.5*iqr)
# print(lowerLimit)
# print(upperLimit)

sampleSeries = sampleSeries[(sampleSeries>lowerLimit) & (sampleSeries<upperLimit)]
# print(sampleSeries)

df = pd.read_csv("./EXCEL FILES/Ames_Housing_Data.csv")

# print(df.corr(numeric_only=True)["SalePrice"].sort_values())

# sns.scatterplot(x="Overall Qual",y="SalePrice",data=df)
# sns.scatterplot(x="Gr Liv Area",y="SalePrice",data=df,color="red")
# plt.show()

# print(df[(df["Overall Qual"]>8)& (df["SalePrice"]<200000)])
# print(df[(df["Gr Liv Area"]>4000)& (df["SalePrice"]<400000)])

dropIndex = df[(df["Gr Liv Area"]>4000)& (df["SalePrice"]<400000)].index
df = df.drop(dropIndex,axis=0)
# sns.scatterplot(x="Gr Liv Area",y="SalePrice",data=df,color="green")
# plt.show()

df.to_csv("./Excel Files/Ames_FE_OutlierRemoved.csv",index=False)