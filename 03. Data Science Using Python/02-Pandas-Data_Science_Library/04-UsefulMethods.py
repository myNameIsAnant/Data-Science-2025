import pandas as pd
import numpy as np

tipsdata = pd.read_csv("./Excel Files/tips.csv")
# tipsdata["MaskedCard"] = tipsdata["CC Number"] % 10000
# print(tipsdata.head())

### Apply Function on Single Column
 
def maskCreditCard(num):
    return "*"*(len(str(num))-4) + str(num)[-4:]

tipsdata["MaskedCard"] = tipsdata["CC Number"].apply(maskCreditCard)
print(tipsdata)

def expCheck(price):
    if price < 10:
        return "$"
    elif price >= 10 and price <30:
        return "$$"
    else:
        return "$$$"

tipsdata["Spend Check"] = tipsdata["total_bill"].apply(expCheck)
print(tipsdata)


### Apply Function on Multiple Column

def quality(total_bill,tip):
    if tip/total_bill > 0.25:
        return "Generous"
    else:
        return "Other"

tipsdata["tipquality"] = tipsdata[["total_bill","tip"]].apply(lambda tipsdata: quality(tipsdata["total_bill"],tipsdata["tip"]),axis=1)
print(tipsdata)

tipsdata["quality"] = np.vectorize(quality)(tipsdata["total_bill"],tipsdata["tip"]) ## Runs Faster
print(tipsdata)





### Describing and Sorting

tipsdata = pd.read_csv("./Excel Files/tips.csv")

print(tipsdata.describe()) ## To get Stats of all numeric columns in dataframe
print(tipsdata.transpose()) ## To transpose the data
tipsdata = tipsdata.sort_values("total_bill",ascending=False)
print(tipsdata)
print(tipsdata["total_bill"].max()) # Returns Maximum Value
print(tipsdata["total_bill"].min()) # Returns Minimum Value
print(tipsdata["total_bill"].idxmax()) # Returns Location of Maximum Value
print(tipsdata["total_bill"].idxmin()) # Returns Location of Minimum Value
print(tipsdata.corr(numeric_only=True)) ## Shows Correlations

print(tipsdata["sex"].value_counts()) ## Shows Counts of Categorical Values
print(tipsdata["smoker"].value_counts()) ## Shows Counts of Categorical Values
print(tipsdata["day"].value_counts()) ## Shows Counts of Categorical Values
print(tipsdata[["sex","smoker"]].value_counts()) ## Shows Counts of Categorical Values

print(tipsdata["day"].unique()) ## Shows Unique Values in a column
print(tipsdata["day"].nunique()) ## Shows Count of Unique Values in a column


## Replacing Values

# Using Replace
print(tipsdata["sex"].replace("Female","F"))
print(tipsdata["sex"].replace(["Female","Male"],["F","M"]))

# Using Map
mymap = {"Female":"F","Male":"M"}
print(tipsdata["sex"].map(mymap))


### Dealing with Duplicate Values
df = pd.DataFrame([[1,2],[2,1],[2,3],[2,3],[3,4]],index=["A","B","C","D","E"],columns=["Values","Reports"])
print(df)

print(df.duplicated())
print(df.drop_duplicates())

print(tipsdata[tipsdata["total_bill"].between(10,20,inclusive="both")])

print(tipsdata.nlargest(5,"tip")) # Grab n largest values based on column
print(tipsdata.nsmallest(5,"tip")) # Grab n smallest values based on column

print(tipsdata.sample(5))
print(tipsdata.sample(frac=0.1))