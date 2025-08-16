import pandas as pd
import numpy as np

import os

d = os.getcwd()
print(d)

### Reading from CSV Files:


ex = pd.read_csv("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\example.csv")
print(ex)

### Reading From Excel Files
import openpyxl
import xlrd

df = pd.read_excel("C:\\Users\\anant\\OneDrive\\Desktop\\Data Science\\03. Data Science Using Python\\Pandas-Data_Science_Library\\my_excel_file.xlsx",sheet_name="First_Sheet")
print(df)
df.to_excel("check.xlsx",sheet_name="ABCD",index=False)

### Reading from HTML Tables

import xml

url = "https://en.wikipedia.org/wiki/World_population"
tables = pd.read_html(url)
mostpop_countries = tables[3]
cols = ["Country / Dependency","Population","% of world"]

mostpop_countries = mostpop_countries.drop(['Date','Source (official or from the United Nations)'],axis=1)
print(mostpop_countries)


### Reading From SQL Databases
