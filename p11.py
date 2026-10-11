# Write a program to remove all duplicates from the first column.

import pandas as pd #importing pandas library
import numpy as np  #importing numpy library

n = int(input("Enter number of Rows to Enter in DataFrame: ")) # input for total size of rows to be entered

stuIds = [] # holds ID of students
names = [] # hold names of students
ages = [] # holds ages of students
percentage = [] # holds percentage of students
 
for i in range(n):
    stuId = int(input(f"Enter Id of student {i+1}: ")) # input for id
    name = input(f"Enter Name of student {i+1}: ") # input for name
    age = int(input(f"Enter Age of student {i+1}: ")) # input for age
    per = float(input(f"Enter Percentage of student {i+1}: ")) # input for percentage
    
    print("\n")
    
    stuIds.append( int(stuId) if stuId else np.nan )
    names.append( name if name else None )
    ages.append( int(age) if age else np.nan )
    percentage.append( float(per) if per else np.nan )

data = {
    "ID": stuIds,
    "Name": names,
    "Age": ages,
    "Percentage": percentage
}

df = pd.DataFrame(data) # converting rows to pandas dataframe

print(f"DataFrame : \n{df}\n")

dropDups = df.drop_duplicates(subset=["ID"], keep="first")  # removing duplicate rows from dataframe

print(f"Data frame After removing Redundant Rows According to ID :\n{dropDups}")