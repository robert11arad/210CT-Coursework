from copy import *

#Working data
maxkg=10
cargo={"material1":["Copper", 7, 65], "material2":["Plastic",15,50], "material3":["Gold",4,100]}
order=list(cargo)

#Arranges the materials from the most valuable to the cheapest.
def arange(arcubes):
    arorder=list(arcubes)
    valors=[]
    for val in range(len(arorder)):
        valors.append(arcubes[str(arorder[val])][2])
    valor=sorted(valors,reverse=True)
    matord=copy(arorder)
    for e in range(len(valor)):
        for i in range(len(arorder)):
            if arcubes[str(arorder[i])][2] == valor[e]:
                matord[e]=str(arorder[i])
    return matord

#Loads the lorry 1 kg at a time, counting how much of each material has been placed
def load(maxkg, cargo):
    order=list(cargo)
    matord = arange(cargo)
    lorry={}
    times=0

    #Creates a dictionary of what the lorry is carrying.
    for ma in matord:
        lorry[cargo[str(ma)][0]]=[0,cargo[str(ma)][2]]

    #Loads the lorry 1 kg at a time until max capacity is reached.
    for inuse in range(len(matord)):
        while cargo[str(matord[inuse])][1]>0 and maxkg>0:
            maxkg-=1
            cargo[str(matord[inuse])][1]-=1
            lorry[str(cargo[str(matord[inuse])][0])][0]+=1
        if maxkg==0:#Stops loading the lorry once it reaches max capacity.
            break
        times+=1#Counts how many materials are on the lorry.
    return [lorry,times]

lorry = load(maxkg,cargo)[0]
times = load(maxkg,cargo)[1]
lorrylist = list(lorry.keys())
total = 0

#Prints out the solution.
print("The lorry can carry:")
for tot in range(times):
    total+=lorry[str(lorrylist[tot])][0]*lorry[str(lorrylist[tot])][1]
    if tot == times-2:
        print(str(lorry[str(lorrylist[tot])][0])+"kg of",str(lorrylist[tot]),end=" and ")
    elif tot < times-1:
        print(str(lorry[str(lorrylist[tot])][0])+"kg of",str(lorrylist[tot]),end=", ")
    else:
        print(str(lorry[str(lorrylist[tot])][0])+"kg of",str(lorrylist[tot]),end="\n")

print("Load composition value = "+str(total))
