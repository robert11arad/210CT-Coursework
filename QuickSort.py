def sort(intlist):
    less = []
    equal = []
    greater = []
    if len(intlist) > 1:
        pivot = intlist[0]#Selects a pivot.
        #Separates the values in the list comparing them with the pivot.
        for x in intlist:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        #After separating the values around the pivot, runs the function recursively on the 2 new lists, the smaller numbers and the bigger ones until they are all sorted.
        return sort(less)+equal+sort(greater)
    #Once it sorted all numbers and has as argument only one intenger it returns it all the way back to the first function.
    else:
        return intlist

intlist=input("Input the numbers separated by commas here: ")
intlist=intlist.split(",")
intlist = [int(x) for x in intlist]#Makes all numbers in the input list intengers if they are strings.
print(sort(intlist)[int(input("What's the possition of the element you'd like to find in the list? "))-1])#Asks user for the possition of the element he would like to find.
