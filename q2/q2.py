punctuations = """!()'"-[]{};:\,<>./?@#$%^&*_~"""

def string_it(s): # Defining the function
    t=""
    for i in range(0,len(s)):
        c=0
        for j in range(0,len(punctuations)):
            if s[i]==punctuations[j]:
                c=c+1
        if c==0:
            t=t+s[i]             
    return t

s="Hello in 36-650, & other MSP courses."
string_it(s) # Calling the function