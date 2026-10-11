import pandas as pd
import numpy as np

n = int(input("Enter number of Rows to Enter in DataFrame :"))

stuIds = []
names = []
ages = []
percentage = []

for i in range(n):
    stuId = input(f"Enter Id of student {i+1} : ")
    name = input(f"Enter Name of student {i+1} : ")
    age = input(f"Enter Age of student {i+1} : ")
    per = input(f"Enter Percentage of student {i+1} :")

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

df = pd.DataFrame(data)

print(f"DataFrame : \n{df}\n")

dropDups = df.drop_duplicates(subset=["ID"], keep="first")

print(f"Data frame After removing Redundant Rows According to ID :\n{dropDups}")