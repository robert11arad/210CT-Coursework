def sort(intlist):
    less = []
    equal = []
    greater = []
    if len(intlist) > 1:
        pivot = intlist[0]
        for x in intlist:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return intlist

intlist=input("Input the numbers separated by commas here: ")
intlist=intlist.split(",")
intlist = [int(x) for x in intlist]
print(sort(intlist)[int(input("What's the possition of the element you'd like to find in the list? "))-1])
