globals()["count"]=0#Keeping count of the current solution.

#Checks to see if a queen can be placed at the given possition.
def place(pos):
    for i in range(pos):
        if globals()["a"][i]==globals()["a"][pos] or abs(globals()["a"][i]-globals()["a"][pos])==abs(i-pos):
            return 0
    return 1

#Prints out a matrix based on the solution given.
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

#Checks for multiple solutions while backtracking.
def queen(n):
    k=1#starting at one so when the place() function checks the diagonals it doesn't get abs(a[i]-a[pos])==abs(i-pos)("0==0")
    #globals()["a"][k]=0
    while k!=0:
        globals()["a"][k]+=1#Starting at a[k]=1 for the place() function.
        #Keeps trying the next position if a queen can not be placed at the current one.
        while globals()["a"][k]<=n and place(k)==0:
            globals()["a"][k]+=1
        #Saves the progress and goes to place the next queen. Prints solution if no queen needs to be placed and backtracks to try other possible solutions.
        if globals()["a"][k]<=n:
            #Prints solution.
            if k==n:
                print_sol(n)
            #Moves on to the next queen.
            else:
                k+=1
                globals()["a"][k]=0
        #Backtracking.
        else:
            k-=1

n=int(input("Enter the number of Queens "))
globals()["a"]=[0]*(n+1)
queen(n)
print("Total solutions = ",globals()["count"])
