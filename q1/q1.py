def transpose_of_matrix(X): # Defining the function
    
    k=[]
    for j in range(0,len(X[0])):
        l=[]
        for i in range(0,len(X)):
            l.append(X[i][j])
        k.append(l)
    
    for m in range(0,len(k)):
        print(k[m])

X=[[10,8],[2,4],[1,7]]
transpose_of_matrix(X) # Calling the function