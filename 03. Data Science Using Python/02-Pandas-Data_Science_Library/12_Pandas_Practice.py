import pandas as pd
import numpy as np

hotels = pd.read_csv("./Excel Files/hotel_booking_data.csv")
print(hotels.head())

## Count Number of Rows/Observations in Hotel Datframe
print(len(hotels))

## Is Their Null Data if Yes Which Column has Mst Missing data
print("Most Missing Vaues are in Column :",hotels.isnull().sum().idxmax())

## Drop Company
print(hotels.drop("company",axis=1).head())

## Top 5 Most repeated Codes
print(hotels["country"].value_counts()[:5])

## Print Name of The Person Having Highest ADR
print(hotels["name"][hotels["adr"] == hotels["adr"].max()])

## Average of ADR across All Hotels
print(np.round(hotels["adr"].mean(),2))

## Average Number of Stay Days
hotels['staydays'] = hotels['stays_in_week_nights'] + hotels['stays_in_weekend_nights']

print(np.round(hotels['staydays'].mean(),2))

"""
What is the average total cost for a stay in the dataset? Not average daily cost, but total stay cost. 
(You will need to calculate total cost your self by using ADR and week day and weeknight stays). 
Feel free to round this to 2 decimal points.
"""

hotels['totcost'] = hotels['staydays'] * hotels['adr']
print(np.round(hotels['totcost'].mean(),2))

## What are the names and emails of people who made exactly 5 "Special Requests"?
print(hotels[hotels["total_of_special_requests"] == 5][["name","email"]])


## What percentage of hotel stays were classified as "repeat guests"? 
# (Do not base this off the name of the person, but instead of the is_repeated_guest column)
rep_guest = len(hotels[hotels["is_repeated_guest"] == True])
print(np.round(100 * (rep_guest/len(hotels)),2))


"""
What are the top 5 most common last name in the dataset? 
Bonus: Can you figure this out in one line of pandas code? 
(For simplicity treat the a title such as MD as a last name, 
for example Caroline Conley MD can be said to have the last name MD)
"""
def last_name(name):
    return name.split()[1]

print(hotels["name"].apply(last_name).value_counts()[:5]) 

# print(hotels["name"].apply(lambda name: name.split()[-1]).value_counts()[:5])


"""
What are the names of the people who had booked the most number children and babies for their stay? 
(Don't worry if they canceled, only consider number of people reported at the time of their reservation)
"""

hotels["totkids"] = hotels["children"] + hotels["babies"]
print(hotels.sort_values("totkids",ascending=False)[["name","adults","totkids","babies","children"]][:3])


"""
What are the top 3 most common area code in the phone numbers? (Area code is first 3 digits)
"""
# print(hotels["phone-number"].dtype)

def areaCode(phonenumber):
    return str(phonenumber)[:3]

print(hotels["phone-number"].apply(areaCode).value_counts()[:3])

"""
How many arrivals took place 
between the 1st and the 15th of the month (inclusive of 1 and 15) ? 
Bonus: Can you do this in one line of pandas code?
"""
print(len(hotels[hotels["arrival_date_day_of_month"].between(1,15,inclusive="both") == True]))

"""
Create a table for counts for each day of the week that people arrived. 
(E.g. 5000 arrivals were on a Monday, 3000 were on a Tuesday, etc..)
"""
from datetime import datetime

def getDate(day,month,year):
    return f"{day}-{month}-{year}"

hotels["DATE"] = np.vectorize(getDate)(hotels['arrival_date_day_of_month'],hotels['arrival_date_month'],hotels['arrival_date_year'])

hotels["DATE"] = pd.to_datetime(hotels["DATE"])

hotels["WEEKDAY"] = hotels["DATE"].dt.day_name()

print(hotels["WEEKDAY"].value_counts())