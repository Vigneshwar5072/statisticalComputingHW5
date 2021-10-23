
def unicode_rep(count1, count2, string1, string2):
    # For each character in input strings get unicode representation
    # and  increment counter in corresponding array
    for i in string1:
        count1[ord(i)] += 1
    for i in string2:
        count2[ord(i)] += 1

    return(count1, count2)



def is_edit(string1, string2):
    """Given two strings, return if they are one or zero edits away.
    Insert, remove or replace a character."""
    # If the absolute difference in length is more than one
    # return false
    string1_len = len(string1)
    string2_len = len(string2)
    if string1_len != string2_len and abs(string1_len - string2_len) > 1:
        return False
    # Initialize two arrays, each for each string
    count1 = [0] * MAX_CHARS
    count2 = [0] * MAX_CHARS
    # For each character in input strings get unicode representation
    # and  increment counter in corresponding array
    count1, count2 = unicode_rep(count1, count2, string1, string2)
    edit = 0
    # compare the arrays
    # If number of edits required is more than 2 return false
    # This will handle replacement when given words of the same length
    for i in range(MAX_CHARS):
        if count1[i] != count2[i]:
            edit += 1
        if edit > 2:
            return False
    # Return false if string1 is the same as string2 (No edit required) e.g pale, pale
    return(False if not edit else True)

MAX_CHARS = 256
print(is_edit('pale', 'bake'))

