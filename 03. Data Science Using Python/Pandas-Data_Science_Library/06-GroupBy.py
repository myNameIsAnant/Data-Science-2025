import pandas as pd
import numpy as np

cols = ["Category","Data Value"]
mydata = [["A",10],["A",5],["B",2],["B",4],["C",12],["C",6]]
df_new = pd.DataFrame(data=mydata,columns=cols)
print(df_new)

mpgdata = pd.read_csv("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\mpg.csv")
print(mpgdata.info())

# Grouping by  1 Columns
print(np.round(mpgdata.groupby("model_year").mean(numeric_only=True)["mpg"],2))

# Grouping by more Than 1 Columns
print(np.round(mpgdata.groupby(["model_year","cylinders"]).mean(numeric_only=True)["mpg"],2))


year_cyl = np.round(mpgdata.groupby(["model_year","cylinders"]).mean(numeric_only=True),2)
print(year_cyl.loc[70])
print(year_cyl.loc[[70,82]])

print(year_cyl.loc[(70,6)])

## Using Cross Section (xs)

print(year_cyl.xs(key=70,level="model_year"))
print(year_cyl.xs(key=4,level="cylinders"))

print(year_cyl.swaplevel()) ## To Swap Levels
print(year_cyl.swaplevel().sort_index(level="model_year",ascending=False)) ## To Swap Levels


# print(mpgdata.agg("mean",numeric_only=True))
print(mpgdata.select_dtypes(include="number").agg(["std","mean"]))
print(mpgdata.agg({"mpg":["mean","std"],"weight":["max","min"]}).fillna("Not Called"))