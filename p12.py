import pandas as pd

df = pd.read_csv("stuData.csv")

print(f"Dataframe : \n{df}")

dfCols = pd.read_csv("stuData.csv",usecols=["ID" ,"Name" ,"Age"])

dfRows = pd.read_csv("stuData.csv",nrows=3)

print(f"\nDataframe with Specific Columns : \n{dfCols}")

print(f"\nDataframe with First 3 Rows : \n{dfRows}")