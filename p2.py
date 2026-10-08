import numpy as np
import random  

rows = int(input("Enter number of rows : ")) 
cols = int(input("Enter number of columns : ")) 

arr = []


for i in range(rows):
    r = []
    for j in range(cols):
        rand = random.random()   
        r.append(rand)
    arr.append(r)

npArr = np.array(arr)

print(f"\n{rows}x{cols} 2D Array : \n {npArr}")

