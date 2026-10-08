import numpy as np

mean = 110
stdDvt = 15
size = 50

ranArr = np.random.normal(mean, stdDvt, size)

print(f"Random Array of 50 Numbers :\n {ranArr} \n")

print(f"Mean : {np.mean(ranArr)}")
print(f"Standard Deviation : {np.std(ranArr)}")