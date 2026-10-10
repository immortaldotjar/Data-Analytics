import pandas as pd

n = int(input("Enter number of Rows to Enter in DataFrame: "))

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

print(f"\nDataFrame : \n{df}")

sortDf = df.sort_values(by="ID")

print(f"\nDataFrame Sorted by ID :\n {sortDf}")