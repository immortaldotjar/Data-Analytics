# Write a Program to calculate the mean, median, standard deviation, and variance using NumPy.

import numpy as np #importing numpy library

n = int(input("Enter number of elements: ")) 

ele = []

for i in range(n):
    num = float(input(f"Enter element {i+1}: "))
    ele.append(num)

arr = np.array(ele) #converts to numpy array

mean = np.mean(arr) #calculates mean of the values in list

median = np.median(arr) #calculates median of the values in list

stdDvt = np.std(arr) #calculates standard deviation of the values in list

var = np.var(arr) #calculates variance of the values in list

print(f"\nEntered Array: {arr} \nMean : {mean}\nMedian : {median} \nStandard Deviation : {stdDvt}\nVariance : {var}")
