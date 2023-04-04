def searchString(arr,target):
    """
       search for a character in a string
    """

    #if array length equals zero
    if(len(arr) == 0):
        return False


    for i in range(len(arr)):
        if(arr[i] == target):
            return True
    
    return False

print(searchString("Wanjema","a"))