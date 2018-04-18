import random

def quicksort(array):

    # We define our 3 arrays
    less = []
    equal = []
    greater = []

    # if the length of our array is greater than 1
    # we perform a sort
    if len(array) > 1:
        # Select our pivot. This doesn't have to be
        # the first element of our array
        pivot = array[0]
        
        # recursively go through every element
        # of the array passed in and sort appropriately 
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        
        # recursively call quicksort on gradually smaller and smaller
        # arrays until we have a sorted list.
        return quicksort(less)+equal+quicksort(greater) 
    
    else:  
        return array
    

def getRandList():
    myList = []
    for x in range(1000):
        myList.append(random.randint(1,2001))
    return myList

print("Random Numbers")
print(getRandList())
print(" ")
print("Sorted Numbers")
print (quicksort(getRandList()))
