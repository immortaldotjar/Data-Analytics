# Write a Program to create a 5x5 2D array for random numbers between 0 and 1 using NumPy.

import numpy as np #importing numpy library
import random  

rows = int(input("Enter number of rows : ")) #for total rows
cols = int(input("Enter number of columns : ")) #for total columns

arr = [] 

for i in range(rows):
    r = []
    for j in range(cols):
        rand = random.random()    
        r.append(rand)
    arr.append(r)

npArr = np.array(arr) #converting to numpy array

print(f"\n{rows}x{cols} 2D Array : \n {npArr}")

