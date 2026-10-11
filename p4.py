# Write a Program to generate a random array of 50 numbers having mean 110 and standard deviation 15.

import numpy as np #importing numpy library

mean = 110 #fixed mean
stdDvt = 15 #fixed standard deviation  
size = 50  

ranArr = np.random.normal(mean, stdDvt, size) #randomly generates Gaussian distribution array of size 50 from the given mean and standard deviation 

print(f"Random Array of 50 Numbers :\n {ranArr} \n") 

print(f"Mean : {np.mean(ranArr)}") #prints mean of the array
print(f"Standard Deviation : {np.std(ranArr)}") #prints standard deviation of array