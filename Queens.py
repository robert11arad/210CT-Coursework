globals()["count"]=0
globals()["a"]=[0]*30

def place(pos):
    for i in range(pos):
        if globals()["a"][i]==globals()["a"][pos] or abs(globals()["a"][i]-globals()["a"][pos])==abs(i-pos):
            return 0
    return 1

def print_sol(n):
    globals()["count"]+=1
    print("\n\nSolution #",globals()["count"])
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i]==j:
                print("Q",end="\t")
            else:
                print("*",end="\t")
        print("\n")

def queen(n):
    k=1
    globals()["a"][k]=0
    while k!=0:
        globals()["a"][k]+=1
        while globals()["a"][k]<=n and place(k)==False:
            globals()["a"][k]+=1
        if globals()["a"][k]<=n:
            if k==n:
                print_sol(n)
            else:
                k+=1
                globals()["a"][k]=0
        else:
            k-=1

n=int(input("Enter the number of Queens "))
queen(n)
print("Total solutions = ",globals()["count"])
