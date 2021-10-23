def triangle(n): # Defining the function
    a=0
    for i in range(1,n+1):
        l=[]
        for j in range(0,i):
            a=a+1
            l.append(a)
        print(*l)

triangle(3) # Calling the function