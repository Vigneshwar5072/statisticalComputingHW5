def triStars(n): # Defining the function
    l = n-1
    for i in range(0, n):
        for j in range(0, l):
            print(end=" ")
        l = l - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

triStars(6)# Calling the function