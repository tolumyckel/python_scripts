import random

def bubbleSort(my_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                print("Swapped: {} with {}".format(my_list[i], my_list[i+1]))
                swapped = True
    return my_list

def getRandList():
    myList = []
    for x in range(100):
        myList.append(random.randint(1,2001))
    return myList

print("Random Numbers")
print(getRandList())
print(" ")
print("Sorted Numbers")
print(bubbleSort(getRandList()))
