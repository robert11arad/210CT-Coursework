class Graph(object):
    def __init__(self):
        self.size=int(input("What dimensions would you like the matrix to be? "))
        self.matrix=[]
        #Creates a matrix of the size specified by the used.
        for i in range(self.size):
            self.matrix.append([])
            for j in range(self.size):
                self.matrix[i].append(0)

    #Asks the used to write the graph.
    def write_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                print("Enter the element in the position ["+str(i)+", "+str(j)+"] of the",end=" ")
                self.matrix[i][j]=input("matrix: ")

    #Prints out the graph.
    def read_matrix(self):
        print("The graph is:")
        for i in range(self.size):
            for j in range(self.size):
                print(self.matrix[i][j],end="\t")
            print("\n\n")

if __name__=="__main__":
    g=Graph()
    g.write_matrix()
    g.read_matrix()
