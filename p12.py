# Write a Program to Reading a CSV File and reading with Specific Columns and rows.

import pandas as pd #importing pandas library

df = pd.read_csv("stuData.csv") # reading student data csv file and conveting is to dataframe

print(f"Dataframe : \n{df}") 

dfCols = pd.read_csv("stuData.csv",usecols=["ID" ,"Name" ,"Age"]) # reading student data csv file and conveting is to dataframe with specific columns

dfRows = pd.read_csv("stuData.csv",nrows=3) # reading student data csv file and conveting is to dataframe with specific rows

print(f"\nDataframe with Specific Columns : \n{dfCols}")

print(f"\nDataframe with First 3 Rows : \n{dfRows}")