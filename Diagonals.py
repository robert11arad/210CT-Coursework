from math import *
from random import *

#Code to create a random matrix.
#Matrix=[]
#m=int(input("What size should the matrix be?"))
#for matrx in range(m):
#    Matrix.append([])
#    for matry in range(m):
#        Matrix[matrx].append(randint(1,9))

Matrix=[
[3, 1, 5, 6, 9],
[2, 4, 1, 9, 7],
[3, 5, 2, 8, 10],
[4, 2, 1, 6, 8],
[1, 4, 7, 9, 1]]

#Verifying user input.
n=0
while n==0 or n>len(Matrix) or n<0:
    n=int(input("How many elements does the smallest diagonal have? "))
    if n==0 or n>len(Matrix) or n<0:
        print("Wrong input, please try again.")

#Print Matrix.
for smth in Matrix:
    print(smth)

#Adds all intengers on a diagonal starting on the left or top side of the matrix.
def adder(matrix,i,j):
    lst=[]
    lst.append(matrix[i][j])
    if j==len(matrix)-1 or i==len(matrix)-1:
        return lst
    else:
        temp=adder(matrix,i+1,j+1)
        lst=lst+list(temp)
    return lst

#Finds all diagonals and saves them in a dictionary.
def diagonals(matrix,n):
    Diagonals={}
    for j in range(1,len(matrix)-n+1):
        i=0
        Diagonals["j"+str(j)]=adder(matrix,i,j)
    Diagonals["maindiagonal"]=adder(matrix,0,0)
    for i in range(1,len(matrix)-n+1):
        j=0
        Diagonals["i"+str(i)]=adder(matrix,i,j)
    return Diagonals

#Returns the common elements from two lists.
def common(a,b):
    return [y for y in a if y not in [x for x in a if x not in b]]

#Calculates all diagonals with at least n elements and then compare them to find the smallest.
Dict=diagonals(Matrix,n)
Dict2={}
Index=list(Dict)
highest=["a",inf]
for element in Index:
    Dict2[element]=sorted(Dict[element],reverse=True)[-n:]
    if sum(Dict2[element])<highest[1]:
        highest=[element,sum(Dict2[element])]


#Prints the solution.
print("\nThe smallest sum of numbers on a diagonal is",highest[1],"and is the sum of",end=" ")
for count, num in enumerate(common(Dict[highest[0]],Dict2[highest[0]])[-n:]):
    if count==n-1:
        print(" and",num,end=" ")
    elif count==0:
        print(num,end="")
    else:
        print(",",num,end="")
if highest[0]=="maindiagonal":
    print("on the main diagonal.")
else:
    print("on a parallel diagonal.")
