# Write a program to detect the outliers and remove the rows having outliers.

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

mean = df["Percentage"].mean() # calculating mean of Percentage column
stdDvt = df["Percentage"].std() # calculating standard deviation of Percentage column

lowerLim = mean - 2 * stdDvt # finding lowerbound
upperLim = mean + 2 * stdDvt # finding upperbound

print("Mean:", mean)
print("Standard Deviation : ", stdDvt)
print("Lower Limit:", lowerLim)
print("Upper Limit:", upperLim)

outliers = df[(df["Percentage"] < lowerLim) | (df["Percentage"] > upperLim)] #finding outliers
print(f"\nDetected Outliers :\n{outliers}")

newDf = df[(df["Percentage"] >= lowerLim) & (df["Percentage"] <= upperLim)] # removing the outliers from dataframe
print(f"\nDataFrame After Removing Outliers : \n{newDf}")