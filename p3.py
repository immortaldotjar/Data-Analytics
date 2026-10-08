import numpy as np

n = int(input("Enter number of elements: "))

ele = []

for i in range(n):
    num = float(input(f"Enter element {i+1}: "))
    ele.append(num)

arr = np.array(ele)

mean = np.mean(arr)
median = np.median(arr)
stdDvt = np.std(arr)
var = np.var(arr)

print(f"\nEntered Array: {arr} \nMean : {mean}\nMedian : {median} \nStandard Deviation : {stdDvt}\nVariance : {var}")
