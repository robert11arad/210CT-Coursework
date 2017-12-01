import copy
from random import *

#Asks user to assigns a color to each number.
for colour in range(1,10):
    print("What colour should number", colour,end=" ")
    globals()["colour"+str(colour)]=input("be? ")

#Creates the matrix of random intengers from 1 to 9 of dimensions mxn.
matrix=[]
m=int(input("How many rows would you like? "))
n=int(input("and how many columns? "))
for l in range(m):
    matrix.append([])
    for k in range(n):
        matrix[l].append(randint(1,9))

#Finds out the lenght of connected elements.
def clenght(astada,i,j):
    matrix=copy.deepcopy(astada)
    lenght=0
    if matrix[i][j]==0:
        print("BPL")
    if len(matrix)-1>i>=1 and len(matrix[i])-1>j>=1:
        if matrix[i][j]==matrix[i+1][j] and matrix[i+1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i+1,j)+1
        elif matrix[i][j]==matrix[i-1][j] and matrix[i-1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i-1,j)+1
        elif matrix[i][j]==matrix[i][j+1] and matrix[i][j+1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j+1)+1
        elif matrix[i][j]==matrix[i][j-1] and matrix[i][j-1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j-1)+1
        else:
            lenght=1
    elif len(matrix)-1>i>=1 and j==0:
        if matrix[i][j]==matrix[i+1][j] and matrix[i+1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i+1,j)+1
        elif matrix[i][j]==matrix[i-1][j] and matrix[i-1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i-1,j)+1
        elif matrix[i][j]==matrix[i][j+1] and matrix[i][j+1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j+1)+1
        else:
            lenght=1
    elif i==0 and 1<=j<len(matrix[i])-1:
        if matrix[i][j]==matrix[i+1][j] and matrix[i+1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i+1,j)+1  
        elif matrix[i][j]==matrix[i][j+1] and matrix[i][j+1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j+1)+1
        elif matrix[i][j]==matrix[i][j-1] and matrix[i][j-1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j-1)+1
        else:
            lenght=1
    elif i==0 and j==0:
        if matrix[i][j]==matrix[i+1][j] and matrix[i+1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i+1,j)+1
        elif matrix[i][j]==matrix[i-1][j] and matrix[i-1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i-1,j)+1
        else:
            lenght=1
    elif i==0 and j==len(matrix[i])-1:
        if matrix[i][j]==matrix[i+1][j] and matrix[i+1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i+1,j)+1
        elif matrix[i][j]==matrix[i][j-1] and matrix[i][j-1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j-1)+1
        else:
            lenght=1
    elif i==len(matrix)-1 and j==0:
        if matrix[i][j]==matrix[i-1][j] and matrix[i-1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i-1,j)+1
        elif matrix[i][j]==matrix[i][j-1] and matrix[i][j-1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j-1)+1
        else:
            lenght=1
    elif i==len(matrix)-1 and 0<j<len(matrix[i])-1:
        if matrix[i][j]==matrix[i-1][j] and matrix[i-1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i-1,j)+1
        elif matrix[i][j]==matrix[i][j+1] and matrix[i][j+1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j+1)+1
        elif matrix[i][j]==matrix[i][j-1] and matrix[i][j-1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j-1)+1
        else:
            lenght=1
    elif 0<i<len(matrix)-1 and j==len(matrix[i])-1:
        if matrix[i][j]==matrix[i+1][j] and matrix[i+1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i+1,j)+1   
        elif matrix[i][j]==matrix[i-1][j] and matrix[i-1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i-1,j)+1
        elif matrix[i][j]==matrix[i][j-1] and matrix[i][j-1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j-1)+1
        else:
            lenght=1
    elif i==len(matrix)-1 and j==len(matrix[i])-1:
        if matrix[i][j]==matrix[i-1][j] and matrix[i-1][j]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i-1,j)+1
        elif matrix[i][j]==matrix[i][j-1] and matrix[i][j-1]!=0:
            matrix[i][j]=0
            lenght+= clenght(matrix,i,j-1)+1
        else:
            lenght=1
    return lenght

#Calculates the maximum lenght of connected colours starting from every point in the matrix and then saving them in a dictionary.
maxpath = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if clenght(matrix,i,j)>maxpath[str(matrix[i][j])]:
            maxpath[str(matrix[i][j])]=clenght(matrix,i,j)

highest = maxpath[str(max(maxpath, key=maxpath.get))]#Gets the highest value from the dictionary.

#Saves the entries from maxpath with the values as keys and the keys with the same value in a list under their previous value.
new_dict = {}
for pair in maxpath.items():
    if pair[1] not in new_dict.keys():
        new_dict[pair[1]] = []
    new_dict[pair[1]].append(pair[0])

#Prints the result.
if len(new_dict[highest])>1:
    print("The size of the biggest sets is",
      highest,"and the colours are",end=" ")
else:
    print("The size of the biggest set is",
      highest,"and the colour is",end=" ")
for elem in new_dict[highest]:
    if len(new_dict[highest])>1:
        if elem==new_dict[highest][-1] and len(new_dict[highest])>1:
            print(" and",globals()["colour"+elem],end=" ")
        elif new_dict[highest][-1]>elem>=new_dict[highest][1] and elem!=new_dict[highest][-1]:
            print(",",globals()["colour"+elem],end="")
        else:
            print(globals()["colour"+elem],end="")
    else:
        print(globals()["colour"+elem],end="")
print(".")
