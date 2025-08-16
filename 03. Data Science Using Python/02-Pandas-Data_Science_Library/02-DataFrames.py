import numpy as np
import pandas as pd

np.random.seed(101)
data = np.random.randint(0,101,(4,3))
# print("My Data for Panda's Dataframe is:\n",data)
myindex = ["CA","NY","AZ","TX"]
mycols = ["Jan","Feb","Mar"]
df = pd.DataFrame(data,myindex,mycols)
print("My First Pandas Python Dataframe:\n",df)

### Reading from CSV File ###

tipsdata = pd.read_csv("tips.csv")
# print("My First Pandas Python Dataframe through csv files:\n",tipsdata)

### Get the Column Names
print("Column Names in Tips File are :",tipsdata.columns)

### Get the Index Names
print("Column Names in Tips File are :",tipsdata.index)

### Get First n Rows
print("Set of First n rows :",tipsdata.head()) ## by Default 5

### Get Last n Rows
print("Set of First n rows :",tipsdata.tail()) ## by Default 5

### Get info of Data Frame
print(tipsdata.info())

### Get Stats info of Numerical Columns of Data Frame
print(tipsdata.describe())

### Transpose Data
print(tipsdata.describe().transpose())

### Working On Columns ###

# Getting Single Column
print(tipsdata["total_bill"])


# Getting Multiple Column
colstofetch = ["total_bill","tip"]
print(tipsdata[colstofetch].head())

# Creating New Column
tipsdata["tippercent"] = np.round((tipsdata["tip"]/tipsdata["total_bill"])*100,2)
print(tipsdata.head())

# Dropping a Column
print(tipsdata.drop("tippercent",axis=1).head()) ## By Default Inplace = false
tipsdatanew = tipsdata.drop("tippercent",axis=1)
print(tipsdatanew.head())

### Working On Rows ###
tipsdata = tipsdata.drop("tippercent",axis=1)
print(tipsdata.head())
print(tipsdata.index)
print(tipsdata)

# Setting Index
tipsdata = tipsdata.set_index("Payment ID") ## To Set Index to Particular Column it 
                                 ## must contain Unique Values i.e should be a primary key
print(tipsdata)

tipsdata = tipsdata.reset_index()
print(tipsdata)

tipsdata = tipsdata.set_index("Payment ID")
print(tipsdata)

# Grab Rows from Data Frame
print(tipsdata.iloc[0])  # If we want to locate using Numeric Index
print(tipsdata.loc["Sun2959"])  # If we want to locate using Labeled Index

# Grabing Multiple Rows
print(tipsdata.iloc[0:5]) # Using Slicing in Numeric Index
print(tipsdata.iloc[[0,3]]) # Using List of Numeric Index
print(tipsdata.loc[["Sun2959","Sun5260"]]) # Providing List for Labeled Index
rowstofetch = ["Sun2959","Sun5260"]
print(tipsdata.loc[rowstofetch]) # Providing variable

# Removing Rows
print(tipsdata.drop("Sun2959"))
# print(tipsdata.drop(0)) # Not Possible if we have labeled Index in DataFrame