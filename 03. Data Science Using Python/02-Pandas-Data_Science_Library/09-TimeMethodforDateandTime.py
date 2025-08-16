import pandas as pd
import numpy as np

from datetime import datetime

myyear = 2025
mymonth= 8
myday = 14
myhour = 5
mymin = 38
mysec = 49

mydate = datetime(myyear,mymonth,myday,myhour,mymin,mysec)
print(mydate)

myser = pd.Series(["Nov 3,1990","2000-01-01",None])
print(myser)

myserdate = pd.to_datetime(myser)
print(myserdate)

mydate = "08/14/2025"
mydate1 = "08-14-2025"
mydate2 = "14-08-2025"
mydate3 = "Aug 14,2025"
mydate4 = "14th of Aug 2025"


print(mydate)
print("mydate :",pd.to_datetime(mydate))
print("mydate1 :",pd.to_datetime(mydate1))
print("mydate2 :",pd.to_datetime(mydate2,dayfirst=True))
print("mydate3:",pd.to_datetime(mydate3,format="%b %d,%Y"))
print("mydate4:",pd.to_datetime(mydate4))

sales = pd.read_csv("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\RetailSales_BeerWineLiquor.csv")
print(sales["DATE"])
sales["DATE"] = pd.to_datetime(sales["DATE"])
print(sales["DATE"])
sales1 = pd.read_csv("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\RetailSales_BeerWineLiquor.csv",parse_dates=[0])
print(sales1["DATE"])
print(sales1["DATE"].dt.year)


sales1 = sales1.set_index("DATE")
print(sales1)

print(sales1.resample(rule="A").sum())
