import pandas as pd
import numpy as np

n = int(input("Enter number of Rows to Enter in DataFrame :"))

stuIds = []
names = []
ages = []
percentage = []

for i in range(n):
    stuId = input(f"Enter Id of student {i+1}: ")
    name = input(f"Enter Name of student {i+1}: ")
    age = int(input(f"Enter Age of student {i+1}: "))
    per = float(input(f"Enter Percentage of student {i+1}: "))
    
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

df = pd.DataFrame(data)

mean = df["Percentage"].mean()
stdDvt = df["Percentage"].std()

lowerLim = mean - 2 * stdDvt
upperLim = mean + 2 * stdDvt

print("Mean:", mean)
print("Standard Deviation : ", stdDvt)
print("Lower Limit:", lowerLim)
print("Upper Limit:", upperLim)

outliers = df[(df["Percentage"] < lowerLim) | (df["Percentage"] > upperLim)]
print(f"\nDetected Outliers :\n{outliers}")

newDf = df[(df["Percentage"] >= lowerLim) & (df["Percentage"] <= upperLim)]
print(f"\nDataFrame After Removing Outliers : \n{newDf}")