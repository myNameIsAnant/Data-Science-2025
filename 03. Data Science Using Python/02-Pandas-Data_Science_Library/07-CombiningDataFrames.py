import numpy as np
import pandas as pd

names = ["Chetan","Nivedha","Anchal","Ashish","Shariq","Rini"]
subjects = ["Name","Maths","Accounts","Business Studies","English","Computer Science"]

def dataSetup(subjects):
    scoredata = [["Chetan",86, 75, 91, 88, 86],["Nivedha",89, 84, 91, 86, 87],["Anchal",74, 72, 78, 72, 77],
                 ["Ashish",85, 85, 86, 78, 75],["Shariq",85, 86, 86, 86, 80],["Rini",79, 75, 77, 75, 72]]
    df = pd.DataFrame(data=scoredata,columns=subjects)
    return df

df = dataSetup(subjects)
print(df)
scoredata1 = [["Chetan",89],["Nivedha",96],["Anchal",91],["Ashish",94],["Shariq",90],["Rini",97]]
df1 = pd.DataFrame(data=scoredata1,columns=["Name","Economics"])
print(df1)


## Concatenating Data Frames
concatdf= pd.concat([df,df1.drop("Name",axis=1)],axis=1)
print(concatdf)

### Merging Data Frames ###

registerations= pd.DataFrame({"Student_ID":[1,2,3,4],"Name":["Satheesh","Vaibhav","Chetan","Riddhi"],"Reg_Id":[1,2,3,4]})
attendance= pd.DataFrame({"Student_ID":[5,1,6,2],"Name":["Nivedha","Satheesh","Shariq","Vaibhav"],"Log_Id":[1,2,3,4]})
print(registerations)
print(attendance)

### Inner Join
training_inner = pd.merge(registerations,attendance.drop("Name",axis=1),how="inner",on="Student_ID")
print(training_inner)

### Left vs Right Join
training_left = pd.merge(registerations,attendance.drop("Name",axis=1),how="left",on="Student_ID")
print(training_left)

training_right = pd.merge(registerations.drop("Name",axis=1),attendance,how="right",on="Student_ID")
print(training_right)

### Outer Join
training_outer = pd.merge(registerations,attendance,how="outer",on="Student_ID")
print(training_outer)

## How to Join by Index
registerations = registerations.set_index("Student_ID")
attendance = attendance.set_index("Student_ID")
print(registerations)
print(attendance)

training_inner = pd.merge(registerations,attendance,how="inner",on="Student_ID",suffixes=("_Reg","_Log"))
print(training_inner)