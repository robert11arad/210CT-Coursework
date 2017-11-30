from copy import *

maxkg=10
cargo={"material1":["Copper", 7, 65], "material2":["Plastic",15,50], "material3":["Gold",4,100]}
order=list(cargo.keys())

def arange(arcubes, arorder):
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


def load(maxkg, cargo, order):
    matord = arange(cargo, order)
    lorry={}
    times=0

    for ma in matord:
        lorry[cargo[str(ma)][0]]=[0,cargo[str(ma)][2]]

    for inuse in range(len(matord)):
        while cargo[str(matord[inuse])][1]>0 and maxkg>0:
            maxkg-=1
            cargo[str(matord[inuse])][1]-=1
            lorry[str(cargo[str(matord[inuse])][0])][0]+=1
        if maxkg==0:
            break
        times+=1
    return [lorry,times]#{'Gold': [4, 100], 'Copper': [6, 65], 'Plastic': [0, 50]}

lorry = load(maxkg,cargo,order)[0]
times = load(maxkg,cargo,order)[1]
lorrylist = list(lorry.keys())
total = 0

print("The lorry is carrying:")

for tot in range(times):
    total+=lorry[str(lorrylist[tot])][0]*lorry[str(lorrylist[tot])][1]
    if tot == times-2:
        print(str(lorry[str(lorrylist[tot])][0])+"kg of",str(lorrylist[tot]),end=" and ")
    elif tot < times-1:
        print(str(lorry[str(lorrylist[tot])][0])+"kg of",str(lorrylist[tot]),end=", ")
    else:
        print(str(lorry[str(lorrylist[tot])][0])+"kg of",str(lorrylist[tot]),end="\n")

print("Load composition value = "+str(total))
