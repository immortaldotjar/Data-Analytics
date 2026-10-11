# Create a Program we use various functions in NumPy library to carry out the ANOVA test. 

import numpy as np

n = int(input("Enter number of groups: "))

groups = []

for i in range(n):
    values = list(map(float, input(f"Enter values for Group {i+1} (space separated): ").split()))
    groups.append(np.array(values))

# Number of observations
N = sum(len(group) for group in groups)

# Number of groups
k = len(groups)

# Grand Mean
grand_mean = np.mean(np.concatenate(groups))

# Sum of Squares Between Groups (SSB)
ssb = sum(len(group) * (np.mean(group) - grand_mean) ** 2 for group in groups)

# Sum of Squares Within Groups (SSW)
ssw = sum(np.sum((group - np.mean(group)) ** 2) for group in groups)

df_between = k - 1
df_within = N - k

ms_between = ssb / df_between
ms_within = ssw / df_within

f_value = ms_between / ms_within

print("Analyis of Varience")
print(f"Grand Mean : {grand_mean}")
print(f"SS Between Groups : {ssb}")
print(f"SS Within Groups : {ssw}")
print(f"MS Between Groups : {ms_between}")
print(f"MS Within Groups : {ms_within}")
print(f"F Statistic : {f_value}")