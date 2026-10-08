import numpy as np

n = int(input("Enter number of Element to enter in Array: "))

arr = []
for i in range(n):
    num = float(input(f"Enter element {i+1}: "))
    arr.append(num)

npArr = np.array(arr)

minVal = np.min(arr)
maxVal = np.max(arr)

norm = (arr - minVal) / (maxVal - minVal)

print(f"Original Array : {npArr} \n")

print(f"Minimum Value : {minVal} \n Maximum Value : {maxVal} \n")

print(f"Normalization of Array : {norm}")
