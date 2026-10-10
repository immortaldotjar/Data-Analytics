import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G"],
    "Marks": [50, 52, 49, 51, 500, 48, 47]  
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

mean = df["Marks"].mean()
std = df["Marks"].std()

lower_limit = mean - 2 * std
upper_limit = mean + 2 * std

print("\nMean:", mean)
print("Standard Deviation:", std)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

outliers = df[(df["Marks"] < lower_limit) | (df["Marks"] > upper_limit)]
print("\nDetected Outliers:")
print(outliers)

cleaned_df = df[(df["Marks"] >= lower_limit) & (df["Marks"] <= upper_limit)]
print("\nDataFrame After Removing Outliers:")
print(cleaned_df)