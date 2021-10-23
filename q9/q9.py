def palindrome(s): # Defining the function
    n=0
    if s[n]==s[n-1]:
        try:
            return True and palindrome(s[n+1:n-1])
        except:
            return True
    else:
        return False

s="kayak"
palindrome(s) # Calling the function

s="hello"
palindrome(s) # Calling the function