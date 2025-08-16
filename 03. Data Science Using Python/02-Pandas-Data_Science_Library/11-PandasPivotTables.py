import pandas as pd

df = pd.read_csv("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\Sales_Funnel_CRM.csv")
print(df)
licenses = df[["Company","Product","Licenses"]]
print(licenses)
check = pd.pivot(data=licenses,index="Company",columns="Product",values="Licenses")
print(check)
check1 = pd.pivot_table(df,index="Company",aggfunc="sum",values=["Licenses","Sale Price"])
print(check1)

pivot3 = pd.pivot_table(df,index=["Account Manager","Contact"],values="Sale Price",columns="Product",aggfunc="sum",fill_value=0)
print(pivot3)

pivot4 = pd.pivot_table(df,index=["Account Manager","Contact","Product"],values="Sale Price",aggfunc="sum",fill_value=0)
print(pivot4)