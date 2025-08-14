import pandas as pd
import numpy as np


stocks = ["ICICI,SBI,PNB","TCS,INFOS,HCL"]

tickers= pd.Series(stocks)
print(tickers)
print(tickers.str.split(",").str[0])
print(tickers.str.split(",",expand=True))

messy_names= pd.Series(["satheesh ","ch:etan","  anchal  "])
print(messy_names)

print(messy_names.str.replace(":",""))
print(messy_names.str.replace(":","").str.strip())
print(messy_names.str.replace(":","").str.strip().str.capitalize())

def cleanup(name:str):
    name = name.replace(":","")
    name = name.strip()
    name = name.capitalize()
    return name

associate_names= pd.Series(["satheesh ","ch:etan","  anchal  "])
associate_names = associate_names.apply(cleanup)
print(associate_names)

employee_names= pd.Series(["satheesh ","ch:etan","  anchal  "])
employee_names = pd.Series(np.vectorize(cleanup)(employee_names))
print(employee_names)
