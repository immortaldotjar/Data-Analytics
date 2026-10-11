# Write a Program to read the data and perform normalization.

import numpy as np # importing numpy library

n = int(input("Enter number of Elements to enter in Array: ")) # taking input for the size of array 

arr = []

for i in range(n):
    num = float(input(f"Enter element {i+1}: ")) # input for values of array
    arr.append(num)

npArr = np.array(arr) # converts to numpy array

minVal = np.min(arr) # gets the minimum value of the array

maxVal = np.max(arr) # gets the maximum value of the array

norm = (arr - minVal) / (maxVal - minVal) # calculating normalization

print(f"Original Array : {npArr} \n")

print(f"Minimum Value : {minVal} \n Maximum Value : {maxVal} \n")

print(f"Normalization of Array : {norm}")