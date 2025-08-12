import numpy as np
import pandas as pd

numpy_series = np.arange(1,11)

my_index = ["USA","Canada","Mexico"]
my_data = [1776,1867,1821]

new_series = pd.Series(data=my_data)
print("My First Panda Series:\n",new_series)

labeled_series = pd.Series(data=my_data,index = my_index)
print("My First Labeled Panda Series:\n",labeled_series)

## Now We can Fetch Values with Both Label and Index
print(labeled_series[0]) 
print(labeled_series["USA"])


## Creating Series from Dictionary

ages = {"Anant":24,"Chetan":22,"Satheesh":27}
ages_series = pd.Series(ages)
print("My First Panda Series from dictionary:\n",ages_series)
print(ages_series["Satheesh"])

# Imaginary Sales Data for 1st and 2nd Quarters for Global Company
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}

q1_sales = pd.Series(q1)
q2_sales = pd.Series(q2)

print("Index in q1_sales are :",q1_sales.keys()) ### Return Index In the Series

print("Applying Factor in q1_sales:\n",q1_sales*1.2) ### Return Index In the Series


### What Happens when we add these series (As we have Difference of Japana and Brazil)
print("First Half Sales for the Year are:\n",q1_sales+q2_sales) ### Return Index In the Series

### To Avoid this we will use Add
print("Correct First Half Sales for the Year are:\n",q1_sales.add(q2_sales,fill_value=0)) ### Return Index In the Series



