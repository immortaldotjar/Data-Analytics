# Write a program to sort the data frame based on the first column.

import pandas as pd # importing pandas library

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
    
    stuIds.append(stuId)
    names.append(name)
    ages.append(age)
    percentage.append(per)

data = {
    "ID": stuIds,
    "Name": names,
    "Age": ages,
    "Percentage": percentage
}

df = pd.DataFrame(data) # converting rows to pandas dataframe

print(f"DataFrame : \n{df}")

sortDf = df.sort_values(by="ID") # sorting the Rows in comparissonn with ID column

print(f"\nDataFrame Sorted by ID :\n {sortDf}")