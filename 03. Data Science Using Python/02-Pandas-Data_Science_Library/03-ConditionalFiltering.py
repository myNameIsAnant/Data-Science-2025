import pandas as pd
import numpy as np

### Conditional Filtering
names = ["Chetan","Nivedha","Anchal","Ashish","Shariq","Rini"]
subjects = ["Maths","Accounts","Business Studies","English","Computer Science"]
scoredata = [[86, 75, 91, 88, 86],[89, 84, 91, 86, 87],[74, 72, 78, 72, 77],[85, 85, 86, 78, 75],[85, 86, 86, 86, 80],[79, 75, 77, 75, 72]]
print(scoredata)
# df = pd.DataFrame([[1776,328,20.5],[1867,38,1.7],[1821,126,1.22]],index=["USA","Canada","Mexico"],columns=["Year","Pop","GDP"])
df = pd.DataFrame(data=scoredata,index=names,columns=subjects)
print(df)

## Filtering by Single Condition
print(df[df["Maths"]>80])

tipsdata = pd.read_csv("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\tips.csv")
bigbill = tipsdata["total_bill"] > 40
print(tipsdata[bigbill])

print(tipsdata[tipsdata["sex"] == "Male"])
print(tipsdata[tipsdata["smoker"] == "No"])
print(tipsdata[tipsdata["size"] <= 3])

## Filtering by Multiple Conditions

"""
Done in 2 Ways
Using And (&) Operator - Both the Conditions are True
Using Or (|) Operator - Either Condition is True
"""

print(tipsdata[(tipsdata["sex"] == "Female") & (tipsdata["smoker"] == "Yes")])
print(tipsdata[(tipsdata["sex"] == "Female") & (tipsdata["total_bill"] > 40)])

print(tipsdata[(tipsdata["day"] == "Sun") | (tipsdata["day"] == "Sat")])

weekend = ["Sat","Sun","Fri"]
print(tipsdata[tipsdata["day"].isin(weekend)])