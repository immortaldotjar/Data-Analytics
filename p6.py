import pandas as pd

n = int(input("Enter number of rows: "))

stuIds = []
names = []
ages = []
marks = []

for i in range(n):
    stuId = input(f"Enter Id of student {i+1}: ")
    name = input(f"Enter Name of student {i+1}: ")
    age = int(input(f"Enter Age of student {i+1}: "))
    mark = float(input(f"Enter Marks of student {i+1}: "))
    
    print("\n")
    
    stuIds.append(stuId)
    names.append(name)
    ages.append(age)
    marks.append(mark)

data = {
    "ID": stuIds,
    "Name": names,
    "Age": ages,
    "Marks": marks
}

df = pd.DataFrame(data)

print(f"\nDataFrame : \n{df}")

