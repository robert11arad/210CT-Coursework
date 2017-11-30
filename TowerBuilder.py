from copy import *

cubes = {}
nrofcubes = int(input("How many cubes are you using? "))

for cub in range(1,nrofcubes+1):
    nr = int(input("What's cube"+str(cub)+"'s edge? "))
    color = str(input("and color? "))
    cubes["cube"+str(cub)]=[nr, color]

workingcubes = copy(cubes)
cubelist = list(cubes.keys())

def baza(cubes, cubelist, iter1=1, maxcube=0, cubenr=0):
    if iter1 <= len(cubes):
        cube = cubes[cubelist[iter1-1]]
        if cube[0] > maxcube:
            maxcube = cube[0]
            cubenr = iter1
        cubenr = baza(cubes, cubelist, iter1+1, maxcube, cubenr)
    return cubenr

def ordinea(workingcubes, cubelist, order = []):
    if len(workingcubes)>1:    
        selected=baza(workingcubes, cubelist)
        order.append(cubelist[selected-1])
        del workingcubes[cubelist[selected-1]]
        del cubelist[selected-1]
        order = ordinea(workingcubes, cubelist, order)
    else:
        order.append(cubelist[0])
    return order

def swap(lista, a, b):
    x=lista[a]
    y=lista[b]
    z=x
    lista[a]=lista[b]
    lista[b]=z
    return lista

def arange(arcubes, arorder):
    last = ""
    chn = False
    for i in range(len(arorder)):
        if last == arcubes[str(arorder[i])][1]:
            chn = True
        if last != arcubes[str(arorder[i])][1] and chn == True:
            arorder = swap(arorder, i, i-1)
            arorder = arange(arcubes, arorder)
        last = arcubes[str(arorder[i])][1]
    return arorder

def maxheight(mhcubes):
    tot = 0
    for i in range(len(cubes)):
        tot = tot + mhcubes["cube"+str(i+1)][0]
    return tot

order = arange(cubes,ordinea(workingcubes, cubelist))

print("The maximum height is", str(maxheight(cubes)))
for i in range(len(cubes)):
    i=i+1
    if str(i)[-1]==1 and i!=11:
        print("The", str(i)+"st cube is", order[i-1])
    elif str(i)[-1]==2 and i!=12:
        print("The", str(i)+"nd cube is", order[i-1])
    elif str(i)[-1]==3 and i!=13:
        print("The", str(i)+"rd cube is", order[i-1])
    else:
        print("The", str(i)+"th cube is", order[i-1])
