# Create a program to identify and count missing values in a data frame.

import pandas as pd #importing pandas library
import numpy as np  #importing numpy library

n = int(input("Enter number of Rows to Enter in DataFrame: ")) # input for total size of rows to be entered

stuIds = [] # holds ID of students
names = [] # hold names of students
ages = [] # holds ages of students
percentage = [] # holds percentage of students
 
for i in range(n):
    stuId = input(f"Enter Id of student {i+1}: ") # input for id
    name = input(f"Enter Name of student {i+1}: ") # input for name
    age = input(f"Enter Age of student {i+1}: ") # input for age
    per = input(f"Enter Percentage of student {i+1}: ") # input for percentage
    
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

print(f"DataFrame : \n{df}")

print(f"\nTotal missing values in each Columns : \n{df.isnull().sum()}") # printing sum of null values of each column

print(f"\nTotal missing values in the Dataframe : {df.isnull().sum().sum()}") #printing sum of null values in the whole dataframe