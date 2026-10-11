# Write a program to create a NumPy array and Access and manipulate elements in the array.

import numpy as np #importing nupmy library

npArr = np.array([]) #creating numpy array

menu = input("want to enter the menu (y/n) : ") #input for opening menu

while(menu == 'y'): #loop run when user enter yes

    arr = [] #for storing values
    
    def inputArr(): 
        global npArr #accessing numpy array
        
        n = int(input("Enter total number of values to be input in array : ")) # input for size of list
        i = 1

        while(i <= n):
            num = input(f"Enter any element for {i} : ") #input for taking values from user for the list
            arr.append(num) #adding value in list 
            i += 1

        npArr = np.array(arr)
        print(npArr) 
        return npArr

    def accessArr():
        global npArr #accessing numpy array
        
        #condition if user directly chooses accessing array before entering elements in array
        if len(npArr) == 0:
            npArr = inputArr()
        
        def accessIndex():
            index = int(input("Enter Index to assess Elements : "))
            print(f"{npArr[index]}")  # getting a specific indexed value

        def accessAllElems():
            for i,ele in enumerate(npArr):
                print(f"Element {ele} = Index {i}") #getting all indexs with values
                                
        ch = int(input("----Menu----\n1.Access First Elementof Array\n2.Access Last Element of Array\n3.Access other element by Indexing\n4.Access All elements with Index\n\n"))
        print(npArr)

        match ch:
            case 1:
                print(f"{npArr[0]}") #for first element of list
            case 2:
                print(f"{npArr[-1]}") #for last element of list
            case 3:
                accessIndex()
            case 4:
                accessAllElems()
            case _:
                print("Choose any option from menu!")
    
    def manipulateArr():
        global npArr #accessing numpy array
            
        if len(npArr) == 0:
            npArr = inputArr()
                
        ch = int(input("----Menu----\n1.Sum of Array\n2.Reverse the Array\n3.Shuffle the Array\n4.Sort the Array\n\n"))
        print(npArr)
        match ch:
            case 1:
                print(f"{np.sum(npArr.astype(int))}") #
            case 2:
                print(f"{np.flip(npArr)}")
            case 3:
                np.random.shuffle(npArr)
                print(f"{npArr}")
            case 4:
                print(f"{np.sort(npArr)}")
            case _:
                print("Choose any option from menu!")
            
            
    opt = int(input("----Menu----\n1.Enter Elements in Array\n2.Access the Elements of Array\n3.Manipulate the Elements of Array\n4.Exit\n"))

    match opt:
        case 1:
            inputArr() 
        case 2:
            accessArr()
        case 3:
            manipulateArr()
        case 4:
            break
        case _:
            print("select any option from the menu!")
        